#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
文件操作工具模块

提供统一的 Markdown 文件扫描逻辑，支持：
- 按目录扫描
- 排除特定模式
- 生成器模式（内存高效）
- 文件统计

此功能在 8 个现有脚本中重复出现，现在统一到此模块。

作者: Claude Sonnet 4.5
创建时间: 2026-01-25
用途: Issue #4 - 自动化脚本体系优化
"""

from pathlib import Path
from typing import List, Iterator, Optional, Set


class FileScanner:
    """
    统一的文件扫描器

    提供高效、灵活的 Markdown 文件扫描功能，支持按目录过滤、
    排除特定模式、生成器模式等特性。

    Attributes:
        vault_root (Path): Vault 根目录
        include_dirs (List[str]): 包含的目录列表
        exclude_patterns (Optional[List[str]]): 排除的模式列表

    Examples:
        >>> scanner = FileScanner(Path("/path/to/vault"))
        >>> for file in scanner.scan_markdown_files():
        ...     print(file)
        /path/to/vault/0.DailyNotes/note.md
        /path/to/vault/1.Projects/project.md

        >>> # 统计文件数量
        >>> count = scanner.count_files()
        >>> print(f"共 {count} 个 Markdown 文件")
        共 535 个 Markdown 文件
    """

    # 默认排除的目录
    DEFAULT_EXCLUDE_DIRS: Set[str] = {
        '.git', '.obsidian', '.trash', 'node_modules', '.venv',
        '.opencode', '.smart-env', '.agent'
    }

    # 默认包含的目录（PARA 结构 + Atlas）
    DEFAULT_INCLUDE_DIRS: List[str] = [
        "0.DailyNotes",
        "1.Projects",
        "2.Topics",
        "3.Resources",
        "4.Archives",
        "5.Misc",
        "6.Calendar",
        "Atlas"
    ]

    def __init__(
        self,
        vault_root: Path,
        include_dirs: Optional[List[str]] = None,
        exclude_patterns: Optional[List[str]] = None
    ):
        """
        初始化文件扫描器

        Args:
            vault_root: Vault 根目录
            include_dirs: 包含的目录列表（默认使用 DEFAULT_INCLUDE_DIRS）
            exclude_patterns: 排除的模式列表（用于过滤文件路径）
        """
        self.vault_root = Path(vault_root)
        self.include_dirs = include_dirs or self.DEFAULT_INCLUDE_DIRS
        self.exclude_patterns = exclude_patterns

    def scan_markdown_files(
        self,
        exclude_patterns: Optional[List[str]] = None
    ) -> Iterator[Path]:
        """
        扫描 Markdown 文件（生成器模式）

        使用生成器模式，避免一次性加载所有文件到内存，
        适合处理大型 vault。

        Args:
            exclude_patterns: 临时排除的模式列表（与实例的 exclude_patterns 合并）

        Yields:
            Path: Markdown 文件的完整路径

        Examples:
            >>> scanner = FileScanner(Path("/path/to/vault"))
            >>> for file in scanner.scan_markdown_files(exclude_patterns=[".backup"]):
            ...     print(file.name)
            note1.md
            note2.md
        """
        # 合并排除模式
        all_exclude_patterns = list(self.exclude_patterns or [])
        if exclude_patterns:
            all_exclude_patterns.extend(exclude_patterns)

        for dir_name in self.include_dirs:
            dir_path = self.vault_root / dir_name

            # 跳过不存在的目录
            if not dir_path.exists():
                continue

            # 递归扫描 .md 文件
            for md_file in dir_path.rglob("*.md"):
                # 跳过隐藏文件
                if md_file.name.startswith('.'):
                    continue

                # 应用排除模式
                if all_exclude_patterns:
                    if any(pattern in str(md_file) for pattern in all_exclude_patterns):
                        continue

                yield md_file

    def count_files(self, exclude_patterns: Optional[List[str]] = None) -> int:
        """
        统计 Markdown 文件数量

        Args:
            exclude_patterns: 排除的模式列表

        Returns:
            int: 文件数量

        Examples:
            >>> scanner = FileScanner(Path("/path/to/vault"))
            >>> count = scanner.count_files()
            >>> print(f"共 {count} 个文件")
            共 535 个文件
        """
        return sum(1 for _ in self.scan_markdown_files(exclude_patterns))

    def get_files_list(self, exclude_patterns: Optional[List[str]] = None) -> List[Path]:
        """
        获取所有 Markdown 文件列表（非生成器模式）

        注意：对于大型 vault，建议使用 scan_markdown_files() 生成器模式。

        Args:
            exclude_patterns: 排除的模式列表

        Returns:
            List[Path]: 文件路径列表

        Examples:
            >>> scanner = FileScanner(Path("/path/to/vault"))
            >>> files = scanner.get_files_list()
            >>> print(f"共 {len(files)} 个文件")
            共 535 个文件
        """
        return list(self.scan_markdown_files(exclude_patterns))

    def scan_directory(self, directory: str) -> Iterator[Path]:
        """
        扫描单个目录

        Args:
            directory: 目录名称（相对于 vault_root）

        Yields:
            Path: Markdown 文件路径

        Examples:
            >>> scanner = FileScanner(Path("/path/to/vault"))
            >>> for file in scanner.scan_directory("0.DailyNotes"):
            ...     print(file.name)
            daily_note_1.md
            daily_note_2.md
        """
        dir_path = self.vault_root / directory
        if not dir_path.exists():
            return

        for md_file in dir_path.rglob("*.md"):
            if md_file.name.startswith('.'):
                continue
            yield md_file


if __name__ == "__main__":
    # 测试代码
    import sys

    # 获取当前脚本的目录作为测试 vault
    test_vault = Path(__file__).parent.parent.parent.parent

    print(f"测试文件扫描器...")
    print(f"测试 Vault: {test_vault}")

    scanner = FileScanner(test_vault)

    # 统计文件数量
    count = scanner.count_files()
    print(f"✓ 找到 {count} 个 Markdown 文件")

    # 列出前 5 个文件
    print("\n前 5 个文件:")
    for i, file in enumerate(scanner.scan_markdown_files()):
        if i >= 5:
            break
        print(f"  {file.relative_to(test_vault)}")

    print("\n✓ 文件扫描器工作正常")
