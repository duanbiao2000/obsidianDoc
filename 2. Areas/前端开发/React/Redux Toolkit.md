
![[assets/img/Redux Toolkit/IMG-Redux Toolkit-20240714124831335.gif]]

SUMMARY 概括

- **Redux is a library for managing global application state  
    - Redux is typically used with the React-Redux library for integrating Redux and React together  
    - Redux Toolkit is the recommended way to write Redux logic  
- **Redux uses a "one-way data flow" app structure  
    - State describes the condition of the app at a point in time, and UI renders based on that state  
    - When something happens in the app:  
        - The UI dispatches an action  
        - The store runs the reducers, and the state is updated based on what occurred  
        - The store notifies the UI that the state has changed  
    - The UI re-renders based on the new state  
- **Redux uses several types of code  
    - _Actions_ are plain objects with a `type` field, and describe "what happened" in the app  
    - _Reducers_ are functions that calculate a new state value based on previous state + an action  
    - A Redux _store_ runs the root reducer whenever an action is _dispatched_  

Part2: Redux Toolkit App Structure
- The structure of a typical React + Redux Toolkit app
- How to view state changes in the Redux DevTools Extension
 [React-Redux](https://react-redux.js.org/) to connect together the Redux store and the React components.

```jsx
//counterSlice.js
import { createSlice } from '@reduxjs/toolkit'

export const counterSlice = createSlice({
  name: 'counter',
  initialState: {
    value: 0,
  },
  reducers: {
    increment: (state) => {
      // Redux Toolkit allows us to write "mutating" logic in reducers. It
      // doesn't actually mutate the state because it uses the immer library,
      // which detects changes to a "draft state" and produces a brand new
      // immutable state based off those changes
      state.value += 1
    },
    decrement: (state) => {
      state.value -= 1
    },
    incrementByAmount: (state, action) => {
      state.value += action.payload
    },
  },
})

export const { increment, decrement, incrementByAmount } = counterSlice.actions

// The function below is called a thunk and allows us to perform async logic. It
// can be dispatched like a regular action: `dispatch(incrementAsync(10))`. This
// will call the thunk with the `dispatch` function as the first argument. Async
// code can then be executed and other actions can be dispatched
export const incrementAsync = (amount) => (dispatch) => {
  setTimeout(() => {
    dispatch(incrementByAmount(amount))
  }, 1000)
}

// The function below is called a selector and allows us to select a value from
// the state. Selectors can also be defined inline where they're used instead of
// in the slice file. For example: `useSelector((state) => state.counter.value)`
export const selectCount = (state) => state.counter.value

export default counterSlice.reducer

```

The Redux store can be extended with "middleware", <font color="#00b050">which are a kind of add-on or plugin that can add extra abilities. The most common reason to use middleware is to let you write code that can have async logic, but still talk to the store at the same time.  </font>
Redux 存储可以通过“中间件”进行扩展，“中间件”是一种可以添加额外功能的附加组件或插件。使用中间件的最常见原因是让您编写具有异步逻辑的代码，但同时仍与存储进行通信。

```jsx
const thunkMiddleware =
  ({ dispatch, getState }) =>
  next =>
  action => {
    if (typeof action === 'function') {
      return action(dispatch, getState)
    }

    return next(action)
  }
```

**In a React + Redux app, your global state should go in the Redux store, and your local state should stay in React components.**



以下是一些关键的 Redux 术语和概念，以及它们的定义：

| 术语 | 定义 |
| --- | --- |
| Actions（动作） | 描述应用中发生的事件的纯 JavaScript 对象。它们是触发状态更改的唯一方法，必须包含 `type` 属性来指示动作的类型。 |
| Reducers（归约器） | 纯函数，接收先前的状态和一个动作作为参数，并返回新的状态。它们负责根据动作的类型来更新应用程序的状态。 |
| Store（存储） | 包含应用程序状态的对象。它是 Redux 的核心，负责存储和管理整个应用程序的状态树。 |
| Dispatching（派发） | 在 Redux 中派发（dispatch）一个动作意味着将动作传递给存储并触发相应的状态更新。它是通过调用存储对象的 `dispatch` 方法来完成的。 |
| Middleware（中间件） | 可以在 Redux 动作被派发到达 reducer 之前或之后进行拦截和处理的功能。它可以用于执行额外的逻辑、异步操作、日志记录等。 |
| Action Creators（动作创建者） | 是一个函数，用于创建并返回一个动作对象。它们简化了派发动作的过程，并可以传递额外的参数给动作对象。 |
| Selectors（选择器） | 函数，用于从存储中选择和提取特定的状态数据。它们提供了一种在组件中获取状态的方法，使组件可以访问存储中的特定数据。 |

### Actions

An **action** sends data from your application to the Redux store. An action is conventionally an object with two properties: `type` and (optional) `payload`. The type is generally an uppercase string (assigned to a constant) that describes the action. The payload is additional data that may be passed.

Action Type

```js
const DELETE_TODO = 'posts/deleteTodo'
```

Action

```js
{
  type: DELETE_TODO,
  payload: id,
}
```

#### Action creators

An **action creator** is a function that returns an action.↳
Action Creator

```js
const deleteTodo = (id) => ({ type: DELETE_TODO, payload: id })
```

### Reducers

A **reducer** is a function that takes two parameters: `state` and `action`. A reducer is immutable and always returns a copy of the entire state. A reducer typically consists of a `switch` statement that goes through all the possible action types.

Reducer

```js
const initialState = {
  todos: [
    { id: 1, text: 'Eat' },
    { id: 2, text: 'Sleep' },
  ],
  loading: false,
  hasErrors: false,
}

function todoReducer(state = initialState, action) {
  switch (action.type) {
    case DELETE_TODO:
      return {
        ...state,
        todos: state.todos.filter((todo) => todo.id !== action.payload),
      }
    default:
      return state
  }
}
```

### Store

The Redux application state lives in the **store**, which is initialized with a reducer. When used with React, a `<Provider>` exists to wrap the application, and anything within the Provider can have access to Redux.

Store

```jsx
import { createStore } from 'redux'
import { Provider } from 'react-redux'
import reducer from './reducers'

const store = createStore(reducer)

render(
  <Provider store={store}>
    <App />
  </Provider>,
  document.getElementById('root')
)
```

### Dispatch

`dispatch` is a method available on the store object that accepts an object which is used to update the Redux state. Usually, this object is the result of invoking an action creator.

```jsx
const Component = ({ dispatch }) => {
  useEffect(() => {
    dispatch(deleteTodo())
  }, [dispatch])
}
```

### Connect

The `connect()` function is one typical way to connect React to Redux. A connected component is sometimes referred to as a **container**.

Okay, that about covers it for the major terms of Redux. It can be overwhelming to read the terminology without any context, so let's begin.

[ ](https://www.taniarascia.com/redux-react-guide/#getting-started)Getting Started

For ease of getting started quickly, my example uses [Create React App](https://reactjs.org/docs/create-a-new-react-app.html) to set up the environment.

```shell
npx create-react-app redux-tutorial
cd redux-tutorial
```
Redux requires a few dependencies.↳

- [Redux](https://github.com/reduxjs/redux) - Core library
- [React Redux](https://github.com/reduxjs/react-redux) - React bindings for Redux
- [Redux Thunk](https://github.com/reduxjs/redux-thunk) - Async middleware for Redux
- [Redux DevTools Extension](https://github.com/reduxjs/redux-devtools-extension) - Connects Redux app to Redux DevTools
And delete all the boilerplate. We'll add everything we need from scratch instead.↳

```shell
cd src && rm * # move to src and delete all files within
```

We'll make directories for Redux [`reducers`](https://www.taniarascia.com/redux-react-guide/#reducers) and Redux [`actions`](https://www.taniarascia.com/redux-react-guide/#actions), as well as `pages` and `components` which you should already be familiar with from React.

```shell
mkdir actions components pages reducers
```

And we'll bring back `index.js`, `App.js`, and `index.css`.

```shell
touch index.js index.css App.js
```

So at this point your project directory tree looks like this.

```text
└── src/
    ├── actions/
    ├── components/
    ├── pages/
    ├── reducers/
    ├── App.js
    ├── index.css
    └── index.js
```

## Setting up the Redux Store

In `index.js`, we'll be bringing in a few things.

- `createStore`, to create the store that will maintain the Redux state
- `applyMiddleware`, to be able to use middleware, in this case `thunk`
- `Provider`, to wrap the entire application in Redux
- `thunk`, a middleware that allows us to make asynchronous actions in Redux
- `composeWithDevTools`, code that connects your app to Redux DevTools

index.js
```jsx
// External imports
import React from 'react'
import { render } from 'react-dom'
import { createStore, applyMiddleware } from 'redux'
import { Provider } from 'react-redux'
import thunk from 'redux-thunk'
import { composeWithDevTools } from 'redux-devtools-extension'

// Local imports
import App from './App'
import rootReducer from './reducers'

// Assets
import './index.css'

const store = createStore(rootReducer, composeWithDevTools(applyMiddleware(thunk)))

render(
  <Provider store={store}>
    <App />
  </Provider>,
  document.getElementById('root')
)
```

Put a component in `App.js`. We'll modify this later, but we just want to get the app up and running for now.

App.js

```jsx
import React from 'react'

const App = () => {
  return <div>Hello, Redux</div>
}

export default App
```

### [](https://www.taniarascia.com/redux-react-guide/#bringing-in-reducers)Bringing in reducers

The last thing to do is bring in the reducer. A **reducer** is a function that determines changes to Redux state. It is a pure function that returns a copy of the state with the new change.

A neat feature of Redux is that we can have many reducers, and combine them all into one root reducer that the store uses, using `combineReducers`. This leads to us being able to easily organize our code while still having everything in one root state tree.

Since this app will be like a blog, it will have a list of posts, and we'll put that in the `postsReducer` in a moment. Having this `combineReducers` method allows us to bring whatever we want in - a `commentsReducer`, an `authReducer`, and so on.

In `reducers/index.js`, create the file that will combine all reducers.

reducers/index.js

```js
import { combineReducers } from 'redux'

import postsReducer from './postsReducer'

const rootReducer = combineReducers({
  posts: postsReducer,
})

export default rootReducer
```

Finally, we'll make the `postsReducer`. We can set it up with an initial state. Just like you might expect from a regular React component, we'll have a `loading` and `hasErrors` state, as well as a `posts` array, where all the posts will live. First we'll set it up with no actions in the switch, just a default case that returns the entire state.

reducers/postsReducer.js

```js
export const initialState = {
  posts: [],
  loading: false,
  hasErrors: false,
}

export default function postsReducer(state = initialState, action) {
  switch (action.type) {
    default:
      return state
  }
}
```

## Setting up Redux Actions

So now we have a reducer for posts, but we don't have any actions, meaning the reducer will only return the state without modifying it in any way. **Actions** are how we communicate with the Redux store. For this blog app, we're going to want to fetch posts from an API and put them in our Redux state.

Since fetching posts is an asynchronous action, it will require the use of Redux thunk. Fortunately, we don't have to do anything special to use thunk beyond setting it up in the store, which we already did.

Create a `actions/postsActions.js`. First, we'll define the **action types** as constants. This is not necessary, but is a common convention, and makes it easy to export the actions around and prevent typos. We want to do three things:

- `getPosts` - begin telling Redux we're going to fetch posts from an API
- `getPostsSuccess` - pass the posts to Redux on successful API call
- `getPostsFailure` - inform Redux that an error was encountered during Redux on failed API call

actions/postsActions.js

```js
// Create Redux action types
export const GET_POSTS = 'GET_POSTS'
export const GET_POSTS_SUCCESS = 'GET_POSTS_SUCCESS'
export const GET_POSTS_FAILURE = 'GET_POSTS_FAILURE'
```

Then create **action creators**, functions that return an **action**, which consists of the type and an optional payload containing data.

actions/postsActions.js

```js
// Create Redux action creators that return an action
export const getPosts = () => ({
  type: GET_POSTS,
})

export const getPostsSuccess = (posts) => ({
  type: GET_POSTS_SUCCESS,
  payload: posts,
})

export const getPostsFailure = () => ({
  type: GET_POSTS_FAILURE,
})
```

Finally, make the asynchronous thunk action that combines all three of the above actions. When called, it will dispatch the initial `getPosts()` action to inform Redux to prepare for an API call, then in a `try/catch`, do everything necessary to get the data, and dispatch a success or failure action as necessary.

actions/postsActions.js

```js
// Combine them all in an asynchronous thunk
export function fetchPosts() {
  return async (dispatch) => {
    dispatch(getPosts())

    try {
      const response = await fetch('https://jsonplaceholder.typicode.com/posts')
      const data = await response.json()

      dispatch(getPostsSuccess(data))
    } catch (error) {
      dispatch(getPostsFailure())
    }
  }
}
```

Great, we're all done with creating actions now! All that's left to do is tell the reducer what to do with the state on each action.

### [](https://www.taniarascia.com/redux-react-guide/#responding-to-actions)Responding to actions

Back at our post reducer, we have a switch that isn't doing anything yet.

reducers/postsReducer.js

```js
export default function postsReducer(state = initialState, action) {
  switch (action.type) {
    default:
      return state
  }
}
```

Now that we have actions, we can bring them in from the `postsActions` page.

```js
// Import all actions
import * as actions from '../actions/postsActions'
```

For each action, we'll make a `case`, that returns the entire state plus whatever change we're making to it. For `GET_POSTS`, for example, all we want to do is tell the app to set `loading` to `true` since we'll be making an API call.

```js
case actions.GET_POSTS:
  return { ...state, loading: true }
```

- `GET_POSTS` - begin loading
- `GET_POSTS_SUCCESS` - the app has posts, no errors, and should stop loading
- `GET_POSTS_FAILURE` - the app has errors and should stop loading

Here's the whole reducer.

reducers/postsReducer.js

```js
import * as actions from '../actions/postsActions'

export const initialState = {
  posts: [],
  loading: false,
  hasErrors: false,
}

export default function postsReducer(state = initialState, action) {
  switch (action.type) {
    case actions.GET_POSTS:
      return { ...state, loading: true }
    case actions.GET_POSTS_SUCCESS:
      return { posts: action.payload, loading: false, hasErrors: false }
    case actions.GET_POSTS_FAILURE:
      return { ...state, loading: false, hasErrors: true }
    default:
      return state
  }
}
```

Now our actions and reducers are ready, so all that's left to do is connect everything to the React app.

## [](https://www.taniarascia.com/redux-react-guide/#connecting-redux-to-react-components)Connecting Redux to React Components

Since the demo app I've created uses React Router to have a few routes - a dashboard, a listing of all posts, and an individual posts page, I'll bring React Router in now. I'll just bring in the dashboard and all posts listing for this demo.

App.js

```jsx
import React from 'react'
import { BrowserRouter as Router, Switch, Route, Redirect } from 'react-router-dom'

import DashboardPage from './pages/DashboardPage'
import PostsPage from './pages/PostsPage'

const App = () => {
  return (
    <Router>
      <Switch>
        <Route exact path="/" component={DashboardPage} />
        <Route exact path="/posts" component={PostsPage} />
        <Redirect to="/" />
      </Switch>
    </Router>
  )
}

export default App
```

We can create the dashboard page, which is just a regular React component.

pages/DashboardPage.js

```jsx
import React from 'react'
import { Link } from 'react-router-dom'

const DashboardPage = () => (
  <section>
    <h1>Dashboard</h1>
    <p>This is the dashboard.</p>

    <Link to="/posts" className="button">
      View Posts
    </Link>
  </section>
)

export default DashboardPage
```

For each post, let's make a `Post` component that will display the title and an excerpt of the text of the article. Make a `Post.js` in the `components` subdirectory.

components/Post.js

```jsx
import React from 'react'

export const Post = ({ post }) => (
  <article className="post-excerpt">
    <h2>{post.title}</h2>
    <p>{post.body.substring(0, 100)}</p>
  </article>
)
```

> Components that do not connect to Redux are still important and useful for smaller, reusable areas, such as this Post component.

Now the interesting part comes in for the posts page - bringing Redux into React. To do this we'll use `connect` from `react-redux`. First, we'll just make a regular component for the page.

pages/PostsPage.js

```jsx
import React from 'react'

const PostsPage = () => {
  return (
    <section>
      <h1>Posts</h1>
    </section>
  )
}

export default PostsPage
```

Then we'll bring in `connect`. The [connect function](https://react-redux.js.org/api/connect) is a higher-order function that connects the Redux store to a React component. We'll pass a parameter called `mapStateToProps` to `connect`. This aptly named function will take any state from the Redux store and pass it to the props of the React component. We'll bring in `loading`, `posts`, and `hasErrors` from the Redux `postsReducer`.

pages/PostsPage.js

```jsx
import React from 'react'
import { connect } from 'react-redux'
// Redux state is now in the props of the component
const PostsPage = ({ loading, posts, hasErrors }) => {
  return (
    <section>
      <h1>Posts</h1>
    </section>
  )
}

// Map Redux state to React component propsconst mapStateToProps = (state) => ({  loading: state.posts.loading,  posts: state.posts.posts,  hasErrors: state.posts.hasErrors,})// Connect Redux to Reactexport default connect(mapStateToProps)(PostsPage)
```

> Since this component uses state from the same reducer, we could also write `state => state.posts`. However, learning how to write it the long way is useful to know in case you need to bring multiple reducers into the same component.

Finally, we'll bring in the asynchronous `fetchPosts` from the actions, which is the action that combines the whole lifecycle of fetching all posts into one. Using `useEffect` from React, we'll `dispatch` `fetchPosts` when the component mounts. `dispatch` will automatically be available on a connected component.

pages/PostsPage.js

```jsx
import React, { useEffect } from 'react'import { connect } from 'react-redux'

// Bring in the asynchronous fetchPosts actionimport { fetchPosts } from '../actions/postsActions'
const PostsPage = ({ dispatch, loading, posts, hasErrors }) => {  useEffect(() => {    dispatch(fetchPosts())  }, [dispatch])
  return (
    <section>
      <h1>Posts</h1>
    </section>
  )
}

const mapStateToProps = (state) => ({
  loading: state.posts.loading,
  posts: state.posts.posts,
  hasErrors: state.posts.hasErrors,
})

export default connect(mapStateToProps)(PostsPage)
```

All that's left to do at this point is display all three possible states of the page - whether it's loading, has an error, or successfully retrieved the posts from the API.

pages/PostsPage.js

```jsx
import React, { useEffect } from 'react'
import { connect } from 'react-redux'

import { fetchPosts } from '../actions/postsActions'
import { Post } from '../components/Post'
const PostsPage = ({ dispatch, loading, posts, hasErrors }) => {
  useEffect(() => {
    dispatch(fetchPosts())
  }, [dispatch])

  // Show loading, error, or success state  const renderPosts = () => {    if (loading) return <p>Loading posts...</p>    if (hasErrors) return <p>Unable to display posts.</p>    return posts.map((post) => <Post key={post.id} post={post} />)  }
  return (
    <section>
      <h1>Posts</h1>
      {renderPosts()}    </section>
  )
}

const mapStateToProps = (state) => ({
  loading: state.posts.loading,
  posts: state.posts.posts,
  hasErrors: state.posts.hasErrors,
})

export default connect(mapStateToProps)(PostsPage)
```

And that's all - we now have a connected component, and are bringing in data from an API to our Redux store. Using Redux DevTools, we can see each action as it happens, and the changes (diff) after each state change.

[![redux posts](https://www.taniarascia.com/static/01d5eae3d92b20bc25e9c61f1e20d5fa/5a190/redux-posts.png "redux posts")](https://www.taniarascia.com/static/01d5eae3d92b20bc25e9c61f1e20d5fa/00d43/redux-posts.png)

## [](https://www.taniarascia.com/redux-react-guide/#the-end)The End

This is where the tutorial for creating an application with plain Redux ends. If you look at the [source code of the demo application](https://codesandbox.io/s/react-redux-application-hewdb), you'll see a lot has been added - a reducer and actions for a single post, and for comments.

I would recommend completing your project so that it matches the demo app. There are no new concepts to be learned, but you will create two more reducers and actions, and see how to bring two states into one component for the single post page, which brings in one post as well as comments for that post.

## [](https://www.taniarascia.com/redux-react-guide/#redux-toolkit)Redux Toolkit

There is one more thing I want to cover - [Redux Toolkit](https://redux-toolkit.js.org/). Redux Toolkit, or RTK, is a newer and easier official way to use Redux. You may notice that Redux has a _lot_ of boilerplate for setup and requires many more folders and files than plain React would. Some patterns have emerged to attempt to mitigate all that, such as [Redux ducks pattern](https://github.com/erikras/ducks-modular-redux), but we can simplify it even more.

View the [source of the demo Redux Toolkit application](https://codesandbox.io/s/react-redux-toolkit-application-cbb6s), which is the same application we just created with Redux, but using RTK. It is much simpler, with a drastic reduction in lines of code for all the same functionality.

Using RTK just requires one dependency, [@reduxjs/toolkit](https://github.com/reduxjs/redux-toolkit).

```shell
npm i @reduxjs/toolkit
```

And no longer requires you to install the `redux-thunk` or `redux-devtools-extension` dependencies.

### [](https://www.taniarascia.com/redux-react-guide/#advantages-to-redux-toolkit)Advantages to Redux Toolkit

The main advantages to using RTK are:

- Easier to set up (less dependencies)
- Reduction of boilerplate code (one slice vs. many files for actions and reducers)
- Sensible defaults (Redux Thunk, Redux DevTools built-in)
- The ability to use [direct state mutation](https://redux-toolkit.js.org/api/createreducer#direct-state-mutation), since RTK uses [immer](https://github.com/immerjs/immer) under the hood. This means you no longer need to return `{ ...state }` with every reducer.

### [](https://www.taniarascia.com/redux-react-guide/#store-1)Store

Since Redux Toolkit comes with a lot built-in already, like Redux DevTools and Redux Thunk, we no longer have to bring them into the `index.js` file. Now we only need `configureStore`, instead of `createStore`.

index.js

```jsx
import React from 'react'
import { render } from 'react-dom'
import { configureStore } from '@reduxjs/toolkit'import { Provider } from 'react-redux'

import App from './App'
import rootReducer from './slices'

import './index.css'

const store = configureStore({ reducer: rootReducer })
render(
  <Provider store={store}>
    <App />
  </Provider>,
  document.getElementById('root')
)
```

### [](https://www.taniarascia.com/redux-react-guide/#slices)Slices

Instead of dealing with reducers, actions, and all as separate files and individually creating all those action types, RTK gives us the concept of **slices**. A [slice](https://redux-toolkit.js.org/api/createSlice) automatically generates reducers, action types, and action creators. As such, you'll only have to create one folder - `slices`.

`initialState` will look the same.

slices/posts.js

```js
import { createSlice } from '@reduxjs/toolkit'

export const initialState = {
  loading: false,
  hasErrors: false,
  posts: [],
}
```

The names of the reducers in the slice will also be the same - `getPosts`, `getPostsSuccess`, and `getPostsFailure`. We'll make all the same changes, but note that we're no longer returning the entire state - we're just mutating state. It's still immutable under the hood, but this approach may be easier and faster for some. If preferred, you can still return the whole state as an object.

slices/posts.js

```js
// A slice for posts with our three reducers
const postsSlice = createSlice({
  name: 'posts',
  initialState,
  reducers: {
    getPosts: (state) => {
      state.loading = true
    },
    getPostsSuccess: (state, { payload }) => {
      state.posts = payload
      state.loading = false
      state.hasErrors = false
    },
    getPostsFailure: (state) => {
      state.loading = false
      state.hasErrors = true
    },
  },
})
```

The actions that get generated are the same, we just don't have to write them out individually anymore. From the same file, we can export all the actions, the reducer, the asynchronous thunk, and one new thing - a `selector`, which we'll use to access any of the state from a React component instead of using `connect`.

slices/posts.js

```jsx
// Three actions generated from the slice
export const { getPosts, getPostsSuccess, getPostsFailure } = postsSlice.actions

// A selector
export const postsSelector = (state) => state.posts

// The reducer
export default postsSlice.reducer

// Asynchronous thunk action
export function fetchPosts() {
  return async (dispatch) => {
    dispatch(getPosts())

    try {
      const response = await fetch('https://jsonplaceholder.typicode.com/posts')
      const data = await response.json()

      dispatch(getPostsSuccess(data))
    } catch (error) {
      dispatch(getPostsFailure())
    }
  }
}
```

### [](https://www.taniarascia.com/redux-react-guide/#selecting-redux-state-in-a-react-component)Selecting Redux state in a React component

The traditional approach, as we just learned, is to use `mapStateToProps` with the `connect()` function. This is still common in codebases and therefore worth learning. You can still use this approach with RTK, but the newer, React Hooks way of going about it is to use `useDispatch` and `useSelector` from `react-redux`. This approach requires less code overall as well.

As you can see in the updated `PostsPage.js` file below, the Redux state is no longer available as props on the connected component, but from the selector we exported in the slice.

pages/PostsPage.js

```jsx
import React, { useEffect } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { fetchPosts, postsSelector } from '../slices/posts'
import { Post } from '../components/Post'

const PostsPage = () => {
  const dispatch = useDispatch()  const { posts, loading, hasErrors } = useSelector(postsSelector)
  useEffect(() => {
    dispatch(fetchPosts())
  }, [dispatch])

  const renderPosts = () => {
    if (loading) return <p>Loading posts...</p>
    if (hasErrors) return <p>Unable to display posts.</p>

    return posts.map((post) => <Post key={post.id} post={post} excerpt />)
  }

  return (
    <section>
      <h1>Posts</h1>
      {renderPosts()}
    </section>
  )
}

export default PostsPage
```

Now we have the same app as before with a few updates from Redux Toolkit, and a lot less code to maintain.

## [](https://www.taniarascia.com/redux-react-guide/#conclusion)Conclusion

We did it! If you followed along with me through this whole tutorial, you should have a really good feel for Redux now, both the old-fashioned way and using Redux Toolkit to simplify things. To summarize, Redux allows us to easily manage global state in a React application. We can access and update the state from anywhere, and easily debug the entire state of an application with Redux Devtools.

You can place most of the state of your application in Redux, but certain areas of an app, such as forms as they are being updated, still make sense to keep in the React component state itself until the form is officially submitted.

I hope you enjoyed this article! It was a lot of work to put together two complete demo applications and run through the whole thing here, and the article ran pretty long, but hopefully this is your one-stop shop for learning all beginner and intermediate Redux concepts.    
Please let me know what you think and share the article if it helped you out, and donations are always welcome!






### Redux Fundamentals Tutorial[​](https://redux-toolkit.js.org/introduction/getting-started#redux-fundamentals-tutorial "Direct link to heading")

The [**Redux Fundamentals tutorial**](https://redux.js.org/tutorials/fundamentals/part-1-overview) is a "bottom-up" tutorial that teaches "how Redux works" from first principles and without any abstractions, and why standard Redux usage patterns exist.

### Learn Modern Redux Livestream[​](https://redux-toolkit.js.org/introduction/getting-started#learn-modern-redux-livestream "Direct link to heading")

Redux maintainer Mark Erikson appeared on the "Learn with Jason" show to explain how we recommend using Redux today. The show includes a live-coded example app that shows how to use Redux Toolkit and React-Redux hooks with Typescript, as well as the new RTK Query data fetching APIs.

See [the "Learn Modern Redux" show notes page](https://www.learnwithjason.dev/let-s-learn-modern-redux) for a transcript and links to the example app source.