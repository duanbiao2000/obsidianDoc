#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
链接分析脚本 (重构版)

功能：分析笔记的链接密度和连通性
使用统一的LinkAnalyzer插件，减少代码重复
作者：Claude Code
日期：2026-01-25
使用方法：python link_analyzer.py
相关：Issue #4 - 自动化脚本体系优化
"""

import argparse
from pathlib import Path

# 导入新的核心库
import sys
sys.path.insert(0, str(Path(__file__).parent.parent))

from obsidian_scripts.core.encoding import auto_setup
from obsidian_scripts.plugins.links import LinkAnalyzer

# 自动设置UTF-8编码
auto_setup()


def main():
    """主函数"""
    parser = argparse.ArgumentParser(
        description="分析链接连通性",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument(
        '--stats',
        action='store_true',
        help='显示链接密度统计'
    )

    parser.add_argument(
        '--connectivity',
        action='store_true',
        help='分析链接连通性'
    )

    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='显示详细信息'
    )

    args = parser.parse_args()

    # 创建链接分析器
    analyzer = LinkAnalyzer()

    print("=" * 60)
    print("链接分析")
    print("=" * 60)
    print()

    # 显示链接密度统计
    if args.stats or not args.connectivity:
        print("=== 链接密度统计 ===")
        stats = analyzer.get_link_density_stats()
        print(f"总文件数: {stats['total_files']}")
        print(f"总链接数: {stats['total_links']}")
        print(f"平均链接数/文件: {stats['avg_links_per_file']}")
        print(f"孤立笔记 (0链接): {stats['orphan_count']}")
        print(f"低连通性 (1-2链接): {stats['low_connectivity_count']}")
        print(f"高连通性 (>2链接): {stats['high_connectivity_count']}")

    # 分析链接连通性
    if args.connectivity:
        print()
        print("=== 链接连通性分析 ===")
        connectivity = analyzer.analyze_connectivity()

        # 按 in_links 数量排序
        sorted_items = sorted(
            connectivity.items(),
            key=lambda x: len(x[1]['in_links']),
            reverse=True
        )

        if args.verbose:
            # 显示所有笔记的连通性
            for title, links in sorted_items[:20]:
                in_count = len(links['in_links'])
                out_count = len(links['out_links'])
                print(f"{title}: {in_count} ← → {out_count}")
        else:
            # 只显示前 10 个高连通性笔记
            print("前 10 个高连通性笔记：")
            for i, (title, links) in enumerate(sorted_items[:10], 1):
                in_count = len(links['in_links'])
                out_count = len(links['out_links'])
                print(f"{i}. {title}: {in_count} ← → {out_count}")

    print()
    print("=" * 60)
    print("✅ 分析完成！")
    print("=" * 60)


if __name__ == "__main__":
    main()
