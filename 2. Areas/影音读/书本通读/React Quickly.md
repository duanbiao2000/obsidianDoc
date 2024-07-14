---
aliases:

---
20230718 0905
links:
title: 
origin: React Quickly, Second Edition - MEAP
tags: #flashcards #todo 

#### P186

Table 5.1. State in functional components and class-based components respectively

|Functional component|Class-based component|
|---|---|
|`const [counter, setCounter] = useState(0);`|`state = { counter: 0 }`|
|This is the case if state is initialized to a static value.|When we initialize state to a static value here, we can use a class member.|
|`const [counter, setCounter] = useState(initialValue);`|`constructor(props) { this.state = { counter: props.initialValue }; }`|
|This is the case if state is initialized to a dynamic value from a property.|Here we have to access the property in the constructor and initialize the state using `this.state`.|
|`<p>Counter: {counter}</p>`|`<p>Counter: {this.state.counter}</p>`|
|Renders the value of `counter` in the component.|Renders the value of `counter` in the component.|
|`onClick={() => setCounter(0)}`|`onClick={() => this.setState({ counter: 0 })}`|
|If we're setting the state to a fixed value, we can use the non-functional variant of the setter.|We do the same thing here, except we need to make it an object.|
|`onClick={() => setCounter(value => value + 1)}`|`onClick={() => this.setState(({ counter }) => ({ counter: counter + 1 }))}`|
|If we use an updater function, we simply use the old value and return a new one using whatever type we have in the state.|If we're setting the state to a dynamic value based on the current state, we can use the functional updater variant of the setter but we have to return an object based on the old state object.|

以上内容以Markdown表格的形式展示了函数组件和基于类的组件在处理状态时的不同写法和对应的效果。 希望对您有所帮助！如果有任何其他问题，请随时提问。

5.3.2 Differences from useState hook 

The main differences are: 
• You can only have **one state object** and it is always an object.
• Components **always re-render if updated**, even if nothing changed. 
• Objects are merged when you update the state, so **partial updates are possible**. 


“If you do convert your state to objects with multiple values in a functional component, there are a few pitfalls to note: 
• Objects are not merged in useState setter functions as they are in setState.
• Re-render only happens when a useState setter function is invoked with an actual new value, whereas setState would always trigger a re-render regardless of value reference equality.”


在给定的代码中，确实是使用了连续两个箭头函数的写法。请允许我详细解释这种用法，并给出最佳实践。
在给定的`useEffect`钩子中，连续两个箭头函数的写法是一种常见的用法，被称为返回清理函数的箭头函数。具体来说，第一个箭头函数被用作`useEffect`的回调函数，用于定义副作用逻辑；而第二个箭头函数则被用作返回的清理函数，用于在组件卸载或下一次副作用执行前执行清理操作。
下面是解释和最佳实践的示例代码：
```javascript
useEffect(() => {
  // 副作用逻辑
  const trackEvent = () => {
    // 跟踪事件的代码
    console.log('Event tracked: dialog_dismissed');
  };
  // 在组件卸载或下一次副作用执行前执行清理操作
  return () => {
    trackEvent(); // 执行清理操作，如跟踪事件
  };
}, []);
```
在这个例子中，当组件挂载时，`useEffect`的回调函数被执行。在回调函数内部，定义了`trackEvent`函数来跟踪事件。同时，返回的第二个箭头函数会在组件卸载时或下一次副作用执行前被调用。在这个清理函数内部，可以执行一些清理操作，比如跟踪事件或取消订阅。
这种用法的最佳实践是在副作用逻辑中处理任何需要清理的操作，并返回一个清理函数以确保在组件被卸载时进行清理。这样可以避免内存泄漏和不必要的副作用。
需要注意的是，第二个箭头函数只在依赖项数组为空（`[]`）时执行一次，因为它没有依赖项。如果有依赖项，清理函数会在依赖项发生变化时被调用，而不是在组件卸载时执行清理操作。
希望这样的解释和最佳实践能够帮助您理解和正确使用连续两个箭头函数的用法。如果您有任何其他问题，请随时提问！


[[../../前端开发/React/useEffect]]