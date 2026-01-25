#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
标签规范化批量处理脚本

功能：为Markdown文件批量添加Domain/Type/Status标签
作者：Claude Code
日期：2026-01-24
使用方法：python batch_add_domain_tags.py
"""

import os
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional

# 设置UTF-8编码输出(修复Windows控制台问题)
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

# === 配置部分 ===
VAULT_ROOT = Path(r"d:\迅雷下载\@同步文件\OneDrive\obsidianDoc")

# 只处理这些笔记目录（include模式）
INCLUDE_DIRS = [
    "0.DailyNotes",
    "1.Projects",
    "2.Topics",
    "3.Resources",
    "4.Archives",
    "5.Misc",
    "6.Calendar",
    "Atlas",
]

# Domain分类规则（基于路径）
DOMAIN_RULES = {
    r"2\.Topics/01\.技术栈": "Domain/Technology",
    r"2\.Topics/02\.认知系统": "Domain/Cognitive",
    r"2\.Topics/04\.职业发展": "Domain/Professional",
    r"2\.Topics/06\.语言与移民": "Domain/Language",
    r"3\.Resources/Prompt工程": "Domain/AI",
    r"4\.Archives/Tools": "Domain/Technology",
    r"Atlas/Index": "Domain/Cognitive",  # 索引文件
}

# 子Domain分类规则
SUBDOMAIN_RULES = {
    # Technology
    r".*[Gg]it.*": "Domain/Technology/Git",
    r".*[Dd]ocker.*|.*[Cc]ontainer.*": "Domain/Technology/Docker",
    r".*[Aa]pi.*|.*[Rr]est.*": "Domain/Technology/API",
    r".*[Pp]ython.*": "Domain/Technology/Python",
    r".*[Jj]ava[Ss]cript.*|.*[Nn]ode.*|.*[Tt]ype[Ss]cript.*": "Domain/Technology/JavaScript",
    r".*[Rr]ust.*": "Domain/Technology/Rust",
    r".*[Gg]o.*": "Domain/Technology/Go",
    r".*[Ss]ystem.*[Dd]esign.*|.*[Aa]rchitecture.*": "Domain/Technology/SystemDesign",
    r".*[Bb]ackend.*|.*[Ss]erver.*": "Domain/Technology/Backend",
    r".*[Dd]atabase.*|.*[Ss]ql.*": "Domain/Technology/Database",
    r".*[Dd]ev[Oo]ps.*|.*[Cc]icd.*": "Domain/Technology/DevOps",

    # AI
    r".*[Aa]gent.*|.*[Mm]ulti.*[Aa]gent.*": "Domain/AI/Agent",
    r".*[Pp]rompt.*|.*[Ll]lm.*": "Domain/AI/PromptEngineering",
    r".*[Cc]hat.*|[Ll]lm.*": "Domain/AI/LLM",
    r".*[Cc]ontent.*[Cc]reation.*|.*[Ww]riting.*": "Domain/AI/ContentCreation",

    # Professional
    r".*[Cc]areer.*|.*[Jj]ob.*|.*[Ww]ork.*": "Domain/Professional/CareerPlanning",
    r".*[Ss]kill.*|.*[Cc]ompeten.*": "Domain/Professional/Skill",
    r".*[Ss]ide.*[Hh]ustle.*": "Domain/Professional/SideHustle",

    # Cognitive
    r".*[Mm]ental.*[Mm]odel.*|.*[Tt]hink.*": "Domain/Cognitive/MentalModel",
    r".*[Ll]earning.*|.*[Ss]tudy.*": "Domain/Cognitive/LearningMethod",
    r".*[Mm]emory.*|.*[Rr]emember.*": "Domain/Cognitive/Memory",
    r".*[Tt]ool.*|.*[Ss]ystem.*": "Domain/Cognitive/Tools",

    # Language
    r".*[Ii]elts.*|.*[Ee]nglish.*": "Domain/Language/IELTS",
    r".*[Ii]mmigration.*|.*[Vv]isa.*": "Domain/Language/Immigration",
}

# Type分类规则
TYPE_RULES = {
    r".*_Index_.*|.*Index.*": "Type/Index",
    r".*模板.*|.*[Tt]emplate.*": "Type/Template",
    r".*[Gg]uide.*|.*[Mm]anual.*|.*[Hh]andbook.*": "Type/Reference",
    r".*[Ss]ystem.*|.*[Pp]rotocol.*": "Type/System",
    r".*[Nn]ote.*|.*[Dd]iary.*|.*[Jj]ournal.*": "Type/Note",
    r".*[Ll]og.*|.*[Rr]ecord.*": "Type/Log",
    r".*[Aa]nalysis.*|.*[Rr]eport.*": "Type/Analysis",
    r".*[Cc]heat.*|.*[Rr]eference.*": "Type/Reference",
    r".*[Ss]pec.*|.*[Dd]oc.*": "Type/Reference",
    r".*[Tt]utorial.*": "Type/Tutorial",
    r".*[Aa]ction.*|.*[Tt]odo.*": "Type/Action",
}

# Status分类规则
STATUS_RULES = {
    r".*已.*|.*done.*|.*完成.*|.*完成.*": "Status/Done",
    r".*todo.*|.*待办.*|.*待处理.*": "Status/TODO",
    r".*review.*|.*复盘.*|.*回顾.*": "Status/Review",
    r".*mastered.*|.*精通.*": "Status/Mastered",
    r".*in.*progress.*|.*进行中.*": "Status/InProgress",
}

def extract_frontmatter(content: str) -> tuple[str, str]:
    """提取并返回YAML frontmatter和正文内容"""
    pattern = r'^---\s*\n(.*?)\n---\s*\n(.*)$'
    match = re.match(pattern, content, re.DOTALL | re.MULTILINE)
    if match:
        return match.group(1), match.group(2)
    return "", content

def add_tags_to_yaml(yaml_content: str, new_tags: List[str]) -> str:
    """为YAML内容添加新标签（修复版：避免重复）"""
    if not yaml_content.strip():
        yaml_content = "tags: []"

    # 解析现有标签
    lines = yaml_content.strip().split('\n')
    tags_start_idx = -1
    tags = []
    tags_indent = ""
    tags_end_idx = -1  # 记录多行标签的结束位置

    for i, line in enumerate(lines):
        if line.strip().startswith('tags:'):
            tags_start_idx = i
            # 提取缩进
            match = re.match(r'^(\s*)tags:', line)
            if match:
                tags_indent = match.group(1)
            # 解析现有标签
            # 检查是否是完整的单行格式: tags: [tag1, tag2]
            inline_match = re.match(r'tags:\s*\[(.*)\]$', line)
            if inline_match:
                # 单行格式: tags: [tag1, tag2]
                tags_content = inline_match.group(1).strip()
                if tags_content:
                    tags = [t.strip().strip('"').strip("'") for t in tags_content.split(',')]
                else:
                    tags = []
            else:
                # 多行格式或空列表
                if line.strip() == 'tags:[]':
                    tags = []
                else:
                    # 读取多行标签（关键修复：正确记录结束位置）
                    j = i + 1
                    while j < len(lines) and lines[j].startswith(tags_indent + '  -'):
                        tag = lines[j].split('-', 1)[1].strip().strip('"').strip("'")
                        if tag:  # 只添加非空标签
                            tags.append(tag)
                        j += 1
                    tags_end_idx = j  # 记录多行标签的结束位置
            break

    # 添加新标签（去重）
    for tag in new_tags:
        if tag and tag not in tags:  # 确保 tag 不为空
            tags.append(tag)

    # 重建YAML（关键修复：正确删除旧的多行标签）
    if tags_start_idx >= 0:
        if len(tags) == 0:
            # 保留tags行但为空
            lines[tags_start_idx] = f"{tags_indent}tags: []"
            # 删除旧的多行标签（如果有）
            if tags_end_idx > tags_start_idx:
                lines = lines[:tags_start_idx + 1] + lines[tags_end_idx:]
        elif len(tags) <= 3:  # 单行格式
            tags_str = ", ".join(f'"{t}"' for t in tags)
            lines[tags_start_idx] = f"{tags_indent}tags: [{tags_str}]"
            # 删除旧的多行标签（如果有）
            if tags_end_idx > tags_start_idx:
                lines = lines[:tags_start_idx + 1] + lines[tags_end_idx:]
        else:
            # 多行格式（关键修复：正确替换整个tags块）
            if tags_end_idx > tags_start_idx:
                # 有旧的多行标签，替换整个块
                new_lines = [
                    f"{tags_indent}tags:"
                ] + [f"{tags_indent}  - {tag}" for tag in tags]
                lines = lines[:tags_start_idx] + new_lines + lines[tags_end_idx:]
            else:
                # 没有旧的多行标签，直接替换单行
                new_lines = [
                    f"{tags_indent}tags:"
                ] + [f"{tags_indent}  - {tag}" for tag in tags]
                lines = lines[:tags_start_idx] + new_lines + lines[tags_start_idx + 1:]

        # 移除空行
        while lines and lines[-1].strip() == '':
            lines.pop()

        yaml_content = '\n'.join(lines)
    else:
        # 没有tags字段，添加一个
        yaml_content = yaml_content.rstrip()
        if yaml_content:
            yaml_content += "\n\n"
        tags_str = ", ".join(f'"{t}"' for t in tags)
        yaml_content += f"{tags_indent}tags: [{tags_str}]\n"

    return yaml_content

def get_tags_from_path(filepath: Path) -> List[str]:
    """根据文件路径推断应该添加的标签"""
    path_str = str(filepath)
    tags = []

    # 1. 主Domain标签
    for pattern, domain in DOMAIN_RULES.items():
        if re.search(pattern, path_str):
            tags.append(domain)
            break

    # 2. 子Domain标签
    for pattern, subdomain in SUBDOMAIN_RULES.items():
        if re.search(pattern, path_str, re.IGNORECASE):
            if subdomain not in tags:
                tags.append(subdomain)

    # 3. Type标签
    for pattern, type_tag in TYPE_RULES.items():
        if re.search(pattern, path_str, re.IGNORECASE):
            if type_tag not in tags:
                tags.append(type_tag)
            break

    # 4. Status标签（可选）
    for pattern, status in STATUS_RULES.items():
        if re.search(pattern, path_str, re.IGNORECASE):
            tags.append(status)
            break

    # 如果没有推断出Domain标签，根据目录结构推断
    if not any(tag.startswith("Domain/") for tag in tags):
        if "2.Topics" in path_str or "3.Resources" in path_str or "4.Archives" in path_str:
            # 默认添加Technology
            tags.append("Domain/Technology")
        elif "Atlas" in path_str:
            tags.append("Domain/Cognitive")

    # 如果没有Type标签，默认添加Reference
    if not any(tag.startswith("Type/") for tag in tags):
        tags.append("Type/Reference")

    return tags

def process_file(filepath: Path) -> bool:
    """处理单个文件（改进版：更好的Domain标签检测）"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        yaml_content, body_content = extract_frontmatter(content)

        # 检查是否已有Domain标签（改进版：更准确的检测）
        has_domain = False
        # 检查单行格式: tags: ["Domain/xxx", ...]
        if re.search(r'tags:\s*\[[^\]]*?Domain/', yaml_content):
            has_domain = True
        # 检查多行格式: - Domain/xxx
        elif re.search(r'^\s*-\s*Domain/', yaml_content, re.MULTILINE):
            has_domain = True

        if has_domain:
            print(f"  ⊙ {filepath.name} - 已有Domain标签，跳过")
            return False

        # 推断应该添加的标签
        new_tags = get_tags_from_path(filepath)

        # 如果没有推断出任何标签，跳过
        if not new_tags:
            print(f"  ⊙ {filepath.name} - 无法推断标签，跳过")
            return False

        # 添加标签
        new_yaml = add_tags_to_yaml(yaml_content, new_tags)

        # 重建文件内容
        if new_yaml.strip():
            new_content = f"---\n{new_yaml}\n---\n{body_content}"
        else:
            new_content = body_content

        # 写回文件
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"  ✓ {filepath.name} - 添加标签: {', '.join(new_tags[:3])}...")
        return True

    except Exception as e:
        print(f"  ✗ {filepath.name} - 错误: {e}")
        return False

