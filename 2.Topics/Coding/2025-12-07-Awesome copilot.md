---
aliases:
  - 项目规划与管理
date: 2025-12-07 18:25
tags:
source:
  - https://github.com/duanbiao2000/awesome-copilot
update:
rating:
related:
  - "[[prompts、instructions 和 chat modes]]"
  - "[[快速理解代码的实战提示词]]"
  - "[[两阶段聚焦工作流]]"
  - "[[Prompt管理科学]]"
  - "[[独立开发者兼产品创意]]"
view-count: 8
---

你提到的“项目规划与管理”主题下有 17 个项目，标签包括：planning, project-management, epic, feature, implementation, task, architecture, technical-spike。这些关键词代表了软件项目从宏观到微观、从战略到执行的一整套流程。

要让这些 prompt（或任务/活动）顺序执行或有效配合，可以按照典型的软件开发生命周期（SDLC）和敏捷项目管理方法（如 Scrum 或 SAFe）进行组织。以下是推荐的执行顺序与配合方式：

🧭 整体流程概览（自上而下 + 迭代反馈）

战略对齐 → 架构设计 → 史诗拆解 → 功能细化 → 任务分解 → 实施执行 → 技术探针验证 → 持续调整

🔢 分阶段执行顺序与配合建议
阶段 1：项目启动与战略对齐（Planning + Architecture）
目标：明确项目目标、范围、技术方向。
关键 Prompt / 活动：
“定义项目愿景与成功指标”
“识别核心用户故事与业务价值”
“制定高层架构方案（Architecture）”
产出：项目章程、技术栈选型、系统边界图。
✅ 配合：架构师 + 产品经理 + 技术负责人协作。

阶段 2：史诗（Epic）管理
目标：将战略目标拆解为可交付的大块能力。
关键 Prompt：
“将业务目标转化为 Epic”
“为每个 Epic 定义验收标准和依赖”
产出：Epic 列表（含优先级、粗略估算）。
✅ 配合：产品负责人主导，开发团队参与评审。

阶段 3：功能（Feature）分解
目标：将 Epic 拆分为更小的、跨职能的功能单元。
关键 Prompt：
“将 Epic X 拆解为具体 Feature”
“定义 Feature 的用户价值与验收条件”
产出：Feature 清单（可用于发布计划）。
✅ 配合：产品 + UX + 开发共同细化。

阶段 4：技术探针（Technical Spike）
目标：在不确定技术方案时，通过短期实验降低风险。
关键 Prompt：
“针对 [某技术难点] 设计 Technical Spike”
“Spike 的验收标准是什么？时间盒多长？”
产出：可行性报告、POC 代码、架构决策记录（ADR）。
✅ 配合：开发团队主导，限时执行（通常 1–3 天）。
⚠️ 注意：Spike 可在任何阶段插入（尤其是架构或功能设计阶段遇到不确定性时）。

阶段 5：实施规划（Implementation Planning）
目标：为即将开发的 Feature 制定实施策略。
关键 Prompt：
“为 Feature Y 制定实施路线图”
“识别微服务边界 / 数据模型 / API 契约”
产出：技术设计文档、接口定义、数据库 schema。
✅ 配合：Tech Lead + 后端/前端开发协同。

阶段 6：任务（Task）组织与分配
目标：将 Feature 拆为可分配、可估时的具体任务。
关键 Prompt：
“将 Feature Z 拆解为开发/测试/文档任务”
“估算任务工时，分配给团队成员”
产出：Jira / Trello / Azure DevOps 中的任务卡片。
✅ 配合：Scrum Master 协调，开发团队认领任务。

阶段 7：迭代执行与反馈闭环
在 Sprint 中执行任务，每日站会同步进展。
每个 Sprint 结束后回顾：是否需要新增 Spike？Epic 是否需调整？
持续配合：所有角色参与计划-执行-检查-改进（PDCA）循环。

🔄 如何配合使用这 17 个 Prompt？

假设你有一组预定义的 17 个 prompt（例如用于 AI 辅助生成内容），建议按以下方式组合：

阶段 使用的 Prompt 类型 示例

---

启动 planning, architecture “生成项目启动检查清单”
规划 epic, feature “将‘用户管理’需求转化为 3 个 Epic”
探索 technical-spike “为实时通知功能设计一个 WebSocket Spike”
执行 implementation, task “为登录功能生成后端任务列表”
管理 project-management “生成 Sprint 计划模板”
💡 技巧：不要线性执行所有 17 个，而是根据当前项目阶段动态选择相关 prompt，并允许回溯（如开发中发现架构问题，重新触发 architecture 或 spike prompt）。

✅ 最佳实践建议

1. 使用看板或 backlog 分层管理：Epic → Feature → Task。
2. Spike 作为特殊任务类型：标记为“研究类”，不直接交付用户价值，但降低风险。
3. 架构决策早期介入：避免后期大规模返工。
4. 自动化辅助：用 AI 工具根据 Epic 自动生成 Feature 草稿，再人工精炼。

如果你能提供这 17 个具体 prompt 的内容，我可以帮你设计一个精确的执行流程图或prompt 调用顺序脚本（例如用于 LangChain 或 AutoGen）。是否需要？
