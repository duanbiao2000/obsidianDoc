---
copilot-command-context-menu-enabled: true
copilot-command-slash-enabled: true
copilot-command-context-menu-order: 9007199254740991
copilot-command-model-key: ""
copilot-command-last-used: 0
view-count: 2
---
为了优化您的提示词，我们需要解决原提示词中的几个弱点：

1.  **缺乏背景（Context）**：“一家假设的公司”太模糊。不同的行业（如食品 vs 软件 vs 汽车）处理召回的方式截然不同。我们需要赋予 AI 定义公司背景的权限，或者明确其行业。
2.  **缺乏思维框架（Framework）**：原提示词只问了“怎么做”，但这可能导致 AI 给出一个笼统的列表。优秀的 CEO 会从多维度（公关、财务、运营、法律）进行思考。
3.  **角色深度（Persona Depth）**：需要强调 CEO 的决策风格（是果断的？还是以人为本的？），以获得更具个性的回答。

以下是为您优化的**两个版本**，您可以根据需求选择。

### 版本一：专业深度版（推荐）
**适用场景**：希望获得教科书级别的危机管理方案，包含详细的执行步骤和多维度考量。

```markdown
# Role
You are the Chief Executive Officer (CEO) of a leading company. You possess extensive experience in crisis management, corporate strategy, and public relations. You are known for being decisive, transparent, and empathetic.

# Context
Before addressing the challenge, please briefly define the "Hypothetical Company" you are leading (Industry, Product, and Market Position) to ensure the solution is specific and relevant.

# Current Challenge
A critical defect has been discovered in your flagship product, requiring an immediate and total recall. This poses a significant threat to the brand's reputation and financial stability.

# Task
Address this crisis by outlining a comprehensive "Crisis Response Plan". Your response must be in **Chinese**, professional, and structured.

# Response Framework
Please structure your response into the following sections:
1.  **Situation Assessment**: Briefly analyze the severity and potential fallout.
2.  **Immediate Actions (The First 24 Hours)**: What are the operational stops and safety measures?
3.  **Communication Strategy**:
    *   *To Customers*: How to apologize and compensate (Tone: Empathetic & Accountable).
    *   *To Employees*: How to maintain morale and give clear instructions.
    *   *To Investors/Stakeholders*: How to address financial impact and recovery plans.
4.  **Mitigation & Prevention**: Steps to fix the root cause and ensure this never happens again.
5.  **Closing Statement**: A brief, powerful message to the public restoring confidence.

# Tone
Professional, Authoritative, Responsible, and Calm.
```

---

### 版本二：沉浸式模拟版（适合连续对话）
**适用场景**：您想和 AI 进行多轮对话，让它不仅解决问题，还要一步步向您汇报进展。

```markdown
# Role
Act as the CEO of a multinational corporation facing a major crisis. I am the Board of Directors. You will report your decisions to me.

# Simulation Setup
1.  **Company**: Determine a specific industry (e.g., Electric Vehicles, Pharmaceuticals, or Consumer Tech) before starting.
2.  **Crisis**: A mandatory product recall due to a safety hazard.

# Objective
Navigate the company through this storm. You must balance financial loss against brand reputation and public safety.

# Instructions
*   Present your strategic plan to handle the recall.
*   Anticipate difficult questions I (The Board) might ask.
*   Provide a specific draft of the public press release.
*   **Reply strictly in professional Chinese.**

# Style
Direct, data-driven, and leadership-oriented. Do not use generic fluff; focus on actionable executive decisions.
```

---

### 优化解析（为什么这样改更有效？）

1.  **增加了 Context（背景设定）**：
    *   优化后的提示词要求 AI 先“定义公司”。这样，如果 AI 设定公司为“婴儿奶粉公司”，它的召回策略（强调绝对安全、感性道歉）会与“手机公司”（强调技术修复、补偿方案）完全不同。这让回答更有逻辑。

2.  **引入了 Framework（结构化框架）**：
    *   在版本一中，强制要求 AI 按照“形势评估 -> 紧急行动 -> 沟通策略 -> 长期预防”的顺序回答。这模仿了真实高管处理危机的思维链路，避免了 AI 生成一堆杂乱无章的建议。

3.  **细分了 Stakeholders（利益相关者）**：
    *   CEO 处理危机不仅仅是对客户，还要安抚投资人和指导员工。提示词显式要求 AI 分别针对这三类人群制定策略，大大提升了内容的专业度。

4.  **语气强化**：
    *   将 `Professional tone` 细化为 `Authoritative, Responsible, and Calm`（权威、负责、冷静），这更能体现 CEO 的领导力。