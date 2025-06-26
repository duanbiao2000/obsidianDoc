好的，根据KISS原则（Keep It Simple, Stupid / Keep It Short and Simple），以下是[[船员AI核心概念学习指南]]这篇笔记的改写：

---

## [[船员AI核心概念学习指南]] (KISS 版本)

**CrewAI 核心概念：用 AI 团队完成任务**

CrewAI 是一个框架，让你组织 AI 代理（Agent）像团队（Crew）一样协作，去完成你分配的任务（Task）。

**核心要素：**

1.  **Crew (团队):** 整个 AI 团队，负责管理成员（Agent）和任务（Task）流程（Process）。
2.  **Agent (代理):** 团队里的**AI 工作者**，有特定**角色**（role）、**目标**（goal）和**背景**（backstory），使用**大模型**（LLM）思考，可以调用**工具**（Tool）。
3.  **Task (任务):** 分配给 Agent 的**具体工作指令**，说明要做什么（description）和想要什么结果（expected_output）。
4.  **Tool (工具):** Agent 用来做特定事情的**外部能力**（如搜索、计算），扩展 Agent 的能力。
5.  **Process (流程):** 团队完成任务的**工作方式**（顺序执行 Sequential 或分层管理 Hierarchical）。
6.  **LLM (大语言模型):** Agent 的“大脑”**，让 Agent 能理解、思考和生成内容。CrewAI 通过 litellm 连接不同模型。
7.  **Memory (记忆):** 让 Agent 和团队**记住**当前运行中的信息或过去经验。
8.  **Knowledge (知识):** 让 Agent 可以**查阅**预先设定的外部信息源（如文档）。

**简单来说：**

你给 Crew (团队) 一堆 Task (任务)，Crew 里的 Agent (AI 工作者) 们用他们的 LLM (大脑) 和 Tool (工具)，按照 Process (流程)，并利用 Memory (记忆) 和 Knowledge (知识)，一起把任务完成。

**关键词汇表 (KISS 版本):**

-   **Crew:** AI 团队经理。
-   **Agent:** AI 工作者。
-   **Task:** 具体工作指令。
-   **Tool:** AI 的外部能力。
-   **Process:** 团队工作方式 (顺序/分层)。
-   **LLM:** AI 大脑模型。
-   **litellm:** 连接 LLM 的工具。
-   **Memory:** AI 的短期/长期记忆。
-   **Knowledge:** AI 的外部信息源。

---