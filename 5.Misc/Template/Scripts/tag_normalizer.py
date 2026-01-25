#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
标签规范化脚本
用于批量替换 Obsidian 笔记中的标签

GitHub Issue #1: https://github.com/duanbiao2000/obsidianDoc/issues/1

使用方法:
    python tag_normalizer.py --dry-run           # 预览模式（不修改文件）
    python tag_normalizer.py --phase invalid    # 删除无效标签
    python tag_normalizer.py --phase high       # 替换高频标签
    python tag_normalizer.py --phase all        # 执行所有替换
"""

import re
import json
import argparse
import sys
from pathlib import Path
from datetime import datetime
from typing import Dict, Optional, Tuple

# Windows 编码支持
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

# ==================== 配置区 ====================

# 笔记目录列表
NOTE_DIRECTORIES = [
    "0.DailyNotes",
    "1.Projects",
    "2.Topics",
    "3.Resources",
    "4.Archives",
    "6.Calendar",
]

# ==================== 标签映射表 ====================

# Phase 1: 删除无效/占位符标签
INVALID_TAGS = [
    "#Domain/<SubDomain>",
    "#Status/<State>",
    "#Type/<ContentType>",
    "#Domain/",
    "#Type/",
    "#Status/",
    "#6f9",
    "#333",
    "#SpecDriven",
    "#javascriptnodejs-testing-best-practices-guide-advanced-testing-techniques",
]

# Phase 2: 高频标签映射（优先级：高）
HIGH_PRIORITY_MAPPINGS = {
    # Domain 标签
    "#AI": "#Domain/AI",
    "#Domain/Cognition": "#Domain/Cognitive",

    # Status 标签
    "#todo": "#Status/TODO",
    "#done": "#Status/Done",

    # Type 标签
    "#note": "#Type/Note",
    "#Project": "#Type/Project",
    "#MOC": "#Type/MOC",
    "#reference": "#Type/Reference",
    "#permanent-note": "#Type/Note",
}

# Phase 3: 中频标签映射（优先级：中）
MEDIUM_PRIORITY_MAPPINGS = {
    # Domain 标签
    "#Domain/CognitiveSystem": "#Domain/Cognitive",
    "#Domain/ContentCreation": "#Domain/Content",
    "#SubDomain/IELTS": "#Domain/Language/IELTS",
    "#ContentCreation": "#Domain/Content",
    "#card": "#Type/Card",
}

# Phase 4: 低频标签映射（优先级：低）
LOW_PRIORITY_MAPPINGS = {
    # Domain 标签
    "#Python": "#Domain/Technology/Python",
    "#Architecture": "#Domain/TechStack/SystemDesign",
    "#SystemDesign": "#Domain/TechStack/SystemDesign",
    "#Tech/AI": "#Domain/AI",
    "#OpenSource": "#Domain/Technology/OpenSource",
    "#Domain/Psychology": "#Domain/Cognitive/Psychology",
    "#Domain/MentalModel": "#Domain/Cognitive/MentalModel",
    "#Concurrency": "#Domain/TechStack/Concurrency",
    "#CloudNative": "#Domain/TechStack/CloudNative",
    "#CareerPlanning": "#Domain/Career/Planning",
    "#EngineeringMindset": "#Domain/Career/Engineering",
}

# 合并所有映射
ALL_MAPPINGS = {
    **HIGH_PRIORITY_MAPPINGS,
    **MEDIUM_PRIORITY_MAPPINGS,
    **LOW_PRIORITY_MAPPINGS,
}

# ==================== 工具函数 ====================

def create_backup_path(file_path: Path) -> Path:
    """创建备份文件路径"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return file_path.with_suffix(f".md.{timestamp}.bak")


