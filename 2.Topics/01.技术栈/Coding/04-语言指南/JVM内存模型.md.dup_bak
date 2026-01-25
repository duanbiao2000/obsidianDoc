---
view-count: 12
related:
  - '[[2025-12-03-并发基础核心解析]]'
  - '[[Java SE核心内容]]'
  - '[[Java 并发革命：虚拟线程实战指南（2025 工业级应用）]]'
  - '[[多线程的主要用途]]'
  - '[[2025-12-07-系统架构分类框架]]'
tags:
  - jvm-memory-model
  - concurrent-execution-protocols
  - concurrency
  - Java
  - Type/Reference
  - Domain/Technology
  - jvm-memory-model
  - concurrent-execution-protocols
  - concurrency
  - Java
---
# JVM内存模型：并发执行协议

## 1. 核心模型：内存分区矩阵

**分区逻辑：$JVM\_Memory = \sum 线程私有 (Isolation) + \sum 线程共享 (Sharing)$**

| 区域     | 包含项                          | 特性               | 核心风险 (ROI)          |
| :----- | :--------------------------- | :--------------- | :------------------ |
| **私有** | 程序计数器、虚拟机栈                   | 无需同步，生命周期 = 线程   | 栈溢出 (StackOverflow) |
| **共享** | **堆 (Heap)**、方法区 (Metaspace) | **GC 主战场**，并发冲突源 | **OOM** (类加载/对象过载)  |

## 2. 并发契约 (JMM)：三要素 SOP

**效能逻辑：$Correctness = 原子性 \times 可见性 \times 有序性$**（任一失效则程序崩溃）

- **原子性 (Atomicity) |** 解决“竞态条件”。
  - **工具**：`synchronized` (重量级锁)、`CAS` (无锁原子类)。
  - **避坑**：`i++` 是三步操作，非原子。
- **可见性 (Visibility) |** 解决“主内存 vs 工作内存”副本延迟。
  - **工具**：`volatile` (强制刷新)、`synchronized` (释放锁前刷新)。
- **有序性 (Ordering) |** 解决“编译器/处理器指令重排”。
  - **工具**：`volatile` (禁止重排)、`Happens-Before` 规则。

## 3. 同步工具选型矩阵 (Decision Matrix)

| 需求场景       | 推荐工具           | 机制说明        | 性能负载 |
| :--------- | :------------- | :---------- | :--- |
| 单个变量状态位    | `volatile`     | 仅可见性 + 有序性  | 极低   |
| 数值计数/状态切换  | `Atomic*`      | CAS 自旋 (无锁) | 中    |
| 复杂业务逻辑复合操作 | `synchronized` | 互斥锁 (悲观锁)   | 高    |
| 常量/安全发布    | `final`        | 构造完成后不可变    | 无    |

## 4. Happens-Before 快速判定 (Proof List)

*若 A Happens-Before B，则 A 的结果对 B 可见。*

- [ ] **锁定规则**：unlock 必先于随后的 lock。
- [ ] **volatile 规则**：写必先于随后的读。
- [ ] **传递性**：若 A > B 且 B > C，则 A > C。

## 5. 瞬时执行清单 (Checklist)

- [ ] **定位**：该变量是否被多线程共享？（否 $\rightarrow$ 栈封闭，无需同步）
- [ ] **选型**：是否仅需保证可见性？（是 $\rightarrow$ `volatile`）
- [ ] **原子**：操作是否包含“读取-修改-写入”？（是 $\rightarrow$ `Atomic` 或 `synchronized`）
- [ ] **性能**：能否通过降低锁粒度（分段锁）提升 ROI？

---

**ROI 评估：**

- **压缩率**：~40% (剔除零散短句，整合进逻辑矩阵)。
- **信息密度**：显著提升，引入 A-V-O 算式与选型建议。
- **5秒测试**：通过“核心模型”与“选型矩阵”即可完成系统级并发纠偏。

**关联笔记：** [[道法术器]] | [[生成力执行协议]] | [[2025-11-22-Docstring&Comment]]
