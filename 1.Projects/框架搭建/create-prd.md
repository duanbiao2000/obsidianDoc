---
description:
globs:
alwaysApply: false
---
# 规则：生成产品需求文档（PRD）

## 目标

指导 AI 助手根据用户的初步提示，创建一个详细的产品需求文档（PRD），格式为 Markdown。PRD 应该清晰、可执行，并且适合初级开发者理解和实现该功能。

## 流程

1.  **接收初步提示：** 用户提供对新功能或特性的简要描述或请求。
2.  **询问澄清问题：** 在编写 PRD 之前，AI **必须** 询问澄清问题以收集足够详细的信息。目标是理解功能的“是什么”和“为什么”，而非必须理解“怎么做”（这由开发者来确定）。
3.  **生成 PRD：** 根据初步提示和用户对澄清问题的回答，按照以下结构生成 PRD。
4.  **保存 PRD：** 将生成的文档保存为 `/tasks` 目录下的 `prd-[feature-name].md` 文件。

## 澄清问题（示例）

AI 应根据提示调整其问题，但这里列出了一些常见的探究领域：

*   **问题/目标：** “这个功能为用户解决了什么问题？” 或 “我们希望通过这个功能实现的主要目标是什么？”
*   **目标用户：** “这个功能的主要用户是谁？”
*   **核心功能：** “您能描述一下用户通过这个功能应该能够执行的关键操作吗？”
*   **用户故事：** “您能提供几个用户故事吗？（例如：作为一名 [用户类型]，我想要 [执行一个操作]，以便 [获得一个好处]。）”
*   **验收标准：** “我们如何知道这个功能是否成功实现？关键的成功标准是什么？”
*   **范围/边界：** “这个功能是否有什么特定的事情是**不应该**做的（非目标）？”
*   **数据需求：** “这个功能需要展示或操作哪种类型的数据？”
*   **设计/UI：** “是否有任何现有的设计稿或 UI 指南需要遵循？” 或 “您能描述一下期望的外观和感觉吗？”
*   **边缘情况：** “是否有任何潜在的边缘情况或错误条件需要考虑？”

## PRD 结构

生成的 PRD 应包含以下部分：

1.  **引言/概述：** 简要描述该功能及其解决的问题。说明目标。
2.  **目标：** 列出该功能的具体、可衡量的目标。
3.  **用户故事：** 详细描述使用该功能的用户场景和带来的好处。
4.  **功能需求：** 列出该功能必须具备的具体功能。使用清晰、简洁的语言（例如：“系统必须允许用户上传头像。”）。对这些需求进行编号。
5.  **非目标（超出范围）：** 明确说明该功能**不**包含的内容，以管理范围。
6.  **设计考虑（可选）：** 链接到设计稿，描述 UI/UX 需求，或提及适用的相关组件/样式。
7.  **技术考虑（可选）：** 提及任何已知的技术限制、依赖项或建议（例如：“应与现有的 Auth 模块集成”）。
8.  **成功指标：** 如何衡量该功能的成功？（例如：“用户参与度提升 10%”，“减少与 X 相关的支持工单”）。
9.  **开放问题：** 列出任何悬而未决的问题或需要进一步澄清的领域。

## 目标受众

假设 PRD 的主要读者是**初级开发者**。因此，需求应该明确、不含糊，并尽可能避免使用行话。提供足够的细节，让他们能够理解功能的用途和核心逻辑。

## 输出

*   **格式：** Markdown (`.md`)
*   **位置：** `/tasks/`
*   **文件名：** `prd-[feature-name].md`

## 最终指示

1.  不要开始实现 PRD
2.  务必向用户询问澄清问题
3.  根据用户对澄清问题的回答改进 PRD