def normalize_tags_in_content(content: str, phase: str = "all") -> Tuple[str, Dict]:
    """
    规范化内容中的标签

    Args:
        content: 文件内容
        phase: 执行阶段 ('invalid', 'high', 'medium', 'low', 'all')

    Returns:
        (处理后的内容, 统计信息)
    """
    original_content = content
    stats = {
        "deleted_tags": 0,
        "replaced_tags": 0,
        "modifications": [],
    }

    # Phase 1: 删除无效标签
    if phase in ["invalid", "all"]:
        for tag in INVALID_TAGS:
            pattern = r'\b' + re.escape(tag) + r'\b'
            matches = re.findall(pattern, content)
            if matches:
                content = re.sub(pattern, '', content)
                stats["deleted_tags"] += len(matches)
                stats["modifications"].append({
                    "action": "delete",
                    "tag": tag,
                    "count": len(matches),
                })

    # Phase 2: 高频标签替换
    if phase in ["high", "all"]:
        for old_tag, new_tag in HIGH_PRIORITY_MAPPINGS.items():
            pattern = r'\b' + re.escape(old_tag) + r'\b'
            matches = re.findall(pattern, content)
            if matches:
                content = re.sub(pattern, new_tag, content)
                stats["replaced_tags"] += len(matches)
                stats["modifications"].append({
                    "action": "replace",
                    "old_tag": old_tag,
                    "new_tag": new_tag,
                    "count": len(matches),
                })

    # Phase 3: 中频标签替换
    if phase in ["medium", "all"]:
        for old_tag, new_tag in MEDIUM_PRIORITY_MAPPINGS.items():
            pattern = r'\b' + re.escape(old_tag) + r'\b'
            matches = re.findall(pattern, content)
            if matches:
                content = re.sub(pattern, new_tag, content)
                stats["replaced_tags"] += len(matches)
                stats["modifications"].append({
                    "action": "replace",
                    "old_tag": old_tag,
                    "new_tag": new_tag,
                    "count": len(matches),
                })

    # Phase 4: 低频标签替换
    if phase in ["low", "all"]:
        for old_tag, new_tag in LOW_PRIORITY_MAPPINGS.items():
            pattern = r'\b' + re.escape(old_tag) + r'\b'
            matches = re.findall(pattern, content)
            if matches:
                content = re.sub(pattern, new_tag, content)
                stats["replaced_tags"] += len(matches)
                stats["modifications"].append({
                    "action": "replace",
                    "old_tag": old_tag,
                    "new_tag": new_tag,
                    "count": len(matches),
                })

    # 清理多余的空行（删除标签后可能产生的空行）
    content = re.sub(r'\n\s*\n\s*\n', '\n\n', content)

    return content, stats


def process_file(file_path: Path, phase: str = "all", dry_run: bool = False) -> Dict:
    """
    处理单个文件

    Args:
        file_path: 文件路径
        phase: 执行阶段
        dry_run: 是否为预览模式

    Returns:
        处理统计信息
    """
    try:
        content = file_path.read_text(encoding='utf-8')
    except Exception as e:
        return {"error": str(e)}

    new_content, stats = normalize_tags_in_content(content, phase)

    # 如果没有修改，返回空统计
    if not stats["modifications"]:
        return {}

    # 如果是预览模式，只返回统计信息
    if dry_run:
        return stats

    # 创建备份
    backup_path = create_backup_path(file_path)
    try:
        file_path.rename(backup_path)
    except Exception as e:
        return {"error": f"备份失败: {str(e)}"}

    # 写入新内容
    try:
        file_path.write_text(new_content, encoding='utf-8')
    except Exception as e:
        # 如果写入失败，恢复备份
        backup_path.rename(file_path)
        return {"error": f"写入失败: {str(e)}"}

    return stats


