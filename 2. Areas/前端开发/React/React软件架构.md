---
aliases: 
date: 
url: https://www.bilibili.com/video/BV1MS4y167Bz/?p=6&spm_id_from=pageDriver&vd_source=7038f96b6bb3b14743531b102b109c43
page-title: 
tags: 
established: 2023-10-22T12:01:00
updated: 
isFinished: false
---
![Basic React SSR](https://www.bilibili.com/video/BV1MS4y167Bz/?p=6&spm_id_from=pageDriver&vd_source=7038f96b6bb3b14743531b102b109c43)

![[assets/img/React 软件架构/IMG-React 软件架构-20240714124854083.png]]

![State management tool : Context](https://www.bilibili.com/video/BV1MS4y167Bz/?p=15&spm_id_from=pageDriver&vd_source=7038f96b6bb3b14743531b102b109c43)

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

`connect(mapStateToProps, { increment, decrement })(Counter)` 是用于连接 React 组件与 Redux store 的函数调用。它是 `react-redux` 库中的一个函数，允许你将 Redux store 的状态和操作映射到组件的属性，以便组件能够访问并更新状态。

以下是对这个函数的详细解释：

- `connect` 是一个高阶函数，它接受两个参数并返回一个函数，用于包装组件。
  
- 第一个参数 `mapStateToProps` 是一个函数，用于将 Redux store 的状态映射到组件的属性。它接受 Redux store 的状态作为参数，并返回一个对象，该对象包含组件所需的属性。

- 第二个参数是一个对象，其中包含操作（action creators）。这允许你将操作映射到组件的属性，以便组件能够触发这些操作。在示例中，操作是 `increment` 和 `decrement`，它们可以通过组件的属性调用。

- 最后，`connect` 返回一个函数，它接受一个组件作为参数，并返回一个连接到 Redux store 的新组件。

在示例中，`Counter` 组件通过 `connect` 函数连接到 Redux store。`mapStateToProps` 函数将 Redux store 中的 `state.count` 映射到组件的 `count` 属性，允许组件访问状态。同时，`increment` 和 `decrement` 操作也被映射到组件的属性，以便组件可以触发这些操作来更新状态。

这种连接模式使组件能够访问 Redux store 的状态和操作，而无需直接与 Redux store 交互，从而简化了组件的代码和逻辑。这也是 React 应用程序中的常见状态管理模式之一。

下面是一个使用 Redux 来管理待办事项应用程序的状态的示例，与之前使用 Recoil 的示例相似。首先，确保你已经安装了 Redux。

1. **创建 Redux Store**：在你的应用程序的入口文件中，通常是 `index.js`，创建一个 Redux store。

```javascript
// index.js
import React from 'react';
import ReactDOM from 'react-dom';
import { createStore, combineReducers } from 'redux';
import { Provider } from 'react-redux';
import App from './App';
import reducers from './reducers'; // 你的根Reducer

const store = createStore(combineReducers(reducers));

ReactDOM.render(
  <Provider store={store}>
    <App />
  </Provider>,
  document.getElementById('root')
);
```

2. **定义 Reducers**：Reducers 是用于处理状态变化的纯函数。在 `reducers.js` 文件中定义你的根Reducer。

```javascript
// reducers.js
const initialState = {
  todoList: [],
  filter: 'all',
};

const rootReducer = (state = initialState, action) => {
  switch (action.type) {
    case 'ADD_TODO':
      return {
        ...state,
        todoList: [
          ...state.todoList,
          { id: state.todoList.length + 1, text: action.text, completed: false },
        ],
      };
    case 'TOGGLE_TODO':
      return {
        ...state,
        todoList: state.todoList.map((todo) =>
          todo.id === action.id ? { ...todo, completed: !todo.completed } : todo
        ),
      };
    case 'SET_FILTER':
      return {
        ...state,
        filter: action.filter,
      };
    default:
      return state;
  }
};

export default rootReducer;
```

3. **创建 Action Creators**：Action creators 是用于创建操作对象的函数。它们描述了操作的类型和携带的数据。

```javascript
// actions.js
export const addTodo = (text) => ({
  type: 'ADD_TODO',
  text,
});

export const toggleTodo = (id) => ({
  type: 'TOGGLE_TODO',
  id,
});

export const setFilter = (filter) => ({
  type: 'SET_FILTER',
  filter,
});
```

4. **App 组件 (App.js)**：在你的React应用程序中，你可以在 `App` 组件中使用 Redux 状态和操作。

```javascript
// App.js
import React from 'react';
import { connect } from 'react-redux';
import { addTodo, toggleTodo, setFilter } from './actions';
import TodoList from './TodoList';
import FilterTodos from './FilterTodos';

function App() {
  return (
    <div>
      <h1>Redux Todo List</h1>
      <AddTodo />
      <FilterTodos />
      <TodoList />
    </div>
  );
}

export default connect(null, { addTodo, toggleTodo, setFilter })(App);
```

5. **AddTodo 组件 (AddTodo.js)**：创建一个组件来添加新的待办事项。

```javascript
// AddTodo.js
import React, { useState } from 'react';

function AddTodo({ addTodo }) {
  const [text, setText] = useState('');

  const handleAddTodo = () => {
    if (text) {
      addTodo(text);
      setText('');
    }
  }

  return (
    <div>
      <input
        type="text"
        value={text}
        onChange={(e) => setText(e.target.value)}
      />
      <button onClick={handleAddTodo}>Add Todo</button>
    </div>
  );
}

export default connect(null, { addTodo })(AddTodo);
```

6. **FilterTodos 组件 (FilterTodos.js)**：创建一个组件来过滤待办事项。

```javascript
// FilterTodos.js
import React from 'react';
import { connect } from 'react-redux';
import { setFilter } from './actions';

function FilterTodos({ setFilter }) {
  return (
    <div>
      <label>
        Show:
        <select onChange={(e) => setFilter(e.target.value)}>
          <option value="all">All</option>
          <option value="completed">Completed</option>
          <option value="uncompleted">Uncompleted</option>
        </select>
      </label>
    </div>
  );
}

export default connect(null, { setFilter })(FilterTodos);
```

7. **TodoList 组件 (TodoList.js)**：创建一个组件来显示待办事项列表。

```javascript
// TodoList.js
import React from 'react';
import { connect } from 'react-redux';
import { toggleTodo } from './actions';

function TodoList({ todoList, filter, toggleTodo }) {
  const filteredTodoList = filterTodoList(todoList, filter);

  return (
    <ul>
      {filteredTodoList.map((todo) => (
        <li key={todo.id}>
          <span
            onClick={() => toggleTodo(todo.id)}
            style={{ textDecoration: todo.completed ? 'line-through' : 'none' }}
          >
            {todo.text}
          </span>
        </li>
      ))}
    </ul>
  );
}

const mapStateToProps = (state) => ({
  todoList: state.todoList,
  filter: state.filter,
});

const filterTodoList = (todoList, filter) => {
  switch (filter) {
    case 'completed':
      return todoList.filter((todo) => todo.completed);
    case 'uncompleted':
      return todoList.filter((todo) => !todo.completed);
    default:
      return todoList;
  }
};

export default connect(mapStateToProps, { toggleTodo })(TodoList);
```

这个示例演示了如何使用 Redux 来管理待办事项应用程序的状态，与之前使用 Recoil 的示例相似。Redux 提供了一种一致的方式来处理状态变化，无需在组件之间手动传递状态。

MobX 是另一个用于状态管理的流行库，它提供了一种响应式的方式来管理和更新状态。下面是如何使用 MobX 来管理上面的待办事项应用程序的状态。

首先，确保你的项目已经安装了 MobX。你可以使用以下命令来安装 MobX 和相关工具：

```bash
npm install mobx mobx-react
```

接下来，我们将创建一个使用 MobX 来管理状态的示例：

1. **创建 MobX Store**：首先，创建一个 MobX store 来存储应用程序的状态。在 MobX 中，store 是一个可观察对象，它包含应用程序的状态和方法来修改状态。

```javascript
// TodoStore.js
import { makeObservable, observable, action, computed } from 'mobx';

class TodoStore {
  todoList = [];
  filter = 'all';

  constructor() {
    makeObservable(this, {
      todoList: observable,
      filter: observable,
      addTodo: action,
      toggleTodo: action,
      setFilter: action,
      filteredTodoList: computed,
    });
  }

  addTodo(text) {
    this.todoList.push({ id: this.todoList.length + 1, text, completed: false });
  }

  toggleTodo(id) {
    const todo = this.todoList.find((t) => t.id === id);
    if (todo) {
      todo.completed = !todo.completed;
    }
  }

  setFilter(filter) {
    this.filter = filter;
  }

  get filteredTodoList() {
    switch (this.filter) {
      case 'completed':
        return this.todoList.filter((todo) => todo.completed);
      case 'uncompleted':
        return this.todoList.filter((todo) => !todo.completed);
      default:
        return this.todoList;
    }
  }
}

const store = new TodoStore();
export default store;
```

2. **使用 MobX Store**：在你的 React 组件中使用 MobX store 来访问和修改状态。

```javascript
// App.js
import React from 'react';
import { Provider, observer } from 'mobx-react';
import store from './TodoStore';
import AddTodo from './AddTodo';
import FilterTodos from './FilterTodos';
import TodoList from './TodoList';

function App() {
  return (
    <Provider store={store}>
      <div>
        <h1>MobX Todo List</h1>
        <AddTodo />
        <FilterTodos />
        <TodoList />
      </div>
    </Provider>
  );
}

export default observer(App);
```

3. **创建组件**：创建组件来处理添加待办事项、过滤待办事项和显示待办事项的功能。

```javascript
// AddTodo.js
import React, { useState } from 'react';
import { inject, observer } from 'mobx-react';

function AddTodo({ store }) {
  const [text, setText] = useState('');

  const handleAddTodo = () => {
    if (text) {
      store.addTodo(text);
      setText('');
    }
  }

  return (
    <div>
      <input
        type="text"
        value={text}
        onChange={(e) => setText(e.target.value)}
      />
      <button onClick={handleAddTodo}>Add Todo</button>
    </div>
  );
}

export default inject('store')(observer(AddTodo));

// FilterTodos.js
import React from 'react';
import { inject, observer } from 'mobx-react';

function FilterTodos({ store }) {
  return (
    <div>
      <label>
        Show:
        <select onChange={(e) => store.setFilter(e.target.value)}>
          <option value="all">All</option>
          <option value="completed">Completed</option>
          <option value="uncompleted">Uncompleted</option>
        </select>
      </label>
    </div>
  );
}

export default inject('store')(observer(FilterTodos));

// TodoList.js
import React from 'react';
import { inject, observer } from 'mobx-react';

function TodoList({ store }) {
  const filteredTodoList = store.filteredTodoList;

  return (
    <ul>
      {filteredTodoList.map((todo) => (
        <li key={todo.id}>
          <span
            onClick={() => store.toggleTodo(todo.id)}
            style={{ textDecoration: todo.completed ? 'line-through' : 'none' }}
          >
            {todo.text}
          </span>
        </li>
      ))}
    </ul>
  );
}

export default inject('store')(observer(TodoList));
```

在上述示例中，我们创建了一个名为 `TodoStore` 的 MobX store，它包含待办事项列表 `todoList`、过滤条件 `filter`，以及一些方法用于添加、切换和设置过滤条件。然后，我们使用 MobX 提供的 `inject` 和 `observer` 函数来连接组件到 MobX store 并监视状态的变化。


以下是关于上述10点内容的核心代码示例，包括加载数据、懒加载、分页、用户交互、缓存、实时更新、后台数据加载、错误处理和性能优化的示例。

**1. 初始页面加载 (Initial Page Load):**

```javascript
// 使用React中的useEffect在组件加载时获取数据
import { useState, useEffect } from 'react';

function App() {
  const [data, setData] = useState([]);

  useEffect(() => {
    // 发起网络请求以获取数据
    fetch('/api/data')
      .then(response => response.json())
      .then(data => setData(data));
  }, []);

  return (
    <div>
      {data.map(item => (
        <div key={item.id}>{item.name}</div>
      )}
    </div>
  );
}
```

**2. 懒加载 (Lazy Loading):**

```javascript
// 当用户点击“加载更多”按钮时懒加载数据
import { useState, useEffect } from 'react';

function LazyLoad() {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(false);

  const loadMoreData = () => {
    setLoading(true);
    // 发起网络请求以获取更多数据
    fetch('/api/more-data')
      .then(response => response.json())
      .then(newData => {
        setData([...data, ...newData]);
        setLoading(false);
      });
  };

  return (
    <div>
      {data.map(item => (
        <div key={item.id}>{item.name}</div>
      )}
      <button onClick={loadMoreData} disabled={loading}>
        {loading ? 'Loading...' : 'Load More'}
      </button>
    </div>
  );
}
```

**3. 分页和无限滚动 (Pagination and Infinite Scrolling):**

```javascript
// 实现分页或无限滚动加载数据
import { useState, useEffect } from 'react';

function InfiniteScroll() {
  const [data, setData] = useState([]);
  const [page, setPage] = useState(1);
  const [loading, setLoading] = useState(false);

  const loadMoreData = () => {
    setLoading(true);
    // 发起网络请求以获取更多数据（使用分页参数）
    fetch(`/api/data?page=${page + 1}`)
      .then(response => response.json())
      .then(newData => {
        setData([...data, ...newData]);
        setPage(page + 1);
        setLoading(false);
      });
  };

  useEffect(() => {
    loadMoreData();
  }, []);

  return (
    <div>
      {data.map(item => (
        <div key={item.id}>{item.name}</div>
      )}
      <button onClick={loadMoreData} disabled={loading}>
        {loading ? 'Loading...' : 'Load More'}
      </button>
    </div>
  );
}
```

**4. 用户交互 (User Interaction):**

```javascript
// 根据用户交互加载数据
import { useState } from 'react';

function UserInteraction() {
  const [searchResults, setSearchResults] = useState([]);
  const [searchQuery, setSearchQuery] = useState('');

  const handleSearch = () => {
    // 发起网络请求以根据搜索查询获取数据
    fetch(`/api/search?query=${searchQuery}`)
      .then(response => response.json())
      .then(results => setSearchResults(results));
  };

  return (
    <div>
      <input
        type="text"
        value={searchQuery}
        onChange={e => setSearchQuery(e.target.value)}
      />
      <button onClick={handleSearch}>Search</button>
      {searchResults.map(result => (
        <div key={result.id}>{result.name}</div>
      )}
    </div>
  );
}
```

**5. 缓存 (Caching and Prefetching):**

```javascript
// 使用localStorage进行数据缓存
function getCachedData() {
  const cachedData = localStorage.getItem('cachedData');
  if (cachedData) {
    return JSON.parse(cachedData);
  }
  return [];
}

function App() {
  const [data, setData] = useState(getCachedData());

  const fetchData = () => {
    fetch('/api/data')
      .then(response => response.json())
      .then(newData => {
        setData(newData);
        localStorage.setItem('cachedData', JSON.stringify(newData));
      });
  };

  return (
    <div>
      <button onClick={fetchData}>Fetch Data</button>
      {data.map(item => (
        <div key={item.id}>{item.name}</div>
      )}
    </div>
  );
}
```

**6. 实时更新 (Real-Time Updates):**

```javascript
// 使用WebSocket进行实时数据更新
const socket = new WebSocket('ws://example.com');

socket.onmessage = event => {
  const updatedData = JSON.parse(event.data);
  // 处理实时更新的数据
};

function RealTimeUpdates() {
  return (
    <div>
      {/* 实时数据渲染 */}
    </div>
  );
}
```

**7. 后台数据加载 (Background Data Loading):**

```javascript
// 使用定时器在后台加载数据
function loadBackgroundData() {
  setInterval(() => {
    // 发起网络请求以获取后台数据
    fetch('/api/background-data')
      .then(response => response.json())
      .then(data => {
        // 处理后台数据
      });
  }, 300000); // 每5分钟加载一次
}

loadBackgroundData();

function App() {
  return (
    <div>
      {/* 应用界面 */}
    </div>
  );
}
```

**8. 错误处理 (Error Handling):**

```javascript
// 处理数据加载错误
function App() {
  const [error, setError] = useState(null);
  const [data, setData] = useState([]);

  const fetchData = () => {
    fetch('/api/data')
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(newData => {
        setData(newData);
        setError(null);
      })
      .catch(error => setError(error.message));
  };

  return (
    <div>
      <button onClick={fetchData}>Fetch Data</button>
      {error && <div>Error: {error}</div>}
      {data.map(item => (
        <div key={item.id}>{item.name}</div>
      )}
    </div>
  );
}
```

**9. 优化性能 (Optimizing Performance):**

```javascript
// 使用懒加载优化图片加载
import { LazyLoadImage } from 'react-lazy-load-image-component';

function PerformanceOptimization() {
  return (
    <div>
      <LazyLoadImage
        alt="Lazy-loaded image"
        src="image.jpg"
      />
      {/* 其他组件 */}
    </div>
  );
}
```

这些示例演示了不同情况下如何加载数据和处理数据加载。你可以根据你的应用程序需求，将这些示例中的代码结合到你的项目中。当然，实际应用中可能需要更多的细节和逻辑，以确保数据加载和用户交互的顺畅性和可靠性。

Data loading with Server-Side Rendering (SSR) involves fetching data on the server and passing it to the client-side JavaScript code for rendering. This approach is often used to improve the initial load time of a web application and to ensure that search engines can crawl the content of the application. Here's how you can implement data loading with SSR in a React application:

**Step 1: Set Up Your Server**

1. Create or configure a server for your application. Common choices include Express.js for Node.js applications or Next.js for React applications. Ensure that your server is capable of server-side rendering.

2. Define routes or URL patterns for the pages that will use SSR. For example, if you have a page at `/products`, set up a route for it.

3. In your server code, handle the SSR route and fetch the necessary data. You can use libraries like `axios` or the built-in `fetch` API to make API requests to fetch the data.

4. After fetching the data, render your React components with the data and use a server-side rendering engine like `ReactDOMServer` or a framework like Next.js to render the page as HTML.

5. Send the HTML response, including the data, to the client.

Here's a simplified example using Express.js as the server:

```javascript
// server.js

const express = require('express');
const React = require('react');
const { renderToString } = require('react-dom/server');
const App = require('./App'); // Your React component
const fetchData = require('./fetchData'); // Function to fetch data

const server = express();

server.get('/products', async (req, res) => {
  try {
    // Fetch data needed for the page
    const data = await fetchData();

    // Render the React component with the data
    const app = <App data={data} />;

    // Convert the React component to HTML
    const html = renderToString(app);

    // Send the HTML response to the client
    res.send(`
      <html>
        <head>
          <!-- Include any necessary styles and scripts -->
        </head>
        <body>
          <div id="root">${html}</div>
          <script>
            // Pass the data to the client-side code
            window.__DATA__ = ${JSON.stringify(data)}
          </script>
          <script src="/client.js"></script>
        </body>
      </html>
    `);
  } catch (error) {
    // Handle errors appropriately
    res.status(500).send('Internal Server Error');
  }
});

server.listen(3000, () => {
  console.log('Server is running on port 3000');
});
```

**Step 2: Set Up Your Client-Side Code**

1. Create a client-side JavaScript file (`client.js`) that will run on the browser.

2. In your client-side code, check if the `window.__DATA__` variable is available. This variable contains the data passed from the server.

3. If the data is available, use it to hydrate your React components. This means you can avoid making additional API requests to fetch the same data that was already loaded on the server.

Here's a simplified example of the client-side code:

```javascript
// client.js

import React from 'react';
import { hydrate } from 'react-dom';
import App from './App'; // Your React component

const data = window.__DATA__ || {};

hydrate(<App data={data} />, document.getElementById('root'));
```

**Step 3: Run Your Application**

- Start your server with `node server.js`.

- Access your application in a web browser by navigating to `http://localhost:3000/products`.

- The server will render the page with the initial data, and the client-side JavaScript will take over and hydrate the React components.

By following this approach, you can achieve server-side rendering with data loading in your React application. This provides improved performance and SEO benefits.

Enhancing Server-Side Rendering (SSR) with context in a React application allows you to share data or state between components during the rendering process on the server. Context provides a way to pass data through the component tree without having to explicitly pass props down to each level. This can be especially useful in an SSR scenario where you might need to share information across multiple components.

Here's a step-by-step guide on how to enhance SSR with context in a React application:

**1. Create a Context Provider:**

First, create a context provider that will encapsulate the shared data or state you want to make available to your components. You can use the `React.createContext` function to create a context. Here's an example:

```javascript
// MyContext.js
import React, { createContext, useContext } from 'react';

const MyContext = createContext();

export function useMyContext() {
  return useContext(MyContext);
}

export function MyContextProvider({ children }) {
  const sharedData = {
    message: 'Hello from context!',
  };

  return <MyContext.Provider value={sharedData}>{children}</MyContext.Provider>;
}
```

In the above code, we've created a context named `MyContext` and a `MyContextProvider` component that wraps your application. The `sharedData` object represents the data you want to make available to components.

**2. Set Up Your SSR-Ready Components:**

In your components, make use of the `useMyContext` hook to access the context. You can use this hook in both functional and class components.

```javascript
// MyComponent.js
import React from 'react';
import { useMyContext } from './MyContext';

function MyComponent() {
  const sharedData = useMyContext();

  return (
    <div>
      <p>{sharedData.message}</p>
      {/* Other content */}
    </div>
  );
}

export default MyComponent;
```

**3. Enhance Your SSR Server Code:**

When performing SSR, ensure that the `MyContextProvider` wraps your application. The shared data will be available to components within the provider's scope. Here's an example of how to modify your SSR server code:

```javascript
// server.js
import express from 'express';
import React from 'react';
import { renderToString } from 'react-dom/server';
import App from './App';
import { MyContextProvider } from './MyContext';

const server = express();

server.get('/', (req, res) => {
  const sharedData = {
    message: 'Hello from server!',
  };

  const app = (
    <MyContextProvider>
      <App sharedData={sharedData} />
    </MyContextProvider>
  );

  const html = renderToString(app);

  res.send(`
    <html>
      <head></head>
      <body>
        <div id="root">${html}</div>
        <script>
          window.__DATA__ = ${JSON.stringify(sharedData)}
        </script>
        <script src="/client.js"></script>
      </body>
    </html>
  `);
});

server.listen(3000, () => {
  console.log('Server is running on port 3000');
});
```

In this modified SSR server code, the `MyContextProvider` wraps your `App` component. It passes the shared data to the `App` component through a prop.

**4. Hydrate the Client-Side Components:**

On the client side, you can hydrate the React components as previously described, making sure that the `window.__DATA__` variable is available for client-side use.

```javascript
// client.js
import React from 'react';
import { hydrate } from 'react-dom';
import App from './App'; // Your React component

const sharedData = window.__DATA__ || {};

hydrate(<App sharedData={sharedData} />, document.getElementById('root'));
```

By following these steps, you can enhance your SSR setup with context to provide shared data or state to your components during server-side rendering. This can be particularly useful for passing data that's required across multiple components without having to pass it explicitly through props at every level.

Code splitting is a technique used in web development to improve the performance and loading times of web applications by splitting the application's JavaScript code into smaller, more manageable chunks. These smaller chunks are loaded only when they are needed, reducing the initial load time of the application. Code splitting is especially useful for large applications to avoid loading all code upfront.



# Splitting Codes
Here's a basic example of code splitting using JavaScript and the ES modules `import()` function. This example demonstrates how you can split your application into multiple chunks and load them on demand:

**1. Set Up Your Project:**

Create a new project or use an existing one with a modern JavaScript build system like Webpack or create-react-app. These tools often handle code splitting for you.

**2. Create a Modular Application:**

Organize your application into modules, with each module representing a feature or a separate part of your application. For this example, let's create two modules: `moduleA` and `moduleB`.

**3. Use `import()` to Dynamically Load Modules:**

In your JavaScript code, use the `import()` function to dynamically load modules when needed. This is where code splitting happens. You specify the path to the module you want to load, and the `import()` function returns a promise that resolves to the module's exports.

```javascript
// App.js
import React, { useState } from 'react';

function App() {
  const [showModuleA, setShowModuleA] = useState(false);
  const [showModuleB, setShowModuleB] = useState(false);

  const loadModuleA = () => {
    import('./moduleA').then((moduleA) => {
      // Now you can use moduleA and render its content
      setShowModuleA(true);
    });
  };

  const loadModuleB = () => {
    import('./moduleB').then((moduleB) => {
      // Now you can use moduleB and render its content
      setShowModuleB(true);
    });
  };

  return (
    <div>
      <button onClick={loadModuleA}>Load Module A</button>
      <button onClick={loadModuleB}>Load Module B</button>
      {showModuleA && <ModuleA />}
      {showModuleB && <ModuleB />}
    </div>
  );
}

export default App;
```

In the example above, we have an `App` component that contains buttons to load `ModuleA` and `ModuleB` using the `import()` function.

**4. Configure Your Build Tool:**

If you are using a build tool like Webpack, ensure that it's set up to handle code splitting. This may involve specifying entry points for your modules and configuring output settings.

For example, in a Webpack configuration, you can use the `entry` and `output` properties:

```javascript
// webpack.config.js
module.exports = {
  entry: {
    main: './src/index.js', // Main entry point
  },
  output: {
    filename: '[name].bundle.js', // Use [name] to generate multiple output files
    path: path.resolve(__dirname, 'dist'),
  },
};
```

**5. Build and Serve Your Application:**

Build your application using your chosen build tool. This will generate separate JavaScript bundles for each module. Serve your application, and when you click the buttons in the `App` component, the corresponding modules will be loaded dynamically.

With this basic setup, your application will load only the code that is needed when it's needed, resulting in faster initial load times and better performance. This is particularly beneficial for larger applications with complex features.

## Splitting code based on routes

Splitting code based on routes is a common use case in web applications, especially in large projects. This approach allows you to load only the JavaScript code that is required for a specific route, improving the initial load time and overall performance. Here's how you can split code based on routes in a React application using the popular library `react-router` and code splitting:

**1. Set Up Your React Application:**

First, make sure you have a React application set up with `react-router` for handling routing. You can create a new application or modify an existing one. If you haven't already installed `react-router`, you can do so using:

```bash
npm install react-router-dom
```

**2. Create Route Components:**

For each route in your application, create a separate component. These components will be loaded on-demand when the user navigates to a specific route.

```javascript
// Home.js
import React from 'react';

function Home() {
  return (
    <div>
      <h1>Home</h1>
      {/* Your home page content */}
    </div>
  );
}

export default Home;
```

```javascript
// About.js
import React from 'react';

function About() {
  return (
    <div>
      <h1>About</h1>
      {/* About page content */}
    </div>
  );
}

export default About;
```

**3. Configure React Router:**

Set up your routing configuration using `react-router`. Import the route components you created in the previous step and define your routes.

```javascript
// App.js
import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Home from './Home';
import About from './About';

function App() {
  return (
    <Router>
      <div>
        <Switch>
          <Route path="/" exact component={Home} />
          <Route path="/about" component={About} />
        </Switch>
      </div>
    </Router>
  );
}

export default App;
```

**4. Code Splitting with React Lazy and Suspense:**

To enable code splitting, use React's built-in `lazy` and `Suspense` components. Wrap the route components with `lazy` to load them asynchronously, and wrap your `Switch` component with `Suspense` to handle the loading state.

```javascript
import React, { lazy, Suspense } from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';

const Home = lazy(() => import('./Home'));
const About = lazy(() => import('./About'));

function App() {
  return (
    <Router>
      <div>
        <Suspense fallback={<div>Loading...</div>}>
          <Switch>
            <Route path="/" exact component={Home} />
            <Route path="/about" component={About} />
          </Switch>
        </Suspense>
      </div>
    </Router>
  );
}

export default App;
```

With this configuration, when a user navigates to a specific route, only the JavaScript code for that route will be loaded asynchronously. The `Suspense` component displays the "Loading..." message while the code is being fetched. Once the code is loaded, the corresponding route component will be displayed.

**5. Build and Serve Your Application:**

Build your application using your chosen build tool (e.g., Webpack) to generate separate JavaScript bundles for each route component. Then, serve your application.

This approach allows you to split your code based on routes, ensuring that your application loads only what is necessary for the currently active route. It's a powerful technique for optimizing performance, especially in large and complex applications.

## WHEN TO USE CODE SPLITTING

Code splitting is a technique that should be used strategically to improve the performance and user experience of web applications. Here are some common scenarios and considerations for when to use code splitting:

1. **Large Web Applications**: Code splitting is especially valuable in large web applications with many components, features, and routes. Loading all code upfront can lead to slow initial page loads, while code splitting allows you to load code as needed.

2. **Complex User Interfaces**: If your application has complex user interfaces with multiple features and components, code splitting can help reduce the initial JavaScript payload, leading to faster loading times.

3. **Mobile and Slow Networks**: Users on mobile devices or slower network connections will benefit significantly from code splitting. Reducing the amount of code that needs to be loaded upfront can make the application more responsive.

4. **Route-Based Splitting**: Code splitting is commonly used in route-based splitting. Load code for a specific route when the user navigates to that route. This approach is useful in single-page applications (SPAs) with multiple views or pages.

5. **Dynamic Imports**: When you have components or features that are conditionally rendered or used only in response to user interactions (e.g., modals, popovers, or advanced form components), using dynamic imports can help load the code only when needed.

6. **Performance Optimization**: Code splitting can be an essential performance optimization tool. By reducing the amount of JavaScript that needs to be parsed and executed during the initial load, you can achieve better Time to Interactive (TTI) and overall page speed.

7. **SEO Considerations**: For SEO purposes, it's important to ensure that critical content for search engines is included in the initial HTML response. Code splitting for non-essential JavaScript can help balance SEO requirements with performance needs.

8. **Reduce Bundle Size**: Smaller bundle sizes can lead to faster loading times, which is a critical factor in retaining users and reducing bounce rates. Code splitting is one way to reduce bundle size.

9. **Caching**: Code splitting can also work well with caching. When code is split, the browser can cache common dependencies, such as libraries or frameworks, for faster subsequent loads.

10. **Optimize User Experience**: In some cases, code splitting can improve the overall user experience. For example, you can load the core functionality of a web app first and then load additional, non-critical features in the background.

11. **Avoiding Overhead**: Reducing the amount of code that is initially loaded helps avoid overhead, especially when using libraries and frameworks that may introduce extra code you don't need right away.

12. **Progressive Web Apps (PWAs)**: Code splitting is a common practice in PWAs, where you load only the necessary code for the initial route and prefetch other routes as the user interacts with the application.


## FUNCTION VS FEATURE BASED ORGANIZATION

理解"Function-Based Organization"和"Feature-Based Organization"的最佳方法之一是通过实际示例来演示它们的差异。我将为您提供两个示例，一个采用函数式组织，另一个采用特征式组织，使用同一个React项目，并演示如何组织和结构代码。

**示例1：Function-Based Organization**

在这个示例中，我们将以函数式组织的方式构建一个购物车应用，其中功能是主要的组织结构。每个功能（如添加商品、删除商品、计算总价等）都将在自己的模块中进行组织。

```plaintext
my-shopping-cart-app/
|-- src/
|   |-- components/
|   |   |-- AddToCartButton.js
|   |   |-- CartItemList.js
|   |   |-- CartTotal.js
|   |   |-- RemoveFromCartButton.js
|   |-- features/
|   |   |-- Cart/
|   |   |   |-- Cart.js
|   |   |   |-- cartReducer.js
|   |   |   |-- cartActions.js
|   |   |   |-- cartSelectors.js
|   |-- App.js
|   |-- index.js
```

在这个示例中，`components` 文件夹包含了可重用的组件，而 `features` 文件夹将购物车功能模块化组织。

**示例2：Feature-Based Organization**

在这个示例中，我们将以特征式组织的方式构建相同的购物车应用。每个特征（如购物车、商品列表、商品详情等）都将有自己的文件夹，包括其相关组件、状态管理和路由。

```plaintext
my-shopping-cart-app/
|-- src/
|   |-- features/
|   |   |-- Cart/
|   |   |   |-- components/
|   |   |   |   |-- Cart.js
|   |   |   |   |-- CartTotal.js
|   |   |   |-- store/
|   |   |   |   |-- cartReducer.js
|   |   |   |   |-- cartActions.js
|   |   |   |   |-- cartSelectors.js
|   |   |-- ProductList/
|   |   |   |-- components/
|   |   |   |   |-- Product.js
|   |   |   |-- store/
|   |   |   |   |-- productListReducer.js
|   |   |   |   |-- productListActions.js
|   |   |   |   |-- productListSelectors.js
|   |-- App.js
|   |-- index.js
```

在这个示例中，每个特征拥有其独立的文件夹，包括组件、状态管理和路由。这种方法使得不同特征之间更加独立，容易维护和开发。

这两个示例演示了如何使用不同的组织方式来构建相同的应用。您可以选择哪种方式更适合您的项目，具体取决于项目的规模、复杂性以及团队的需求。无论哪种方式，重要的是建立清晰的代码组织约定，以确保一致性和可维护性。


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

这个表格提供了对这三种组织方法的简要比较，可以帮助您更好地了解它们的特征和适用情况。您可以根据您的项目需求和团队结构来选择合适的组织方式。

## CI/CD PIPLINE

| 阶段                | 描述                                                                                      |
|---------------------|-------------------------------------------------------------------------------------------|
| 源码（Source）      | 开发人员提交代码更改到源代码库。                                                       |
| 构建（Build）       | 自动构建过程，编译代码并生成可执行的构建版本。                                          |
| 测试（Test）        | 运行自动化测试来验证代码质量和功能。                                                   |
| 打包（Package）      | 准备应用程序以进行部署，例如创建容器映像或构建存档。                                     |
| 部署（Deployment）  | 将应用程序自动部署到测试环境、预发布环境或生产环境。                                    |
| 监测（Monitoring）  | 持续监测应用程序以检测问题并记录性能指标。                                             |
这个表格描述了一个典型的CI/CD管线的主要阶段，从代码提交到最终的监测和性能评估。每个阶段都有其特定的任务和目标，有助于确保代码质量、自动化部署和持续监测。在实际项目中，这些阶段的具体实现和工具可以根据项目需求和团队的偏好而有所不同。
