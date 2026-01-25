#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
pytest 配置和共享 fixtures

提供测试用的共享 fixtures 和配置。

作者: Claude Sonnet 4.5
创建时间: 2026-01-25
相关: Issue #4 - 自动化脚本体系优化
"""

import pytest
from pathlib import Path
import tempfile
import shutil


@pytest.fixture
def temp_vault(tmp_path):
    """
    创建临时测试 vault

    Args:
        tmp_path: pytest 提供的临时目录

    Returns:
        Path: 临时 vault 路径

    Examples:
        >>> def test_something(temp_vault):
        ...     note = temp_vault / "test.md"
        ...     note.write_text("# Test")
    """
    # 创建标准目录结构
    for dir_name in ["0.DailyNotes", "1.Projects", "2.Topics", "Atlas"]:
        (tmp_path / dir_name).mkdir(parents=True, exist_ok=True)

    return tmp_path


@pytest.fixture
def sample_note(temp_vault):
    """
    创建示例笔记文件

    Args:
        temp_vault: 临时 vault 目录

    Returns:
        Path: 示例笔记文件路径

    Examples:
        >>> def test_note(sample_note):
        ...     content = sample_note.read_text()
        ...     assert "Test" in content
    """
    note_path = temp_vault / "2.Topics" / "test_note.md"
    note_path.write_text("""---
tags: [Domain/AI, Type/Note, Status/TODO]
update: 2026-01-25
---

# 测试笔记

这是一个测试笔记，包含 [[链接]] 和 #标签。
""")
    return note_path


@pytest.fixture
def sample_note_with_links(temp_vault):
    """
    创建包含链接的示例笔记

    Args:
        temp_vault: 临时 vault 目录

    Returns:
        Path: 示例笔记文件路径
    """
    note_path = temp_vault / "2.Topics" / "linked_note.md"
    note_path.write_text("""---
tags: [Domain/Cognitive, Type/Reference]
---

# 链接笔记

这个笔记链接到 [[其他笔记]]。
""")
    return note_path


@pytest.fixture
def config(temp_vault):
    """
    创建测试配置对象

    Args:
        temp_vault: 临时 vault 目录

    Returns:
        Config: 配置对象
    """
    from obsidian_scripts.core.config import Config

    # 创建临时配置文件
    config_file = temp_vault / "test_config.yaml"
    config_file.write_text(f"""vault_root: "{temp_vault}"
scan:
  include_dirs:
    - "2.Topics"
  exclude_patterns: []
""")

    return Config(config_path=config_file)
