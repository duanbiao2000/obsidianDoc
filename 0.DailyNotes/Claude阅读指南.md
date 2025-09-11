---
aliases:
date: 2025-08-28 16:27
tags:
source:
  - https://www.anthropic.com/engineering/claude-code-best-practices
---

`.claude/settings.json` 和 `~/.claude.json` 都是用于配置 Claude 相关工具（如 Claude Code）的文件，但两者在**作用范围、使用场景和共享属性**上有明显区别，具体如下：

| **区别维度** | `.claude/settings.json`                   | `~/.claude.json`                              |
| -------- | ----------------------------------------- | --------------------------------------------- |
| **文件位置** | 位于项目根目录下的 `.claude` 文件夹中                  | 位于用户的个人主目录（`~` 代表用户根目录）下                      |
| **作用范围** | 仅针对当前项目生效，是「项目级配置」                        | 对用户所有项目生效，是「全局级配置」                            |
| **使用场景** | 用于配置当前项目专属的工具规则、团队协作参数等，确保项目内的配置统一        | 用于配置用户个人习惯的全局规则（如通用工具偏好、个人权限等），适用于所有项目共享的个人设置 |
| **共享属性** | 建议签入源代码管理（如 Git），方便团队成员同步配置，保证团队协作时的规则一致性 | 属于个人本地配置，不建议共享（可能包含个人隐私或个性化设置），通常不会纳入源代码管理    |
| **优先级**  | 若与全局配置冲突，项目级配置可能优先生效（具体取决于工具的解析逻辑）        | 全局配置为默认值，若项目中存在同名配置，可能被项目级配置覆盖                |

简单来说，`.claude/settings.json` 是「团队/项目专用配置」，强调协作一致性；`~/.claude.json` 是「个人全局配置」，强调个人使用便利性。两者配合使用可实现「项目专属规则+个人通用习惯」的灵活配置。

---
## 示例

以下是 `.claude/settings.json` 和 `~/.claude.json` 的具体配置实例，基于 Claude Code 对「允许工具列表」的管理需求设计，可直接参考或修改使用：


### 1. `.claude/settings.json`（项目级配置，建议团队共享）
适用于特定项目的工具权限配置，例如前端项目可能需要允许更多文件编辑和构建工具，可签入 Git 确保团队成员使用一致的规则。

```json
{
  "allowedTools": {
    // 允许文件编辑操作（如修改代码文件）
    "Edit": {
      "enabled": true,
      // 限制仅允许编辑特定类型的文件（可选）
      "allowedFilePatterns": ["*.ts", "*.tsx", "*.js", "*.json", "*.md"]
    },
    // 允许 Bash 命令，限定安全的操作范围
    "Bash": {
      "enabled": true,
      // 允许的具体命令（支持通配符）
      "allowedCommands": [
        "npm run *",       // 允许所有 npm 脚本（如 build、test、lint）
        "git commit *",    // 允许 git 提交（带任意参数）
        "git push",        // 允许 git 推送
        "ls", "cd", "pwd"  // 允许基础目录操作命令
      ],
      // 禁止的危险命令（优先级高于允许列表）
      "blockedCommands": ["rm -rf *", "sudo *", "curl *"]
    },
    // 允许 MCP 工具（如 Puppeteer 用于前端截图）
    "mcp__puppeteer__puppeteer_navigate": {
      "enabled": true
    },
    // 允许 GitHub 相关操作
    "GitHub": {
      "enabled": true,
      "allowedActions": ["create_pr", "comment_on_pr", "label_issue"]
    }
  },
  // 其他项目级配置（如默认工作目录）
  "defaultWorkingDir": "./src",
  "autoConfirmSmallChanges": true  // 自动确认小型代码修改（如格式调整）
}
```


### 2. `~/.claude.json`（全局级配置，个人专用）
适用于所有项目的通用配置，例如个人习惯的工具偏好或全局安全规则，不建议共享。

```json
{
  "allowedTools": {
    // 全局允许的基础工具
    "Bash": {
      "enabled": true,
      // 个人常用的全局命令（如代码搜索工具 ripgrep）
      "allowedCommands": ["rg *", "grep *", "cat *"]
    },
    // 全局禁用高风险操作（覆盖项目配置）
    "Edit": {
      "enabled": true,
      // 个人额外限制：禁止编辑敏感文件
      "blockedFilePatterns": ["*.env", "*.key", "*.pem"]
    },
    // 禁用所有网络请求类工具（个人安全偏好）
    "Http": {
      "enabled": false
    }
  },
  // 全局默认设置（如输出日志级别）
  "logLevel": "info",
  // 个人习惯的提示模板路径
  "customPromptTemplatesDir": "~/.claude/commands"
}
```


