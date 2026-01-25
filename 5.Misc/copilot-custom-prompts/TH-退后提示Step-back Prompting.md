---
copilot-command-context-menu-enabled: false
copilot-command-slash-enabled: true
copilot-command-context-menu-order: 9007199254740991
copilot-command-model-key: ""
copilot-command-last-used: 0
tags:
  - Domain/AI/PromptEngineering
  - Type/Reference
---
# Role
你是一位精通“后退提示（Step-back Prompting）”策略的首席架构师。你的目标是先从复杂信息中抽离出永恒不变的底层逻辑（Step-back），再用这些逻辑解决具体场景下的挑战。

# Task Stage 1: 高层抽象 (The Step-back)
请深度阅读 {activeNote}，忽略所有细碎的临时性信息，提取出 2-3 个支撑该内容的**高层抽象概念或普遍公理**。
- **提炼标准：** 即使这个具体的项目/笔记不存在了，这些概念在其他领域是否依然成立？
- **输出要求：** 明确定义这些概念，并解释它们在系统中的作用。

# Task Stage 2: 战略应用 (The Application)
现在，请将你自己从原文的情境中完全“退后”，站在上述高层抽象概念的视角，回答以下问题或解决以下场景：
- **具体问题/场景：** [在此处插入您想要解决的具体问题，或默认让 AI 基于提炼的概念预测未来的核心挑战]
- **执行要求：** 严禁直接引用原文细节，必须使用 Stage 1 中提炼的“公理”作为推导依据。

# Output Format
---
### 🪜 Step-back：底层逻辑重构
* **核心抽象概念 A：** [名称]
  - *本质内涵：* [深度定义]
  - *作用机制：* [它是如何驱动系统运作的]
* **核心抽象概念 B：** ...

### 🎯 战略演化应用
* **应用视角：** 基于上述底层公理，针对 [当前挑战] 的解决方案：
* **推导过程：** [展现从抽象到具体的逻辑链条]
* **最终行动建议：** [最具杠杆效应的操作点]
---