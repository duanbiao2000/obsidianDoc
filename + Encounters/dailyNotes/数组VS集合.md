---
aliases:
source:
author:
createdAt:
updateAt:
categories:
high_priority: false
tags:
---
## Java 中数组、集合以及列表的区别

在 Java 中，数组、集合和列表是存储数据的常用数据结构，它们各有特点，适用于不同的场景。

### 数组（Array）

- **特点：**
  - 长度固定：一旦创建，数组的长度就不能改变。
  - 元素类型相同：数组只能存储同一种类型的数据。
  - 访问效率高：通过索引可以直接访问数组元素，效率很高。
- **使用场景：**
  - 需要固定长度的元素集合。
  - 频繁访问元素，对访问效率要求较高。
  - 元素类型已知且不会改变。

### 集合（Collection）

- **特点：**
  - 长度可变：集合的大小可以动态调整。
  - 元素类型可以不同（泛型）：可以通过泛型指定集合元素的类型。
  - 提供丰富的操作：集合提供了多种操作方法，如添加、删除、查找等。
- **主要接口：**
  - **List:** 有序的集合，允许重复元素，可以通过索引访问元素。常见实现类有 ArrayList、LinkedList。
  - **Set:** 无序的集合，不允许重复元素。常见实现类有 HashSet、TreeSet。
  - **Map:** 键值对的集合，键是唯一的。常见实现类有 HashMap、TreeMap。

### 列表（List）

- **特点：**
  - List 是 Collection 接口的一个子接口。
  - 有序的集合，元素可以重复。
  - 可以通过索引访问元素。
- **常见实现类：**
  - **ArrayList:** 基于动态数组实现，随机访问效率高，插入和删除元素效率较低。
  - **LinkedList:** 基于双向链表实现，插入和删除元素效率高，随机访问效率较低。

### 总结

|特点|数组|集合（List）|
|---|---|---|
|长度|固定|可变|
|元素类型|相同|可以不同（泛型）|
|有序性|有序|有序|
|允许重复元素|允许|允许|
|访问方式|索引|索引或迭代器|
|常用操作|访问、赋值|添加、删除、查找、排序等|

### 选择哪个？

- **数组：** 适合存储固定数量的同类型元素，且频繁访问元素的场景。
- **List：** 适合存储有序的元素集合，需要频繁插入、删除元素的场景。
  - **ArrayList：** 随机访问频繁，插入删除较少。
  - **LinkedList：** 插入删除频繁，随机访问较少。
- **Set：** 适合存储无序且不重复的元素。
- **Map：** 适合存储键值对。

**示例：**

Java

```
// 数组
int[] scores = new int[5];

// List
List<String> names = new ArrayList<>();
names.add("Alice");
names.add("Bob");

// Set
Set<Integer> numbers = new HashSet<>();
numbers.add(1);
numbers.add(2);
```

**何时选择哪个？**

- **性能：** 如果对性能要求很高，且元素数量确定，数组是更好的选择。
- **灵活性：** 如果需要动态添加或删除元素，集合更适合。
- **去重：** 如果需要保证元素不重复，Set 是更好的选择。
- **键值对：** 如果需要存储键值对，Map 是更好的选择。

**总结来说，数组和集合各有优缺点，选择哪种数据结构取决于具体的应用场景。**
