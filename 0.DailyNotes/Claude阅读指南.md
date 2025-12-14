---
aliases:
date: 2025-08-28 16:27
tags:
source:
  - https://www.anthropic.com/engineering/claude-code-best-practices
view-count: 6
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
