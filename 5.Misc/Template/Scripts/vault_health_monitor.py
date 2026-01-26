#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
知识库健康监控脚本

功能：综合检查知识库健康度，生成每日健康报告
作者：Claude Sonnet 4.5
日期：2026-01-26
使用方法：python vault_health_monitor.py
相关：知识库优化线路图 P1-索引健康监控自动化
"""

import argparse
import sys
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Tuple
import re

# 导入核心库
sys.path.insert(0, str(Path(__file__).parent))
from obsidian_scripts.core.encoding import auto_setup
from obsidian_scripts.core.config import Config
from obsidian_scripts.core.frontmatter import parse_frontmatter
from obsidian_scripts.core.markdown import extract_links
from obsidian_scripts.plugins.links import LinkAnalyzer

# 自动设置UTF-8编码
auto_setup()


class VaultHealthMonitor:
    """知识库健康监控器"""

    def __init__(self):
        self.config = Config()
        self.link_analyzer = LinkAnalyzer()
        self.health_scores = {}

    def check_orphan_notes(self) -> Dict:
        """检查孤立笔记（链接数 < 2）"""
        print("🔍 检查孤立笔记...")
        orphans = self.link_analyzer.find_orphan_notes(link_threshold=1)

        total_files = len(self.link_analyzer.get_all_markdown_files())
        orphan_count = len(orphans)
        orphan_rate = (orphan_count / total_files * 100) if total_files > 0 else 0

        return {
            "status": "critical"
            if orphan_rate > 10
            else "warning"
            if orphan_rate > 5
            else "good",
            "total_files": total_files,
            "orphan_count": orphan_count,
            "orphan_rate": orphan_rate,
            "orphans": orphans[:20],  # 只保留前20个用于报告
        }

    def check_index_coverage(self) -> Dict:
        """检查索引覆盖率"""
        print("📁 检查索引覆盖率...")
        all_files = self.link_analyzer.get_all_markdown_files()
        index_files = []

        # 查找所有索引文件
        for file in all_files:
            if file.name.startswith("_Index_of_") or file.name.endswith("MOC.md"):
                index_files.append(file)

        # 按目录分类
        directories = {}
        for file in all_files:
            parent = file.parent.relative_to(self.config.vault_root)
            if str(parent).startswith("."):
                continue  # 跳过隐藏目录
            parent_str = (
                str(parent).split("/")[0] if "/" in str(parent) else str(parent)
            )
            if parent_str not in directories:
                directories[parent_str] = 0
            directories[parent_str] += 1

        # 计算每个目录的索引覆盖率
        index_coverage = {}
        for dir_name, file_count in directories.items():
            dir_index_files = [f for f in index_files if dir_name in str(f)]
            has_index = 1 if dir_index_files else 0
            index_coverage[dir_name] = {
                "file_count": file_count,
                "has_index": has_index,
                "coverage": 100 if has_index else 0,
            }

        total_dirs = len(directories)
        indexed_dirs = sum(1 for v in index_coverage.values() if v["has_index"])
        coverage_rate = (indexed_dirs / total_dirs * 100) if total_dirs > 0 else 0

        return {
            "status": "critical"
            if coverage_rate < 50
            else "warning"
            if coverage_rate < 80
            else "good",
            "total_dirs": total_dirs,
            "indexed_dirs": indexed_dirs,
            "coverage_rate": coverage_rate,
            "details": index_coverage,
        }

    def check_tag_quality(self) -> Dict:
        """检查标签规范性"""
        print("🏷️ 检查标签规范性...")
        all_files = self.link_analyzer.get_all_markdown_files()

        issues = {"missing_tags": [], "invalid_format": [], "duplicate_tags": []}

        for file in all_files:
            try:
                frontmatter = parse_frontmatter(file)
                tags = frontmatter.get("tags", [])

                if not tags:
                    issues["missing_tags"].append(
                        file.relative_to(self.config.vault_root)
                    )
                    continue

                # 检查标签格式
                for tag in tags:
                    if isinstance(tag, str):
                        # 检查是否符合三层标签规范
                        if not re.match(r"^(Domain|Status|Type)/", tag):
                            issues["invalid_format"].append(
                                {
                                    "file": file.relative_to(self.config.vault_root),
                                    "tag": tag,
                                }
                            )

            except Exception as e:
                print(f"警告: 无法解析文件 {file}: {e}")

        total_files = len(all_files)
        files_with_issues = len(
            set(
                [f for f in issues["missing_tags"]]
                + [item["file"] for item in issues["invalid_format"]]
            )
        )

        issue_rate = (files_with_issues / total_files * 100) if total_files > 0 else 0

        return {
            "status": "critical"
            if issue_rate > 30
            else "warning"
            if issue_rate > 15
            else "good",
            "total_files": total_files,
            "missing_tags_count": len(issues["missing_tags"]),
            "invalid_format_count": len(issues["invalid_format"]),
            "issue_rate": issue_rate,
            "issues": {
                "missing_tags": issues["missing_tags"][:10],
                "invalid_format": issues["invalid_format"][:10],
            },
        }

    def calculate_overall_health(self, checks: Dict) -> Dict:
        """计算整体健康度"""
        # 每个检查的权重
        weights = {"orphan_notes": 0.4, "index_coverage": 0.3, "tag_quality": 0.3}

        # 将状态转换为分数
        status_scores = {"good": 100, "warning": 70, "critical": 40}

        total_score = 0
        details = {}

        for check_name, weight in weights.items():
            if check_name in checks:
                status = checks[check_name]["status"]
                score = status_scores[status]
                weighted_score = score * weight
                total_score += weighted_score
                details[check_name] = {
                    "status": status,
                    "score": score,
                    "weight": weight,
                    "weighted_score": weighted_score,
                }

        # 确定整体状态
        if total_score >= 85:
            overall_status = "excellent"
        elif total_score >= 75:
            overall_status = "good"
        elif total_score >= 60:
            overall_status = "warning"
        else:
            overall_status = "critical"

        return {
            "status": overall_status,
            "score": round(total_score, 1),
            "details": details,
        }

    def generate_daily_report(self, checks: Dict, health_score: Dict) -> str:
        """生成每日健康报告"""
        timestamp = datetime.now().strftime("%Y-%m-%d")
        report_lines = []

        # 报告头部
        report_lines.extend(
            [
                f"# 知识库健康日报 - {timestamp}",
                "",
                "> 自动生成的健康监控报告",
                "> 运行时间: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "",
                "---",
                "",
            ]
        )

        # 整体健康度
        overall_status_emoji = {
            "excellent": "✅",
            "good": "👍",
            "warning": "⚠️",
            "critical": "🚨",
        }[health_score["status"]]

        report_lines.extend(
            [
                "## 📊 整体健康度",
                "",
                f"**健康评分**: {health_score['score']}/100",
                f"**状态**: {overall_status_emoji} {health_score['status'].upper()}",
                "",
            ]
        )

        # 预警机制
        if health_score["score"] < 75:
            report_lines.extend(
                [
                    "### ⚠️ 健康度预警",
                    "",
                    f"当前健康度 ({health_score['score']}) 低于阈值 (75)，建议立即采取行动：",
                    "",
                    "- 检查孤立笔记清单",
                    "- 完善目录索引",
                    "- 修复标签格式问题",
                    "- 运行链接密度优化脚本",
                    "",
                ]
            )

        # 分项检查结果
        report_lines.extend(["## 📋 分项检查", ""])

        # 孤立笔记
        orphan_check = checks["orphan_notes"]
        orphan_emoji = {"good": "✅", "warning": "⚠️", "critical": "🚨"}[
            orphan_check["status"]
        ]

        report_lines.extend(
            [
                f"### 孤立笔记 {orphan_emoji}",
                "",
                f"- 总文件数: {orphan_check['total_files']}",
                f"- 孤立笔记数: {orphan_check['orphan_count']} ({orphan_check['orphan_rate']:.1f}%)",
                f"- 状态: {orphan_check['status'].upper()}",
                "",
            ]
        )

        if orphan_check["orphan_count"] > 0:
            report_lines.append("前 10 个孤立笔记:")
            for i, orphan in enumerate(orphan_check["orphans"][:10], 1):
                report_lines.append(
                    f"{i}. {orphan.filepath.relative_to(self.config.vault_root)}"
                )
            report_lines.append("")

        # 索引覆盖率
        index_check = checks["index_coverage"]
        index_emoji = {"good": "✅", "warning": "⚠️", "critical": "🚨"}[
            index_check["status"]
        ]

        report_lines.extend(
            [
                f"### 索引覆盖率 {index_emoji}",
                "",
                f"- 总目录数: {index_check['total_dirs']}",
                f"- 有索引目录: {index_check['indexed_dirs']}",
                f"- 覆盖率: {index_check['coverage_rate']:.1f}%",
                f"- 状态: {index_check['status'].upper()}",
                "",
            ]
        )

        # 标签质量
        tag_check = checks["tag_quality"]
        tag_emoji = {"good": "✅", "warning": "⚠️", "critical": "🚨"}[
            tag_check["status"]
        ]

        report_lines.extend(
            [
                f"### 标签质量 {tag_emoji}",
                "",
                f"- 总文件数: {tag_check['total_files']}",
                f"- 缺少标签: {tag_check['missing_tags_count']}",
                f"- 格式问题: {tag_check['invalid_format_count']}",
                f"- 问题率: {tag_check['issue_rate']:.1f}%",
                f"- 状态: {tag_check['status'].upper()}",
                "",
            ]
        )

        # 建议行动
        report_lines.extend(["## 🚀 建议行动", "", "### 立即处理 (P0)", ""])

        if health_score["status"] == "critical":
            report_lines.extend(
                [
                    "- [ ] 运行孤立笔记修复脚本: `python links/find_orphan_notes.py`",
                    "- [ ] 检查并创建缺失的索引文件",
                    "- [ ] 修复标签格式问题",
                    "",
                ]
            )
        elif health_score["status"] == "warning":
            report_lines.extend(
                [
                    "- [ ] 审查孤立笔记清单",
                    "- [ ] 完善目录索引",
                    "- [ ] 运行标签规范化脚本",
                    "",
                ]
            )

        report_lines.extend(
            [
                "### 定期维护 (P1)",
                "",
                "- [ ] 每周运行健康检查",
                "- [ ] 更新项目元数据",
                "- [ ] 归档过时内容",
                "- [ ] 检查链接有效性",
                "",
            ]
        )

        # 执行历史
        report_lines.extend(
            [
                "---",
                "",
                "## 📈 健康度趋势",
                "",
                "| 日期 | 评分 | 状态 |",
                "|------|------|------|",
                f"| {timestamp} | {health_score['score']} | {health_score['status'].upper()} |",
                "",
            ]
        )

        report_lines.extend(
            [
                "---",
                "",
                "**生成工具**: `vault_health_monitor.py`",
                "**查看完整报告**: [Atlas/Index/索引健康报告](../../Atlas/Index/索引健康报告.md)",
                "",
            ]
        )

        return "\n".join(report_lines)

    def save_daily_report(self, report: str) -> Path:
        """保存每日健康报告"""
        timestamp = datetime.now().strftime("%Y-%m-%d")
        filename = f"知识库健康日报_{timestamp}.md"
        output_path = self.config.vault_root / "0.DailyNotes" / filename

        # 确保目录存在
        output_path.parent.mkdir(parents=True, exist_ok=True)

        # 写入报告
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(report)

        return output_path


def main():
    """主函数"""
    parser = argparse.ArgumentParser(
        description="知识库健康监控",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    parser.add_argument(
        "--output", type=str, help="输出报告文件路径（可选，默认保存到 0.DailyNotes/）"
    )

    parser.add_argument(
        "--no-save", action="store_true", help="不保存报告，只输出到控制台"
    )

    parser.add_argument("--verbose", "-v", action="store_true", help="显示详细信息")

    args = parser.parse_args()

    # 创建健康监控器
    monitor = VaultHealthMonitor()

    print("=" * 60)
    print("知识库健康监控")
    print("=" * 60)
    print()

    # 执行各项检查
    checks = {
        "orphan_notes": monitor.check_orphan_notes(),
        "index_coverage": monitor.check_index_coverage(),
        "tag_quality": monitor.check_tag_quality(),
    }

    # 计算整体健康度
    health_score = monitor.calculate_overall_health(checks)

    # 生成报告
    report = monitor.generate_daily_report(checks, health_score)

    # 输出结果
    print()
    print("=" * 60)
    print("📊 健康度评估结果")
    print("=" * 60)
    print()
    print(f"整体评分: {health_score['score']}/100")
    print(f"健康状态: {health_score['status'].upper()}")

    if health_score["score"] < 75:
        print()
        print("⚠️ 健康度预警: 低于阈值 75，请查看报告中的建议行动")

    print()
    print("=" * 60)
    print("✅ 监控完成！")
    print("=" * 60)

    # 保存报告
    if not args.no_save:
        output_path = args.output if args.output else None
        if output_path:
            output_path = Path(output_path)

        saved_path = monitor.save_daily_report(report)
        print()
        print(f"📄 报告已保存到: {saved_path}")
    else:
        if args.verbose:
            print()
            print("--- 完整报告 ---")
            print(report)


if __name__ == "__main__":
    main()
