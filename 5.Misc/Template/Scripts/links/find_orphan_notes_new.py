#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
孤立笔记检测脚本 (重构版)

功能：扫描所有Markdown文件，识别孤立笔记（链接数<=threshold）
使用统一的LinkAnalyzer插件，减少代码重复
作者：Claude Code
日期：2026-01-25
使用方法：python find_orphan_notes.py
相关：Issue #4 - 自动化脚本体系优化
"""

import argparse
from pathlib import Path
from datetime import datetime

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
        description="查找孤立笔记",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument(
        '--threshold',
        type=int,
        default=0,
        help='链接阈值（默认：0）'
    )

    parser.add_argument(
        '--output',
        type=str,
        help='输出报告文件路径（可选）'
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
    print("孤立笔记检测")
    print("=" * 60)
    print(f"阈值: 链接数 <= {args.threshold}")
    print()

    # 执行检测
    output_file = Path(args.output) if args.output else None
    orphans = analyzer.find_orphan_notes(
        link_threshold=args.threshold,
        output_file=output_file
    )

    # 输出统计信息
    print()
    print("=" * 60)
    print("✅ 检测完成！")
    print("=" * 60)
    print(f"找到 {len(orphans)} 个孤立笔记")

    if args.verbose and orphans:
        print()
        print("前 10 个孤立笔记：")
        for i, orphan in enumerate(orphans[:10], 1):
            relative_path = orphan.filepath.relative_to(analyzer.config.vault_root)
            print(f"{i}. {relative_path} ({orphan.total_links} 链接)")

    if output_file:
        print()
        print(f"📄 报告已保存到: {output_file}")


if __name__ == "__main__":
    main()
