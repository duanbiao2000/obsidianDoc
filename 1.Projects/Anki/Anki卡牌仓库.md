---
aliases:
date: 2025-10-30 11:45
tags:
source:
update:
rating:
view-count: 4
---
# Copilot 专业化定制协议：极简框架

## 核心组件架构
| 类型 | 作用域 | 执行逻辑 | 配置难度 |
| :--- | :--- | :--- | :--- |
| **Prompts (提示模板)** | 特定任务 | `/name` 直接调用，即插即用。 | 低 |
| **Instructions (指令集)** | 项目/团队 | 基于 `.github/copilot-instructions.md` 自动约束行为。 | 低 |
| **Chat Modes (聊天模式)** | UI 交互 | 切换 AI Persona（如架构师、DBA），改变对话语境。 | 中 |
| **Agents (专业代理)** | 复杂工作流 | 接入 MCP 服务器，具备工具调用与环境感知能力。 | 高 |

## 定制化功能矩阵
- **Awesome Agents**: 专用工作流（DevOps、数据库、云原生），接入 MCP 实现自动化。
- **Awesome Prompts**: 场景化模板，提升代码生成与文档编写精度。
- **Awesome Instructions**: 强制执行 Coding Standard 与最佳实践，降低风格偏差。
- **Awesome Chat Modes**: 提供专家级咨询体验，支持结构化决策建议。
- **Collections**: 主题化资源包，支持按技术领域（如前端、安全）批量配置。

## 测试自动化 (TDD) 实施逻辑
- **Red (失败)**: `tdd-red` 引导编写失败用例，明确需求边界。
- **Green (通过)**: `tdd-green` 驱动实现最小可用代码，严控逻辑复杂度。
- **Refactor (重构)**: `tdd-refactor` 专注结构优化与代码清理。
- **工具链集成**:
    - **Playwright**: 支持 TS/Python 自动化，提供网页探查与脚本生成提示。
    - **标准框架**: 覆盖 C# NUnit、Java JUnit 的用例生成。
- **安全审计**: `ai-prompt-engineering-safety-review` 专门用于 AI 场景下的提示词合规评审。

## 术语定义
- **Enabler**: 支撑核心 Feature 实现的基础性组件或使能需求。

---
**关联笔记**
- [[智能代理]]
- [[2025-12-14-经典软件测试方法]]
- [[Prompt 模板库结构设计]]
- [[Meta Prompt 元提示词表达式]]
- [[LangChain]]
- [[2020年代技术趋势 (2025更新版)]]