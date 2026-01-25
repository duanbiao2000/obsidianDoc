#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
YAML Frontmatter 处理模块

提供统一的 YAML frontmatter 解析和修改功能，支持：
- 解析 YAML frontmatter
- 提取和修改元数据
- 标签管理
- 序列化为字符串

此功能在 3+ 个现有脚本中重复出现，现在统一到此模块。

作者: Claude Sonnet 4.5
创建时间: 2026-01-25
用途: Issue #4 - 自动化脚本体系优化
"""

import re
from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass, field

try:
    import yaml
    HAS_YAML = True
except ImportError:
    HAS_YAML = False


@dataclass
class Frontmatter:
    """
    YAML frontmatter 数据类

    封装 YAML frontmatter 的原始内容、元数据和正文内容。

    Attributes:
        raw (str): YAML frontmatter 的原始字符串
        metadata (Dict): 解析后的元数据字典
        body (str): 正文内容

    Examples:
        >>> fm = Frontmatter("", {"tags": ["test"]}, "正文内容")
        >>> tags = fm.get_tags()
        >>> fm.set_tags(["new_tag"])
        >>> content = fm.to_string()
    """

    raw: str
    metadata: Dict[str, Any]
    body: str

    def get_tags(self) -> List[str]:
        """
        提取标签列表

        Returns:
            List[str]: 标签列表（如果没有标签返回空列表）

        Examples:
            >>> fm = Frontmatter("", {"tags": ["AI", "Python"]}, "")
            >>> fm.get_tags()
            ['AI', 'Python']
        """
        tags = self.metadata.get('tags', [])

        # 处理不同的标签格式
        if isinstance(tags, list):
            return tags
        elif isinstance(tags, str):
            # 单个标签字符串
            return [tags]
        else:
            return []

    def set_tags(self, tags: List[str], inline_threshold: int = 3) -> 'Frontmatter':
        """
        设置标签（自动选择单行/多行格式）

        Args:
            tags: 新的标签列表
            inline_threshold: 少于等于此数量使用单行格式

        Returns:
            Frontmatter: 返回自身以支持链式调用

        Examples:
            >>> fm = Frontmatter("", {}, "")
            >>> fm.set_tags(["tag1", "tag2"])
            >>> fm.set_tags(["tag1", "tag2", "tag3", "tag4"], inline_threshold=3)
        """
        # 去重但保持顺序
        unique_tags = list(dict.fromkeys(tags))

        # 根据数量选择格式
        if len(unique_tags) <= inline_threshold:
            # 单行格式
            self.metadata['tags'] = unique_tags
        else:
            # 多行格式
            self.metadata['tags'] = unique_tags

        return self

    def add_tag(self, tag: str) -> 'Frontmatter':
        """
        添加单个标签（自动去重）

        Args:
            tag: 要添加的标签

        Returns:
            Frontmatter: 返回自身以支持链式调用

        Examples:
            >>> fm = Frontmatter("", {"tags": ["AI"]}, "")
            >>> fm.add_tag("Python")
            >>> fm.get_tags()
            ['AI', 'Python']
        """
        tags = self.get_tags()
        if tag not in tags:
            tags.append(tag)
            self.set_tags(tags)
        return self

    def remove_tag(self, tag: str) -> 'Frontmatter':
        """
        删除标签

        Args:
            tag: 要删除的标签

        Returns:
            Frontmatter: 返回自身以支持链式调用
        """
        tags = self.get_tags()
        if tag in tags:
            tags.remove(tag)
            self.set_tags(tags)
        return self

    def has_tag(self, tag: str) -> bool:
        """
        检查是否包含指定标签

        Args:
            tag: 要检查的标签

        Returns:
            bool: 如果包含标签返回 True
        """
        return tag in self.get_tags()

    def get(self, key: str, default: Any = None) -> Any:
        """
        获取元数据字段

        Args:
            key: 字段名
            default: 默认值

        Returns:
            字段值或默认值
        """
        return self.metadata.get(key, default)

    def set(self, key: str, value: Any) -> 'Frontmatter':
        """
        设置元数据字段

        Args:
            key: 字段名
            value: 字段值

        Returns:
            Frontmatter: 返回自身以支持链式调用
        """
        self.metadata[key] = value
        return self

    def to_string(self) -> str:
        """
        序列化为字符串

        Returns:
            str: 完整的 Markdown 内容（包括 frontmatter 和正文）

        Examples:
            >>> fm = Frontmatter("---\\ntags: [test]\\n---\\n正文", {"tags": ["test"]}, "正文")
            >>> content = fm.to_string()
        """
        if not self.metadata:
            # 没有 metadata，只返回正文
            return self.body

        # 生成 YAML frontmatter
        if HAS_YAML:
            yaml_str = yaml.dump(self.metadata, default_flow_style=False, allow_unicode=True)
            # 移除末尾的换行符
            yaml_str = yaml_str.rstrip()
        else:
            # 简单的字符串格式化（不使用 PyYAML）
            yaml_str = self._simple_yaml_dump(self.metadata)

        return f"---\n{yaml_str}\n---\n{self.body}"

    def _simple_yaml_dump(self, data: Dict, indent: int = 0) -> str:
        """
        简单的 YAML 转储（不依赖 PyYAML）

        Args:
            data: 要转储的数据
            indent: 缩进级别

        Returns:
            str: YAML 格式字符串
        """
        lines = []
        indent_str = "  " * indent

        for key, value in data.items():
            if isinstance(value, list):
                if len(value) == 0:
                    lines.append(f"{indent_str}{key}: []")
                elif len(value) <= 3:
                    # 单行格式
                    str_value = ", ".join(str(v) for v in value)
                    lines.append(f"{indent_str}{key}: [{str_value}]")
                else:
                    # 多行格式
                    lines.append(f"{indent_str}{key}:")
                    for item in value:
                        lines.append(f"{indent_str}  - {item}")
            elif isinstance(value, dict):
                lines.append(f"{indent_str}{key}:")
                lines.append(self._simple_yaml_dump(value, indent + 1))
            elif isinstance(value, str):
                lines.append(f"{indent_str}{key}: {value}")
            elif isinstance(value, bool):
                lines.append(f"{indent_str}{key}: {'true' if value else 'false'}")
            else:
                lines.append(f"{indent_str}{key}: {value}")

        return "\n".join(lines)


class FrontmatterParser:
    """
    YAML frontmatter 解析器

    提供 YAML frontmatter 的解析功能。

    Examples:
        >>> parser = FrontmatterParser()
        >>> content = "---\\ntags: [test]\\n---\\n正文"
        >>> fm = parser.parse(content)
        >>> print(fm.metadata)
        {'tags': ['test']}
    """

    # Frontmatter 模式
    FRONTMATTER_PATTERN = r'^---\s*\n(.*?)\n---\s*\n(.*)$'

    @classmethod
    def parse(cls, content: str) -> Frontmatter:
        """
        解析 frontmatter

        Args:
            content: Markdown 内容

        Returns:
            Frontmatter: 解析后的 frontmatter 对象

        Examples:
            >>> parser = FrontmatterParser()
            >>> fm = parser.parse("---\\ntags: [test]\\n---\\n正文")
            >>> fm.get_tags()
            ['test']
        """
        match = re.match(cls.FRONTMATTER_PATTERN, content, re.DOTALL | re.MULTILINE)

        if match:
            yaml_content = match.group(1)
            body_content = match.group(2)
            metadata = cls._parse_yaml(yaml_content)
            return Frontmatter(yaml_content, metadata, body_content)

        # 没有 frontmatter
        return Frontmatter("", {}, content)

    @staticmethod
    def _parse_yaml(yaml_content: str) -> Dict[str, Any]:
        """
        解析 YAML 内容

        Args:
            yaml_content: YAML 字符串

        Returns:
            Dict: 解析后的字典
        """
        if HAS_YAML:
            try:
                return yaml.safe_load(yaml_content) or {}
            except Exception as e:
                print(f"警告: YAML 解析失败: {e}")
                return {}

        # 简单的解析器（不依赖 PyYAML）
        return FrontmatterParser._simple_yaml_parse(yaml_content)

    @staticmethod
    def _simple_yaml_parse(yaml_content: str) -> Dict[str, Any]:
        """
        简单的 YAML 解析器（基础功能）

        Args:
            yaml_content: YAML 字符串

        Returns:
            Dict: 解析后的字典
        """
        result = {}
        for line in yaml_content.split('\n'):
            line = line.strip()
            if not line or line.startswith('#'):
                continue

            if ':' in line:
                key, value = line.split(':', 1)
                key = key.strip()
                value = value.strip()

                # 处理列表
                if value.startswith('[') and value.endswith(']'):
                    value = [v.strip().strip('"\'') for v in value[1:-1].split(',')]
                # 处理布尔值
                elif value.lower() == 'true':
                    value = True
                elif value.lower() == 'false':
                    value = False
                # 处理空值
                elif value == 'null' or value == '~':
                    value = None

                result[key] = value

        return result


if __name__ == "__main__":
    # 测试代码
    print("测试 Frontmatter 模块...")

    # 测试解析
    test_content = """---
tags: [AI, Python, Test]
status: TODO
update: 2026-01-25
---
这是正文内容
"""

    parser = FrontmatterParser()
    fm = parser.parse(test_content)

    print("\n=== 解析结果 ===")
    print(f"标签: {fm.get_tags()}")
    print(f"状态: {fm.get('status')}")
    print(f"更新日期: {fm.get('update')}")
    print(f"正文: {fm.body.strip()}")

    # 测试标签操作
    print("\n=== 标签操作 ===")
    fm.add_tag("NewTag")
    print(f"添加标签后: {fm.get_tags()}")

    fm.remove_tag("Test")
    print(f"删除标签后: {fm.get_tags()}")

    print(f"是否包含 'AI': {fm.has_tag('AI')}")

    # 测试序列化
    print("\n=== 序列化 ===")
    print(fm.to_string())

    print("\n✓ Frontmatter 模块工作正常")
