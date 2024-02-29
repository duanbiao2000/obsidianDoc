#### React组件间通信代码示例

好的，以下是逐行注释后的完整React组件间通信示例代码：

```jsx
import React, { createContext, useContext, useState } from 'react';
// 引入React和相关Hook

// 创建一个Context对象
const DataContext = createContext();
// 创建一个Context对象

function App() {
  // 将共享状态保存在父组件中，并使用useState Hook进行状态管理
  const [data, setData] = useState('Hello World');

  return (
    // 在最外层包裹一个提供者（Provider）组件，使用Provider将数据共享给所有子组件
    <DataContext.Provider value={{ data, setData }}>
      <div className="App">
        <h1>Parent Component</h1>
        {/* 调用ChildComponent组件 */}
        <ChildComponent />
        {/* 调用SiblingComponent组件 */}
        <SiblingComponent />
      </div>
    </DataContext.Provider>
  );
}

function ChildComponent() {
  // 使用useContext Hook获取数据状态
  const { data, setData } = useContext(DataContext);

  // 定义更新共享状态的回调函数
  const handleClick = () => {
    setData('New Data From Child');
  };

  return (
    <div>
      <h2>Child Component</h2>
      {/* 显示来自父组件的数据 */}
      <p>Data from Parent: {data}</p>
      {/* 点击此按钮将触发回调函数 */}
      <button onClick={handleClick}>Update Data</button>
    </div>
  );
}

function SiblingComponent() {
  // 使用useContext Hook获取数据状态
  const { data } = useContext(DataContext);

  return (
    <div>
      <h2>Sibling Component</h2>
      {/* 显示来自父组件的数据 */}
      <p>Data from Parent: {data}</p>
    </div>
  );
}

// 输出App组件
export default App;
```

在上面的注释中，我们对每一行代码都进行了详细的说明。其中，关键点是使用useContext Hook获取父组件状态，以及如何使用Provider将状态共享给子组件。同时，我们还演示了如何使用Props和回调函数在父子组件之间传递数据。

#### React组件间通信示例代码2

在React中，组件之间的通信可以通过props传递数据和回调函数来实现。下面是一个简单的示例代码：

```javascript
import React, { useState } from 'react';

function Counter(props) {
  const [count, setCount] = useState(0);

  function handleIncrement() {
    setCount(count + 1);
    props.onIncrement(count + 1);
  }

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={handleIncrement}>Increment</button>
    </div>
  );
}

function App() {
  function handleCounterIncrement(newCount) {
    console.log(`New count is ${newCount}`);
  }

  return (
    <div>
      <h1>App</h1>
      <Counter onIncrement={handleCounterIncrement} />
    </div>
  );
}
```

在该示例中，Counter组件负责计数并响应"Increment"按钮的点击事件，当按钮被点击时调用handleIncrement函数更新状态，并通过props将新的计数值传递给父级组件App。

此外，在App组件中定义了名为handleCounterIncrement的回调函数，用于处理Counter组件传递过来的值。该函数被作为props传递给Counter组件，并在Counter中被调用。因此，Counter组件可以将计数值传递给App组件，实现了组件之间的通信。

这段代码主要是演示组件之间的通信机制，下面逐行解释：

1. `import React, { useState } from 'react';`：引入React和useState钩子函数。
2. `function Counter(props) {`：定义名为Counter的函数式组件，接收一个props对象作为参数。
3. `const [count, setCount] = useState(0);`：使用useState钩子函数来声明一个状态变量count，并用setCount函数来更新它的值。初始值为0。
4. `function handleIncrement() {`：定义一个名为handleIncrement的函数，该函数将在用户点击"Increment"按钮时被调用。
5. `setCount(count + 1);`：使用setCount函数来更新count的值，让它加1。
6. `props.onIncrement(count + 1);`：调用传递过来的onIncrement回调函数，并将新的计数值作为参数传递给它。
7. `<div>`...`</div>`：返回一个包含当前计数值和"Increment"按钮的div元素。
8. `<button onClick={handleIncrement}>Increment</button>`：渲染一个按钮，并在用户点击它时调用handleIncrement函数。
9. `function App() {`：定义名为App的函数式组件。
10. `function handleCounterIncrement(newCount) {`：定义一个叫做handleCounterIncrement的函数，将在Counter组件中调用。
11. `console.log(`New count is ${newCount}`);`：在浏览器控制台中打印一个字符串，显示新的计数值。
12. `<Counter onIncrement={handleCounterIncrement} />`：渲染一个Counter组件，并将handleCounterIncrement函数作为参数传递给它。此时，Counter组件已经具备了通知App组件更新计数值的能力。
13. `<div>`...`</div>`：最后，将<h1>和<Counter>元素打包在一个<div>元素中，并返回该元素，完成组件渲染。