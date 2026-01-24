---
view-count: 6
tags:
  - Domain/Technology/Docker
  - Domain/Technology/DevOps
  - Type/Reference
  - Status/Done
---
# Dockerfile 部署流程：极简流水线指南

---

### 一、 核心本质
**Dockerfile 部署 = 资源隔离与构建流水线化**。
目标：通过 **多阶段构建 (Multi-stage Build)** 实现极小镜像体积、极速构建响应与极致生产安全。

### 二、 多阶段流水线矩阵 (The Pipeline)

| 阶段 | 别名 | 核心职责 | 关键产出 |
| :--- | :--- | :--- | :--- |
| **L1. 基础环境** | `base` | OS 选择 (Alpine) + 运行时 (Node.js) | 标准化运行底座 |
| **L2. 依赖安装** | `deps` | 系统兼容库 (`libc6-compat`) + `npm ci` | 完整 `node_modules` |
| **L3. 编译构建** | `builder` | 源码拷贝 + 静态资源打包 (`npm run build`) | `standalone` 产物 |
| **L4. 生产运行** | `runner` | 环境变量 + 权限限制 + 产出拷贝 | 最终生产镜像 |

### 三、 核心代码逻辑 (Next.js 最佳实践)

```dockerfile
# 1. 依赖锁层 (deps)
FROM node:18-alpine AS deps
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci  # 严格锁定版本，利用 Docker 层缓存

# 2. 构建产出层 (builder)
FROM node:18-alpine AS builder
WORKDIR /app
COPY --from=deps /app/node_modules ./node_modules
COPY . .
RUN npm run build  # 产出 standalone 文件夹

# 3. 极简运行层 (runner)
FROM node:18-alpine AS runner
WORKDIR /app
ENV NODE_ENV production

# 权限加固：创建非 root 用户
RUN addgroup --system --gid 1001 nodejs && adduser --system --uid 1001 nextjs
COPY --from=builder --chown=nextjs:nodejs /app/.next/standalone ./
USER nextjs
CMD ["node", "server.js"]
```

### 四、 核心优化原则 (Principles)

- **缓存优先**：先 COPY 配置文件再 COPY 源码。依赖未变时，`npm ci` 层将被永久缓存。
- **环境兼容**：Alpine 需手动添加 `libc6-compat` 补偿 glibc 缺失，防止二进制包报错。
- **产物隔离**：`runner` 阶段不包含源码、构建工具和原始 `node_modules`。仅通过 `standalone` 模式获取运行时必需文件。
- **最小权限**：生产环境严禁使用 `root` 用户运行。通过 `USER nextjs` 实现受限权限执行。
- **原子化构建**：每个阶段仅处理单一职责，利用 `--from=` 实现层间数据精细透传。

### 五、 关联笔记

- [[AIGC 能力飞轮学习路线图]] (云原生底座与资产自动化)
- [[Ripgrep 与现代 CLI 工具箱：极简指南]] (本地构建脚本检索)
- [[内容结构模式：产品化创作框架]] (部署文档的版本化管理)
- [[任务规划器-追求更有规划]] (构建流水线的逻辑拆解)