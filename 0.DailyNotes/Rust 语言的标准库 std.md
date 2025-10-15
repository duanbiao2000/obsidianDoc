Rust 的标准库（`std`）是 Rust 语言自带的核心库，提供了基础且强大的功能集合，涵盖了内存管理、数据结构、I/O 操作、并发编程等核心能力。标准库设计遵循 Rust 的核心原则：安全性、性能和零成本抽象。

### 标准库的核心组成

1. **根模块（`std`）**

标准库的入口点，包含最基础的类型和功能，例如：

- `std::mem`：内存管理相关函数（如 `size_of`、`swap`）

- `std::ptr`：原始指针操作（ unsafe 相关）

- `std::panic`：恐慌处理机制

- `std::process`：进程管理（如启动子进程、获取环境变量）

2. **基础数据类型与集合**

提供了常用的数据结构，确保安全且高效：

- **标量类型**：`i32`、`u64`、`f64`、`bool`、`char` 等（由语言直接提供，标准库补充方法）

- **字符串**：`std::string::String`（动态可增长字符串）和 `&str`（字符串切片）

- **集合**：

- `Vec<T>`：动态数组（可增长）

- `HashMap<K, V>` / `BTreeMap<K, V>`：哈希表和有序映射

- `HashSet<T>` / `BTreeSet<T>`：哈希集合和有序集合

- `LinkedList<T>`：双向链表（特定场景使用）

- **其他**：`Option<T>`（可选值）、`Result<T, E>`（结果处理）、`Box<T>`（堆分配指针）等

3. **I/O 操作（`std::io`）**

提供输入输出功能，包括：

- 标准输入输出：`std::io::stdin()`、`std::io::stdout()`

- 文件操作：`std::fs::File`（文件读写）、`std::fs::Path`（路径处理）

- 流操作：`Read`、`Write` 等 trait，支持缓冲（`BufReader`/`BufWriter`）

4. **并发与多线程（`std::thread`、`std::sync`）**

安全的并发编程工具：

- 线程管理：`std::thread::spawn`（创建线程）、`join`（等待线程结束）

- 同步原语：

- `Mutex<T>`：互斥锁（确保数据独占访问）

- `RwLock<T>`：读写锁（多读者单写者）

- `Arc<T>`：原子引用计数（线程安全的共享所有权）

- `Barrier`、`Condvar` 等同步工具

5. **错误处理**

- `std::error::Error`：统一的错误 trait，用于自定义错误类型

- `Option<T>` 和 `Result<T, E>`：避免空指针和异常，通过模式匹配处理可选值和错误

6. **算法与工具**

- `std::cmp`：比较相关（`PartialOrd`、`Ord` 等 trait）

- `std::iter`：迭代器 trait（`Iterator`）及适配器（如 `map`、`filter`）

- `std::fmt`：格式化输出（`Display`、`Debug` 等 trait，用于 `println!`）

- `std::num`：数值相关功能（如大整数 `u128`、浮点数操作）

7. **网络编程（`std::net`）**

基础网络功能：

- TCP：`TcpListener`（服务器）、`TcpStream`（客户端）

- UDP：`UdpSocket`

- 地址处理：`IpAddr`、`SocketAddr` 等

8. **时间与日期（`std::time`）**

- `SystemTime`：系统时间（可跨平台）

- `Duration`：时间间隔（如 `Duration::from_secs(5)` 表示 5 秒）

### 标准库的特点

- **安全性**：避免空指针、缓冲区溢出等问题（例如 `Vec` 自动管理内存，`String` 保证 UTF-8 有效性）。

- **零成本抽象**：标准库的抽象（如迭代器、`Vec`）不会带来额外性能开销，编译后与手写优化代码相当。

- **跨平台**：接口统一，内部适配不同操作系统（如文件操作在 Windows 和 Linux 下行为一致）。

- **模块化**：可通过 `use` 导入所需模块，避免编译冗余代码。

### 如何使用标准库

无需额外安装，Rust 自带标准库。使用时通过 `use` 导入所需模块：

```rust

use std::collections::HashMap;

use std::io::{self, Read};

fn main() {

// 使用 HashMap

let mut map = HashMap::new();

map.insert("key", "value");

// 读取标准输入

let mut input = String::new();

io::stdin().read_to_string(&mut input).unwrap();

}

```

### `std` 与 `core` 的关系

- `std` 依赖于操作系统（提供 I/O、线程等功能），无法在无操作系统的环境（如嵌入式）使用。

- `core` 是 `std` 的子集，不依赖操作系统，仅包含基础功能（数据结构、算法等），适用于裸机编程。

标准库是 Rust 开发的基础，大多数程序都会直接或间接依赖它。其设计兼顾了安全性和性能，是 Rust 语言哲学的集中体现。