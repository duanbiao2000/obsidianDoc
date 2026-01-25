---
rating: 3.0
tags:
- discord-message-storage
- mongodb-to-cassandra-migration
- database-evolution
- scylla-db
- Type/Reference
- Domain/Technology
view-count: 2
---

## 🔗 相关链接

**上级索引**:
- [[2.Topics\00.协议与规范\PRD\_Index_of_PRD.md|PRD]]
- [[2.Topics\00.协议与规范\_Index_of_00.协议与规范.md|00.协议与规范]]
- [[2.Topics\_Index_of_2.Topics.md|2.Topics]]

---

![image.png](https://cdn.jsdelivr.net/gh/duanbiao2000/BlogGallery@main/picutre/20250513134754924.png)
您提供了一段文字和一张图片，图片标题是 **"How Discord Stores Trillions Of Messages"**。

这段文字和图片详细阐述了 Discord 消息存储技术栈的演进过程，从 MongoDB 到 Cassandra，最终迁移到 ScyllaDB，以及每次迁移的原因和解决的问题。

以下是对图片和文字内容的解读：

### 核心概念：

1. **Scalability (可伸缩性)：** Discord 存储系统演进的核心驱动力，旨在处理从数亿到数万亿条消息的增长，并保持低延迟。
2. **Latency (延迟)：** 在高并发和大数据量下，如何保持消息的读写延迟在一个可接受的范围内，是每次迁移的关键考量。
3. **Database Evolution (数据库演进)：** 大型互联网公司根据业务增长和技术挑战，不断调整和优化其底层数据库技术栈的典型案例。
4. **Data Model (数据模型)：** 消息存储这种特定场景对数据库选择有特殊要求（高写入、高读取、低延迟）。

### 消息存储技术栈的演进过程：

图片和文字共同展示了 Discord 消息存储的三个主要阶段：

**阶段一：MongoDB (2015年)**

- **初期架构：** Discord 的第一个版本（2015年）基于单个 MongoDB 副本构建。
- **遇到的问题 (2015年11月)：**
    - **数据量：** 存储了约 1 亿条消息。
    - **内存限制：** RAM 无法再容纳数据和索引，导致数据溢出到磁盘。
    - **性能影响：** 延迟变得**不可预测 (unpredictable)**。
- **迁移原因：** MongoDB 在达到一定规模后，单副本的内存限制和不可预测的延迟使其不再适合海量消息存储的需求。

**阶段二：Cassandra (2015年后期 - 2022年初)**

- **选择原因：** Discord 选择了 Cassandra 来替代 MongoDB，因为它在高写入吞吐量和横向扩展方面具有优势。
- **发展规模：**
    - **2017年：** 拥有 12 个 Cassandra 节点，存储了数十亿条消息。
    - **2022年初：** 扩展到 177 个 Cassandra 节点，存储了数万亿条消息。
- **遇到的问题 (2022年初)：** 尽管规模庞大，Cassandra 在极高负载下也暴露出新的问题：
    - **延迟不可预测：** 再次出现延迟不可预测的问题。
    - **维护成本过高：** 维护操作（如压缩 SSTables）变得过于昂贵，并且影响性能。
    - **具体原因分析：**
        - **LSM 树结构：** Cassandra 使用 LSM (Log-Structured Merge) 树作为内部数据结构。LSM 树的特点是写入快，但读取通常更慢（可能需要合并多个 SSTable）。在有数百用户的服务器上同时进行大量并发读取时，容易导致**热点 (hotspots)** 和性能下降。
        - **SSTable 压缩：** 维护 Cassandra 集群，特别是对 SSTable 文件进行压缩（Compaction），会严重影响性能，因为这是 CPU 密集型和 I/O 密集型操作。
        - **垃圾回收 (GC) 暂停：** Cassandra 是用 Java 编写的，Java 的垃圾回收机制可能会导致 **“Stop-the-world”暂停 (Stop-the-world GC pauses)**，从而引发显著的延迟尖峰（图片中提到了“10 seconds 'stop-the-world' GC”）。

**阶段三：ScyllaDB (2022年至今)**

- **选择原因：** ScyllaDB 被选为 Cassandra 的继任者。
    - **兼容性：** ScyllaDB 是**与 Cassandra 兼容的数据库**，这意味着迁移的成本相对较低，因为数据模型和 API 接口是兼容的。
    - **性能：** ScyllaDB 使用 **C++ 编写**，通常具有更高的性能和更低的延迟，且避免了 Java GC 暂停问题。
    - **“Shard-per-core”架构：** 图片中提到 ScyllaDB 使用“Shard-per-core database”，这是一种将每个 CPU 核心分配一个独立的分片，减少锁争用，提高并发处理能力的设计。
- **架构重构：** Discord 重新设计了其架构，包括：
    - 一个**单体 API (monolithic API)**。
    - 一个用 **Rust** 编写的**数据服务 (data service)**。
    - 以及基于 ScyllaDB 的存储。
- **性能提升：**
    - **P99 读取延迟：** ScyllaDB 降至 15ms (Cassandra 为 40-125ms)。
    - **P99 写入延迟：** ScyllaDB 降至 5ms (Cassandra 为 5-70ms)。
- **理解 ScyllaDB 内部结构（图片右侧）：**
    - **Python API：** 应用程序通过 Python API 与数据服务交互。
    - **Data Service (Rust)：** 用 Rust 编写的数据服务，负责处理业务逻辑和数据访问，并通过 REST RPC 与 ScyllaDB 通信。
    - **ScyllaDB (Shard-per-core database)：** ScyllaDB 利用多核 CPU 优势，每个核心处理一个分片。
    - **Memtable：** 内存中的写缓冲区，数据先写入这里。
    - **Row-based Cache：** 内存中的行级缓存，提高读取性能。
    - **Commit Log：** 写入操作的持久化日志，用于恢复。
    - **SSTables (Sorted String Tables)：** 数据持久化到磁盘的文件，与 Cassandra 类似。
    - **CPU / RAM / Storage (SSD)：** 表示 ScyllaDB 充分利用这些硬件资源。

### 总结：

Discord 的消息存储演进史是一个经典的案例，展示了如何在应对海量数据和高并发场景时，不断优化底层数据库技术。

- **MongoDB (初期)：** 适合小规模快速原型，但存在内存和延迟瓶颈。
- **Cassandra (中期)：** 解决了大规模写入和横向扩展问题，但随着数据量进一步爆炸性增长，其 LSM 树的读取特性、GC 暂停和维护开销成为新的瓶颈。
- **ScyllaDB (当前)：** 作为 Cassandra 的高性能 C++ 实现，通过更优化的内部架构和内存管理，解决了 Cassandra 遇到的延迟和维护问题，提供了卓越的读写性能和可伸缩性，最终支持了数万亿条消息的存储。

这个演进过程也反映了 Discord 在其关键数据存储上对性能和可用性不懈的追求。