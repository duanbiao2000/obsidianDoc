---
aliases: []
---
Arrow function箭头函数
箭头函数嵌套写法是指在箭头函数中返回另一个箭头函数的写法。这种写法可以用于创建高阶函数或在函数定义中定义函数。

下面是箭头函数嵌套写法的示例：
```javascript
const outerFunction = (param) => {
  // 返回一个内部的箭头函数
  return (innerParam) => {
    // 内部箭头函数的函数体
    console.log(param, innerParam);
  };
};
// 调用外部函数，返回内部箭头函数
const innerArrowFunction = outerFunction("Hello");
// 调用内部箭头函数
innerArrowFunction("World");
```

在上述示例中，`outerFunction` 是一个外部函数，它接受一个参数 `param`。在外部函数中，返回了一个内部的箭头函数，该箭头函数也接受一个参数`innerParam`。当内部箭头函数被调用时，它会在控制台打印出外部函数的参数 `param` 和内部函数的参数 `innerParam`。

箭头函数嵌套写法可以用于许多场景，例如在高阶函数中创建闭包，或在函数中定义私有函数。

```jsx
const onChange = (key) => (evt) => { #B 
  setData(oldData => ({
    ...oldData, #C 
    [key]: evt.target.value, #D 
    }));
};
```


`evt.target.selectedOptions` 是一个 DOM 属性，用于获取在选择框（`<select>`）中被选中的选项（`<option>`）的集合。
当用户在选择框中选择一个或多个选项时，可以通过访问 `evt.target.selectedOptions` 属性来获取被选中的选项。这个属性返回一个类似数组的对象，包含了被选中的选项元素。
以下是一个简单的示例，展示如何使用 `evt.target.selectedOptions` 属性来获取选中的选项：
```javascript
function handleChange(evt) {
  const selectedOptions = evt.target.selectedOptions;
  
  for (let i = 0; i < selectedOptions.length; i++) {
    console.log(selectedOptions[i].value);
  }
}
// 使用事件监听器来监听选择框的改变事件
const selectElement = document.getElementById("mySelect");
selectElement.addEventListener("change", handleChange);
```


```jsx
import React, { useContext } from 'react';

const MyContext = React.createContext();

// 在某个组件层级中提供上下文值
function App() {
  return (
  <MyContext.Provider value={{ name: 'John', age: 25 }}>
    <ChildComponent />
  </MyContext.Provider>
  );
}

// 在另一个组件中选择访问特定上下文的某些值
function ChildComponent() {
  const { name } = useContext(MyContext);

  return <div>Hello, {name}!</div>;
}

```

```jsx
import { useReducer } from 'react';
// 定义 reducer 函数
function reducer(state, { type }) { // A
  switch (type) {
    case "INCREMENT":
      return state + 1; // B
    case "DECREMENT":
      return state - 1; // B
    default:
      return state;
  }
}
function Counter() {
  // 使用 useReducer 钩子来管理状态和分发动作
  const [counter, dispatch] = useReducer(reducer, 0); // C
  return (
    // 计数器组件的 JSX
    <section>
      <h1>Counter: {counter}</h1>
      <div>
        <button onClick={() => dispatch({ type: "INCREMENT" })}>Increment</button> // D
        <button onClick={() => dispatch({ type: "DECREMENT" })}>Decrement</button> // D
      </div>
    </section>
  );
}
```


```jsx
import { useReducer, useEffect } from 'react';
const URL = 'https://swapi.dev/api/films';
const INITIAL_STATE = {
  status: "INITIALIZE",
  result: null,
  error: null
};
function reducer(state, { type, payload }) {
  switch (type) {
    case "LOADING":
      return {...state, status: "LOADING"}; // 更新状态为加载中
    case "FAILURE":
      return {...state, status: "FAILURE", error: payload}; // 更新状态为失败，并设置错误信息
    case "SUCCESS":
      return {...state, status: "SUCCESS", result: payload}; // 更新状态为成功，并设置返回结果
    default:
      return state;
  }
}
function Loader() {
  const [state, dispatch] = useReducer(reducer, INITIAL_STATE); // 使用 useReducer 管理状态
  useEffect(() => {
    dispatch({ type: "LOADING" }); // 发起请求前，更新状态为加载中
    fetch(URL)
      .then(res => res.json())
      .then(({results}) => dispatch({ type: "SUCCESS", payload: results }) // 请求成功，更新状态为成功，并设置返回结果
      )
      .catch(({message}) => dispatch({ type: "FAILURE", payload: message }) // 请求失败，更新状态为失败，并设置错误信息
      );
  }, []);
  const { status, error, result } = state; // 获取状态的各个属性
  if (status === "INITIALIZE") {
    return <h1>Initializing...</h1>; // 初始状态，显示初始化中
  }
  if (status === "LOADING") {
    return <h1>Loading...</h1>; // 加载中，显示加载中
  }
  if (status === "FAILURE") {
    return <h1>Error occurred: {error}</h1>; // 请求失败，显示错误信息
  }
  return (
    <>
      <h1>Results are in</h1> // 请求成功，显示结果标题
      <ul>
        {result.map(({ title }) => (
          <li key={title}>{title}</li> // 显示结果列表
        ))}
      </ul>
    </>
  );
}
```

