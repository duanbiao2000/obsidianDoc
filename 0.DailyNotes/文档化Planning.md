---
aliases:
  - 强制慢思考
  - Review新范式
  - ".3"
date: 2025-12-03 10:54
tags:
update:
rating:
related:
  - "[[Plan文档比较与实例]]"
view-count: 9
---
# [[文档化Planning]]

## 1. 核心逻辑：强制慢思考 (Forced Slow Thinking)

**系统目标：** 通过文档化手段将非线性的直觉决策转化为线性的逻辑链条，实现风险前置。

**价值公式 (Decision Metric)：**
$$Plan_{Granularity} = Risk\_Cost \times Uncertainty \times Complexity$$

- **本质**：文档不是终点，而是决策过程的“缓存”与“编译”。
- **阴暗面**：警惕过度规划（Over-engineering）、僵化诅咒（Rigidity）及以文档掩盖行动力（Procrastination）。

## 2. 文档层级与风险矩阵 (The Hierarchy)

| 级别 | 文档形态 | 作用域 | 粒度 |
| :--- | :--- | :--- | :--- |
| **L1 (Strategic)** | **RFC** | 架构/年度 | 极粗（Why & Constraints） |
| **L2 (Decisional)** | **ADR** | 选型/月度 | 中等（Trade-offs & Context） |
| **L3 (Technical)** | **Spec** | 模块/周级 | 细致（Logic & Data Schema） |
| **L4 (Operational)** | **Runbook** | 上线/天级 | 极细（Step-by-Step Operator） |

## 3. 执行指南：Plan 构造协议

### **核心要素 (The Checklist)**
- **Problem Definition**：严谨定义“为什么要做”。
- **Alternatives**：必须包含至少 2 个可选路径。
- **Trade-offs**：明确列出“为什么不选路径 B”。
- **Risk Identification**：识别系统的崩溃边界。
- **Success Criteria**：可量化的完成标志。

### **评审机制 (Review Algorithm)**
- **Timebox**：设置强制截止时间，防止评审死锁。
- **Dissenting Opinion**：鼓励并记录异议，对冲资深者垄断（The Hippo Effect）。
- **Signal Check**：若执行中频繁出现“早知道就...”，说明 Plan 粒度过低；若文档写完无人查看，说明 Plan 过重。

## 4. 性能参数 (Performance Tuning)

- **认知陷阱**：双曲折扣（眼前痛苦 > 未来风险）、可见性悖论（Plan 越好，故障越少，存在感越低）。
- **状态切换**：严格区分“探索期”（轻量 Plan）与“执行期”（标准 Spec）。

## 关联笔记
- [[sequential - thinking的适用场景]] (系统性思考的底层工具) [^13]
- [[Go开发者实战指南]] (L3 层级解耦的工程实践参考) [^2]
- [[2025-12-30-跨领域播客 Transcript 快速框架构建法]] (快速构建认知骨架的方法论) [^3]
