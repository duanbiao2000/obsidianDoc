#!/usr/bin/env python3
"""
为项目文件补充 update 字段
"""

import os
import re
from datetime import datetime
from pathlib import Path


def add_update_field(file_path: str, dry_run: bool = False) -> bool:
    """
    为文件添加 update 字段

    Args:
        file_path: 文件路径
        dry_run: 是否为试运行（不实际修改文件）

    Returns:
        bool: 是否成功添加或已存在
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # 检查是否已有 update 字段
        if re.search(r'\nupdate:\s*\d{4}-\d{2}-\d{2}', content):
            print(f"[SKIP] Already has update field: {file_path}")
            return False

        # 匹配 YAML frontmatter
        yaml_pattern = r'^---\n(.*?)\n---'
        match = re.match(yaml_pattern, content, re.DOTALL)

        if not match:
            print(f"[ERROR] No YAML frontmatter found: {file_path}")
            return False

        yaml_end = match.end()
        yaml_content = match.group(1)

        # 在 frontmatter 末尾添加 update 字段
        today = datetime.now().strftime('%Y-%m-%d')

        # 检查是否有其他字段，决定是否换行
        if yaml_content.strip():
            new_yaml = yaml_content.rstrip() + f'\nupdate: {today}\n'
        else:
            new_yaml = f'update: {today}\n'

        # 替换原来的 YAML
        new_content = content[:yaml_end - len(yaml_content) - 4] + new_yaml + content[yaml_end - 4:]

        if dry_run:
            print(f"[DRY RUN] Would add update field to: {file_path}")
            print(f"[DRY RUN] New YAML:\n{new_yaml}")
            return True

        # 写入文件
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"[OK] Added update field to: {file_path}")
        return True

    except Exception as e:
        print(f"[ERROR] Failed to process {file_path}: {str(e)}")
        return False


def main():
    import sys

    # 设置 UTF-8 编码输出
    if sys.platform == 'win32':
        import codecs
        sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')

    # 需要添加 update 字段的文件列表
    files_to_update = [
        '1.Projects/AI知识IP打造/01.战略规划/AI知识IP打造OKR (Q3).md',
        '1.Projects/AI知识IP打造/01.战略规划/从目标设定到时间追踪.md',
        '1.Projects/AI知识IP打造/02.方法论与框架/通过Figma和Notion建立SOP内容工厂.md',
        '1.Projects/技术能力晋升/01.职业规划/IC 职级演进.md',
    ]

    # 转换为绝对路径
    base_dir = os.getcwd()
    files_abs = [os.path.join(base_dir, f.replace('/', os.sep)) for f in files_to_update]

    print(f"[START] Adding update field to {len(files_abs)} files...")
    print(f"[INFO] Base directory: {base_dir}")
    print()

    # 先试运行
    print("=" * 60)
    print("DRY RUN - Preview changes")
    print("=" * 60)
    for file_path in files_abs:
        if os.path.exists(file_path):
            add_update_field(file_path, dry_run=True)
            print()

    print("\n" + "=" * 60)
    print("EXECUTING - Applying changes")
    print("=" * 60)

    # 实际执行
    success_count = 0
    for file_path in files_abs:
        if os.path.exists(file_path):
            if add_update_field(file_path, dry_run=False):
                success_count += 1
        else:
            print(f"[ERROR] File not found: {file_path}")

    print()
    print(f"[DONE] Successfully added update field to {success_count}/{len(files_abs)} files")


if __name__ == '__main__':
    main()
