---
aliases: 📝 Rust编程：掌握所有核心特性！
createdAt: 2024-11-10 20:57
categories:
  - Creative
tags:
  - Creative/Github
  - Creative/Product
---
Rust核心特性初识
<!--more-->

[📝 Rust编程：掌握所有核心特性！\_哔哩哔哩\_bilibili](https://www.bilibili.com/video/BV1XMD2YDEH3/?vd_source=7038f96b6bb3b14743531b102b109c43)

### 详细笔记列表：Rust编程：掌握所有核心特性

#### 1. Rust的特性来源

- Rust从C++、Haskell和JavaScript等语言中借鉴了许多特性，并将其融合成一个单一的杰作。

#### 2. 零成本抽象（Zero Cost Abstractions）
   >
   > "What you don't use you don't pay for, and what you do use you couldn't have hand coded any better."

- Rust的迭代器抽象、Option枚举和模式匹配都是零成本抽象的例子。

#### 3. 所有权模型（Ownership Model）
   >
   > "Ownership is actually based on the Resource Acquisition Is Initialization (RAII) design pattern in C++."

- Rust的所有权规则强制执行资源管理，避免了资源泄漏。

#### 4. 代数数据类型（Algebraic Data Types, ADTs）
   >
   > "ADTs are a type system concept commonly found in functional languages."

- Rust通过枚举和结构体实现ADTs，允许在类型级别上建模复杂数据结构和约束。

#### 5. 模式匹配（Pattern Matching）
   >
   > "Pattern matching in Rust also enforces exhaustiveness, which means all variants of an enum must be handled."

- Rust的模式匹配要求处理枚举的所有变体，防止潜在的运行时错误。

#### 6. 多态性（Polymorphism）

 > "Polymorphism is implemented with traits and generics."
- Rust通过特质（traits）和泛型（generics）实现多态性，避免了传统继承的一些问题。

#### 7. 异步编程（Asynchronous Programming）

> "Async/await syntax for asynchronous program."
- Rust的异步编程模型结合了零成本抽象原则，使得异步代码更易于理解和维护。

#### 8. 宏（Macros）

> "Macros are a language feature that allows developers to define custom syntax and perform code generation or code transformation."
- Rust的宏允许在编译时操纵或生成代码，提供了强大的元编程能力。

#### 9. 包管理（Package Management）

 > "Cargo is Rust's official build system and package manager."
- Rust的Cargo和crates.io提供了可靠的依赖管理和项目构建工具。


## 讲座中的例子

1. **C++中的迭代器抽象**：使用`max_element`函数简化代码。
2. **Rust中的所有权模型**：使用`Option`类型处理空向量的情况。
3. **Haskell中的ADTs**：定义`employee`数据类型，包含`manager`和`worker`变体。
4. **Rust中的ADTs**：使用`enum`实现`employee`类型。
5. **异步编程**：使用`async/await`简化异步代码的编写。
6. **Rust宏**：使用`map`宏创建哈希映射。
7. **Cargo和crates.io**：Rust的包管理和依赖工具。

## 示例代码

根据提供的文本内容，以下是节目中提到的一些代码示例及其解释：

### 1. 零成本抽象（Zero Cost Abstractions）

**Rust 示例**：

```rust
struct DatabaseConnection {
    connection: Connection,
}

impl DatabaseConnection {
    fn new(db_name: &str) -> Self {
        DatabaseConnection {
            connection: open_database(db_name),
        }
    }
}

fn main() {
    let db = DatabaseConnection::new("my_database");
    // 执行数据库操作
}
```

这段Rust代码使用所有权规则自动管理资源，无需显式析构函数。

### 3. 代数数据类型（Algebraic Data Types, ADTs）


**Rust 示例**：

```rust
enum Employee {
    Manager { name: String, subordinates: Vec<Employee> },
    Worker { name: String, manager: Employee },
}
```

这段Rust代码使用枚举实现ADTs，与Haskell类似，但集成了Rust的所有权和借用规则。

### 4. 异步编程（Asynchronous Programming）



**Rust 示例**：

```rust
async fn get_user_data(user_id: u32) -> Result<UserData, Error> {
    let response = reqwest::get(format!("https://api.example.com/users/{}", user_id))
        .await?
        .text()
        .await?;
    Ok(response)
}
```

这段Rust代码使用`async/await`处理异步API调用，错误处理使用`?`操作符。

这些代码示例展示了Rust的核心特性，包括零成本抽象、所有权模型、代数数据类型、异步编程等，以及它们如何在实际代码中应用。