### 配置说明：
- **优先级**：项目级配置（`.claude/settings.json`）会覆盖全局配置（`~/.claude.json`）中冲突的部分，非冲突配置会合并生效。
- **安全性**：通过 `allowedCommands` 和 `blockedCommands` 限制危险操作，避免误删文件或执行恶意命令。
- **灵活性**：可根据项目类型（如前端、后端、数据科学）调整 `allowedFilePatterns` 或 `allowedCommands`，例如后端项目可添加 `python *` 允许 Python 脚本执行。

通过以上配置，既能保证团队协作时的操作一致性，又能保留个人使用的灵活性。

---

### 为什么是rg 而不是 grep?

`rg` 是 **ripgrep** 的缩写，是一款比 `grep` 更快、功能更强大的命令行搜索工具，尤其适合在代码库中快速查找关键词、正则表达式等内容。它默认忽略 `.gitignore` 中的文件，且对代码文件有更好的支持（如自动识别编码、跳过二进制文件）。

以下是 `rg` 的核心用法示例，结合代码搜索场景说明：


### 1. 基础搜索：查找关键词
```bash
# 在当前目录及子目录中，搜索所有文件里的 "user_id"
rg "user_id"

# 搜索时不区分大小写（-i 即 --ignore-case）
rg -i "User_Id"

# 只搜索特定类型的文件（-t 指定文件类型，如 js、ts、md）
rg -t js "fetchData"  # 只在 JavaScript 文件中搜 "fetchData"
rg -t tsx "useState"  # 只在 TypeScript JSX 文件中搜 "useState"
```

支持的文件类型可通过 `rg --type-list` 查看（如 py、java、json 等）。


### 2. 搜索并显示上下文
```bash
# 显示匹配行的前后各 3 行内容（-C 即 --context）
rg -C 3 "error_log"

# 只显示匹配行的前 2 行（-B 即 --before-context）
rg -B 2 "unhandled rejection"

# 只显示匹配行的后 5 行（-A 即 --after-context）
rg -A 5 "successfully connected"
```


### 3. 正则表达式搜索（默认支持）
```bash
# 搜索所有以 "func" 开头、后面跟括号的内容（如函数定义）
rg "func \w+\(\)"

# 搜索邮箱格式（简单正则示例）
rg "\b[\w\.-]+@[\w\.-]+\.\w+\b"

# 关闭正则表达式，按纯文本搜索（-F 即 --fixed-strings）
rg -F "a.b.c"  # 此时 "." 不会被当作正则通配符
```


### 4. 排除/包含特定文件/目录
```bash
# 排除 node_modules 目录和 dist 目录（-g 即 --glob，支持通配符）
rg "api_key" -g "!node_modules" -g "!dist"

# 只搜索 src 目录下的文件
rg "config" -g "src/**/*"

# 排除 .json 文件
rg "password" -g "!*.json"
```


### 5. 其他实用选项
```bash
# 只显示匹配的文件名，不显示具体内容（-l 即 --files-with-matches）
rg -l "deprecated"  # 列出所有包含 "deprecated" 的文件路径

# 统计匹配次数（-c 即 --count）
rg -c "console.log"  # 显示每个文件中 "console.log" 出现的次数

# 以 JSON 格式输出结果（方便程序处理，-oJ 即 --json）
rg -oJ "user_login"

# 搜索时显示行号（默认已显示，-n 可显式开启）
rg -n "database_url"
```


### 为什么用 `rg` 而不是 `grep`？
- **速度更快**：底层用 Rust 实现，多线程搜索，比 `grep` 快 2-10 倍。
- **默认更智能**：自动忽略 `.gitignore`、`.ignore` 中的文件，跳过二进制文件和隐藏文件。
- **对代码友好**：原生支持多种编码（UTF-8、GBK 等），自动识别代码注释格式。

如果系统未安装，可通过包管理器安装（如 `brew install ripgrep`、`sudo apt install ripgrep`）。