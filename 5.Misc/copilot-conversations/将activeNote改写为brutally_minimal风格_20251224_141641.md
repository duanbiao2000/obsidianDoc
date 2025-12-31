---
epoch: 1766557001367
modelKey: gemini-3-flash-preview|google
tags:
  - copilot-conversation
topic: Brutally Minimal Note Rewriting
---

**user**: 将{activeNote}改写为brutally minimal风格
[Context: Notes: 0.DailyNotes/2025-12-21-高性能, 推理密集与现实业务关系.md]
[Timestamp: 2025/12/24 14:16:41]

**ai**: 以下是 [[2025-12-21-高性能, 推理密集与现实业务关系]] 的极简改写版本：

# 模型选型逻辑

- **L1：低成本 / 单工具** (`gpt-4o-mini`)
  - **场景**：客服 FAQ、订单查询、表单校验、简单 RAG。
  - **核心**：高并发、低复杂度、单次调用。

- **L2：高性能 / 多工具** (`gpt-4o`)
  - **场景**：全流程 Agent、金融投研、自动化运维、营销自动化。
  - **核心**：并行调用、状态跟踪、任务规划。

- **L3：强推理 / 深度逻辑** (`o1` / `o3`)
  - **场景**：法律审计、复杂 Debug、科研评审、战略推演。
  - **核心**：慢思考（System 2）、自我验证、长逻辑链。

### 决策表

| 业务级别 | 推荐模型 | 核心优势 | |
| --- | --- | --- | --- |
| **基础型** | `4o-mini` | 极低成本 | |
| **协作型** | `4o` | 复杂规划 | |
| **专家型** | `o1` | 逻辑推导 | |
[Timestamp: 2025/12/24 14:16:50]

**user**: {activeNote} 同上
[Context: Notes: 0.DailyNotes/2025-12-19-极度耐心+极度爆发.md]
[Timestamp: 2025/12/24 14:18:33]