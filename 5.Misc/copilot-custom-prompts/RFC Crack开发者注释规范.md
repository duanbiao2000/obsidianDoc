---
copilot-command-context-menu-enabled: false
copilot-command-slash-enabled: true
copilot-command-context-menu-order: 9007199254740991
copilot-command-model-key: ""
copilot-command-last-used: 0
---
要生成与上述笔记思想高度契合的代码注释，关键在于将注释从「描述代码做了什么」（What）提升到「解释为何如此设计、权衡了哪些因素、系统层面的影响是什么」（Why & How at a deeper level）。这正是“Crack 开发者”思维在代码文档中的体现。

以下是为贯彻四大洞见而制定的 「深度系统级代码注释规范」：

📜 深度系统级代码注释规范（Crack Developer Style）
1. 注释目标：揭示抽象层次，而非复述逻辑
✅ 正确：解释设计决策背后的系统原理或权衡
❌ 错误：重复代码字面意思（如 // 增加计数器）

c
// BAD
i++; // 增加循环计数

// GOOD
// 使用原子操作而非互斥锁，因该计数器仅用于监控（非关键路径），
// 可接受少量丢失以换取更低的 CPU 缓存行争用（避免 false sharing）。
// 参见：perf stat 显示 mutex contention 占比 >15% 时 P99 延迟陡增。
atomic_fetch_add(&metrics->req_count, 1);

2. 强制包含「权衡声明」（Trade-off Declaration）
在关键路径、性能敏感或非直观设计处，必须说明：
为什么不用更“优雅”/“标准”的方案？
牺牲了什么？换来了什么？
适用边界是什么？

python
TRADE-OFF: 使用 raw socket 而非 asyncio + HTTP client
✅ 收益：绕过 TCP_NODELAY 默认延迟，实现 <50μs 的请求响应（实测）
❌ 代价：失去高层协议抽象，需手动处理连接池、重试、TLS
⚠️ 仅适用于内部低延迟服务间通信（<1ms SLA），不可用于公网
def send_low_latency_request(payload: bytes) -> bytes:
...

3. 关联可观测性证据（Observability-Driven Design）
注释应引用实际观测数据（perf、strace、火焰图、监控指标），而非主观判断。

go
// WHY: 避免在 hot path 中分配内存（GC pressure 导致 STW >2ms）
// pprof 显示 allocs/op 从 3 → 0 后，P99 延迟从 8ms → 1.2ms
// 见：https://grafana.example.com/d/latency-profile?var-job=order-service
var buffer = sync.Pool{
New: func() interface{} { return make([]byte, 4096) },
}

4. 区分「应用层意图」与「系统层机制」
用分层注释明确表达：
// INTENT: 业务/功能目标（What we want）
// MECHANISM: 系统实现手段（How the machine does it）

rust
// INTENT: 确保订单状态变更的原子性与可追溯性
// MECHANISM: 使用 PostgreSQL advisory lock (key = order_id)
// 避免表级锁竞争，同时利用 WAL 实现变更日志（无需额外 audit 表）
// 注意：advisory lock 不随事务自动释放，需显式 unlock
pg_advisory_xact_lock(order_id);

5. 自动化优于手动：注释即契约（Comment as Contract）
对于「一人军团」系统，注释应成为自动化系统的输入依据，例如：
监控告警规则生成
SLO 定义
故障自愈触发条件

yaml
AUTOMATION CONTRACT:
若此函数执行时间 > 100μs，触发 P1 告警（SLO violation）
自动回滚到 v2.3.1（已知稳定版本）
详见 runbook: /docs/incidents/order-validation-latency.md
def validate_order(order: Order) -> ValidationResult:
...

6. 禁用模糊词汇，使用精确系统术语
避免：“快一点”、“更稳定”、“高效”
改用：“减少 2 次系统调用”、“消除 L3 cache miss”、“降低 tail latency”

c
// BAD: "优化性能"
// GOOD: "合并两次 write() 系统调用为一次，减少 syscall overhead (~1.2μs per call)"

🧠 总结：注释即思维外显
优秀的注释不是代码的附庸，而是开发者系统思维的结晶。
它应当让后来者（包括未来的自己）一眼看出：
这段代码在系统栈中的位置
设计者权衡了哪些约束
证据支撑了这一决策
自动化系统如何围绕它构建
