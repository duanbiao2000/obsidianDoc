本书第19章 “Literature（参考文献）” 提供了 C++ 性能优化和底层编程相关的权威参考书籍和资料推荐。其主要内容和体系包括：

- **作者Agner Fog的优化手册系列**
    
    - 本书是该系列之一，此外还有《Optimizing subroutines in assembly language》《The microarchitecture of Intel, AMD, and VIA CPUs》《Instruction tables》《Calling conventions for different C++ compilers and operating systems》。
        
    - 这些都是C++及x86性能优化领域的顶级资料，长期更新，最新版本可在作者官网获取。
        
- **相关经典与现代参考书籍**
    
    - 推荐的优化、编译器实现、底层架构、系统设计书目，覆盖范围包括算法、C++高效编程、现代硬件架构说明等。适合进阶开发者和程序性能工程师作为进修资料。
        
- **扩展学习路径建议**
    
    - 本书建议如需深入学习，可以逐步参考：
        
        - C++ 语言与标准库权威教材。
            
        - 汇编与微架构层面优化专著（适合系统级高阶程序员）。
            
        - 针对Intel/AMD/C++优化的各类官方文档和专业社区。
            
        - 实用开源库和框架文档（如Boost、Intel MKL等）。
            
- **各章节均有细分的文献与专题扩展**
    
    - 包含部分侧重内存、编译器、算法、数学库、并行与系统编程方面的详细指引，以及社区讨论与最新论文线索。
        
    - 鼓励结合实际项目或Benchmark报告做深入测试与调优。
        

如果你希望掌握C++性能优化及现代编程底层技术，除本书外，建议系统性浏览上述系列手册、结合推荐书目与库文档，并在实践和社区交流中不断迭代学习。

1. [https://agner.org/optimize/optimizing_cpp.pdf](https://agner.org/optimize/optimizing_cpp.pdf)

---

Agner Fog 是一位丹麦计算机科学家、进化人类学家，以其在 **x86 CPU 架构性能优化** 领域的深入研究和广泛传播而闻名。他撰写了多本权威的、免费公开的技术手册，被全球系统程序员、编译器开发者和高性能计算工程师广泛参考。

---

### 🔍 Agner Fog 的主要贡献

#### 1. **五本经典优化手册（免费公开）**

这些手册系统讲解了从硬件微架构到软件优化的完整知识体系：

- **《Optimizing software in C++》**  
    面向 C++ 程序员，讲解如何编写高效代码，涵盖缓存、分支预测、向量化、编译器行为等。
    
- **《Microarchitecture》**  
    深入剖析 Intel 和 AMD 各代 CPU 微架构（如 Core, Sandy Bridge, Zen 等），包括流水线、执行单元、缓存结构、延迟/吞吐量等。
    
- **《Instruction tables》**  
    详尽列出 x86/x64 指令在不同 CPU 上的 **延迟（latency）**、**吞吐量（throughput）** 和 **μop 分解**，是底层优化的“圣经”。
    
- **《Calling conventions》**  
    解释 Windows（x64）、Linux/macOS（System V ABI）等平台的函数调用约定、寄存器使用规则、栈帧布局等。
    
- **《The microarchitecture of Intel, AMD and VIA CPUs》**  
    对各厂商 CPU 微架构的横向对比与深度分析。
    

> 所有手册均可在其官网免费下载：  
> 👉 [https://www.agner.org/optimize/](https://www.agner.org/optimize/)

---

#### 2. **开源工具与测试程序**

- 提供用于 CPU 性能测试的 **C/C++/汇编代码示例**。
- 包含测量指令延迟、吞吐量、缓存行为的基准测试程序。
- 这些工具常被用于验证 CPU 行为或调试性能问题。

---

#### 3. **对编译器和开发者社区的影响**

- GCC、LLVM、Intel ICC 等编译器团队参考其手册设计优化策略。
- 高性能库（如 BLAS、FFTW、游戏引擎、数据库）开发者常依据其建议进行手工优化或指导自动向量化。

---

### 📚 为什么 Agner Fog 的资料如此重要？

- **深度结合硬件与软件**：他不仅懂汇编，还深入理解 CPU 内部工作机制。
- **实证精神**：所有结论基于大量实验测量，而非理论推测。
- **持续更新**：从 Pentium III 到最新的 Intel Core Ultra / AMD Zen 4，他持续跟踪并更新文档。
- **免费开放**：极大降低了系统级性能优化的学习门槛。

---

### 💡 应用场景举例

- 你想知道 `vaddps` 在 Intel Ice Lake 上的吞吐量？查《Instruction tables》。
- 你的循环性能不佳？用《Optimizing software in C++》检查是否破坏了缓存局部性或引入了依赖链。
- 你想手写汇编内联函数？参考《Calling conventions》确保 ABI 兼容。

---

### 🌐 相关项目（如你提到的 “Agner 项目”）

社区中有一些基于 Agner Fog 工具和思想的开源项目，例如：

- 自动化性能测试框架
- 教学用的 CPU 行为模拟器
- 集成其指令表数据的 IDE 插件

但需注意：**Agner Fog 本人并未维护名为 “Agner” 的官方 GitHub 项目**，相关项目多为第三方实现。

---

如果你正在从事高性能计算、游戏引擎、数据库、编译器开发或系统编程，**Agner Fog 的资料几乎是必读内容**。