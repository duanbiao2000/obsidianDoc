#!/usr/bin/env python3
"""
链接完整性分析脚本
分析 vault 中的单向链接情况
"""
import os
import re
from pathlib import Path
from collections import defaultdict
import json

def extract_links_from_file(file_path):
    """从文件中提取所有 wiki-links"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        # 匹配 [[...]] 格式的链接
        links = re.findall(r'\[\[([^\]]+)\]', content)
        # 处理别名格式 [[链接|别名]]
        clean_links = []
        for link in links:
            if '|' in link:
                link = link.split('|')[0]
            clean_links.append(link)
        return clean_links
    except:
        return []

def get_all_md_files(root_dir):
    """获取所有 markdown 文件"""
    md_files = []
    for root, dirs, files in os.walk(root_dir):
        # 跳过隐藏目录和特定目录
        dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ['.trash', 'node_modules', '.git']]
        for file in files:
            if file.endswith('.md') and not file.startswith('_Index'):
                md_files.append(os.path.join(root, file))
    return md_files

def get_note_title(file_path):
    """从文件路径提取笔记标题"""
    # 移除 .md 扩展名
    title = Path(file_path).stem
    # 尝试从文件内容中提取 YAML frontmatter 中的 title
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            first_lines = f.read(500)
            if first_lines.startswith('---'):
                yaml_match = re.search(r'title:\s*(.+)', first_lines)
                if yaml_match:
                    return yaml_match.group(1).strip()
    except:
        pass
    return title

def build_link_index(vault_path):
    """构建链接索引"""
    print(f"扫描目录: {vault_path}")

    md_files = get_all_md_files(vault_path)
    print(f"找到 {len(md_files)} 个 markdown 文件")

    # 构建文件名到文件路径的映射
    filename_to_path = {}
    file_to_title = {}
    for file_path in md_files:
        title = get_note_title(file_path)
        filename_to_path[title] = file_path
        file_to_title[file_path] = title

    # 分析所有文件的链接
    out_links = defaultdict(set)  # 文件 -> 出链
    in_links = defaultdict(set)   # 文件 -> 入链

    for file_path in md_files:
        links = extract_links_from_file(file_path)
        source_title = file_to_title[file_path]

        for link in links:
            # 只统计存在于 vault 中的链接
            if link in filename_to_path:
                out_links[source_title].add(link)
                in_links[link].add(source_title)

    # 找出单向链接
    one_way_links = []
    for source, targets in out_links.items():
        for target in targets:
            if source not in in_links[target]:
                one_way_links.append({
                    'source': source,
                    'target': target,
                    'source_file': filename_to_path.get(source),
                    'target_file': filename_to_path.get(target)
                })

    return {
        'total_files': len(md_files),
        'one_way_links': one_way_links,
        'out_links_count': sum(len(links) for links in out_links.values()),
        'in_links_count': sum(len(links) for links in in_links.values())
    }

if __name__ == '__main__':
    # 分析整个 vault
    vault_path = r'd:\迅雷下载\@同步文件\OneDrive\obsidianDoc'
    result = build_link_index(vault_path)

    print(f"\n=== 链接分析结果 ===")
    print(f"总文件数: {result['total_files']}")
    print(f"单向链接数: {len(result['one_way_links'])}")
    print(f"总出链数: {result['out_links_count']}")
    print(f"总入链数: {result['in_links_count']}")

    print(f"\n=== 单向链接列表 (前30个) ===")
    for i, link in enumerate(result['one_way_links'][:30], 1):
        print(f"{i}. {link['source']} -> {link['target']}")
        if link['source_file']:
            print(f"   源: {Path(link['source_file']).relative_to(vault_path)}")
        if link['target_file']:
            print(f"   目标: {Path(link['target_file']).relative_to(vault_path)}")

    # 保存结果到 JSON
    output_file = r'd:\迅雷下载\@同步文件\OneDrive\obsidianDoc\5.Misc\Scripts\link_analysis_result.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    print(f"\n详细结果已保存到: {output_file}")
