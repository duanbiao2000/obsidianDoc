#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
知识库笔记自动质量评分工具 V2

基于内容质量评估标准，自动为笔记打分 (1-5 分)
评分标准参考: Atlas/BASE/内容质量评估标准.md

V2 算法改进:
- 每个维度都有基础分 (1.0 分起步)
- 降低门槛，增加评分梯度
- 更合理的加分机制
- 评分分布更均匀
"""

import os
import re
import sys
from pathlib import Path
from datetime import datetime
from collections import Counter
import yaml

# 设置标准输出编码为 UTF-8
if sys.platform == "win32":
    import codecs
    sys.stdout = codecs.getwriter("utf-8")(sys.stdout.buffer, 'strict')
    sys.stderr = codecs.getwriter("utf-8")(sys.stderr.buffer, 'strict')


class NoteQualityRater:
    """笔记质量自动评分器 V2"""

    def __init__(self, vault_root: str, dry_run: bool = True):
        self.vault_root = Path(vault_root)
        self.dry_run = dry_run
        self.ratings = []

    def extract_yaml_frontmatter(self, content: str) -> dict:
        """提取 YAML frontmatter"""
        yaml_match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
        if not yaml_match:
            return {}

        try:
            yaml_data = yaml.safe_load(yaml_match.group(1))
            return yaml_data if yaml_data else {}
        except:
            # YAML 解析失败，使用简单的正则提取
            yaml_content = yaml_match.group(1)
            result = {}
            for line in yaml_content.split('\n'):
                if ':' in line:
                    key, value = line.split(':', 1)
                    result[key.strip()] = value.strip()
            return result

    def count_links(self, content: str) -> int:
        """统计内部链接数量"""
        wikilinks = len(re.findall(r'\[\[([^\]]+)\]\]', content))
        return wikilinks

    def count_headings(self, content: str) -> dict:
        """统计标题层级"""
        headings = Counter()
        for match in re.finditer(r'^(#{1,3})\s+(.+)$', content, re.MULTILINE):
            level = len(match.group(1))
            headings[level] += 1
        return dict(headings)

    def has_code_blocks(self, content: str) -> bool:
        """是否有代码块"""
        return bool(re.search(r'```', content))

    def has_tables(self, content: str) -> bool:
        """是否有表格"""
        return bool(re.search(r'\|.*\|', content))

    def has_callouts(self, content: str) -> bool:
        """是否有引用块"""
        return bool(re.search(r'^>\s*', content, re.MULTILINE))

    def count_words(self, content: str) -> int:
        """统计字数（粗略）"""
        # 移除 YAML frontmatter
        content = re.sub(r'^---\n.*?\n---', '', content, flags=re.DOTALL)
        # 统计中文字符和英文单词
        chinese_chars = len(re.findall(r'[\u4e00-\u9fff]', content))
        english_words = len(re.findall(r'\b[a-zA-Z]{3,}\b', content))
        return chinese_chars + english_words

    def calculate_quality_score(self, content: str, yaml_data: dict) -> float:
        """
        计算笔记质量评分 (1-5 分)

        V2 算法改进:
        - 每个维度都有基础分 (1.0 分起步)
        - 降低门槛，增加评分梯度
        - 更合理的加分机制
        """

        # 基础分：每个维度起步 1.0 分
        scores = {
            "clarity": 1.0,
            "structure": 1.0,
            "depth": 1.0,
            "maintainability": 1.0
        }

        word_count = self.count_words(content)

        # === 清晰度评分 (1-5 分，30%) ===
        # 检查是否有"核心概念"、"定义"等关键词
        clarity_keywords = ["定义", "概念", "是指", "所谓", "核心思想", "一句话", "简单来说"]
        if any(keyword in content for keyword in clarity_keywords):
            scores["clarity"] += 0.8

        # 检查字数（内容充实度）
        if word_count > 100:
            scores["clarity"] += 0.3
        if word_count > 300:
            scores["clarity"] += 0.3
        if word_count > 500:
            scores["clarity"] += 0.2

        # 检查是否有"总结"、"要点"等
        if any(keyword in content for keyword in ["总结", "要点", "关键", "核心", "总而言之", "综上"]):
            scores["clarity"] += 0.4

        # === 结构评分 (1-5 分，25%) ===
        # 统计标题层级
        headings = self.count_headings(content)
        h2_count = headings.get(2, 0)
        h3_count = headings.get(3, 0)

        if h2_count >= 1:
            scores["structure"] += 0.5
        if h2_count >= 3:
            scores["structure"] += 0.5
        if h2_count >= 5:
            scores["structure"] += 0.3
        if h3_count >= 3:
            scores["structure"] += 0.2

        # 统计内部链接
        link_count = self.count_links(content)
        if link_count >= 1:
            scores["structure"] += 0.5
        if link_count >= 3:
            scores["structure"] += 0.5
        if link_count >= 5:
            scores["structure"] += 0.3
        if link_count >= 10:
            scores["structure"] += 0.2

        # 检查格式化元素
        format_count = 0
        if self.has_code_blocks(content):
            format_count += 1
        if self.has_tables(content):
            format_count += 1
        if self.has_callouts(content):
            format_count += 1
        if re.search(r'^\s*[-*+]\s+', content, re.MULTILINE):
            format_count += 1

        if format_count >= 1:
            scores["structure"] += 0.2
        if format_count >= 2:
            scores["structure"] += 0.2
        if format_count >= 3:
            scores["structure"] += 0.1

        # === 深度评分 (1-5 分，25%) ===
        # 检查是否有"背景"、"为什么"、"原因"等
        depth_keywords = ["背景", "为什么", "原因", "动机", "目的", "目标", "初衷", "来源"]
        if any(keyword in content for keyword in depth_keywords):
            scores["depth"] += 0.8

        # 检查是否有"例如"、"比如"、"案例"等
        example_keywords = ["例如", "比如", "案例", "示例", "例子", "实践", "具体来说"]
        if any(keyword in content for keyword in example_keywords):
            scores["depth"] += 0.8

        # 检查是否有"反思"、"思考"等
        reflection_keywords = ["反思", "思考", "心得", "体会", "理解", "看法", "观点", "我认为"]
        if any(keyword in content for keyword in reflection_keywords):
            scores["depth"] += 0.6

        # 检查字数（深度内容通常字数较多）
        if word_count > 200:
            scores["depth"] += 0.3
        if word_count > 500:
            scores["depth"] += 0.2

        # === 可维护性评分 (1-5 分，20%) ===
        # 检查 YAML 完整性
        yaml_fields = ["tags", "created", "update"]
        yaml_score = 0
        for field in yaml_fields:
            if field in yaml_data and yaml_data.get(field) not in [None, "null", "", "None"]:
                yaml_score += 1

        if yaml_score >= 1:
            scores["maintainability"] += 0.4
        if yaml_score >= 2:
            scores["maintainability"] += 0.4
        if yaml_score == 3:
            scores["maintainability"] += 0.2

        # 检查标签规范
        if "tags" in yaml_data:
            tags = yaml_data.get("tags", [])
            # 检查是否有 Domain/Status/Type 三层标签
            if isinstance(tags, list):
                has_domain = any("Domain/" in str(tag) for tag in tags)
                has_status = any("Status/" in str(tag) for tag in tags)
                has_type = any("Type/" in str(tag) for tag in tags)

                tag_count = sum([has_domain, has_status, has_type])
                if tag_count >= 1:
                    scores["maintainability"] += 0.3
                if tag_count >= 2:
                    scores["maintainability"] += 0.3
                if tag_count == 3:
                    scores["maintainability"] += 0.2

        # 确保每个维度不超过 5 分
        for key in scores:
            scores[key] = min(5.0, scores[key])

        # === 计算总分 ===
        total_score = (
            scores["clarity"] * 0.3 +
            scores["structure"] * 0.25 +
            scores["depth"] * 0.25 +
            scores["maintainability"] * 0.2
        )

        # 四舍五入到 0.5 的倍数（即 1.0, 1.5, 2.0, 2.5, 3.0...）
        total_score = round(total_score * 2) / 2

        # 确保在 1-5 范围内
        return max(1.0, min(5.0, total_score))

    def rate_file(self, file_path: Path):
        """为单个文件评分"""
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            # 提取 YAML
            yaml_data = self.extract_yaml_frontmatter(content)

            # 检查是否已经有有效评分
            current_rating = yaml_data.get("rating")
            if current_rating not in [None, "null", "", "None"]:
                # 已有评分，跳过
                return

            # 计算评分
            score = self.calculate_quality_score(content, yaml_data)

            # 获取文件信息
            word_count = self.count_words(content)
            link_count = self.count_links(content)

            self.ratings.append({
                "file": str(file_path.relative_to(self.vault_root)),
                "score": score,
                "word_count": word_count,
                "link_count": link_count,
                "has_yaml": bool(yaml_data),
                "tags": yaml_data.get("tags", "N/A")
            })

            # 添加评分到文件
            yaml_match = re.match(r"^(---\n.*?)\n(---)", content, re.DOTALL)

            if yaml_match:
                yaml_content = yaml_match.group(1)

                # 解析 YAML
                try:
                    yaml_dict = yaml.safe_load(yaml_content) or {}
                except:
                    yaml_dict = {}

                # 更新或添加 rating
                yaml_dict["rating"] = score

                # 重新生成 YAML
                new_yaml = yaml.dump(yaml_dict, allow_unicode=True, default_flow_style=False)
                new_yaml = "---\n" + new_yaml + "---"

                new_content = new_yaml.join(content.split(yaml_match.group(0)))

                if self.dry_run:
                    print(f"[DRY RUN] Would rate: {file_path.relative_to(self.vault_root)} → {score}")
                else:
                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write(new_content)
                    print(f"[RATED] {file_path.relative_to(self.vault_root)} → {score}")

        except Exception as e:
            print(f"[ERROR] {file_path.relative_to(self.vault_root)}: {e}")

    def scan_and_rate(self):
        """扫描并评分目录下的所有 markdown 文件"""
        target_dirs = [
            self.vault_root / "1.Projects",
            self.vault_root / "2.Topics",
            self.vault_root / "3.Resources",
        ]

        for target_dir in target_dirs:
            if not target_dir.exists():
                continue

            for md_file in target_dir.rglob("*.md"):
                # 跳过索引文件
                if md_file.name.startswith("_Index"):
                    continue
                # 跳过隐藏文件
                if md_file.name.startswith("."):
                    continue

                self.rate_file(md_file)

    def print_report(self):
        """打印评分报告"""
        print("\n" + "=" * 80)
        print("📊 笔记质量评分报告 (V2 算法)")
        print("=" * 80)
        print(f"模式: {'DRY RUN (预览)' if self.dry_run else 'LIVE (实际执行)'}")
        print(f"评分数: {len(self.ratings)}")
        print()

        if not self.ratings:
            print("✅ 没有需要评分的文件")
            return

        # 统计分布
        score_distribution = Counter()
        for rating in self.ratings:
            score_range = int(rating["score"])
            score_distribution[score_range] += 1

        print("## 📈 评分分布")
        print("-" * 80)
        for score in sorted(score_distribution.keys(), reverse=True):
            count = score_distribution[score]
            bar = "█" * int(count / 5)
            percentage = count / len(self.ratings) * 100
            print(f"  {score} 分: {count:3d} 个 ({percentage:5.1f}%) {bar}")
        print()

        # 平均分
        avg_score = sum(r["score"] for r in self.ratings) / len(self.ratings)
        print(f"## 📊 平均分: {avg_score:.2f}")
        print()

        # 低质量笔记
        low_quality = [r for r in self.ratings if r["score"] < 3.0]
        if low_quality:
            print("## ⚠️ 低质量笔记 (< 3.0 分)")
            print("-" * 80)
            for rating in sorted(low_quality, key=lambda x: x["score"])[:15]:
                print(f"  {rating['file']}: {rating['score']}")
                print(f"    字数: {rating['word_count']}, 链接: {rating['link_count']}")
            if len(low_quality) > 15:
                print(f"  ... 还有 {len(low_quality) - 15} 个文件")
            print()

        # 优秀笔记
        excellent = [r for r in self.ratings if r["score"] >= 4.0]
        if excellent:
            print("## 🌟 优秀笔记 (≥ 4.0 分)")
            print("-" * 80)
            for rating in sorted(excellent, key=lambda x: x["score"], reverse=True)[:10]:
                print(f"  {rating['file']}: {rating['score']}")
                print(f"    字数: {rating['word_count']}, 链接: {rating['link_count']}")
            if len(excellent) > 10:
                print(f"  ... 还有 {len(excellent) - 10} 个文件")
            print()

        print("=" * 80)
        if not self.dry_run:
            print("✅ 评分完成")
        else:
            print("⚠️  这是 DRY RUN 模式，没有实际修改文件")
            print("💡 如需实际执行，请使用: python auto_rate_notes_v2.py --execute")
        print("=" * 80)


def main():
    """主函数"""
    import argparse

    parser = argparse.ArgumentParser(description="自动为笔记打分 (V2 算法)")
    parser.add_argument("--execute", action="store_true", help="实际执行评分（默认为 dry run）")
    args = parser.parse_args()

    # 获取脚本所在目录的父目录作为 vault 根目录
    # 脚本在: 5.Misc/Template/Scripts/content-quality/auto_rate_notes_v2.py
    # 需要向上 3 层到: obsidianDoc/
    script_dir = Path(__file__).parent
    vault_root = script_dir.parent.parent.parent.parent

    print(f"知识库根目录: {vault_root}")
    print(f"算法: V2 (基础分 1.0 + 梯度加分)")
    print()

    rater = NoteQualityRater(str(vault_root), dry_run=not args.execute)
    rater.scan_and_rate()
    rater.print_report()


if __name__ == "__main__":
    main()
