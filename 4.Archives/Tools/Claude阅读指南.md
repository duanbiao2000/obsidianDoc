---
aliases:
date: 2025-08-28 16:27
tags: ["Domain/Cognitive/Tools", "Type/Reference"]
source:
  - https://www.anthropic.com/engineering/claude-code-best-practices
view-count: 5
---
# Claude Code 配置协议

## 1. 核心逻辑
**优先级公式：$Active\_Config = Project (.claude/settings.json) \gg Global (~/.claude.json)$**

| 维度 | 项目级配置 (`.claude/settings.json`) | 全局级配置 (`~/.claude.json`) |
| :--- | :--- | :--- |
| **定位** | **团队/项目边界** | **个人习惯/隐私** |
| **共享** | 建议签入 Git（团队同步） | 严禁共享（本地私有） |
| **核心作用** | 规范构建流程、定义安全边界 | 常用全局工具、禁止编辑敏感文件 |
| **场景案例** | 允许 `npm run build` | 允许 `rg` (ripgrep) 搜索 |

## 2. 配置执行矩阵 (SOP)

### A. 项目级：安全与协作
*   **目标**：确保团队成员在受控环境下操作。
*   **关键配置项**：
    - **`Edit`**：限制文件模式（如 `["*.ts", "*.json"]`）。
    - **`Bash`**：
        - `allowedCommands`: 项目相关指令（`npm run *`, `git commit`）。
        - `blockedCommands`: 危险动作（`rm -rf *`, `sudo *`）。
    - **`MCP`**：启用特定工具（如 `puppeteer`）。

### B. 全局级：效率与防护
*   **目标**：保护个人隐私并加速日常工作。
*   **关键配置项**：
    - **隐私过滤**：在 `Edit.blockedFilePatterns` 中强制加入 `["*.env", "*.key", "*.pem"]`。
    - **通用工具**：全局允许搜索工具（`grep`, `cat`, `rg`）。
    - **环境预设**：自定义 Prompt 模板路径或日志级别。

## 3. 极简配置模板 (JSON)

### 项目级 (Minimal)
```json
{
  "allowedTools": {
    "Edit": { "allowedFilePatterns": ["src/**/*"] },
    "Bash": { "allowedCommands": ["npm run *"], "blockedCommands": ["rm -rf *"] }
  },
  "autoConfirmSmallChanges": true
}
```

### 全局级 (Minimal)
```json
{
  "allowedTools": {
    "Edit": { "blockedFilePatterns": ["*.env", "*.key"] },
    "Http": { "enabled": false }
  },
  "logLevel": "info"
}
```

## 4. 冲突处理协议
1. **完全覆盖**：若两处定义了同一个 `allowedCommands`，项目级配置直接取代全局级（不合并）。
2. **逻辑合并**：不同功能的配置项（如全局设 `logLevel`，项目设 `Edit`）会同时生效。

## 5. 瞬时执行清单 (Checklist)
- [ ] **隐私**：`~/.claude.json` 是否已排除 `.env` 文件？
- [ ] **合规**：`.claude/settings.json` 是否已进入 Git 仓库？
- [ ] **减熵**：是否存在重复的 `allowedCommands`？（项目级应优于全局级）
- [ ] **安全**：是否已设置 `blockedCommands` 过滤危险的 `rm` 或 `sudo` 操作？

---

**ROI 评估：**
- **压缩率**：~65% (剔除背景描述和冗长 JSON，保留核心差异与最小化模板)。
- **信息密度**：显著提升，引入优先级公式。
- **5秒测试**：通过“核心逻辑”矩阵，5秒内完成位置与作用域的快速定界。

**关联笔记：** [[道法术器]] | [[BMAD-METHOD：工程防御协议]] | [[生成力执行协议]]