---
aliases:

---
20230717 2222
links:
title:
origin:  React Quickly, Second Edition - MEAP... (Z-Library)
tags: #flashcards #todo 



### P220

下面是对之前提到的Hook分类、用法、作用和使用场景的总结表格：

|Hook分类|用法|作用|使用场景|
|---|---|---|---|
|State Hooks|useState|在函数组件中创建和管理局部状态|用于管理组件的局部状态，例如计数器、表单输入等|
||useReducer|提供更强大的状态管理解决方案，用于处理复杂的状态更新|适用于处理复杂的状态逻辑，例如购物车、游戏状态等|
||useRef|允许组件持有在多次渲染之间保持持久的可变值|用于保存引用、获取 DOM 元素的引用、保存上一次渲染的值等|
|Effect Hooks|useEffect|在组件渲染后执行副作用操作，如数据获取、事件订阅等|适用于处理组件副作用，例如数据请求、订阅、更新文档标题等|
||useLayoutEffect|类似于 useEffect，但在渲染后同步执行，适用于测量元素或执行 DOM 操作等|用于在渲染后立即执行同步操作，例如测量元素尺寸、直接操作 DOM 等|
|Memoization Hooks|useMemo|通过避免重新计算值来进行性能优化，只在依赖项更改时重新计算值|当需要对计算成本较高的值进行缓存，并且只有在依赖项变化时重新计算时使用，例如计算结果、数据转换等|
||useCallback|缓存回调函数，避免不必要的重新渲染，只在依赖项更改时创建新的回调函数|适用于将回调函数作为 prop 传递给子组件，避免子组件不必要的重新渲染，提高性能|
|Library Hooks|useDebugValue|在 React DevTools 中显示自定义 Hook 的标签|用于在开发工具中提供更友好的自定义 Hook 标签，方便调试和理解自定义 Hook 的作用|
||useImperativeHandle|允许父组件访问子组件实例的函数或属性|在父组件中获取子组件的实例，用于调用子组件的方法或获取子组件的数据|
||useInsertionEffect|在组件被插入到 DOM 中时运行副作用|当组件被插入到 DOM 中时，运行一些特定的副作用操作，例如设置焦点、执行动画效果等|
||useSyncExternalStore|将组件的状态与外部数据源同步|当需要与外部数据源进行同步，保持状态一致性时使用，例如使用 WebSocket 更新数据、与服务器同步状态等|




   - `useReducer`: Provides a more powerful state management solution for complex state updates.
   - `useRef`: Allows components to hold a mutable value that persists across renders.
2. Effect Hooks:
   - `useEffect`: Runs side effects after rendering, such as fetching data or subscribing to events.
   - `useLayoutEffect`: Similar to `useEffect`, but runs synchronously after rendering, which can be useful for measuring elements or performing DOM manipulations.
3. Memorization Hooks:
   - `useMemo`: Memorizes a value, recalculating it only if its dependencies change.
   - `useCallback`: Memorizes a callback function, preventing unnecessary re-renders if the dependencies haven't changed.
4. Library Hooks:
   - `useDebugValue`: Displays a label for custom hooks in React DevTools.
   - `useImperativeHandle`: Allows a parent component to access functions or properties of a child component's instance.
   - `useInsertionEffect`: Runs an effect only when a component is inserted into the DOM.
   - `useSyncExternalStore`: Synchronizes a component's state with an external data source.


1. State Hooks:
- `useReducer`: Manages state transitions based on actions.
  ```jsx
  import React, { useReducer } from 'react';
  const initialState = { count: 0 };
  function reducer(state, action) {
    switch (action.type) {
      case 'increment':
        return { count: state.count + 1 };
      case 'decrement':
        return { count: state.count - 1 };
      default:
        throw new Error();
    }
  }
  function Counter() {
    const [state, dispatch] = useReducer(reducer, initialState);
    return (
      <div>
        <p>Count: {state.count}</p>
        <button onClick={() => dispatch({ type: 'increment' })}>Increment</button>
        <button onClick={() => dispatch({ type: 'decrement' })}>Decrement</button>
      </div>
    );
  }
  export default Counter;
  ```
2. Effect Hooks:
- `useEffect`: Performs side effects after rendering.
  ```jsx
  import React, { useState, useEffect } from 'react';
  function Timer() {
    const [seconds, setSeconds] = useState(0);
    useEffect(() => {
      const interval = setInterval(() => {
        setSeconds((prevSeconds) => prevSeconds + 1);
      }, 1000);
      return () => clearInterval(interval);
    }, []);
    return <div>Seconds: {seconds}</div>;
  }
  export default Timer;
  ```
3. Memoization Hooks:
- `useMemo`: Memorizes a value based on dependencies.
  ```jsx
  import React, { useMemo } from 'react';
  function ExpensiveCalculation({ a, b }) {
    const result = useMemo(() => {
      console.log('Performing expensive calculation...');
      return a + b;
    }, [a, b]);
    return <div>Result: {result}</div>;
  }
  export default ExpensiveCalculation;
  ```
- `useCallback`: Memorizes a callback function.
  ```jsx
  import React, { useState, useCallback } from 'react';
  function Parent() {
    const [count, setCount] = useState(0);
    const increment = useCallback(() => {
      setCount((prevCount) => prevCount + 1);
    }, []);
    return (
      <div>
        <Child increment={increment} />
        <p>Count: {count}</p>
      </div>
    );
  }
  function Child({ increment }) {
    return <button onClick={increment}>Increment</button>;
  }
  export default Parent;
  ```


1. `useReducer`:
   - Use `useReducer` when you have complex state updates that require multiple actions.
   - Separate the reducer function from the component to keep the code organized and maintainable.
