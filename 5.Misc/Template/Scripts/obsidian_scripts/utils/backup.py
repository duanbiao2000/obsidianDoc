#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
备份工具模块

提供统一的文件备份功能，支持：
- 创建时间戳备份
- 自动清理过期备份
- 备份目录管理

此功能在 4+ 个现有脚本中重复出现，现在统一到此模块。

作者: Claude Sonnet 4.5
创建时间: 2026-01-25
用途: Issue #4 - 自动化脚本体系优化
"""

import shutil
from pathlib import Path
from typing import Optional, List
from datetime import datetime, timedelta


class BackupManager:
    """
    备份管理器

    提供文件备份和管理功能。

    Attributes:
        backup_dir (Path): 备份目录路径
        keep_days (int): 保留备份的天数

    Examples:
        >>> backup_mgr = BackupManager()
        >>> backup_mgr.create_backup(Path("note.md"))
        >>> backup_mgr.cleanup_old_backups()
    """

    def __init__(
        self,
        backup_dir: Optional[Path] = None,
        keep_days: int = 30
    ):
        """
        初始化备份管理器

        Args:
            backup_dir: 备份目录（默认为 .backup_enhance）
            keep_days: 保留天数（默认 30 天）
        """
        self.backup_dir = Path(backup_dir) if backup_dir else Path('.backup_enhance')
        self.keep_days = keep_days

        # 确保备份目录存在
        self.backup_dir.mkdir(exist_ok=True)

    def create_backup(self, file_path: Path) -> Path:
        """
        创建备份文件

        使用时间戳命名备份文件，格式为：<原文件名>.<时间戳>.bak<扩展名>

        Args:
            file_path: 要备份的文件路径

        Returns:
            Path: 备份文件路径

        Raises:
            FileNotFoundError: 如果原文件不存在
            IOError: 如果备份创建失败

        Examples:
            >>> backup_mgr = BackupManager()
            >>> backup_path = backup_mgr.create_backup(Path("note.md"))
            >>> print(backup_path)
            .backup_enhance/note.20260125_143022.bak.md
        """
        if not file_path.exists():
            raise FileNotFoundError(f"文件不存在: {file_path}")

        # 生成时间戳
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        # 生成备份文件名
        backup_name = f"{file_path.stem}.{timestamp}.bak{file_path.suffix}"
        backup_path = self.backup_dir / backup_name

        # 复制文件
        shutil.copy2(file_path, backup_path)

        return backup_path

    def restore_backup(self, backup_path: Path, target_path: Path) -> None:
        """
        恢复备份文件

        Args:
            backup_path: 备份文件路径
            target_path: 目标文件路径

        Raises:
            FileNotFoundError: 如果备份文件不存在

        Examples:
            >>> backup_mgr = BackupManager()
            >>> backup_mgr.restore_backup(
            ...     Path(".backup_enhance/note.20260125_143022.bak.md"),
            ...     Path("note.md")
            ... )
        """
        if not backup_path.exists():
            raise FileNotFoundError(f"备份文件不存在: {backup_path}")

        # 确保目标目录存在
        target_path.parent.mkdir(parents=True, exist_ok=True)

        # 复制备份文件
        shutil.copy2(backup_path, target_path)

    def cleanup_old_backups(self, days: Optional[int] = None) -> List[Path]:
        """
        清理过期备份

        删除超过指定天数的备份文件。

        Args:
            days: 保留天数（默认使用实例的 keep_days）

        Returns:
            List[Path]: 已删除的备份文件列表

        Examples:
            >>> backup_mgr = BackupManager(keep_days=30)
            >>> deleted = backup_mgr.cleanup_old_backups()
            >>> print(f"删除了 {len(deleted)} 个过期备份")
        """
        keep_days = days if days is not None else self.keep_days
        cutoff_date = datetime.now() - timedelta(days=keep_days)

        deleted_files = []

        for backup_file in self.backup_dir.glob("*.bak*"):
            # 获取文件修改时间
            mtime = datetime.fromtimestamp(backup_file.stat().st_mtime)

            # 如果文件超过保留天数，删除它
            if mtime < cutoff_date:
                backup_file.unlink()
                deleted_files.append(backup_file)

        return deleted_files

    def list_backups(self, file_path: Optional[Path] = None) -> List[Path]:
        """
        列出备份文件

        Args:
            file_path: 如果指定，只列出该文件的备份

        Returns:
            List[Path]: 备份文件列表（按修改时间排序）

        Examples:
            >>> backup_mgr = BackupManager()
            >>> backups = backup_mgr.list_backups(Path("note.md"))
            >>> for backup in backups:
            ...     print(backup.name)
        """
        if file_path:
            # 列出特定文件的备份
            pattern = f"{file_path.stem}.*.bak{file_path.suffix}"
            backups = list(self.backup_dir.glob(pattern))
        else:
            # 列出所有备份
            backups = list(self.backup_dir.glob("*.bak*"))

        # 按修改时间排序（最新的在前）
        backups.sort(key=lambda p: p.stat().st_mtime, reverse=True)

        return backups

    def get_backup_count(self, file_path: Optional[Path] = None) -> int:
        """
        获取备份文件数量

        Args:
            file_path: 如果指定，只统计该文件的备份

        Returns:
            int: 备份文件数量

        Examples:
            >>> backup_mgr = BackupManager()
            >>> count = backup_mgr.get_backup_count(Path("note.md"))
            >>> print(f"共有 {count} 个备份")
        """
        return len(self.list_backups(file_path))

    def clear_all_backups(self) -> List[Path]:
        """
        清空所有备份

        Returns:
            List[Path]: 已删除的备份文件列表

        Examples:
            >>> backup_mgr = BackupManager()
            >>> deleted = backup_mgr.clear_all_backups()
            >>> print(f"删除了 {len(deleted)} 个备份文件")
        """
        deleted_files = []

        for backup_file in self.backup_dir.glob("*.bak*"):
            backup_file.unlink()
            deleted_files.append(backup_file)

        return deleted_files

    def get_backup_size(self) -> int:
        """
        获取备份目录总大小（字节）

        Returns:
            int: 备份目录总大小

        Examples:
            >>> backup_mgr = BackupManager()
            >>> size = backup_mgr.get_backup_size()
            >>> print(f"备份总大小: {size / 1024 / 1024:.2f} MB")
        """
        total_size = 0

        for backup_file in self.backup_dir.glob("*.bak*"):
            total_size += backup_file.stat().st_size

        return total_size


if __name__ == "__main__":
    # 测试代码
    import tempfile

    print("测试备份管理器...")

    # 创建临时目录进行测试
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)
        test_file = temp_path / "test_note.md"
        test_backup_dir = temp_path / "backups"

        # 创建测试文件
        test_file.write_text("# 测试内容\n\n这是测试文件。")

        # 创建备份管理器
        backup_mgr = BackupManager(backup_dir=test_backup_dir, keep_days=30)

        print(f"\n=== 创建备份 ===")
        backup_path = backup_mgr.create_backup(test_file)
        print(f"备份文件: {backup_path.name}")
        print(f"备份存在: {backup_path.exists()}")

        print(f"\n=== 列出备份 ===")
        backups = backup_mgr.list_backups(test_file)
        print(f"备份数量: {len(backups)}")
        for backup in backups:
            print(f"  - {backup.name}")

        print(f"\n=== 备份统计 ===")
        print(f"备份数量: {backup_mgr.get_backup_count(test_file)}")
        print(f"备份大小: {backup_mgr.get_backup_size()} 字节")

        print(f"\n=== 清理备份 ===")
        deleted = backup_mgr.cleanup_old_backups(days=0)  # 清理所有备份
        print(f"删除了 {len(deleted)} 个备份")

    print("\n✓ 备份管理器工作正常")
