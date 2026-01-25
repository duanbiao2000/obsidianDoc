---
view-count: 4
related:
  - '[[200组开发选题]]'
  - '[[20250624-技能点+3]]'
  - '[[编程范式]]'
  - '[[微服务生态系统]]'
  - '[[领域驱动设计]]'
  - '[[2025-12-06-企业应用架构模式]]'
  - '[[系统设计：规模化与权衡指南]]'
  - '[[前端开发原则]]'
tags:
  - microservices-architecture
  - ddd-implementation
  - system-design
  - architecture
  - Type/Reference
  - Domain/Technology
---
# 程序员圈 LFSP Top 100

## 架构设计 (1-15)
1. **微服务** - Microservices
2. **单体架构** - Monolithic
3. **SOA** - Service-Oriented Architecture
4. **DDD** - Domain-Driven Design
5. **CQRS** - Command Query Responsibility Segregation
6. **Event Sourcing** - 事件溯源
7. **BFF** - Backend For Frontend
8. **Service Mesh** - 服务网格
9. **Sidecar** - 边车模式
10. **API Gateway** - API 网关
11. **负载均衡** - Load Balancing
12. **服务发现** - Service Discovery
13. **熔断器** - Circuit Breaker
14. **降级** - Degradation
15. **限流** - Rate Limiting

## 并发/异步 (16-30)
16. **异步非阻塞** - Async Non-blocking
17. **IO 多路复用** - IO Multiplexing
18. **协程** - Coroutine
19. **线程池** - Thread Pool
20. **死锁** - Deadlock
21. **竞态条件** - Race Condition
22. **CAS** - Compare And Swap
23. **自旋锁** - Spinlock
24. **互斥锁** - Mutex
25. **读写锁** - RWLock
26. **信号量** - Semaphore
27. **Actor 模型** - Actor Model
28. **事件循环** - Event Loop
29. **背压** - Backpressure
30. **响应式编程** - Reactive Programming

## 数据库 (31-50)
31. **ACID** - 原子性/一致性/隔离性/持久性
32. **BASE** - 基本可用/软状态/最终一致
33. **CAP 定理** - Consistency/Availability/Partition tolerance
34. **分库分表** - Sharding
35. **主从复制** - Master-Slave Replication
36. **读写分离** - Read-Write Splitting
37. **ORM** - Object-Relational Mapping
38. **事务隔离级别** - Transaction Isolation Level
39. **脏读** - Dirty Read
40. **幻读** - Phantom Read
41. **MVCC** - Multi-Version Concurrency Control
42. **索引** - Index
43. **B+ 树** - B+ Tree
44. **慢查询** - Slow Query
45. **N+1 问题** - N+1 Query Problem
46. **连接池** - Connection Pool
47. **NoSQL** - Not Only SQL
48. **文档数据库** - Document Database
49. **列式存储** - Columnar Storage
50. **时序数据库** - Time-Series Database

## 性能优化 (51-65)
51. **CDN** - Content Delivery Network
52. **缓存穿透** - Cache Penetration
53. **缓存雪崩** - Cache Avalanche
54. **缓存击穿** - Cache Breakdown
55. **预热** - Warm-up
56. **懒加载** - Lazy Loading
57. **防抖** - Debounce
58. **节流** - Throttle
59. **JIT** - Just-In-Time Compilation
60. **AOT** - Ahead-Of-Time Compilation
61. **GC** - Garbage Collection
62. **内存泄漏** - Memory Leak
63. **CPU 密集型** - CPU-bound
64. **IO 密集型** - IO-bound
65. **火焰图** - Flame Graph

## 开发模式 (66-80)
66. **TDD** - Test-Driven Development
67. **BDD** - Behavior-Driven Development
68. **CI/CD** - Continuous Integration/Deployment
69. **DevOps** - Development + Operations
70. **GitOps** - Git-based Operations
71. **IaC** - Infrastructure as Code
72. **蓝绿部署** - Blue-Green Deployment
73. **金丝雀发布** - Canary Release
74. **灰度发布** - Gray Release
75. **AB 测试** - A/B Testing
76. **特性开关** - Feature Toggle
77. **技术债** - Technical Debt
78. **重构** - Refactoring
79. **代码异味** - Code Smell
80. **结对编程** - Pair Programming

