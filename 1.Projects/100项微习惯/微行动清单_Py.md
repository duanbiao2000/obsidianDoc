[高产者效率策划表格（Structure–Action–Feedback Loop） - Google Sheets](https://docs.google.com/spreadsheets/d/1a9f8bm1dMUISTiCFW37poJ9xZjym134uoXzYPRZHVPg/edit?gid=597618502#gid=597618502)

好的，我挑选了“手写一个类，重载 `__getitem__` 实现切片操作”这个微行动，写一篇结构清晰、技术深刻的博客文章，内容如下：

---

# 深度解析 Python 中 `__getitem__` 的切片支持及实践体会

在 Python 中，切片（slice）操作是序列类型使用最频繁的特性之一，表现为 `obj[start:stop:step]` 语法。作为一名高级开发者，理解并掌握自定义类如何支持切片操作，是设计兼容 Python 生态的关键能力。本文将围绕“手写一个类，重载 `__getitem__` 实现切片操作”这一微行动，深入解析切片支持的实现原理，并分享我的实践收获。

## 一、`__getitem__` 方法与切片的关系

`__getitem__` 是 Python 中访问容器元素的魔法方法，接收单个参数作为索引。当我们写 `obj[key]` 时，实际调用的是 `obj.__getitem__(key)`。其中，`key` 可以是：

- 整数索引：如 `obj[3]`，传入 `3`
    
- 切片对象：如 `obj[1:5:2]`，传入一个 `slice` 类型实例，等价于 `slice(1, 5, 2)`
    

因此，重载 `__getitem__` 方法时，需要能够识别 `key` 是否为 `slice` 类型，并针对切片对象做相应处理。

## 二、切片对象的内部结构

Python 提供了内置 `slice` 类，包含三个属性：

- `start`：切片起始索引
    
- `stop`：切片结束索引（不包含）
    
- `step`：步长，默认是 1
    

通过访问这些属性，可以实现对切片的细粒度控制。

## 三、实现示例与核心逻辑

以下是一个简单的示例，展示如何在自定义类中实现切片支持：

```python
class MyVector:
    def __init__(self, data):
        self._data = list(data)

    def __getitem__(self, index):
        if isinstance(index, slice):
            return self._data[index.start:index.stop:index.step]
        return self._data[index]
```

此实现通过判断 `index` 是否为 `slice`，直接将切片操作委托给底层列表，从而支持了切片的所有功能，包括负索引和步长为负的反向切片。

## 四、实践收获

1. **深刻理解切片本质**  
    切片实际上是一个标准化的 `slice` 对象，而非语法糖。这种设计使自定义容器可以灵活响应不同切片操作。
    
2. **接口兼容性设计**  
    重用 Python 内置类型（如 `list`）的切片处理逻辑，避免重复造轮子，同时保证行为一致性。
    
3. **边界条件考虑**  
    需要考虑负索引、步长为零或负数的特殊情况，确保切片行为符合预期。
    
4. **扩展空间**  
    可在切片返回结果基础上，添加自定义包装、惰性计算或其他业务逻辑，增强功能灵活性。
    

## 五、总结

通过这次微行动，我不仅巩固了 Python 魔法方法的使用，更深刻理解了切片协议的设计哲学和实践价值。支持切片是自定义序列类型不可或缺的能力，掌握它有助于设计更符合 Python 习惯的高质量组件。未来，我计划基于此扩展，实现完整的序列协议，进一步提升自定义容器的功能与性能。

---

如果你对实现细节或拓展应用有兴趣，欢迎交流探讨！