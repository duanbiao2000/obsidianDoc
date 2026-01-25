#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
0.DailyNotes 自动化分类脚本
扫描 0.DailyNotes/ 和 0.DailyNotes/0.mindset/ 所有 .md 文件
根据规则自动分类，去除日期前缀，输出 classification_plan.csv
"""

import os
import re
import csv
from collections import defaultdict


def extract_title_from_filename(filename):
    """从文件名中提取标题，去除日期前缀"""
    original = filename

    # 格式1: YYYY-MM-DD-标题.md -> 标题.md
    match = re.match(r"^(\d{4}-\d{2}-\d{2})-(.+\.md)$", filename)
    if match:
        return match.group(2)

    # 格式2: YYYY-MM-DD- 标题.md -> 标题.md（去除前导空格）
    match = re.match(r"^\d{4}-\d{2}-\d{2}-\s+(.+\.md)$", filename)
    if match:
        return match.group(1).strip()

    # 格式3: YYYY-MM-DD标题.md -> 标题.md
    match = re.match(r"^\d{4}-\d{2}-\d{2}(.+\.md)$", filename)
    if match:
        return match.group(1)

    # 格式4: YYYYMMDD - 标题.md -> 标题.md
    match = re.match(r"^\d{8}\s*-\s*(.+\.md)$", filename)
    if match:
        return match.group(1)

    # 格式5: YYYY-MM-DD - 标题.md (带空格）-> 标题.md
    match = re.match(r"^\d{4}-\d{2}-\d{2}\s+-\s*(.+\.md)$", filename)
    if match:
        return match.group(1)

    # 特殊格式：2025-W##.md (周复盘）保留
    if re.match(r"^\d{4}-W\d{2}\.md$", filename):
        return filename

    # 无日期前缀
    return original


def is_special_file(filename, filepath):
    """判断是否为特殊文件"""
    # 模板文件
    if filename.startswith("@"):
        return True, "模板文件"

    # 索引文件
    if filename.startswith("_Index_of_"):
        return True, "索引文件"

    # 空文件或系统文件
    if filename.startswith("."):
        return True, "系统文件"

    # 周复盘文件
    if re.match(r"^\d{4}-W\d{2}\.md$", filename):
        return True, "周复盘"

    return False, None


def classify_note(filename, content):
    """根据规则分类笔记"""

    # 先检查是否为特殊文件
    is_special, special_type = is_special_file(filename, filename)
    if is_special:
        return "0.DailyNotes/特殊文件/", "SPECIAL", special_type

    # 规则组 A: 编程语言与技术栈 → 2.Topics/Coding/语言指南/
    language_keywords = [
        "Java",
        "Python",
        "Rust",
        "Go",
        "Golang",
        "JavaScript",
        "TypeScript",
        "SQL",
        "C\\+\\+",
        "Kotlin",
        "Swift",
        "Django",
        "FastAPI",
        "React",
        "Vue",
        "Spring",
        "Flask",
        "CPython",
        "Pydantic",
    ]

    for lang in language_keywords:
        if re.search(lang, filename, re.IGNORECASE):
            return "2.Topics/Coding/语言指南/", "HIGH", f"A1-语言:{lang}"

    # 规则组 B: 系统设计/架构 → 2.Topics/Coding/系统设计/
    system_design_keywords = [
        "系统设计",
        "架构",
        "分布式",
        "微服务",
        "高并发",
        "推荐系统",
        "12-Factor",
        "实时应用",
        "B站",
    ]

    for keyword in system_design_keywords:
        if keyword in filename:
            return "2.Topics/Coding/系统设计/", "HIGH", f"B1-{keyword}"

    # 内容关键词检测（系统设计）
    if content:
        content_lower = content.lower()
        if any(
            k in content_lower
            for k in ["系统架构", "架构模式", "秒杀", "削峰", "限流", "负载均衡"]
        ):
            return "2.Topics/Coding/系统设计/", "HIGH", "B2-内容关键词"

    # 规则组 C: AI与大模型 → 2.Topics/Coding/AI与大模型/
    ai_keywords = [
        "AI",
        "GPT",
        "LLM",
        "大模型",
        "Copilot",
        "Fabric",
        "Agent",
        "LangGraph",
        "智能",
        "协作白皮书",
        "FabricAI",
    ]

    for keyword in ai_keywords:
        if keyword in filename:
            return "2.Topics/Coding/AI与大模型/", "HIGH", f"C1-{keyword}"

    # 内容关键词检测（AI）
    if content:
        content_lower = content.lower()
        if "prompt" in content_lower:
            if any(k in content_lower for k in ["上下文工程", "提示词", "元提示"]):
                return "2.Topics/Coding/AI与大模型/", "HIGH", "C2-Prompt"

    # 规则组 D: 工程实践 → 2.Topics/Coding/工程实践/
    practice_keywords = [
        "TDD",
        "Code Review",
        "代码质量",
        "测试",
        "开源",
        "Spec-Driven",
        "Design Thinking",
        "开发标记",
    ]

    for keyword in practice_keywords:
        if keyword in filename:
            return "2.Topics/Coding/工程实践/", "HIGH", f"D1-{keyword}"

    # 内容关键词检测（工程实践）
    if content:
        content_lower = content.lower()
        if any(k in content_lower for k in ["测试", "代码审查", "重构", "最佳实践"]):
            return "2.Topics/Coding/工程实践/", "MEDIUM", "D2-内容关键词"

    # 规则组 E: 数据库与存储 → 2.Topics/Coding/数据库与存储/
    db_keywords = [
        "PostgreSQL",
        "Redis",
        "MySQL",
        "MongoDB",
        "数据库",
        "存储",
        "消息队列",
        "中间件",
    ]

    for keyword in db_keywords:
        if keyword in filename:
            return "2.Topics/Coding/数据库与存储/", "HIGH", f"E1-{keyword}"

    # 内容关键词检测（数据库）
    if content:
        content_lower = content.lower()
        if any(k in content_lower for k in ["数据库", "缓存", "消息队列", "持久化"]):
            return "2.Topics/Coding/数据库与存储/", "MEDIUM", "E2-内容关键词"

    # 规则组 F1: 认知科学/思维模型 → 2.Topics/认知科学/思维模型/
    mindset_keywords = [
        "YAGNI",
        "蜜蜂算法",
        "思维",
        "决策",
        "模型",
        "第一性原理",
        "抽象",
        "思维链",
        "机器思维",
        "hacker",
    ]

    for keyword in mindset_keywords:
        if keyword in filename:
            return "2.Topics/认知科学/思维模型/", "HIGH", f"F1-{keyword}"

    # 规则组 F2: 认知科学/决策框架
    decision_keywords = ["决策", "策略", "优先级", "帕累托", "37 signals"]

    for keyword in decision_keywords:
        if keyword in filename:
            return "2.Topics/认知科学/决策框架/", "HIGH", f"F2-{keyword}"

    # 规则组 F3: 认知科学/行动协议
    action_keywords = ["行动", "触发", "协议", "原则", "每日固定"]

    for keyword in action_keywords:
        if keyword in filename:
            return "2.Topics/认知科学/行动协议/", "HIGH", f"F3-{keyword}"

    # 规则组 F4: 认知科学/学习系统
    learning_keywords = ["学习", "笔记", "PKM", "知识库", "程序员的逻辑整理"]

    for keyword in learning_keywords:
        if keyword in filename:
            return "2.Topics/认知科学/学习系统/", "HIGH", f"F4-{keyword}"

    # 规则组 G1: 个人效能/职业发展
    career_keywords = [
        "职业",
        "工程师",
        "幸福",
        "薪资",
        "成长",
        "晋升",
        "Effective Engineer",
    ]

    for keyword in career_keywords:
        if keyword in filename:
            return "2.Topics/个人效能/职业发展/", "HIGH", f"G1-{keyword}"

    # 规则组 G2: 个人效能/生产力系统
    productivity_keywords = ["生产力", "效率", "复利", "习惯", "精英", "每日"]

    for keyword in productivity_keywords:
        if keyword in filename:
            return "2.Topics/个人效能/生产力系统/", "HIGH", f"G2-{keyword}"

    # 规则组 H: 健康与健身 → 2.Topics/健康生活/训练协议/
    health_keywords = ["健身", "训练", "HIIT", "运动", "塑形", "营养"]

    for keyword in health_keywords:
        if keyword in filename:
            return "2.Topics/健康生活/训练协议/", "HIGH", f"H1-{keyword}"

    # 规则组 I1: 写作与英语/英语学习
    english_keywords = ["DSE", "写作", "英文", "英语", "粤语", "DES"]

    for keyword in english_keywords:
        if keyword in filename:
            if (
                "DSE" in keyword
                or "英文" in keyword
                or "英语" in keyword
                or "粤语" in keyword
                or "DES" in keyword
            ):
                return "2.Topics/写作与英语/英语学习/", "HIGH", f"I1-{keyword}"

    # 规则组 I2: 写作与英语/写作技巧
    if "写作" in filename:
        return "2.Topics/写作与英语/写作技巧/", "HIGH", f"I2-写作"

    # 内容关键词检测（写作）
    if content and "写作" in content.lower():
        return "2.Topics/写作与英语/写作技巧/", "MEDIUM", "I2-内容关键词"

    # 规则组 J: 创业与产品 → 2.Topics/创业与产品/
    business_keywords = ["创业", "产品经理", "PRD", "MVP", "商业模式", "商业", "Bezos"]

    for keyword in business_keywords:
        if keyword in filename:
            return "2.Topics/创业与产品/", "HIGH", f"J-{keyword}"

    # 规则组 K1: 学习资料/学习路径 → 3.Resources/学习资料/学习路径/
    learning_path_keywords = [
        "学习计划",
        "Roadmap",
        "LeetCode",
        "学习路径",
        "Baby Steps",
    ]

    for keyword in learning_path_keywords:
        if keyword in filename:
            return "3.Resources/学习资料/学习路径/", "HIGH", f"K1-{keyword}"

    # 规则组 K2: 日志/趋势预测
    trend_keywords = ["趋势", "预测"]

    for keyword in trend_keywords:
        if keyword in filename:
            return "3.Resources/日志/趋势预测/", "HIGH", f"K2-{keyword}"

    # 规则组 K3: 日志/周复盘 (已在前面的 is_special_file 处理)

    # 未分类
    return "UNCATEGORIZED", "LOW", "未匹配任何规则"


def main():
    """主函数"""
    results = []
    stats = defaultdict(int)
    stats_by_folder = defaultdict(int)

    base_dir = "0.DailyNotes"

    # 扫描文件
    for root, dirs, files in os.walk(base_dir):
        # 跳过 .obsidian 等系统文件夹
        if ".obsidian" in root or ".git" in root:
            continue

        for file in files:
            if not file.endswith(".md"):
                continue

            filepath = os.path.join(root, file)

            # 读取文件内容（仅前2000字符用于分类）
            content = ""
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read(2000)
            except Exception as e:
                print(f"警告：无法读取文件 {filepath}: {e}")

            # 提取标题
            new_title = extract_title_from_filename(file)

            # 分类
            target_folder, confidence, rule_id = classify_note(file, content)
            target_path = os.path.join(target_folder, new_title)

            # 统计
            stats[confidence] += 1
            stats_by_folder[target_folder] += 1

            results.append(
                {
                    "source_path": filepath,
                    "target_path": target_path,
                    "confidence": confidence,
                    "matched_rule": rule_id,
                    "old_title": file,
                    "new_title": new_title,
                }
            )

    # 输出 CSV
    with open("classification_plan.csv", "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "source_path",
                "target_path",
                "confidence",
                "matched_rule",
                "old_title",
                "new_title",
            ],
        )
        writer.writeheader()
        writer.writerows(results)

    # 打印统计
    print(f"=" * 60)
    print(f"分类完成，共处理 {len(results)} 个文件")
    print(f"建议已保存到 classification_plan.csv")
    print(f"=" * 60)
    print(f"\n置信度统计:")
    for confidence, count in sorted(stats.items()):
        print(f"  {confidence}: {count}")

    print(f"\n分类统计:")
    for folder, count in sorted(
        stats_by_folder.items(), key=lambda x: x[1], reverse=True
    ):
        print(f"  {folder}: {count}")

    print(f"=" * 60)


if __name__ == "__main__":
    main()
