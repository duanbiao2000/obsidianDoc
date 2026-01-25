#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Windows 编码处理模块

提供统一的 Windows UTF-8 编码支持，解决控制台输出乱码问题。
此功能在 16 个现有脚本中重复出现，现在统一到此模块。

作者: Claude Sonnet 4.5
创建时间: 2026-01-25
用途: Issue #4 - 自动化脚本体系优化
"""

import sys
import io
from typing import Optional


def setup_utf8_output() -> bool:
    """
    配置 Windows UTF-8 编码输出

    在 Windows 平台上，将 stdout 和 stderr 重新配置为 UTF-8 编码，
    以解决中文输出乱码问题。

    Returns:
        bool: 如果进行了配置返回 True，否则返回 False

    Examples:
        >>> from obsidian_scripts.core.encoding import setup_utf8_output
        >>> setup_utf8_output()
        True
        >>> print("中文输出正常")
        中文输出正常
    """
    if sys.platform == 'win32':
        # Windows 平台：重新配置 stdout 和 stderr
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
        sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')
        return True
    return False


def auto_setup() -> None:
    """
    自动设置 UTF-8 编码（脚本开头调用）

    这是推荐的入口函数，在脚本开头调用一次即可。
    不会抛出异常，适用于所有平台。

    Examples:
        >>> from obsidian_scripts.core.encoding import auto_setup
        >>> auto_setup()
        >>> # 现在可以安全地输出中文
        >>> print("你好，世界！")
        你好，世界！
    """
    try:
        setup_utf8_output()
    except Exception:
        # 静默失败，避免影响脚本执行
        pass


def get_encoding() -> str:
    """
    获取当前标准输出的编码

    Returns:
        str: 当前编码名称

    Examples:
        >>> get_encoding()
        'utf-8'
    """
    return sys.stdout.encoding


def is_utf8() -> bool:
    """
    检查标准输出是否使用 UTF-8 编码

    Returns:
        bool: 如果是 UTF-8 编码返回 True

    Examples:
        >>> is_utf8()
        True
    """
    return get_encoding().lower() in ('utf-8', 'utf8')


# 为了向后兼容，提供一个简单的函数别名
configure_utf8 = setup_utf8_output


if __name__ == "__main__":
    # 测试代码
    print("测试编码模块...")
    print(f"平台: {sys.platform}")
    print(f"编码: {get_encoding()}")
    print(f"是否UTF-8: {is_utf8()}")
    print("中文测试：你好，世界！")
    print("✓ 编码模块工作正常")
