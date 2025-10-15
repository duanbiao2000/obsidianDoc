# 🌐 **MCP (Model Context Protocol) 开发者指南：Claude Desktop AI 代理集成指南**  
> 💡 **核心概念**:  
> **"MCP 是 AI 模型与外部服务标准化通信的协议。无需编写 API 代码，即可在 Claude Desktop 中连接 Slack、Notion、网页爬虫等多种服务。"**

---

## 🚀 1. MCP 基本概念与架构

### 🔍 MCP 是什么？
- **MCP (Model Context Protocol)**：AI 模型与外部服务交互的标准化协议
- **架构**：`主机(Host) → 客户端(Client) → 服务器(Server) → 资源(Resources)`
  - **主机**：Claude Desktop、VS Code、Cursor 等 AI 运行环境
  - **服务器**：连接特定服务（Slack、Notion 等）的微服务
  - **资源**：实际服务数据（消息、文档、频道等）

### ✅ MCP 的优势
| 传统方式 | MCP 方式 |
|-----------|----------|
| 每个服务需单独编写 API 代码 | 单一协议标准化连接 |
| 服务变更时需修改代码 | 仅需更换服务器 |
| 认证/权限设置复杂 | 仅需服务器设置即可轻松连接 |
| 跨平台兼容性问题 | 无论主机环境，均以相同方式连接 |

> 💡 **开发者视角**：MCP 是 **"AI 的插件系统"**，简化了复杂的 API 集成工作。

---

## 🛠️ 2. 系统准备与安装（5分钟完成）

