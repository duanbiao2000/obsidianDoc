
# 目录

## CONTENT

1. 什么是进程？
2. 什么是线程？
3. 并行与并发
4. Go语言中的goroutine和channel
5. 并行编程的应用场景
6. Go语言并行编程的优势
7. 小结

---

# 什么是进程？

1. 进程是一个正在执行程序的实例。
2. 每个进程都有独立的内存空间和资源分配。
3. 创建新的进程需要消耗系统资源，因此在使用时需要谨慎。

```go
package main

import (
	"fmt"
	"os/exec"
)

func main() {
	// 使用exec.Command创建新进程
	cmd := exec.Command("ls", "-l")
	output, err := cmd.Output()
	if err != nil {
		fmt.Println("Error:", err)
	}
	fmt.Println(string(output))
}
```

---

# 什么是线程？

1. 线程是进程内部的一个执行单元。
2. 多个线程可以共享同一个进程的内存空间和资源。
3. 线程切换开销相对较小，可以提高程序的响应速度。

```go
package main

import (
	"fmt"
	"runtime"
)

func worker(id int) {
	fmt.Printf("Worker %d starting\n", id)
}

func main() {
	// 获取当前进程的可用CPU核数
	numCPU := runtime.NumCPU()
	fmt.Println("Number of CPUs:", numCPU)

	// 创建多个goroutine
	for i := 0; i < numCPU; i++ {
		go worker(i)
	}
	fmt.Println("All workers started")
}
```

---

# 并行与并发

1. 并行：多个任务同时进行，每个任务占用不同的CPU核。
2. 并发：多个任务交替执行，在一个CPU核上快速切换。

---

# Go语言中的goroutine和channel

1. goroutine 是 Go 语言中的轻量级线程。
2. channel 用于通信和同步goroutine。

```go
package main

import (
	"fmt"
)

func worker(id int, jobs <-chan int, results chan<- int) {
	for j := range jobs {
		fmt.Println("Worker", id, "processing job", j)
		results <- j * 2
	}
}

func main() {
	jobs := make(chan int, 100)
	results := make(chan int, 100)

	// 创建多个goroutine
	for w := 1; w <= 3; w++ {
		go worker(w, jobs, results)
	}

	// 发送任务到channel
	for j := 1; j <= 5; j++ {
		jobs <- j
	}
	close(jobs)

	// 从channel接收结果
	for a := 1; a <= 5; a++ {
		<-results
	}
}
```

---

# 并行编程的应用场景

1. 网络服务器：处理多个客户端请求并行。
2. 数据处理：将大数据分解成多个任务并行处理。
3. 科学计算：利用多核CPU加速计算。

---

# Go语言并行编程的优势

1. 简洁易用：Go 语言提供了丰富的并发工具，例如 goroutine 和 channel。
2. 高性能：Go 语言的并发模型能够充分利用多核CPU的性能。
3. 安全可靠：Go 语言的内存管理机制可以有效避免数据竞争问题。
---
# **Goroutine**

* 轻量级协程：
* 并发执行：多个 goroutine 可以同时运行
* 简易创建：使用 `go` 关键字

```go
package main

import (
	"fmt"
	"time"
)

func sayHello(name string) {
	for i := 0; i < 5; i++ {
		fmt.Println(name, ":", i)
		time.Sleep(100 * time.Millisecond)
	}
}

func main() {
	go sayHello("Alice") // 启动一个 goroutine 执行 sayHello 函数
	sayHello("Bob")       // 主 goroutine 继续执行
	time.Sleep(2 * time.Second)
	fmt.Println("Main goroutine exiting.")
}
```


---

# **Channel**

- `jobs` 通道用于发送任务给工作者 
- `results` 通道用于接收结果
- 主 Goroutine 可以安全地将任务发送给多个 worker 

```go
package main

import (
	"fmt"
)

func worker(id int, jobs <-chan int, results chan<- int) {
	for j := range jobs {
		fmt.Println("Worker", id, "processing job", j)
		results <- j * 2
	}
}

func main() {
	jobs := make(chan int, 100)
	results := make(chan int, 100)

	// 创建多个 goroutine
	for w := 1; w <= 3; w++ {
		go worker(w, jobs, results)
	}

	// 发送任务到channel
	for j := 1; j <= 5; j++ {
		jobs <- j
	}
	close(jobs)

	// 从channel接收结果
	for a := 1; a <= 5; a++ {
		<-results
	}
}
```







