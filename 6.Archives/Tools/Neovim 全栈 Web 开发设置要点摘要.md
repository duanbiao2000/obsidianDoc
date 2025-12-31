
### 二、基础设置与默认选项

1. **LazyVim 起始配置：**
    
    - 利用LazyVim starter作为起点，因其内置的Lazy插件管理器和优秀的初始配置。只需进行少量调整即可满足需求。
    - 默认启用包括eslint、prettier、typescript、json、tailwind支持以及GitHub Copilot等“必不可少”的插件。
2. **默认Vim选项：**
    
    - 将Leader键映射为空格键，设定文件类型默认编码为UTF8，启用行号显示，并使用当前缓冲区名称作为窗口标题。
    - 启用自动缩进，将制表符转换为空格（每级缩进为两个空格），并允许回删缩进和换行。
    - 搜索结果不区分大小写，并启用命令预览功能。

### 三、关键键绑定与UI美化

1. **通用键绑定：**
    
    - 对单个字符剪切操作进行优化，避免干扰剪贴板内容；对数字重构进行了细微改进。
    - 定义了保存、关闭文档，标签页与窗口管理，以及错误与诊断检查的快捷键。
2. **配色方案与UI美化：**
    
    - 使用sonokai配色方案提升视觉体验。
    - 禁用了pin dashboard插件和LuaLine，移除了状态栏以增加屏幕空间。
    - 使用noise.nvim替换消息弹出菜单，禁用了“无可用信息”的提示，并通过nvim-notify配置了通知显示选项。
    - 利用bufferline实现了GUI风格的标签页，并通过inline-nvim在所有打开窗口的右上角显示文件名。

### 四、核心插件与集成

1. **LSP与自动补全：**
2. 
    
    - mason.nvim作为包管理器，支持LSP、调试适配器协议、Linter和Formatter。
    - nvim-lspconfig用于配置语言服务器，nvim-cmp提供美观的自动补全下拉菜单，cmp-emoji则增加了图标支持。
    - 内联提示功能增强了代码理解，但需要Neovim 0.10及以上版本。
3. **语法高亮与代码结构：**
    
    - treesitter提供了强大的语法高亮、缩进和代码折叠功能。
4. **实用工具插件：**
    
    - mini high patterns用于直接显示颜色值，telescope实现快速查找文件等功能。
    - lazy-git和nvim-tree分别提供了Git版本控制支持和文件树视图。
    - nvim-dap允许直接在Neovim中执行数据库查询。
5. **重构插件：**
    
    - incremental-rename.nvim和refactoring.nvim简化了变量重命名和函数提取的过程。
6. **集成插件：**
    
    - rest.nvim使发送HTTP请求变得更加便捷。
    - neotest作为一个通用测试插件，支持多种测试框架，特别是Jest。

