---
view-count: 7
update: 2026-01-07 16:07
related:
  - "[[Roadmap]]"
  - "[[2025-12-05-Python学习套件]]"
  - "[[如何才算学好了Python]]"
---

当然可以！以下是将你提供的笔记（特别是 **“常用命令”** 部分）从 `grep` 迁移到更现代、高效的 **`fd` + `ripgrep`（`rg`）** 组合的改写版本。这种组合不仅速度更快，而且语法更简洁、默认行为更智能（例如自动递归、尊重 `.gitignore` 等）。

---

## ✅ 改写为 `fd` + `ripgrep`（`rg`）版本

> 💡 前提：已安装 [`ripgrep`](https://github.com/BurntSushi/ripgrep)（命令 `rg`）和 [`fd`](https://githubute.com/sharkdp/fd)（命令 `fd`）。\
> 若未安装，在 Debian/Ubuntu 上可运行：
>
> ```bash
> sudo apt install ripgrep fd-find
> # 注意：在某些系统中 fd 命令名为 fdfind，可创建软链接：sudo ln -s $(which fdfind) /usr/local/bin/fd
> ```

---

### 🔍 常用命令（`fd` + `rg` 版）

```bash
# 查找所有类定义（仅 .py 文件）
rg "^class " --type py

# 查找所有函数入口（前20个）
rg "^def " --type py | head -20

# 查找导入关系（from / import）
rg "^(from|import) " --type py | sort | uniq

# 查找关键概念（不区分大小写，高亮匹配）
rg -i "llm|model|context|cache" --type py

# 追踪函数调用（查找 function_name( 的调用）
rg "function_name$" --type py
```

> ✅ 说明：
>
> - `rg` 默认递归搜索当前目录。
> - `--type py` 等价于 `--include="*.py"`，且 `ripgrep` 内置了常见语言类型（可通过 `rg --type-list` 查看）。
> - 不需要像 `grep -rn` 那样手动加行号和递归选项——`rg` 默认就带行号、文件路径、彩色高亮！

---

### 🧠 如果你想结合 `fd`（虽然 `rg` 本身已足够）

通常 **`rg` 单独使用就足够了**，但如果你有特殊文件筛选需求（比如排除某些子目录），可以用 `fd` 先找文件，再传给 `rg`：

```bash
# 用 fd 找出所有 .py 文件，再用 rg 搜索
fd -e py | xargs rg "^class "

# 或使用 rg 的 --files 选项（等效）
rg --files --type py | xargs rg "^def "
```

不过，**绝大多数场景下直接用 `rg` 更简洁高效**。

---

### 📚 推荐阅读顺序（不变，但可用 rg 辅助探索）

1. `rg -l "README|readme" -g "*.{md,txt}"` → 快速定位文档
2. `rg -l "setup\.py|pyproject\.toml"` → 找构建配置
3. `rg -l "__main__|if __name__" --type py` → 找入口点
4. `fd core -t d | xargs fd -e py | head -5` → 列出 core 目录下最简单的 Python 文件
5. `fd test -t d | xargs fd -e py` → 查看测试用例
6. `rg "^class\s+\w+" --type py` → 全局查看类定义

---

### ✅ 总结优势

| 原命令                                   | 新命令                      | 优势               |
| ------------------------------------- | ------------------------ | ---------------- |
| `grep -rn "^class " --include="*.py"` | `rg "^class " --type py` | 更短、更快、自带颜色/行号/路径 |
| 需要手动指定递归、行号、文件类型                      | `rg` 默认全有                | 开箱即用             |
| 无法智能跳过 `.git`/`node_modules`          | `rg` 自动跳过                | 更干净的结果           |

---

如需，我也可以帮你写一个 **`alias` 快捷方式**，让 `grep` 命令自动转为 `rg`（兼容模式）！