---
不可以，将 `contextValue[property]` 改为 `contextValue.property` 是不正确的写法。
在 JavaScript 中，当我们想要通过变量来访问对象的属性时，我们需要使用方括号（`[]`）的语法来进行属性的动态访问。而使用点号（`.`）语法只能用于访问对象属性的字面量名称。
在给定的代码中，`contextValue` 是一个对象，在访问属性时应该使用方括号语法来传递变量或属性名称。因此，正确的写法是使用 `contextValue[property]`。
所以，您应该保留原始代码中的 `contextValue[property]`，而不是将其改为 `contextValue.property`。

---
在 React 中，渲染图标有多种方法。以下是一些常见的方法：
1. 使用图标字体库（Icon Font Library）：引入图标字体库，例如 Font Awesome、Material Icons 或 Ionicons，然后通过在元素中使用相应的类名来渲染图标。
```jsx
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faCoffee } from '@fortawesome/free-solid-svg-icons';
function MyComponent() {
  return (
    <div>
      <FontAwesomeIcon icon={faCoffee} />
    </div>
  );
}
```
2. 使用 SVG 图标：将 SVG 图标文件导入为 React 组件，并在 JSX 中直接使用该组件来渲染图标。
```jsx
import { ReactComponent as Logo } from './logo.svg';
function MyComponent() {
  return (
    <div>
      <Logo />
    </div>
  );
}
```
3. 使用第三方 React 图标库：引入第三方的 React 图标库，例如 react-icons，然后通过使用相应的组件来渲染图标。
```jsx
import { FaCoffee } from 'react-icons/fa';
function MyComponent() {
  return (
    <div>
      <FaCoffee />
    </div>
  );
}
```
4. 使用 CSS 样式：使用 CSS 样式来渲染图标，例如使用 `background-image` 或 `::before` 伪元素来显示图标。
```jsx
import './icon.css';
function MyComponent() {
  return (
    <div className="icon"></div>
  );
}
```
这些方法中的每一种都有其自己的优势和适用场景。您可以根据项目需求和个人喜好选择适合的方法来渲染图标。

---
```jsx
import { useState, useEffect } from 'react';
import Button from './Button';
import Number from './Number';
function Timer({ startTime }) {
  const [remaining, setRemaining] = useState(startTime); 
  const [isRunning, setRunning] = useState(false); 
  useEffect(() => { 
    if (!isRunning) {
      return;
    }
    function tick() {
      setRemaining(oldValue => {
        const value = oldValue - 1;
        if (value <= 0) {
          setRunning(false);
          return startTime;
        }
        return value;
      });
    }
    const interval = setInterval(tick, 1000); 
    return () => clearInterval(interval); 
  }, [isRunning, startTime]); 
  const play = () => setRunning(true);
  const pause = () => setRunning(false);
  return (
    <section className={`timer ${isRunning ? 'timer-ticking' : ''}`}> 
      <TimeDisplay time={remaining} /> 
      {isRunning 
        ? <Button icon="pause" label="Pause" onClick={pause} /> 
        : <Button icon="play" label="Play" onClick={play} /> 
      }
    </section>
  );
};
export default Timer;
```
在上述代码块中，注释已添加以解释每个部分的作用：
A. 使用 `useState` 钩子创建 `remaining` 状态变量，用于存储剩余时间。
B. 使用 `useState` 钩子创建 `isRunning` 状态变量，用于表示计时器是否正在运行。
C. 使用 `useEffect` 钩子来处理副作用，即启动或暂停计时器。
D. 使用 `setInterval` 创建一个间隔，每秒触发 `tick` 函数来更新剩余时间。
E. 使用 `clearInterval` 在组件卸载或 `useEffect` 重新运行时清除间隔。
F. 在 `useEffect` 依赖数组中添加 `isRunning` 和 `startTime`，以确保在这些值发生变化时重新运行 `useEffect`。
G. 根据计时器是否正在运行，添加 `timer-ticking` 类名来进行样式控制。
H. 渲染 `TimeDisplay` 组件来显示剩余时间。
I. 根据计时器是否正在运行，渲染不同的按钮。
J. 根据计时器是否正在运行，渲染不同的按钮图标、标签和点击事件。