def main():
    """主函数（改进版：更准确的文件过滤）"""
    print("=" * 60)
    print("标签规范化批量处理脚本")
    print("=" * 60)

    # 只在指定的笔记目录中查找Markdown文件
    print("\n🔍 扫描Markdown文件...")
    md_files = []
    for dir_name in INCLUDE_DIRS:
        dir_path = VAULT_ROOT / dir_name
        if dir_path.exists():
            md_files.extend(dir_path.rglob("*.md"))
            print(f"  ✓ 扫描 {dir_name}/")
        else:
            print(f"  ⊙ 跳过 {dir_name}/ (目录不存在)")

    # 过滤出需要处理的文件（没有Domain标签的）
    files_to_process = []
    skipped = 0

    for filepath in md_files:
        # 跳过agent配置文件
        if '.agent' in str(filepath) or filepath.name.startswith('.'):
            skipped += 1
            continue

        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            # 更准确的Domain标签检测
            has_domain = False
            # 检查单行格式
            if re.search(r'tags:\s*\[[^\]]*?Domain/', content):
                has_domain = True
            # 检查多行格式
            elif re.search(r'^\s*-\s*Domain/', content, re.MULTILINE):
                has_domain = True

            if not has_domain:
                files_to_process.append(filepath)
        except:
            skipped += 1

    print(f"\n📊 找到 {len(files_to_process)} 个需要处理的文件")
    if skipped > 0:
        print(f"  ⊙ 跳过 {skipped} 个文件（已有Domain标签或无法读取）")

    if not files_to_process:
        print("\n✅ 所有文件已规范化，无需处理！")
        return

    print(f"\n🚀 开始处理...\n")

    # 处理文件
    processed = 0
    failed = 0

    for filepath in files_to_process:
        if process_file(filepath):
            processed += 1
        else:
            failed += 1

    print(f"\n{'=' * 60}")
    print(f"✅ 处理完成！")
    print(f"  成功: {processed} 个文件")
    print(f"  失败: {failed} 个文件")
    print(f"  总计: {len(files_to_process)} 个文件")
    print("=" * 60)

if __name__ == "__main__":
    main()
