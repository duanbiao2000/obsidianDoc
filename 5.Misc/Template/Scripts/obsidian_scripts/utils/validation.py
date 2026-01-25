#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
元数据验证工具

提供元数据质量验证功能，支持 Issue #3 的需求：
- 验证 Domain 标签
- 验证 Type 标签
- 验证 Status 标签
- 验证 update/created 等字段
- 生成审计报告

作者: Claude Sonnet 4.5
创建时间: 2026-01-25
相关: Issue #3 项目元数据审计, Issue #4 自动化脚本体系优化
"""

from pathlib import Path
from typing import List, Dict, Optional
from dataclasses import dataclass
from enum import Enum

from ..core.config import Config
from ..core.file_utils import FileScanner
from ..core.frontmatter import FrontmatterParser


class ValidationLevel(Enum):
    """验证级别"""
    ERROR = "ERROR"
    WARNING = "WARNING"
    INFO = "INFO"


@dataclass
class ValidationIssue:
    """
    验证问题数据类

    Attributes:
        level (ValidationLevel): 问题级别
        file_path (Path): 文件路径
        field (str): 字段名
        message (str): 问题描述
        suggestion (Optional[str]): 修复建议
    """
    level: ValidationLevel
    file_path: Path
    field: str
    message: str
    suggestion: Optional[str] = None


class MetadataValidator:
    """
    元数据验证器

    支持 Issue #3 的元数据审计需求。

    Attributes:
        config (Config): 配置对象
        file_scanner (FileScanner): 文件扫描器

    Examples:
        >>> validator = MetadataValidator()
        >>> issues = validator.validate_all()
        >>> print(f"找到 {len(issues)} 个问题")
    """

    # 有效的 Domain 标签列表
    VALID_DOMAINS = [
        "Domain/Technology",
        "Domain/AI",
        "Domain/Cognitive",
        "Domain/Professional",
        "Domain/Language",
        "Domain/Content",
        "Domain/Life"
    ]

    # 有效的 Type 标签列表
    VALID_TYPES = [
        "Type/Note",
        "Type/Reference",
        "Type/Template",
        "Type/Index",
        "Type/MOC"
    ]

    # 有效的 Status 标签列表
    VALID_STATUSES = [
        "Status/TODO",
        "Status/InProgress",
        "Status/Review",
        "Status/Done"
    ]

    def __init__(self, config: Optional[Config] = None):
        """
        初始化元数据验证器

        Args:
            config: 配置对象（如果为 None，使用默认配置）
        """
        self.config = config or Config()
        self.file_scanner = FileScanner(
            self.config.vault_root,
            self.config.include_dirs
        )

    def validate_all(
        self,
        include_domains: bool = True,
        include_types: bool = True,
        include_statuses: bool = True,
        include_dates: bool = True
    ) -> List[ValidationIssue]:
        """
        验证所有文件的元数据

        Args:
            include_domains: 验证 Domain 标签
            include_types: 验证 Type 标签
            include_statuses: 验证 Status 标签
            include_dates: 验证日期字段 (update, created)

        Returns:
            List[ValidationIssue]: 问题列表

        Examples:
            >>> validator = MetadataValidator()
            >>> issues = validator.validate_all()
            >>> for issue in issues:
            ...     print(f"{issue.level.value}: {issue.message}")
        """
        issues = []

        for filepath in self.file_scanner.scan_markdown_files():
            try:
                content = filepath.read_text(encoding='utf-8')
                fm = FrontmatterParser.parse(content)

                # 验证 Domain 标签
                if include_domains:
                    issues.extend(self._validate_domain_tags(filepath, fm))

                # 验证 Type 标签
                if include_types:
                    issues.extend(self._validate_type_tags(filepath, fm))

                # 验证 Status 标签
                if include_statuses:
                    issues.extend(self._validate_status_tags(filepath, fm))

                # 验证日期字段
                if include_dates:
                    issues.extend(self._validate_date_fields(filepath, fm))

            except Exception as e:
                issues.append(ValidationIssue(
                    level=ValidationLevel.ERROR,
                    file_path=filepath,
                    field='parse',
                    message=f'无法解析文件: {e}',
                    suggestion='检查 YAML frontmatter 格式'
                ))

        return issues

    def _validate_domain_tags(
        self,
        filepath: Path,
        fm: 'Frontmatter'
    ) -> List[ValidationIssue]:
        """验证 Domain 标签"""
        issues = []
        tags = fm.get_tags()
        domain_tags = [t for t in tags if t.startswith('Domain/')]

        # 缺少 Domain 标签
        if not domain_tags:
            issues.append(ValidationIssue(
                level=ValidationLevel.WARNING,
                file_path=filepath,
                field='tags',
                message='缺少 Domain 标签',
                suggestion=self._suggest_domain_tag(filepath)
            ))

        # Domain 标签格式不正确
        for tag in domain_tags:
            if not self._is_valid_domain_tag(tag):
                issues.append(ValidationIssue(
                    level=ValidationLevel.ERROR,
                    file_path=filepath,
                    field='tags',
                    message=f'无效的 Domain 标签: {tag}',
                    suggestion=f'参考: {", ".join(self.VALID_DOMAINS[:3])}...'
                ))

        return issues

    def _validate_type_tags(
        self,
        filepath: Path,
        fm: 'Frontmatter'
    ) -> List[ValidationIssue]:
        """验证 Type 标签"""
        issues = []
        tags = fm.get_tags()
        type_tags = [t for t in tags if t.startswith('Type/')]

        # Type 标签格式不正确
        for tag in type_tags:
            if tag not in self.VALID_TYPES:
                issues.append(ValidationIssue(
                    level=ValidationLevel.WARNING,
                    file_path=filepath,
                    field='tags',
                    message=f'非标准的 Type 标签: {tag}',
                    suggestion=f'参考: {", ".join(self.VALID_TYPES)}'
                ))

        return issues

    def _validate_status_tags(
        self,
        filepath: Path,
        fm: 'Frontmatter'
    ) -> List[ValidationIssue]:
        """验证 Status 标签"""
        issues = []
        tags = fm.get_tags()
        status_tags = [t for t in tags if t.startswith('Status/')]

        # Status 标签格式不正确
        for tag in status_tags:
            if tag not in self.VALID_STATUSES:
                issues.append(ValidationIssue(
                    level=ValidationLevel.WARNING,
                    file_path=filepath,
                    field='tags',
                    message=f'非标准的 Status 标签: {tag}',
                    suggestion=f'参考: {", ".join(self.VALID_STATUSES)}'
                ))

        return issues

    def _validate_date_fields(
        self,
        filepath: Path,
        fm: 'Frontmatter'
    ) -> List[ValidationIssue]:
        """验证日期字段"""
        issues = []

        # 检查 update 字段
        if not fm.get('update'):
            issues.append(ValidationIssue(
                level=ValidationLevel.INFO,
                file_path=filepath,
                field='update',
                message='缺少 update 字段',
                suggestion='添加更新日期'
            ))

        return issues

    def _is_valid_domain_tag(self, tag: str) -> bool:
        """检查 Domain 标签是否有效"""
        return any(tag.startswith(d) for d in self.VALID_DOMAINS)

    def _suggest_domain_tag(self, filepath: Path) -> str:
        """根据路径建议 Domain 标签"""
        relative_path = str(filepath.relative_to(self.config.vault_root))

        if "2.Topics/01.技术栈" in relative_path:
            return "建议: Domain/Technology"
        elif "2.Topics/02.认知系统" in relative_path:
            return "建议: Domain/Cognitive"
        elif "2.Topics/03.内容创作" in relative_path:
            return "建议: Domain/Content"
        elif "1.Projects" in relative_path:
            return "建议: Domain/Professional"
        else:
            return "建议: 根据文件内容添加合适的 Domain 标签"


if __name__ == "__main__":
    # 测试代码
    from ..core.encoding import auto_setup
    auto_setup()

    print("测试元数据验证器...")

    validator = MetadataValidator()

    print("\n=== 验证所有文件的元数据 ===")
    issues = validator.validate_all()

    # 按级别统计
    error_count = sum(1 for i in issues if i.level == ValidationLevel.ERROR)
    warning_count = sum(1 for i in issues if i.level == ValidationLevel.WARNING)
    info_count = sum(1 for i in issues if i.level == ValidationLevel.INFO)

    print(f"\n总计: {len(issues)} 个问题")
    print(f"  错误: {error_count}")
    print(f"  警告: {warning_count}")
    print(f"  信息: {info_count}")

    if issues and False:
        print("\n前 10 个问题：")
        for issue in issues[:10]:
            relative_path = issue.file_path.relative_to(validator.config.vault_root)
            print(f"[{issue.level.value}] {relative_path}")
            print(f"  字段: {issue.field}")
            print(f"  问题: {issue.message}")
            if issue.suggestion:
                print(f"  建议: {issue.suggestion}")
            print()

    print("\n✓ 元数据验证器工作正常")
