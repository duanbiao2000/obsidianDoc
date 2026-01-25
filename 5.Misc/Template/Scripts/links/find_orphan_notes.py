#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
孤立笔记识别与分析脚本
GitHub Issue #2: 孤立笔记链接密度提升计划

识别没有任何wiki链接的笔记,并按目录和重要性分类
"""

import re
import sys
from pathlib import Path
from collections import defaultdict
from datetime import datetime

# Windows 编码支持
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

# 笔记目录列表
NOTE_DIRECTORIES = [
    "0.DailyNotes",
    "1.Projects",
    "2.Topics",
    "3.Resources",
    "4.Archives",
    "5.Misc",
    "6.Calendar",
    "Atlas",
]

def count_links(content: str) -> dict:
    """
    统计笔记中的链接数量

    Args:
        content: 文件内容

    Returns:
        {
            'wiki_links': int,      # [[wiki-links]] 数量
            'embeds': int,          # ![[embeds]] 数量
            'headers': int,         # # 标题数量
            'tags': int,            # #标签 数量
            'total_links': int      # 总链接数
        }
    """
    # 统计wiki链接 [[link]]
    wiki_links = len(re.findall(r'\[\[([^\]]+)\]\]', content))

    # 统计嵌入 ![[embed]]
    embeds = len(re.findall(r'!\[\[([^\]]+)\]\]', content))

    # 统计标签 #tag
    tags = len(re.findall(r'#\w+', content))

    # 统计标题
    headers = len(re.findall(r'^#+\s+', content, re.MULTILINE))

    return {
        'wiki_links': wiki_links,
        'embeds': embeds,
        'tags': tags,
        'headers': headers,
        'total_links': wiki_links + embeds,
    }

def analyze_orphan_notes():
    """分析所有笔记,识别孤立笔记"""

    vault_root = Path(r"d:\迅雷下载\@同步文件\OneDrive\obsidianDoc")

    print("=" * 70)
    print("孤立笔记识别与分析工具")
    print("=" * 70)
    print(f"扫描根目录: {vault_root}")
    print("=" * 70)
    print()

    # 统计数据
    total_files = 0
    orphan_files = []  # 完全孤立的文件(没有任何链接)
    low_connectivity_files = []  # 低连通性文件(1-2个链接)
    directory_stats = defaultdict(lambda: {'total': 0, 'orphans': 0})

    # 扫描所有笔记目录
    for directory in NOTE_DIRECTORIES:
        dir_path = vault_root / directory
        if not dir_path.exists():
            print(f"⊙ 跳过不存在的目录: {directory}")
            continue

        print(f"🔍 扫描目录: {directory}/")

        # 查找所有Markdown文件
        for md_file in dir_path.rglob("*.md"):
            # 跳过隐藏文件
            if md_file.name.startswith('.'):
                continue

            total_files += 1
            directory_stats[directory]['total'] += 1

            try:
                content = md_file.read_text(encoding='utf-8')
                links = count_links(content)

                # 判断是否为孤立笔记(没有wiki链接和嵌入)
                if links['total_links'] == 0:
                    orphan_files.append({
                        'path': md_file.relative_to(vault_root),
                        'directory': directory,
                        'links': links,
                    })
                    directory_stats[directory]['orphans'] += 1

                # 判断是否为低连通性笔记(1-2个链接)
                elif links['total_links'] <= 2:
                    low_connectivity_files.append({
                        'path': md_file.relative_to(vault_root),
                        'directory': directory,
                        'links': links,
                    })

            except Exception as e:
                print(f"  ✗ 错误读取文件 {md_file.name}: {e}")

    # 打印统计信息
    print()
    print("=" * 70)
    print("📊 统计结果:")
    print("=" * 70)
    print(f"总文件数: {total_files}")
    print(f"孤立笔记(0个链接): {len(orphan_files)} ({len(orphan_files)/total_files*100:.1f}%)")
    print(f"低连通性笔记(1-2个链接): {len(low_connectivity_files)} ({len(low_connectivity_files)/total_files*100:.1f}%)")
    print(f"需要改进的笔记总数: {len(orphan_files) + len(low_connectivity_files)} ({(len(orphan_files) + len(low_connectivity_files))/total_files*100:.1f}%)")
    print()

    # 按目录统计
    print("📂 各目录孤立笔记统计:")
    print("-" * 70)
    priority_dirs = ["1.Projects", "2.Topics", "3.Resources", "4.Archives",
                     "0.DailyNotes", "5.Misc", "6.Calendar", "Atlas"]

    for directory in priority_dirs:
        if directory in directory_stats:
            stats = directory_stats[directory]
            orphan_rate = stats['orphans'] / stats['total'] * 100 if stats['total'] > 0 else 0
            print(f"  {directory:20s} | 总计: {stats['total']:4d} | 孤立: {stats['orphans']:4d} | 孤立率: {orphan_rate:5.1f}%")

    print()
    print("=" * 70)
    print("🔗 高优先级孤立笔记 (Projects目录):")
    print("-" * 70)

    # 列出Projects目录的孤立笔记(最高优先级)
    project_orphans = [f for f in orphan_files if f['directory'] == '1.Projects']
    if project_orphans:
        for orphan in project_orphans[:20]:  # 只显示前20个
            print(f"  • {orphan['path']}")
        if len(project_orphans) > 20:
            print(f"  ... 还有 {len(project_orphans) - 20} 个")
    else:
        print("  ✅ Projects目录没有孤立笔记!")

    print()
    print("=" * 70)
    print("🔗 Topics目录孤立笔记 (技术栈相关):")
    print("-" * 70)

    # 列出Topics/01.技术栈的孤立笔记(次高优先级)
    tech_orphans = [f for f in orphan_files if '2.Topics/01.技术栈' in str(f['path'])]
    if tech_orphans:
        for orphan in tech_orphans[:20]:
            print(f"  • {orphan['path']}")
        if len(tech_orphans) > 20:
            print(f"  ... 还有 {len(tech_orphans) - 20} 个")
    else:
        print("  ✅ 技术栈目录没有孤立笔记!")

    # 保存完整列表到文件
    print()
    print("=" * 70)
    print("💾 保存孤立笔记列表...")

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # 保存所有孤立笔记
    orphan_list_file = vault_root / f"孤立笔记清单_{timestamp}.md"
    with open(orphan_list_file, 'w', encoding='utf-8') as f:
        f.write(f"# 孤立笔记清单\n\n")
        f.write(f"**生成时间**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"**扫描文件**: {total_files} 个\n")
        f.write(f"**孤立笔记**: {len(orphan_files)} 个 ({len(orphan_files)/total_files*100:.1f}%)\n")
        f.write(f"**低连通性**: {len(low_connectivity_files)} 个 ({len(low_connectivity_files)/total_files*100:.1f}%)\n\n")

        f.write("## 按优先级分类\n\n")
        f.write("### 🔴 P0 - Projects目录(最高优先级)\n\n")
        project_orphans = [f for f in orphan_files if f['directory'] == '1.Projects']
        if project_orphans:
            for orphan in project_orphans:
                f.write(f"- [{orphan['path']}]({orphan['path']})\n")
        else:
            f.write("_无_\n")

        f.write("\n### 🟠 P1 - Topics/技术栈目录\n\n")
        tech_orphans = [f for f in orphan_files if '2.Topics/01.技术栈' in str(f['path'])]
        if tech_orphans:
            for orphan in tech_orphans:
                f.write(f"- [{orphan['path']}]({orphan['path']})\n")
        else:
            f.write("_无_\n")

        f.write("\n### 🟡 P2 - Topics其他目录\n\n")
        topic_orphans = [f for f in orphan_files if f['directory'] == '2.Topics' and '01.技术栈' not in str(f['path'])]
        if topic_orphans:
            for orphan in topic_orphans:
                f.write(f"- [{orphan['path']}]({orphan['path']})\n")
        else:
            f.write("_无_\n")

        f.write("\n### 🟢 P3 - Resources和Archives\n\n")
        resource_orphans = [f for f in orphan_files if f['directory'] in ['3.Resources', '4.Archives']]
        if resource_orphans:
            for orphan in resource_orphans:
                f.write(f"- [{orphan['path']}]({orphan['path']})\n")
        else:
            f.write("_无_\n")

        f.write("\n### ⚪ P4 - 其他目录\n\n")
        other_orphans = [f for f in orphan_files if f['directory'] not in ['1.Projects', '2.Topics', '3.Resources', '4.Archives']]
        if other_orphans:
            for orphan in other_orphans:
                f.write(f"- [{orphan['path']}]({orphan['path']})\n")
        else:
            f.write("_无_\n")

        f.write("\n## 完整清单\n\n")
        f.write("| 路径 | 目录 | Wiki链接 | 嵌入 | 标签 |\n")
        f.write("|------|------|----------|------|------|\n")
        for orphan in orphan_files:
            f.write(f"| {orphan['path']} | {orphan['directory']} | {orphan['links']['wiki_links']} | {orphan['links']['embeds']} | {orphan['links']['tags']} |\n")

    print(f"  ✅ 已保存到: {orphan_list_file.name}")

    # 保存低连通性笔记
    low_conn_list_file = vault_root / f"低连通性笔记清单_{timestamp}.md"
    with open(low_conn_list_file, 'w', encoding='utf-8') as f:
        f.write(f"# 低连通性笔记清单\n\n")
        f.write(f"**生成时间**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"**扫描文件**: {total_files} 个\n")
        f.write(f"**低连通性笔记(1-2个链接)**: {len(low_connectivity_files)} 个\n\n")

        f.write("## 完整清单\n\n")
        f.write("| 路径 | 目录 | 总链接数 | Wiki链接 | 嵌入 | 标签 |\n")
        f.write("|------|------|----------|----------|------|------|\n")
        for note in low_connectivity_files:
            f.write(f"| {note['path']} | {note['directory']} | {note['links']['total_links']} | {note['links']['wiki_links']} | {note['links']['embeds']} | {note['links']['tags']} |\n")

    print(f"  ✅ 已保存到: {low_conn_list_file.name}")
    print()

    print("=" * 70)
    print("✅ 分析完成!")
    print()
    print("下一步建议:")
    print("  1. 优先处理Projects目录的孤立笔记")
    print("  2. 为技术栈相关的孤立笔记添加索引链接")
    print("  3. 为低连通性笔记添加双向链接")
    print("  4. 使用Templater脚本自动添加基本链接")
    print("=" * 70)

if __name__ == "__main__":
    analyze_orphan_notes()
