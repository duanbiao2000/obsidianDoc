---
page-title: "Tutorials Overview | Redux Toolkit"
url: https://redux-toolkit.js.org/tutorials/overview
date: "2023-07-18 23:17:40"
---

**The Redux core docs site at [https://redux.js.org](https://redux.js.org/) contains the primary tutorials for learning Redux**, including how to use Redux Toolkit and React-Redux together.

### Redux Toolkit Example[​](https://redux.js.org/introduction/getting-started#redux-toolkit-example "Direct link to heading")

Redux Toolkit simplifies the process of writing Redux logic and setting up the store. With Redux Toolkit, that same logic looks like:
这段代码使用了 Redux Toolkit 中的 `createSlice` 和 `configureStore` 函数来简化 Redux 的创建和管理过程。以下是对代码的详细注释：
```javascript
import { createSlice, configureStore } from '@reduxjs/toolkit';
// 创建 Redux Slice
const counterSlice = createSlice({
  name: 'counter', // Slice 的名称
  initialState: {
    value: 0, // 初始状态值
  },
  reducers: {
    incremented: state => {
      // Redux Toolkit 允许我们在 reducer 函数中进行 "mutating" 的逻辑。它不会直接修改状态，而是使用 Immer 库，
      // 检测到对 "draft state" 的更改，并基于这些更改生成一个全新的不可变状态
      state.value += 1;
    },
    decremented: state => {
      state.value -= 1;
    },
  },
});
// 导出 action 创建函数
export const { incremented, decremented } = counterSlice.actions;
// 创建 Redux store
const store = configureStore({
  reducer: counterSlice.reducer, // 设置 reducer
});
// 仍然可以订阅 store 更新
store.subscribe(() => console.log(store.getState()));
// 可以使用 action 创建函数来调度 action
store.dispatch(incremented());
// {value: 1}
store.dispatch(incremented());
// {value: 2}
store.dispatch(decremented());
// {value: 1}
```
这段代码使用了 Redux Toolkit 提供的 `createSlice` 函数来创建 Redux Slice，它简化了 reducer 和 action 的创建。`configureStore` 函数用于创建 Redux store，将 reducer 传递给 `reducer` 属性。
通过 `createSlice` 函数创建的 Redux Slice，会自动生成包含了定义的 reducer 函数和对应的 action 创建函数的对象。我们可以通过解构赋值的方式将这些 action 创建函数导出，然后在其他地方使用。
在这段代码中，我们创建了一个名为 `counter` 的 Redux Slice，包含了 `incremented` 和 `decremented` 两个 action 创建函数和对应的 reducer 逻辑。然后，我们使用 `configureStore` 函数创建 Redux store，并将 `counterSlice.reducer` 作为 reducer 传递给 `reducer` 属性。
最后，我们可以使用生成的 action 创建函数来调度 action，通过 `store.dispatch()` 方法将 action 分发给 Redux store。我们也可以通过 `store.subscribe()` 方法订阅 store 的更新，以便在 store 变化时执行相应的回调函数。
Redux Toolkit 还提供了许多其他功能，如异步 action 的处理、内置的状态持久化、性能优化等。上述代码只是简单示例了 Redux Toolkit 的一些用法。

Redux Toolkit allows us to write shorter logic that's easier to read, while still following the same Redux behavior and data flow.

## Learn Redux[​](https://redux.js.org/introduction/getting-started#learn-redux "Direct link to heading")

We have a variety of resources available to help you learn Redux.

### Redux Essentials Tutorial[​](https://redux.js.org/introduction/getting-started#redux-essentials-tutorial "Direct link to heading")

The [**Redux Essentials tutorial**](https://redux.js.org/tutorials/essentials/part-1-overview-concepts) is a "top-down" tutorial that teaches "how to use Redux the right way", using our latest recommended APIs and best practices. We recommend starting there.

### Redux Fundamentals Tutorial[​](https://redux.js.org/introduction/getting-started#redux-fundamentals-tutorial "Direct link to heading")

The [**Redux Fundamentals tutorial**](https://redux.js.org/tutorials/fundamentals/part-1-overview) is a "bottom-up" tutorial that teaches "how Redux works" from first principles and without any abstractions, and why standard Redux usage patterns exist.

### Learn Modern Redux Livestream[​](https://redux.js.org/introduction/getting-started#learn-modern-redux-livestream "Direct link to heading")

Redux maintainer Mark Erikson appeared on the "Learn with Jason" show to explain how we recommend using Redux today. The show includes a live-coded example app that shows how to use Redux Toolkit and React-Redux hooks with TypeScript, as well as the new RTK Query data fetching APIs.

See [the "Learn Modern Redux" show notes page](https://www.learnwithjason.dev/let-s-learn-modern-redux) for a transcript and links to the example app source.

### Additional Tutorials[​](https://redux.js.org/introduction/getting-started#additional-tutorials "Direct link to heading")

- The Redux repository contains several example projects demonstrating various aspects of how to use Redux. Almost all examples have a corresponding CodeSandbox sandbox. This is an interactive version of the code that you can play with online. See the complete list of examples in the **[Examples page](https://redux.js.org/introduction/examples)**.
- Redux creator Dan Abramov's **free ["Getting Started with Redux" video series](https://app.egghead.io/playlists/fundamentals-of-redux-course-from-dan-abramov-bd5cc867)** and **[Building React Applications with Idiomatic Redux](https://egghead.io/courses/building-react-applications-with-idiomatic-redux)** video courses on Egghead.io
- Redux maintainer Mark Erikson's **["Redux Fundamentals" conference talk](https://blog.isquaredsoftware.com/2018/03/presentation-reactathon-redux-fundamentals/)** and [**"Redux Fundamentals" workshop slides**](https://blog.isquaredsoftware.com/2018/06/redux-fundamentals-workshop-slides/)
- Dave Ceddia's post [**A Complete React Redux Tutorial for Beginners**](https://daveceddia.com/redux-tutorial/)Dave Ceddia 的帖子《面向初学者的完整 React Redux 教程》
