---
view-count: 6
---
## 1. 核心逻辑：特性规格体系 (Feature Spec Hierarchy)

**系统目标：** 通过 `specs/[###-feature]/` 目录结构化，将模糊需求解构为可执行、可验证的原子工程路径。

**文档生命周期：**
- **$T_0$ (Research)**：可行性/风险边界扫描。
- **$T_1$ (Design)**：契约、模式与环境初始化。
- **$T_2$ (Implementation)**：并行执行与状态追踪。

## 2. 协议矩阵：文档架构 (Doc Architecture)

| 阶段 | 文件 (Operator) | 逻辑职能 (Function) | 核心输出 |
| :--- | :--- | :--- | :--- |
| **Stage 0** | `research.md` | 技术选型与风险建模 | Trade-offs & Risk Mitigation |
| **Stage 1** | `data-model.md` | 状态机与持久化定义 | Schema & ERD |
| **Stage 1** | `contracts/` | 边界协议对齐 | API Spec (OpenAPI) |
| **Stage 1** | `quickstart.md` | 环境一致性保证 | `.env` & Docker-compose |
| **Stage 2** | `tasks.md` | 任务原子化分解 | P0/P1/P2 Backlog |
| **Core** | `plan.md` | 全局调度与资源分配 | Timeline & Strategy |

## 3. 实战案例：用户头像管理 (User Avatar Management)

### **A. 决策矩阵 (Decision Matrix)**
- **Storage**: AWS S3 (Ecosystem fit).
- **Processing**: Sharp (High perf libvips).
- **Client**: React-Image-Crop (Standard UI).
- **Persistence**: PostgreSQL + JSONB (Variant metadata).

### **B. 数据协议 (Data Protocol)**
```sql
-- 核心：支持多尺寸 (Variants) 且通过 JSONB 提升扩展性
ALTER TABLE users ADD COLUMN current_avatar_id UUID;
CREATE TABLE avatars (
    id UUID PRIMARY KEY,
    user_id UUID REFERENCES users(id),
    variants JSONB NOT NULL, -- {"64x64": "url", "256x256": "url"}
    is_active BOOLEAN DEFAULT true
);
```

### **C. 安全与风险 (Safety & Risk)**
- **恶意注入**: 强制后端 MIME 校验 + 病毒扫描。
- **性能过载**: 异步 Worker 队列处理图片缩放，脱离请求响应主链路。
- **一致性**: S3 Upload 与 DB Update 的补偿机制。

## 4. 执行指南 (Execution Protocol)

- **原子性**: `tasks.md` 必须将任务颗粒度拆解至单人 1 天内。
- **P0 优先级**: 数据库迁移脚本、核心 API 端点、基础 UI 组件。
- **环境隔离**: 强制使用 MinIO 模拟 S3 进行本地闭环开发。

## 关联笔记
- [[文档化Planning]] (理解规格化设计的底层逻辑) [^1]
- [[原则驱动行动]] (KISS/YAGNI 在设计阶段的应用) [^2]
- [[如何利用意图理解结构化规范方法]] (需求解析至规格的转化) [^3]
- [[Go开发者实战指南]] (L3 层级解耦的架构实践) [^4]
