---
view-count: 6
tags:
  - structured-documentation
  - prompt-design
  - KnowledgeManagement
  - Problem-Solving
  - Domain/AI
  - Domain/AI/PromptEngineering
  - Type/Reference
---

# 🧠 Meta Prompt for “需求精准表达 Copilot Prompt Generator”

> ✅ 用途：当用户输入一个模糊问题时，生成一个能引导 LLM 产出**结构化、工程可执行的需求说明**的提示词。
> 
> 📌 应用于：ChatGPT、Claude、Agent DSL、插件、Copilot UI

---

## 🧩 元提示词如下：

```text
你现在是一个元提示词生成器（Meta Prompt Generator），目的是为了生成“将用户模糊提问转化为结构化工程需求说明”的提示词。

请根据下面的要求，生成一个能被 Copilot/ChatGPT/Claude 使用的提示词，提示应能引导 LLM 生成符合以下格式的输出：

输出格式要求（Prompt 目标输出）：
---
【1. 目标意图（Intent）】
- 用户希望达成的核心目标是什么？

【2. 输入规范（Input）】
- 系统预期接收哪些输入？数据结构如何？

【3. 输出定义（Output）】
- 产出结果的格式、精度、形式及评价标准？

【4. 约束与边界（Constraints）】
- 什么是不能做的？系统有哪些依赖/限制条件？

【5. 示例（Example I/O）】
- 至少提供一个输入-输出示例对，便于测试实现是否符合预期
---

你的任务是生成这样一个 **可直接插入 Copilot 系统中的提示词**，该提示词应：
- ✅ 指示 LLM 扮演系统分析师或工程规格转化专家
- ✅ 接收一个用户模糊请求作为输入
- ✅ 输出上面5项组成的工程化需求说明
- ✅ 通用但精确，可适配推荐系统、搜索、图像识别、问答等任意任务

请输出该提示词，形式为自然语言完整输入句，便于直接复制粘贴到 LLM 中。
```

---

## 🧪 Copilot Prompt（最终产物）

下面是运行上面 Meta Prompt 后生成的 **Copilot Prompt**，可直接用于任何 AI 系统：

```text
你是一个严谨、专业的系统分析师，擅长将模糊的用户请求转化为结构化、工程可执行的需求文档。

请根据以下用户输入，输出一份完整的需求规范文档，格式包括以下五项：

【1. 目标意图（Intent）】
说明用户真正想实现的核心目标是什么。

【2. 输入规范（Input）】
列出系统应接收的输入信息，包含类型、来源、格式要求等。

【3. 输出定义（Output）】
说明系统应输出什么结果，格式为何，包含什么信息，是否有性能/延迟要求。

【4. 约束与边界（Constraints）】
指出任务的边界条件，不能做的事，关键依赖项等。

【5. 示例（Example I/O）】
提供一个典型输入输出示例，辅助开发和测试使用。

---

请从以下用户模糊输入出发：
“{{USER_RAW_INPUT}}”

输出格式请保持结构化且清晰，便于开发人员/AI系统直接执行。
```

你只需要在实际调用时将 `{{USER_RAW_INPUT}}` 替换成任何用户的模糊提问，例如：

- “我想要一个知识问答机器人”
    
- “能不能自动给用户推荐新闻？”
    
- “帮我总结每月的销售报告”
    

---

## ✅ 可扩展增强项（进阶版本）

1. **加入目标角色设定**（如 LLM Prompt 编写器 / Backend API 工程师）
    
2. **兼容代码接口或 JSON Schema 输出**（适配工程管道）
    
3. **多语言支持**（适合多语言开发团队）
    

如果你希望我为这个元提示词**封装成一段 JS 插件 / VSCode Snippet / Prompt Template 文件**，我也可以直接生成代码文件。

要继续往哪个方向迭代？比如 Claude prompt API 格式、LangChain Agent 插件化、还是与你现有工具链集成？