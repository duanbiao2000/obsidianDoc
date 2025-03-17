---
aliases:
  - Neovim从零开始设置教程
createdAt: 2024-11-10 14:26
categories:
  - Tools
tags:
  - Effective/Tools
  - Archive
---
以上配置涵盖了从语法高亮、代码导航、自动补全、自动格式化到 Git 集成等多个方面，可以显著提升开发效率和代码质量。
<!--more-->

视频链接:
[Neovim从零开始设置教程！🛠️_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1gqDLYhEeH/?vd_source=7038f96b6bb3b14743531b102b109c43)

## 初级概念

1. **Neovim 安装**：
   - 确保 Neovim 已安装，可通过 `nvim --version` 检查版本。
   - 如果未安装，可访问 Neovim GitHub 仓库获取安装指南。

2. **基础配置**：
   - Neovim 配置文件位于 `~/.config/nvim/init.lua`。
   - 配置文件在每次启动 Neovim 时加载。
   - 可以通过设置选项来自定义 Neovim，例如启用行号：`vim.wo.number = true`。

3. **配置语言 Lua**：
   - Neovim 使用 Lua 作为配置语言，对于已知其他编程语言的用户来说，Lua 易于上手。
   - 推荐资源：learnxinyminutes.com/doog 以快速学习 Lua 基础。

4. **模块化配置**：
   - 通过 `require` 导入其他 Lua 文件，实现配置的模块化。
   - 在 `~/.config/nvim/lua/` 目录下创建模块文件。

5. **Kickstart nvim**：
   - Kickstart nvim 是一个最小化的模板，用于快速开始自定义配置。
   - 克隆 Kickstart 仓库以获取其配置作为起点。

6. **插件管理器**：
   - 使用 `lazy.nvim` 作为插件管理器。
   - 克隆并配置 `lazy.nvim` 以管理其他插件。

7. **核心插件**：
   - **neotree**：文件树插件。
   - **nvim-lspconfig**：LSP 配置插件。
   - **telescope.nvim**：模糊查找器插件。
   - **nvim-treesitter**：语法树插件。
   - **nvim-cmp**：自动补全插件。
   - **gitsigns.nvim**：Git 集成插件。

8. **LSP 集成**：
   - LSP 提供代码跳转、自动补全、悬停信息等功能。
   - 使用 Mason 安装语言服务器。
   - 配置 LSP 以支持多种语言。

9. **自动补全和格式化**：
   - 使用 `nvim-cmp` 和 `LuaSnip` 提供自动补全功能。
   - 使用 `null-ls` 和 `Mason` 进行自动代码格式化。

10. **其他插件**：
    - **fidget.nvim**：Git 状态显示插件。
    - **which-key.nvim**：快捷键提示插件。
    - **vim-sneak**：快速跳转插件。
    - **nvim-autopairs**：自动补全括号和引号插件。
    - **nvim-colorizer**：颜色高亮插件。

11. **配置文件结构**：
    - 创建 `~/.config/nvim/lua/plugins/` 目录，用于存放插件配置。
    - 在 `init.lua` 中使用 `require` 导入插件配置。

12. **个性化配置**：
    - 根据个人喜好调整插件设置和快捷键。
    - 通过克隆 Kickstart 配置作为起点，然后根据需要添加或修改插件和配置。

这个视频提供了一个全面的指南，帮助用户从零开始构建一个现代化、高效的 Neovim 环境。

## 概念vs提问

作者选择Kickstart作为个人配置的起点是因为Kickstart提供了很多已经解决的复杂问题，同时保持了配置的简洁性，允许用户在此基础上快速搭建并定制自己的Neovim配置。

> [!NOTE]
>
> 1. "Kickstart is a minimal template that is designed to be a starting point for one's own configuration."
> 2. "I feel like learning someone else's workflow rather than creating my own."
> 3. "Kickstart strikes the perfect balance, here it is minimal but all the hard stuff has been solved."
>
> 这些引用显示了作者选择Kickstart的核心理由：它提供了一个平衡点，既不是过于复杂，也不是功能不全，而是恰到好处地提供了一个可以快速开始并个性化定制的基础。

