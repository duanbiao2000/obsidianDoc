---
date: 2025-04-17 00:58
update: 2025-04-21 00:11
---

`samples/python/` 目录包含使用 Python 语言实现的 A2A 协议的示例代码。这些示例代码可以帮助开发者了解如何使用 A2A 协议构建 Agent 和客户端。

### 主要子目录和文件

- **`agents/`**: 包含各种 Agent 的示例代码。
- `crewai/`: 包含使用 CrewAI 框架实现的 Agent 示例。CrewAI 是一个用于构建多 Agent 系统的框架。
- `google_adk/`: 包含使用 Google ADK (Agent Development Kit) 实现的 Agent 示例。
- `langgraph/`: 包含使用 LangGraph 框架实现的 Agent 示例。LangGraph 是一个用于构建 Agent 图的框架。

  #A2A #Python #Tech/Agent #CrewAI #GoogleADK #LangGraph

  - `types.py`: 定义 A2A 协议中使用的数据模型类，例如 `Task`、`Message`、`Artifact` 等。

> [!NOTE]
> `Task`: 表示 Agent 需要执行的一项任务。它可能包含任务描述、输入数据、截止日期等信息。任务是 A2A 协议的核心概念，Agent 通过接收和执行任务来完成工作。 * **`Message`**: 表示 Agent 之间传递的消息。消息可以包含文本、数据、指令等内容。Agent 使用消息进行通信和协作。 * **`Artifact`**: 表示 Agent 生成的工件或成果。工件可以是文件、数据、报告等。Agent 通过生成工件来提供价值。

### 主要功能

- **Agent 示例**: 展示如何使用不同的框架（例如 CrewAI、Google ADK、LangGraph）构建 Agent。
- **客户端实现**: 提供 `A2AClient` 类，用于与 Agent 进行通信，发送任务、获取任务信息等。
- **服务端实现**: 提供 `A2AServer` 类，用于构建 A2A 服务，接收和处理客户端请求。
- **数据模型**: 定义 A2A 协议中使用的数据模型，例如 `Task`、`Message`、`Artifact` 等。
- **通用工具**: 提供一些通用的工具函数，例如用于验证输出模式是否兼容的函数。
