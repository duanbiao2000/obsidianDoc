Rust 标准库提供了多种常用集合（collections）类型，用于存储和管理多个值。这些集合在堆上分配内存，长度可以动态变化，是处理复杂数据的核心工具。以下是 Rust 中最常用的集合及其特点：


### 1. `Vec<T>`（动态数组）
`Vec<T>` 是最常用的集合类型，代表一个**可动态增长的数组**，存储相同类型的元素，在内存中连续存放。

**特点**：
- 随机访问速度快（O(1) 时间复杂度）
- 尾部插入/删除效率高（O(1)）
- 中间插入/删除效率低（需要移动元素，O(n)）

**基本用法**：
```rust
use std::vec;

// 创建 Vec
let mut numbers = vec![1, 2, 3];  // 字面量创建
let mut words = Vec::new();       // 空 Vec

// 添加元素
words.push("hello");
words.push("world");

// 访问元素（两种方式）
let first = numbers[0];               // 直接索引（越界会 panic）
let second = numbers.get(1).unwrap();  // get 方法（返回 Option<T>，安全）

// 迭代
for num in &numbers {
    println!("{}", num);
}

// 修改元素
numbers[2] = 100;
```


### 2. `String` 与 `&str`（字符串）
Rust 中字符串有两种形式：`String`（可增长的堆分配字符串）和 `&str`（字符串切片，不可变）。

**特点**：
- `String` 是 `Vec<u8>` 的包装，但保证存储 UTF-8 编码的文本
- 支持动态修改（拼接、插入等）
- 字符串切片 `&str` 是对字符串数据的引用，通常作为函数参数使用

**基本用法**：
```rust
// 创建 String
let mut s = String::new();
s.push_str("hello");  // 拼接字符串切片
let s2 = "world".to_string();  // 从 &str 转换

// 拼接
let s3 = s + &s2;  // s 被移动，之后不可再使用
let s4 = format!("{} {}", "hello", "world");  // 安全拼接，不移动原字符串

// 访问（注意：不能直接索引，需通过字符迭代）
for c in s4.chars() {
    println!("{}", c);
}
```


### 3. `HashMap<K, V>`（哈希表）
`HashMap<K, V>` 存储键值对（key-value pairs），通过哈希函数实现快速查找，适用于需要通过键快速访问值的场景。

**特点**：
- 查找、插入、删除的平均时间复杂度为 O(1)
- 键（K）必须实现 `Hash` 和 `Eq` trait
- 元素无序存储（Rust 1.53+ 可通过 `HashMap::into_iter_sorted` 排序）
<!--ID: 1761111101490-->


**基本用法**：
```rust
use std::collections::HashMap;

// 创建 HashMap
let mut scores = HashMap::new();

// 插入键值对
scores.insert(String::from("Alice"), 90);
scores.insert(String::from("Bob"), 85);

// 访问值
let alice_score = scores.get("Alice");  // 返回 Option<&V>

// 迭代
for (name, score) in &scores {
    println!("{}: {}", name, score);
}

// 更新值
scores.insert(String::from("Alice"), 95);  // 覆盖已有值
scores.entry(String::from("Charlie")).or_insert(70);  // 不存在则插入默认值
```


### 4. `HashSet<T>`（哈希集合）
`HashSet<T>` 是基于 `HashMap` 的集合类型，仅存储唯一元素（无重复），本质是 `HashMap<T, ()>` 的包装。

**特点**：
- 元素唯一，插入重复值会被忽略
- 查找、插入、删除效率高（O(1) 平均）
- 元素无序

**基本用法**：
```rust
use std::collections::HashSet;

let mut fruits = HashSet::new();

// 插入元素
fruits.insert("apple");
fruits.insert("banana");
fruits.insert("apple");  // 重复插入，无效果

// 检查是否包含元素
if fruits.contains("banana") {
    println!("Has banana!");
}

// 迭代
for fruit in &fruits {
    println!("{}", fruit);
}
```


### 5. `BTreeMap<K, V>`（有序映射）
`BTreeMap<K, V>` 基于 B 树实现，存储有序的键值对，键需要实现 `Ord` trait。

**特点**：
- 元素按键的自然顺序排序
- 查找、插入、删除的时间复杂度为 O(log n)
- 适合需要范围查询的场景（如查找某一区间的键）

