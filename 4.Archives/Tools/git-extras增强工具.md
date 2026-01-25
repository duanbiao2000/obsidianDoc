---
aliases:
date: 2026-01-12 11:06
tags:
  - #Domain/Technology/Git
  - #Domain/Technology/DevOps
  - Domain/Technology/Git
  - Domain/Cognitive/Tools
  - Type/Reference
  - '#Domain/Technology/Git'
  - '#Domain/Technology/DevOps'
source:
rating:
related:
  - "[[Git典型工作流及高阶操作]]"
  - "[[Git提交规范]]"
  - "[[Git版本控制与回滚]]"
view-count: 4
---
以下是 **`git-extras`** 提供的全部命令，按功能分类整理为清晰列表，并附上简要说明，便于快速查阅与使用。

---

## 🧰 一、仓库初始化与设置

| 命令 | 说明 |
|------|------|
| `git setup` | 初始化仓库（若无）、添加所有文件、创建初始提交 |
| `git gh-pages` | 快速设置 `gh-pages` 分支用于 GitHub Pages |
| `git force-clone` | 强制克隆：若目标目录存在且是 Git 仓库，则重置为远程最新状态（⚠️会丢本地修改） |
| `git get` | 克隆仓库到预设目录（通过 `git config git-extras.get.clone-path` 配置） |

---

## 🌿 二、分支管理

| 命令 | 说明 |
|------|------|
| `git feature` / `bug` / `refactor` / `chore` | 快速创建/切换/合并带前缀的分支（如 `feature/login`） |
| `git create-branch` | 创建本地分支（可选设远程跟踪） |
| `git delete-branch` | 删除本地和远程同名分支 |
| `git rename-branch` | 重命名本地分支并同步到远程 |
| `git fresh-branch` | 创建一个**空的**新分支（无父提交，适合文档/gh-pages） |
| `git delete-merged-branches` | 删除所有已合并的本地分支 |
| `git delete-squashed-branches` | 删除已被 squash 合并的分支 |
| `git show-merged-branches` | 列出已合并到当前分支的分支 |
| `git show-unmerged-branches` | 列出未合并的分支 |
| `git brv` | 按最后提交时间排序列出分支（含远程信息） |

---

## 🔖 三、标签（Tag）管理

| 命令 | 说明 |
|------|------|
| `git release` | 创建带注释的标签、提交变更、推送标签（支持 semver：`--semver major/minor/patch`） |
| `git delete-tag` | 删除本地和远程标签 |
| `git rename-tag` | 重命名标签（本地+远程） |

---

## 🔄 四、提交与历史操作

| 命令 | 说明 |
|------|------|
| `git undo [N]` | 撤销最近 N 次提交（保留工作区更改） |
| `git wip` | 创建“Work In Progress”提交（包含所有变更） |
| `git unwip` | 撤销最近的 WIP 提交，恢复工作区 |
| `git squash <branch>` | 将某分支的所有提交压缩为**单个提交**合并到当前分支 |
| `git merge-into [src] dest` | 将 `src` 分支合并到 `dest`，**不切换当前分支** |
| `git graft <src> <dest>` | 将 `src` 分支的提交“嫁接”到 `dest` 分支 |
| `git reauthor` | 批量重写提交历史中的作者/提交者信息 |
| `git obliterate <file>` | **彻底删除**文件（包括历史记录和标签中） |
| `git magic` | 自动生成提交信息并提交 |
| `git stamp <text>` | 在最近提交末尾追加文本（如 Jira ID、Review 链接） |
| `git coauthor <name> <email>` | 为上次提交添加 Co-authored-by 尾部 |

---

## 🔍 五、信息查看与统计

| 命令 | 说明 |
|------|------|
| `git info` | 显示仓库详细信息（远程、分支、子模块、最近提交、配置等） |
| `git summary` | 项目摘要（年龄、活跃度、提交数、贡献者统计；支持 `--line` 按行统计） |
| `git effort` | 按文件统计提交次数（识别热点文件） |
| `git count` | 统计总提交数或按作者列出 |
| `git authors` | 生成 `AUTHORS` 文件（基于提交者邮箱） |
| `git contrib <author>` | 显示某作者的具体提交列表 |
| `git commits-since [date]` | 列出自指定日期以来的提交（默认“last week”） |
| `git standup [-a author] [-d days]` | 查看某人近期（如过去7天）的提交 |
| `git local-commits` | 列出本地有但远程没有的提交 |
| `git root` | 输出仓库根目录路径（可用于 `cd $(git root)`） |
| `git show-tree` | 图形化显示所有分支的提交历史（类似 `git log --graph --all` 增强版） |

---

## 🗂️ 六、文件与忽略规则

