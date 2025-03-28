---
aliases:
  - React-Redux
source: 
author: 
createdAt: 
updateAt: 
categories: 
high_priority: false
tags:
  - Effective/Tools
---
```js
store.subscribe(()=>{
	ReactDom.render(<App/>,document.getElementById('root'))
})
```

![image.png](https://cdn.jsdelivr.net/gh/duanbiao2000/BlogGallery@main/picture/20240816134351.png)

## 用 React-Redux 写容器组件

### 理解容器组件

在 React-Redux 中，容器组件（Container Component）是专门负责连接 Redux store 和 UI 组件的组件。它们从 Redux store 中获取数据，并将其作为 props 传递给 UI 组件。此外，容器组件还可以 dispatch action 来更新 store。
![image.png](https://cdn.jsdelivr.net/gh/duanbiao2000/BlogGallery@main/picture/20240816140009.png)
**容器组件的主要职责：**

- **连接 Redux store:** 使用 `connect` 高阶组件将组件连接到 Redux store。
- **映射 state:** 将 Redux store 中需要的数据映射到组件的 props 上。
- **映射 dispatch:** 将组件的事件处理函数映射到 dispatch action 的函数上。

### 写一个容器组件的示例

```js
import React from 'react';
import { connect } from 'react-redux';
import { increment, decrement } from '../actions';
import Counter from './Counter'; // UI 组件

// 容器组件
const CounterContainer = ({ count, increment, decrement }) => {
  return <Counter count={count} onIncrement={increment} onDecrement={decrement} />;
};

// 将 state 映射到组件的 props
const mapStateToProps = state => ({
  count: state.count
});

// 将 dispatch 映射到 props
const mapDispatchToProps = dispatch => ({
  increment: () => dispatch(increment()),
  decrement: () => dispatch(decrement())
});

export default connect(mapStateToProps, mapDispatchToProps)(CounterContainer);
```

**代码解释：**

1. **导入：** 导入 `connect` 高阶组件、action creators 和 UI 组件。
2. **创建容器组件：**
    - 接收 `count`、`increment` 和 `decrement` 作为 props。
    - 将这些 props 传递给 UI 组件 `Counter`。
3. **映射 state：**
    - `mapStateToProps` 函数将 Redux store 中的 `count` 状态映射到组件的 `count` props 上。
4. **映射 dispatch：**
    - `mapDispatchToProps` 函数将 `increment` 和 `decrement` action creators 映射到组件的 `onIncrement` 和 `onDecrement` props 上。
5. **连接组件：**
    - 使用 `connect` 高阶组件将容器组件连接到 Redux store，并传入 `mapStateToProps` 和 `mapDispatchToProps`。


> [!NOTE] Title
> 这段代码就是把一个普通的 React 组件 `CounterContainer` 变成了一个与 Redux store 相连接的容器组件。它使得 `CounterContainer` 可以访问 Redux store 中的数据，并且可以通过 dispatch action 来修改 store 中的数据。
> 
> **`connect`:**
> - 这是 `react-redux` 提供的一个高阶组件（Higher-Order Component，HOC）。它的作用是将一个普通的 React 组件连接到 Redux store 上。

### 容器组件和 UI 组件的区别

- **容器组件：**
    - 与 Redux store 紧密耦合。
    - 负责数据获取和分发。
    - 不包含 UI 逻辑。
- **UI 组件：**
    - 纯粹的 UI 组件，只负责展示。
    - 接收从容器组件传递过来的 props。
    - 不直接与 Redux store 交互。

### 总结

容器组件是 React-Redux 中非常重要的概念，它将 Redux store 和 UI 组件连接起来，使得数据流变得清晰和可管理。通过将数据获取和分发逻辑集中在容器组件中，可以保持 UI 组件的纯净和可重用性。

**使用容器组件的好处：**

- **清晰的数据流:** 组件之间的数据传递更加明确。
- **可复用性:** UI 组件可以独立于 Redux store 存在。
- **可测试性:** 容器组件和 UI 组件可以分别进行测试。
<!--SR:!2000-01-01,1,250!2000-01-01,1,250!2025-03-21,4,270-->

**需要注意的点：**

- **过度使用容器组件:** 如果每个组件都连接到 Redux store，可能会导致代码变得复杂。
- **性能优化:** 对于频繁更新的组件，可以考虑使用 `reselect` 等库来优化性能。



## React-Redux 和 Redux Toolkit 的区别

### React-Redux

- **定义:** React-Redux 是一个用于将 Redux 集成到 React 应用程序中的官方库。它提供了一系列工具和 API，使得在 React 组件中管理全局状态变得更加方便。
- **主要功能:**
    - **Provider:** 将 Redux store 连接到 React 应用程序的根组件。
    - **connect:** 将 React 组件连接到 Redux store，使得组件可以访问 store 中的状态并 dispatch action。
    - **useSelector:** (React Hooks API) 允许函数式组件从 Redux store 中选择数据。
    - **useDispatch:** (React Hooks API) 允许函数式组件 dispatch action。
- **作用:**
    - 建立 React 和 Redux 之间的桥梁。
    - 简化在 React 组件中使用 Redux 的方式。

### Redux Toolkit

- **定义:** Redux Toolkit 是一个官方的、面向生产环境的工具集，用于简化 Redux 的使用。它提供了一组工具和函数，可以帮助你快速地创建 Redux store 和编写 Redux logic。
- **主要功能:**
    - **configureStore:** 一个函数，用于创建 Redux store，它包含了默认的中间件和增强器，简化了 store 的配置。
    - **createSlice:** 一个函数，用于创建 Redux slice，将 reducer 的逻辑、action creators 和初始状态封装在一起。
    - **createAsyncThunk:** 一个函数，用于创建异步 action creator，简化了异步操作的处理。
    - **immer:** 集成了 Immer 库，使得我们可以以一种更直观的方式来修改 state。
- **作用:**
    - 简化 Redux 的配置和开发。
    - 提供了一些常用的工具函数，提高开发效率。
    - 鼓励最佳实践，如将 reducer 分割成多个 slice。

### 两者的关系和区别

- **React-Redux 是 Redux 的官方 React 绑定库**，而 **Redux Toolkit 是 Redux 的官方工具集**。
- **React-Redux 主要负责连接 React 和 Redux**，而 **Redux Toolkit 主要关注 Redux 本身的开发体验**。
- **Redux Toolkit 可以看作是 Redux 的最佳实践的集合**，它提供了一系列工具和函数，帮助开发者更好地使用 Redux。
- **React-Redux 仍然需要与 Redux Toolkit 一起使用**，以实现 React 组件和 Redux store 之间的连接。

### 总结

- **React-Redux** 是必不可少的，它负责连接 React 和 Redux。
- **Redux Toolkit** 是可选的，但它可以极大地简化 Redux 的开发过程。

**何时使用 Redux Toolkit？**

- 当你希望简化 Redux 的配置和开发时。
- 当你希望遵循 Redux 的最佳实践时。
- 当你需要处理异步操作时，`createAsyncThunk` 可以大大简化你的代码。


- React-Redux: [https://react-redux.js.org/](https://react-redux.js.org/)
- Redux Toolkit: https://redux-toolkit.js.org/



