2. `useRef`:
   - Use `useRef` when you need to store mutable values that persist across renders.
   - Avoid using `useRef` as a replacement for state unless you specifically need the persistence across renders.
3. Effect Hooks (`useEffect` and `useLayoutEffect`):
   - Use `useEffect` for most cases of running side effects after rendering.
   - Use `useLayoutEffect` when you need to perform measurements or DOM manipulations that require synchronous updates.
4. Memoization Hooks (`useMemo` and `useCallback`):
   - Use `useMemo` to memoize a value that is expensive to compute and only needs to be recalculated when dependencies change.
   - Use `useCallback` to memoize a callback function to prevent unnecessary re-renders of child components.
5. Library Hooks:
   - Use `useDebugValue` to provide a custom label for your custom hooks, improving the debugging experience in React DevTools.
   - Use `useImperativeHandle` sparingly, as it breaks encapsulation and can make components harder to understand and maintain.
   - Use `useInsertionEffect` when you need to run an effect only when a component is inserted into the DOM.
   - Use `useSyncExternalStore` when you want to synchronize a component's state with an external data source.

1. `useReducer`:
```jsx
import React, { useReducer } from 'react';
const initialState = { count: 0 };
function reducer(state, action) {
  switch (action.type) {
    case 'increment':
      return { count: state.count + 1 };
    case 'decrement':
      return { count: state.count - 1 };
    default:
      throw new Error();
  }
}
function Counter() {
  const [state, dispatch] = useReducer(reducer, initialState);
  const increment = () => {
    dispatch({ type: 'increment' });
  };
  const decrement = () => {
    dispatch({ type: 'decrement' });
  };
  return (
    <div>
      <p>Count: {state.count}</p>
      <button onClick={increment}>Increment</button>
      <button onClick={decrement}>Decrement</button>
    </div>
  );
}
export default Counter;
```
2. `useRef`:
```jsx
import React, { useRef } from 'react';
function ExampleComponent() {
  const inputRef = useRef();
  const handleButtonClick = () => {
    inputRef.current.focus();
  };
  return (
    <div>
      <input type="text" ref={inputRef} />
      <button onClick={handleButtonClick}>Focus Input</button>
    </div>
  );
}
export default ExampleComponent;
```
3. Effect Hooks (`useEffect` and `useLayoutEffect`):
```jsx
import React, { useEffect, useLayoutEffect, useState } from 'react';
function ExampleComponent() {
  const [count, setCount] = useState(0);
  useEffect(() => {
    // Runs after every render
    console.log('Effect triggered');
    document.title = `Count: ${count}`;
  });
  useLayoutEffect(() => {
    // Runs synchronously after render but before painting
    console.log('Layout effect triggered');
  });
  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>Increment</button>
    </div>
  );
}
export default ExampleComponent;
```
4. Memoization Hooks (`useMemo` and `useCallback`):
```jsx
import React, { useState, useMemo, useCallback } from 'react';
function ExampleComponent() {
  const [count, setCount] = useState(0);
  const expensiveValue = useMemo(() => {
    console.log('Calculating expensive value...');
    return count * 2;
  }, [count]);
  const increment = useCallback(() => {
    setCount(prevCount => prevCount + 1);
  }, []);
  return (
    <div>
      <p>Count: {count}</p>
      <p>Expensive Value: {expensiveValue}</p>
      <button onClick={increment}>Increment</button>
    </div>
  );
}
export default ExampleComponent;
```

1. `useDebugValue`:
```jsx
import React, { useDebugValue, useState } from 'react';
function useCustomHook() {
  const [count, setCount] = useState(0);
  useDebugValue(count > 5 ? 'Count is greater than 5' : 'Count is not greater than 5');
  const increment = () => {
    setCount(prevCount => prevCount + 1);
  };
  return { count, increment };
}
function ExampleComponent() {
  const { count, increment } = useCustomHook();
  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={increment}>Increment</button>
    </div>
  );
}
export default ExampleComponent;
```
2. `useImperativeHandle`:
```jsx
import React, { useRef, useImperativeHandle, forwardRef } from 'react';
const ChildComponent = forwardRef((props, ref) => {
  const inputRef = useRef();
  useImperativeHandle(ref, () => ({
    focusInput: () => {
      inputRef.current.focus();
    }
  }));
  return <input type="text" ref={inputRef} />;
});
function ExampleComponent() {
  const childRef = useRef();
  const handleButtonClick = () => {
    childRef.current.focusInput();
  };
  return (
    <div>
      <ChildComponent ref={childRef} />
      <button onClick={handleButtonClick}>Focus Input</button>
    </div>
  );
}
export default ExampleComponent;
```
3. `useInsertionEffect`:
```jsx
import React, { useInsertionEffect } from 'react';
function ExampleComponent() {
  useInsertionEffect(() => {
    console.log('Component inserted into the DOM');
    return () => {
      console.log('Component removed from the DOM');
    };
  }, []);
  return <div>Example Component</div>;
}
export default ExampleComponent;
```
4. `useSyncExternalStore`:
```jsx
import React, { useState, useEffect } from 'react';
const externalStore = {
  getState: () => ({ count: 0 }),
  subscribe: (callback) => {
    const interval = setInterval(() => {
      callback({ count: Math.floor(Math.random() * 100) });
    }, 1000);
    return () => clearInterval(interval);
  },
};
function ExampleComponent() {
  const [count, setCount] = useState(externalStore.getState().count);
  useEffect(() => {
    const unsubscribe = externalStore.subscribe((state) => {
      setCount(state.count);
    });
    return unsubscribe;
  }, []);
  return <div>Count: {count}</div>;
}
export default ExampleComponent;
```

