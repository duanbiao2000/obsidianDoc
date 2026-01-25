#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
批量添加 Domain 标签脚本 (重构版)

功能：为Markdown文件批量添加Domain/Type/Status标签
使用统一的TagManager插件，减少代码重复
作者：Claude Code
日期：2026-01-25
使用方法：python batch_add_domain_tags.py
相关：Issue #4 - 自动化脚本体系优化
"""

import argparse
from pathlib import Path

# 导入新的核心库
import sys
sys.path.insert(0, str(Path(__file__).parent.parent))

from obsidian_scripts.core.encoding import auto_setup
from obsidian_scripts.plugins.tags import TagManager

# 自动设置UTF-8编码
auto_setup()


def main():
    """主函数"""
    parser = argparse.ArgumentParser(
        description="批量添加Domain/Type/Status标签",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='预览模式（不实际修改文件）'
    )

    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='显示详细信息'
    )

    args = parser.parse_args()

    # 创建标签管理器
    tag_manager = TagManager()

    print("=" * 60)
    print("批量添加 Domain 标签")
    print("=" * 60)

    if args.dry_run:
        print("🔍 预览模式（不会实际修改文件）")
        print()

    # 执行批量添加
    stats = tag_manager.add_domain_tags(
        dry_run=args.dry_run,
        verbose=args.verbose
    )

    # 输出统计信息
    print()
    print("=" * 60)
    print("✅ 处理完成！")
    print("=" * 60)
    print(f"成功: {stats['processed']} 个文件")
    print(f"跳过: {stats['skipped']} 个文件")
    print(f"失败: {stats['failed']} 个文件")

    if args.dry_run:
        print()
        print("💡 这是预览模式，实际修改请移除 --dry-run 参数")


if __name__ == "__main__":
    main()
