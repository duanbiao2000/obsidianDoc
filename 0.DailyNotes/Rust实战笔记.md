---
aliases:
date: 2025-10-05 09:14
tags:
source:
  - https://app.codecrafters.io/courses/
update:
rating:
---

这几个是Rust语言的 crate（类似其他语言的库）：

- `anyhow = "1.0.68"`：专注于简化错误处理的库，提供了灵活的`Result`类型和错误处理宏，适合快速开发时使用，无需手动定义大量错误类型。

- `bytes = "1.3.0"`：用于高效处理字节缓冲区的库，提供了`Bytes`和`BytesMut`等类型，支持零拷贝操作，常用于网络编程和IO操作中管理字节数据。

- `thiserror = "1.0.38"`：用于定义自定义错误类型的库，通过宏简化错误枚举的实现，生成符合Rust最佳实践的错误类型，适合需要精确定义错误种类的场景。

这三个库常结合使用：`thiserror`定义结构化错误，`anyhow`处理动态错误场景，`bytes`则在数据传输相关的错误处理中管理字节数据。
