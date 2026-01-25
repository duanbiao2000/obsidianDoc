#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
智能链接添加脚本 - 为孤立笔记添加相关链接
GitHub Issue #2: 孤立笔记链接密度提升计划

功能:
- 自动为孤立笔记添加向上链接(父级索引)
- 基于文件名和路径智能匹配相关主题
- 为低连通性笔记添加额外链接
"""

import re
import sys
from pathlib import Path
from collections import defaultdict

# Windows 编码支持
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

VAULT_ROOT = Path(r"d:\迅雷下载\@同步文件\OneDrive\obsidianDoc")

# 主题关键词映射表
TOPIC_KEYWORDS = {
    # AI相关
    'ai': ['2.Topics/03.内容创作/AI',
           '3.Resources/Prompt工程/README.md'],

    # 编程语言
    'python': ['2.Topics/01.技术栈/Coding/04-语言指南'],
    'javascript': ['2.Topics/01.技术栈/Coding/04-语言指南'],
    'java': ['2.Topics/01.技术栈/Coding/04-语言指南',
             '1.Projects/技术能力晋升/02.学习路径/如何快速成长为生产级Java后端开发者.md'],
    'rust': ['2.Topics/01.技术栈/Coding/04-语言指南'],
    'go': ['2.Topics/01.技术栈/Coding/04-语言指南'],

    # 系统设计
    '系统设计|system.*design|architecture': [
        '2.Topics/01.技术栈/Coding/03-系统设计/系统架构完全指南.md',
        '2.Topics/01.技术栈/Coding/03-系统设计集.md'
    ],
    '微服务|microservice': [
        '2.Topics/01.技术栈/Coding/03-系统设计/微服务架构完全指南.md'
    ],

    # 数据库
    '数据库|database': [
        '2.Topics/01.技术栈/系统构建/02-后端工程实践/数据库与存储.md'
    ],

    # API
    'api|rest|graphql': [
        '2.Topics/01.技术栈/Coding/API开发集.md'
    ],

    # 测试
    '测试|test': [
        '2.Topics/01.技术栈/Coding/02-工程实践/测试最佳实践.md'
    ],

    # DevOps
    'docker|kubernetes|devops|cicd': [
        '2.Topics/01.技术栈/系统构建/03-运维实践集.md'
    ],

    # Git
    'git': [
        '2.Topics/01.技术栈/Coding/01-Git集.md'
    ],

    # IELTS/英语
    'ielts|雅思': [
        '2.Topics/06.语言与移民/英语/IELTS/雅思口语知识库.md',
        '2.Topics/06.语言与移民/英语/IELTS/IELTS大作文命题框架与策略.md'
    ],

    # 职业发展
    '职业|career|job|求职': [
        '2.Topics/04.职业发展/行业洞察',
        '1.Projects/技术能力晋升'
    ],

    # 内容创作
    'writing|写作|内容创作': [
        '2.Topics/03.内容创作/Writing'
    ],

    # 认知系统
    '思维|mental|认知|cognitive': [
        '2.Topics/02.认知系统/思维模型',
        '2.Topics/02.认知系统'
    ],

    # 学习方法
    '学习|learn|study': [
        '2.Topics/02.认知系统/学习系统'
    ],
}

def find_parent_indexes(file_path: Path) -> list:
    """查找父级索引文件"""

    indexes = []
    relative_path = file_path.relative_to(VAULT_ROOT)
    parts = relative_path.parts

    # 查找各级目录的_Index文件
    for i in range(len(parts) - 1, 0, -1):
        parent_dir = VAULT_ROOT.joinpath(*parts[:i])
        index_files = list(parent_dir.glob("_Index_of_*.md"))

        if index_files:
            for idx in index_files:
                rel_path = idx.relative_to(VAULT_ROOT)
                indexes.append(f"[[{rel_path}|{idx.stem.replace('_Index_of_', '')}]]")

    return indexes

def find_related_topics(file_path: Path) -> list:
    """基于文件名和路径查找相关主题"""

    related = []
    filename = file_path.name.lower()
    path_str = str(file_path).lower()

    for keyword, topic_paths in TOPIC_KEYWORDS.items():
        # 检查文件名或路径是否包含关键词
        if re.search(keyword, filename) or re.search(keyword, path_str):
            for topic_path in topic_paths:
                topic_file = VAULT_ROOT / topic_path
                if topic_file.exists():
                    rel_path = topic_file.relative_to(VAULT_ROOT)
                    related.append(f"[[{rel_path}]]")
                elif '/' in topic_path:
                    # 目录路径
                    rel_path = topic_path
                    display = topic_path.split('/')[-2] if topic_path.split('/')[-2] else topic_path
                    related.append(f"[[{rel_path}|{display}]]")

    return related

def add_links_to_file(file_path: Path) -> bool:
    """为单个文件添加智能链接"""

    try:
        content = file_path.read_text(encoding='utf-8')

        # 检查是否已经有相关链接部分
        if '## 🔗 相关链接' in content or '## 相关链接' in content:
            return False

        # 查找父级索引
        parent_indexes = find_parent_indexes(file_path)

        # 查找相关主题
        related_topics = find_related_topics(file_path)

        # 如果没有找到任何链接,跳过
        if not parent_indexes and not related_topics:
            return False

        # 构建链接部分
        links_section = "## 🔗 相关链接\n\n"

        # 添加父级索引链接
        if parent_indexes:
            links_section += "**上级索引**:\n"
            for idx in parent_indexes[:3]:  # 最多3个
                links_section += f"- {idx}\n"
            links_section += "\n"

        # 添加相关主题链接
        if related_topics:
            links_section += "**相关主题**:\n"
            for topic in related_topics[:5]:  # 最多5个
                links_section += f"- {topic}\n"
            links_section += "\n"

        links_section += "---\n\n"

        # 在YAML frontmatter之后插入
        yaml_pattern = r'^---\s*\n(.*?)\n---\s*\n'
        yaml_match = re.match(yaml_pattern, content, re.DOTALL)

        if yaml_match:
            yaml_end = yaml_match.end()
            new_content = content[:yaml_end] + '\n' + links_section + content[yaml_end:]
        else:
            # 没有YAML,直接在开头添加
            new_content = links_section + content

        # 写回文件
        file_path.write_text(new_content, encoding='utf-8')
        return True

    except Exception as e:
        print(f"  ✗ {file_path.name} - 错误: {e}")
        return False

def main():
    """主函数"""
    import argparse

    parser = argparse.ArgumentParser(
        description="智能链接添加脚本 - 为孤立笔记添加相关链接"
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='预览模式,不修改文件'
    )
    parser.add_argument(
        '--directory',
        type=str,
        help='只处理指定目录(如: 2.Topics, 3.Resources)'
    )

    args = parser.parse_args()

    print("=" * 70)
    print("智能链接添加工具")
    print("=" * 70)
    print(f"模式: {'预览(不修改文件)' if args.dry_run else '执行模式'}")
    if args.directory:
        print(f"目录: {args.directory}")
    print("=" * 70)
    print()

    # 读取孤立笔记清单
    orphan_list_file = VAULT_ROOT / "孤立笔记清单_20260125_142549.md"

    if not orphan_list_file.exists():
        print("✗ 孤立笔记清单文件不存在!")
        print("  请先运行 find_orphan_notes.py 生成清单")
        return

    # 从清单中提取孤立笔记路径
    orphan_files = []
    with open(orphan_list_file, 'r', encoding='utf-8') as f:
        content = f.read()
        # 提取markdown链接中的路径
        matches = re.findall(r'\[([^\]]+)\]\(([^)]+\.md)\)', content)
        for display, path in matches:
            file_path = VAULT_ROOT / path.replace('\\', '/')
            if args.directory:
                if args.directory in str(file_path):
                    orphan_files.append(file_path)
            else:
                orphan_files.append(file_path)

    # 过滤掉已处理的Projects和Atlas
    orphan_files = [f for f in orphan_files
                    if '1.Projects' not in str(f)
                    and 'Atlas' not in str(f)]

    print(f"📊 找到 {len(orphan_files)} 个待处理的孤立笔记")
    print()

    processed = 0
    skipped = 0
    failed = 0

    for i, file_path in enumerate(orphan_files, 1):
        if not file_path.exists():
            skipped += 1
            continue

        rel_path = file_path.relative_to(VAULT_ROOT)
        print(f"[{i}/{len(orphan_files)}] {rel_path}")

        if args.dry_run:
            # 预览模式:只显示会添加哪些链接
            parent_indexes = find_parent_indexes(file_path)
            related_topics = find_related_topics(file_path)

            if parent_indexes:
                print(f"  上级索引: {len(parent_indexes)} 个")
            if related_topics:
                print(f"  相关主题: {len(related_topics)} 个")

            if parent_indexes or related_topics:
                processed += 1
            else:
                print(f"  ⊙ 未找到相关链接")
                skipped += 1
        else:
            # 执行模式:实际添加链接
            if add_links_to_file(file_path):
                processed += 1
            else:
                skipped += 1

    print()
    print("=" * 70)
    print("✅ 处理完成!")
    print(f"  处理成功: {processed} 个")
    print(f"  跳过: {skipped} 个")
    print(f"  失败: {failed} 个")
    print("=" * 70)

    if not args.dry_run:
        print()
        print("💡 建议: 运行 git diff 查看修改内容")

if __name__ == "__main__":
    main()
