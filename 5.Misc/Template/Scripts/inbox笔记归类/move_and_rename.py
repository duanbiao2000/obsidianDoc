#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
执行分类脚本 - 移动文件到目标位置，重命名（去除日期前缀）
读取 classification_plan.csv，处理文件名冲突，生成执行日志
"""

import os
import csv
import shutil
from pathlib import Path


def handle_conflict(target_path):
    """处理文件名冲突"""
    path = Path(target_path)
    base = path.stem
    ext = path.suffix
    counter = 1
    parent = path.parent

    while path.exists():
        new_name = f"{base}_v{counter}{ext}"
        path = parent / new_name
        counter += 1

    return str(path)


def move_file(source, target):
    """移动文件"""
    # 创建目标目录
    target_dir = os.path.dirname(target)
    os.makedirs(target_dir, exist_ok=True)

    # 处理冲突
    actual_target = handle_conflict(target)

    if actual_target != target:
        print(f"  [冲突] {target}")
        print(f"         -> {actual_target}")

    # 移动文件
    try:
        shutil.move(source, actual_target)
        return actual_target, True, None
    except Exception as e:
        return target, False, str(e)


def main():
    """主函数"""
    # 读取分类计划
    csv_path = "classification_plan.csv"

    with open(csv_path, "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    # 创建执行日志
    log_path = "execution_log.txt"
    moved_files = []
    failed_files = []

    with open(log_path, "w", encoding="utf-8") as log_file:
        log_file.write("=" * 60 + "\n")
        log_file.write("执行日志 - 文件移动与重命名\n")
        log_file.write("=" * 60 + "\n\n")

        for i, row in enumerate(rows, 1):
            source = row["source_path"]
            target = row["target_path"]
            old_title = row["old_title"]
            new_title = row["new_title"]

            log_file.write(f"[{i:3d}] {old_title}\n")
            log_file.write(f"  源路径: {source}\n")
            log_file.write(f"  目标路径: {target}\n")

            # 跳过特殊文件或未分类文件（移动到特殊文件夹）
            if target.startswith("UNCATEGORIZED"):
                log_file.write(f"  状态: 跳过（未分类）\n\n")
                continue

            # 执行移动
            actual_target, success, error = move_file(source, target)

            if success:
                log_file.write(f"  状态: 成功\n")
                log_file.write(f"  实际路径: {actual_target}\n")
                moved_files.append(
                    {
                        "source": source,
                        "target": actual_target,
                        "old_title": old_title,
                        "new_title": Path(actual_target).name,
                    }
                )
            else:
                log_file.write(f"  状态: 失败\n")
                log_file.write(f"  错误: {error}\n")
                failed_files.append(
                    {"source": source, "target": target, "error": error}
                )

            log_file.write("\n")

    # 写入统计
    with open(log_path, "a", encoding="utf-8") as log_file:
        log_file.write("=" * 60 + "\n")
        log_file.write("执行统计\n")
        log_file.write("=" * 60 + "\n")
        log_file.write(f"成功移动: {len(moved_files)}\n")
        log_file.write(f"失败: {len(failed_files)}\n")

        if failed_files:
            log_file.write("\n失败文件列表:\n")
            for i, f in enumerate(failed_files, 1):
                log_file.write(f"{i}. {f['source']}\n")
                log_file.write(f"   错误: {f['error']}\n")

    # 输出摘要
    print("=" * 60)
    print("执行完成")
    print("=" * 60)
    print(f"成功: {len(moved_files)}")
    print(f"失败: {len(failed_files)}")
    print(f"详细日志: {log_path}")

    # 生成已移动文件清单
    moved_csv = "moved_files.csv"
    with open(moved_csv, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(
            f, fieldnames=["source", "target", "old_title", "new_title"]
        )
        writer.writeheader()
        writer.writerows(moved_files)

    print(f"已移动文件清单: {moved_csv}")

    if failed_files:
        print("\n警告：有文件移动失败，请检查日志")
        return 1
    else:
        print("\n所有文件移动成功！")
        return 0


if __name__ == "__main__":
    exit(main())
