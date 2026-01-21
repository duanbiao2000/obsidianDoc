---
view-count: 5
update: 2026-01-07 10:42
related:
  - "[[编译器优化]]"
  - "[[程序员的“费曼学习法”：如何高效学习并掌握一门新技术？]]"
  - "[[嵌入式系统中的优化]]"
  - "[[为开源项目贡献核心代码]]"
---

如果你希望掌握C++性能优化及现代编程底层技术，除本书外，建议系统性浏览上述系列手册、结合推荐书目与库文档，并在实践和社区交流中不断迭代学习。

1. <https://agner.org/optimize/optimizing_cpp.pdf>

---

Agner Fog 是一位丹麦计算机科学家、进化人类学家，以其在 **x86 CPU 架构性能优化** 领域的深入研究和广泛传播而闻名。他撰写了多本权威的、免费公开的技术手册，被全球系统程序员、编译器开发者和高性能计算工程师广泛参考。

---

### 🔍 Agner Fog 的主要贡献

#### 1. **五本经典优化手册（免费公开）**

这些手册系统讲解了从硬件微架构到软件优化的完整知识体系：

- **《Optimizing software in C++》**\
  面向 C++ 程序员，讲解如何编写高效代码，涵盖缓存、分支预测、向量化、编译器行为等。

- **《Microarchitecture》**\
  深入剖析 Intel 和 AMD 各代 CPU 微架构（如 Core, Sandy Bridge, Zen 等），包括流水线、执行单元、缓存结构、延迟/吞吐量等。

- **《Instruction tables》**\
  详尽列出 x86/x64 指令在不同 CPU 上的 **延迟（latency）**、**吞吐量（throughput）** 和 **μop 分解**，是底层优化的“圣经”。

- **《Calling conventions》**\
  解释 Windows（x64）、Linux/macOS（System V ABI）等平台的函数调用约定、寄存器使用规则、栈帧布局等。

- **《The microarchitecture of Intel, AMD and VIA CPUs》**\
  对各厂商 CPU 微架构的横向对比与深度分析。

> 所有手册均可在其官网免费下载：\
> 👉 <https://www.agner.org/optimize/>
