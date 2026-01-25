#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
知识库 Rating 字段规范化工具

功能:
1. 将超出范围的 rating 值转换为 1-5 范围
2. 移除 null 值的 rating 字段
3. 备份修改前的文件
"""

import os
import re
import sys
from pathlib import Path
from datetime import datetime
import shutil

# 设置标准输出编码为 UTF-8
if sys.platform == "win32":
    import codecs
    sys.stdout = codecs.getwriter("utf-8")(sys.stdout.buffer, 'strict')
    sys.stderr = codecs.getwriter("utf-8")(sys.stderr.buffer, 'strict')


class RatingFixer:
    """Rating 字段规范化工具"""

    def __init__(self, vault_root: str, dry_run: bool = True):
        self.vault_root = Path(vault_root)
        self.dry_run = dry_run
        self.changes = []
        self.backup_dir = self.vault_root / "4.Archives" / "Backups" / f"rating_fix_{datetime.now().strftime('%Y%m%d_%H%M%S')}"

    def convert_rating_10_to_5(self, rating_10: float) -> float:
        """将 10 分制转换为 5 分制"""
        rating_5 = round(rating_10 / 2, 1)
        # 确保在 1-5 范围内
        return max(1.0, min(5.0, rating_5))

    def fix_file(self, file_path: Path):
        """修复单个文件的 rating 字段"""
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            # 提取 YAML frontmatter
            yaml_match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
            if not yaml_match:
                return

            yaml_content = yaml_match.group(1)
            new_yaml = yaml_content
            modified = False

            # 检查 rating 字段
            rating_match = re.search(r'^rating:\s*(.+?)\s*$', yaml_content, re.MULTILINE)

            if rating_match:
                rating_value = rating_match.group(1).strip()
                new_rating_value = None

                # 处理 null 值
                if rating_value.lower() in ["null", "none", "~", "''", '""']:
                    new_yaml = re.sub(
                        r'^rating:\s*(.+?)\s*$\n',
                        '',
                        new_yaml,
                        flags=re.MULTILINE
                    )
                    modified = True
                    self.changes.append({
                        "file": str(file_path.relative_to(self.vault_root)),
                        "action": "remove_null",
                        "old_value": rating_value,
                        "new_value": "[REMOVED]"
                    })

                # 处理超出范围的数字值
                else:
                    try:
                        rating_num = float(rating_value)
                        if rating_num > 5 or rating_num < 1:
                            # 转换为 1-5 范围
                            new_rating_value = self.convert_rating_10_to_5(rating_num)
                            new_yaml = re.sub(
                                r'^rating:\s*(.+?)\s*$',
                                f'rating: {new_rating_value}',
                                new_yaml,
                                flags=re.MULTILINE
                            )
                            modified = True
                            self.changes.append({
                                "file": str(file_path.relative_to(self.vault_root)),
                                "action": "convert_range",
                                "old_value": rating_value,
                                "new_value": str(new_rating_value)
                            })
                    except ValueError:
                        # 非数字值，保持不变
                        pass

            if modified:
                # 重新组装内容
                new_content = new_yaml.join(yaml_match.group(0).split(yaml_content))

                if self.dry_run:
                    print(f"[DRY RUN] Would modify: {file_path.relative_to(self.vault_root)}")
                else:
                    # 备份原文件
                    if not self.backup_dir.exists():
                        self.backup_dir.mkdir(parents=True, exist_ok=True)

                    backup_path = self.backup_dir / file_path.relative_to(self.vault_root)
                    backup_path.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(file_path, backup_path)

                    # 写入修改后的内容
                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write(new_content)

                    print(f"[MODIFIED] {file_path.relative_to(self.vault_root)}")

        except Exception as e:
            print(f"[ERROR] {file_path.relative_to(self.vault_root)}: {e}")

    def scan_and_fix(self, directory: str = None):
        """扫描并修复目录下的所有 markdown 文件"""
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

                self.fix_file(md_file)

    def print_report(self):
        """打印修改报告"""
        print("\n" + "=" * 80)
        print("📝 Rating 字段规范化报告")
        print("=" * 80)
        print(f"模式: {'DRY RUN (预览)' if self.dry_run else 'LIVE (实际执行)'}")
        print(f"修改数量: {len(self.changes)}")
        print()

        if not self.changes:
            print("✅ 没有需要修复的文件")
            return

        # 按操作类型分组
        by_action = {}
        for change in self.changes:
            action = change["action"]
            if action not in by_action:
                by_action[action] = []
            by_action[action].append(change)

        for action, changes in by_action.items():
            action_name = {
                "convert_range": "转换范围 (10分制 → 5分制)",
                "remove_null": "移除 null 值"
            }.get(action, action)

            print(f"\n## {action_name} ({len(changes)} 个文件)")
            print("-" * 80)
            for change in changes[:10]:
                print(f"  {change['file']}")
                print(f"    {change['old_value']} → {change['new_value']}")
            if len(changes) > 10:
                print(f"  ... 还有 {len(changes) - 10} 个文件")

        print("\n" + "=" * 80)

        if not self.dry_run:
            print(f"✅ 修改完成")
            print(f"📁 备份位置: {self.backup_dir.relative_to(self.vault_root)}")
        else:
            print("⚠️  这是 DRY RUN 模式，没有实际修改文件")
            print("💡 如需实际执行，请使用: python fix_ratings.py --execute")
        print("=" * 80)


def main():
    """主函数"""
    import argparse

    parser = argparse.ArgumentParser(description="规范化知识库中的 rating 字段")
    parser.add_argument("--execute", action="store_true", help="实际执行修改（默认为 dry run）")
    args = parser.parse_args()

    # 获取脚本所在目录的父目录作为 vault 根目录
    # 脚本在: 5.Misc/Template/Scripts/content-quality/fix_ratings.py
    # 需要向上 3 层到: obsidianDoc/
    script_dir = Path(__file__).parent
    vault_root = script_dir.parent.parent.parent.parent

    print(f"知识库根目录: {vault_root}")
    print()

    fixer = RatingFixer(str(vault_root), dry_run=not args.execute)
    fixer.scan_and_fix()
    fixer.print_report()


if __name__ == "__main__":
    main()
