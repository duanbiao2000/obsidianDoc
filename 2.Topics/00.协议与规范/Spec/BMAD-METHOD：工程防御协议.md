---
tags:
  - Tech/DeepWiki
  - Method
  - Domain/Creativity/Product
  - Checklist-防呆清单
  - clippings
source: https://github.com/bmad-code-org/BMAD-METHOD/blob/main/docs/working-in-the-brownfield.md
view-count: 20
update: 2026-01-08 23:13
related:
aliases: BMAD-METHOD/docs/user-guide.md at main · bmad-code-org/BMAD-METHOD
author:
  - "[[GitHub]]"
published:
date: 2025-08-17
description: Breakthrough Method for Agile Ai Driven Development - BMAD-METHOD/docs/user-guide.md at main · bmad-code-org/BMAD-METHOD
---
根据你的 ROI 优化策略，对 [[BMAD-METHOD]] 的三篇整合笔记进行重构，将清单、指令集与决策流压缩为高密度的**工程防御协议**。

---

# [[BMAD-METHOD]]：工程防御协议 (Full Edition)

## 1. 核心模型：可靠性逻辑
**可靠性算式：$Reliability = \prod (角色清单 \times 阶段准入) - 风险熵$**
- **风险评分 (Score)**：概率 $\times$ 影响。9 (P0/必测) $\rightarrow$ 1 (最小风险)。
- **质量门态**：**PASS** (满足) / **CONCERNS** (非关键缺口) / **FAIL** (强制拦截) / **WAIVED** (文档化接受)。

## 2. 角色防御矩阵 (Role-Phase Matrix)

| 角色 | 核心任务 | 核心防御点 (Focus) | 必备指令/模板 |
| :--- | :--- | :--- | :--- |
| **Architect** | 系统设计 | 边界隔离、容灾、NFR (非功能需求) | `*nfr`, `arch-tmpl` |
| **PM / PO** | 需求定义 | 场景闭环、MVP 范围、DoR 准入 | `*elicitation`, `prd-tmpl` |
| **SM** | 故事验收 | DoD 达成、DoR 准入、风险识别 | `*risk`, `story-tmpl` |
| **Dev / QA** | 实现与审计 | 单测 $\ge 90\%$、无硬等待、自清理数据 | `*design`, `*review` |
| **DevOps** | 环境与发布 | 灰度策略、1分钟回滚路径、DoD 验证 | `*gate`, `release-checklist` |

## 3. 測試架構師 (TA) 指令协议

| 指令 | 优先级 | 触发场景 | 执行动作 |
| :--- | :--- | :--- | :--- |
| **`*risk`** | **P0** | **变更/遗留代码** | 识别集成与回归风险（未执行则门禁 FAIL）。 |
| **`*design`** | **P1** | **新功能/Major** | 创建测试策略与路径设计。 |
| **`*review`** | **强制** | **合并前** | 综合评估变更影响（必填项）。 |
| **`*nfr`** | P1 | 关键路径 | 验证性能、安全等非功能性指标。 |
| **`*trace`** | P2 | 复杂逻辑 | 验证需求到测试的覆盖全链路。 |
| **`*gate`** | 按需 | 发布决策 | 更新质量门状态 (Go/No-Go)。 |

## 4. 决策逻辑算子 (Decision Algorithms)

### A. 文档路径选型
- **IF** (大型库/Monorepo) **OR** (团队熟悉度高) $\rightarrow$ **[PRD-First]** (先写需求，后补影响区文档)。
- **ELSE** (小型库 **AND** 不熟悉) $\rightarrow$ **[Document-First]** (先通过文档理清逻辑)。

### B. 工作流选型 (Brownfield 逻辑)
1. **重大增强** $\rightarrow$ **[Full Brownfield]**：强制 `*risk` + `*design`。
2. **复杂变更/新功能** $\rightarrow$ **[Epic/Story]**：执行 `*risk`。
3. **简单 Bug 修复**：
    - **IF** (触及关键路径) $\rightarrow$ 运行 `*risk`。
    - **ELSE** $\rightarrow$ 直接修复。

### C. 遗留代码 (Legacy) 处理
- **IF** (触及 Legacy) $\rightarrow$ **[强制 TA 嵌入]**：`*risk` $\rightarrow$ `*design` $\rightarrow$ `*review`。
- **ELSE** $\rightarrow$ **[推荐 TA 嵌入]**：至少运行 `*review` 确保质量门。

## 5. 瞬时执行清单 (Checklist)
- [ ] **准入**：是否满足 `DoR`（准备就绪定义）？
- [ ] **防御**：针对遗留系统，是否已执行 `*risk` 识别回归风险？
- [ ] **质量**：测试是否消除了“硬等待”与“不稳定性”？
- [ ] **门禁**：是否存在 P0 风险项未覆盖（若有则状态为 FAIL）？

---

**ROI 评估：**
- **压缩率**：~60% (合并三篇笔记，剔除冗余流程描述)。
- **信息密度**：显著提升，将指令、矩阵与分支逻辑系统化。
- **5秒测试**：通过“决策逻辑算子”即可在 5 秒内锁定当前任务的工程路径。

**关联笔记：** [[道法术器]] | [[生成力执行协议]] | [[Claude阅读指南]]