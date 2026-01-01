---
aliases:
  - Git的意义在于diff
date: 2025-12-14 13:43
tags:
  - Status/TODO
source:
  - https://claude.ai/public/artifacts/0a767ddd-3d55-4f7a-9c66-f5023e8457d8
update:
rating:
related:
view-count: 8
---
# [[Prompt 管理系统(todo)]] | Minimal

---

## 0. 本质 (The Essence)
- **核心逻辑**：Prompt 即代码 (Prompt as Code)。
- **价值点**：Markdown 固化逻辑 + Git 追踪演进 + 跨平台即插即用。
- **定位**：拒绝散落在对话记录里的“一次性灵感”，建立可迭代的指令资产库。

---

## 1. 核心架构 (The Hierarchy)

| 目录层级 | 内容 | 作用 |
| :--- | :--- | :--- |
| **00_META/** | INDEX / STANDARDS | 全局索引与质量规范 |
| **01_DOCS/** | 文档分析类 Prompt | 场景化指令分库 |
| **02_CODE/** | 代码审查类 Prompt | 场景化指令分库 |
| **05_CUSTOM/** | 个人特定领域 | 扩展分区 |
| **TEMPLATE.md**| 标准化模板 | 保持所有 Prompt 结构一致 |

---

## 2. 逻辑骨架 (Minimal Schema)

每个 Prompt 文件必须包含的四个核心区块：

- **元数据 (Metadata)**：版本号、适配模型（Claude/GPT-4）、标签。
- **效果记录 (Metrics)**：成功率、节省时间、质量评分。
- **版本演进 (Evolution)**：记录 `v1.0 -> v2.0` 改进了什么，解决了哪个坑。
- **正文 (Body)**：**角色 + 目标 + 输入格式 + 输出要求 + 约束条件**。

---

## 3. 避坑指南 (Brutal Truths)

- **别相信记忆**：不在 Markdown 里记录失败案例，下次还会犯同样的错。
- **拒绝“万能 Prompt”**：越通用的指令效果越平庸。按需拆分，链式调用（Chaining）。
- **「_current」原则**：始终保持一个 `v_current.md` 文件，避免在几十个版本文件中翻找。
- **Git 不是用来备份的**：Git 的意义在于 `diff`，通过对比不同版本的输出差异来精准调优。

---

## 4. 执行工作流 (Execution Map)

1. **初始化**：创建目录结构，执行 `git init`。
2. **规范化**：将笔记、收藏夹里的 Prompt 填入 `TEMPLATE.md`。
3. **索引化**：在 `INDEX.md` 建立场景映射表。
4. **迭代循环**：`使用 -> 发现不满意 -> 复制新版本 -> 修改记录改进点 -> 更新 _current`。

---

## 5. 决策树：如何命名版本？

1. **只是修补错别字/微调格式？** → `v1.0.1` (Patch)。
2. **新增了评估维度/优化了逻辑？** → `v1.1.0` (Minor)。
3. **彻底重构了角色或流程？** → `v2.0.0` (Major)。

---

**原则**：极简胜过复杂。没有版本控制的 Prompt 只是文字，有版本控制的 Prompt 才是生产力工具。