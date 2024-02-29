---
aliases: React Quickly, Second Edition - MEAP... (Z-Library).pdf

---
20230815 0957
links: 
title: 
origin: React Quickly, Second Edition - MEAP... (Z-Library).pdf
tags: #flashcards #todo #bookStatusOnreading 

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
在上述示例中，`outerFunction` 是一个外部函数，它接受一个参数 `param`。在外部函数中，返回了一个内部的箭头函数，该箭头函数也接受一个参数 `innerParam`。当内部箭头函数被调用时，它会在控制台打印出外部函数的参数 `param` 和内部函数的参数 `innerParam`。
箭头函数嵌套写法可以用于许多场景，例如在高阶函数中创建闭包，或在函数中定义私有函数。

```jsx
const onChange = (key) => (evt) => { #B 
  setData(oldData => ({
    ...oldData, #C 
    [key]: evt.target.value, #D 
    }));
};
```
在给定的代码中，`const onChange = (key) => (evt) => { ... }` 是一个函数定义，用于创建一个事件处理函数 `onChange`。
下面对代码中的每个部分进行解释：
B. `(key) => (evt) => { ... }`：这是一个箭头函数的嵌套写法，表示 `onChange` 函数接受一个参数 `key`，返回一个接受 `evt` 参数的函数。
C. `setData(oldData => ({ ...oldData, ... }))`：这是一个更新数据的操作，使用函数式更新（Functional Update）的方式，通过展开运算符（spread operator）来复制旧数据对象的内容。
D. `[key]: evt.target.value`：这是一个动态属性名的方式，使用 `[key]` 来作为属性名，将 `evt.target.value` 的值赋给对应的属性。
通过这个函数定义，可以创建一个可用于处理不同键（`key`）的事件处理函数 `onChange`。当事件触发时，该函数会更新数据对象的对应键的值，实现数据的更新和管理。
希望这个解释对您有所帮助！如果您还有其他问题，请随时提问。

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
在上述示例中，当选择框的值发生变化时，事件处理函数 `handleChange` 会被调用，并通过访问 `evt.target.selectedOptions` 属性来获取被选中的选项。然后，通过遍历选中的选项，可以获取它们的值（`value`）并进行处理。
需要注意的是，`evt.target.selectedOptions` 返回的是一个类似数组的对象（HTMLCollection 或 NodeList），可以使用索引或迭代方法（如 `for` 循环或 `forEach`）来访问其中的选项元素。
希望这个解释对您有所帮助！如果您还有其他问题，请随时提问。

`Array.from(evt.target.selectedOptions)` 是一个将类数组对象转换为数组的操作。
在给定的代码中，`evt.target.selectedOptions` 是一个类数组对象，表示在选择框中被选中的选项的集合。为了将这个类数组对象转换为真正的数组，可以使用 `Array.from()` 方法。
下面是对代码中每个部分的解释：
B. `Array.from(evt.target.selectedOptions)`：这是一个调用 `Array.from()` 方法的表达式。`Array.from()` 方法将一个类数组对象或可迭代对象转换为一个新的数组。在这种情况下，它将 `evt.target.selectedOptions` 类数组对象转换为一个数组。
通过这个操作，我们可以获得一个真正的数组 `options`，其中包含了选择框中被选中的选项元素。这样，我们可以使用数组的方法和属性来处理这些选项。
需要注意的是，`Array.from()` 方法在转换类数组对象时非常有用，因为它可以将类数组对象转换为具有数组功能的真正的数组。

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
在上述代码块中，注释已添加以解释每个部分的作用：
- 在 `reducer` 函数中，根据动作的类型来更新状态。
- 在 `Counter` 组件中，使用 `useReducer` 钩子来管理状态和分发动作。
- 在返回的 JSX 中，展示计数器的当前值，并通过点击按钮来分发不同类型的动作。
这段代码实现了一个简单的计数器功能。通过使用 `useReducer` 钩子，可以将状态和状态更新逻辑封装在一个 reducer 函数中，并通过分发动作来更新状态。
请注意，这里使用的是 React 的官方 `useReducer` 钩子，它允许将状态逻辑与组件逻辑分离，并提供了一种更可控和可预测的状态管理方式。
希望这些注释能够进一步解释代码块中的内容！如果您还有其他问题，请随时提问。

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
A. `INITIAL_STATE` 定义了初始的状态对象，其中包含了 `status`、`result` 和 `error` 属性。
B. 在 reducer 函数中，根据动作的类型来更新状态。
C. `default` 分支用于返回当前状态对象。
D. 使用 `useReducer` 钩子来管理状态和分发动作，并将初始状态设置为 `INITIAL_STATE`。
E. 在 `useEffect` 钩子中发起异步请求之前，分发 `LOADING` 动作。
F. 在异步请求成功后，根据返回结果分发 `SUCCESS` 动作。
G. 在异步请求失败后，根据错误信息分发 `FAILURE` 动作。
H. 从状态对象中提取 `status`、`error` 和 `result`。
I. 根据不同的状态值进行条件渲染。
在给定的代码中，`payload` 是一个通用的术语，表示在动作中携带的附加数据。它可以是任何类型的值，根据具体的应用和上下文而定。
在 reducer 函数中，`payload` 参数用于接收动作中携带的附加数据，以便在更新状态时使用。根据具体的动作类型和需求，`payload` 可以是一个单一的值、一个对象或任何其他数据类型。
在给定的代码中，`payload` 在不同的动作类型中被用于不同的目的：
- 在 "FAILURE" 动作中，`payload` 用于传递错误信息。
- 在 "SUCCESS" 动作中，`payload` 用于传递返回的结果数据。
这样，通过在动作中使用 `payload`，可以将相关的数据传递给 reducer 函数，并在更新状态时使用。
需要注意的是，`payload` 只是一个约定的名称，您可以根据实际情况和需求选择任何其他的名称来表示附加数据。
希望这个解释对您有所帮助！如果您还有其他问题，请随时提问。
在给定的代码中，`.catch(({ message }) => dispatch({ type: "FAILURE", payload: message })` 中的 `message` 是来自于捕获到的错误对象的 `message` 属性。
在 JavaScript 中，当 Promise 被拒绝（rejected）时，`.catch()` 方法用于捕获错误。在这种情况下，`catch` 回调函数会接收到一个错误对象作为参数。错误对象通常包含了有关错误的信息，例如错误消息、错误代码等。
在给定的代码中，通过解构赋值 `{ message }`，从错误对象中提取 `message` 属性，并将其作为 `payload` 传递给 `FAILURE` 动作。这样，在更新状态时，`message` 将作为错误信息被存储在状态对象的 `error` 属性中。
所以，`message` 来自于捕获到的错误对象的 `message` 属性，表示错误的相关信息。
希望这个解释对您有所帮助！如果您还有其他问题，请随时提问。

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
  const [remaining, setRemaining] = useState(startTime); // A
  const [isRunning, setRunning] = useState(false); // B
  useEffect(() => { // C
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
    const interval = setInterval(tick, 1000); // D
    return () => clearInterval(interval); // E
  }, [isRunning, startTime]); // F
  const play = () => setRunning(true);
  const pause = () => setRunning(false);
  return (
    <section className={`timer ${isRunning ? 'timer-ticking' : ''}`}> // G
      <TimeDisplay time={remaining} /> // H
      {isRunning // I
        ? <Button icon="pause" label="Pause" onClick={pause} /> // J
        : <Button icon="play" label="Play" onClick={play} /> // J
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

