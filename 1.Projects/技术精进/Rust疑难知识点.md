---
view-count: 15
update: 2026-01-07 18:11
related:
  - "[[Rust 异步与并发系统学习路径]]"
---
 
# Rust 并发与异步：OS 线程 vs Tokio 协程

## 1. 核心逻辑：决策矩阵

并发选型取决于任务性质。**不要在异步运行时执行耗时的同步计算。**

| 维度       | OS 线程 (`std::thread`) | Tokio 异步 (`async/await`)     |
| :------- | :-------------------- | :--------------------------- |
| **适用场景** | **CPU 密集型**（加密、图像处理）  | **I/O 密集型**（Web 服务、数据库）      |
| **开销**   | 较高（操作系统内核调度）          | 极低（用户态任务切换）                  |
| **通信**   | `mpsc` 通道             | `tokio::sync::mpsc`          |
| **共享变量** | `Arc<Mutex<T>>`       | `Arc<tokio::sync::Mutex<T>>` |

## 2. OS 线程实战协议 (CPU-Bound)

### **模式 A：安全数据共享 (Arc + Mutex)**

- **场景**：多个线程需要同时修改同一个计数器或状态。
- **Action**：用 `Arc` 提供多所有权，用 `Mutex` 提供可变性。

```rust
let counter = Arc::new(Mutex::new(0));
for _ in 0..10 {
    let c = Arc::clone(&counter);
    thread::spawn(move || {
        let mut num = c.lock().unwrap(); // 阻塞直到获取锁
        *num += 1;
    });
}
```

### **模式 B：消息传递 (mpsc)**

- **原则**：**不要通过共享内存来通信，而要通过通信来共享内存。**

```rust
let (tx, rx) = mpsc::channel();
thread::spawn(move || tx.send("数据").unwrap());
let data = rx.recv().unwrap(); // 阻塞直到收到消息
```

## 3. Tokio 异步协议 (I/O-Bound)

### **模式 C：并发任务管理 (tokio::spawn)**

- **场景**：同时处理数千个 TCP 连接。
- **注意**：`tokio::spawn` 立即返回 `JoinHandle`，任务在后台运行。

```rust
#[tokio::main]
async fn main() {
    let handle = tokio::spawn(async { "结果" });
    let res = handle.await.unwrap(); // 非阻塞等待
}
```

### **模式 D：跨越阻塞红线 (spawn_blocking)**

- **红线**：禁止在 `async` 函数中调用 `std::thread::sleep` 或耗时计算，否则会**冻结**整个运行时。
- **Action**：必须包裹在 `spawn_blocking` 中。

```rust
// 错误：tokio::time::sleep(d).await; // 正确
// 错误：std::thread::sleep(d);       // 阻塞！
let res = tokio::task::spawn_blocking(|| {
    std::thread::sleep(Duration::from_secs(1)); // 安全
}).await;
```

## 4. 避坑指南：执行红线 (Safeguards)

- [ ] **死锁预防**：异步 `Mutex` 的锁守卫 (`lock().await`) 不能跨越 `.await` 点，除非使用 `tokio::sync::Mutex`。
- [ ] **性能陷阱**：线程池大小默认等于 CPU 核心数，不要创建超过核心数太多的 OS 线程。
- [ ] **所有权**：`thread::spawn` 和 `tokio::spawn` 的闭包必须是 `move`，以确保数据在子任务生命周期内有效。

---
