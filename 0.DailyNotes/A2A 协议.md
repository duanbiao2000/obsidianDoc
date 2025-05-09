---
date: 2025-04-17 00:58
update: 2025-04-23 18:50
tags:
  - DG/Seedling
---
该笔记介绍了 Python 实现 A2A 协议的示例代码，其核心在于理解协议交互所依赖的**三大基础数据模型**。这些模型定义在 `types.py` 文件中，是 Agent 间协同工作的关键载体：

1.  **Task (任务)**: 定义 Agent 需要执行的具体工作，包含描述和必要输入。它是驱动 Agent 行动的核心。
2.  **Message (消息)**: Agent 之间沟通和信息交换的载体，可包含文本、数据或指令。确保 Agent 间能有效协同。
3.  **Artifact (工件)**: Agent 完成任务后的产出或结果，是 Agent 工作价值的体现。

理解这三个模型（Task, Message, Artifact）对于使用或修改 `samples/python/` 目录下的任何 Agent 框架（如 CrewAI, Google ADK, LangGraph）示例至关重要，能够让你快速抓住重点，务实地解决基于 A2A 协议的开发问题。