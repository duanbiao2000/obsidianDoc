---
aliases: 

source: https://www.bilibili.com/video/BV1MS4y167Bz/?p=6&spm_id_from=pageDriver&vd_source=7038f96b6bb3b14743531b102b109c43
title: 
tags: 
createdAt: 2023-10-22T12:01:00
updateAt:

---
![Basic React SSR](https://www.bilibili.com/video/BV1MS4y167Bz/?p=6&spm_id_from=pageDriver&vd_source=7038f96b6bb3b14743531b102b109c43)

![[assets/img/React 软件架构/IMG-React 软件架构-20240714124854083.png]]

当使用React Context进行状态管理时，通常会在不同的组件和文件之间进行数据共享。下面是一个更复杂的实际示例，将展示如何创建、提供和消费上下文数据，同时将不同组件分开到不同的JavaScript文件中。

1. **创建上下文文件 (MyContext.js)**

```javascript
import React, { createContext, useContext, useState } from 'react';

const MyContext = createContext();

export function MyContextProvider({ children }) {
  const [data, setData] = useState('Some data');

  return (
    <MyContext.Provider value={{ data, setData }}>
      {children}
    </MyContext.Provider>
  );
}

export function useMyContext() {
  return useContext(MyContext);
}
```

在这里，我们创建了一个名为`MyContext`的上下文，同时定义了一个`MyContextProvider`组件，它提供了数据并包裹了子组件。我们还导出了`useMyContext`自定义钩子，以便在其他组件中访问上下文数据。

2. **App 组件 (App.js)**

```javascript
import React from 'react';
import { MyContextProvider } from './MyContext';
import ChildComponent from './ChildComponent';

function App() {
  return (
    <MyContextProvider>
      <div className="App">
        <h1>App Component</h1>
        <ChildComponent />
      </div>
    </MyContextProvider>
  );
}

export default App;
```

在`App`组件中，我们导入`MyContextProvider`，并将其用于提供上下文数据。然后，我们呈现了`ChildComponent`，使其能够访问上下文数据。

3. **ChildComponent 组件 (ChildComponent.js)**

```javascript
import React from 'react';
import { useMyContext } from './MyContext';

function ChildComponent() {
  const { data, setData } = useMyContext();

  return (
    <div className="ChildComponent">
      <h2>Child Component</h2>
      <p>Data: {data}</p>
      <button onClick={() => setData('Updated data')}>Update Data</button>
    </div>
  );
}

export default ChildComponent;
```

在`ChildComponent`组件中，我们导入`useMyContext`自定义钩子，并使用它来访问上下文中的`data`和`setData`。我们还展示了如何更新上下文数据。

这个示例演示了如何将不同的组件放在不同的JavaScript文件中，并使用React Context在这些组件之间进行数据共享。`MyContextProvider`用于提供数据，而`useMyContext`用于访问数据，这使得状态管理非常方便。



![[IMG-React 软件架构-20240719192335649.png]]

下面是一个稍微复杂一点的 Recoil 应用程序示例，其中包含多个组件和更复杂的状态管理。

1. **Recoil状态定义 (recoilState.js)**

首先，我们将创建一个文件来定义我们的 Recoil 状态：

```javascript
// recoilState.js
import { atom, selector } from 'recoil';

export const todoListState = atom({
  key: 'todoListState',
  default: [],
});

export const todoListFilterState = atom({
  key: 'todoListFilterState',
  default: 'all',
});

export const filteredTodoListState = selector({
  key: 'filteredTodoListState',
  get: ({ get }) => {
    const filter = get(todoListFilterState);
    const list = get(todoListState);

    switch (filter) {
      case 'completed':
        return list.filter((item) => item.completed);
      case 'uncompleted':
        return list.filter((item) => !item.completed);
      default:
        return list;
    }
  },
});
```

这个示例包括一个`todoListState`用于存储待办事项，一个`todoListFilterState`用于存储筛选条件，以及一个`filteredTodoListState`选择器，用于根据筛选条件过滤待办事项。

2. **待办事项列表组件 (TodoList.js)**

接下来，我们将创建一个组件来显示待办事项列表：

```javascript
// TodoList.js
import React from 'react';
import { useRecoilValue } from 'recoil';
import { filteredTodoListState } from './recoilState';

function TodoList() {
  const todoList = useRecoilValue(filteredTodoListState);

  return (
    <ul>
      {todoList.map((todo) => (
        <li key={todo.id}>
          {todo.text} {todo.completed ? '✔' : '❌'}
        </li>
      ))}
    </ul>
  );
}

export default TodoList;
```

3. **添加待办事项组件 (AddTodo.js)**

然后，我们创建一个组件来添加新的待办事项：

```javascript
// AddTodo.js
import React, { useState } from 'react';
import { useSetRecoilState } from 'recoil';
import { todoListState } from './recoilState';

function AddTodo() {
  const [text, setText] = useState('');
  const setTodoList = useSetRecoilState(todoListState);

  const addTodo = () => {
    if (text) {
      setTodoList((prevTodoList) => [
        ...prevTodoList,
        { id: prevTodoList.length, text, completed: false },
      ]);
      setText('');
    }
  };

  return (
    <div>
      <input
        type="text"
        value={text}
        onChange={(e) => setText(e.target.value)}
      />
      <button onClick={addTodo}>Add Todo</button>
    </div>
  );
}

export default AddTodo;
```

4. **过滤待办事项组件 (FilterTodos.js)**

接着，我们创建一个组件来过滤待办事项：

```javascript
// FilterTodos.js
import React from 'react';
import { useRecoilState } from 'recoil';
import { todoListFilterState } from './recoilState';

function FilterTodos() {
  const [filter, setFilter] = useRecoilState(todoListFilterState);

  return (
    <div>
      <label>
        Show:
        <select value={filter} onChange={(e) => setFilter(e.target.value)}>
          <option value="all">All</option>
          <option value="completed">Completed</option>
          <option value="uncompleted">Uncompleted</option>
        </select>
      </label>
    </div>
  );
}

export default FilterTodos;
```

5. **App 组件 (App.js)**

最后，我们将在 App 组件中使用 Recoil 状态和所有子组件：

```javascript
// App.js
import React from 'react';
import { RecoilRoot } from 'recoil';
import TodoList from './TodoList';
import AddTodo from './AddTodo';
import FilterTodos from './FilterTodos';

function App() {
  return (
    <RecoilRoot>
      <div>
        <h1>Recoil Todo List</h1>
        <AddTodo />
        <FilterTodos />
        <TodoList />
      </div>
    </RecoilRoot>
  );
}

export default App;
```

这个示例演示了如何使用 Recoil 管理多个状态，并将它们分成不同的组件文件。`RecoilRoot` 用于包装应用程序，以便状态能够在整个组件树中共享。你可以在此基础上进一步构建和扩展你的应用程序，包括待办事项的编辑、删除、标记为完成等功能。


# Redux
Redux 是一个用于管理 JavaScript应用程序状态的流行库。它通常与React一起使用，但也可以与其他JavaScript框架或库结合使用。Redux 的核心思想是将整个应用程序的状态存储在一个单一的状态树中，并通过分发（dispatching）操作（actions）来修改这个状态。

以下是一个简单的示例，展示了如何在React应用程序中使用Redux：

1. **安装 Redux**：首先，确保你的项目已经安装了 Redux。你可以使用以下命令来安装 Redux：

   ```bash
   npm install redux react-redux
   ```

2. **创建 Redux Store**：Redux 应用程序的核心是创建一个 Redux store，用于存储应用程序的状态。在你的应用程序的入口文件中，通常是 `index.js`，创建一个 Redux store。

   ```javascript
   // index.js
   import { createStore } from 'redux';
   import { Provider } from 'react-redux';
   import rootReducer from './reducers'; // 你的根Reducer

   const store = createStore(rootReducer);

   // 将Redux store包装在Provider中，以便在整个应用程序中访问状态
   ReactDOM.render(
     <Provider store={store}>
       <App />
     </Provider>,
     document.getElementById('root')
   );
   ```

3. **定义 Reducer**：Reducers 是用于处理状态变化的纯函数。它们根据操作（action）来更新应用程序的状态。在 `reducers.js` 文件中定义你的根Reducer。

   ```javascript
   // reducers.js
   const initialState = {
     count: 0,
   };

   const rootReducer = (state = initialState, action) => {
     switch (action.type) {
       case 'INCREMENT':
         return { ...state, count: state.count + 1 };
       case 'DECREMENT':
         return { ...state, count: state.count - 1 };
       default:
         return state;
     }
   };

   export default rootReducer;
   ```

4. **创建 Action Creators**：Action creators 是用于创建操作对象的函数。它们描述了操作的类型和携带的数据。

   ```javascript
   // actions.js
   export const increment = () => ({
     type: 'INCREMENT',
   });

   export const decrement = () => ({
     type: 'DECREMENT',
   });
   ```

5. **连接 React 组件**：使用 `react-redux` 库中的 `connect` 函数将React组件与Redux store连接起来，以便它们可以访问状态和操作。

   ```javascript
   // Counter.js
   import React from 'react';
   import { connect } from 'react-redux';
   import { increment, decrement } from './actions';

   function Counter({ count, increment, decrement }) {
     return (
       <div>
         <p>Count: {count}</p>
         <button onClick={increment}>Increment</button>
         <button onClick={decrement}>Decrement</button>
       </div>
     );
   }

   const mapStateToProps = (state) => ({
     count: state.count,
   });

   export default connect(mapStateToProps, { increment, decrement })(Counter);
   ```

6. **使用状态和操作**：在你的React组件中，你可以通过 `connect` 函数注入状态和操作，然后在组件中使用它们。

Redux 允许你在整个应用程序中有效地管理状态，并提供了一种一致的方式来处理状态变化。以上示例只是一个简单的入门示例，Redux 还提供了中间件、异步操作、DevTools 和更多功能，以满足复杂应用程序的需求。


# Monoliths, Muti-repos, and Monorepos


当涉及到比较和描述"Monoliths"、"Multi-repos" 和 "Monorepos" 时，Markdown 表格可以是一个清晰的方式。以下是一个表格，用于对这三种软件组织方法进行简要的对比：

| 特征                | Monolith（单体应用） | Multi-repos（多仓库） | Monorepo（单仓库）  |
|-----------------------|-------------------|-----------------------|-------------------|
| 单一代码库           | 是               | 否                   | 是               |
| 解决方案复杂性       | 适用于小到中等规模项目  | 适用于大规模和微服务架构 | 适用于多个相关项目    |
| 团队协作             | 单一代码库内协作  | 独立仓库，可独立协作 | 单一仓库内或独立协作 |
| 代码管理复杂性       | 较低              | 需要工具来管理不同仓库 | 中等              |
| 调试和维护           | 相对简单           | 独立仓库，分散调试和维护 | 相对中等           |
| 独立性               | 所有功能紧密耦合  | 不同仓库相对独立    | 不同项目相对独立    |
| 模块化和独立部署     | 较困难             | 独立部署各个仓库     | 较容易             |
| 共享依赖项           | 有限共享           | 有限共享           | 更容易共享         |

d