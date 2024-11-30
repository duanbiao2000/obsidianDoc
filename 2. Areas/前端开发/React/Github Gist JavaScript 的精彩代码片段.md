---
date_created: 2024-08-03 10:02
---

好的，以下是另外 10 处 Github Gist 中 JavaScript 的精彩代码片段及详细解释：

1. 手写 Promise

```javascript
function MyPromise(fn) {
  const self = this;
  self.value = null;
  self.error = null;
  self.onFulfilled = null;
  self.onRejected = null;
  function resolve(value) {
    self.value = value;
    self.onFulfilled(self.value);
  }
  function reject(error) {
    self.error = error;
    self.onRejected(self.error);
  }
  fn(resolve, reject);
}
MyPromise.prototype.then = function(onFulfilled, onRejected) {
  const self = this;
  self.onFulfilled = onFulfilled;
  self.onRejected = onRejected;
};
```

这是一个手写 Promise 的示例，用于演示 Promise 的基本原理。Promise 是一种异步编程解决方案，用于处理异步操作的返回值。在上述代码中，MyPromise 是一个 Promise 构造函数，它接收一个函数作为参数，该函数接收 resolve 和 reject 两个回调函数作为参数。MyPromise.prototype.then 方法用于注册 Promise 的回调函数。
2. 手写 AJAX

```javascript
function ajax(method, url, data) {
  const xhr = new XMLHttpRequest();
  xhr.open(method, url, true);
  xhr.setRequestHeader('Content-Type', 'application/json');
  xhr.onreadystatechange = function() {
    if (this.readyState === 4 && this.status === 200) {
      const response = JSON.parse(this.responseText);
      console.log(response);
    }
  };
  xhr.send(JSON.stringify(data));
}
ajax('POST', '/api', { foo: 'bar' });
```

这是一个手写 AJAX 的示例，用于演示 AJAX 的基本原理。AJAX 是一种异步通信技术，用于在不刷新页面的情况下向服务器发送请求和接收响应。在上述代码中，ajax 函数接收请求方法、请求地址和请求数据三个参数，通过 XMLHttpRequest 对象发送异步请求，并在 onreadystatechange 事件中获取服务器响应。
3. 函数柯里化

```javascript
function add(x) {
  return function(y) {
    return x + y;
  };
}
const add5 = add(5);
console.log(add5(3)); // 8
```

函数柯里化是一种将多个参数的函数转换为一系列单参数函数的技术。在上述代码中，add 函数接收一个参数 x，并返回一个新的函数，该函数接收一个参数 y，并返回 x + y 的结果。通过 add(5) 可以得到一个新的 add5 函数，该函数可以直接传入一个参数 y 并返回相应的结果。
4. 防抖

```javascript
function debounce(fn, delay) {
  let timer;
  return function() {
    const args = arguments;
    clearTimeout(timer);
    timer = setTimeout(() => {
      fn.apply(this, args);
    }, delay);
  };
}
function handleResize() {
  console.log(window.innerWidth);
}
window.addEventListener('resize', debounce(handleResize, 200));
```

防抖是一种限制函数调用频率的技术，用于在连续触发事件时只执行最后一次。在上述代码中，debounce 函数接收一个函数和一个延迟时间作为参数，返回一个新的函数。当事件触发时，debounce 函数会清除之前的计时器并创建一个新的计时器，在延迟时间之后执行函数。
5. 节流

```javascript
function throttle(fn, delay) {
  let timer;
  return function() {
    if (!timer) {
      const args = arguments;
      timer = setTimeout(() => {
        fn.apply(this, args);
        timer = null;
      }, delay);
    }
  };
}
function handleScroll() {
  console.log(window.pageYOffset);
}
window.addEventListener('scroll', throttle(handleScroll, 200));
```

节流是一种限制函数调用频率的技术，用于在连续触发事件时间隔一定时间执行一次。在上述代码中，throttle 函数接收一个函数和一个间隔时间作为参数，返回一个新的函数。当事件触发时，throttle 函数会创建一个计时器，在间隔时间之后执行函数。

