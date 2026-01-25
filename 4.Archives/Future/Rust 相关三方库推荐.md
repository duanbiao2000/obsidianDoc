---
view-count: 3
update: 2026-01-09 13:51
related:
  - "[[Rust 异步与并发系统学习路径]]"
  - "[[Rust生产级综合开发技能学习系统提示词模板]]"
  - "[[2025-12-05-Go与Rust的权衡]]"
  - "[[Rust疑难知识点]]"
  - "[[2025-12-10-高质量开源项目的特征]]"

tags: ["Domain/Technology/Rust", "Type/Reference"]

---
# 🦀 Rust 第三方库速查 Cheatsheet（工程实战向）

---

## 一、Rust 高赞 & 高价值三方库（非玩具）

### 🧮 数值 / 科学计算

**faer**

- 定位：高性能线性代数
- 特点：
  - 纯 Rust（无 C / BLAS 依赖）
  - 多线程优化
  - 性能接近 LAPACK
- 适用场景：科学计算 / 图形 / 仿真 / ML infra

---

### 🧠 解析 & 编译器工具链

**nom-supreme**

- 定位：`nom` 的 UX 增强层
- 解决问题：
  - 错误信息难看
  - 组合子样板代码多
- 适合：DSL / 配置解析 / 编译器前端

**arena**

- 定位：Arena Allocator（批量内存管理）
- 优势：
  - 快
  - 无碎片
  - 生命周期统一释放
- 常见用途：AST / IR / 图结构

---

### 🖥 CLI & 开发者工具

**reedline**

- 定位：高级 CLI 输入组件
- 能力：
  - 自动补全
  - 历史
  - 语法高亮
- 背景：Nushell 官方库

**addr2line**

- 定位：地址 → 源码映射
- 用途：
  - backtrace
  - crash analysis
- 属于：调试基础设施核心组件

---

## 二、Rust 生态“事实标准”库（避坑必知）

### ⚡ 异步 & 并发

**tokio**

- Rust 异步事实标准
- 提供：
  - runtime
  - async IO
  - timer / task scheduler

**async-std**

- API 风格 ≈ std
- 易学但生态弱于 tokio
- 适合：学习 / 小项目

---

### 🌐 网络 & HTTP

**reqwest**

- 高层 HTTP Client
- 特点：
  - 易用
  - sync / async
- 适合：业务代码

**hyper**

- 底层 HTTP 协议实现
- 特点：
  - 高性能
  - 高复杂度
- 适合：框架 / infra

> 经验法则：\
> **99% 情况用 reqwest，1% 才需要 hyper**

---

### 📦 序列化 / 数据模型

**serde**

- Rust 生态“隐形标准库”
- 核心价值：
  - 零成本抽象
  - 格式无关

**rustc_hash**

- 提供 FxHash
- 优势：
  - 小数据
  - 整数 key
  - 比 std::HashMap 快
- 常用于：编译器 / cache / hot path

---

### 🧰 CLI 工具

**clap**

- CLI 参数解析事实标准
- 能力：
  - 子命令
  - help 自动生成
  - shell 补全

---

### 🗄 数据库

**sqlx**

- 类型安全 SQL client
- 核心优势：
  - 编译期 SQL 校验
- 适合：偏 SQL 控制流团队

**diesel**

- 完整 ORM
- 特点：
  - 强类型 DSL
  - 迁移支持好
- 代价：抽象重、学习曲线高

---

## 四、工程级选型经验（重要）

- CLI 工具：`clap + reedline`

- 高性能服务：

  - async：`tokio`

  - HTTP：`reqwest`

- 编译器 / 解析器：

  - `nom-supreme + arena + rustc_hash`

- 数据持久化：

  - SQL-first → `sqlx`

  - Domain-heavy → `diesel`

- 数据交换层：

  - 永远优先 `serde`

[[IC 职级演进]]
