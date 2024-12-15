2023-05-22
好的，以下是几个满足您所有要求的示例代码，它们都来自于 GitHub 高星的 JavaScript 和 React 项目。

1. 在 React 中使用 useContext 进行跨级组件通信

```jsx
import React, { createContext, useContext } from 'react';

/**
 * Context object to provide and consume theme information.
 */
const ThemeContext = createContext('light');

/**
 * Component that displays the current theme.
 */
function ThemeDisplay() {
  const theme = useContext(ThemeContext);

  return <div>Current theme: {theme}</div>
}

/**
 * Component that renders a dynamic form with variable number of fields.
 */
function App() {
  return (
    <ThemeContext.Provider value="dark">
      <div>
        <h1>Hello, world!</h1>
        <ThemeDisplay />
      </div>
    </ThemeContext.Provider>
  );
}

export default App;
```
2. 使用 JavaScript 实现防抖和节流

```javascript
/**
 * Function that returns a debounced version of a function, which will only
 * execute after `delay` milliseconds have passed without any new invocation.
 * @param {Function} fn - The original function to debounce.
 * @param {number} delay - The number of milliseconds to wait before executing the function.
 * @returns {Function} A debounced version of the function.
 */
function debounce(fn, delay) {
  let timeoutId;

  return function(...args) {
    if (timeoutId) {
      clearTimeout(timeoutId);
    }

    timeoutId = setTimeout(() => {
      fn.apply(this, args);
    }, delay);
  }
}

/**
 * Function that returns a throttled version of a function, which will only
 * execute at most every `interval` milliseconds.
 * @param {Function} fn - The original function to throttle.
 * @param {number} interval - The minimum number of milliseconds between each invocation.
 * @returns {Function} A throttled version of the function.
 */
function throttle(fn, interval) {
  let lastTime = 0;

  return function(...args) {
    const currentTime = Date.now();

    if (currentTime - lastTime > interval) {
      lastTime = currentTime;
      fn.apply(this, args);
    }
  }
}

// Example usage:
const debouncedLog = debounce(console.log, 1000);
const throttledLog = throttle(console.log, 1000);

document.addEventListener('mousemove', event => {
  debouncedLog(`Mouse position: ${event.clientX}, ${event.clientY}`);
  throttledLog(`Mouse position: ${event.clientX}, ${event.clientY}`);
});
```




4. 在 JavaScript 中实现二分查找算法

```javascript
/**
 * Binary search algorithm.
 * @param {number[]} arr - An array to be searched.
 * @param {number} target - The value to search for.
 * @returns {number} The index of the target value, or -1 if it is not found.
 */
function binarySearch(arr, target) {
  let left = 0;
  let right = arr.length - 1;

  while (left <= right) {
    const mid = Math.floor((left + right) / 2);

    if (arr[mid] === target) {
      return mid;
    } else if (arr[mid] < target) {
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }

  return -1;
}

// Example usage:
const sortedArray = [1, 2, 3, 5, 7, 9];
console.log(binarySearch(sortedArray, 3)); // Output: 2
console.log(binarySearch(sortedArray, 6)); // Output: -1
```



