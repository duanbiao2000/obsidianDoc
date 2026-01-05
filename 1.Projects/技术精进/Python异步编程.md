---
view-count: 4
---
# Python 高并发异步工程手册 (10k+ 并发)

---

### 一、 核心引擎：asyncio 内部机制
*   **本质**：基于 **I/O 多路复用**（epoll/kqueue/IOCP）的单线程调度器。
*   **三剑客**：
    *   **Event Loop**：调度中心，循环执行就绪回调。
    *   **Coroutine (`async def`)**：可暂停的函数，封装执行逻辑。
    *   **Task**：协程的调度单位，负责状态追踪。
*   **运行链路**：
    1.  `await` 挂起协程 $\rightarrow$ 注册 I/O 监听 $\rightarrow$ 控制权交还 Loop。
    2.  Loop 执行其他 Task $\rightarrow$ I/O 就绪 $\rightarrow$ 触发中断信号。
    3.  Loop 唤醒挂起的 Task $\rightarrow$ 从 `await` 处恢复执行。
*   **关键函数**：`_run_once`（单次循环逻辑）、`call_soon`（注册立即回调）。

---

### 二、 替代方案：uvloop vs Trio
| 方案 | 核心技术 | 性能 | 适用场景 |
| :--- | :--- | :--- | :--- |
| **asyncio** | 纯 Python 选择器 | 基础 | 标准开发，中低并发 |
| **uvloop** | **libuv (C语言)** | **⚡ 极高 (2-4倍)** | 生产环境、高性能 Web API |
| **Trio** | 结构化并发 | 高 | 逻辑复杂、对取消/超时控制极严的项目 |

*   **生产首选**：`asyncio + uvloop`（一行代码无缝替换）。
    ```python
    import uvloop
    uvloop.install()
    ```

---

### 三、 高并发架构设计规范
*   **黄金准则**：**全链路异步化**。禁止出现任何阻塞调用。
*   **禁忌清单**：
    *   ❌ `time.sleep()` $\rightarrow$ ✅ `asyncio.sleep()`
    *   ❌ `requests.get()` $\rightarrow$ ✅ `httpx.get()` / `aiohttp`
    *   ❌ 同步 DB Driver $\rightarrow$ ✅ `asyncpg` / `motor` / `aioredis`
*   **连接池管理**：必须使用异步池（Pool），避免频繁握手。
*   **并发限流**：使用 `asyncio.Semaphore(1000)` 防止下游崩溃（数据库连接过载）。

---

### 四、 10k+ 并发生产级方案
#### 1. 技术栈 (Stack)
*   **框架**：FastAPI (基于 Starlette/Pydantic)。
*   **引擎**：uvloop。
*   **数据库**：PostgreSQL + `asyncpg`（目前最快的异步驱动）。
*   **部署**：Gunicorn + Uvicorn Workers。

#### 2. 系统调优 (OS Tuning)
*   **文件描述符**：`ulimit -n 65535`（解决 "Too many open files"）。
*   **TCP 队列**：`sysctl -w net.core.somaxconn=4096`。

#### 3. 部署模型
利用多核，通过多进程横向扩展（每个进程一个独立 Event Loop）：
```bash
# 启动 4 个进程，每个进程处理数千并发
gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker --worker-connections 4096
```

---

### 五、 避坑与监控
*   **CPU 密集任务**：不要在协程中计算！使用 `run_in_executor` 扔进进程池。
*   **Task 泄漏**：监控 `len(asyncio.all_tasks())`，防止长耗时任务堆积内存。
*   **超时控制**：所有外部调用必须包裹 `asyncio.wait_for(..., timeout=5)`。
*   **压测工具**：使用 `wrk` 或 `locust` 模拟 10,000+ 连接进行闭环验证。

---

### 六、 总结建议
**10k+ 并发 = uvloop引擎 + 全链路异步组件 + 异步连接池 + 多进程部署 + 系统参数调优。**