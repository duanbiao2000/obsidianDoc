#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
为Atlas目录的孤立笔记添加链接
GitHub Issue #2: 孤立笔记链接密度提升计划
"""

import re
import sys
from pathlib import Path

# Windows 编码支持
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

VAULT_ROOT = Path(r"d:\迅雷下载\@同步文件\OneDrive\obsidianDoc")

# Atlas孤立笔记列表(从清单中提取)
ATLAS_ORPHANS = [
    "Atlas/Index/Dataview-7日内新建的笔记.md",
    "Atlas/Index/Dataviewer过时+高Rating.md",
    "Atlas/Index/标签映射表_20260125.md",
    "Atlas/Index/标签系统规范化执行计划.md",
    "Atlas/Index/标签规范化Session完成报告_2026-01-24.md",
    "Atlas/Index/标签规范化完成报告_20260125.md",
    "Atlas/Index/标签规范化审计报告_20260125.md",
    "Atlas/Index/标签规范化待处理文件清单.md",
    "Atlas/Index/标签规范化执行进度报告.md",
    "Atlas/Index/标签规范化最终完成报告_2026-01-24.md",
    "Atlas/Index/标签规范化项目完成报告.md",
    "Atlas/Index/标签规范化项目总结报告.md",
    "Atlas/Index/认知系统去重执行报告_第三阶段_2026-01-24.md",
    "Atlas/kanban/2025-06-07GPT_Researcher.md",
    "Atlas/Docs/plans/2025-01-22-claude-md-integration-guide.md",
    "Atlas/Docs/plans/2025-01-22-claude-md-verification-report.md",
    "Atlas/Docs/plans/2025-01-22-subdirectory-characteristics-map.md",
    "Atlas/Cards/Excalidraw/个人能力图谱.excalidraw.md",
]

def add_links_to_file(file_path: Path) -> bool:
    """为单个文件添加链接"""

    try:
        content = file_path.read_text(encoding='utf-8')

        # 检查是否已经有相关链接部分
        if '## 🔗 相关链接' in content or '## 相关链接' in content:
            print(f"  ⊙ {file_path.name} - 已有链接部分,跳过")
            return False

        # 构建链接部分
        related_links = "## 🔗 相关链接\n\n"

        # 根据文件路径判断应该添加哪些链接
        path_str = str(file_path)

        if '标签' in path_str:
            # 标签相关文件
            related_links += "- **主索引**: [[Atlas/Index/仓库标签管理系统 | 仓库标签管理系统]]\n"
            related_links += "- **相关索引**: [[Atlas/MOCs.md | 系统主索引]]\n"
            related_links += "- **关联报告**: 标签规范化系列报告\n"

            # 添加同目录下的其他相关文件
            if '审计报告' in path_str or '完成报告' in path_str:
                related_links += "- **前置任务**: [[Atlas/Index/标签系统规范化执行计划]]\n"
            elif '执行计划' in path_str:
                related_links += "- **后续报告**: [[Atlas/Index/标签规范化完成报告_20260125]]\n"

        elif 'Dataview' in path_str:
            # Dataview相关文件
            related_links += "- **主索引**: [[Atlas/Index/Whole Vault任务管理.md | 任务管理]]\n"
            related_links += "- **Dataview文档**: [[Atlas/Index/Dataviewer.md | Dataview使用指南]]\n"

        elif 'kanban' in path_str:
            # Kanban相关文件
            related_links += "- **主索引**: [[Atlas/BASE/Whole Vault任务管理.md | 任务管理]]\n"
            related_links += "- **看板系统**: [[Atlas/kanban/]]\n"

        elif 'claude-md' in path_str:
            # Claude Code相关文档
            related_links += "- **主索引**: [[4.Archives/Tools/claude.md范例.md | Claude Code开发规范]]\n"
            related_links += "- **CLAUDE.md**: [[CLAUDE.md | 项目指南]]\n"

        elif 'Excalidraw' in path_str:
            # Excalidraw绘图
            related_links += "- **主索引**: [[Atlas/Cards/]]\n"
            related_links += "- **绘图工具**: [[Atlas/Index/绘图工具索引.md]]\n"

        else:
            # 默认链接
            related_links += "- **主索引**: [[Atlas/MOCs.md | 系统主索引]]\n"
            related_links += "- **BASE**: [[Atlas/BASE/]]\n"

        related_links += "\n---\n\n"

        # 在YAML frontmatter之后插入链接
        yaml_pattern = r'^---\s*\n(.*?)\n---\s*\n'
        yaml_match = re.match(yaml_pattern, content, re.DOTALL)

        if yaml_match:
            yaml_end = yaml_match.end()
            new_content = content[:yaml_end] + '\n' + related_links + content[yaml_end:]
        else:
            # 没有YAML,直接在开头添加
            new_content = related_links + content

        # 写回文件
        file_path.write_text(new_content, encoding='utf-8')
        print(f"  ✓ {file_path.name} - 已添加链接")
        return True

    except Exception as e:
        print(f"  ✗ {file_path.name} - 错误: {e}")
        return False

def main():
    print("=" * 70)
    print("为Atlas孤立笔记添加链接")
    print("=" * 70)
    print()

    processed = 0
    skipped = 0

    for orphan_rel_path in ATLAS_ORPHANS:
        file_path = VAULT_ROOT / orphan_rel_path

        if not file_path.exists():
            print(f"  ⊙ {orphan_rel_path} - 文件不存在")
            skipped += 1
            continue

        if add_links_to_file(file_path):
            processed += 1
        else:
            skipped += 1

    print()
    print("=" * 70)
    print(f"✅ 处理完成!")
    print(f"  处理成功: {processed} 个")
    print(f"  跳过: {skipped} 个")
    print("=" * 70)

if __name__ == "__main__":
    main()
