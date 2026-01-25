#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
知识库 Rating 字段分析与规范化工具

功能:
1. 扫描所有 markdown 文件的 rating 字段
2. 识别数据质量问题（超出范围、null、格式不统一等）
3. 生成待改进笔记列表
4. 批量规范化 rating 字段
"""

import os
import re
import sys
from pathlib import Path
from collections import defaultdict
from datetime import datetime
import yaml

# 设置标准输出编码为 UTF-8
if sys.platform == "win32":
    import codecs
    sys.stdout = codecs.getwriter("utf-8")(sys.stdout.buffer, 'strict')
    sys.stderr = codecs.getwriter("utf-8")(sys.stderr.buffer, 'strict')


class RatingAnalyzer:
    """Rating 字段分析器"""

    def __init__(self, vault_root: str):
        self.vault_root = Path(vault_root)
        self.issues = defaultdict(list)
        self.stats = {
            "total_files": 0,
            "with_rating": 0,
            "without_rating": 0,
            "invalid_range": 0,
            "null_values": 0,
            "emoji_format": 0,
            "empty_values": 0,
        }

    def extract_rating_from_yaml(self, yaml_content: dict) -> tuple:
        """
        从 YAML 中提取 rating 值

        Returns:
            (rating_value, issue_type)
        """
        if "rating" not in yaml_content:
            return None, "missing"

        rating = yaml_content["rating"]

        # null 值
        if rating is None:
            return None, "null"

        # 空字符串
        if rating == "":
            return None, "empty"

        # emoji 格式
        if isinstance(rating, str) and "⭐" in rating:
            # 转换 emoji 到数字
            star_count = rating.count("⭐")
            return star_count, "emoji"

        # 数字值
        try:
            rating_num = float(rating)
            if rating_num < 1 or rating_num > 5:
                return rating_num, "out_of_range"
            return rating_num, "valid"
        except (ValueError, TypeError):
            return rating, "invalid_format"

    def scan_directory(self, directory: str, pattern: str = "**/*.md"):
        """扫描目录下的所有 markdown 文件"""
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

                self.analyze_file(md_file)

    def analyze_file(self, file_path: Path):
        """分析单个文件的 rating 字段"""
        self.stats["total_files"] += 1

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            # 提取 YAML frontmatter
            yaml_match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
            if not yaml_match:
                self.issues["no_yaml"].append(str(file_path.relative_to(self.vault_root)))
                return

            yaml_content = yaml.safe_load(yaml_match.group(1))
            if not yaml_content:
                self.issues["empty_yaml"].append(str(file_path.relative_to(self.vault_root)))
                return

            rating, issue_type = self.extract_rating_from_yaml(yaml_content)

            if issue_type == "missing":
                self.stats["without_rating"] += 1
                self.issues["missing_rating"].append(str(file_path.relative_to(self.vault_root)))
            elif issue_type == "null":
                self.stats["null_values"] += 1
                self.issues["null_values"].append(str(file_path.relative_to(self.vault_root)))
            elif issue_type == "empty":
                self.stats["empty_values"] += 1
                self.issues["empty_values"].append(str(file_path.relative_to(self.vault_root)))
            elif issue_type == "out_of_range":
                self.stats["invalid_range"] += 1
                self.issues["invalid_range"].append((str(file_path.relative_to(self.vault_root)), rating))
            elif issue_type == "emoji":
                self.stats["emoji_format"] += 1
                self.issues["emoji_format"].append((str(file_path.relative_to(self.vault_root)), rating))
            elif issue_type == "valid":
                self.stats["with_rating"] += 1
                if rating < 3:
                    self.issues["low_quality"].append((str(file_path.relative_to(self.vault_root)), rating))

        except Exception as e:
            self.issues["error"].append((str(file_path.relative_to(self.vault_root)), str(e)))

    def print_report(self):
        """打印分析报告"""
        print("=" * 80)
        print("📊 知识库 Rating 字段分析报告")
        print("=" * 80)
        print(f"扫描时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"扫描范围: 1.Projects, 2.Topics, 3.Resources")
        print()

        print("## 📈 总体统计")
        print("-" * 80)
        print(f"总文件数: {self.stats['total_files']}")
        print(f"有评分文件: {self.stats['with_rating']} ({self.stats['with_rating']/self.stats['total_files']*100:.1f}%)")
        print(f"无评分文件: {self.stats['without_rating']} ({self.stats['without_rating']/self.stats['total_files']*100:.1f}%)")
        print()

        print("## ❌ 数据质量问题")
        print("-" * 80)
        print(f"超出范围 (1-5): {self.stats['invalid_range']}")
        print(f"null 值: {self.stats['null_values']}")
        print(f"空值: {self.stats['empty_values']}")
        print(f"emoji 格式: {self.stats['emoji_format']}")
        print()

        if self.issues["invalid_range"]:
            print("## 🚨 超出范围的 Rating 值")
            print("-" * 80)
            for file_path, rating in self.issues["invalid_range"][:10]:
                print(f"  {file_path}: {rating}")
            if len(self.issues["invalid_range"]) > 10:
                print(f"  ... 还有 {len(self.issues['invalid_range']) - 10} 个文件")
            print()

        if self.issues["emoji_format"]:
            print("## ⭐ Emoji 格式的 Rating")
            print("-" * 80)
            for file_path, rating in self.issues["emoji_format"][:10]:
                print(f"  {file_path}: {rating}")
            if len(self.issues["emoji_format"]) > 10:
                print(f"  ... 还有 {len(self.issues['emoji_format']) - 10} 个文件")
            print()

        if self.issues["low_quality"]:
            print("## ⚠️ 低质量笔记 (rating < 3)")
            print("-" * 80)
            for file_path, rating in sorted(self.issues["low_quality"], key=lambda x: x[1])[:10]:
                print(f"  {file_path}: {rating}")
            if len(self.issues["low_quality"]) > 10:
                print(f"  ... 还有 {len(self.issues['low_quality']) - 10} 个文件")
            print()

        print("=" * 80)
        print("✅ 分析完成")
        print("=" * 80)


def main():
    """主函数"""
    # 获取脚本所在目录的父目录作为 vault 根目录
    # 脚本在: 5.Misc/Template/Scripts/content-quality/analyze_and_fix_ratings.py
    # 需要向上 3 层到: obsidianDoc/
    script_dir = Path(__file__).parent
    vault_root = script_dir.parent.parent.parent.parent

    print(f"知识库根目录: {vault_root}")
    print()

    analyzer = RatingAnalyzer(str(vault_root))
    analyzer.scan_directory(str(vault_root))
    analyzer.print_report()


if __name__ == "__main__":
    main()
