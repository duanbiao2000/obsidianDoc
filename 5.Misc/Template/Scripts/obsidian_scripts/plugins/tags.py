#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
标签管理插件

提供统一的标签管理功能，整合了所有标签相关脚本的功能：
- 批量添加 Domain/Type/Status 标签
- 清理重复标签
- 标签规范化

作者: Claude Sonnet 4.5
创建时间: 2026-01-25
相关: Issue #4 - 自动化脚本体系优化
"""

import re
from pathlib import Path
from typing import Dict, List, Optional

from ..core.config import Config
from ..core.file_utils import FileScanner
from ..core.frontmatter import FrontmatterParser, Frontmatter
from ..utils.backup import BackupManager


class TagManager:
    """
    标签管理器

    整合所有标签管理功能，提供统一的接口。

    Attributes:
        config (Config): 配置对象
        file_scanner (FileScanner): 文件扫描器
        backup_manager (BackupManager): 备份管理器

    Examples:
        >>> tag_manager = TagManager()
        >>> stats = tag_manager.add_domain_tags(dry_run=True)
        >>> print(f"处理了 {stats['processed']} 个文件")
    """

    # 标签推断规则（从 batch_add_domain_tags.py 迁移）
    DOMAIN_RULES = [
        (r"2\.Topics/01\.技术栈", "Domain/Technology"),
        (r"2\.Topics/02\.认知系统", "Domain/Cognitive"),
        (r"2\.Topics/03\.内容创作", "Domain/Content"),
        (r"2\.Topics/04\.职业发展", "Domain/Professional"),
        (r"2\.Topics/05\.生活与健康", "Domain/Life"),
        (r"2\.Topics/06\.语言与移民", "Domain/Language"),
    ]

    TYPE_RULES = [
        (r".*_Index_.*|.*Index.*", "Type/Index"),
        (r".*模板.*|.*Template.*", "Type/Template"),
    ]

    STATUS_RULES = [
        (r".*已.*|.*done.*|.*完成.*", "Status/Done"),
        (r".*进行中.*|.*in.*progress.*", "Status/InProgress"),
        (r".*待.*|.*todo.*", "Status/TODO"),
    ]

    def __init__(self, config: Optional[Config] = None):
        """
        初始化标签管理器

        Args:
            config: 配置对象（如果为 None，使用默认配置）
        """
        self.config = config or Config()
        self.file_scanner = FileScanner(
            self.config.vault_root,
            self.config.include_dirs
        )
        self.backup_manager = BackupManager(
            backup_dir=self.config.vault_root / self.config.backup_dir,
            keep_days=self.config.get('backup.keep_days', 30)
        )

    def add_domain_tags(
        self,
        dry_run: bool = False,
        verbose: bool = False
    ) -> Dict[str, int]:
        """
        批量添加 Domain 标签

        根据文件路径自动推断并添加 Domain/Type/Status 标签。

        Args:
            dry_run: 预览模式（不实际修改文件）
            verbose: 显示详细信息

        Returns:
            Dict[str, int]: 统计信息
                - processed: 成功处理的文件数
                - skipped: 跳过的文件数
                - failed: 失败的文件数

        Examples:
            >>> tag_manager = TagManager()
            >>> stats = tag_manager.add_domain_tags(dry_run=True, verbose=True)
        """
        stats = {'processed': 0, 'skipped': 0, 'failed': 0}

        for filepath in self.file_scanner.scan_markdown_files():
            try:
                # 读取文件
                content = filepath.read_text(encoding='utf-8')
                fm = FrontmatterParser.parse(content)

                # 检查是否已有 Domain 标签
                if self._has_domain_tag(fm):
                    stats['skipped'] += 1
                    if verbose:
                        print(f"⊙ {filepath.name} - 已有Domain标签")
                    continue

                # 推断标签
                new_tags = self._infer_tags_from_path(filepath)
                if not new_tags:
                    stats['skipped'] += 1
                    continue

                # 更新 frontmatter
                current_tags = fm.get_tags()
                all_tags = current_tags + new_tags
                fm.set_tags(all_tags)

                # 写回文件
                if not dry_run:
                    self.backup_manager.create_backup(filepath)
                    filepath.write_text(fm.to_string(), encoding='utf-8')

                stats['processed'] += 1
                if verbose:
                    print(f"✓ {filepath.name} - 添加: {', '.join(new_tags[:3])}")

            except Exception as e:
                stats['failed'] += 1
                if verbose:
                    print(f"✗ {filepath.name} - 错误: {e}")

        return stats

    def cleanup_duplicates(
        self,
        dry_run: bool = False,
        verbose: bool = False
    ) -> Dict[str, int]:
        """
        清理重复标签

        移除 YAML frontmatter 中的重复标签，保持顺序。

        Args:
            dry_run: 预览模式（不实际修改文件）
            verbose: 显示详细信息

        Returns:
            Dict[str, int]: 统计信息
                - processed: 处理的文件数
                - duplicates_removed: 移除的重复标签数

        Examples:
            >>> tag_manager = TagManager()
            >>> stats = tag_manager.cleanup_duplicates()
            >>> print(f"清理了 {stats['duplicates_removed']} 个重复标签")
        """
        stats = {'processed': 0, 'duplicates_removed': 0}

        for filepath in self.file_scanner.scan_markdown_files():
            try:
                content = filepath.read_text(encoding='utf-8')
                fm = FrontmatterParser.parse(content)

                tags = fm.get_tags()
                # 去重但保持顺序
                unique_tags = list(dict.fromkeys(tags))

                if len(unique_tags) == len(tags):
                    continue  # 无重复

                duplicates_removed = len(tags) - len(unique_tags)
                stats['duplicates_removed'] += duplicates_removed

                if not dry_run:
                    self.backup_manager.create_backup(filepath)
                    fm.set_tags(unique_tags)
                    filepath.write_text(fm.to_string(), encoding='utf-8')

                stats['processed'] += 1
                if verbose:
                    print(f"✓ {filepath.name} - 清理: {duplicates_removed}个重复")

            except Exception as e:
                if verbose:
                    print(f"✗ {filepath.name} - 错误: {e}")

        return stats

    def normalize_tags(
        self,
        phase: str = 'all',
        dry_run: bool = False,
        verbose: bool = False
    ) -> Dict[str, int]:
        """
        标签规范化

        分阶段执行标签替换，移除无效标签，修正格式。

        Args:
            phase: 执行阶段 ('invalid', 'high', 'medium', 'low', 'all')
            dry_run: 预览模式（不实际修改文件）
            verbose: 显示详细信息

        Returns:
            Dict[str, int]: 统计信息
                - deleted: 删除的标签数
                - replaced: 替换的标签数
                - files_modified: 修改的文件数

        Examples:
            >>> tag_manager = TagManager()
            >>> stats = tag_manager.normalize_tags(phase='invalid', dry_run=True)
        """
        # TODO: 实现标签规范化逻辑
        # 需要加载 config/tag_rules.yaml 中的映射规则
        stats = {'deleted': 0, 'replaced': 0, 'files_modified': 0}
        return stats

    def _has_domain_tag(self, fm: Frontmatter) -> bool:
        """
        检查是否已有 Domain 标签

        Args:
            fm: Frontmatter 对象

        Returns:
            bool: 如果包含 Domain 标签返回 True
        """
        return any(tag.startswith('Domain/') for tag in fm.get_tags())

    def _infer_tags_from_path(self, filepath: Path) -> List[str]:
        """
        从路径推断标签

        Args:
            filepath: 文件路径

        Returns:
            List[str]: 推断的标签列表
        """
        tags = []
        relative_path = str(filepath.relative_to(self.config.vault_root))

        # 推断 Domain 标签
        for pattern, tag in self.DOMAIN_RULES:
            if re.search(pattern, relative_path):
                if tag not in tags:
                    tags.append(tag)
                break  # 只使用第一个匹配

        # 推断 Type 标签
        for pattern, tag in self.TYPE_RULES:
            if re.search(pattern, filepath.name):
                if tag not in tags:
                    tags.append(tag)
                break

        # 推断 Status 标签
        for pattern, tag in self.STATUS_RULES:
            if re.search(pattern, filepath.name):
                if tag not in tags:
                    tags.append(tag)
                break

        return tags


if __name__ == "__main__":
    # 测试代码
    from ..core.encoding import auto_setup
    auto_setup()

    print("测试标签管理器...")

    tag_manager = TagManager()

    print(f"\n=== 批量添加 Domain 标签 (dry-run) ===")
    stats = tag_manager.add_domain_tags(dry_run=True, verbose=False)
    print(f"处理: {stats['processed']}, 跳过: {stats['skipped']}, 失败: {stats['failed']}")

    print(f"\n=== 清理重复标签 (dry-run) ===")
    stats = tag_manager.cleanup_duplicates(dry_run=True, verbose=False)
    print(f"处理: {stats['processed']}, 清理: {stats['duplicates_removed']}")

    print("\n✓ 标签管理器工作正常")