> [!NOTE] 防抖VS节流
> - **防抖（Debouncing）**：在事件停止触发一定时间后才执行回调函数。如果事件在计时器结束前再次触发，则重新计时。适用于需要等待用户操作完成后再执行的场景。
> - **节流（Throttling）**：在固定时间间隔内只执行一次回调函数。适用于需要限制事件处理频率的场景。

6. 闭包实现私有变量

```javascript
function Counter() {
  let count = 0;
  return {
    increment() {
      count++;
    },
    getCount() {
      return count;
    }
  };
}
const counter = Counter();
counter.increment();
counter.increment();
console.log(counter.getCount()); // 2
```

闭包是一种在函数内部创建变量，并使其在函数外部可访问的机制。在上述代码中，Counter 函数返回一个对象，该对象中包含 increment 和 getCount 两个方法。由于 count 变量被定义在 Counter 函数内部，因此只能通过返回的对象中的方法访问。
7. Promise.all 实现并行请求

```javascript
const promises = [
  fetch('/api/user'),
  fetch('/api/posts'),
  fetch('/api/comments')
];
Promise.all(promises)
  .then(([user, posts, comments]) => {
    console.log(user);
    console.log(posts);
    console.log(comments);
  })
  .catch(error => {
    console.error(error);
  });
```

Promise.all 是一种在多个 Promise 对象都成功时才执行的技术，用于实现并行请求。在上述代码中，promises 数组中包含三个 fetch 请求，通过 Promise.all 包装后可以并行执行这三个请求。当所有请求都成功时，then 方法中的回调函数会接收到三个响应对象。
8. 手写发布订阅模式

```javascript
function EventEmitter() {
  this.events = {};
}
EventEmitter.prototype.on = function(eventName, listener) {
  if (!this.events[eventName]) {
    this.events[eventName] = [];
  }
  this.events[eventName].push(listener);
};
EventEmitter.prototype.emit = function(eventName, ...args) {
  if (this.events[eventName]) {
    this.events[eventName].forEach(listener => {
      listener.apply(this, args);
    });
  }
};
const emitter = new EventEmitter();
emitter.on('click', function(e) {
  console.log(e);
});
emitter.emit('click', { target: 'button' });
```

发布

当然，我可以为您提供十个React Hooks的代码示例。请注意，这些示例是为了帮助您了解React Hooks的用法，并不一定适用于所有情况。在实际项目中，请根据具体需求进行修改和调整。以下是示例代码：

3. useContext Hook：

```jsx
import React, { useContext } from 'react';
const MyContext = React.createContext();
function Example() {
  const value = useContext(MyContext);
  return <p>Value from context: {value}</p>;
}
```

