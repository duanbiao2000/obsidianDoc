---
aliases:
  - 20250226-0002
createdAt: 2025-02-26 13:16
updateAt: 2025-02-26 13:16
categories:
  - Mindset
tags:
  - Creative/Github
  - Tech/项目分析
---
# AI ContentCraft 项目分析
## 项目概述
AI ContentCraft 是一个多功能内容创作工具，集成了文本生成、语音合成和图像生成功能。该项目使用 Node.js 和 Express 构建后端，前端使用原生 HTML/JavaScript，并集成了多种 AI 服务。
## 主要功能
- **故事生成**：基于用户提供的主题自动生成短篇故事
- **脚本转换**：将故事转换为标准剧本格式
- **播客内容**：生成播客大纲和对话脚本
- **语音合成**：支持多种声音的文本转语音功能
- **图像生成**：为故事场景生成配图
- **双语支持**：支持中英文内容转换
- **批量处理**：支持批量生成和下载内容
## 技术栈
- **前端**：HTML/JavaScript
- **后端**：Node.js + Express
- **AI 服务**：
  - DeepSeek AI：文本生成
  - Kokoro TTS：语音合成
  - Replicate：图像生成
- **其他工具**：FFmpeg（音频处理）
## 项目结构
### 后端（server.js）
后端使用 Express 框架，提供以下主要 API 端点：
1. `/voices`：获取可用的语音列表
2. `/generate`：单段文本转语音
3. `/generate-and-merge`：多段文本转语音并合并
4. `/generate-story`：生成故事
5. `/generate-script`：转换脚本
6. `/generate-image`：生成图片
7. `/generate-all-images`：批量生成图片
8. `/download-images`：批量下载图片
9. `/translate-podcast`：播客脚本翻译
10. `/translate-story-script`：故事脚本翻译
### 前端（index.html）
前端界面分为四个主要页面：
1. **故事生成器**：生成故事、转换脚本、生成配图
2. **简单 TTS**：单段文本转语音
3. **多声音 TTS**：多段文本转语音并合并
4. **播客生成器**：生成播客内容、对话脚本
### 环境配置
项目使用 `.env` 文件存储 API 密钥：
- `DEEPSEEK_API_KEY`：DeepSeek AI 的 API 密钥
- `REPLICATE_API_TOKEN`：Replicate 的 API 令牌
### 工作流程
1. **故事生成**：
   - 用户输入故事主题
   - 系统使用 DeepSeek AI 生成故事
   - 可选择转换为脚本格式
   - 可为每个场景生成配图
2. **语音合成**：
   - 支持单段或多段文本转语音
   - 可选择不同的声音
   - 多段语音可自动合并
3. **图像生成**：
   - 自动为场景生成提示词
   - 使用 Replicate API 生成图片
   - 支持批量下载和预览
### 部署要求
- Node.js 16+
- FFmpeg 安装
- AI 服务的 API 密钥
- 稳定的网络连接
### 注意事项
- 需要有效的 API 密钥才能使用 AI 服务
- 音频合并功能需要正确配置 FFmpeg
- 注意 API 调用限制和费用
这个项目展示了如何集成多种 AI 服务来创建一个功能丰富的内容创作工具，特别适合需要快速生成多媒体内容的创作者使用。
##  Mermaid 流程图
### 整体系统架构
```mermaid
flowchart TD
    A[用户界面 - 前端] --> B[Express 服务器 - 后端]
    B --> C[DeepSeek AI\n文本生成]
    B --> D[Kokoro TTS\n语音合成]
    B --> E[Replicate\n图像生成]
    C --> B
    D --> B
    E --> B
    B --> A
```
### 故事生成流程
```mermaid
flowchart TD
    A[用户输入故事主题] --> B[调用 DeepSeek AI 生成故事]
    B --> C[显示生成的故事]
    C --> D{用户选择}
    D -->|转换为脚本| E[调用 DeepSeek AI\n转换为JSON格式脚本]
    E --> F[显示脚本内容]
    D -->|生成场景图片| G[为每个场景生成提示词]
    G --> H[调用 Replicate API\n生成图片]
    H --> I[显示生成的图片]
```
### 播客生成流程
```mermaid
flowchart TD
    A[用户输入播客主题] --> B[调用 DeepSeek AI 生成播客内容]
    B --> C[显示生成的播客内容]
    C --> D[转换为对话脚本]
    D --> E[选择声音配音]
    E --> F[调用 Kokoro TTS\n生成语音]
    F --> G[合并多段语音\n使用 FFmpeg]
    G --> H[提供音频预览和下载]
```
### 语音合成流程
```mermaid
flowchart TD
    A{语音合成类型} -->|单段文本转语音| B[输入文本]
    B --> C[选择声音]
    C --> D[调用 Kokoro TTS\n生成语音]
    D --> E[提供音频预览和下载]
    A -->|多段文本转语音| F[输入多段文本]
    F --> G[为每段选择声音]
    G --> H[调用 Kokoro TTS\n生成多段语音]
    H --> I[使用 FFmpeg 合并\n多段语音]
    I --> J[提供合并后的音频\n预览和下载]
```
### 图像生成流程
```mermaid
flowchart TD
    A{图像生成类型} -->|单张图片生成| B[输入图像提示词]
    B --> C[调用 Replicate API\n生成图片]
    C --> D[显示生成的图片]
    A -->|批量图片生成| E[从脚本场景自动\n生成多个提示词]
    E --> F[批量调用 Replicate API\n生成多张图片]
    F --> G[显示所有生成的图片]
    G --> H[提供批量下载选项]
```
### 数据流向
```mermaid
flowchart LR
    A[用户输入\n- 故事主题\n- 播客主题\n- 文本内容\n- 提示词] --> B[AI 处理\n- 文本生成\n- 语音合成\n- 图像生成]
    B --> C[内容输出\n- 故事文本\n- 脚本格式\n- 语音文件\n- 图片文件]
```
### API 调用流程
```mermaid
flowchart TD
    A[前端请求] --> B[Express 路由处理]
    B --> C{API 类型}
    C -->|DeepSeek API| D[构建提示词]
    D --> E[发送 API 请求]
    E --> F[处理 AI 响应]
    C -->|Kokoro TTS API| G[准备文本和声音参数]
    G --> H[发送 API 请求]
    H --> I[处理音频响应]
    C -->|Replicate API| J[准备图像提示词]
    J --> K[发送 API 请求]
    K --> L[处理图像响应]
    F --> M[返回结果给前端]
    I --> M
    L --> M
```
