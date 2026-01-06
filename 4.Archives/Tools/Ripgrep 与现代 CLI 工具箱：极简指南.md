---
date: 2025-06-10 19:10
tags:
  - Domain/Productivity/Tools
view-count: 4
---
# Ripgrep 与现代 CLI 工具箱：极简指南

---

### 一、 核心本质
**命令行工具 = 代码库的“高精度雷达”**。
目标：通过 **高速检索** 与 **组合管道**，将万级文件转化为即时可得的工程见解。

### 二、 Ripgrep (rg) 核心参数矩阵

| 需求 | 参数 | 功能说明 |
| :--- | :--- | :--- |
| **基础搜索** | `rg "pattern"` | 递归搜索字符串/正则 (默认尊重 `.gitignore`) |
| **上下文** | `-C 5` / `-A` / `-B` | 显示匹配行前后各 N 行代码 |
| **文件类型** | `-t py` / `-T js` | 仅搜索（或排除）特定语言文件 |
| **范围限制** | `-g 'src/**/*.go'` | 通过 Glob 模式精确包含/排除路径 |
| **统计模式** | `-c` / `--stats` | 仅输出匹配行数或详细执行统计 |
| **穿透模式** | `-u` / `-uu` / `-uuu` | 搜索被忽略文件、隐藏文件甚至二进制文件 |

### 三、 辅助工具生态位 (The Ecosystem)

- **查找 (Find)**：`fd` (比 `find` 快，语法直观，默认忽略无效路径)。
- **过滤 (Filter)**：`fzf` (交互式模糊查找，万能匹配器)。
- **导航 (Navigate)**：`zoxide` (智能 `cd`，基于访问频率自动跳转)。
- **查看 (View)**：`bat` (带语法高亮和 Git 状态的 `cat`)。
- **差异 (Diff)**：`delta` (并排显示、语法高亮的超级 `diff`)。
- **处理 (Process)**：`jq` (命令行 JSON 瑞士军刀)。

### 四、 核心原则 (Principles)
- **忽略即速度**：rg 和 fd 默认遵守 `.gitignore`，手动过滤琐碎信息是低效的，系统级忽略才是常态。
- **组合胜过单体**：利用管道 (`|`) 组合工具（如 `rg ... | fzf`），建立个性化的信息检索工作流。
- **模糊即效率**：放弃精确记忆完整路径，利用 `fzf` 和 `zoxide` 的模糊匹配实现毫秒级定位。

### 五、 关联笔记
- [[思维模型：极简认知工具箱]] (底层决策逻辑)
- [[内容结构模式：产品化创作框架]] (工具化输出范式)
- [[高级开发者多场景高效沟通]] (技术信息对齐)

**参考文献/资源**

> [!NOTE]
> 
> *   ripgrep (rg): [https://github.com/BurntSushi/ripgrep](https://github.com/BurntSushi/ripgrep)
> *   fd: [https://github.com/sharkdp/fd](https://github.com/sharkdp/fd)
> *   ag (The Silver Searcher): [https://github.com/ggreer/the_silver_searcher](https://github.com/ggreer/the_silver_searcher)
> *   fzf: [https://github.com/junegunn/fzf](https://github.com/junegunn/fzf)
> *   zoxide: [https://github.com/ajeetdsouza/zoxide](https://github.com/ajeetdsouza/zoxide)
> *   eza: [https://github.com/eza-community/eza](https://github.com/eza-community/eza)
> *   bat: [https://github.com/sharkdp/bat](https://github.com/sharkdp/bat)
> *   delta: [https://github.com/dandavison/delta](https://github.com/dandavison/delta)
> *   tldr: [https://tldr.sh/](https://tldr.sh/)
> *   htop: [https://github.com/htop-dev/htop](https://github.com/htop-dev/htop)
> *   btop: [https://github.com/aristocratos/btop](https://github.com/aristocratos/btop)
> *   jq: [https://github.com/stedolan/jq](https://github.com/stedolan/jq)
> *   Algorithm Visualizer: [https://algorithm-visualizer.org/](https://algorithm-visualizer.org/)
> *   trekhleb/javascript-algorithms: [https://github.com/trekhleb/javascript-algorithms](https://github.com/trekhleb/javascript-algorithms)
> *   keon/algorithms: [https://github.com/keon/algorithms](https://github.com/keon/algorithms)
> 
