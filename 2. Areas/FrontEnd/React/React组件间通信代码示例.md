#### React组件间通信代码示例


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

