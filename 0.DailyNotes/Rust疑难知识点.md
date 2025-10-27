
### Rust 并发与异步编程核心笔记

本文档旨在提供 Rust 中并发与异步编程最核心概念的快速参考。

### 1. 并发：使用 OS 线程 (std::thread)

适用于 CPU 密集型任务，利用多核处理器并行计算。

#### 1.1 线程的创建与数据共享 (thread + Arc)

通过 thread::spawn 创建新线程。若要在线程间共享数据所有权，需使用 Arc (原子引用计数)。

codeRust

```
use std::thread;
use std::sync::Arc;

fn main() {
    // Arc 允许多个线程安全地共享数据所有权
    let data = Arc::new(vec![1, 2, 3, 4, 5]);
    let mut handles = vec![];

    for i in 0..3 {
        // Arc::clone() 只增加引用计数，成本很低
        let data_clone = Arc::clone(&data);
        let handle = thread::spawn(move || {
            // 在新线程中使用共享数据
            println!("线程 {} 看到数据: {:?}", i, data_clone);
        });
        handles.push(handle);
    }

    // 等待所有线程执行完毕
    for handle in handles {
        handle.join().unwrap();
    }
}
```

#### 1.2 线程间通信：通道 (mpsc::channel)

通道是线程间传递消息的主要方式，避免了直接共享内存的复杂性。"mpsc" 代表 "多生产者，单消费者"。


```Rust
use std::sync::mpsc;
use std::thread;

fn main() {
    let (tx, rx) = mpsc::channel(); // tx: 发送端, rx: 接收端

    thread::spawn(move || {
        let message = String::from("来自子线程的消息");
        // 发送消息，所有权被移动
        tx.send(message).unwrap(); 
    });

    // rx.recv() 会阻塞主线程，直到收到消息
    let received = rx.recv().unwrap();
    println!("主线程收到: '{}'", received);
}
```


#### 1.3 共享可变状态：互斥锁` (Arc<Mutex<T>>)`

当多个线程需要修改同一个数据时，使用 Mutex (互斥锁) 来保证同一时间只有一个线程可以访问数据。

```Rust
use std::sync::{Arc, Mutex};
use std::thread;

fn main() {
    // 使用 Arc<Mutex<T>> 组合来实现线程安全的共享可变状态
    let counter = Arc::new(Mutex::new(0));
    let mut handles = vec![];

    for _ in 0..10 {
        let counter_clone = Arc::clone(&counter);
        let handle = thread::spawn(move || {
            // .lock() 会阻塞直到获取锁
            let mut num = counter_clone.lock().unwrap();
            *num += 1;
        });
        handles.push(handle);
    }

    for handle in handles {
        handle.join().unwrap();
    }

    println!("最终结果: {}", *counter.lock().unwrap());
}
```

### 2. 异步编程：使用 `tokio` 运行时

适用于 I/O 密集型任务（如网络请求、文件读写），能在单个线程上并发管理大量任务。

**依赖配置 (`Cargo.toml`):**
```toml
[dependencies]
tokio = { version = "1", features = ["full"] }
````

#### 2.1 核心概念：async/await

async fn 定义了一个异步函数，它返回一个 Future。.await 用于暂停当前函数，等待 Future 完成，期间不会阻塞线程。

codeRust

```
// #[tokio::main] 宏创建了一个运行时来执行 async 函数
#[tokio::main]
async fn main() {
    println!("开始执行异步任务...");
    let result = compute_something_async().await;
    println!("异步任务完成，结果: {}", result);
}

async fn compute_something_async() -> u32 {
    println!("异步计算开始");
    // 模拟一个非阻塞的 I/O 等待，例如网络请求
    tokio::time::sleep(tokio::time::Duration::from_secs(1)).await;
    println!("异步计算结束");
    100
}
```

#### 2.2 并发任务：tokio::spawn

tokio::spawn 将一个异步任务提交给运行时并发执行，立即返回一个 JoinHandle，主任务无需等待它。

codeRust

```
#[tokio::main]
async fn main() {
    // 启动一个后台任务，它会和主任务并发执行
    let handle = tokio::spawn(async {
        tokio::time::sleep(tokio::time::Duration::from_secs(1)).await;
        "后台任务的结果"
    });

    println!("主任务继续执行...");

    // 在需要时，可以 .await JoinHandle 来获取后台任务的结果
    let result = handle.await.unwrap();
    println!("获取到: {}", result);
}
```

#### 2.3 异步共享可变状态：tokio::sync::Mutex

与标准库的 Mutex 类似，但它的 .lock() 方法是异步的。在等待锁时，它会交出线程控制权，允许其他任务运行。

codeRust

```
use tokio::sync::Mutex;
use std::sync::Arc;

#[tokio::main]
async fn main() {
    let counter = Arc::new(Mutex::new(0));
    let mut handles = vec![];

    for _ in 0..10 {
        let counter_clone = Arc::clone(&counter);
        let handle = tokio::spawn(async move {
            // .lock().await 不会阻塞线程，而是异步等待
            let mut num = counter_clone.lock().await;
            *num += 1;
        });
        handles.push(handle);
    }

    // 等待所有并发任务完成
    for handle in handles {
        handle.await.unwrap();
    }

    println!("最终结果: {}", *counter.lock().await);
}
```

#### 2.4 处理阻塞代码：tokio::task::spawn_blocking

在 async 代码中调用会阻塞线程的同步函数（如 CPU 密集计算或传统文件 I/O）时，必须使用 spawn_blocking 将其移到专门的线程池，防止阻塞整个异步运行时。

codeRust

```
fn blocking_computation() -> String {
    // 这是一个耗时的、阻塞的同步函数
    std::thread::sleep(std::time::Duration::from_secs(1));
    "计算完成".to_string()
}

#[tokio::main]
async fn main() {
    println!("异步任务开始");
    
    // 将阻塞函数包裹在 spawn_blocking 中
    let handle = tokio::task::spawn_blocking(blocking_computation);

    // 在等待阻塞任务时，可以并发执行其他异步操作
    tokio::time::sleep(std::time::Duration::from_millis(500)).await;
    println!("主任务在阻塞计算期间做了一些其他事");

    let result = handle.await.unwrap();
    println!("阻塞任务的结果: {}", result);
}
```
