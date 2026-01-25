---
view-count: 9
update: 2026-01-09 13:26
related:
  - "[[Anki卡牌仓库]]"
  - "[[PostgreSQL开发者实战指南]]"
  - "[[学习框架]]"

tags: ["Domain/Cognitive/Tools", "Type/Reference"]

---
# LazyVim 精华 (Brutally Minimal)

## 核心概念

**LazyVim**
Neovim 配置框架，基于 `lazy.nvim` 插件管理器，强调懒加载和模块化

**安装**

```bash
git clone https://github.com/LazyVim/Starter ~/.config/nvim
```

**目录结构**

```
lua/config/     # 用户配置
lua/plugins/    # 插件配置
init.lua        # 入口文件
lazy-lock.json  # 版本锁定
```

---

## 插件管理

**查看插件**
`:Lazy` 打开管理界面

**更新同步**
`:Lazy sync`

**性能分析**
`:Lazy profile` 查看加载耗时

**启用/禁用**

```lua
-- plugins/example.lua
{ "user/plugin", enabled = false }
```

**懒加载**

```lua
{ "user/plugin", event = "VeryLazy" }
{ "user/plugin", cmd = "Command" }
{ "user/plugin", keys = "<leader>x" }
```

**立即加载**

```lua
{ "user/plugin", lazy = false, priority = 1000 }
```

---

## 键绑定

**Leader 键**
默认 `Space`，修改：

```lua
vim.g.mapleader = ","
```

**核心快捷键**

```
<leader>ff  # 查找文件
<leader>fg  # grep 搜索
<leader>bd  # 关闭缓冲区
<leader>e   # 文件树
<leader>E   # 切换文件树
```

**查看所有快捷键**
`:WhichKey`

**自定义键绑定**

```lua
-- config/keymaps.lua
vim.keymap.set("n", "<leader>x", ":cmd<CR>")
```

---

## LSP

**安装语言服务器**
`:Mason` 打开 UI 安装

**查看状态**
`:LspInfo`

**核心操作**

```
gd          # 跳转定义
gr          # 查找引用
K           # 悬停文档
<leader>cr  # 重命名
<leader>ca  # 代码动作
<leader>cf  # 格式化
```

**禁用自动格式化**

```lua
-- config/lsp.lua
format = { enabled = false }
```

---

## 补全

**触发**
插入模式自动触发，或 `Ctrl-n`/`Ctrl-p`

**代码片段**
输入缩写 + `Tab` 展开，`Tab`/`Shift-Tab` 跳转占位符

**配置源**

```lua
-- plugins/cmp.lua
sources = {
  { name = "nvim_lsp" },
  { name = "luasnip" },
  { name = "path" }
}
```

---

## Telescope

**核心命令**

```
:Telescope find_files
:Telescope live_grep
:Telescope buffers
:Telescope help_tags
:Telescope lsp_document_symbols
```

---

## 文件树 (neo-tree)

**操作**

```
<leader>e   # 打开
<leader>E   # 切换
a           # 创建文件/目录
r           # 重命名
d           # 删除
```

---

## Git (gitsigns)

**查看状态**
行号旁显示修改标记

**操作**

```
hp   # 暂存当前行
gsp  # 预览更改
gsu  # 撤销更改
```

**提交**
`:Neogit` 图形化界面

**查看历史**

```
:Telescope git_commits
:Telescope git_branches
```

---

## 调试 (DAP)

**安装调试器**
通过 Mason 安装

**操作**

```
db          # 设置断点
<leader>dc  # 启动调试
<leader>dn  # 下一步
<leader>du  # 步出
<leader>di  # 步进
```

**配置**

```lua
-- config/dap.lua
dap.adapters.python = { ... }
dap.configurations.python = { ... }
```

---

## 终端

**打开**

```
:term
<leader>tt  # 水平分屏终端
```

**模式切换**

```
i/a              # 进入插入模式
Ctrl-\ Ctrl-n    # 退出到普通模式
```

---

## Treesitter

**安装语法**
`:TSInstall all` 或 `:TSInstall python`

**查看状态**
`:TSBufEnable highlight`

**折叠**
`za` 切换折叠

---

## 配置

**选项**

```lua
-- config/options.lua
vim.o.shiftwidth = 2
vim.o.tabstop = 2
vim.o.expandtab = true
vim.wo.number = true
vim.wo.relativenumber = true
vim.o.mouse = "a"
```

**自动命令**

```lua
-- config/autocmds.lua
vim.api.nvim_create_autocmd("BufWritePre", {
  pattern = "*",
  command = ":%s/\\s\\+$//e"  -- 删除行尾空格
})
```

**主题**

```lua
-- config/options.lua
vim.cmd("colorscheme tokyonight")
```

**添加新主题**

```lua
-- plugins/theme.lua
{ "folke/gruvbox.nvim", lazy = false, priority = 1000 }
```

---

## 其他

**注释**

```
gcc   # 注释行
gc    # 可视模式注释区域
```

**括号自动补全**
`nvim-autopairs` 默认启用

**状态栏**
`lualine.nvim` 默认启用，自定义：

```lua
-- config/lualine.lua
sections = { ... }
```

**缩进线**
`indent-blankline.nvim` 可视化缩进层级

**拼写检查**

```
:set spell
zg  # 添加到字典
```

---

## 诊断

**健康检查**
`:checkhealth`

**插件日志**
`:Lazy log`

**LSP 信息**
`:LspInfo`

**Treesitter 状态**
`:TSBufEnable highlight`

---

## 进阶

**自定义模块**

```lua
-- lua/user/mymodule.lua
require("user.mymodule")
```

**覆盖默认配置**
在对应模块文件返回新配置

**备份配置**
推送 `~/.config/nvim` 到 GitHub

**重置配置**
删除 `~/.config/nvim` 重新克隆

**性能优化**

- `:Lazy profile` 分析加载
- 使用懒加载条件 (`event`, `cmd`, `keys`)
- 禁用不需要的插件

---

**核心理念**

懒加载 + 模块化 + 可定制
