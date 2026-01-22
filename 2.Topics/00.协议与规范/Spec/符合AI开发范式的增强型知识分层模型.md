---
aliases: null
date: 2026-01-08 13:05
tags:
  - AI-Assisted-Development
  - Knowledge-Code-Integration
  - AI-Agent-Development
  - Algorithm
source: null
rating: null
related:
  - '[[AI 辅助编程全流程指南]]'
  - '[[2020年代技术趋势 (2025更新版)]]'
  - '[[SpecKit四个阶段]]'
  - '[[2025-12-22-AI大模型知识体系]]'
  - '[[学习框架]]'
view-count: 5
---

这是一个非常前沿且实用的问题！当你在使用 **Claude（Anthropic）** 或 **OpenAI Codex / GPT 系列（如 o1、GPT-4o）** 进行开发辅助时，它们的“技能”（skills）、“工具调用”（tool calling）、“函数定义”（function schema）等能力，实际上对应着传统软件工程中的**模块化能力单元**。而你希望将你的笔记仓库结构与这类 AI 辅助开发工作流对齐，本质上是在构建一个 **“人机协同的知识-代码一体化架构”**。

下面我将从 **AI 开发范式特点** 出发，结合你已有的 PRD/ADR/Spec 分层体系，提出一种 **兼容 Claude Skills / OpenAI Function Calling 的增强型知识分层模型**，并给出具体的目录结构和集成建议。

---

## 一、AI 原生开发工作流的核心概念

| 概念                   | Claude（Skills）                              | OpenAI（Function Calling / Assistants API）      | 对应传统开发                    |
| -------------------- | ------------------------------------------- | ---------------------------------------------- | ------------------------- |
| **Skill / Function** | 定义可被调用的能力（如 `search_user`, `calculate_tax`） | Function schema（name, parameters, description） | 微服务 / 工具函数 / API endpoint |
| **Tool Definition**  | JSON Schema 描述输入输出                          | 同左，需严格符合 OpenAPI 风格                            | 接口规范（Spec）                |
| **Orchestration**    | Agent 决策调用哪些 Skill                          | Assistant 调用 Functions 并组合结果                   | 工作流引擎 / 编排逻辑              |
| **Context Window**   | 依赖上下文理解用户意图                                 | 同左，需 prompt + tools 注入                         | 需求上下文（PRD/用户故事）           |

> ✅ 关键洞察：**每个 Skill / Function 本质上是一个“可执行的 Spec”**，它必须有清晰的：
>
> - 输入/输出契约（= TSD/Spec）
> - 业务语义（= PRD 片段）
> - 技术实现（= Code + TRD）
> - 变更记录（= CMR）

---

## 二、增强型六层模型 + AI Skills 层（L3.5）

我们在原有六层基础上，**插入一个“AI 能力层”**，专门管理 AI 可调用的技能单元：

| 层级       | 名称                       | 内容                                                    | 与 AI 工作流映射                           |
| -------- | ------------------------ | ----------------------------------------------------- | ------------------------------------ |
| L0       | 市场与战略                    | MRD, Vision                                           | —                                    |
| L1       | 需求与范围                    | PRD, User Stories                                     | 用户意图来源                               |
| L2       | 提案与决策                    | RFC, ADR                                              | 决定是否用 AI 实现某功能                       |
| **L3**   | **规范与设计**                | TSD, Data Model, API Spec                             | **人工系统接口**                           |
| **L3.5** | **AI 能力层（Skills Layer）** | **Skill Definitions, Tool Schemas, Prompt Templates** | **Claude Skills / OpenAI Functions** |
| L4       | 实现与验证                    | Code, TRD, Tests                                      | Skill 的具体实现（Python/JS 函数）            |
| L5       | 演进与复盘                    | CMR, Retros                                           | Skill 效果评估、迭代                        |

> 💡 **L3.5 是桥梁**：它把“人类可读的设计文档”转化为“AI 可执行的工具描述”。

---

## 三、推荐目录结构（兼容 AI 开发）

