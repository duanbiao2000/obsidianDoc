#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
标签替换脚本 - 简化版
"""

import re
from pathlib import Path
from datetime import datetime

# 标签映射
MAPPINGS = {
    "#AI": "#Domain/AI",
    "#todo": "#Status/TODO",
    "#done": "#Status/Done",
    "#note": "#Type/Note",
    "#Project": "#Type/Project",
    "#MOC": "#Type/MOC",
    "#reference": "#Type/Reference",
    "#Domain/Cognition": "#Domain/Cognitive",
}

# 笔记目录
NOTE_DIRS = [
    "0.DailyNotes",
    "1.Projects",
    "2.Topics",
    "3.Resources",
    "4.Archives",
    "6.Calendar",
]

def replace_in_file(file_path):
    """替换单个文件中的标签"""
    try:
        content = file_path.read_text(encoding='utf-8')
        original = content

        for old_tag, new_tag in MAPPINGS.items():
            # 替换正文中的标签
            pattern = r'\b' + re.escape(old_tag) + r'\b'
            content = re.sub(pattern, new_tag, content)

        if content != original:
            # 备份原文件
            backup = file_path.with_suffix('.md.bak')
            if not backup.exists():
                file_path.rename(backup)

            # 写入新内容
            file_path.write_text(content, encoding='utf-8')
            return True

        return False

    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False

def main():
    """主函数"""
    total = 0
    modified = 0

    for directory in NOTE_DIRS:
        dir_path = Path(directory)
        if not dir_path.exists():
            continue

        for md_file in dir_path.rglob("*.md"):
            total += 1
            if replace_in_file(md_file):
                modified += 1
                print(f"Updated: {md_file}")

    print(f"\nTotal files: {total}")
    print(f"Modified files: {modified}")
    print(f"Rate: {modified/total*100:.1f}%")

if __name__ == "__main__":
    main()