| 命令 | 说明 |
|------|------|
| `git ignore <pattern>` | 快速将模式添加到 `.gitignore` |
| `git ignore-io <lang>` | 从 gitignore.io 生成忽略规则（支持 `-a` 追加、`-r` 替换） |
| `git touch <file>` | 创建文件并自动 `git add` |
| `git cp <src> <dst>` | 复制文件并保留 Git 历史（便于后续合并冲突处理） |
| `git rename-file <old> <new>` | 安全重命名文件（尤其适用于大小写变更） |
| `git reset-file <file> [commit]` | 将文件重置到 HEAD 或指定提交版本 |
| `git delta` | 列出与另一分支有差异的文件 |
| `git utimes [--newer]` | 将文件修改时间设为其最后一次提交时间 |

---

## 🌐 七、远程协作（GitHub / GitLab）

| 命令 | 说明 |
|------|------|
| `git pr <ID\|URL>` | 检出 GitHub Pull Request（支持 URL 和 `clean` 清理） |
| `git mr <ID\|URL>` | 检出 GitLab Merge Request |
| `git fork <repo>` | Fork 并克隆 GitHub 仓库，自动添加 `upstream` 远程 |
| `git pull-request` | 通过命令行创建 Pull Request |
| `git browse [remote]` | 在浏览器中打开仓库主页 |
| `git browse-ci [remote]` | 在浏览器中打开 CI 页面（如 GitHub Actions） |

---

## 🧹 八、清理与重置

| 命令 | 说明 |
|------|------|
| `git clear` | `git reset --hard` + 删除**所有**未跟踪文件（含 `.gitignore` 中的） |
| `git clear-soft` | `git reset --hard` + 删除未跟踪文件（**不含** `.gitignore` 中的） |

---

## ⚙️ 九、高级工具与批量操作

| 命令 | 说明 |
|------|------|
| `git bulk` | 对多个 Git 仓库批量执行命令（需先注册 workspace） |
| `git repl` | 进入 Git REPL 环境（无需输入 `git` 前缀） |
| `git alias` | 管理 Git 别名（定义/搜索/列出） |
| `git sed 'old' 'new'` | 在 Git 跟踪的文件中执行替换（类似 `sed`，但限于版本控制文件） |
| `git scp <remote> [commits...]` | 将变更文件同步到远程服务器工作目录（基于 `rsync`） |
| `git rscp` | 反向 `scp`：从远程拉取文件到本地 |
| `git archive-file` | 创建当前 HEAD 的 zip 归档（文件名含 commit hash） |
| `git changelog` | 根据 tag 和提交生成 CHANGELOG |
| `git guilt <old> <new>` | 计算两个版本间代码“责任”变化（基于 blame） |
| `git missing <branch>` | 显示当前分支与另一分支独有的提交 |
| `git lock/unlock/locked` | 本地文件锁定机制（非 Git 原生，仅标记） |
| `git merge-repo <repo> <branch> <dir>` | 将另一仓库的历史合并到当前仓库的指定目录 |
| `git psykorebase` | 智能变基：用一次冲突解决完成整个 rebase |
| `git rebase-patch <patch>` | 自动寻找可应用 patch 的提交并 rebase |
| `git sync [remote] [branch]` | 同步本地分支与远程（fetch + reset --hard） |
| `git paste` | 将提交内容上传到 pastebin（依赖 `pastebinit`） |
| `git abort` | 一键中止当前冲突操作（merge/rebase/cherry-pick） |
| `git continue` | 一键继续当前冲突操作 |

---

## ℹ️ 十、辅助命令

| 命令 | 说明 |
|------|------|
| `git extras` | 主命令：查看版本 (`--version`)、帮助 (`--help`)、更新 (`update`) |

---

### ✅ 使用建议

- **日常开发**：重点掌握 `git ignore`, `git feature`, `git undo`, `git summary`, `git pr`
- **团队协作**：善用 `git release`, `git coauthor`, `git changelog`
- **多仓库管理**：`git bulk` 是利器
- **安全第一**：`git obliterate`、`git force-clone`、`git clear` 等命令会**不可逆删除数据**，慎用！

> 💡 所有命令均可通过 `git extras --help` 查看，或单独 `git <command> --help` 获取详情。

这份清单可作为你的 **`git-extras` 速查手册**，大幅提升 Git 工作流效率！


`git-extras` 是一个非常实用的开源工具集，它在标准 Git 命令的基础上**扩展了大量高频、便捷的子命令**，极大提升了开发者在日常 Git 操作中的效率和体验。

---

## 📦 什么是 git-extras？

- **官方仓库**：<https://github.com/tj/git-extras>
- **作者**：TJ Holowaychuk（Node.js 生态早期贡献者）
- **本质**：一组用 Shell/Perl/Python 编写的 Git 插件脚本
- **安装后使用方式**：`git <命令>`，就像原生命令一样

> ✅ 示例：`git ignore`, `git setup`, `git feature`, `git undo` 等

---

## 🔧 安装方式（在 WSL / Linux / macOS）

### 在 Nix 环境中（推荐）：

```nix
# 在 devShell 的 packages 中添加
packages = with pkgs; [ git-extras ];
```

### Ubuntu/Debian：

```bash
sudo apt install git-extras
```

### macOS（Homebrew）：

```bash
brew install git-extras
```

---

## 🚀 常用命令 & 带来的便利

