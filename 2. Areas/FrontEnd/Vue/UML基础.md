---
aliases: null
source: null
author: null
createdAt: null
updateAt: 2024-07-17 00:44
categories: null
status: false
theme: null
priority: false
date_created: 2024-12-15 05:28
date_update: null
---

### UML基础

UML（统一建模语言）中常见的元素包括：

1. 类（Class）
2. 对象（Object）
3. 接口（Interface）
4. 枚举（Enumeration）
5. 用例（Use Case）
6. 组件（Component）
7. 节点（Node）
8. 数据库（Database）

其中，类、对象、接口和枚举通常表示软件系统的静态结构，用例表示系统与用户之间的功能需求，组件和节点表示软件系统的物理部署方式，数据库表示软件系统的数据存储机制。

在UML中，这些元素之间的关系包括：

<font color="#92cddc">1. 关联（Association）</font> <font color="#92cddc">2. 泛化（Generalization）</font> <font color="#92cddc">3. 实现（Realization）</font> <font color="#92cddc">4. 依赖（Dependency）</font> <font color="#92cddc">5. 聚合（Aggregation）</font> <font color="#92cddc">6. 组合（Composition）</font>

> 关联表示两个元素之间存在某种联系，泛化表示一个元素是另一个元素的一种特殊形式，实现表示一个元素实现了一个接口，依赖表示一个元素依赖于另一个元素，聚合表示一个元素包含多个其他元素，组合表示一个元素由多个其他元素组成。

1. 关联（Association）：通常用一条直线连接两个元素，并在连线中心位置加上菱形或者箭头，用于表示两个类之间的关系。

2. 泛化（Generalization）：通常用带空心箭头的实线或虚线表示，箭头从具体元素指向更抽象的元素。在类图中，泛化表示继承关系，即一个类继承了另一个类的属性和方法。

3. 实现（Realization）：通常用带空心箭头的虚线表示，箭头从具体元素指向抽象元素。在类图中，实现表示接口的实现关系。

4. 依赖（Dependency）：通常用带箭头的虚线表示，箭头从被依赖元素指向依赖元素。在类图中，依赖表示一个元素依赖于另外一个元素，但是不必须由它创建或管理生存期。

5. 聚合（Aggregation）：通常用带空心菱形的实线表示，菱形连接到整体，并指向部分。在一个聚合关系中，一个整体对象包含了若干个部分对象，但这些部分对象可以独立存在。

6. 组合（Composition）：通常用带实心菱形的实线表示，菱形连接到整体，并指向部分。在一个组合关系中，一个整体对象包含了若干个部分对象，但这些部分对象不能独立存在，与整体对象具有相同的生命周期。
