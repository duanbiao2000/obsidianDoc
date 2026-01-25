#!/usr/bin/env python3
"""
检查项目活跃度，识别需要归档的项目
"""

import os
import re
from datetime import datetime, timedelta
from pathlib import Path


def extract_update_date(file_path: str) -> datetime | None:
    """提取文件的 update 日期"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # 匹配 update: YYYY-MM-DD
        match = re.search(r'\nupdate:\s*(\d{4}-\d{2}-\d{2})', content)
        if match:
            date_str = match.group(1)
            return datetime.strptime(date_str, '%Y-%m-%d')

        return None
    except Exception as e:
        print(f"[ERROR] Failed to read {file_path}: {e}")
        return None


def check_project_activity(projects_dir: str, days_threshold: int = 90):
    """
    检查项目活跃度

    Args:
        projects_dir: Projects 目录路径
        days_threshold: 不活跃天数阈值（默认90天）
    """
    projects_path = Path(projects_dir)
    md_files = list(projects_path.rglob('*.md'))

    # 排除索引文件和 CLAUDE.md
    excluded_files = ['_Index_', 'CLAUDE.md']

    results = {
        'active': [],
        'warning': [],
        'inactive': [],
        'no_update_field': []
    }

    threshold_date = datetime.now() - timedelta(days=days_threshold)
    warning_date = datetime.now() - timedelta(days=int(days_threshold * 0.7))  # 70% 阈值

    for file_path in md_files:
        # 跳过排除的文件
        if any(excluded in file_path.name for excluded in excluded_files):
            continue

        rel_path = str(file_path.relative_to(projects_path.parent))
        update_date = extract_update_date(str(file_path))

        if update_date is None:
            results['no_update_field'].append({
                'path': rel_path,
                'full_path': str(file_path)
            })
        elif update_date < threshold_date:
            days_inactive = (datetime.now() - update_date).days
            results['inactive'].append({
                'path': rel_path,
                'full_path': str(file_path),
                'update_date': update_date.strftime('%Y-%m-%d'),
                'days_inactive': days_inactive
            })
        elif update_date < warning_date:
            results['warning'].append({
                'path': rel_path,
                'full_path': str(file_path),
                'update_date': update_date.strftime('%Y-%m-%d'),
                'days_inactive': (datetime.now() - update_date).days
            })
        else:
            results['active'].append({
                'path': rel_path,
                'full_path': str(file_path),
                'update_date': update_date.strftime('%Y-%m-%d')
            })

    return results


def generate_activity_report(results: dict, output_file: str, days_threshold: int = 90):
    """生成项目活跃度报告"""
    today = datetime.now().strftime('%Y-%m-%d')

    lines = [
        f"# 项目活跃度审计报告\n",
        f"**生成时间**: {today}",
        f"**审计阈值**: {days_threshold} 天未更新视为不活跃",
        f"",
        "## 📊 总体统计\n",
        f"- **活跃项目**: {len(results['active'])} 个",
        f"- **预警项目** ({days_threshold*0.7:.0f}天未更新): {len(results['warning'])} 个",
        f"- **不活跃项目** (超过{days_threshold}天): {len(results['inactive'])} 个",
        f"- **无 update 字段**: {len(results['no_update_field'])} 个",
        f"",
    ]

    # 不活跃项目
    if results['inactive']:
        lines.extend([
            f"## 🔴 不活跃项目（需要归档）\n",
            f"以下项目超过 {days_threshold} 天未更新，建议归档到 `4.Archives/Projects/`：\n"
        ])

        for item in sorted(results['inactive'], key=lambda x: x['days_inactive'], reverse=True):
            lines.append(
                f"- **[{item['path']}]({item['path']})** - "
                f"更新于 {item['update_date']} "
                f"（{item['days_inactive']} 天前）"
            )

    # 预警项目
    if results['warning']:
        lines.extend([
            f"\n## 🟡 预警项目（即将不活跃）\n",
            f"以下项目接近 {days_threshold} 天阈值，需要关注：\n"
        ])

        for item in sorted(results['warning'], key=lambda x: x['days_inactive'], reverse=True):
            days_inactive = item['days_inactive']
            lines.append(
                f"- **[{item['path']}]({item['path']})** - "
                f"更新于 {item['update_date']} "
                f"（{days_inactive} 天前）"
            )

    # 活跃项目
    if results['active']:
        lines.extend([
            f"\n## 🟢 活跃项目\n",
            f"以下项目最近有更新：\n"
        ])

        for item in sorted(results['active'], key=lambda x: x['update_date'], reverse=True):
            lines.append(
                f"- **[{item['path']}]({item['path']})** - 更新于 {item['update_date']}"
            )

    # 无 update 字段
    if results['no_update_field']:
        lines.extend([
            f"\n## ⚪ 无 update 字段\n",
            f"以下项目缺少 update 字段：\n"
        ])

        for item in sorted(results['no_update_field'], key=lambda x: x['path']):
            lines.append(f"- [{item['path']}]({item['path']})")

    # 归档建议
    lines.extend([
        f"\n## 📝 归档建议\n",
        f"1. **立即归档**: 将 {len(results['inactive'])} 个不活跃项目移动到 `4.Archives/Projects/`",
        f"2. **更新索引**: 修改 `1.Projects/_Index_of_1.Projects.md`",
        f"3. **检查链接**: 确保归档后链接仍然有效",
        f"4. **建立监控**: 使用 Phase 4 脚本定期检查项目活跃度"
    ])

    # 写入报告
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))

    print(f"[OK] Activity report generated: {output_file}")
    print(f"   - Active: {len(results['active'])}")
    print(f"   - Warning: {len(results['warning'])}")
    print(f"   - Inactive: {len(results['inactive'])}")
    print(f"   - No update field: {len(results['no_update_field'])}")


def main():
    import sys

    # 设置 UTF-8 编码输出
    if sys.platform == 'win32':
        import codecs
        sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')

    projects_dir = '1.Projects'
    report_file = '项目活跃度审计报告_Phase3.md'
    days_threshold = 90  # 90天阈值

    print(f"[START] Checking project activity (threshold: {days_threshold} days)...")

    results = check_project_activity(projects_dir, days_threshold)
    generate_activity_report(results, report_file, days_threshold)


if __name__ == '__main__':
    main()
