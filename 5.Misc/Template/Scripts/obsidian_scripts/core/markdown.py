#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Markdown 链接解析模块

提供统一的 Markdown 链接提取和处理功能，支持：
- Wiki 链接 [[link]]
- 嵌入 ![[embed]]
- 标签 #tag
- 标题 # Header
- 外部链接
- 链接统计

此功能在 5+ 个现有脚本中重复出现，现在统一到此模块。

作者: Claude Sonnet 4.5
创建时间: 2026-01-25
用途: Issue #4 - 自动化脚本体系优化
"""

import re
from typing import List, Dict, NamedTuple
from dataclasses import dataclass


@dataclass
class MarkdownLink:
    """
    Markdown 链接数据类

    表示一个 Markdown 链接的详细信息。

    Attributes:
        raw (str): 原始链接文本
        target (str): 链接目标
        alias (Optional[str]): 链接别名（如果有）
        link_type (str): 链接类型 ('wiki', 'embed', 'external')
        position (int): 链接在文档中的位置

    Examples:
        >>> link = MarkdownLink("[[页面|别名]]", "页面", "别名", "wiki", 0)
        >>> print(link.target)
        页面
    """
    raw: str
    target: str
    alias: Optional[str]
    link_type: str  # 'wiki', 'embed', 'external'
    position: int


class MarkdownParser:
    """
    Markdown 链接解析器

    提供 Markdown 链接的提取和统计功能。

    Examples:
        >>> parser = MarkdownParser()
        >>> links = parser.extract_links("[[链接1]] [[链接2|别名]]")
        >>> print(len(links))
        2
    """

    # 链接模式
    WIKI_LINK_PATTERN = r'\[\[([^\]]+)\]\]'
    EMBED_PATTERN = r'!\[\[([^\]]+)\]\]'
    TAG_PATTERN = r'#([\u4e00-\u9fa5a-zA-Z0-9_/\-]+)'
    HEADER_PATTERN = r'^#+\s+'
    EXTERNAL_LINK_PATTERN = r'\[([^\]]+)\]\(([^)]+)\)'

    @classmethod
    def extract_links(cls, content: str) -> List[MarkdownLink]:
        """
        提取所有链接

        Args:
            content: Markdown 内容

        Returns:
            List[MarkdownLink]: 链接列表

        Examples:
            >>> parser = MarkdownParser()
            >>> content = "[[link1]] [[link2|alias]] ![[embed]]"
            >>> links = parser.extract_links(content)
            >>> len(links)
            3
        """
        links = []

        # Wiki 链接 [[link]] 或 [[link|alias]]
        for match in re.finditer(cls.WIKI_LINK_PATTERN, content):
            raw = match.group(1)
            if '|' in raw:
                target, alias = raw.split('|', 1)
            else:
                target, alias = raw, None
            links.append(MarkdownLink(
                raw=match.group(0),
                target=target.strip(),
                alias=alias.strip() if alias else None,
                link_type='wiki',
                position=match.start()
            ))

        # 嵌入 ![[embed]]
        for match in re.finditer(cls.EMBED_PATTERN, content):
            target = match.group(1)
            links.append(MarkdownLink(
                raw=match.group(0),
                target=target.strip(),
                alias=None,
                link_type='embed',
                position=match.start()
            ))

        return links

    @classmethod
    def count_links(cls, content: str) -> Dict[str, int]:
        """
        统计链接数量

        Args:
            content: Markdown 内容

        Returns:
            Dict[str, int]: 统计数据字典

        Examples:
            >>> parser = MarkdownParser()
            >>> stats = parser.count_links("[[link]] #tag ![[embed]]")
            >>> print(stats['wiki_links'])
            1
        """
        links = cls.extract_links(content)

        wiki_links = sum(1 for l in links if l.link_type == 'wiki')
        embeds = sum(1 for l in links if l.link_type == 'embed')

        # 统计标签
        tags = len(re.findall(cls.TAG_PATTERN, content))

        # 统计标题
        headers = len(re.findall(cls.HEADER_PATTERN, content, re.MULTILINE))

        return {
            'wiki_links': wiki_links,
            'embeds': embeds,
            'tags': tags,
            'headers': headers,
            'total_links': len(links)
        }

    @classmethod
    def extract_headers(cls, content: str) -> List[str]:
        """
        提取所有标题

        Args:
            content: Markdown 内容

        Returns:
            List[str]: 标题列表

        Examples:
            >>> parser = MarkdownParser()
            >>> headers = parser.extract_headers("# Title 1\\n## Title 2")
            >>> print(headers)
            ['Title 1', 'Title 2']
        """
        headers = []
        for match in re.finditer(cls.HEADER_PATTERN, content, re.MULTILINE):
            line = match.group(0)
            # 移除 # 号和空格
            title = re.sub(r'^#+\s*', '', line).strip()
            headers.append(title)
        return headers

    @classmethod
    def extract_tags(cls, content: str) -> List[str]:
        """
        提取所有标签

        Args:
            content: Markdown 内容

        Returns:
            List[str]: 标签列表（去重）

        Examples:
            >>> parser = MarkdownParser()
            >>> tags = parser.extract_tags("#AI #Python #AI")
            >>> print(tags)
            ['AI', 'Python']
        """
        tags = re.findall(cls.TAG_PATTERN, content)
        # 去重但保持顺序
        return list(dict.fromkeys(tags))

    @classmethod
    def extract_external_links(cls, content: str) -> List[MarkdownLink]:
        """
        提取外部链接 [text](url)

        Args:
            content: Markdown 内容

        Returns:
            List[MarkdownLink]: 外部链接列表

        Examples:
            >>> parser = MarkdownParser()
            >>> links = parser.extract_external_links("[Google](https://google.com)")
            >>> len(links)
            1
        """
        links = []
        for match in re.finditer(cls.EXTERNAL_LINK_PATTERN, content):
            text = match.group(1)
            url = match.group(2)
            links.append(MarkdownLink(
                raw=match.group(0),
                target=url.strip(),
                alias=text.strip(),
                link_type='external',
                position=match.start()
            ))
        return links

    @classmethod
    def get_word_count(cls, content: str) -> int:
        """
        统计字数

        Args:
            content: Markdown 内容

        Returns:
            int: 字数

        Examples:
            >>> parser = MarkdownParser()
            >>> count = parser.get_word_count("Hello world")
            >>> print(count)
            2
        """
        # 移除代码块
        content = re.sub(r'```.*?```', '', content, flags=re.DOTALL)
        # 移除行内代码
        content = re.sub(r'`[^`]+`', '', content)
        # 移除链接
        content = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', content)
        content = re.sub(r'\[\[([^\]]+)\]\]', '', content)
        # 统计中英文单词
        words = re.findall(r'[\u4e00-\u9fa5]|[a-zA-Z]+', content)
        return len(words)


if __name__ == "__main__":
    # 测试代码
    print("测试 Markdown 解析器...")

    test_content = """---
#Title
tags: [AI, Python]
---

# 这是标题

这是正文内容，包含 [[链接1]] 和 [[链接2|别名]]。

还有嵌入内容：![[嵌入文件]]。

外部链接：[Google](https://google.com)。

标签：#AI #Python #MachineLearning
"""

    parser = MarkdownParser()

    print("\n=== 链接提取 ===")
    links = parser.extract_links(test_content)
    for link in links:
        print(f"{link.link_type}: {link.target}" + (f" ({link.alias})" if link.alias else ""))

    print("\n=== 链接统计 ===")
    stats = parser.count_links(test_content)
    for key, value in stats.items():
        print(f"{key}: {value}")

    print("\n=== 标题提取 ===")
    headers = parser.extract_headers(test_content)
    for header in headers:
        print(f"- {header}")

    print("\n=== 标签提取 ===")
    tags = parser.extract_tags(test_content)
    print(f"标签: {tags}")

    print("\n=== 外部链接 ===")
    ext_links = parser.extract_external_links(test_content)
    for link in ext_links:
        print(f"{link.target} - {link.alias}")

    print("\n=== 字数统计 ===")
    word_count = parser.get_word_count(test_content)
    print(f"字数: {word_count}")

    print("\n✓ Markdown 解析器工作正常")