## 分布式系统 (81-95)
81. **分布式锁** - Distributed Lock
82. **分布式事务** - Distributed Transaction
83. **2PC** - Two-Phase Commit
84. **3PC** - Three-Phase Commit
85. **Paxos** - Paxos 算法
86. **Raft** - Raft 算法
87. **一致性哈希** - Consistent Hashing
88. **幂等性** - Idempotency
89. **最终一致性** - Eventual Consistency
90. **分布式追踪** - Distributed Tracing
91. **链路追踪** - Trace
92. **服务降级** - Service Degradation
93. **雪崩效应** - Avalanche Effect
94. **脑裂** - Split-Brain
95. **Quorum** - 法定人数机制

## 安全/其他 (96-100)
96. **XSS** - Cross-Site Scripting
97. **CSRF** - Cross-Site Request Forgery
98. **SQL 注入** - SQL Injection
99. **零信任** - Zero Trust
100. **JWT** - JSON Web Token

---

✅ **使用场景**：技术面试、Code Review、架构讨论、文档撰写

### 程序员圈常见 LFSP Top 100（术语 + 极简释义）

> 说明：偏抽象、高密度的“圈内黑话”，按主题分组，方便扫读。

---

#### 一、编程范式 & 抽象（1–10）

1. **OOP（面向对象编程）**：用对象、类、继承、封装来组织代码。  
2. **FP（函数式编程）**：强调纯函数、不可变数据和组合。  
3. **Imperative（命令式）**：一步步告诉计算机“怎么做”。  
4. **Declarative（声明式）**：只描述“要什么”，不写具体步骤。  
5. **Abstraction（抽象）**：隐藏细节，只暴露必要接口。  
6. **Encapsulation（封装）**：数据 + 行为打包在一起，对外隔离内部实现。  
7. **Polymorphism（多态）**：同一接口，不同实现。  
8. **Side Effect（副作用）**：函数之外状态被修改。  
9. **Immutability（不可变性）**：一旦创建就不能修改的值/结构。  
10. **DSL（领域特定语言）**：为特定领域定制的迷你语言。

---

#### 二、设计原则 & 模式（11–20）

11. **SOLID**：五大面向对象设计原则集合。  
12. **KISS**：Keep It Simple, Stupid，保持简单。  
13. **DRY**：Don’t Repeat Yourself，避免重复。  
14. **YAGNI**：You Aren’t Gonna Need It，不做当前用不上的设计。  
15. **IoC / DI**：控制反转 / 依赖注入，用容器管理依赖。  
16. **MVC**：Model–View–Controller 三层分离。  
17. **MVVM**：Model–View–ViewModel，常见于前端。  
18. **Layered Architecture（分层架构）**：表示层 / 业务层 / 数据层。  
19. **Hexagonal Architecture**：核心与外设解耦的“六边形架构”。  
20. **CQRS**：命令与查询职责分离。

---

#### 三、架构 & 系统风格（21–30）

21. **Monolith（单体应用）**：所有功能打包在一个应用里。  
22. **Microservices（微服务）**：按业务拆成多个小服务。  
23. **Service Mesh**：用基础设施层处理服务间通信。  
24. **API Gateway**：所有外部请求的统一入口。  
25. **Orchestration（编排）**：统一调度容器/服务的运行。  
26. **Event-driven（事件驱动）**：用事件触发业务流程。  
27. **Saga**：分布式事务的长事务补偿模式。  
28. **Circuit Breaker（熔断器）**：下游挂了就自动“跳闸”。  
29. **Backpressure（背压）**：下游压力大时反向限流。  
30. **Observability（可观测性）**：日志 + 指标 + Trace 构成的可观测体系。

---

#### 四、数据一致性 & 存储（31–40）

31. **ACID**：事务的原子性、一致性、隔离性、持久性。  
32. **BASE**：Basically Available, Soft state, Eventual consistency。  
33. **CAP**：一致性 / 可用性 / 分区容错不可能三角。  
34. **Strong Consistency（强一致性）**：读写总是最新。  
35. **Eventual Consistency（最终一致性）**：一段时间后才一致。  
36. **Isolation Level（隔离级别）**：控制事务间相互影响程度。  
37. **Idempotency / 幂等**：同一操作重复多次效果相同。  
38. **Sharding（分片）**：按规则拆成多库/多表。  
39. **Index（索引）**：加速查询的数据结构。  
40. **OLTP / OLAP**：联机事务处理 / 联机分析处理。

---

#### 五、网络 & 接口（41–50）

