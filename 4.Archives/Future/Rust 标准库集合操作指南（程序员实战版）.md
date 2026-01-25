---
view-count: 6
update: 2026-01-09 11:56
related:
  - "[[Rust生产级综合开发技能学习系统提示词模板]]"
  - "[[2025-12-05-Go与Rust的权衡]]"
  - "[[Rust 异步与并发系统学习路径]]"
  - "[[Plan文档比较与实例]]"
  - "[[Prompt管理科学]]"

tags: ["Domain/Technology/Rust", "Type/Reference"]

---
# Rust 集合实战：极简决策手册

### 1. 核心选型决策树

- **连续存储 + 随机访问** $\rightarrow$ `Vec<T>`（90% 场景的首选）
- **唯一性去重**：
  - 不关心顺序 $\rightarrow$ `HashSet<T>`
  - 需要排序/范围查询 $\rightarrow$ `BTreeSet<T>`
- **键值对映射 (Key-Value)**：
  - 追求查找速度 $\rightarrow$ `HashMap<K, V>`
  - 需要按键排序/范围检索 $\rightarrow$ `BTreeMap<K, V>`
- **双端操作队列** $\rightarrow$ `VecDeque<T>`

---

### 2. 性能与安全协议 (The Rules)

#### **内存分配优化**

- **规则**：已知大小时必用 `with_capacity(n)`。
- **收益**：减少内存重分配，均摊 O(1) 变真 O(1)，性能提升 2-3 倍。

#### **访问安全**

- **❌ 禁忌**：`let x = v[i];` （越界即崩溃/Panic）。
- **✅ 推荐**：`v.get(i)` （返回 `Option`，安全处理空值）。

#### **所有权陷阱**

- **Move**：插入集合后所有权转移。需再次使用请传引用或 `clone`。
- **Key 生命周期**：`HashMap` 的 Key 推荐用 `String` 而非 `&str`（除非生命周期明确）。

---

### 3. 极简对比矩阵

| 特性       | Rust (std)        | C++ (STL)        | Go              |
| :------- | :---------------- | :--------------- | :-------------- |
| **安全性**  | 编译期内存安全           | 需手动防越界           | GC 自动管理         |
| **开销**   | 零成本抽象             | 零成本抽象            | GC 运行时开销        |
| **核心工具** | `Vec` / `HashMap` | `vector` / `map` | `slice` / `map` |

---

### 4. 进阶生产建议

- **高性能哈希**：默认 `HashMap` 防 DoS 攻击。追求极限速度改用 `hashbrown` 或 `ahash`。
- **保持插入顺序**：原生 Map 无序。需要按插入顺序迭代请用 `indexmap`。
- **流式转换**：`iter()` $\rightarrow$ `map()` / `filter()` $\rightarrow$ `collect()` 是标准工业链路。

---

### 5. 总结观点

- **选型即性能**：选错结构是最大性能债，微调代码补不回来。
- **安全即生产力**：优先用 `get()` 处理潜在异常，杜绝运行时 Panic。
- **预分配是美德**：在大规模数据面前，不预配容量等同于资源浪费。