> [!NOTE]
>
> 1. **引言和概述**
>    - "in this video I'm going to rebuild my entire new Vim configuration from scratch by the end we'll have a config, that has most of the features you'll find in a modern IDE like vs code"
>    - "we'll base our config, on a project called Kickstart nvim, Kickstart is a minimal template that is designed to be a starting point for one's own configuration"
> 2. **Neovim安装和配置基础**
>    - "the first thing we want to do is make sure that we have neovim installed so if you type nvim --version you should see the version of neovim"
>    - "let's go back to the terminal we can open neovim with the NVM command but currently it looks pretty boring and basic to customize it"
> 3. **Lua配置语言入门**
>    - "Neovim uses Lua, as a configuration language seemed a bit intimidating to me at first but actually, it turns out that Lua is an incredibly simple language"
> 4. **配置文件的模块化**
>    - "since Lua is a programming language it means that we can use programming concepts like variables functions and loops and of course we can also import other files, this allows us to make our config, incredibly modular"
> 5. **Kickstart nvim的使用**
>    - "let's have a look at the Kickstart GitHub repo if we scroll down a bit in the readme, you can see that Kickstart is not meant to be a neovim distribution it's not fully featured it's meant to be a starting point for your own configuration"
>    - "if we scroll down a bit further you can find the Clone instructions"
> 6. **个性化配置**
>    - "now let's take your config to the next level by having a look at Kickstart"
>    - "if you for example want to have a file tree plugin you could uncomment neotree"
> 7. **Vim选项和键位映射**
>    - "let's configure some Vim options to get a better experience with the editor"
>    - "let's open neotree Again by going into command mode and typing NEtree"
> 8. **插件管理和使用**
>    - "since Lua is a programming language it means that we can use programming concepts like variables functions and loops and of course we can also import other files"
>    - "let's create this file and move our option there"
> 9. **高级配置**
>    - "now let's take your config to the next level by having a look at Kickstart"
>    - "let's go into command mode e lua plugins color theme"
> 10. **LSP集成**
>     - "LSP integration with AO completion"
>     - "LSP stands for language server protocol and it is what allows us to jump to the definition of a function, for example across files"
> 11. **自动补全和格式化**
>     - "a Sleek status line and buffer line a fuzzy finder G integration and so much more"
>     - "I would like to change in the color theme so let's go into command mode e lua plugins color theme"
> 12. **Git集成**
>     - "let's also add a Sleek buffer line to our config so we can always see which files we're currently working in"
> 13. **启动屏幕和美化**
>     - "let's add a nice greeting screen with the alpha plugin"
>     - "this plugin will show up every time you start neovim and it will display some character art like here and your most recently used files"
> 14. **其他插件和功能**
>     - "I just want to add a few more miscellaneous plugins let's add them now"
>     - "the Vim TX Navigator is super essential for my workflow this allows me to seamlessly navigate between vim and t-x splits"
> 15. **总结**
>     - "if you found this valuable at all please consider liking and subscribing it really does help the channel"
>     - "I will create a git repository with this entire configuration and leave a link to it in the description box down below for your reference"
>
> 这些引用直接来自作者的原话，证实了讲稿的结构和流程。

在视频中，作者提到了对`KICKSTART.NVIM`文件的详细注释，他强调了阅读这些注释的重要性，因为它们非常简洁且写得非常好，能够帮助观众了解配置是如何工作的。以下是作者的原话：

> [!NOTE]
>
> "if you want to learn more about how configuration Neovim works in general I would highly encourage you to read through all of these comments, they're extremely concise and well written and it taught me personally a lot about how the configuration works" 。

## (核心)进阶

[kickstart.nvim/init.lua at master · nvim-lua/kickstart.nvim · GitHub](https://github.com/nvim-lua/kickstart.nvim/blob/master/init.lua)
