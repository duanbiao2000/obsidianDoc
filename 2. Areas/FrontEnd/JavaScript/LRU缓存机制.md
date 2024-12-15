---
aliases: 
tags: 
source: 
author: 
<<<<<<< HEAD
date_created: 2024-07-14 17:02
type: 
priority: false
=======
createdAt: 
updateAt: 2024-07-14 17:02
categories: 
status: false
>>>>>>> 93a933e (refactor(dailyNotes): update metadata structure for daily notes)
---
LRU（Least Recently Used）缓存机制是一种常用的缓存淘汰策略，当缓存满时，会优先淘汰最近最少使用的数据。下面是一个使用JavaScript实现的简单LRU缓存类，包括关键代码行内注释以及一个简单的单元测试示例。

### LRU Cache 实现

```javascript
class LRUCache {
    constructor(capacity) {
        // 初始化容量
        this.capacity = capacity;
        // 使用Map来存储键值对，同时利用双向链表维护访问顺序
        this.cache = new Map();
        // 辅助指针，指向最近最少使用的项
        this.tail = null;
        // 辅助指针，指向最常使用的项
        this.head = null;
    }

    /**
     * 获取键对应的值，同时将该键值对移到链表头部，表示最近被访问
     */
    get(key) {
        if (this.cache.has(key)) {
            const value = this.cache.get(key);
            // 移除当前节点
            this.cache.delete(key);
            // 重新插入到头部
            this.put(key, value);
            return value;
        }
        return -1; // 如果key不存在，返回-1
    }

    /**
     * 添加或更新键值对，如果超出容量则删除最老的键值对
     */
    put(key, value) {
        if (this.cache.has(key)) {
            // 如果已经存在，则先删除再添加，确保移到头部
            this.cache.delete(key);
        } else if (this.cache.size === this.capacity) {
            // 如果达到容量上限，删除尾部节点
            this.cache.delete(this.tail.key);
            // 更新尾部指针
            if (this.tail.prev) {
                this.tail = this.tail.prev;
                this.tail.next = null;
            } else {
                // 如果之前只有一个节点，现在为空了
                this.head = null;
                this.tail = null;
            }
        }

        // 创建新节点，并插入到头部
        const newNode = { key, value, prev: null, next: null };
        if (this.head) {
            newNode.next = this.head;
            this.head.prev = newNode;
        }
        this.head = newNode;
        if (!this.tail) {
            this.tail = newNode;
        }
        this.cache.set(key, newNode);
    }
}
```

### 单元测试示例

为了进行单元测试，我们可以使用像Jest这样的测试框架。下面是一个简化的测试用例示例，展示如何测试LRU Cache的基本功能。

```javascript
// 假设已经安装并配置了Jest
const LRUCache = require('./LRUCache'); // 或者是import，取决于你的环境

test('LRU Cache Test', () => {
    const cache = new LRUCache(2);

    cache.put(1, 1);
    cache.put(2, 2);
    expect(cache.get(1)).toBe(1); // 应该返回1
    expect(cache.get(2)).toBe(2); // 应该返回2

    cache.put(3, 3); // 这将使得键1的数据被移除，因为容量为2
    expect(cache.get(1)).toBe(-1); // 应该返回-1，因为1已经被移除
    expect(cache.get(2)).toBe(2); // 应该返回2
    expect(cache.get(3)).toBe(3); // 应该返回3

    cache.put(4, 4); // 现在键2应该被移除
    expect(cache.get(2)).toBe(-1); // 应该返回-1，因为2已经被移除
    expect(cache.get(3)).toBe(3); // 应该返回3
    expect(cache.get(4)).toBe(4); // 应该返回4
});
```

请注意，实际运行上述测试代码前，你需要确保已经安装了Jest，并且根据你的项目配置进行了适当的导入语句调整。