41. **API**：对外暴露的功能接口。  
42. **REST**：基于资源和 HTTP 动词的接口风格。  
43. **RESTful**：更规范化的 REST 实践。  
44. **RPC**：远程过程调用，像本地函数那样调远程服务。  
45. **gRPC**：基于 HTTP/2 和 Protobuf 的高性能 RPC 框架。  
46. **Webhook**：由服务器主动回调的 HTTP 请求。  
47. **WebSocket**：双向持久连接协议。  
48. **Rate Limiting（限流）**：限制请求频率。  
49. **Throttling（节流）**：按速率平滑请求。  
50. **Contract-first（契约优先）**：先定义接口契约，再写实现。

---

#### 六、工程实践 & 流程（51–60）

51. **Refactor（重构）**：不改行为，只改内部结构。  
52. **Tech Debt（技术债）**：为了快而留下的隐性问题。  
53. **Code Smell（代码坏味道）**：看起来就可能有问题的代码特征。  
54. **Code Review**：提交前由他人审查代码。  
55. **Pair Programming**：两个人一台电脑协作写代码。  
56. **CI/CD**：持续集成 / 持续交付/部署。  
57. **Trunk-based Development**：所有人围绕主干分支快速集成。  
58. **TDD**：测试驱动开发，先写测试再写实现。  
59. **BDD**：行为驱动开发，从业务行为出发写测试。  
60. **Blue-Green Deployment（蓝绿发布）**：两套环境无缝切流。

---

#### 七、性能 & 并发（61–70）

61. **Latency（延迟）**：单次请求耗时。  
62. **Throughput（吞吐量）**：单位时间处理的请求数。  
63. **Bottleneck（瓶颈）**：限制整体性能的关键点。  
64. **Profiling**：分析性能热点。  
65. **Concurrency（并发）**：逻辑上“同时”处理多任务。  
66. **Parallelism（并行）**：物理上在多个核上同时运行。  
67. **Race Condition（竞态条件）**：结果依赖执行先后顺序。  
68. **Deadlock（死锁）**：一组线程互相等待，永远卡住。  
69. **Lock-free（无锁）**：不用互斥锁完成并发控制。  
70. **Backoff（退避）**：失败或冲突后延迟重试。

---

#### 八、运行时 & 内存（71–80）

71. **GC（垃圾回收）**：自动回收不再使用的内存。  
72. **Heap（堆）**：动态分配内存区域。  
73. **Stack（栈）**：函数调用栈帧所在区域。  
74. **Pointer / Reference（指针/引用）**：指向内存地址的“指针”。  
75. **Copy-on-write**：写时复制策略。  
76. **Memory Leak（内存泄漏）**：不再用的内存没被释放。  
77. **Cache Hit / Miss**：缓存命中 / 未命中。  
78. **Warm-up（预热）**：让系统先跑一段时间以达稳定状态。  
79. **Hot Path（热点路径）**：最常走、最该优化的执行路径。  
80. **JIT（即时编译）**：运行时把字节码编译成本地码。

---

#### 九、前端 & 客户端词汇（81–90）

81. **SPA（单页应用）**：一个页面内前端路由切换。  
82. **CSR / SSR**：客户端渲染 / 服务端渲染。  
83. **Virtual DOM**：用虚拟节点描述 UI，再计算差异更新。  
84. **Responsive Design（响应式设计）**：自适应不同设备尺寸。  
85. **Componentization（组件化）**：UI 拆成可复用组件。  
86. **Tree Shaking**：构建时移除未使用代码。  
87. **Bundling（打包）**：把多文件打成一个或少数包。  
88. **Polyfill**：用代码补齐旧环境不支持的新特性。  
89. **Debounce（防抖）**：只在频繁操作停止后触发一次。  
90. **Throttle（节流）**：频繁操作中按固定间隔触发。

---

#### 十、产品 & 团队语境（91–100）

91. **MVP（最小可行产品）**：用最小功能验证想法。  
92. **PoC（概念验证）**：先证明“理论上可行”。  
93. **Dogfooding**：自己团队先用自己的产品。  
94. **Stakeholder（干系人）**：对项目有利益关系的人。  
95. **Single Source of Truth（单一可信源）**：唯一权威数据来源。  
96. **Backlog**：等待实施的需求列表。  
97. **Sprint**：敏捷中的短迭代周期。  
98. **Regression（回归问题）**：改动导致旧功能坏掉。  
99. **Breaking Change**：不向后兼容的改动。  
100. **Backward Compatibility（向后兼容）**：新版本仍能兼容旧用法。