---
copilot-command-context-menu-enabled: false
copilot-command-slash-enabled: true
copilot-command-context-menu-order: 9007199254740991
copilot-command-model-key: ""
copilot-command-last-used: 1753894322452
---
#### **1. 核心指令 (Core Instruction)**

**任务：** 为笔记 `{activeNote}` 设计一套多阶OKR。

---

#### **2. 上下文注入 (Context Injection)**

*   **@风格 (Style):** `[在此处指定风格，例如：500强商务、硅谷硬核、初创公司敏捷(默认)、学术研究严谨]`
*   **@场景 (Scenario):** `[在此处描述应用场景，例如：个人发展、项目管理(默认)、团队战略规划、产品发布]`
*   - **@约束 (Constraints):** `[在此处定义约束，例如：最多3个KR、聚焦于短期成果、必须可自动化验证、周期为季度]` 默认:以上全部约束

---

#### **3. 完成定义 (Definition of Done)**

*一个成功的OKR输出必须满足以下验收标准：*

1.  `[验收标准一，例如：所有KR必须是结果导向(Outcome)，而非任务列表(Output)]`
2.  `[验收标准二，例如：顶层目标(Objective)必须直接回应笔记中的核心论点或痛点]`
3.  `[验收标准三，例如：各阶段OKR之间必须存在明确的依赖和输入/输出关系]`
4.  `[（可选）验收标准四，例如：... ]`

---

#### **4. 处理逻辑 (Processing Logic)**

*请遵循以下计算步骤：*

1.  **结构解析 (Structural Parsing):**
    *   首先，将 `{activeNote}` 的内容解析为一个**抽象概念树 (Abstract Concept Tree)**。
    *   识别出**核心论点**（根节点）、**支撑论据/关键要素**（子节点）以及它们之间的**逻辑关系**（因果、并列、递进）。

2.  **状态机转换 (State Machine Transformation):**
    *   基于解析出的结构，采用多阶状态机模型生成OKR。
    *   **阶段一 (战略层 | `Phase 1: Strategy`):** 将笔记的**根节点**或**核心论点**，转换为顶层战略目标 (Objective)。
    *   **阶段二 (战术层 | `Phase 2: Tactics`):** 将根节点的**一级子节点**（支撑论据），转换为实现该目标的关键成果 (Key Results)。如果某个子节点本身足够复杂，则将其递归地视为下一阶段的Objective。
    *   **阶段三 (执行层 | `Phase 3: Execution`):** 确保最底层的KR是可量化、可验证的具体指标，形成一个完整的、可追溯的依赖图。

3.  **验证与输出 (Validation & Output):**
    *   确保最终生成的OKR完全符合上述【完成定义】中的所有验收标准。
    *   以【上下文注入】中指定的【@风格】进行语言表述和格式化输出。

