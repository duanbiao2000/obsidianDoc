---
view-count: 5
---
<details><summary>1. LazyVim - Pre-configured Neovim distro</summary>Based on Lazy.nvim plugin manager.</details>
<details><summary>2. Installation: curl -s https://raw.githubusercontent.com/folke/lazyvim.org/main/install.sh | sh</summary>Standard install script.</details>
<details><summary>3. Config location: ~/.config/nvim</summary>Where LazyVim files reside.</details>
<details><summary>4. lua/config/lazy.lua - Main config file</summary>Entry point for customizations.</details>
<details><summary>5. lua/plugins/ - Directory for plugin configs</summary>Add or override plugins here.</details>
<details><summary>6. Lazy.nvim - Plugin manager used</summary>Handles lazy loading.</details>
<details><summary>7. :Lazy - Open Lazy UI</summary>Manage plugins: update, sync, etc.</details>
<details><summary>8. Leader key: Space</summary>Default leader for mappings.</details>
<details><summary>9. [leader]l  LazyVim menu</summary>Access Lazy commands.</details>
<details><summary>10. [leader]q - Quit</summary>Quick quit mapping.</details>
<details><summary>11. [leader]w - Save</summary>Quick save.</details>
<details><summary>12. [leader]h - No highlight</summary>Clear search highlights.</details>
<details><summary>13. [leader]fn - New file</summary>Create new file.</details>
<details><summary>14. [leader]xl - Location list</summary>Open location list.</details>
<details><summary>15. [leader]xq - Quickfix list</summary>Open quickfix.</details>
<details><summary>16. [leader]bb - Buffer list</summary>Via Telescope.</details>
<details><summary>17. [leader]bd - Delete buffer</summary>Close current buffer.</details>
<details><summary>18. [leader]ff - Find files</summary>Telescope find files.</details>
<details><summary>19. [leader]fg - Live grep</summary>Telescope grep.</details>
<details><summary>20. [leader]fb - Buffers</summary>Telescope buffers.</details>
<details><summary>21. [leader]fh - Help tags</summary>Telescope help.</details>
<details><summary>22. [leader]gc - Comment line</summary>Toggle comment.</details>
<details><summary>23. [leader]gb - Comment block</summary>Block comment.</details>
<details><summary>24. [leader]sn - Noice history</summary>Notification history.</details>
<details><summary>25. [leader]ui - Toggle UI elements</summary>Via LazyVim menu.</details>
<details><summary>26. [leader]gg - LazyGit</summary>Open LazyGit.</details>
<details><summary>27. [leader]gf - Git file history</summary>Via Telescope.</details>
<details><summary>28. [leader]gl - Git blame line</summary>Toggle blame.</details>
<details><summary>29. [leader]gL - Git blame buffer</summary>Full buffer blame.</details>
<details><summary>30. [leader]gd - Git diff</summary>Open diff.</details>
<details><summary>31. [leader]L - Lazy extras</summary>Manage optional plugins.</details>
<details><summary>32. :Mason - Manage LSP servers</summary>Install/update LSPs.</details>
<details><summary>33. [leader]cl - LSP info</summary>Show LSP status.</details>
<details><summary>34. gd - Go to definition</summary>LSP jump to def.</details>
<details><summary>35. gD - Go to declaration</summary>LSP declaration.</details>
<details><summary>36. gr - References</summary>LSP find references.</details>
<details><summary>37. gI - Implementations</summary>LSP implementations.</details>
<details><summary>38. gy - Type definition</summary>LSP type def.</details>
<details><summary>39. K - Hover</summary>LSP hover info.</details>
<details><summary>40. [leader]cr - Rename</summary>LSP rename symbol.</details>
<details><summary>41. [leader]ca - Code action</summary>LSP code actions.</details>
<details><summary>42. [leader]cf - Format</summary>Format buffer.</details>
<details><summary>43. [leader]cd - Diagnostics</summary>Show diagnostics.</details>
<details><summary>44. [d - Prev diagnostic</summary>Navigate prev.</details>
<details><summary>45. ]d - Next diagnostic</summary>Navigate next.</details>
<details><summary>46. [leader]cs - Signature help</summary>LSP sig help.</details>
<details><summary>47. Ctrl-Space - Completion</summary>Trigger cmp.</details>
<details><summary>48. Ctrl-n - Next completion</summary>In insert mode.</details>
<details><summary>49. Ctrl-p - Prev completion</summary>In insert mode.</details>
<details><summary>50. Ctrl-y - Confirm completion</summary>Accept suggestion.</details>
<details><summary>51. [leader]ft - Telescope todo</summary>Find todos.</details>
<details><summary>52. [leader]fw - Grep word</summary>Telescope current word.</details>
<details><summary>53. [leader]fR - Resume Telescope</summary>Resume last search.</details>
<details><summary>54. [leader]fr - Recent files</summary>Telescope oldfiles.</details>
<details><summary>55. [leader]fc - Commands</summary>Telescope commands.</details>
<details><summary>56. [leader]fk - Keymaps</summary>Telescope keymaps.</details>
<details><summary>57. [leader]fm - Man pages</summary>Telescope man.</details>
<details><summary>58. [leader]fs - Symbols</summary>Telescope symbols.</details>
<details><summary>59. [leader]fd - Diagnostics</summary>Telescope diagnostics.</details>
<details><summary>60. [leader]fC - Command history</summary>Telescope cmd history.</details>
<details><summary>61. [leader]uC - Colorscheme</summary>Toggle colorscheme.</details>
<details><summary>62. [leader]uB - Background</summary>Toggle bg.</details>
<details><summary>63. [leader]ub - Bufferline</summary>Toggle bufferline.</details>
<details><summary>64. [leader]uc - Conceal</summary>Toggle conceal.</details>
<details><summary>65. [leader]uD - Diagnostics</summary>Toggle diag bg.</details>
<details><summary>66. [leader]ud - Document highlight</summary>Toggle doc hl.</details>
<details><summary>67. [leader]uh - HL chunk</summary>Toggle chunk hl.</details>
<details><summary>68. [leader]ui - Indent guides</summary>Toggle indent.</details>
<details><summary>69. [leader]ul - Line numbers</summary>Toggle numbers.</details>
<details><summary>70. [leader]uL - LSP</summary>Toggle LSP.</details>
<details><summary>71. [leader]un - Notifications</summary>Toggle noice.</details>
<details><summary>72. [leader]up - Pairs</summary>Toggle autopairs.</details>
<details><summary>73. [leader]us - Spell</summary>Toggle spellcheck.</details>
<details><summary>74. [leader]uS - Syntax</summary>Toggle treesitter.</details>
<details><summary>75. [leader]ut - Treesitter context</summary>Toggle context.</details>
<details><summary>76. [leader]uT - Transparent</summary>Toggle transparency.</details>
<details><summary>77. [leader]uw - Wrap</summary>Toggle wrap.</details>
<details><summary>78. :LazyExtras - Install extras</summary>Add optional features.</details>
<details><summary>79. lua/config/options.lua - Global options</summary>Customize vim options.</details>
<details><summary>80. lua/config/keymaps.lua - Custom keymaps</summary>Add your mappings.</details>
<details><summary>81. lua/config/autocmds.lua - Autocommands</summary>Custom autocmds.</details>
<details><summary>82. [leader]tn - Next terminal</summary>Navigate terminals.</details>
<details><summary>83. [leader]tp - Prev terminal</summary>Navigate prev.</details>
<details><summary>84. [leader]tf - Float terminal</summary>Open floating term.</details>
<details><summary>85. [leader]tt - Toggle terminal</summary>Toggle term.</details>
<details><summary>86. [leader]cm - Mason update</summary>Update LSPs.</details>
<details><summary>87. [leader]cM - Markdown preview</summary>If extra installed.</details>
<details><summary>88. [leader]cR - Restart LSP</summary>Restart servers.</details>
<details><summary>89. [leader]ch - Checkhealth</summary>Neovim health.</details>
<details><summary>90. [leader]ci - Inspector</summary>LSP inspector.</details>
<details><summary>91. [leader]gd - Diffview open</summary>Git diffview.</details>
<details><summary>92. [leader]gh - Hunk preview</summary>Git hunk.</details>
<details><summary>93. ]h - Next hunk</summary>Navigate hunks.</details>
<details><summary>94. [h - Prev hunk</summary>Navigate prev.</details>
<details><summary>95. [leader]gs - Stage hunk</summary>Git stage.</details>
<details><summary>96. [leader]gS - Stage buffer</summary>Stage all.</details>
<details><summary>97. [leader]gu - Unstage hunk</summary>Unstage.</details>
<details><summary>98. [leader]gU - Unstage buffer</summary>Unstage all.</details>
<details><summary>99. [leader]gr - Reset hunk</summary>Reset changes.</details>
<details><summary>100. [leader]gR - Reset buffer</summary>Reset all.</details>
---

当然可以！以下是 **LazyVim**（基于 Neovim 的现代化配置框架，使用 `lazy.nvim` 作为插件管理器）从入门到精通的 **100 个必须掌握的知识点**，采用 HTML 的 `<details>` 和 `<summary>` 格式展示，便于折叠浏览与学习。

---

<details>
<summary>1. LazyVim 是什么？</summary>
LazyVim 是一个基于 Neovim 的开箱即用的现代化配置框架，使用 <code>lazy.nvim</code> 作为插件管理器，强调模块化、性能和可定制性。
</details>

<details>
<summary>2. LazyVim 与 AstroVim 的区别？</summary>
LazyVim 使用 <code>lazy.nvim</code>，启动更快、模块更清晰；AstroVim 使用 <code>packer.nvim</code>，更早出现，生态广泛。LazyVim 更强调“懒加载”和“按需加载”。
</details>

<details>
<summary>3. 如何安装 LazyVim？</summary>
克隆模板仓库：<br>
<code>git clone https://github.com/LazyVim/Starter ~/.config/nvim</code><br>
首次启动自动安装插件。
</details>

<details>
<summary>4. LazyVim 配置目录结构</summary>
- <code>lua/config/</code>：用户配置<br>
- <code>lua/plugins/</code>：插件配置<br>
- <code>init.lua</code>：入口文件<br>
- <code>lazy-lock.json</code>：插件锁定版本
</details>

<details>
<summary>5. 如何启用/禁用插件？</summary>
在 <code>lua/plugins/</code> 中创建文件，使用 <code>enabled = false</code> 禁用插件，或通过 <code>return false</code> 条件性禁用。
</details>

<details>
<summary>6. 如何查看已加载的插件？</summary>
命令：<code>:Lazy</code> 打开插件管理界面，查看状态、依赖、加载条件等。
</details>

<details>
<summary>7. 什么是 lazy.nvim？</summary>
<code>lazy.nvim</code> 是一个高性能 Neovim 插件管理器，支持懒加载、条件加载、运行时优化，是 LazyVim 的核心。
</details>

<details>
<summary>8. 如何更新 LazyVim？</summary>
进入配置目录：<br>
<code>cd ~/.config/nvim</code><br>
<code>git pull</code><br>
重启 Neovim 并运行 <code>:Lazy sync</code>
</details>

<details>
<summary>9. 如何自定义启动界面？</summary>
LazyVim 使用 <code>alpha-nvim</code>，可在 <code>config/alpha.lua</code> 中修改启动页布局、禁用或替换。
</details>

<details>
<summary>10. 如何禁用 alpha 启动页？</summary>
在 <code>plugins/alpha.lua</code> 中返回 <code>enabled = false</code> 即可。
</details>

<details>
<summary>11. 如何设置主题？</summary>
LazyVim 默认使用 <code>tokyonight</code>，可在 <code>config/options.lua</code> 中修改：<br>
<code>vim.cmd("colorscheme tokyonight")</code>
</details>

<details>
<summary>12. 如何安装新主题？</summary>
添加插件到 <code>plugins/theme.lua</code>，例如：<br>
<code>{ "folke/gruvbox.nvim", lazy = false, priority = 1000 }</code>
</details>
<!--ID: 1761111102084-->


<details>
<summary>13. 如何配置 LSP（语言服务器）？</summary>
LazyVim 集成 <code>nvim-lspconfig</code>，支持自动配置常见语言服务器，只需安装对应语言服务器（如 <code>pyright</code>、<code>tsserver</code>）。
</details>

<details>
<summary>14. 如何安装语言服务器？</summary>
推荐使用 <code>mason.nvim</code>：<br>
<code>:Mason</code> 打开 UI，选择并安装 LSP、DAP、linter 等工具。
</details>

<details>
<summary>15. 如何查看当前 LSP 状态？</summary>
<code>:LspInfo</code> 查看已启用的 LSP 客户端及其状态。
</details>

<details>
<summary>16. 如何手动附加 LSP 到缓冲区？</summary>
<code>:LspStart pyright</code> 启动指定服务器<br>
<code>vim.lsp.buf.attach_client(0, client_id)</code>（高级）
</details>

<details>
<summary>17. 如何格式化代码？</summary>
默认绑定 <code>[leader]cf</code> 触发格式化，依赖 LSP 或 <code>null-ls</code>。
</details>

<details>
<summary>18. 如何禁用自动格式化？</summary>
在 <code>config/lsp.lua</code> 中设置：<br>
<code>format = { enabled = false }</code>
</details>
<!--ID: 1761111102094-->


<details>
<summary>19. 如何配置键绑定（Keymaps）？</summary>
在 <code>config/keymaps.lua</code> 中使用 <code>vim.keymap.set()</code> 添加或覆盖快捷键。
</details>

<details>
<summary>20. [leader] 键是什么？</summary>
默认是空格键 <code> </code>，用于组合快捷键，如 <code>[leader]ff</code> 搜索文件。
</details>

<details>
<summary>21. 如何修改 [leader] 键？</summary>
在 <code>config/options.lua</code> 中设置：<br>
<code>vim.g.mapleader = ","</code>
</details>

<details>
<summary>22. 常用 [leader] 快捷键有哪些？</summary>
- <code>[leader]ff</code>：查找文件<br>
- <code>[leader]fg</code>：grep 搜索<br>
- <code>[leader]bd</code>：关闭缓冲区<br>
- <code>[leader]pn</code>：切换主题
</details>

<details>
<summary>23. 如何查找所有快捷键？</summary>
使用 <code>:WhichKey</code> 插件查看所有绑定的快捷键树。
</details>

<details>
<summary>24. 如何自定义 WhichKey 提示？</summary>
在 <code>config/which-key.lua</code> 中修改或扩展快捷键描述。
</details>

<details>
<summary>25. 如何启用 Treesitter？</summary>
LazyVim 默认启用，使用 <code>nvim-treesitter</code>，需运行 <code>:TSInstall all</code> 安装语法。
</details>

<details>
<summary>26. 如何查看 Treesitter 高亮状态？</summary>
<code>:TSBufEnable highlight</code> 检查当前缓冲区是否启用。
</details>

<details>
<summary>27. 如何启用 Treesitter 折叠？</summary>
默认启用，使用 <code>za</code> 切换折叠，依赖 <code>foldmethod=expr</code>。
</details>

<details>
<summary>28. 如何禁用折叠？</summary>
在 <code>config/options.lua</code> 中设置：<br>
<code>vim.o.foldmethod = "manual"</code>
</details>

<details>
<summary>29. 如何使用 Telescope？</summary>
LazyVim 集成 <code>telescope.nvim</code>，常用命令：<br>
<code>:Telescope find_files</code>，<code>:Telescope live_grep</code>
</details>

<details>
<summary>30. 如何自定义 Telescope 源？</summary>
在 <code>plugins/telescope.lua</code> 中扩展 <code>pickers</code> 或 <code>extensions</code>。
</details>

<details>
<summary>31. 如何搜索帮助文档？</summary>
<code>:Telescope help_tags</code> 搜索 Neovim 内置帮助。
</details>

<details>
<summary>32. 如何查看 LSP 符号？</summary>
<code>:Telescope lsp_document_symbols</code> 查看当前文件符号。
</details>

<details>
<summary>33. 如何打开文件树（File Explorer）？</summary>
<code>[leader]e</code> 打开 <code>neo-tree</code> 文件浏览器。
</details>

<details>
<summary>34. 如何切换文件树隐藏/显示？</summary>
<code>[leader]E</code> 切换文件树可见性。
</details>

<details>
<summary>35. 如何在文件树中创建文件？</summary>
在 <code>neo-tree</code> 中按 <code>a</code> 创建新文件或目录。
</details>

<details>
<summary>36. 如何重命名文件树中的文件？</summary>
选中文件按 <code>r</code> 重命名。
</details>

<details>
<summary>37. 如何删除文件树中的文件？</summary>
按 <code>d</code> 删除，<code>shift + d</code> 彻底删除。
</details>

<details>
<summary>38. 如何启用自动补全（nvim-cmp）？</summary>
LazyVim 默认集成 <code>nvim-cmp</code>，自动从 LSP、luasnip、路径等来源补全。
</details>

<details>
<summary>39. 如何触发补全？</summary>
插入模式下自动触发，或按 <code>Ctrl-n</code>/<code>Ctrl-p</code> 手动选择。
</details>

<details>
<summary>40. 如何配置补全源？</summary>
在 <code>plugins/cmp.lua</code> 中修改 <code>sources</code> 列表。
</details>

<details>
<summary>41. 如何使用代码片段（Snippets）？</summary>
集成 <code>friendly-snippets</code> 和 <code>luasnip</code>，输入缩写（如 <code>for</code>）后按 <code>Tab</code> 展开。
</details>

<details>
<summary>42. 如何创建自定义代码片段？</summary>
在 <code>snippets/</code> 目录下创建 Lua 文件，使用 <code>luasnip</code> API 定义片段。
</details>

<details>
<summary>43. 如何跳转片段占位符？</summary>
使用 <code>Tab</code> 跳到下一个占位符，<code>Shift+Tab</code> 返回上一个。
</details>

<details>
<summary>44. 如何注释代码？</summary>
使用 <code>Comment.nvim</code>，快捷键：<br>
<code>gcc</code> 注释行，<code>gc</code> + 可视模式选择区域。
</details>

<details>
<summary>45. 如何启用括号自动补全？</summary>
<code>nvim-autopairs</code> 默认启用，自动补全 ()、{}、"" 等。
</details>

<details>
<summary>46. 如何禁用 autopairs 在某些文件类型？</summary>
在 <code>plugins/autopairs.lua</code> 中配置 <code>disable_filetype</code>。
</details>

<details>
<summary>47. 如何启用状态栏（lualine）？</summary>
LazyVim 默认使用 <code>lualine.nvim</code>，显示模式、文件名、LSP 状态等。
</details>

<details>
<summary>48. 如何自定义 lualine 组件？</summary>
在 <code>config/lualine.lua</code> 中修改左右侧组件内容。
</details>

<details>
<summary>49. 如何显示 Git 状态？</summary>
集成 <code>gitsigns.nvim</code>，在行号旁显示修改、添加、删除标记。
</details>

<details>
<summary>50. 如何查看 Git 差异？</summary>
<code>gsp</code> 预览暂存的更改，<code>gsu</code> 撤销更改。
</details>

<details>
<summary>51. 如何暂存 Git 文件？</summary>
在 <code>gitsigns</code> 中按 <code>hp</code> 暂存当前行更改。
</details>

<details>
<summary>52. 如何提交 Git？</summary>
使用 <code>:Neogit</code>（LazyVim 集成）打开图形化 Git 界面提交。
</details>

<details>
<summary>53. 如何查看 Git 日志？</summary>
<code>:Telescope git_commits</code> 查看提交历史。
</details>

<details>
<summary>54. 如何切换分支？</summary>
<code>:Telescope git_branches</code> 切换分支。
</details>

<details>
<summary>55. 如何启用调试（DAP）？</summary>
LazyVim 集成 <code>nvim-dap</code>，需安装对应语言的调试器（通过 Mason）。
</details>

<details>
<summary>56. 如何配置 DAP？</summary>
在 <code>config/dap.lua</code> 中添加适配器（adapters）和配置（configurations）。
</details>

<details>
<summary>57. 如何启动调试？</summary>
设置断点 <code>dp</code>，按 <code>[leader]dc</code> 启动调试。
</details>

<details>
<summary>58. 如何设置断点？</summary>
在代码行按 <code>db</code> 设置/取消断点。
</details>

<details>
<summary>59. 如何单步执行？</summary>
<code>[leader]dn</code> 下一步，<code>[leader]du</code> 步出，<code>[leader]di</code> 步进。
</details>

<details>
<summary>60. 如何查看变量？</summary>
调试时自动在侧边栏（<code>dap-ui</code>）显示变量和调用栈。
</details>

<details>
<summary>61. 如何启用自动保存？</summary>
LazyVim 默认不启用，可添加 autocmd：<br>
<code>vim.api.nvim_create_autocmd("BufWritePre", { command = "write" })</code>
</details>
<!--ID: 1761111102111-->


<details>
<summary>62. 如何启用自动切换工作目录？</summary>
<code>autochdir</code> 默认关闭，可在 <code>options.lua</code> 中启用。
</details>

<details>
<summary>63. 如何管理缓冲区？</summary>
使用 <code>:Telescope buffers</code> 切换缓冲区，<code>[leader]bd</code> 关闭。
</details>

<details>
<summary>64. 如何预览缓冲区？</summary>
在 <code>Telescope buffers</code> 中按 <code>Ctrl-p</code> 预览内容。
</details>

<details>
<summary>65. 如何启用终端？</summary>
<code>:term</code> 打开终端，<code>[leader]tt</code> 水平分屏终端。
</details>

<details>
<summary>66. 如何在终端中输入？</summary>
进入终端后按 <code>i</code> 或 <code>a</code> 进入插入模式输入命令。
</details>

<details>
<summary>67. 如何退出终端模式？</summary>
按 <code>Ctrl-\</code> <code>Ctrl-n</code> 退出到普通模式。
</details>

<details>
<summary>68. 如何发送代码到终端？</summary>
使用 <code>vim-slime</code> 或 <code>conjure</code> 插件发送代码块。
</details>

<details>
<summary>69. 如何启用拼写检查？</summary>
<code>:set spell</code> 启用，<code>zg</code> 添加单词到字典。
</details>

<details>
<summary>70. 如何跳转到匹配括号？</summary>
按 <code>%</code> 在 ()、{}、[] 间跳转。
</details>

<details>
<summary>71. 如何启用行尾空格高亮？</summary>
在 <code>plugins/highlight.lua</code> 中启用或自定义。
</details>

<details>
<summary>72. 如何禁用行号？</summary>
不推荐，但可在 <code>options.lua</code> 中设置：<br>
<code>vim.wo.number = false</code>
</details>

<details>
<summary>73. 如何启用相对行号？</summary>
默认启用，在 <code>options.lua</code> 中设置：<br>
<code>vim.wo.relativenumber = true</code>
</details>

<details>
<summary>74. 如何设置缩进为 2 个空格？</summary>
在 <code>options.lua</code> 中设置：<br>
<code>vim.o.shiftwidth = 2</code><br>
<code>vim.o.tabstop = 2</code><br>
<code>vim.o.expandtab = true</code>
</details>

<details>
<summary>75. 如何根据文件类型设置缩进？</summary>
使用 autocmd 或插件（如 <code>indent-blankline.nvim</code>）实现。
</details>

<details>
<summary>76. 如何显示缩进线？</summary>
<code>indent-blankline.nvim</code> 默认启用，可视化缩进层级。
</details>

<details>
<summary>77. 如何启用自动命令（autocmd）？</summary>
在 <code>config/autocmds.lua</code> 中使用 <code>vim.api.nvim_create_autocmd</code>。
</details>

<details>
<summary>78. 如何在保存时删除行尾空格？</summary>
在 <code>autocmds.lua</code> 中添加：<br>
<code>BufWritePre</code> 事件执行 <code>:%s/\s\+$//e</code>
</details>

<details>
<summary>79. 如何加载自定义 Lua 模块？</summary>
将 Lua 文件放在 <code>lua/user/</code> 目录，使用 <code>require("user.mymodule")</code> 加载。
</details>

<details>
<summary>80. 如何覆盖 LazyVim 默认配置？</summary>
在对应模块文件中 return 新配置，或使用 <code>setup = { ... }</code> 覆盖。
</details>
<!--ID: 1761111102118-->


<details>
<summary>81. 如何查看插件加载性能？</summary>
<code>:Lazy profile</code> 查看各插件加载耗时。
</details>

<details>
<summary>82. 如何延迟加载插件？</summary>
<code>lazy.nvim</code> 自动按 <code>event</code>、<code>cmd</code>、<code>keys</code> 等条件懒加载。
</details>

<details>
<summary>83. 如何强制立即加载插件？</summary>
设置 <code>lazy = false</code> 或使用 <code>cmd = "VimEnter"</code>。
</details>

<details>
<summary>84. 如何添加新插件？</summary>
在 <code>plugins/</code> 目录创建 Lua 文件，返回插件表：<br>
<code>{ "user/plugin", event = "VeryLazy" }</code>
</details>
<!--ID: 1761111102133-->


<details>
<summary>85. 如何卸载插件？</summary>
从 <code>plugins/</code> 目录删除对应文件，或设 <code>enabled = false</code>。
</details>

<details>
<summary>86. 如何备份 LazyVim 配置？</summary>
将 <code>~/.config/nvim</code> 目录推送到 GitHub 私有仓库。
</details>

<details>
<summary>87. 如何迁移 Vim 配置到 LazyVim？</summary>
提取关键键绑定、缩进设置、主题等，逐步集成到 LazyVim 模块中。
</details>

<details>
<summary>88. 如何调试插件加载问题？</summary>
使用 <code>:Lazy log</code> 查看错误日志，或 <code>:checkhealth</code> 检查依赖。
</details>

<details>
<summary>89. 如何启用/禁用行号分隔符？</summary>
在 <code>options.lua</code> 中设置 <code>numberwidth</code> 和 <code>signcolumn</code>。
</details>

<details>
<summary>90. 如何启用鼠标？</summary>
默认启用，在 <code>options.lua</code> 中 <code>vim.o.mouse = "a"</code>。
</details>

<details>
<summary>91. 如何禁用滚动条？</summary>
Neovim 无原生滚动条，GUI（如 Neovide）需单独配置。
</details>

<details>
<summary>92. 如何启用备份文件？</summary>
LazyVim 默认禁用，可在 <code>options.lua</code> 中启用：<br>
<code>vim.o.backup = true</code>
</details>

<details>
<summary>93. 如何设置交换文件目录？</summary>
<code>vim.o.directory = "/tmp//.swp"</code> 避免交换文件污染项目。
</details>

<details>
<summary>94. 如何查看当前模式？</summary>
状态栏显示，或 <code>:echo mode()</code>。
</details>

<details>
<summary>95. 如何启用 spelllang 中文？</summary>
安装中文拼写字典，设置：<br>
<code>vim.o.spelllang = "en,cjk"</code>
</details>

<details>
<summary>96. 如何快速切换文件？</summary>
<code>[leader]bp</code> 切换到上一个缓冲区，<code>[leader]`</code> 切换到最近文件。
</details>

<details>
<summary>97. 如何搜索帮助？</summary>
<code>:help lazyvim</code> 或 <code>:help mason</code> 查阅内置文档。
</details>

<details>
<summary>98. 如何贡献 LazyVim？</summary>
Fork GitHub 仓库，提交 PR 修复 bug 或添加功能。
</details>

<details>
<summary>99. 如何重置 LazyVim 配置？</summary>
删除 <code>~/.config/nvim</code> 并重新克隆 Starter 仓库。
</details>

<details>
<summary>100. 如何持续提升 LazyVim 技能？</summary>
- 阅读 <code>:help lazy</code><br>
- 学习 <code>lazy.nvim</code> 高级功能（条件加载、模块化）<br>
- 参与社区（Discord、GitHub Issues）<br>
- 构建自己的模块并分享
</details>

