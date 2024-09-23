### Zustand
- **用途**：Zustand 是一个轻量级的状态管理库，用于React应用。它提供了一种简单而强大的方式来管理全局状态。
- **主要功能**：
  - 简洁的API设计，易于上手。
  - 支持自定义中间件（例如用于日志记录、性能监控等）。
  - 高效的状态更新机制。
  - 可以与React Hooks无缝集成。

- **使用示例**：
  ```javascript
  import create from 'zustand';

  const useStore = create(set => ({
    count: 0,
    increase: () => set(state => ({ count: state.count + 1 })),
    decrease: () => set(state => ({ count: state.count - 1 }))
  }));

  // 在组件中使用
  function Counter() {
    const { count, increase, decrease } = useStore();

    return (
      <div>
        <button onClick={decrease}>-</button>
        <span>{count}</span>
        <button onClick={increase}>+</button>
      </div>
    );
  }
  ```