### ✅ 必需工具
| 工具 | 安装方法 | 验证命令 |
|------|-----------|------------|
| **Claude Desktop** | [claude.ai/download](https://claude.ai/download) | 应用运行确认 |
| **VS Code** | [code.visualstudio.com](https://code.visualstudio.com) | `code --version` |
| **Node.js (v18+)** | [nodejs.org](https://nodejs.org) | `node -v` |
| **Git** | [git-scm.com](https://git-scm.com) | `git --version` |

### 📌 安装步骤
1. **Claude Desktop 安装**  
   - 下载对应操作系统的版本 → 运行

2. **VS Code 安装**  
   - 优化 JSON 文件编辑的编辑器

3. **Node.js 安装**  
   - MCP 服务器运行必需的运行时

> ⚠️ **注意**：MCP 服务器 **仅在 Claude Desktop 的开发者模式下运行**

---

## 🌐 3. MCP 服务器安装与设置（实战指南）

### 🔑 MCP 配置文件结构
```json
{
  "mcp_servers": [
    {
      "name": "slack",
      "command": "node /path/to/slack-server/index.js",
      "env": {
        "SLACK_BOT_TOKEN": "xoxb-...",
        "SLACK_TEAM_ID": "T..."
      }
    },
    {
      "name": "firecrawl",
      "command": "node /path/to/firecrawl-server/index.js",
      "env": {
        "FIRECRAWL_API_KEY": "fc-..."
      }
    }
  ]
}
```

#### 📌 配置文件位置
- **Windows**: `%APPDATA%\Claude\config.json`
- **Mac**: `~/Library/Application Support/Claude/config.json`
- **Linux**: `~/.config/Claude/config.json`

---

## 🛠️ 4. 主要服务 MCP 服务器安装指南

### ✅ 4.1. Slack MCP 服务器连接
#### 📌 分步设置
1. **Slack 应用创建**  
   - [Slack API 页面](https://api.slack.com/apps) → "Create New App" → "From scratch"  
   - App 名称：`Claude-MCP` → 选择工作区

2. **机器人权限设置**  
   - "OAuth & Permissions" → "Bot Token Scopes" 添加：  
     ```text
     chat:write
     channels:read
     channels:history
     groups:read
     im:read
     ```
   - "Install to Workspace" → 授权

3. **令牌及工作区 ID 确认**  
   - "OAuth & Permissions" → "Bot User OAuth Token" 复制  
   - Slack 频道 URL 中提取以 `T...` 开头的工作区 ID（例如：`https://slack.com/archives/C12345678` → `T12345678`）

4. **config.json 设置**  
   ```json
   {
     "mcp_servers": [
       {
         "name": "slack",
         "command": "npx @claude-ai/mcp-slack@latest",
         "env": {
           "SLACK_BOT_TOKEN": "xoxb-...",
           "SLACK_TEAM_ID": "T..."
         }
       }
     ]
   }
   ```

> ✅ **验证方法**：  
> - Claude Desktop → 设置 → 开发者选项 → "MCP 服务器连接" → 确认 `slack` 服务器显示

---

### ✅ 4.2. FireCrawl MCP 服务器（网页爬虫）
#### 📌 分步设置
1. **FireCrawl 账户创建**  
   - [firecrawl.dev](https://firecrawl.dev) → "Sign Up" → 获取 API 密钥

2. **config.json 设置**  
   ```json
   {
     "mcp_servers": [
       {
         "name": "firecrawl",
         "command": "npx @claude-ai/mcp-firecrawl@latest",
         "env": {
           "FIRECRAWL_API_KEY": "fc-..."
         }
       }
     ]
   }
   ```

> 💡 **特点**：  
> - `https://firecrawl.dev` → "API" 选项卡中用 `curl` 命令测试  
> - 网页爬取时使用 `?mode=extract` 参数提取结构化数据

---

### ✅ 4.3. Notion MCP 服务器连接
#### 📌 分步设置
1. **Notion 集成创建**  
   - [Notion 开发者页面](https://developers.notion.com) → "New Integration"  
   - 名称：`Claude-MCP` → 选择 "Internal Integration"  
   - 权限：`Content` → `Read content`, `Insert content`, `Update content`  
   - "Save" → 复制密钥

2. **Notion 页面连接**  
   - 需连接的 Notion 页面 → 右上角 `•••` → "Connect to AI" → 选择 `Claude-MCP`

3. **config.json 设置**  
   ```json
   {
     "mcp_servers": [
       {
         "name": "notion",
         "command": "npx @claude-ai/mcp-notion@latest",
         "env": {
           "NOTION_INTEGRATION_TOKEN": "secret_..."
         }
       }
     ]
   }
   ```

> ⚠️ **注意**：  
> - Notion 页面 URL 中的 `?v=...` 部分 **不使用**  
> - `NOTION_INTEGRATION_TOKEN` 为 `secret_...` 格式的令牌

---

### ✅ 4.4. Perplexity MCP 服务器（浏览器自动化）
#### 📌 分步设置
1. **Perplexity 服务器安装**  
   ```bash
   npm install -g @claude-ai/mcp-perplexity
   ```

2. **config.json 设置**  
   ```json
   {
     "mcp_servers": [
       {
         "name": "perplexity",
         "command": "perplexity-mcp",
         "env": {}
       }
     ]
   }
   ```

> 💡 **特点**：  
> - 提供浏览器自动化功能（需 Chrome/Chromium）  
> - 使用 `perplexity-mcp --help` 查看用法

---

## 💡 5. 实战案例（开发者实用技巧）

### ✅ 案例 1：TechCrunch AI 新闻爬取 → Slack 发送
```text
"从 TechCrunch 爬取 5 条最新 AI 新闻并发送到 Slack 频道 #ai-news。  
格式使用 Slack Block Kit 兼容 JSON，每条新闻包含标题、链接、简短描述"
```

#### 📌 执行结果
- FireCrawl 服务器爬取 TechCrunch 页面
- Notion 服务器存储数据
- Slack 服务器向频道发送格式化消息

> ✅ **开发者提示**：  
> - 使用 `?mode=extract` 参数提取结构化数据  
> - Slack Block Kit 格式参考 [Slack API 文档](https://api.slack.com/block-kit)

---

### ✅ 案例 2：YouTube 频道分析 → Notion 数据库更新
```text
"收集我的 YouTube 频道 'AI-Sync' 最近 10 个视频数据，更新到 Notion 数据库 'YouTube-Analysis'。  
所需字段：视频标题、观看次数、上传日期、平均观看时长、标签"
```

#### 📌 执行结果
- Perplexity 服务器自动化 YouTube 页面
- 数据解析 → 在 Notion 数据库中创建页面
- 生成自动化报告

> ✅ **开发者提示**：  
> - YouTube URL 使用 `?feature=share` 格式而非 `?v=...`  
> - Notion 数据库需预先定义字段（标题、观看次数等）

---

## ⚠️ 6. 主要问题解决与故障排除

### ❌ 问题：MCP 服务器无法运行
| 现象 | 解决方法 |
|------|-----------|
| "服务器连接失败" | 1. 检查 config.json 文件路径<br>2. 确认 Node.js 版本 v18+<br>3. 测试服务器命令（`npx @claude-ai/mcp-slack@latest`） |
| "API 密钥错误" | 1. 重新生成 Slack/Notion 令牌<br>2. 确认令牌所需权限<br>3. 直接在 `env` 部分设置，而非使用 `.env` 文件 |
| "浏览器错误"（Perplexity） | 1. 安装 Chrome/Chromium<br>2. 添加 `--no-sandbox` 选项<br>3. 使用 `perplexity-mcp --headless=false` 调试 |

### 🛠️ 开发者工具
```bash
# MCP 服务器日志查看
npx @claude-ai/mcp-slack@latest --debug

# 服务器测试
curl -X POST http://localhost:3000/test -d '{"query": "test"}'
```

> 💡 **推荐工具**：  
> - **Postman**：MCP 服务器 API 测试  
> - **VS Code JSON Linter**：config.json 语法验证  
> - **Node.js Debugger**：服务器调试

---

## 🌈 7. MCP 开发者技巧（高级应用）

### ✅ 7.1. 自定义 MCP 服务器制作
```bash
# 基础服务器模板创建
npx create-mcp-server@latest my-custom-server
```

**服务器结构**：
```js
// index.js
module.exports = {
  name: "my-custom-server",
  description: "我的 MCP 服务器",
  commands: {
    "get-data": {
      handler: async (params) => {
        return { data: "自定义响应" };
      }
    }
  }
};
```

> 💡 **优势**：  
> - 为特定业务逻辑定制服务器  
> - 直接在 Claude 中通过 `get-data` 命令调用

### ✅ 7.2. MCP 服务器打包
```bash
# npm 包发布
npm init
npm pack
npm publish
```

**使用方法**：  
```json
{
  "mcp_servers": [
    {
      "name": "my-custom-server",
      "command": "npm install -g my-custom-server && my-custom-server"
    }
  ]
}
```

---

## 🚀 8. MCP 开发者生态系统

### 🔗 有用资源
| 资源 | 链接 | 说明 |
|--------|------|------|
| **官方 MCP 服务器列表** | [github.com/claude-ai/mcp-servers](https://github.com/claude-ai/mcp-servers) | Claude 官方提供的服务器 |
| **社区 MCP 服务器** | [github.com/awesome-mcp-servers](https://github.com/awesome-mcp-servers) | 社区贡献的服务器 |
| **MCP 开发指南** | [claude.ai/mcp-dev](https://claude.ai/mcp-dev) | 服务器制作方法 |
| **MCP 模板** | [github.com/claude-ai/mcp-template](https://github.com/claude-ai/mcp-template) | 基础服务器模板 |

> 💡 **开发者策略**：  
> - **项目定制服务器制作** → 自动化重复工作  
> - **公开服务器包发布** → 贡献社区  
> - **MCP + GitHub Actions** → CI/CD 流水线自动化

---

## ✅ 最终检查事项
1. **Claude Desktop** 运行 → 设置 → 开发者选项 → 修改 config.json  
2. **MCP 服务器** 安装及测试（`npx @claude-ai/mcp-slack@latest`）  
3. **config.json** 添加服务器设置 → 重启 Claude  
4. **使用提示示例** 测试功能  
5. **查看日志** → 出现问题时调试  

> 💬 **开发者反馈**：  
> *"引入 MCP 后，Slack/Notion 集成工作时间减少了 80%。  
> 无需编写复杂 API 代码，AI 可直接操作服务，生产力大幅提升。"*  
> —— 谷歌 AI 工程师

---

## 🌟 9. 实战练习题
**问题**：  
> "爬取 GitHub 仓库 'claude-ai/mcp-servers' 的最新 5 个 issue，更新到 Notion 数据库 'GitHub-Issues'，并发送通知到 Slack 频道 #github。"

**解决步骤**：  
1. **GitHub MCP 服务器** 安装（使用社区服务器）  
2. **config.json** 设置 GitHub API 令牌  
3. **提示编写**：  
   ```text
   "爬取 GitHub 仓库 claude-ai/mcp-servers 的最新 5 个 issue，  
   更新到 Notion 数据库 'GitHub-Issues'，  
   发送通知到 Slack 频道 #github。  
   字段：issue 标题、状态、作者、创建日期、URL"
   ```

> ✅ **完成条件**：  
> - Notion 数据库中保存 issue 信息  
> - Slack 频道中发送格式化消息  
> - 无错误正常运行

---

## 💡 核心结论
> **"MCP 是 AI 代理的'插件系统'。  
> 无需编写复杂 API 集成代码，  
> 即可在 Claude Desktop 中连接多种服务。"**

- **开发者所需**：  
  - MCP 服务器安装（5分钟完成）  
  - config.json 设置（JSON 文件编辑）  
  - 通过提示操作服务（自然语言命令）  

- **未来展望**：  
> *"MCP 将成为 AI 开发的新标准。  
> 未来所有 AI 工具都支持 MCP，  
> 开发者将无需处理复杂 API 集成，而是专注于创意 AI 应用设计。"*