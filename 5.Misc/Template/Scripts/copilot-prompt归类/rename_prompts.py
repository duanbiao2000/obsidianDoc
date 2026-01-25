#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Copilot 提示词批量重命名脚本
根据分类映射表添加前缀代码
"""

import os
import shutil

# 基础目录
base_dir = r"D:\迅雷下载\@同步文件\OneDrive\obsidianDoc\5.Misc\copilot-custom-prompts"

# 重命名映射表
rename_map = {
    "04推理扩展.md": "TH-04推理扩展.md",
    "10%核心要素识别.md": "KM-10%核心要素识别.md",
    "200字卡片笔记.md": "KM-200字卡片笔记.md",
    "4D 笔记重构助手.md": "KM-4D 笔记重构助手.md",
    "AI writing tutor.md": "WR-AI writing tutor.md",
    "AI 诤友.md": "RL-AI 诤友.md",
    "AI精英学院™课程页面开发规范.md": "TD-AI精英学院课程页面开发规范.md",
    "Alias-系统基础设施栈.md": "TD-Alias-系统基础设施栈.md",
    "Anki 闪卡生成器和知识萃取专家-flashcard语法.md": "LR-Anki闪卡生成器和知识萃取专家.md",
    "Canvas笔记生成器.md": "KM-Canvas笔记生成器.md",
    "Cheat Sheet.md": "META-Cheat Sheet.md",
    "C-level知识架构顾问-Fits-in核查.md": "RL-C-level知识架构顾问.md",
    "Compare&Contrast.md": "TH-Compare&Contrast.md",
    "CoT 增强版系统提示词.md": "META-CoT增强版系统提示词.md",
    "debate辩论性分析.md": "TH-debate辩论性分析.md",
    "DIKW金字塔模型.md": "TH-DIKW金字塔模型.md",
    "empirical evidence风格重写.md": "WR-empirical evidence风格重写.md",
    "Excalidraw图表生成PROMPT.md": "TD-Excalidraw图表生成PROMPT.md",
    "For High-IQ one-screen summary.md": "KM-For High-IQ one-screen summary.md",
    "FQA反复提问选择题.md": "LR-FQA反复提问选择题.md",
    "FQA反复提问间隔复习版.md": "LR-FQA反复提问间隔复习版.md",
    "Google Calendar 日历生成器(debug).md": "MISC-Google Calendar日历生成器.md",
    "GRE英文写作大师.md": "WR-GRE英文写作大师.md",
    "Hierarchy is  everything.md": "TH-Hierarchy is everything.md",
    "HTML页面生成与排版优化.md": "TD-HTML页面生成与排版优化.md",
    "IELTS-style essay.md": "WR-IELTS-style essay.md",
    "LFSP风格AI助手.md": "TD-LFSP风格AI助手.md",
    "life coach.md": "RL-life coach.md",
    "Lisa对知识充满渴望和好奇的机器人助理.md": "RL-Lisa知识渴望助理.md",
    "LLM指令架构师.md": "META-LLM指令架构师.md",
    "manictime今日活动日志分析.md": "DA-manictime今日活动日志分析.md",
    "Master Prompt逆向工程提示词生成器.md": "META-Master Prompt逆向工程提示词生成器.md",
    "Mermaid-实体关系图.md": "TD-Mermaid实体关系图.md",
    "Next Step.md": "MISC-Next Step.md",
    "Notion AI 主要功能提示词合集.md": "MISC-Notion AI主要功能提示词合集.md",
    "NPL语义分析.md": "DA-NPL语义分析.md",
    "Obsidian2Anki题目生成.md": "LR-Obsidian2Anki题目生成.md",
    "O'Reilly传奇技术编辑.md": "RL-OReilly传奇技术编辑.md",
    "PALC结构分析器.md": "TH-PALC结构分析器.md",
    "PERE元认知引擎-结构化目标.md": "TH-PERE元认知引擎.md",
    "PracticalExample.md": "MISC-PracticalExample.md",
    "PRD全链路分析与设计.md": "TD-PRD全链路分析与设计.md",
    "python之禅三原则(reflective).md": "TD-python之禅三原则.md",
    "ReAct AI执行代理.md": "META-ReAct AI执行代理.md",
    "Roast writing  and give actionable feedback.md": "WR-Roast writing and feedback.md",
    "ROI重构.md": "TH-ROI重构.md",
    "Role_ 资深全栈架构师 (GolangAngular).md": "RL-Role_资深全栈架构师.md",
    "Role_ 运动教练.md": "RL-Role_运动教练.md",
    "Role_CEO沉浸式模拟版.md": "RL-Role_CEO沉浸式模拟版.md",
    "Role_完型填空生成.md": "WR-Role_完型填空生成.md",
    "Role_心理医生.md": "RL-Role_心理医生.md",
    "Role_提示词增强_Senior Prompt Engineering Consultant.md": "META-Role_提示词增强顾问.md",
    "Role_网站设计顾问.md": "RL-Role_网站设计顾问.md",
    "SCQRA提问框架.md": "TH-SCQRA提问框架.md",
    "spoken English teacher and improver.md": "WR-spoken English teacher.md",
    "Steve Jobs (Visionary Storyteller).md": "RL-Steve Jobs Storyteller.md",
    "Storyteller.md": "WR-Storyteller.md",
    "storyteller-结构化故事生成引擎.md": "WR-storyteller结构化故事生成引擎.md",
    "TL;DR summary.md": "KM-TL;DR summary.md",
    "TodoList.md": "MISC-TodoList.md",
    "Top1%程序员的硬核视角与逻辑思维.md": "TD-Top1%程序员视角与逻辑.md",
    "ToT策略优化.md": "TH-ToT策略优化.md",
    "web design consultant.md": "RL-web design consultant.md",
    "Zettelkasten 卡片生成器.md": "KM-Zettelkasten卡片生成器.md",
    "Zettelkasten_洞见笔记.md": "KM-Zettelkasten洞见笔记.md",
    "Zettelkasten英文卡片生成器.md": "KM-Zettelkasten英文卡片生成器.md",
    "一句话论文.md": "WR-一句话论文.md",
    "一页法则战略顾问.md": "RL-一页法则战略顾问.md",
    "三阶思考.md": "TH-三阶思考.md",
    "上下文工程专家.md": "TD-上下文工程专家.md",
    "专业笔记优化助手.md": "KM-专业笔记优化助手.md",
    "专业认知激活提示词创建框架.md": "META-专业认知激活提示词创建框架.md",
    "两阶段聚焦工作流.md": "TH-两阶段聚焦工作流.md",
    "严谨且善于解释的助手附思路与推理过程.md": "TH-严谨解释助手附推理过程.md",
    "个体发展刻意练习理论CLO.md": "LR-个体发展刻意练习理论.md",
    "主题追问问题生成器.md": "TH-主题追问问题生成器.md",
    "二八定律+实用主义.md": "TH-二八定律实用主义.md",
    "交互式探索者Lisa.md": "RL-交互式探索者Lisa.md",
    "交互式苏格拉底诘问引擎.md": "TH-交互式苏格拉底诘问引擎.md",
    "产品经理式问题解决方案.md": "TD-产品经理式问题解决方案.md",
    "代码审查专家.md": "TD-代码审查专家.md",
    "代码解释.md": "TD-代码解释.md",
    "以 Brian Kernighan 为原型的 AI 助手角色设定.md": "RL-Brian Kernighan AI助手.md",
    "任务分解专家.md": "TH-任务分解专家.md",
    "作者认知与方法论审阅者.md": "KM-作者认知与方法论审阅者.md",
    "保罗·格雷厄姆PG视角.md": "TH-保罗格雷厄姆PG视角.md",
    "借助已有经验使得抽象概念可感知.md": "TH-借助经验使抽象概念可感知.md",
    "全维度批判性审计师.md": "TH-全维度批判性审计师.md",
    "关键概念提取与应用路径分析.md": "KM-关键概念提取与应用路径分析.md",
    "决策科学顾问.md": "TH-决策科学顾问.md",
    "分层知识重构引擎.md": "KM-分层知识重构引擎.md",
    "分治法笔记重构专家.md": "KM-分治法笔记重构专家.md",
    "动态规划知识架构师.md": "KM-动态规划知识架构师.md",
    "升维思考.md": "TH-升维思考.md",
    "南科大每日三技能点.md": "LR-南科大每日三技能点.md",
    "原子代理内容生成器.md": "META-原子代理内容生成器.md",
    "可复用的知识单元风格改写.md": "KM-可复用的知识单元风格改写.md",
    "可配置沟通助理.md": "RL-可配置沟通助理.md",
    "图式思考.md": "TH-图式思考.md",
    "基于 CIS 架构的 ToT 扩展.md": "TH-基于CIS架构的ToT扩展.md",
    "复杂性分析-分层抽象.md": "TH-复杂性分析分层抽象.md",
    "多Agent自适应内容生成.md": "META-多Agent自适应内容生成.md",
    "大纲格式结构化笔记.md": "KM-大纲格式结构化笔记.md",
    "如何有效地学习和传授知识.md": "LR-如何有效地学习和传授知识.md",
    "学术情报分析师.md": "KM-学术情报分析师.md",
    "审视者角度更清晰高效.md": "TH-审视者角度更清晰高效.md",
    "对文件夹进行语义分析.md": "DA-对文件夹进行语义分析.md",
    "工程学思维通用提示词.md": "TH-工程学思维通用提示词.md",
    "建模分析.md": "TH-建模分析.md",
    "引入名人名言.md": "WR-引入名人名言.md",
    "归纳推理引擎.md": "TH-归纳推理引擎.md",
    "心智模型-原子笔记.md": "KM-心智模型原子笔记.md",
    "心理认知助手.md": "RL-心理认知助手.md",
    "快速内容价值评估.md": "KM-快速内容价值评估.md",
    "快速理解代码的实战提示词.md": "TD-快速理解代码的实战提示词.md",
    "思想精炼与重塑.md": "TH-思想精炼与重塑.md",
    "思维导图大纲.md": "KM-思维导图大纲.md",
    "技术术语表构建器.md": "TD-技术术语表构建器.md",
    "技术知识萃取专家.md": "TD-技术知识萃取专家.md",
    "抽象层次分析器.md": "TH-抽象层次分析器.md",
    "提问-通用思维模式-元认知式提问.md": "TH-通用思维模式元认知式提问.md",
    "文本视觉优化专家.md": "WR-文本视觉优化专家.md",
    "明确意图-沟通价值与可维护.md": "TH-明确意图沟通价值与可维护.md",
    "智能笔记诊断师.md": "KM-智能笔记诊断师.md",
    "条件性反射提问.md": "TH-条件性反射提问.md",
    "极简主义技术文档专家.md": "WR-极简主义技术文档专家.md",
    "极简版.md": "MISC-极简版.md",
    "案例驱动学习系统.md": "LR-案例驱动学习系统.md",
    "概念剖析机.md": "TH-概念剖析机.md",
    "概念压缩包.md": "KM-概念压缩包.md",
    "模式调用-Plan then Execution.md": "TH-模式调用Plan then Execution.md",
    "求实型问题分析助手.md": "TH-求实型问题分析助手.md",
    "洞见提取器.md": "TH-洞见提取器.md",
    "深度复盘私人教练.md": "LR-深度复盘私人教练.md",
    "深度思考引路人.md": "TH-深度思考引路人.md",
    "深度提问并Wiki回答.md": "TH-深度提问并Wiki回答.md",
    "深度文本架构师.md": "WR-深度文本架构师.md",
    "深度研读与学术分析助手.md": "KM-深度研读与学术分析助手.md",
    "深度笔记精炼师.md": "KM-深度笔记精炼师.md",
    "深度系统架构师.md": "TD-深度系统架构师.md",
    "清晰化表达.md": "WR-清晰化表达.md",
    "清晰度审计与重构器.md": "KM-清晰度审计与重构器.md",
    "清晰度架构师.md": "TH-清晰度架构师.md",
    "狐狸博士教师型AI.md": "RL-狐狸博士教师型AI.md",
    "独立开发者兼产品创意.md": "RL-独立开发者兼产品创意.md",
    "独立理解重构.md": "KM-独立理解重构.md",
    "知识产品设计师.md": "KM-知识产品设计师.md",
    "知识图谱构建分析师.md": "KM-知识图谱构建分析师.md",
    "知识架构师：对笔记进行深度重构与升华.md": "RL-知识架构师笔记深度重构与升华.md",
    "知识架构顾问-Fits-in核查.md": "RL-知识架构顾问Fits-in核查.md",
    "知识爆破手.md": "KM-知识爆破手.md",
    "知识精炼.md": "KM-知识精炼.md",
    "知识蒸馏架构师.md": "KM-知识蒸馏架构师.md",
    "知识解构.md": "KM-知识解构.md",
    "知识重构工程师.md": "KM-知识重构工程师.md",
    "硅谷技术布道师.md": "RL-硅谷技术布道师.md",
    "科学记忆阅读法助手.md": "LR-科学记忆阅读法助手.md",
    "笔记反向工程分析师.md": "KM-笔记反向工程分析师.md",
    "笔记核心要点速览.md": "KM-笔记核心要点速览.md",
    "笔记模块化-正交设计原则.md": "KM-笔记模块化正交设计原则.md",
    "笔记深度重构与洞察提取.md": "KM-笔记深度重构与洞察提取.md",
    "笔记结构化处理器.md": "KM-笔记结构化处理器.md",
    "笔记降熵重构.md": "KM-笔记降熵重构.md",
    "第一性原理思考者.md": "TH-第一性原理思考者.md",
    "策略结晶采集器.md": "TH-策略结晶采集器.md",
    "系统化提问.md": "TH-系统化提问.md",
    "系统思考架构师.md": "TH-系统思考架构师.md",
    "系统架构演进.md": "TD-系统架构演进.md",
    "红队逻辑审计师.md": "TH-红队逻辑审计师.md",
    "结构化思维专家.md": "TH-结构化思维专家.md",
    "结构化拆解能力-Task Grpah建模(工程,战略,心理三维视角).md": "TH-结构化拆解能力Task Graph建模.md",
    "自动化方案设计助手.md": "TD-自动化方案设计助手.md",
    "自定义风格写作编辑.md": "WR-自定义风格写作编辑.md",
    "苏格拉底式提问.md": "TH-苏格拉底式提问.md",
    "苏菲式认知重构元提示词.md": "TH-苏菲式认知重构元提示词.md",
    "英文严谨性表达理论框架.md": "WR-英文严谨性表达理论框架.md",
    "认知审计员 (Cognitive Auditor).md": "TH-认知审计员.md",
    "认知追问框架.md": "TH-认知追问框架.md",
    "认知降噪专家.md": "TH-认知降噪专家.md",
    "记忆增强专家.md": "LR-记忆增强专家.md",
    "记忆测验-选择与论述.md": "LR-记忆测验选择与论述.md",
    "论题与结论.md": "TH-论题与结论.md",
    "证伪分析提示词.md": "TH-证伪分析提示词.md",
    "语义压缩高价值内容提取器.md": "KM-语义压缩高价值内容提取器.md",
    "语义建模与知识工程专家.md": "KM-语义建模与知识工程专家.md",
    "费曼与第一性原理笔记精简.md": "KM-费曼与第一性原理笔记精简.md",
    "费曼学习法教学专家.md": "LR-费曼学习法教学专家.md",
    "费曼第一原理排除法.md": "TH-费曼第一原理排除法.md",
    "资深文本挖掘与知识管理专家.md": "KM-资深文本挖掘与知识管理专家.md",
    "跨学科审核校对.md": "KM-跨学科审核校对.md",
    "跨界策略顾问模式.md": "RL-跨界策略顾问模式.md",
    "追问式提问.md": "TH-追问式提问.md",
    "退后提示 (Step-back Prompting).md": "TH-退后提示Step-back Prompting.md",
    "适时追问.md": "TH-适时追问.md",
    "逻辑审计流水线.md": "TH-逻辑审计流水线.md",
    "长青笔记重构器.md": "KM-长青笔记重构器.md",
    "领域专家.md": "RL-领域专家.md",
    "首席战略架构师.md": "RL-首席战略架构师.md",
    "首席技术专家.md": "RL-首席技术专家.md",
    "首席智库专家.md": "RL-首席智库专家.md",
    "首席逻辑官.md": "TH-首席逻辑官.md",
    "香港DSE顶流补习名师.md": "RL-香港DSE顶流补习名师.md",
    "高效学习卡片生成器.md": "KM-高效学习卡片生成器.md",
    "高级学术研究与分析系统.md": "KM-高级学术研究与分析系统.md",
}

def main():
    os.chdir(base_dir)

    success_count = 0
    fail_count = 0
    failed_files = []

    for old_name, new_name in rename_map.items():
        old_path = os.path.join(base_dir, old_name)
        new_path = os.path.join(base_dir, new_name)

        if os.path.exists(old_path):
            try:
                os.rename(old_path, new_path)
                # 简化输出以避免编码问题
                print(f"[OK] {new_name}")
                success_count += 1
            except Exception as e:
                print(f"[FAIL] {old_name}: {e}")
                fail_count += 1
                failed_files.append(f"{old_name} -> {new_name}: {e}")
        else:
            print(f"[SKIP] {old_name}")

    print(f"\n=== Done ===")
    print(f"Success: {success_count}")
    print(f"Failed: {fail_count}")

    if failed_files:
        print("\nFailed:")
        for f in failed_files:
            print(f"  - {f}")

if __name__ == "__main__":
    main()
