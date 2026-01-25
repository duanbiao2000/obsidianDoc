#!/usr/bin/env python3
"""
项目元数据审计脚本
扫描 1.Projects/ 目录下所有文件，检查 YAML frontmatter 完整性
"""

import os
import re
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Tuple


def extract_yaml_frontmatter(file_path: str) -> Dict[str, any]:
    """提取文件的 YAML frontmatter"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # 匹配 YAML frontmatter (在 --- 之间)
        yaml_pattern = r'^---\n(.*?)\n---'
        match = re.match(yaml_pattern, content, re.DOTALL)

        if not match:
            return {'valid': False, 'error': 'No YAML frontmatter found'}

        yaml_content = match.group(1)
        frontmatter = {'valid': True, 'raw': yaml_content}

        # 解析常见字段
        if 'update:' in yaml_content:
            update_match = re.search(r'update:\s*(.+)', yaml_content)
            if update_match:
                frontmatter['update'] = update_match.group(1).strip()

        if 'created:' in yaml_content:
            created_match = re.search(r'created:\s*(.+)', yaml_content)
            if created_match:
                frontmatter['created'] = created_match.group(1).strip()

        if 'tags:' in yaml_content:
            tags_match = re.search(r'tags:\s*\[(.*?)\]', yaml_content, re.DOTALL)
            if tags_match:
                frontmatter['tags'] = tags_match.group(1).strip()

        if 'status:' in yaml_content:
            status_match = re.search(r'status:\s*(.+)', yaml_content)
            if status_match:
                frontmatter['status'] = status_match.group(1).strip()

        # 检查关键字段
        frontmatter['has_update'] = 'update' in frontmatter
        frontmatter['has_created'] = 'created' in frontmatter
        frontmatter['has_tags'] = 'tags' in frontmatter
        frontmatter['has_status'] = 'status' in frontmatter

        return frontmatter

    except Exception as e:
        return {'valid': False, 'error': str(e)}


def audit_projects_directory(projects_dir: str) -> List[Dict]:
    """审计 Projects 目录下所有文件"""
    results = []
    projects_path = Path(projects_dir)

    # 递归查找所有 .md 文件
    md_files = list(projects_path.rglob('*.md'))

    print(f"[DEBUG] Found {len(md_files)} markdown files in {projects_dir}")

    # 排除索引文件和 CLAUDE.md
    excluded_files = ['_Index_', 'CLAUDE.md']

    for file_path in md_files:
        # 跳过排除的文件
        if any(excluded in file_path.name for excluded in excluded_files):
            print(f"[SKIP] Excluded: {file_path.name}")
            continue

        # 获取相对路径
        rel_path = file_path.relative_to(projects_path.parent)

        # 提取 frontmatter
        frontmatter = extract_yaml_frontmatter(str(file_path))

        result = {
            'path': str(rel_path),
            'full_path': str(file_path),
            'frontmatter': frontmatter
        }

        results.append(result)
        print(f"[OK] Processed: {rel_path}")

    return results


def generate_audit_report(results: List[Dict], output_file: str):
    """生成审计报告"""
    total_files = len(results)
    missing_update = [r for r in results if not r['frontmatter'].get('has_update', False)]
    missing_created = [r for r in results if not r['frontmatter'].get('has_created', False)]
    missing_tags = [r for r in results if not r['frontmatter'].get('has_tags', False)]

    report_lines = [
        "# 项目元数据审计报告\n",
        f"**生成时间**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"**扫描范围**: `1.Projects/` 目录",
        f"",
        "## 📊 总体统计\n",
        f"- **扫描文件数**: {total_files} 个",
        f"- **缺少 update 字段**: {len(missing_update)} 个 ({len(missing_update)/total_files*100:.1f}%)",
        f"- **缺少 created 字段**: {len(missing_created)} 个 ({len(missing_created)/total_files*100:.1f}%)",
        f"- **缺少 tags 字段**: {len(missing_tags)} 个 ({len(missing_tags)/total_files*100:.1f}%)",
        f"",
        "## 🔴 缺少 update 字段的文件\n",
        f"共 {len(missing_update)} 个文件需要补充：\n"
    ]

    # 按目录分组
    missing_update_sorted = sorted(missing_update, key=lambda x: x['path'])
    for item in missing_update_sorted:
        report_lines.append(f"- [{item['path']}]({item['path']})")

    report_lines.extend([
        f"\n## 🟡 缺少 created 字段的文件\n",
        f"共 {len(missing_created)} 个文件：\n"
    ])

    for item in sorted(missing_created, key=lambda x: x['path']):
        report_lines.append(f"- [{item['path']}]({item['path']})")

    report_lines.extend([
        f"\n## 🟢 详细清单\n",
        "| 文件路径 | has_update | has_created | has_tags | has_status |",
        "|----------|------------|-------------|----------|------------|"
    ])

    for item in sorted(results, key=lambda x: x['path']):
        fm = item['frontmatter']
        report_lines.append(
            f"| {item['path']} | {'✅' if fm.get('has_update') else '❌'} | "
            f"{'✅' if fm.get('has_created') else '❌'} | "
            f"{'✅' if fm.get('has_tags') else '❌'} | "
            f"{'✅' if fm.get('has_status') else '❌'} |"
        )

    report_lines.extend([
        f"\n## 📝 下一步行动\n",
        "1. **Phase 2**: 为所有缺少 `update` 字段的文件补充时间戳",
        "2. **Phase 3**: 基于 `update` 字段识别超过 90 天未更新的项目",
        "3. **Phase 3**: 将不活跃项目归档到 `4.Archives/` 目录",
        "4. **Phase 4**: 建立自动化监控机制，定期检查项目活跃度"
    ])

    # 写入报告文件
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(report_lines))

    print(f"[OK] Audit report generated: {output_file}")
    print(f"   - Total files: {total_files}")
    print(f"   - Missing update: {len(missing_update)}")
    print(f"   - Missing created: {len(missing_created)}")


if __name__ == '__main__':
    import sys
    import os

    # 设置 UTF-8 编码输出
    if sys.platform == 'win32':
        import codecs
        sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')

    # 使用当前目录（脚本运行目录应该是 worktree 根目录）
    projects_dir = '1.Projects'
    report_file = '项目元数据审计报告_Phase1.md'

    print(f"[START] Scanning project metadata...")
    print(f"[INFO] Current directory: {os.getcwd()}")
    results = audit_projects_directory(projects_dir)
    generate_audit_report(results, report_file)
