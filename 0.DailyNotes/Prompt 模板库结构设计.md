---
date: 2025-05-20 22:38
tags: 
source: https://docs.google.com/spreadsheets/d/1nYHNzIWxsfiYkNXYioct2gIu-edwMvCg05qGfZgLi-M/edit?gid=1738715959#gid=1738715959
---

明白了，Sam。我们来构建一个「持续迭代的 Prompt 模板库」系统，适用于你的高级应用开发、研究和运营实践。以下是第一版设计方案，分为**结构、格式、分类体系和管理机制**四个层面。

## [Prompt模板库 - Google Sheets](https://docs.google.com/spreadsheets/d/1nYHNzIWxsfiYkNXYioct2gIu-edwMvCg05qGfZgLi-M/edit?gid=1738715959#gid=1738715959)

## 一、Prompt 模板库结构设计（推荐用 Google Sheet + Obsidian 配合管理）

| 字段            | 说明             | 示例                                 |
| ------------- | -------------- | ---------------------------------- |
| `模板名称`        | 简明命名，便于引用      | 总结提取-简洁版                           |
| `使用场景`        | 应用场景、系统模块      | 报告生成 / 数据增强 / QA Bot               |
| `Prompt 内容`   | 完整 prompt，可含变量 | 请从以下文本中提取关键信息并总结为100字内摘要：{{input}} |
| `输出格式`        | 要求输出的结构        | Markdown / JSON / PlainText        |
| `模型推荐`        | 最适用的 LLM       | GPT-4 / Claude / Gemini            |
| `Few-shot 示例` | 可选：训练样例        | Q: ... A: ...                      |
| `版本号`         | 便于版本控制         | v1.0.1                             |
| `更新记录`        | 修改人+时间+变更说明    | Sam@2025-05-20：加入格式限制              |
| `反馈记录`        | 测试评估或用户反馈      | 输出冗长，需要加字数限制                       |

---

## 二、分类体系（推荐采用 Obsidian 双向链接管理）

### 核心分类

- 文本摘要 / 信息抽取 / 文本生成 / 翻译改写

- 数据增强 / 对话生成 / 搜索增强 / 多轮推理

- JSON结构化输出 / Markdown文档生成

- Agent/工具链调用/Chain-of-Thought 模型

- 安全过滤 / 情感判断 / 用户意图识别

### 技术维度标签（支持多标签）

- `zero-shot` / `few-shot` / `CoT` / `ReAct`

- `structured-output` / `persona-prompt` / `feedback-loop`

- `multilingual` / `domain-specific` / `function-calling`

---

## 三、版本控制与迭代机制

建议采用 Git 风格的迭代原则：

| 类型       | 用法             |
| -------- | -------------- |
| `v1.0.x` | 小幅格式或措辞调整      |
| `v1.x.0` | 增加示例或支持更多输入    |
| `v2.0.0` | 完全重构，逻辑或结构重大变更 |

每个 prompt 模板下附加 changelog 块，记录迭代历史。

---

## 四、模板复用与脚本化接口建议

你可以配套开发一个脚本（如在 LangChain、Python、Node 中），支持以下功能：

1. 输入参数自动填充模板

2. 调用模型并控制温度/格式

3. 输出存入统一日志或数据库

4. 收集响应+错误信息用于反馈优化

---

## 五、启动建议（可以现在开始构建）

- **Google Sheet 模板库**：用于结构化表格管理 + 数据集成

- **Obsidian 插件库**：用于链接上下游场景、引用版本关系

- **Prompt 使用反馈表单**：如 Google Form，用于记录真实模型输出体验

---

如果你愿意，我可以为你初始化一个 Google Sheet Prompt 模板表格，并附带几个高质量基础模板（比如结构化输出 / 摘要压缩 / Agent调度等）。是否需要我帮你搭好这个框架？你也可以把你已有的 Prompt 模块发我，我来帮你标准化并整理入库。
