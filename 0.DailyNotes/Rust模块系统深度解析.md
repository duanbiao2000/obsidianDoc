
# Rust 模块系统

## 一、核心架构与概念

### Rust 模块系统的层次结构 #card
**问题**：请描述 Rust 模块系统的层次结构。
**答案**：
`Workspace` -> `Package` -> `Crate` (Binary/Library) -> `Crate Root` -> `Module Tree` -> `Modules` -> `Items` (Functions, Structs, etc.)

### 核心概念定义
什么是 Workspace？::一个由多个互相关联的包（Package）组成的集合，用于组织大型项目。
什么是 Package？::一个功能单元，包含一个或多个 Crate，并且由一个 `Cargo.toml` 文件定义。
一个 Package 最多可以包含多少个 Library Crate？::最多一个。
一个 Package 可以包含多少个 Binary Crate？::任意数量。
什么是 Crate Root？::模块树的根节点，通常是 `src/lib.rs`（对于库 Crate）或 `src/main.rs`（对于二进制 Crate）。
模块（Module）在 Rust 中的主要用途是什么？::作为代码组织单元，用于{封装}和{隐私控制}。

## 二、包与 Crate

### 包结构
一个标准的 Rust 包（Package）通常包含哪些核心文件和目录？::
- `Cargo.toml`: 包定义文件
- `src/`: 源代码目录
- `src/main.rs`: 默认的二进制 Crate 根
- `src/lib.rs`: 默认的库 Crate 根

### Cargo 命令
创建一个新的库包（Library Package）的 Cargo 命令是什么？::`cargo new <package_name> --lib`
如何在一个已有的包中添加一个新的二进制 Crate？::在 `src/bin/` 目录下创建一个新的 `.rs` 文件。
如何将多个独立的包组织成一个 Workspace？::在项目根目录创建一个 `Cargo.toml` 文件，并在其中定义 `[workspace]` 和 `members` 列表。

## 三、模块树与路径

### 路径类型与使用场景
### 绝对路径 vs 相对路径 #card
**问题**：在 Rust 中，绝对路径和相对路径（包括 `super`）各自推荐的使用场景是什么？
**答案**：
-   **跨模块访问**：推荐使用 **绝对路径** (`crate::...`)，因为其清晰明确。
-   **同模块内访问**：推荐使用 **相对路径** (`self::...` 或直接写子模块名)，因为其简洁。
-   **访问父模块**：推荐使用 **`super`**，以避免硬编码父模块的名称，方便重构。

### 路径关键字
在模块路径中，`crate` 关键字代表什么？::代表当前 Crate 的根。
在模块路径中，`self` 关键字代表什么？::代表当前模块。
在模块路径中，`super` 关键字代表什么？::代表当前模块的父模块。

## 四、隐私规则

### 默认可见性
在 Rust 中，模块内定义的项（如函数、结构体）的默认可见性是什么？::默认是 **私有的**（private），只在当前模块及其子模块中可见。

### `pub` 关键字
如何使一个结构体的字段也变为公共可见？::必须在字段前也使用 `pub` 关键字，例如 `pub struct Point { pub x: i32, pub y: i32 }`。
如果一个枚举是公共的（`pub enum`），它的变体（variants）的可见性是什么？::默认与枚举本身的可见性相同，即也是公共的。

### 受限可见性
`pub(crate)` 的含义是什么？::使一个项在整个 Crate 内部可见，但在 Crate 外部是私有的。
`pub(in path)` 的含义是什么？::使一个项在指定的路径（`path`）内可见。
`pub(super)` 的含义是什么？::使一个项在父模块中可见。

### 隐私设计原则
什么是“最小暴露原则”？::只将绝对必要的部分作为公共 API 暴露出去，其余所有实现细节都应保持私有。

## 五、`use` 语句

### `use` 语句最佳实践
### 函数 vs 类型导入 #card
**问题**：使用 `use` 语句时，导入函数和导入类型（如 Struct、Enum）的最佳实践有何不同？
**答案**：
-   **函数**：推荐导入其 **父模块**，调用时使用 `module::function()` 的形式，以明确其来源。
-   **类型**：推荐导入其 **完整路径**，可以直接使用类型名，如 `HashMap`。

### 解决命名冲突
当引入的两个不同模块的项名称相同时，如何解决命名冲突？::有两种主要方法：
1.  导入父模块，通过 `module1::Result` 和 `module2::Result` 区分。
2.  使用 `as` 关键字进行重命名，例如 `use std::io::Result as IoResult;`。

### `use` 反模式
为什么应谨慎使用 `glob` 操作符（`*`）进行导入？::因为它会把模块中所有公共项都引入当前作用域，可能导致命名冲突，并使代码的依赖关系变得不明确。

### 重新导出
什么是“重新导出”（re-exporting）？它有什么作用？::使用 `pub use` 语句将一个项引入当前作用域，并使其也成为当前模块公共 API 的一部分。这常用于构建清晰、扁平化的公共 API。

## 六、多文件模块组织

### 文件与模块的对应关系
如果 `lib.rs` 中有 `mod front_of_house;`，编译器会从哪里加载该模块的内容？::它会查找 `src/front_of_house.rs` 文件或 `src/front_of_house/mod.rs` 文件。
如果一个模块 `back_of_house` 拥有子模块，推荐的文件结构是什么？::创建一个 `src/back_of_house/` 目录，并在其中放置一个 `mod.rs` 文件作为 `back_of_house` 模块的声明入口，子模块则作为同级文件（如 `hosting.rs`）。

## 七、企业级实践

### 架构模式
在大型项目中，常见的分层架构是怎样的？::通常分为：
1.  **Public API / Presentation Layer** (最上层)
2.  **Application Layer** (应用逻辑)
3.  **Domain Layer** (核心业务逻辑和模型)
4.  **Infrastructure Layer** (数据库、网络等具体实现)

### 工作区（Workspace）
在超大型项目中，使用 Workspace 管理有什么好处？::
-   **统一依赖管理**：可以在根 `Cargo.toml` 中共享依赖版本。
-   **构建优化**：可以独立或并行构建工作区内的成员。
-   **代码共享**：便于在多个 Crate 之间共享代码（如 `shared-utils` 库）。