```text
📁 00-Market-Strategy/
📁 01-Requirements/
📁 02-Proposals-Decisions/
📁 03-Design-Specs/
│   ├── TSD-Payment.md
│   └── API-Spec-User.json          # 人工 API

📁 04-AI-Skills/                    # ← 新增：L3.5
│   ├── skill_search_user.yaml      # Claude Skill 定义
│   ├── function_calculate_tax.json # OpenAI Function Schema
│   ├── prompt_template_summarize.md
│   └── README.md                   # 说明如何注册到 Claude Console / OpenAI Assistants

📁 05-Implementation-Tests/
│   ├── src/
│   │   ├── skills/                 # 实际 Python/JS 实现
│   │   │   ├── search_user.py
│   │   │   └── calculate_tax.js
│   │   └── api/                    # 传统 API 实现
│   └── tests/
│       └── test_skills.py

📁 06-Evolution-Retros/
```

### 📄 示例：`function_calculate_tax.json`（OpenAI 格式）

```json
{
  "name": "calculate_tax",
  "description": "根据收入和地区计算个人所得税",
  "parameters": {
    "type": "object",
    "properties": {
      "income": {"type": "number", "description": "年收入（人民币）"},
      "region": {"type": "string", "enum": ["beijing", "shanghai"], "description": "纳税地区"}
    },
    "required": ["income", "region"]
  }
}
```

> 此文件既是 **文档（Spec）**，也是 **可直接加载到 OpenAI Assistants API 的工具定义**。

---

## 四、如何与 Claude / OpenAI 工作流集成？

### 1. **Claude Skills（目前限企业版）**

- 将 `04-AI-Skills/` 中的 YAML/JSON 文件上传到 **Claude Console**
- 在 PRD 中标注：“此功能由 AI Skill `calculate_tax` 实现”
- 在 ADR 中记录：“选择 Claude Skill 而非自建微服务，因延迟要求 <500ms”

### 2. **OpenAI Assistants API**

- 用脚本自动将 `04-AI-Skills/*.json` 注册为 Assistant 的 tools
- 在开发时，通过 `assistant.create(tool_resources=...)` 动态绑定
- 在 TRD 中写：“验证 Assistant 能正确调用 `calculate_tax` 并处理错误”

### 3. **本地开发 & 测试**

- 使用 `pytest` 模拟 AI 调用，测试 `skills/` 下的函数
- 用 `dataview`（Obsidian）或 Notion 数据库关联：
  - PRD → 对应 Skill
  - Skill → 对应 CMR（当 Skill 逻辑变更时）

---

## 五、最佳实践建议

| 实践             | 说明                                                                                        |
| -------------- | ----------------------------------------------------------------------------------------- |
| **Skill 即文档**  | 每个 Skill 文件必须包含 human-readable description，不仅是机器 schema                                   |
| **版本化 Skill**  | 在文件名或元数据中标注版本（如 `skill_v2_search_user.yaml`），便于回滚                                         |
| **双向链接**       | 在 Obsidian 中：`[[PRD-税务计算]]` → `[[skill_calculate_tax]]` → `[[CMR-202601-TaxLogicUpdate]]` |
| **自动化同步**      | 写脚本将 `04-AI-Skills/` 同步到 Claude Console / OpenAI 后台（CI/CD 集成）                             |
| **Prompt 也归档** | 复杂的系统 prompt（如角色设定、输出格式）存为 `.md`，纳入 L3.5                                                  |

---

## 六、未来演进建议

随着 AI Agent 能力增强，你可能会有：

- **Skill Composition**（技能编排）→ 新增 `04.5-Agent-Workflows/`
- **Skill Evaluation**（效果评估）→ 在 L5 中增加 `Skill-Metrics-2026Q1.md`

---

如果你告诉我你主要用 **Claude 还是 OpenAI**，以及你的项目类型（Web 应用？数据分析？自动化工具？），我可以：

- 生成一套完整的 Skill 模板（YAML/JSON）
- 提供自动注册到 API 的 Python 脚本
- 设计一个 Obsidian 插件或 Dataview 查询，可视化“PRD → Skill → Code”链路

这样你的笔记仓库就真正成为 **AI-Native Development 的中枢知识库** 🧠✨。
