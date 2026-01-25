#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
核心模块单元测试

测试 obsidian_scripts.core 包中的核心功能。

作者: Claude Sonnet 4.5
创建时间: 2026-01-25
相关: Issue #4 - 自动化脚本体系优化
"""

import pytest
from pathlib import Path

from obsidian_scripts.core.encoding import setup_utf8_output, is_utf8
from obsidian_scripts.core.file_utils import FileScanner
from obsidian_scripts.core.config import Config
from obsidian_scripts.core.frontmatter import FrontmatterParser, Frontmatter
from obsidian_scripts.core.markdown import MarkdownParser


class TestEncoding:
    """测试编码处理模块"""

    def test_setup_utf8_output(self):
        """测试 UTF-8 编码设置"""
        # 应该不抛出异常
        setup_utf8_output()
        assert True

    def test_is_utf8(self):
        """测试 UTF-8 检测"""
        # 当前环境应该是 UTF-8
        result = is_utf8()
        assert isinstance(result, bool)


class TestFileScanner:
    """测试文件扫描器"""

    def test_scan_markdown_files(self, temp_vault):
        """测试 Markdown 文件扫描"""
        # 创建测试文件
        (temp_vault / "2.Topics" / "test1.md").write_text("# Test 1")
        (temp_vault / "2.Topics" / "test2.md").write_text("# Test 2")
        (temp_vault / "0.DailyNotes" / "test3.md").write_text("# Test 3")

        scanner = FileScanner(temp_vault, include_dirs=["2.Topics"])
        files = list(scanner.scan_markdown_files())

        assert len(files) == 2
        assert all(f.suffix == ".md" for f in files)

    def test_count_files(self, temp_vault):
        """测试文件统计"""
        (temp_vault / "2.Topics" / "test.md").write_text("# Test")

        scanner = FileScanner(temp_vault, include_dirs=["2.Topics"])
        count = scanner.count_files()

        assert count == 1


class TestFrontmatterParser:
    """测试 Frontmatter 解析器"""

    def test_parse_with_frontmatter(self):
        """测试解析带 frontmatter 的内容"""
        content = """---
tags: [AI, Python]
---
正文内容"""
        parser = FrontmatterParser()
        fm = parser.parse(content)

        assert fm.get_tags() == ["AI", "Python"]
        assert fm.body.strip() == "正文内容"

    def test_parse_without_frontmatter(self):
        """测试解析不带 frontmatter 的内容"""
        content = "没有 frontmatter 的内容"
        parser = FrontmatterParser()
        fm = parser.parse(content)

        assert fm.get_tags() == []
        assert fm.body == content

    def test_add_tag(self):
        """测试添加标签"""
        fm = Frontmatter("", {}, "")
        fm.add_tag("Test")

        assert "Test" in fm.get_tags()

    def test_remove_tag(self):
        """测试删除标签"""
        fm = Frontmatter("", {"tags": ["AI", "Python"]}, "")
        fm.remove_tag("AI")

        assert "AI" not in fm.get_tags()
        assert "Python" in fm.get_tags()


class TestMarkdownParser:
    """测试 Markdown 解析器"""

    def test_extract_wiki_links(self):
        """测试提取 Wiki 链接"""
        content = "[[链接1]] [[链接2|别名]]"
        parser = MarkdownParser()
        links = parser.extract_links(content)

        assert len(links) == 2
        assert links[0].target == "链接1"
        assert links[1].target == "链接2"
        assert links[1].alias == "别名"

    def test_count_links(self):
        """测试链接统计"""
        content = "[[link]] #tag ![[embed]]"
        parser = MarkdownParser()
        stats = parser.count_links(content)

        assert stats['wiki_links'] == 1
        assert stats['tags'] == 1
        assert stats['embeds'] == 1

    def test_extract_tags(self):
        """测试提取标签"""
        content = "内容包含 #AI #Python 和 #AI"
        parser = MarkdownParser()
        tags = parser.extract_tags(content)

        assert len(tags) == 2  # AI 和 Python（去重）
        assert "AI" in tags
        assert "Python" in tags


class TestConfig:
    """测试配置管理器"""

    def test_get_vault_root(self, temp_vault):
        """测试获取 vault 根目录"""
        config = Config()
        assert isinstance(config.vault_root, Path)

    def test_get_with_default(self):
        """测试获取配置值（带默认值）"""
        config = Config()
        value = config.get("nonexistent.key", "default_value")

        assert value == "default_value"

    def test_include_dirs(self):
        """测试获取包含目录"""
        config = Config()
        dirs = config.include_dirs

        assert isinstance(dirs, list)
        assert "2.Topics" in dirs