**基本用法**：
```rust
use std::collections::BTreeMap;

let mut map = BTreeMap::new();
map.insert(3, "three");
map.insert(1, "one");
map.insert(2, "two");

// 迭代（自动按键排序）
for (key, value) in &map {
    println!("{}: {}", key, value);  // 输出：1: one, 2: two, 3: three
}

// 范围查询
let range = map.range(1..=2);  // 获取键 1 到 2 的元素
```


### 6. `BTreeSet<T>`（有序集合）
`BTreeSet<T>` 基于 `BTreeMap` 实现，存储唯一且有序的元素，元素需要实现 `Ord` trait。

**特点**：
- 元素自动排序且唯一
- 适合需要有序遍历或范围查询的场景

**基本用法**：
```rust
use std::collections::BTreeSet;

let mut numbers = BTreeSet::new();
numbers.insert(3);
numbers.insert(1);
numbers.insert(2);

// 迭代（自动排序）
for num in &numbers {
    println!("{}", num);  // 输出：1, 2, 3
}
```


### 集合的选择指南
- 需动态数组且随机访问 → `Vec<T>`
- 需键值对且无序快速访问 → `HashMap<K, V>`
- 需键值对且有序/范围查询 → `BTreeMap<K, V>`
- 需唯一元素且无序 → `HashSet<T>`
- 需唯一元素且有序 → `BTreeSet<T>`
- 需字符串操作 → `String`（动态）或 `&str`（切片）


# Rust集合类型完全指南：从基础到实战

## 🎯 核心概念

Rust集合类型是**堆上分配**的动态数据结构，提供类型安全和内存安全的集合操作。

## 📋 六大核心集合

### **1. Vec- 动态数组**
```rust
use std::vec;

// 创建方式
let mut vec1 = vec![1, 2, 3];           // 宏创建
let mut vec2 = Vec::new();              // 空向量
let mut vec3: Vec<i32> = Vec::with_capacity(10); // 预分配容量

// 常用操作
vec1.push(4);                           // 尾部添加
vec1.pop();                             // 尾部删除
let element = vec1[0];                  // 索引访问（panic on bounds error）
let element = vec1.get(0);              // 安全访问（Option<T>）

// 性能特点
// - 随机访问: O(1)
// - 尾部操作: O(1) 
// - 中间操作: O(n)
```

### **2. String & &str - 字符串类型**
```rust
// String vs &str
let owned_string = String::from("hello");    // 堆分配，可变
let string_slice = "world";                  // 静态，不可变引用

// 字符串操作
let mut s = String::new();
s.push_str("hello");
s.push('!');                                 // 单字符

// 字符串拼接
let s1 = String::from("hello");
let s2 = String::from("world");
let s3 = format!("{} {}", s1, s2);          // 不移动原字符串
let s4 = s1 + &s2;                           // s1被移动

// 字符遍历（不能直接索引）
for c in s3.chars() {
    println!("{}", c);
}
```

### **3. HashMap<K, V> - 哈希映射**
```rust
use std::collections::HashMap;

// 创建和基本操作
let mut map = HashMap::new();
map.insert("key1", 100);
map.insert("key2", 200);

// 访问和更新
let value = map.get("key1");                 // Option<&V>
map.entry("key3").or_insert(300);            // 不存在则插入
*map.get_mut("key1").unwrap() = 150;         // 修改值

// 性能特点
// - 查找/插入/删除: O(1) 平均
// - 需要 K: Hash + Eq
// - 元素无序
```

### **4. HashSet - 哈希集合**
```rust
use std::collections::HashSet;

let mut set = HashSet::new();
set.insert(1);
set.insert(2);
set.insert(1);                               // 重复插入被忽略

// 集合操作
if set.contains(&1) {
    println!("Contains 1");
}

// 集合运算
let set2: HashSet<i32> = [2, 3, 4].iter().cloned().collect();
let intersection: HashSet<i32> = set.intersection(&set2).cloned().collect();
```

### **5. BTreeMap<K, V> - 有序映射**
```rust
use std::collections::BTreeMap;

let mut ordered_map = BTreeMap::new();
ordered_map.insert(3, "three");
ordered_map.insert(1, "one");
ordered_map.insert(2, "two");

// 自动按键排序
for (key, value) in &ordered_map {
    println!("{}: {}", key, value);          // 输出: 1:one, 2:two, 3:three
}

// 范围查询
let range = ordered_map.range(1..=2);        // 获取范围内的键值对
```

