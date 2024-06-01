---
aliases:

---
20230719 1823
links: [useReducer – React](https://zh-hans.react.dev/reference/react/useReducer)
title:
origin:
tags: #flashcards #todo 







### `useReducer(reducer, initialArg, init?)` [](https://zh-hans.react.dev/reference/react/useReducer#usereducer "Link for this heading")

在组件的顶层作用域调用 `useReducer` 以创建一个用于管理状态的 [reducer](https://zh-hans.react.dev/learn/extracting-state-logic-into-a-reducer)。

```js
import { useReducer } from 'react';  


function reducer(state, action) {  

// ...  

}  

function MyComponent() {  

const [state, dispatch] = useReducer(reducer, { age: 42 });  

// ...
```

[参见下方更多示例](https://zh-hans.react.dev/reference/react/useReducer#usage)。

#### 参数 [](https://zh-hans.react.dev/reference/react/useReducer#parameters "Link for 参数")

- `reducer`：用于更新 state 的纯函数。参数为 state 和 action，返回值是更新后的 state。state 与 action 可以是任意合法值。
- `initialArg`：用于初始化 state 的任意值。初始值的计算逻辑取决于接下来的 `init` 参数。
- **可选参数** `init`：用于计算初始值的函数。如果存在，使用 `init(initialArg)` 的执行结果作为初始值，否则使用 `initialArg`。

#### 返回值 [](https://zh-hans.react.dev/reference/react/useReducer#returns "Link for 返回值")

`useReducer` 返回一个由两个值组成的数组：

1. 当前的 state。初次渲染时，它是 `init(initialArg)` 或 `initialArg` （如果没有 `init` 函数）。
2. [`dispatch` 函数](https://zh-hans.react.dev/reference/react/useReducer#dispatch)。用于更新 state 并触发组件的重新渲染。

#### 注意事项 [](https://zh-hans.react.dev/reference/react/useReducer#caveats "Link for 注意事项")

- `useReducer` 是一个 Hook，所以只能在 **组件的顶层作用域** 或自定义 Hook 中调用，而不能在循环或条件语句中调用。如果你有这种需求，可以创建一个新的组件，并把 state 移入其中。
- 严格模式下 React 会 **调用两次 reducer 和初始化函数**，这可以 [帮助你发现意外的副作用](https://zh-hans.react.dev/reference/react/useReducer#my-reducer-or-initializer-function-runs-twice)。这只是开发模式下的行为，并不会影响生产环境。只要 reducer 和初始化函数是纯函数（理应如此）就不会改变你的逻辑。其中一个调用结果会被忽略。


[useReducer – React](https://zh-hans.react.dev/reference/react/useReducer)

action 可以是任意类型，不过通常至少是一个存在 `type` 属性的对象。也就是说它需要携带计算新的 state 值所必须的数据。

```js
function Form() {   

const [state, dispatch] = useReducer(reducer, { name: 'Taylor', age: 42 });  

  

function handleButtonClick() {  

dispatch({ type: 'incremented_age' });  

}  

  

function handleInputChange(e) {  

dispatch({  

type: 'changed_name',  

nextName: e.target.value  

});  

}  

// ...
```

action 的 type 依赖于组件的实际情况。[即使它会导致数据的多次更新，每个 action 都只描述一次交互](https://zh-hans.react.dev/learn/extracting-state-logic-into-a-reducer#writing-reducers-well)。state 的类型也是任意的，不过一般会使用对象或数组。

阅读 [迁移状态逻辑至 Reducer 中](https://zh-hans.react.dev/learn/extracting-state-logic-into-a-reducer) 来了解更多内容。

### 陷阱

state 是只读的。即使是对象或数组也不要尝试修改它：

```js
function reducer(state, action) {   

switch (action.type) {  

case 'incremented_age': {  

// 🚩 不要像下面这样修改一个对象类型的 state：  

state.age = state.age + 1;  

return state;  

}
```
function reducer(state, action) {   



正确的做法是返回新的对象：

```js
function reducer(state, action) {  

switch (action.type) {  

case 'incremented_age': {  

// ✅ 正确的做法是返回新的对象  

return {  

...state,  

age: state.age + 1  

};  

}
```

#### useReducer 的基础示例[](https://zh-hans.react.dev/reference/react/useReducer#examples-basic "Link for useReducer 的基础示例")


第 1 个示例 共 3 个挑战: 

表单（对象类型） [](https://zh-hans.react.dev/reference/react/useReducer#form-object "Link for this heading")

在这个示例中，state 是一个有 `name` 和 `age` 属性的对象。
```js
import { useReducer } from 'react';

function reducer(state, action) {
  switch (action.type) {
    case 'incremented_age': {
      return {
        name: state.name,
        age: state.age + 1
      };
    }
    case 'changed_name': {
      return {
        name: action.nextName,
        age: state.age
      };
    }
  }
  throw Error('Unknown action: ' + action.type);
}

const initialState = { name: 'Taylor', age: 42 };

export default function Form() {
  const [state, dispatch] = useReducer(reducer, initialState);

  function handleButtonClick() {
    dispatch({ type: 'incremented_age' });
  }

  function handleInputChange(e) {
    dispatch({
      type: 'changed_name',
      nextName: e.target.value
    }); 
  }

  return (
    <>
      <input
        value={state.name}
        onChange={handleInputChange}
      />
      <button onClick={handleButtonClick}>
        Increment age
      </button>
      <p>Hello, {state.name}. You are {state.age}.</p>
    </>
  );
}

```


#### 

第 2 个示例 共 3 个挑战: 

代办事项（数组类型） [](https://zh-hans.react.dev/reference/react/useReducer#todo-list-array "Link for this heading")

在这个示例中，reducer 管理一个名为 tasks 的数组。数组 [不能使用修改方法](https://zh-hans.react.dev/learn/updating-arrays-in-state) 来更新。
```js
import { useReducer } from 'react';
import AddTask from './AddTask.js';
import TaskList from './TaskList.js';

function tasksReducer(tasks, action) {
  switch (action.type) {
    case 'added': {
      return [...tasks, {
        id: action.id,
        text: action.text,
        done: false
      }];
    }
    case 'changed': {
      return tasks.map(t => {
        if (t.id === action.task.id) {
          return action.task;
        } else {
          return t;
        }
      });
    }
    case 'deleted': {
      return tasks.filter(t => t.id !== action.id);
    }
    default: {
      throw Error('Unknown action: ' + action.type);
    }
  }
```

#### 

第 3 个示例 共 3 个挑战: 

使用 Immer 编写简洁的更新逻辑 [](https://zh-hans.react.dev/reference/react/useReducer#writing-concise-update-logic-with-immer "Link for this heading")

如果使用复制方法更新数组和对象让你不厌其烦，那么可以使用 [Immer](https://github.com/immerjs/use-immer#useimmerreducer) 这样的库来减少一些重复的样板代码。Immer 让你可以专注于逻辑，因为它在内部均使用复制方法来完成更新：


```javascript
// Importing the useImmerReducer hook from 'use-immer' library. This hook is used to manage complex state in a more readable way.
import { useImmerReducer } from 'use-immer';

// Importing the AddTask and TaskList components from local files.
import AddTask from './AddTask.js';
import TaskList from './TaskList.js';

// This is a reducer function that takes the current state (draft) and an action, and returns the new state based on the action type.
function tasksReducer(draft, action) {
  switch (action.type) {
    case 'added': {
      // When the action type is 'added', a new task is added to the state.
      draft.push({
        id: action.id,
        text: action.text,
        done: false
      });
      break;
    }
    case 'changed': {
      // When the action type is 'changed', the task with the given id is updated.
      const index = draft.findIndex(t =>
        t.id === action.task.id
      );
      draft[index] = action.task;
      break;
    }
    case 'deleted': {
      // When the action type is 'deleted', the task with the given id is removed from the state.
      return draft.filter(t => t.id !== action.id);
    }
    default: {
      // If the action type is not recognized, an error is thrown.
      throw Error('Unknown action: ' + action.type);
    }
  }
}

// This is the main component of the application.
export default function TaskApp() {
  // The useImmerReducer hook is used to manage the state of the tasks. It takes the reducer function and the initial state as arguments.
  const [tasks, dispatch] = useImmerReducer(
    tasksReducer,
    initialTasks
  );

  // This function is used to add a new task. It dispatches an 'added' action with the task id and text.
  function handleAddTask(text) {
    dispatch({
      type: 'added',
      id: nextId++,
      text: text,
    });
  }

  // This function is used to update a task. It dispatches a 'changed' action with the updated task.
  function handleChangeTask(task) {
    dispatch({
      type: 'changed',
      task: task
    });
  }

  // This function is used to delete a task. It dispatches a 'deleted' action with the id of the task to be deleted.
  function handleDeleteTask(taskId) {
    dispatch({
      type: 'deleted',
      id: taskId
    });
  }

  // The component renders a title, the AddTask component, and the TaskList component. The tasks and the handler functions are passed as props to the child components.
  return (
    <>
      <h1>Prague itinerary</h1>
      <AddTask
        onAddTask={handleAddTask}
      />
      <TaskList
        tasks={tasks}
        onChangeTask={handleChangeTask}
        onDeleteTask={handleDeleteTask}
      />
    </>
  );
}

// This is a counter for the task ids. It is incremented every time a new task is added.
let nextId = 3;

// This is the initial state of the tasks.
const initialTasks = [
  { id: 0, text: 'Visit Kafka Museum', done: true },
  { id: 1, text: 'Watch a puppet show', done: false },
  { id: 2, text: 'Lennon Wall pic', done: false },
];
```

This code is a simple task management application in React using the useImmerReducer hook for state management. The application allows users to add, update, and delete tasks.


### 避免重新创建初始值 [](https://zh-hans.react.dev/reference/react/useReducer#avoiding-recreating-the-initial-state "Link for 避免重新创建初始值")

React 会保存 state 的初始值并在下一次渲染时忽略它。

```
function createInitialState(username) {  // ...}function TodoList({ username }) {  const [state, dispatch] = useReducer(reducer, createInitialState(username));  // ...
```

虽然 `createInitialState(username)` 的返回值只用于初次渲染，但是在每一次渲染的时候都会被调用。如果它创建了比较大的数组或者执行了昂贵的计算就会浪费性能。

你可以通过给 `useReducer` 的第三个参数传入 **初始化函数** 来解决这个问题：

```
function createInitialState(username) {  // ...}function TodoList({ username }) {  const [state, dispatch] = useReducer(reducer, username, createInitialState);  // ...
```

需要注意的是你传入的参数是 `createInitialState` 这个 **函数自身**，而不是执行 `createInitialState()` 后的返回值。这样传参就可以保证初始化函数不会再次运行。

在上面这个例子中，`createInitialState` 有一个 `username` 参数。如果初始化函数不需要参数就可以计算出初始值，可以把 `useReducer` 的第二个参数改为 `null`。


#### 使用初始化函数和直接传入初始值的区别?
使用初始化函数和直接传入初始值是在使用 `useReducer` 钩子时的两种不同方式。

`useReducer(reducer, initialArg, init?)`
#### 参数 [](https://zh-hans.react.dev/reference/react/useReducer#parameters "Link for 参数")

- `reducer`：用于更新 state 的纯函数。参数为 state 和 action，返回值是更新后的 state。state 与 action 可以是任意合法值。
- `initialArg`：用于初始化 state 的任意值。初始值的计算逻辑取决于接下来的 `init` 参数。
- **可选参数** `init`：用于计算初始值的函数。如果存在，使用 `init(initialArg)` 的执行结果作为初始值，否则使用 `initialArg`。


使用初始化函数时，你可以传入一个函数作为 `useReducer` 的第三个参数。这个函数会在组件初次渲染时被调用，并且它的返回值将作为初始状态值。这样做的好处是，你可以在初始化函数中进行一些逻辑计算，根据需要动态生成初始状态值。这个初始化函数只会在初次渲染时被调用一次，之后不会再被调用。

而直接传入初始值时，你可以将一个固定的值作为 `useReducer` 的第二个参数。这个固定值将作为初始状态值。这种方式适用于初始状态值是固定的情况，不需要进行额外的逻辑计算。

使用初始化函数和直接传入初始值的区别在于灵活性和计算逻辑。使用初始化函数可以根据需要动态生成初始状态值，而直接传入初始值则适用于固定的初始状态值。具体使用哪种方式取决于你的需求和代码逻辑。


 ` const [state, dispatch] = useReducer(reducer, { age: 42 });`

这行代码使用了 `useReducer` 钩子函数来创建一个状态 `state` 和一个分发函数 `dispatch`。`reducer` 是一个纯函数，它接收当前状态 `state` 和一个动作 `action`，并返回新的状态。在这个例子中，初始状态是一个对象 `{ age: 42 }`。

通过使用 `useReducer`，我们可以将状态和状态更新逻辑封装在一个地方，以便更好地管理复杂的状态变化。当我们调用 `dispatch` 函数并传递一个动作时，`reducer` 函数将被调用，并根据动作的类型来更新状态。在这个例子中，我们可以通过调用 `dispatch({ type: 'increaseAge' })` 来增加年龄。

使用 `useReducer` 可以更好地组织和管理状态，特别适用于需要处理复杂状态逻辑的场景。它提供了一种可预测和可维护的方式来处理状态更新。

```js
import { useReducer } from 'react';

function reducer(state, action) {
  if (action.type === 'incremented_age') {
    return {
      age: state.age + 1
    };
  }
  throw Error('Unknown action.');
}

export default function Counter() {
  const [state, dispatch] = useReducer(reducer, { age: 42 });

  return (
    <>
      <button onClick={() => {
        dispatch({ type: 'incremented_age' })
      }}>
        Increment age
      </button>
      <p>Hello! You are {state.age}.</p>
    </>
  );
}

```

你需要往函数体里面添加计算并返回新的 state 的逻辑。一般会使用 [`switch` 语句](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Statements/switch) 来完成。在 `switch` 语句中通过匹配 `case` 条件来计算并返回相应的 state。

```js
function reducer(state, action) {  
	switch (action.type) {  
		case 'incremented_age': {  
			return {  
			
				name: state.name,  
				
				age: state.age + 1  
			};  
		}  
		case 'changed_name': {  
		
			return {  
			
				name: action.nextName,  
				
				age: state.age  
		
			};  
		
		}  
	}  
	throw Error('Unknown action: ' + action.type);
}
```

action 可以是任意类型，不过通常至少是一个存在 `type` 属性的对象。也就是说它需要携带计算新的 state 值所必须的数据。

```js
function Form() {  
	const [state, dispatch] = useReducer(reducer, { name: 'Taylor', age: 42 });  
	
	function handleButtonClick() {  
	dispatch({ type: 'incremented_age' });  
}  

	function handleInputChange(e) {  
	dispatch({  
	type: 'changed_name',  
	nextName: e.target.value  
	});  
}  
// ...
```

action 的 type 依赖于组件的实际情况。[即使它会导致数据的多次更新，每个 action 都只描述一次交互](https://zh-hans.react.dev/learn/extracting-state-logic-into-a-reducer#writing-reducers-well)。state 的类型也是任意的，不过一般会使用对象或数组。

### 在 dispatch 后 state 的某些属性变为了 `undefined`

请确保每个 `case` 语句中所返回的新的 state **都复制了当前的属性**：

```js
function reducer(state, action) {  

	switch (action.type) {  
	
		case 'incremented_age': {  
		
			return {  
			
			...state, // 不要忘记复制之前的属性！  
			
			age: state.age + 1  
			
			};  
		}  
// ...
```


### 我收到了一个报错：“Too many re-renders” [](https://zh-hans.react.dev/reference/react/useReducer#im-getting-an-error-too-many-re-renders "Link for 我收到了一个报错：“Too many re-renders”")

你可能会收到这样一条报错信息：`Too many re-renders. React limits the number of renders to prevent an infinite loop.`。这通常是在 **渲染期间** dispatch 了 action 而导致组件进入了无限循环：dispatch（会导致一次重新渲染）、渲染、dispatch（再次导致重新渲染），然后无限循环。大多数这样的错误是由于事件处理函数中存在错误的逻辑：

```js
// 🚩 错误：渲染期间调用了处理函数
return <button onClick={handleClick()}>Click me</button>
// ✅ 修复：传递一个处理函数，而不是调用
return <button onClick={handleClick}>Click me</button>
// ✅ 修复：传递一个内联的箭头函数
return <button onClick={(e) => handleClick(e)}>Click me</button>
```



#### useRef

第 1 个示例 共 2 个挑战: 

点击计数器 [](https://zh-hans.react.dev/reference/react/useRef#click-counter "Link for this heading")

这个组件使用 ref 来记录按钮被点击的次数。注意，在这里使用 ref 而不是 state 是可以的，因为点击次数只在事件处理程序中被读取和写入。
```js
import { useRef } from 'react';

export default function Counter() {
  let ref = useRef(0);

  function handleClick() {
    ref.current = ref.current + 1;
    alert('You clicked ' + ref.current + ' times!');
  }

  return (
    <button onClick={handleClick}>
      Click me!
    </button>
  );
}

```

#### 

第 2 个示例 共 2 个挑战: 

秒表 [](https://zh-hans.react.dev/reference/react/useRef#a-stopwatch "Link for this heading")

这个例子使用了 state 和 ref 的组合。`startTime` 和 `now` 都是 state 变量，因为它们是用来渲染的。但是我们还需要持有一个 [interval ID](https://developer.mozilla.org/zh-CN/docs/Web/API/setInterval)，这样我们就可以在按下按钮时停止定时器。因为 interval ID 不用于渲染，所以应该把它保存在一个 ref 中，并且手动更新它。
```js
import { useState, useRef } from 'react';

export default function Stopwatch() {
  const [startTime, setStartTime] = useState(null);
  const [now, setNow] = useState(null);
  const intervalRef = useRef(null);

  function handleStart() {
    setStartTime(Date.now());
    setNow(Date.now());

    clearInterval(intervalRef.current);
    intervalRef.current = setInterval(() => {
      setNow(Date.now());
    }, 10);
  }

  function handleStop() {
    clearInterval(intervalRef.current);
  }

  let secondsPassed = 0;
  if (startTime != null && now != null) {
    secondsPassed = (now - startTime) / 1000;
  }

  return (
    <>
      <h1>Time passed: {secondsPassed.toFixed(3)}</h1>
      <button onClick={handleStart}>
        Start
      </button>
      <button onClick={handleStop}>
        Stop
      </button>
    </>
  );
}

```

### useState

### 根据先前的 state 更新 state [](https://zh-hans.react.dev/reference/react/useState#updating-state-based-on-the-previous-state "Link for 根据先前的 state 更新 state")

假设 `age` 为 `42`，这个处理函数三次调用 `setAge(age + 1)`：

```js
function handleClick() {  
	setAge(age + 1); // setAge(42 + 1)  
	setAge(age + 1); // setAge(42 + 1)  
	setAge(age + 1); // setAge(42 + 1)}
```

然而，点击一次后，`age` 将只会变为 `43` 而不是 `45`！这是因为调用 `set` 函数 [不会更新](https://zh-hans.react.dev/learn/state-as-a-snapshot) 已经运行代码中的 `age` 状态变量。因此，每个 `setAge(age + 1)` 调用变成了 `setAge(43)`。

为了解决这个问题，**你可以向 `setAge` 传递一个 _更新函数_**，而不是下一个状态：

```js
function handleClick() {
	setAge(a => a + 1); // setAge(42 => 43)
	setAge(a => a + 1); // setAge(43 => 44) 
	setAge(a => a + 1); // setAge(44 => 45)}
```

### 更新状态中的对象和数组 [](https://zh-hans.react.dev/reference/react/useState#updating-objects-and-arrays-in-state "Link for 更新状态中的对象和数组")

你可以将对象和数组放入状态中。在 React 中，状态被认为是只读的，因此 **你应该替换它而不是改变现有对象**。例如，如果你在状态中保存了一个 `form` 对象，请不要改变它：

```js
// 🚩 不要像下面这样改变一个对象：
form.firstName = 'Taylor';
```

相反，可以通过创建一个新对象来替换整个对象：

```js
// ✅ 使用新对象替换 
statesetForm({  ...form,  firstName: 'Taylor'});
```


