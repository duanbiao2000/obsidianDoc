---
aliases: BMAD-METHOD/docs/user-guide.md at main · bmad-code-org/BMAD-METHOD
source: https://github.com/bmad-code-org/BMAD-METHOD/blob/main/docs/working-in-the-brownfield.md
author:
  - "[[GitHub]]"
published:
date: 2025-08-17
description: Breakthrough Method for Agile Ai Driven Development - BMAD-METHOD/docs/user-guide.md at main · bmad-code-org/BMAD-METHOD
tags:
  - clippings
---
好的，根据您提供的决策树内容，以下是其流程的清晰文字表述：

这里包含了三个独立的决策流程，分别用于指导在不同情境下的开发和文档工作。

### 流程一：选择文档编写方法

这个流程帮助你根据代码库的规模和熟悉度，决定是先写产品需求文档（PRD）还是先写技术文档。

1.  **首先，判断代码库的规模。**
    - **如果**你面对的是一个大型代码库或单体仓库（monorepo），那么应该采用 **“PRD优先（PRD-First Approach）”** 的方法。具体操作是：先创建PRD，然后只针对变更所影响的区域编写文档。
    - **如果**代码库不大，则进入下一步。
2.  **接着，判断你对代码库的熟悉程度。**
    - **如果**你对这个（较小的）代码库非常熟悉，那么同样采用 **“PRD优先”** 的方法。
    - **如果**你对这个代码库不熟悉，那么应该采用 **“文档优先（Document-First Approach）”** 的方法。

### 流程二：确定开发工作流的类型

这个流程用于判断变更的规模，并选择合适的开发工作流和工具命令。

1.  **首先，判断变更是否为重大增强。**
    - **如果**这是一项影响多个系统的重大功能增强，那么你需要采用 **“完整的棕地（Full Brownfield）工作流”**。在这种情况下，**必须**首先运行 Test Architect 的 `*risk` 和 `*design` 命令。
    - **如果**不是重大增强，则进入下一步。
2.  **接着，判断变更是否超过简单的Bug修复。**
    - **如果**变更内容比一个简单的Bug修复更复杂（例如一个小功能），那么你应该使用 `*create-brownfield-epic` 命令来创建任务，并需要针对集成点运行 Test Architect 的 `*risk` 命令。
    - **如果**这只是一个简单的Bug修复，那么你应该使用 `*create-brownfield-story` 命令来创建任务。但需要注意，**如果**这个修复触及了系统的关键路径，你仍然需要运行 `*risk` 命令。

### 流程三：处理涉及遗留代码的变更

这个流程指导你在代码变更触及遗留代码（legacy code）时，如何使用 Test Architect 工具。

1.  **首先，判断变更是否触及遗留代码。**
    - **如果**变更触及了遗留代码，那么使用 Test Architect 是 **强制性的**。你需要按顺序执行以下操作：
        - 运行 `*risk` 来识别潜在的回归风险。
        - 运行 `*design` 来规划测试覆盖范围。
        - 运行 `*review` 来验证没有破坏现有功能。
    - **如果**变更没有触及遗留代码，那么使用 Test Architect 则是 **推荐的**（非强制）。在这种情况下，建议至少运行 `*review` 命令来确保代码质量符合标准。