4. useReducer Hook：

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
function Example() {
  const [state, dispatch] = useReducer(reducer, initialState);
  return (
    <div>
      <p>Count: {state.count}</p>
      <button onClick={() => dispatch({ type: 'increment' })}>Increase Count</button>
      <button onClick={() => dispatch({ type: 'decrement' })}>Decrease Count</button>
    </div>
  );
}
```

5. useCallback Hook：

```jsx
import React, { useState, useCallback } from 'react';
function Example() {
  const [count, setCount] = useState(0);
  const incrementCount = useCallback(() => {
    setCount(count + 1);
  }, [count]);
  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={incrementCount}>Increase Count</button>
    </div>
  );
}
```

6. useMemo Hook：

```jsx
import React, { useState, useMemo } from 'react';
function Example() {
  const [count, setCount] = useState(0);
  const doubleCount = useMemo(() => {
    return count * 2;
  }, [count]);
  return (
    <div>
      <p>Count: {count}</p>
      <p>Double Count: {doubleCount}</p>
      <button onClick={() => setCount(count + 1)}>Increase Count</button>
    </div>
  );
}
```

7. useRef Hook：

```jsx
import React, { useRef } from 'react';
function Example() {
  const inputRef = useRef();
  const handleButtonClick = () => {
    inputRef.current.focus();
  };
  return (
    <div>
      <input ref={inputRef} type="text" />
      <button onClick={handleButtonClick}>Focus Input</button>
    </div>
  );
}
```

8. useLayoutEffect Hook：

```jsx
import React, { useState, useLayoutEffect } from 'react';
function Example() {
  const [width, setWidth] = useState(0);
  useLayoutEffect(() => {
    const handleResize = () => {
      setWidth(window.innerWidth);
    };
    window.addEventListener('resize', handleResize);
    handleResize();
    return () => {
      window.removeEventListener('resize', handleResize);
    };
  }, []);
  return <p>Window width: {width}</p>;
}
```

9. useImperativeHandle Hook：

```jsx
import React, { useRef, useImperativeHandle } from 'react';
function ChildComponent(props, ref) {
  const childRef = useRef();
  useImperativeHandle(ref, () => ({
    focusChildInput: () => {
      childRef.current.focus();
    }
  }));
  return <input ref={childRef} type="text" />;
}
ChildComponent = React.forwardRef(ChildComponent);
function ParentComponent() {
  const childRef = useRef();
  const handleButtonClick = () => {
    childRef.current.focusChildInput();
  };
  return (
    <div>
      <ChildComponent ref={childRef} />
      <button onClick={handleButtonClick}>Focus Child Input</button>
    </div>
  );
}
```

10. Custom Hook:

```jsx
import React, { useState } from 'react';
function useCounter(initialCount) {
  const [count, setCount] = useState(initialCount);
  const increment = () => {
    setCount(count + 1);
  };
  const decrement = () => {
    setCount(count - 1);
  };
  return { count, increment, decrement };
}
function Example() {
  const { count, increment, decrement } = useCounter(0);
  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={increment}>Increase Count</button>
      <button onClick={decrement}>Decrease Count</button>
    </div>
  );
}
```

希望这些示例能帮助您更好地理解React Hooks的用法！如果您有任何问题，请随时提问。

当然，以下是另外五个React Hooks的代码示例，并附带详细的注释说明：

1. useFetch Hook：用于处理异步数据获取

```jsx
import React, { useState, useEffect } from 'react';
function useFetch(url) {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch(url);
        const jsonData = await response.json();
        setData(jsonData);
        setLoading(false);
      } catch (error) {
        console.error(error);
      }
    };
    fetchData();
  }, [url]);
  return { data, loading };
}
function Example() {
  const { data, loading } = useFetch('https://api.example.com/data');
  if (loading) {
    return <p>Loading...</p>;
  }
  return <p>Data: {data}</p>;
}
```

2. useDebounce Hook：用于延迟处理用户输入

```jsx
import React, { useState, useEffect } from 'react';
function useDebounce(value, delay) {
  const [debouncedValue, setDebouncedValue] = useState(value);
  useEffect(() => {
    const handler = setTimeout(() => {
      setDebouncedValue(value);
    }, delay);
    return () => {
      clearTimeout(handler);
    };
  }, [value, delay]);
  return debouncedValue;
}
function Example() {
  const [inputValue, setInputValue] = useState('');
  const debouncedInputValue = useDebounce(inputValue, 500);
  const handleInputChange = (event) => {
    setInputValue(event.target.value);
  };
  return (
    <div>
      <input type="text" value={inputValue} onChange={handleInputChange} />
      <p>Debounced Value: {debouncedInputValue}</p>
    </div>
  );
}
```

3. useLocalStorage Hook：用于在本地存储中保存数据

```jsx
import React, { useState } from 'react';
function useLocalStorage(key, initialValue) {
  const [storedValue, setStoredValue] = useState(() => {
    try {
      const item = window.localStorage.getItem(key);
      return item ? JSON.parse(item) : initialValue;
    } catch (error) {
      console.error(error);
      return initialValue;
    }
  });
  const setValue = (value) => {
    try {
      setStoredValue(value);
      window.localStorage.setItem(key, JSON.stringify(value));
    } catch (error) {
      console.error(error);
    }
  };
  return [storedValue, setValue];
}
function Example() {
  const [name, setName] = useLocalStorage('name', '');
  const handleInputChange = (event) => {
    setName(event.target.value);
  };
  return (
    <div>
      <input type="text" value={name} onChange={handleInputChange} />
      <p>Welcome, {name}!</p>
    </div>
  );
}
```

4. useMedia Hook：用于监听媒体查询

```jsx
import React, { useState, useEffect } from 'react';
function useMedia(query) {
  const [matches, setMatches] = useState(false);
  useEffect(() => {
    const mediaQuery = window.matchMedia(query);
    const handleChange = (event) => {
      setMatches(event.matches);
    };
    mediaQuery.addEventListener('change', handleChange);
    setMatches(mediaQuery.matches);
    return () => {
      mediaQuery.removeEventListener('change', handleChange);
    };
  }, [query]);
  return matches;
}
function Example() {
  const isSmallScreen = useMedia('(max-width: 768px)');
  return (
    <div>
      {isSmallScreen ? (
        <p>Small screen layout</p>
      ) : (
        <p>Large screen layout</p>
      )}
    </div>
  );
}
```

5. useKeyPress Hook：用于捕捉键盘按键事件

```jsx
import React, { useState, useEffect } from 'react';
function useKeyPress(targetKey) {
  const [keyPressed, setKeyPressed] = useState(false);
  const handleKeyDown = (event) => {
    if (event.key === targetKey) {
      setKeyPressed(true);
    }
  };
  const handleKeyUp = (event) => {
    if (event.key === targetKey) {
      setKeyPressed(false);
    }
  };
  useEffect(() => {
    document.addEventListener('keydown', handleKeyDown);
    document.addEventListener('keyup', handleKeyUp);
    return () => {
      document.removeEventListener('keydown', handleKeyDown);
      document.removeEventListener('keyup', handleKeyUp);
    };
  }, [targetKey]);
  return keyPressed;
}
function Example() {
  const isSpacePressed = useKeyPress(' ');
  return (
    <div>
      {isSpacePressed ? (
        <p>Space key is pressed</p>
      ) : (
        <p>Press and hold the space key</p>
      )}
    </div>
  );
}
```

希望这些示例能给您带来更多帮助！如果您还有其他问题，请随时提问。

以下是一个使用类组件生命周期方法来管理状态和副作用的示例：

```javascript
import React, { Component } from "react";
class MyComponent extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data: [],
      isLoading: true
    };
  }
  componentDidMount() {
    // 在组件挂载后，执行异步操作，比如发送网络请求
    fetch("https://api.example.com/data")
      .then(response => response.json())
      .then(data => {
        this.setState({ data: data, isLoading: false });
      })
      .catch(error => {
        console.error(error);
      });
  }
  componentDidUpdate(prevProps, prevState) {
    // 在组件更新后，根据新的props或state执行一些操作
    if (this.props.someProp !== prevProps.someProp) {
      // 执行一些操作
    }
  }
  componentWillUnmount() {
    // 在组件卸载前做一些清理工作，比如取消订阅、清除定时器
    clearInterval(this.timer);
  }
  render() {
    const { data, isLoading } = this.state;
    if (isLoading) {
      return <div>Loading...</div>;
    }
    return (
      <div>
        {data.map(item => (
          <div key={item.id}>{item.name}</div>
        ))}
      </div>
    );
  }
}
export default MyComponent;
```

在上面的示例中，我们使用了类组件`MyComponent`来管理状态和副作用。在`componentDidMount`生命周期方法中，我们发送了一个网络请求来获取数据，并在请求完成后将数据存储在组件的状态中。在`componentDidUpdate`生命周期方法中，我们可以根据新的props或state执行一些操作，这里我们比较了前后两个props来判断是否需要执行一些操作。在`componentWillUnmount`生命周期方法中，我们清除了一个定时器。
在`render`方法中，我们根据组件的状态来渲染UI。当数据正在加载时，显示"Loading..."，加载完成后，展示数据列表。
这是一个简单的示例，演示了如何使用类组件的生命周期方法来管理状态和处理副作用。在实际开发中，你可以根据具体需求和场景来使用不同的生命周期方法来管理状态和副作用。
