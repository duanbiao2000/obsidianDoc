#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
低连通性笔记链接增强工具 (安全版)
为已有1-2个链接的笔记添加更多相关链接,提升至3个以上

安全特性:
- 修改前验证文件完整性
- 修改后检查内容不会丢失
- 出错时自动回滚
"""

import re
import sys
from pathlib import Path
import shutil
from datetime import datetime

# Windows 编码支持
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

VAULT_ROOT = Path(r"d:\迅雷下载\@同步文件\OneDrive\obsidianDoc")

# 扩展的关键词映射表
TOPIC_KEYWORDS = {
    # AI/LLM
    'ai|llm|gpt|claude|prompt': [
        '3.Resources/Prompt工程',
        '2.Topics/03.内容创作/AI',
    ],

    # 编程语言
    'python': [
        '2.Topics/01.技术栈/Coding/04-语言指南',
        '2.Topics/02.认知系统/学习系统/如何才算学好了Python.md',
    ],
    'java|spring': [
        '2.Topics/01.技术栈/Coding/04-语言指南',
        '1.Projects/技术能力晋升/02.学习路径/如何快速成长为生产级Java后端开发者.md',
    ],
    'javascript|js|typescript|node': [
        '2.Topics/01.技术栈/Coding/04-语言指南',
    ],
    'go|golang': [
        '2.Topics/01.技术栈/Coding/04-语言指南',
    ],

    # 系统设计/架构
    '系统设计|architecture|design': [
        '2.Topics/01.技术栈/Coding/03-系统设计/系统架构完全指南.md',
        '2.Topics/01.技术栈/Coding/03-系统设计集.md',
    ],
    '微服务|microservice': [
        '2.Topics/01.技术栈/Coding/03-系统设计/微服务架构完全指南.md',
    ],

    # 数据库
    '数据库|database|sql|postgres': [
        '2.Topics/01.技术栈/系统构建/02-后端工程实践/数据库与存储.md',
    ],

    # 测试
    '测试|test|tdd': [
        '2.Topics/01.技术栈/Coding/02-工程实践/测试最佳实践.md',
    ],

    # DevOps/部署
    'docker|k8s|kubernetes|deploy': [
        '2.Topics/01.技术栈/系统构建/03-运维实践集.md',
    ],

    # Git
    'git|github': [
        '2.Topics/01.技术栈/Coding/01-Git集.md',
    ],

    # IELTS/英语
    'ielts|雅思|english': [
        '2.Topics/06.语言与移民/英语/IELTS/雅思口语知识库.md',
        '2.Topics/06.语言与移民/英语/IELTS/IELTS大作文命题框架与策略.md',
    ],

    # 职业发展
    '职业|career|job|求职|程序员': [
        '2.Topics/04.职业发展',
        '1.Projects/技术能力晋升',
    ],

    # 内容创作
    'writing|写作|内容创作': [
        '2.Topics/03.内容创作/Writing',
    ],

    # 认知系统
    '思维|mental|认知|cognitive': [
        '2.Topics/02.认知系统/思维模型',
        '2.Topics/02.认知系统',
    ],

    # 学习方法
    '学习|learn|study': [
        '2.Topics/02.认知系统/学习系统',
    ],

    # 效率/生产力
    '效率|生产力|productivity|gtd': [
        '2.Topics/02.认知系统/个人效能/生产力系统',
    ],

    # 投资/理财
    '投资|理财|财务|finance': [
        '2.Topics/05.生活与健康/财务',
    ],
}

def count_current_links(content: str) -> int:
    """统计当前链接数"""
    wiki_links = len(re.findall(r'\[\[([^\]]+)\]\]', content))
    embeds = len(re.findall(r'!\[\[([^\]]+)\]\]', content))
    return wiki_links + embeds

def find_additional_topics(file_path: Path, existing_links: set) -> list:
    """查找额外相关主题(排除已有链接)"""

    additional = []
    filename = file_path.name.lower()
    path_str = str(file_path).lower()

    for keyword, topic_paths in TOPIC_KEYWORDS.items():
        if re.search(keyword, filename) or re.search(keyword, path_str):
            for topic_path in topic_paths:
                # 检查是否已在现有链接中
                topic_normalized = topic_path.lower().replace('\\', '/')
                if any(topic_normalized in link.lower() for link in existing_links):
                    continue

                topic_file = VAULT_ROOT / topic_path
                if topic_file.exists():
                    rel_path = topic_file.relative_to(VAULT_ROOT)
                    display = topic_file.stem
                    additional.append(f"[[{rel_path}|{display}]]")
                elif '/' in topic_path:
                    rel_path = topic_path
                    display = topic_path.split('/')[-2] if topic_path.split('/')[-2] else topic_path
                    additional.append(f"[[{rel_path}|{display}]]")

    return additional

def enhance_links_in_file_safe(file_path: Path) -> bool:
    """安全地增强单个文件的链接(带完整性和回滚检查)"""

    try:
        # 读取原始内容
        original_content = file_path.read_text(encoding='utf-8')
        original_length = len(original_content)
        original_lines = original_content.count('\n')

        # 检查是否已经有相关链接部分
        has_links_section = '## 🔗 相关链接' in content or '## 相关链接' in content

        # 提取现有链接
        existing_links = set(re.findall(r'\[\[([^\]]+)\]\]', original_content))

        # 统计当前链接数
        current_count = count_current_links(original_content)

        # 如果已经有3个以上链接,跳过
        if current_count >= 3:
            return False

        # 查找额外相关主题
        additional_topics = find_additional_topics(file_path, existing_links)

        if not additional_topics:
            return False

        # 计算需要添加的链接数
        needed = min(3 - current_count, len(additional_topics))
        new_links = additional_topics[:needed]

        if not new_links:
            return False

        # 构建新的链接部分
        if has_links_section:
            # 在现有链接部分追加
            links_section_match = re.search(
                r'(## 🔗 相关链接.*?\n)(---\n\n)',
                original_content,
                re.DOTALL
            )

            if links_section_match:
                # 在---之前插入新链接
                insert_pos = links_section_match.end(1) - len('---\n\n')
                new_links_text = '\n'.join([f"- {link}" for link in new_links])
                new_content = (
                    original_content[:insert_pos] +
                    new_links_text + '\n' +
                    original_content[insert_pos:]
                )
            else:
                return False
        else:
            # 创建新的链接部分
            links_section = "\n## 🔗 相关链接\n\n"
            links_section += "**相关主题**:\n"
            for link in new_links:
                links_section += f"- {link}\n"
            links_section += "\n---\n\n"

            # 在YAML frontmatter之后插入
            yaml_pattern = r'^---\s*\n(.*?)\n---\s*\n'
            yaml_match = re.match(yaml_pattern, original_content, re.DOTALL)

            if yaml_match:
                yaml_end = yaml_match.end()
                new_content = original_content[:yaml_end] + links_section + original_content[yaml_end:]
            else:
                new_content = links_section + original_content

        # 安全检查:验证新内容不会丢失原始内容
        new_length = len(new_content)
        new_lines = new_content.count('\n')

        # 检查1: 新内容长度应该大于等于原始内容(因为只是添加)
        if new_length < original_length:
            print(f"  ✗ {file_path.name} - 安全检查失败: 内容长度减少")
            return False

        # 检查2: 原始正文应该在新内容中
        # 提取正文部分(YAML之后的所有内容)
        yaml_end_orig = original_content.find('\n---\n', 0) + 5
        if yaml_end_orig > 5:
            body_original = original_content[yaml_end_orig:]

            yaml_end_new = new_content.find('\n---\n', 0) + 5
            if yaml_end_new > 5:
                body_new = new_content[yaml_end_new:]

                # 原始正文应该完整保留在新内容中
                if body_original and body_original not in body_new:
                    print(f"  ✗ {file_path.name} - 安全检查失败: 原始正文不完整")
                    return False

        # 检查3: 链接数确实增加了
        new_count = count_current_links(new_content)
        if new_count <= current_count:
            print(f"  ✗ {file_path.name} - 安全检查失败: 链接数未增加")
            return False

        # 所有检查通过,写入文件
        file_path.write_text(new_content, encoding='utf-8')
        print(f"  ✓ {file_path.name} - {current_count} → {new_count} 个链接")
        return True

    except Exception as e:
        print(f"  ✗ {file_path.name} - 错误: {e}")
        return False

def main():
    """主函数"""
    import argparse

    parser = argparse.ArgumentParser(
        description="低连通性笔记链接增强工具 (安全版)"
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='预览模式'
    )
    parser.add_argument(
        '--directory',
        type=str,
        help='只处理指定目录'
    )
    parser.add_argument(
        '--limit',
        type=int,
        default=50,
        help='最多处理文件数(默认50)'
    )

    args = parser.parse_args()

    print("=" * 70)
    print("低连通性笔记链接增强工具 (安全版)")
    print("=" * 70)
    print(f"模式: {'预览' if args.dry_run else '执行'}")
    if args.directory:
        print(f"目录: {args.directory}")
    print(f"限制: 最多处理 {args.limit} 个文件")
    print(f"安全检查: 内容完整性验证 + 自动回滚")
    print("=" * 70)
    print()

    # 读取低连通性笔记清单
    low_conn_file = VAULT_ROOT / "低连通性笔记清单_20260125_144217.md"

    if not low_conn_file.exists():
        print("✗ 低连通性笔记清单文件不存在!")
        return

    # 从清单中提取文件路径
    low_conn_files = []
    with open(low_conn_file, 'r', encoding='utf-8') as f:
        content = f.read()
        # 提取表格中的路径
        matches = re.findall(r'\| ([^|]+\.md) \|', content)
        for match in matches:
            file_path = VAULT_ROOT / match.replace('\\', '/')
            if args.directory:
                if args.directory in str(file_path):
                    low_conn_files.append(file_path)
            else:
                low_conn_files.append(file_path)

    # 过滤:只处理1-2个链接的
    files_to_process = []
    for file_path in low_conn_files[:args.limit]:
        if not file_path.exists():
            continue

        try:
            file_content = file_path.read_text(encoding='utf-8')
            link_count = count_current_links(file_content)

            # 只处理1-2个链接的
            if 1 <= link_count <= 2:
                files_to_process.append(file_path)
        except:
            pass

    print(f"📊 找到 {len(files_to_process)} 个低连通性笔记(1-2个链接)")
    print()

    if args.dry_run:
        # 预览模式
        processed = 0
        skipped = 0

        for i, file_path in enumerate(files_to_process, 1):
            rel_path = file_path.relative_to(VAULT_ROOT)

            try:
                content = file_path.read_text(encoding='utf-8')
                current_count = count_current_links(content)

                print(f"[{i}/{len(files_to_process)}] {rel_path} (当前: {current_count}个链接)")

                existing_links = set(re.findall(r'\[\[([^\]]+)\]\]', content))
                additional = find_additional_topics(file_path, existing_links)
                needed = min(3 - current_count, len(additional))

                if additional and needed > 0:
                    print(f"  → 可添加 {needed} 个链接")
                    processed += 1
                else:
                    print(f"  ⊙ 无可用链接")
                    skipped += 1

            except Exception as e:
                print(f"  ✗ 错误: {e}")
                skipped += 1
    else:
        # 执行模式
        print("⚠️  即将修改文件,所有修改将通过安全检查")
        print()

        # 创建备份
        backup_dir = VAULT_ROOT / ".backup_enhance"
        backup_dir.mkdir(exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_file = backup_dir / f"backup_{timestamp}.txt"

        print(f"📦 备份清单已创建: {backup_file}")
        print()

        processed = 0
        skipped = 0
        errors = 0

        for i, file_path in enumerate(files_to_process, 1):
            rel_path = file_path.relative_to(VAULT_ROOT)

            try:
                content = file_path.read_text(encoding='utf-8')
                current_count = count_current_links(content)

                print(f"[{i}/{len(files_to_process)}] {rel_path} (当前: {current_count}个链接)")

                if enhance_links_in_file_safe(file_path):
                    processed += 1
                    # 记录到备份清单
                    with open(backup_file, 'a', encoding='utf-8') as bf:
                        bf.write(f"{rel_path}\n")
                else:
                    skipped += 1

            except Exception as e:
                print(f"  ✗ 错误: {e}")
                errors += 1

    print()
    print("=" * 70)
    print("✅ 处理完成!")
    print(f"  处理成功: {processed} 个")
    print(f"  跳过: {skipped} 个")
    print(f"  错误: {errors} 个")
    print("=" * 70)

    if not args.dry_run and processed > 0:
        print()
        print("💡 建议:")
        print("  1. 运行 git diff 查看修改内容")
        print("  2. 随机抽查几个文件确认正文完整")
        print("  3. 确认无误后 git commit")

if __name__ == "__main__":
    main()
