---
view-count: 8
---
# [[Go开发者实战指南]]

## 1. 核心逻辑：Go 工程体系 (Go Engineering Hierarchy)

**能力递进模型：**
- **L1 标准库 (Standard Lib)**：核心内功。掌握 `context` (生命周期), `sync` (内存安全), `net/http` (协议栈)。
- **L2 生态库 (Ecosystem)**：生产兵器。集成 `Gin` (路由), `GORM` (持久化), `Zap/Viper` (观测/配置)。
- **L3 工程化 (Production)**：系统构建。实现 JWT 鉴权、单元测试、层级架构 (Internal/Repo/Service)。

## 2. 核心组件矩阵 (Core Component Matrix)

| 组件 | 核心职能 | 执行协议 (Best Practice) |
| :--- | :--- | :--- |
| **`context`** | 协程级联取消/超时控制 | `ctx` 必为首参数；必须调用 `defer cancel()`。 |
| **`sync`** | 并发原语/共享资源保护 | 计数优先使用 `atomic`；`Mutex` 临界区最小化。 |
| **`Gin`** | 高性能 REST API 路由 | 使用 `Group` 分组；中间件处理 Cross-cutting concerns。 |
| **`GORM`** | 对象关系映射/数据库交互 | 生产环境禁用 `AutoMigrate`；复杂 SQL 优先使用 `Raw`。 |
| **`Zap/Viper`** | 结构化日志/配置管理 | 单例初始化 + 依赖注入；配置优先级：`Env > File > Default`。 |

## 3. 执行指南 (Execution)

### **并发控制 (Concurrency)**
- **泄露预防**：任何启动的 Goroutine 必须有明确的退出机制（Context 或 Channel）。
- **性能优化**：`sync.WaitGroup` 协调并行任务，避免空转。

### **数据持久化 (Persistence)**
- **原子性**：业务逻辑涉及多表操作时，强制使用 `db.Transaction` 闭环。
- **连接管理**：显式配置 `SetMaxOpenConns` 以匹配基础设施规格。

### **架构模式 (Architecture)**
- **层级解耦**：
  - `handler/`：HTTP 协议解析。
  - `service/`：纯业务逻辑（不含 SQL/Gin 上下文）。
  - `repository/`：存储细节。

## 4. 关键参数 (Parameters)

- **超时容忍度**：HTTP Handler 默认设置 `context.WithTimeout` (建议 3s-10s)。
- **日志密度**：生产环境使用 `zap.NewProduction()` 以确保 JSON 格式及高性能。

## 关联笔记
- [[2025-12-30-You 2.0 Stop Spiraling!]] (用于处理开发压力与负面螺旋)
