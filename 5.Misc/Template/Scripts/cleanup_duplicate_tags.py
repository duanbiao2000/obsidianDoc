#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
清理重复标签脚本
修复 batch_add_domain_tags.py 造成的标签重复问题
"""

import re
import sys
from pathlib import Path
from datetime import datetime

# Windows 编码支持
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

# 笔记目录
NOTE_DIRS = [
    "0.DailyNotes",
    "1.Projects",
    "2.Topics",
    "3.Resources",
    "4.Archives",
    "6.Calendar",
]

def cleanup_duplicate_tags(file_path, dry_run=True):
    """
    清理文件中的重复标签

    Args:
        file_path: 文件路径
        dry_run: 是否为预览模式

    Returns:
        (是否修改, 统计信息)
    """
    try:
        content = file_path.read_text(encoding='utf-8')
        original_content = content

        # 查找 YAML tags 部分
        tags_match = re.search(r'^tags:\s*\n((?:[ \t]+-.+\n?)+)', content, re.MULTILINE)

        if not tags_match:
            return False, {}

        tags_text = tags_match.group(1)
        tags_start = tags_match.start(1)
        tags_end = tags_match.end(1)

        # 提取所有标签
        tags = re.findall(r'^[ \t]+-+(.+)$', tags_text, re.MULTILINE)

        if len(tags) <= 1:
            return False, {}

        # 去重并保持顺序
        seen = set()
        unique_tags = []
        for tag in tags:
            tag = tag.strip()
            if tag not in seen:
                seen.add(tag)
                unique_tags.append(tag)

        # 如果没有重复，返回
        if len(unique_tags) == len(tags):
            return False, {}

        # 生成新的 tags 文本
        indent = '  '
        new_tags_text = '\n'.join([f"{indent}- {tag}" for tag in unique_tags]) + '\n'

        # 替换内容
        new_content = content[:tags_start] + new_tags_text + content[tags_end:]

        # 统计信息
        stats = {
            'total_tags': len(tags),
            'unique_tags': len(unique_tags),
            'duplicates_removed': len(tags) - len(unique_tags),
            'tags_list': unique_tags
        }

        if not dry_run:
            # 创建备份
            backup_path = file_path.with_suffix('.md.dup_bak')
            if not backup_path.exists():
                file_path.rename(backup_path)

            # 写入新内容
            file_path.write_text(new_content, encoding='utf-8')

        return True, stats

    except Exception as e:
        print(f"错误处理 {file_path}: {e}")
        return False, {'error': str(e)}

def main():
    import argparse

    parser = argparse.ArgumentParser(
        description="清理重复标签",
        formatter_class=argparse.RawDescriptionHelpFormatter
 )

    parser.add_argument('--dry-run', action='store_true', help='预览模式（不修改文件）')
    parser.add_argument('--verbose', '-v', action='store_true', help='显示详细信息')

    args = parser.parse_args()

    repo_root = Path(r"d:\迅雷下载\@同步文件\OneDrive\obsidianDoc")

    print("=" * 70)
    print("标签重复清理工具")
    print("=" * 70)
    print(f"模式: {'预览（不修改文件）' if args.dry_run else '执行模式（将修改文件）'}")
    print(f"工作目录: {repo_root}")
    print("=" * 70)
    print()

    total_files = 0
    modified_files = 0
    total_duplicates = 0
    errors = []

    for directory in NOTE_DIRS:
        dir_path = repo_root / directory
        if not dir_path.exists():
            continue

        print(f"扫描目录: {directory}")

        for md_file in dir_path.rglob("*.md"):
            total_files += 1

            modified, stats = cleanup_duplicate_tags(md_file, dry_run=args.dry_run)

            if modified and 'error' not in stats:
                modified_files += 1
                duplicates = stats['duplicates_removed']
                total_duplicates += duplicates

                if args.verbose:
                    print(f"  ✓ {md_file.relative_to(repo_root)}")
                    print(f"    总标签: {stats['total_tags']}, 唯一: {stats['unique_tags']}, 清理: {duplicates}")

            elif 'error' in stats:
                errors.append({'file': str(md_file), 'error': stats['error']})

    print()
    print("=" * 70)
    print("清理统计:")
    print("-" * 70)
    print(f"扫描文件: {total_files}")
    print(f"需要清理: {modified_files}")
    print(f"总重复次数: {total_duplicates}")
    print(f"清理率: {total_duplicates}/{total_files} = {total_duplicates/total_files*100:.1f} 次/文件")

    if errors:
        print(f"错误: {len(errors)}")

    print("=" * 70)

    if not args.dry_run:
        print()
        print("✅ 清理完成！")
        print("💡 提示: 备份文件使用 .dup_bak 后缀")
        print("💡 确认无误后可删除备份文件")
    else:
        print()
        print("⚠️  预览模式完成，未修改任何文件")
        print("💡 提示: 使用不带 --dry-run 的参数执行实际清理")

if __name__ == "__main__":
    main()