def main():
    """主函数"""
    parser = argparse.ArgumentParser(
        description="标签规范化脚本 - GitHub Issue #1",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  %(prog)s --dry-run           # 预览模式（不修改文件）
  %(prog)s --phase invalid    # 删除无效标签
  %(prog)s --phase high       # 替换高频标签
  %(prog)s --phase all        # 执行所有替换
        """
    )

    parser.add_argument(
        "--phase",
        choices=["invalid", "high", "medium", "low", "all"],
        default="all",
        help="执行阶段 (默认: all)"
    )

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="预览模式，不修改文件"
    )

    parser.add_argument(
        "--dir",
        choices=NOTE_DIRECTORIES,
        help="只处理指定目录（默认处理所有目录）"
    )

    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="显示详细信息"
    )

    args = parser.parse_args()

    # 确定要处理的目录
    if args.dir:
        directories = [Path(args.dir)]
    else:
        directories = [Path(d) for d in NOTE_DIRECTORIES]

    # 统计信息
    total_stats = {
        "total_files": 0,
        "updated_files": 0,
        "deleted_tags": 0,
        "replaced_tags": 0,
        "errors": [],
    }

    print(f"🚀 开始标签规范化 (Phase: {args.phase})")
    print(f"📁 处理目录: {[str(d) for d in directories]}")
    print(f"🔍 预览模式: {'是' if args.dry_run else '否'}")
    print("=" * 60)

    # 处理每个目录
    for note_dir in directories:
        if not note_dir.exists():
            print(f"⚠️  跳过不存在的目录: {note_dir}")
            continue

        print(f"\n📂 扫描目录: {note_dir}")

        # 查找所有 Markdown 文件
        for md_file in note_dir.rglob("*.md"):
            total_stats["total_files"] += 1

            # 处理文件
            result = process_file(md_file, phase=args.phase, dry_run=args.dry_run)

            # 处理错误
            if "error" in result:
                total_stats["errors"].append({
                    "file": str(md_file),
                    "error": result["error"],
                })
                if args.verbose:
                    print(f"❌ 错误: {md_file}")
                    print(f"   {result['error']}")
                continue

            # 如果没有修改，跳过
            if not result:
                continue

            total_stats["updated_files"] += 1
            total_stats["deleted_tags"] += result.get("deleted_tags", 0)
            total_stats["replaced_tags"] += result.get("replaced_tags", 0)

            # 显示详细信息
            if args.verbose:
                print(f"✅ {md_file}")
                for mod in result["modifications"]:
                    if mod["action"] == "delete":
                        print(f"   删除: {mod['tag']} ({mod['count']}次)")
                    else:
                        print(f"   替换: {mod['old_tag']} → {mod['new_tag']} ({mod['count']}次)")

    # 打印统计信息
    print("\n" + "=" * 60)
    print("📊 统计信息:")
    print(f"  扫描文件: {total_stats['total_files']}")
    print(f"  更新文件: {total_stats['updated_files']}")
    print(f"  删除标签: {total_stats['deleted_tags']} 次")
    print(f"  替换标签: {total_stats['replaced_tags']} 次")

    if total_stats['errors']:
        print(f"  错误数量: {len(total_stats['errors'])}")
        if args.verbose:
            print("\n❌ 错误详情:")
            for err in total_stats['errors']:
                print(f"  {err['file']}")
                print(f"  {err['error']}")

    # 更新率
    if total_stats['total_files'] > 0:
        update_rate = total_stats['updated_files'] / total_stats['total_files'] * 100
        print(f"  更新率: {update_rate:.1f}%")

    print("=" * 60)

    # 保存统计信息到 JSON
    stats_file = Path("tag_normalization_stats.json")
    stats_data = {
        "timestamp": datetime.now().isoformat(),
        "phase": args.phase,
        "dry_run": args.dry_run,
        "stats": total_stats,
    }
    stats_file.write_text(json.dumps(stats_data, indent=2, ensure_ascii=False), encoding='utf-8')
    print(f"💾 统计信息已保存到: {stats_file}")

    if not args.dry_run:
        print("\n✅ 完成！请检查修改后的文件。")
        print("💡 提示: 备份文件使用 .bak 后缀，确认无误后可删除。")
    else:
        print("\n⚠️  预览模式完成，未修改任何文件。")
        print("💡 提示: 使用 --phase all 执行实际替换。")


if __name__ == "__main__":
    main()
