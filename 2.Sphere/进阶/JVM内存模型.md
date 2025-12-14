---
view-count: 7
---
# JVM 内存模型｜语义压缩锚点

★ JVM 内存 = 并发基础  
★ 资源管理 → 正确性前提  

★ 线程私有 → PC / 栈  
★ 线程共享 → 堆 / 方法区  
❗ 堆 = GC 主战场  

★ Metaspace → 本地内存  
❗ 类加载失控 → OOM  

★ JMM ≠ 物理内存  
★ JMM → 并发契约  

★ 主内存 ↔ 工作内存  
❗ 本地副本 → 可见性问题  

★ 并发三要素  
原子性 / 可见性 / 有序性  

❗ i++ ≠ 原子操作  

★ synchronized → 互斥 + 可见  
△ CAS → 无锁原子性  

★ volatile → 可见 + 有序  
❗ volatile ≠ 原子性  

★ 指令重排 → 性能优化  
❗ 重排 → 并发失序  

★ Happens-Before → 行为证明  
△ unlock → lock  
△ write volatile → read  

★ final → 构造安全发布  

★ 并发 bug = 物理映射  
❗ CPU 缓存 → 软件复杂性  

★ 少锁 ≻ 乱锁  
★ 精确同步 ≻ 过度同步  

★ JMM 理解 → 系统级能力