以下是最常用、最能提升效率的 `git-extras` 命令：

---

### 1. `git ignore <file|pattern>`

**作用**：快速将文件/模式添加到 `.gitignore`

```bash
git ignore "*.log"
git ignore node_modules/
```

✅ **便利性**：无需手动编辑 `.gitignore`，避免拼写错误，支持追加。

---

### 2. `git ignore-io <lang>`

**作用**：从 [gitignore.io](https://www.toptal.com/developers/gitignore) 自动生成某语言/IDE 的忽略规则

```bash
git ignore-io python > .gitignore
git ignore-io python,vscode,node >> .gitignore
```

✅ **便利性**：一键生成专业级 `.gitignore`，覆盖操作系统、编辑器、语言临时文件等。

---

### 3. `git setup <repo-url>`

**作用**：克隆 + 自动进入目录 + 初始化子模块（如果存在）

```bash
git setup https://github.com/user/project.git
# 相当于：
# git clone ...
# cd project
# git submodule update --init --recursive
```

✅ **便利性**：减少重复操作，尤其适合频繁切换项目。

---

### 4. `git feature | git bug | git refactor | git chore`

**作用**：基于 Git Flow 风格快速创建/切换分支

```bash
git feature user-login    # 创建并切换到 feature/user-login
git bug fix-crash         # → bug/fix-crash
git refactor api-v2       # → refactor/api-v2
```

✅ **便利性**：

- 自动加前缀，规范分支命名；
- 避免手动输入 `git checkout -b feature/xxx`；
- 团队协作更统一。

> 💡 对应命令还有 `git feature finish`（合并并删除分支）。

---

### 5. `git undo [N]`

**作用**：撤销最近 N 次提交（保留工作区更改）

```bash
git undo      # 撤销最后一次 commit，但保留修改
git undo 2    # 撤销最近两次 commit
```

✅ **便利性**：比 `git reset --soft HEAD~1` 更直观安全，尤其适合“提交太早想重写”的场景。

> ⚠️ 注意：不是 `git reset --hard`，不会丢代码！

---

### 6. `git effort`

**作用**：统计各文件的提交次数（粗略评估“热点文件”）

```bash
git effort
# 输出示例：
#  src/main.py        42
#  README.md          8
```

✅ **便利性**：快速识别频繁修改的模块，辅助重构决策。

---

### 7. `git summary`

**作用**：显示项目贡献者统计摘要

```bash
git summary
# 输出：
#  project  : my-app
#  repo age : 2 years
#  active   : 120 days
#  commits  : 420
#  files    : 89
#  authors  :
#     Alice    210 (50.0%)
#     Bob      180 (42.9%)
#     CI Bot   30  (7.1%)
```

✅ **便利性**：快速了解项目活跃度和人员分布。

---

### 8. `git release <version>`

**作用**：创建带标签的发布版本

```bash
git release v1.2.0
# 相当于：
# git tag -a v1.2.0 -m "Release v1.2.0"
# git push origin v1.2.0
```

✅ **便利性**：简化发布流程，避免忘记推送标签。

---

### 9. `git info`

**作用**：显示当前仓库的详细信息（远程地址、分支、HEAD 等）

```bash
git info
```

✅ **便利性**：比 `git remote -v` + `git branch -v` 更集中。

---

### 10. `git line-summary`

**作用**：按作者统计代码行数（需 `cloc` 工具）

```bash
git line-summary
```

✅ **便利性**：量化贡献（谨慎用于考核！），更多用于技术债分析。

---

## 🌟 总结：git-extras 带来的核心价值

| 价值点            | 说明                                                  |
| -------------- | --------------------------------------------------- |
| ✅ **减少重复输入**   | 如 `git checkout -b feature/xxx` → `git feature xxx` |
| ✅ **降低出错概率**   | 自动生成 `.gitignore`、规范分支名                             |
| ✅ **提升操作语义化**  | `git undo` 比 `git reset` 更易理解                       |
| ✅ **增强团队一致性**  | 统一分支策略、忽略规则                                         |
| ✅ **快速获取项目洞察** | `summary`、`effort` 等提供元数据视角                         |

---

## ⚠️ 注意事项

- `git-extras` 是**辅助工具**，不替代 Git 核心概念学习；
- 某些命令依赖外部工具（如 `cloc`、`hub`），若未安装会提示；
- 在 CI/脚本中慎用（非标准 Git 命令，可能不可移植）；
- 在 Nix Flakes 环境中，只需在 `devShell` 中加入 `git-extras`，即可在开发时使用，不影响构建纯净性。

---

## ✅ 推荐配置（Nix Flakes 示例）

```nix
devShells.default = pkgs.mkShell {
  packages = with pkgs; [
    git
    git-extras
    cloc          # 用于 line-summary
  ];
};
```

这样，所有团队成员进入 `nix develop` 后，都能使用这些高效命令！

---

需要我为你整理一份 **`git-extras` 速查表（cheatsheet）**，或者演示如何在 WSL + Nix 环境中结合 `git-extras` 和 `direnv` 实现全自动开发环境？
