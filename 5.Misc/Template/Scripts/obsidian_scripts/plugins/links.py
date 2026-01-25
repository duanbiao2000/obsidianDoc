#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
链接分析插件

提供统一的链接分析功能，整合了所有链接相关脚本的功能：
- 查找孤立笔记
- 分析链接连通性
- 查找低连通性笔记

作者: Claude Sonnet 4.5
创建时间: 2026-01-25
相关: Issue #4 - 自动化脚本体系优化
"""

from pathlib import Path
from typing import Dict, List, Optional
from dataclasses import dataclass
from collections import defaultdict
from datetime import datetime

from ..core.config import Config
from ..core.file_utils import FileScanner
from ..core.markdown import MarkdownParser


@dataclass
class LinkAnalysis:
    """
    链接分析结果数据类

    Attributes:
        filepath (Path): 文件路径
        wiki_links (int): Wiki 链接数量
        embeds (int): 嵌入数量
        tags (int): 标签数量
        headers (int): 标题数量
        total_links (int): 总链接数量

    Examples:
        >>> analysis = LinkAnalysis(Path("note.md"), 5, 2, 3, 2, 7)
        >>> print(analysis.total_links)
        7
    """
    filepath: Path
    wiki_links: int
    embeds: int
    tags: int
    headers: int
    total_links: int


class LinkAnalyzer:
    """
    链接分析器

    整合所有链接分析功能，提供统一的接口。

    Attributes:
        config (Config): 配置对象
        file_scanner (FileScanner): 文件扫描器

    Examples:
        >>> analyzer = LinkAnalyzer()
        >>> orphans = analyzer.find_orphan_notes()
        >>> print(f"找到 {len(orphans)} 个孤立笔记")
    """

    def __init__(self, config: Optional[Config] = None):
        """
        初始化链接分析器

        Args:
            config: 配置对象（如果为 None，使用默认配置）
        """
        self.config = config or Config()
        self.file_scanner = FileScanner(
            self.config.vault_root,
            self.config.include_dirs
        )

    def find_orphan_notes(
        self,
        link_threshold: int = 0,
        output_file: Optional[Path] = None
    ) -> List[LinkAnalysis]:
        """
        查找孤立笔记

        孤立笔记定义为：链接总数 <= link_threshold 的笔记

        Args:
            link_threshold: 链接阈值（默认 0）
            output_file: 输出文件路径（可选）

        Returns:
            List[LinkAnalysis]: 孤立笔记列表

        Examples:
            >>> analyzer = LinkAnalyzer()
            >>> orphans = analyzer.find_orphan_notes(threshold=0)
            >>> for orphan in orphans:
            ...     print(orphan.filepath.name)
        """
        orphans = []

        for filepath in self.file_scanner.scan_markdown_files():
            try:
                content = filepath.read_text(encoding='utf-8')
                link_counts = MarkdownParser.count_links(content)

                if link_counts['total_links'] <= link_threshold:
                    orphans.append(LinkAnalysis(
                        filepath=filepath,
                        **link_counts
                    ))
            except Exception as e:
                print(f"警告: 无法分析 {filepath.name}: {e}")

        # 保存结果
        if output_file and orphans:
            self._save_orphans_report(orphans, output_file, link_threshold)

        return orphans

    def analyze_connectivity(self) -> Dict[str, Dict]:
        """
        分析链接连通性

        构建整个 vault 的链接图谱，统计每个笔记的：
        - 入链接（in_links）：有多少其他笔记链接到这里
        - 出链接（out_links）：这个笔记链接到多少其他笔记

        Args:
            None

        Returns:
            Dict[str, Dict]: 链接图谱
                {
                    "笔记标题": {
                        "in_links": set([...]),  # 链接到此笔记的其他笔记
                        "out_links": set([...])  # 此笔记链接到的其他笔记
                    }
                }

        Examples:
            >>> analyzer = LinkAnalyzer()
            >>> connectivity = analyzer.analyze_connectivity()
            >>> for title, links in connectivity.items():
            ...     print(f"{title}: {len(links['in_links'])} in, {len(links['out_links'])} out")
        """
        link_map = defaultdict(lambda: {'in_links': set(), 'out_links': set()})

        for filepath in self.file_scanner.scan_markdown_files():
            try:
                content = filepath.read_text(encoding='utf-8')
                links = MarkdownParser.extract_links(content)

                source_title = filepath.stem
                for link in links:
                    if link.link_type in ['wiki', 'embed']:
                        target = link.target
                        link_map[source_title]['out_links'].add(target)
                        link_map[target]['in_links'].add(source_title)
            except Exception as e:
                print(f"警告: 无法分析 {filepath.name}: {e}")

        return dict(link_map)

    def find_low_connectivity(
        self,
        min_links: int = 1,
        max_links: int = 2
    ) -> List[LinkAnalysis]:
        """
        查找低连通性笔记

        低连通性笔记定义为：链接数量在 min_links 和 max_links 之间

        Args:
            min_links: 最小链接数
            max_links: 最大链接数

        Returns:
            List[LinkAnalysis]: 低连通性笔记列表

        Examples:
            >>> analyzer = LinkAnalyzer()
            >>> low_conn = analyzer.find_low_connectivity(min_links=1, max_links=2)
            >>> print(f"找到 {len(low_conn)} 个低连通性笔记")
        """
        low_conn = []

        for filepath in self.file_scanner.scan_markdown_files():
            try:
                content = filepath.read_text(encoding='utf-8')
                link_counts = MarkdownParser.count_links(content)

                if min_links <= link_counts['total_links'] <= max_links:
                    low_conn.append(LinkAnalysis(
                        filepath=filepath,
                        **link_counts
                    ))
            except Exception as e:
                print(f"警告: 无法分析 {filepath.name}: {e}")

        return low_conn

    def get_link_density_stats(self) -> Dict[str, int]:
        """
        获取链接密度统计

        返回整个 vault 的链接密度分布统计。

        Returns:
            Dict[str, int]: 统计数据
                - total_files: 总文件数
                - total_links: 总链接数
                - avg_links_per_file: 平均每文件链接数
                - orphan_count: 孤立笔记数
                - low_connectivity_count: 低连通性笔记数
                - high_connectivity_count: 高连通性笔记数（>2个链接）

        Examples:
            >>> analyzer = LinkAnalyzer()
            >>> stats = analyzer.get_link_density_stats()
            >>> print(f"平均链接密度: {stats['avg_links_per_file']:.2f}")
        """
        total_files = 0
        total_links = 0
        orphan_count = 0
        low_connectivity_count = 0
        high_connectivity_count = 0

        for filepath in self.file_scanner.scan_markdown_files():
            try:
                content = filepath.read_text(encoding='utf-8')
                link_counts = MarkdownParser.count_links(content)

                total_files += 1
                total_links += link_counts['total_links']

                if link_counts['total_links'] == 0:
                    orphan_count += 1
                elif link_counts['total_links'] <= 2:
                    low_connectivity_count += 1
                else:
                    high_connectivity_count += 1

            except Exception as e:
                print(f"警告: 无法分析 {filepath.name}: {e}")

        avg_links = total_links / total_files if total_files > 0 else 0

        return {
            'total_files': total_files,
            'total_links': total_links,
            'avg_links_per_file': round(avg_links, 2),
            'orphan_count': orphan_count,
            'low_connectivity_count': low_connectivity_count,
            'high_connectivity_count': high_connectivity_count
        }

    def _save_orphans_report(
        self,
        orphans: List[LinkAnalysis],
        output_file: Path,
        threshold: int
    ) -> None:
        """
        保存孤立笔记报告

        Args:
            orphans: 孤立笔记列表
            output_file: 输出文件路径
            threshold: 链接阈值
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        report = f"""# 孤立笔记清单

生成时间: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
阈值: 链接数 <= {threshold}
总计: {len(orphans)} 个文件

---

## 孤立笔记列表

"""

        for orphan in orphans:
            relative_path = orphan.filepath.relative_to(self.config.vault_root)
            report += f"### {relative_path}\n\n"
            report += f"- **Wiki链接**: {orphan.wiki_links}\n"
            report += f"- **嵌入**: {orphan.embeds}\n"
            report += f"- **标签**: {orphan.tags}\n"
            report += f"- **标题**: {orphan.headers}\n"
            report += f"- **总链接数**: {orphan.total_links}\n\n"

        output_file.write_text(report, encoding='utf-8')


if __name__ == "__main__":
    # 测试代码
    from ..core.encoding import auto_setup
    auto_setup()

    print("测试链接分析器...")

    analyzer = LinkAnalyzer()

    print(f"\n=== 链接密度统计 ===")
    stats = analyzer.get_link_density_stats()
    for key, value in stats.items():
        print(f"{key}: {value}")

    print(f"\n=== 查找孤立笔记 (threshold=0) ===")
    orphans = analyzer.find_orphan_notes(link_threshold=0)
    print(f"找到 {len(orphans)} 个孤立笔记")
    if orphans:
        print(f"前 5 个:")
        for orphan in orphans[:5]:
            print(f"  {orphan.filepath.name} ({orphan.total_links} 链接)")

    print(f"\n=== 查找低连通性笔记 (1-2 链接) ===")
    low_conn = analyzer.find_low_connectivity(min_links=1, max_links=2)
    print(f"找到 {len(low_conn)} 个低连通性笔记")

    print("\n✓ 链接分析器工作正常")
