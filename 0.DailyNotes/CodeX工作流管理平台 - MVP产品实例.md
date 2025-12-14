---
view-count: 4
---
# CodeX工作流管理平台 - MVP产品实例

## 项目概述

基于CodeX生态系统的生产级MVP产品，实现任务批处理、优先级管理、分支策略和人机协作决策的完整工作流。

## 技术栈选择

```json
{
  "frontend": "React + TypeScript + Vite",
  "backend": "Node.js + Express + TypeScript",
  "database": "PostgreSQL + Prisma",
  "auth": "JWT + GitHub OAuth",
  "codeX": "OpenAI CodeX API",
  "ci": "GitHub Actions",
  "deployment": "Docker + Kubernetes"
}
```

## 项目结构

```
codex-workflow-platform/
├── client/                 # 前端应用
│   ├── src/
│   │   ├── components/     # UI组件
│   │   ├── hooks/          # 自定义Hook
│   │   ├── services/       # API服务
│   │   ├── types/          # TypeScript类型定义
│   │   └── utils/          # 工具函数
│   └── package.json
├── server/                 # 后端服务
│   ├── src/
│   │   ├── controllers/    # 控制器
│   │   ├── middleware/     # 中间件
│   │   ├── models/         # 数据模型
│   │   ├── routes/         # 路由
│   │   ├── services/       # 业务逻辑
│   │   ├── utils/          # 工具函数
│   │   └── config/         # 配置文件
│   ├── prisma/             # 数据库Schema
│   └── package.json
├── docker-compose.yml      # Docker配置
├── README.md
└── package.json            # 根目录配置
```

 