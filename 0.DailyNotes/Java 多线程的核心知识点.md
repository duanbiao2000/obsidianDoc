在 Java 中，**多线程**是一种允许程序同时执行多个任务的机制，广泛用于提升程序性能、响应速度和资源利用率。下面我来带你系统梳理一下 Java 多线程的核心知识点 🚀

---

## 🧠 什么是线程？

- **线程（Thread）**是程序执行的最小单位，是进程中的一个执行路径。
- 一个 Java 程序至少有一个线程：**主线程（main）**。
- 多线程允许多个任务“同时”运行（并发），尤其适合处理 I/O 密集型或用户交互场景。

---

## 🛠 Java 创建线程的三种方式

| 方式 | 简述 | 示例 |
|------|------|------|
| **继承 Thread 类** | 重写 `run()` 方法 | `class MyThread extends Thread { public void run() { ... } }` |
| **实现 Runnable 接口** | 推荐方式，避免单继承限制 | `class MyRunnable implements Runnable { public void run() { ... } }` |
| **实现 Callable 接口 + FutureTask** | 有返回值，可抛异常 | `Callable<Integer> task = () -> { return 42; };` |

---

## 🔁 线程的生命周期

1. **新建（New）**：创建线程对象
2. **就绪（Runnable）**：调用 `start()`，等待 CPU 调度
3. **运行（Running）**：获得 CPU 时间片，执行 `run()`
4. **阻塞（Blocked）/等待（Waiting）**：等待资源或条件
5. **死亡（Terminated）**：执行完毕或异常退出

---

## 🧩 常用线程方法

| 方法 | 说明 |
|------|------|
| `start()` | 启动线程，进入就绪状态 |
| `run()` | 线程执行体（不要手动调用） |
| `sleep(ms)` | 让当前线程休眠指定毫秒 |
| `join()` | 等待其他线程执行完毕 |
| `yield()` | 暂时让出 CPU |
| `interrupt()` | 中断线程（配合 `isInterrupted()` 使用） |

---

## 🧱 线程安全与同步

多线程访问共享资源时可能出现**线程安全问题**，解决方式包括：

- `synchronized` 关键字（同步方法/代码块）
- `Lock` 接口（如 `ReentrantLock`）
- 原子类（如 `AtomicInteger`）
- 并发集合（如 `ConcurrentHashMap`）

---

## ⚙️ 高级特性

| 特性 | 简述 |
|------|------|
| **线程池（ExecutorService）** | 复用线程，提升性能 |
| **并发工具类** | 如 `CountDownLatch`、`Semaphore`、`CyclicBarrier` |
| **并发包（java.util.concurrent）** | 提供丰富的并发支持 |

---

## 🧪 示例：使用线程池执行任务

```java
ExecutorService pool = Executors.newFixedThreadPool(3);
pool.execute(() -> System.out.println("任务1"));
pool.shutdown();
```

---

如果你想，我可以帮你写一个“多线程抢票”或“并发计数器”的实战小项目，或者深入讲讲线程池的底层原理。你最近在学哪一块？我可以帮你定制讲解 😄

---

