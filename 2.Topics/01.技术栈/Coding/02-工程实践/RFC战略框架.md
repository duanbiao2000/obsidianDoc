---
tags:
  - RFC-process
  - technical-proposal
  - decision-making
  - document-structure
  - Type/Reference
  - Domain/Technology
  - RFC-process
  - technical-proposal
  - decision-making
  - document-structure
---
# RFC (Request for Comments) 极简手册

### 1. 核心定义
*   **本质**：决策**前**的技术提案。
*   **目的**：暴露风险、对齐共识、记录权衡。
*   **地位**：写下来的设计讨论，而非行政审批。

---

### 2. 决策矩阵：何时写 RFC？

| 维度 | **✅ 必须写 (High Impact)** | **❌ 无需写 (Low Impact)** |
| :--- | :--- | :--- |
| **影响范围** | 跨团队、跨服务、影响核心链路 | 单一模块内部、UI 微调 |
| **技术难度** | 新架构、新算法、高并发挑战 | 简单 Bug 修复、已有模式复用 |
| **选型成本** | 涉及高额预算、多方案博弈 | 临时 PoC 实验、小功能迭代 |

**经验法则**：影响 **>3 名工程师** 或 **>6 个月演进** $\rightarrow$ **必须写**。

---

### 3. 文档生命周期：RFC vs ADR

*   **RFC (提案阶段)**：
    *   **问题**：我们要怎么做？选 A 还是 B？
    *   **动作**：征求意见、激烈讨论、方案对比。
*   **ADR (定案阶段)**：
    *   **问题**：我们最终定了什么？为什么？
    *   **动作**：快照记录、历史溯源、不可篡改。

**路径**：`RFC` (讨论) $\rightarrow$ `Decision` (决策) $\rightarrow$ `ADR` (归档)。

---

### 4. 核心价值
1.  **防返工**：早期暴露性能瓶颈和逻辑漏洞。
2.  **去中心化**：不靠“拍脑袋”，靠文档协作。
3.  **知识遗产**：新成员通过 RFC 理解系统演进的“为什么”。

---

### 5. 总结
*   **不是每个功能都要 RFC**。
*   **RFC = 预防针**（上线前对齐）。
*   **ADR = 存盘点**（上线后查阅）。