---
aliases:
date: 2025-10-19 14:16
tags:
source:
  - https://github.com/bregman-arie/devops-exercises/blob/master/topics/software_development/README.md
update:
rating:
---
好的，我将对这篇笔记进行重构，特别是代码部分将采用生产级别的标准，并添加 Google 风格的注释。

---

# Kanban vs Scrum：敏捷方法论对比指南

## 核心区别

**Kanban** 是基于持续流动的工作方式，**Scrum** 是基于固定周期冲刺的迭代框架。选择哪一种取决于团队的工作性质、交付节奏和组织成熟度。

---

## 详细对比

### 1. 工作节奏与交付模式

#### Kanban：持续流动 (Continuous Flow)
- **特点**：任务持续进入系统，完成即交付，无固定周期
- **适用场景**：
  - 运维团队处理线上问题
  - 客服团队响应用户工单
  - 需要快速响应变化的业务需求

#### Scrum：时间盒迭代 (Time-boxed Iterations)
- **特点**：固定周期（通常 1-4 周）的 Sprint，每个 Sprint 产出可交付增量
- **适用场景**：
  - 产品功能开发
  - 有明确里程碑的项目
  - 需要可预测交付节奏的团队

---

### 2. 结构化程度

#### Kanban：轻量级框架
- **灵活性**：可以叠加在现有工作流程上
- **规则**：仅 3 个核心实践
  1. 可视化工作流
  2. 限制在制品 (WIP Limits)
  3. 管理流动
- **变更成本**：低，易于渐进式采用

#### Scrum：高度结构化框架
- **固定要素**：
  - **3 个角色**：Product Owner、Scrum Master、Development Team
  - **5 个事件**：Sprint Planning、Daily Scrum、Sprint Review、Sprint Retrospective、Sprint 本身
  - **3 个工件**：Product Backlog、Sprint Backlog、Increment
- **变更成本**：高，需要组织级支持

---

### 3. 可视化与流程控制

#### Kanban：流程优化为核心

**关键机制**：
- **看板 (Kanban Board)**：实时展示工作项状态
- **WIP 限制**：每个工作阶段的并行任务上限
- **累积流图 (CFD)**：识别瓶颈和流动效率

**度量指标**：
- Lead Time（前置时间）
- Cycle Time（周期时间）
- Throughput（吞吐量）

#### Scrum：交付节奏为核心

**关键机制**：
- **Sprint Backlog**：当前冲刺的承诺
- **燃尽图 (Burndown Chart)**：追踪 Sprint 进度
- **Definition of Done**：质量标准

**度量指标**：
- Velocity（速度）
- Sprint Goal 达成率
- 缺陷率

---

### 4. 团队协作模式

#### Kanban
- **会议**：按需召开，通常只有站会和流程回顾
- **角色**：无固定角色要求，鼓励自组织
- **承诺**：基于容量的拉动式系统

#### Scrum
- **会议**：4 个强制仪式，固定时间盒
- **角色**：明确的职责划分
- **承诺**：Sprint 承诺（Sprint Commitment）

---

>[!note]
>**选择指南**
>- **选 Kanban**：工作高度不可预测、需要快速响应、团队已有成熟流程
>- **选 Scrum**：需要固定交付节奏、团队需要结构化指导、产品开发场景
>- **混合使用**：Scrumban（Scrum + Kanban）适合过渡期或需要两者优势的团队