### **6. BTreeSet - 有序集合**
```rust
use std::collections::BTreeSet;

let mut ordered_set = BTreeSet::new();
ordered_set.insert(3);
ordered_set.insert(1);
ordered_set.insert(2);

// 自动排序遍历
for item in &ordered_set {
    println!("{}", item);                    // 输出: 1, 2, 3
}
```

## ⚡ 性能对比表

| 集合类型 | 访问复杂度 | 插入复杂度 | 空间效率 | 排序 | 适用场景 |
|---------|-----------|-----------|---------|------|----------|
| Vec<T> | O(1) | O(1)尾部 | 高 | 有序 | 动态数组 |
| HashMap<K,V> | O(1) | O(1) | 中 | 无序 | 键值映射 |
| HashSet<T> | O(1) | O(1) | 中 | 无序 | 唯一元素 |
| BTreeMap<K,V> | O(log n) | O(log n) | 低 | 有序 | 有序映射 |
| BTreeSet<T> | O(log n) | O(log n) | 低 | 有序 | 有序集合 |

## 🎯 选择指南

### **决策树**
```rust
// 1. 需要动态数组？
//   → 随机访问多？ → Vec<T>
//   → 字符串操作？ → String

// 2. 需要键值对？
//   → 需要快速查找？ → HashMap<K, V>
//   → 需要排序？ → BTreeMap<K, V>

// 3. 需要唯一元素？
//   → 快速操作？ → HashSet<T>
//   → 需要排序？ → BTreeSet<T>
```

### **实际应用示例**
```rust
// Web应用中的用户管理
use std::collections::{HashMap, HashSet};
<!--ID: 1761111101508-->


struct UserManager {
    users: HashMap<String, User>,
    active_sessions: HashSet<String>,
}

impl UserManager {
    fn new() -> Self {
        UserManager {
            users: HashMap::new(),
            active_sessions: HashSet::new(),
        }
    }
    
    fn add_user(&mut self, username: String, user: User) {
        self.users.insert(username, user);
    }
    
    fn login(&mut self, username: &str) -> bool {
        if self.users.contains_key(username) {
            self.active_sessions.insert(username.to_string());
            true
        } else {
            false
        }
    }
}

// 配置管理 - 有序配置
use std::collections::BTreeMap;

struct Config {
    settings: BTreeMap<String, String>,
}

impl Config {
    fn get_sorted_keys(&self) -> Vec<&String> {
        self.settings.keys().collect()
    }
}
```

## 🔧 高级用法

### **迭代器优化**
```rust
use std::collections::HashMap;

// 高效的数据转换
let numbers = vec![1, 2, 3, 4, 5];
let squared: Vec<i32> = numbers.iter()
    .map(|x| x * x)
    .collect();

// HashMap的函数式操作
let mut map = HashMap::new();
for i in 0..10 {
    *map.entry(i % 3).or_insert(0) += 1;
}
```

### **内存优化**
```rust
// 预分配容量
let mut vec = Vec::with_capacity(1000);      // 避免频繁重分配
let mut string = String::with_capacity(100); // 预分配字符串容量

// HashMap的容量控制
let mut map = HashMap::with_capacity(100);
```

## 💡 最佳实践

### **性能优化**
```rust
// 1. Vec预分配容量
fn create_large_vec(n: usize) -> Vec<i32> {
    let mut vec = Vec::with_capacity(n);  // 避免多次重分配
    for i in 0..n {
        vec.push(i as i32);
    }
    vec
}

// 2. HashMap避免重复查找
fn update_scores(scores: &mut HashMap<String, i32>, updates: &[(String, i32)]) {
    for (name, score) in updates {
        *scores.entry(name.clone()).or_insert(0) += score;  // 单次查找
    }
}
```

### **错误处理**
```rust
// 安全的数组访问
fn safe_access<T: Clone>(vec: &Vec<T>, index: usize) -> Option<T> {
    vec.get(index).cloned()
}

// HashMap的安全操作
fn get_or_default<K: Eq + std::hash::Hash + Clone, V: Clone>(
    map: &HashMap<K, V>, 
    key: &K, 
    default: V
) -> V {
    map.get(key).cloned().unwrap_or(default)
}
```

## 📝 总结

Rust集合类型提供了：
✅ **类型安全**：编译时类型检查  
✅ **内存安全**：运行时边界检查  
✅ **性能优化**：针对不同场景的最优实现  
✅ **功能完整**：覆盖所有常见集合操作需求  

**选择原则**：根据访问模式、性能要求和功能需求选择最适合的集合类型。