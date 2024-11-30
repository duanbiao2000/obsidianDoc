---
aliases: 
theme: 
priority: false
tags:
---
在约定式提交（Conventional Commits）格式中，`feat` 是用来表示新增功能（feature）的。除了 `feat`，还有其他几种常见的类型，每种类型都有其特定的含义和用途：

1. **feat (feature)**: 引入新功能。
   - 例如：`feat: add login functionality`

2. **fix**: 修复bug。
   - 例如：`fix: correct typo in button label`

3. **docs**: 仅文档（documentation）的变更。
   - 例如：`docs: update installation guide`

4. **style**: 不影响代码含义的改动，例如空格、格式化、缺少分号等。
   - 例如：`style: format code according to style guide`

5. **refactor**: 代码重构（即不是新增功能，也不是修复bug的代码更改）。
   - 例如：`refactor: simplify algorithm in utility function`

6. **perf**: 提升性能的改动。
   - 例如：`perf: optimize search performance`

7. **test**: 添加缺失的测试或更正现有的测试。
   - 例如：`test: add unit tests for utility functions`

8. **build**: 影响构建系统或外部依赖项的变更（如webpack、npm）。
   - 例如：`build: update npm dependencies`

9. **ci**: 更改持续集成（Continuous Integration）配置。
   - 例如：`ci: add node.js version to travis build`

10. **chore**: 工具或库的变动，不涉及源代码，如构建流程、依赖管理。
    - 例如：`chore: update npm scripts`

11. **revert**: 回滚到上一个提交。
    - 例如：`revert: move to Semantic Versioning`

这些类型帮助开发者快速理解提交的目的和影响，特别是在自动化工具和版本控制系统中。
