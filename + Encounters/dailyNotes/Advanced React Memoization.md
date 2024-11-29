---
aliases: 
theme: 
original: 
url: https://www.goodreads.com/book/show/199277807-advanced-react?ref=rae_0
author: 
date_created: 
date_updated: 
type: 
high_priority: false
tags:
---
![image.png](https://cdn.jsdelivr.net/gh/duanbiao2000/BlogGallery@main/picture/20240811123954.png)

## React 中的 re-render（重新渲染）

**React 中的 re-render 指的是当组件的状态（state）或属性（props）发生变化时，React 自动重新执行组件的 render 函数，从而更新 UI 的过程。**

### 为什么会发生 re-render？

- **状态更新 (state change):** 当你调用 `setState` 方法修改组件的状态时，React 会触发 re-render。
- **属性更新 (props change):** 当父组件向子组件传递新的 props 时，子组件也会触发 re-render。
- **父组件 re-render：** 当父组件 re-render 时，它的所有子组件通常也会 re-render。
- **使用了一些会触发 re-render 的 Hooks：** 比如 `useEffect` 在某些情况下会触发组件 re-render。

### re-render 的过程

1. **检测变化：** React 会比较当前的 state 和 props 与上一次渲染时的值，如果发生变化，就会标记组件为需要更新。
2. **执行 render 函数：** React 会重新执行组件的 render 函数，生成新的虚拟 DOM (Virtual DOM)。
3. **Diff 算法：** React 会比较新的虚拟 DOM 与旧的虚拟 DOM，找出差异。
4. **更新 DOM：** React 会高效地更新真实的 DOM，只改变那些有差异的部分，以达到更新 UI 的目的。

### 为什么要 re-render？

- **保持 UI 与数据同步：** 确保用户界面始终反映最新的数据。
- **响应用户交互：** 当用户点击按钮、输入文字等操作时，通过更新 state 来触发 re-render，实现交互。

### 如何优化 re-render？

- **避免不必要的 re-render：**
    - 使用 `React.memo` 或 `useMemo` 优化纯组件和计算结果。
    - 使用 `shouldComponentUpdate` (类组件) 或自定义 Hooks 优化组件的更新逻辑。
- **合理使用 `useEffect`：** 避免在 `useEffect` 中触发不必要的副作用。
- **优化子组件的更新逻辑：** 减少不必要的子组件 re-render。
- **利用 React 的性能优化工具：** 如 React DevTools 可以帮助你分析组件的 re-render 情况。


## Memoization 与 Re-render 的关系

### Memoization 的概念

Memoization 是一种优化技术，它通过缓存函数的返回值，避免重复计算相同参数下的函数结果。在 React 中，Memoization 可以用来优化组件的渲染性能。

### Memoization 与 Re-render 的关联

- **减少不必要的渲染：** 当一个组件的 props 或 state 没有发生变化时，如果这个组件被标记为可记忆化（memoized），React 就会直接返回之前缓存的渲染结果，从而避免不必要的 re-render。
- **提升性能：** 减少 re-render 可以显著提升应用的性能，尤其是对于那些计算开销较大的组件。
- **优化用户体验：** 减少不必要的 UI 更新可以提供更流畅的用户体验。

### React 中的 Memoization
“Memoization”这个单词在中文中可以表达“备忘录法”或“记忆化”。

- **`React.memo`:** 用于优化函数组件。它会对组件进行浅比较，如果 props 没有变化，则返回之前缓存的渲染结果。
- **`useMemo`:** 用于缓存计算结果。它可以缓存任何表达式，只要它的依赖项没有变化。
- **`useCallback`:** 用于缓存回调函数。它可以防止回调函数在每次渲染时都创建新的引用，从而避免不必要的重新渲染。

### 示例

JavaScript

```
import { useState, useMemo } from 'react';

function ExpensiveCalculation() {
  // 模拟一个耗时的计算
  const [count, setCount] = useState(0);
  const result = useMemo(() => {
    console.log('Expensive calculation');
    return expensiveCalculation(count);
  }, [count]);

  return <div>{result}</div>;
}
```

在上面的例子中，`expensiveCalculation` 函数的结果被缓存在了 `result` 中。只有当 `count` 发生变化时，才会重新计算 `result`。

### 注意事项

- **浅比较：** `React.memo` 和 `useMemo` 默认进行浅比较。对于对象和数组，只有当引用发生变化时才会触发重新计算。
- **过度优化：** 过度使用 Memoization 可能会导致代码难以维护。
- **性能分析：** 在优化之前，最好使用性能分析工具来确定哪些组件需要优化。

### 总结

Memoization 和 re-render 是密切相关的两个概念。通过合理使用 Memoization，我们可以有效地减少不必要的 re-render，提升 React 应用的性能。

**总结来说，Memoization 是一种优化手段，通过缓存计算结果，减少不必要的组件渲染，从而提高应用性能。**
