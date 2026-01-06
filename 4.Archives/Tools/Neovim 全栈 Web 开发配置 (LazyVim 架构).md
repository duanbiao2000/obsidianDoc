---
view-count: 6
update: 2026-01-06 23:15
related:
  - "[[Browser-use关键技术]]"
---

## Neovim 全栈 Web 开发配置 (LazyVim 架构)

**核心架构：** 基于 **LazyVim Starter** 建立标准化开发流，通过剥离冗余 UI 释放屏幕空间。

### 1. 基础环境 (Standard Baseline)

- **管理器：** Lazy.nvim (插件) + Mason (LSP/DAP/Linter/Formatter)。
- **核心全局配置：**
  - `Leader` $\to$ `<Space>`
  - `Indent` $\to$ 2 Spaces (Auto-indent, UTF8)
  - `Search` $\to$ Case-insensitive, Live Preview
  - `Requirements` $\to$ Neovim $\ge 0.10$ (开启 Inline Hints 关键)

### 2. UI 极简主义：最大化屏幕 ROI

- **空间优化：** 禁用 `LuaLine` 与 `Pin dashboard`，移除状态栏以获得垂直视野。
- **视觉增强：**
  - 配色：`Sonokai`
  - 消息：`noise.nvim` (接管弹出菜单) + `nvim-notify`
  - 导航：`bufferline` (GUI 标签页) + `inline-nvim` (窗口内显示文件名)

### 3. 开发工具链：语言与工程能力

- **LSP/补全：** `nvim-lspconfig` + `nvim-cmp` (含 `cmp-emoji`)。
- **语法分析：** `Treesitter` (高亮、折叠、缩进)。
- **工程组件：**
  - **检索：** `Telescope` (文件/符号查找)
  - **Git：** `LazyGit` 集成
  - **文件树：** `nvim-tree`

### 4. 全栈增强功能 (Full-Stack Leverage)

- **API 开发：** `rest.nvim` (HTTP Request 直接发送)。
- **数据库：** `nvim-dap` (支持直接执行 SQL 查询)。
- **测试/重构：**
  - `neotest` (深度适配 Jest 框架)
  - `incremental-rename.nvim` (渐进式重命名)
  - `refactoring.nvim` (函数提取等重构操作)

### 5. 决策规则 (Decision Rules)

- **IF** 追求最低认知负载 **THEN** 保持 LazyVim 默认插件集（Eslint, Prettier, TS, Tailwind, Copilot）。
- **IF** 进行大范围重构 **THEN** 优先调用 `refactoring.nvim` 而非手动修改。
- **IF** 发现状态栏干扰思维 **THEN** 强制执行 `disable LuaLine` 策略。

---

**执行 Checklists:**

- [ ] Leader 键是否映射为空格？
- [ ] Neovim 版本是否 $\ge 0.10$ (验证 Inline Hints)？
- [ ] Mason 内部语言服务器是否已完成安装？
- [ ] 状态栏是否已移除以优化空间？
