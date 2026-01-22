---
date: 2025-05-15 18:27
tags:
  - complexity-theory
  - graph-theory
  - algorithm
  - data-structures
source: https://deepwiki.com/kdn251/interviews/
view-count: 7
---

## 1. 复杂度定义 (Complexity)

- **$O$ (Big O)**: 最坏情况 (上界)。
- **$\Theta$ (Big Theta)**: 平均/确界。
- **$\Omega$ (Big Omega)**: 最好情况 (下界)。
- **$o / \omega$**: 严格快于/慢于。

---

## 2. 基础数据结构矩阵 (Data Structures)

| 数据结构 | Access | Search | Insert | Delete | 核心本质 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Array** | $O(1)$ | $O(n)$ | $O(n)$ | $O(n)$ | 连续内存，索引直达 |
| **Linked List** | $O(n)$ | $O(n)$ | $O(1)$ | $O(1)$ | 指针链接，分散存储 |
| **Stack** | $O(n)$ | $O(n)$ | $O(1)$ | $O(1)$ | LIFO (后进先出) |
| **Queue** | $O(n)$ | $O(n)$ | $O(1)$ | $O(1)$ | FIFO (先进先出) |
| **Hash Table** | N/A | $O(1)$ | $O(1)$ | $O(1)$ | 哈希映射，最坏 $O(n)$ |

---

## 3. 树与图 (Trees & Graphs)

### 树分类 (Tree Taxonomy)
- **满二叉树**: 0 或 2 子节点。
- **完美二叉树**: 全满且叶子同深。
- **完全二叉树**: 除底层全满，底层左对齐。
- **BST (二叉搜索树)**: 左 < 根 < 右。平衡时 $O(\log n)$，极端时 $O(n)$。

### 图类型 (Graph Types)
- **无向/有向**: 边是否有箭头。
- **加权**: 边有成本/权重。
- **连通**: 任意两点可达。
- **循环**: 存在回路。

---

## 4. 排序算法 (Sorting)

| 类别 | 算法 | 时间复杂度 (Avg) | 空间复杂度 | 特点 |
| :--- | :--- | :--- | :--- | :--- |
| **In-place** | QuickSort | $O(n \log n)$ | $O(\log n)$ | 分区基准，最坏 $O(n^2)$ |
| **D&C** | MergeSort | $O(n \log n)$ | $O(n)$ | 稳定，稳定分治 |
| **Distribution** | BucketSort | $O(n + k)$ | $O(n)$ | 桶分布，依赖分布均匀 |
| **Distribution** | RadixSort | $O(nk)$ | $O(n + k)$ | 按位排序 (LSD/MSD) |

---

## 5. 图遍历协议 (Traversal)

- **DFS (深度优先)**: 栈/递归。探索深度。用于：路径存在、环检测、拓扑排序。
- **BFS (广度优先)**: 队列。探索广度 (层级)。用于：无权图最短路径、连通分量。

---

## 6. 性能红线 (Complexity Hierarchy)

$O(1) < O(\log n) < O(n) < O(n \log n) < O(n^2) < O(2^n) < O(n!)$

---

**最后更新: 2026-01-01**