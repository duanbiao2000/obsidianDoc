---
description: null
globs: null
alwaysApply: false
view-count: 2
tags:
  - markdown-documentation
  - developer-guidance
  - product-management
  - task-creation
  - Type/Reference
  - Domain/Technology
---
# 规则：从 PRD 生成任务列表

## 目标

指导 AI 助手根据现有的产品需求文档（PRD），以 Markdown 格式创建一个详细的、逐步的任务列表。该任务列表应能指导开发者完成功能实现。

## 输出

- **格式：** Markdown (`.md`)
- **位置：** `/tasks/`
- **文件名：** `tasks-[prd-file-name].md` (例如，`tasks-prd-user-profile-editing.md`)

## 流程

1.  **接收 PRD 引用：** 用户指定 AI 需要参考的特定 PRD 文件。
2.  **分析 PRD：** AI 读取并分析指定 PRD 的功能需求、用户故事及其他部分。
3.  **阶段 1：生成父任务：** 基于 PRD 分析，创建文件并生成实现该功能所需的主要、高层次的任务。根据您的判断确定高层次任务的数量，大概是 5 个左右。以指定的格式将这些任务呈现给用户（暂时不包含子任务）。告知用户：“我已根据 PRD 生成了高层次任务。准备好生成子任务了吗？回复 'Go' 以继续。”
4.  **等待确认：** 暂停并等待用户回复 “Go”。
5.  **阶段 2：生成子任务：** 用户确认后，将每个父任务分解为更小、可执行的子任务，这些子任务是完成父任务所必需的。确保子任务逻辑上承接父任务，并覆盖 PRD 中隐含的实现细节。
6.  **识别相关文件：** 根据任务和 PRD，识别可能需要创建或修改的文件。将这些文件列在“相关文件（Relevant Files）”部分下，如果适用，也包括对应的测试文件。
7.  **生成最终输出：** 将父任务、子任务、相关文件和注意事项（Notes）组合成最终的 Markdown 结构。
8.  **保存任务列表：** 将生成的文档保存在 `/tasks/` 目录中，文件名格式为 `tasks-[prd-file-name].md`，其中 `[prd-file-name]` 应与输入的 PRD 文件名（不含扩展名）匹配（例如，如果输入是 `prd-user-profile-editing.md`，则输出是 `tasks-prd-user-profile-editing.md`）。

## 输出格式

生成的任务列表**必须**遵循以下结构：

```markdown
## Relevant Files

- `path/to/potential/file1.ts` - 文件相关的简要说明（例如：包含该功能的主要组件）。
- `path/to/file1.test.ts` - `file1.ts` 的单元测试。
- `path/to/another/file.tsx` - 简要说明（例如：用于数据提交的 API 路由处理程序）。
- `path/to/another/file.test.tsx` - `another/file.tsx` 的单元测试。
- `lib/utils/helpers.ts` - 简要说明（例如：计算所需的工具函数）。
- `lib/utils/helpers.test.ts` - `helpers.ts` 的单元测试。

### Notes

- 单元测试通常应与它们测试的代码文件放在同一目录下（例如，`MyComponent.tsx` 和 `MyComponent.test.tsx` 在同一目录）。
- 使用 `npx jest [optional/path/to/test/file]` 运行测试。不带路径运行时，Jest 将执行其配置找到的所有测试。

## Tasks

- [ ] 1.0 父任务标题
  - [ ] 1.1 [子任务描述 1.1]
  - [ ] 1.2 [子任务描述 1.2]
- [ ] 2.0 父任务标题
  - [ ] 2.1 [子任务描述 2.1]
- [ ] 3.0 父任务标题（如果是纯粹的结构或配置任务，可能不需要子任务）
```

## 交互模式

流程明确要求在生成父任务后暂停，等待用户确认（回复“Go”）才能继续生成详细的子任务。这确保了在深入细节之前，高层次的计划与用户期望一致。

## 目标受众

假设任务列表的主要读者是**初级开发者**，他们将负责实现该功能。