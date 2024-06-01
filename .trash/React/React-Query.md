---
page-title: "Data Fetching And Cache Maintenance With React-Query | Apiumhub"
url: https://apiumhub.com/tech-blog-barcelona/data-fetching-and-cache-maintenance-with-react-query/
date: "2023-07-18 22:27:09"
---

Fetching data from the server and maintaining it is a very crucial issue in the frontend development. 

## Into React-Query

In React, there are three types of state: ==the local state==, which is persisted in the React components; ==the global state==, all components can access to it; and <span ==the server state== which is persisted in the server most of the time and depends on both sides. To manage the server state in the frontend and sync with the backend, we need to <span style="background:#d3f8b6">update, cache or re-fetch the data</span> efficiently. Sometimes we call the backend more than necessary, and this could cause performance problems in our applications. There, the React-query library helps us to solve these performance issues, manage the cache properly and give us useful features like <span style="background:#d3f8b6">query cancellation, stale time configuration, infinite query refetching</span> etc.


React Query is a library that has 2 simple hooks which provide fetching, caching and updating asynchronous data in React applications. , and now it is proven that it is very useful in <span style="background:#d3f8b6">server state management</span> in React applications. <span style="background:#d3f8b6">There are also other libraries like SWR, Apollo Client and RTK-Query for the server state management </span>and we can see their comparison with React query in their webpage: [https://react-query.tanstack.com/comparison](https://react-query.tanstack.com/comparison). According to react-query page comparison, <span style="background:#d3f8b6">react-query is the best option</span> objectively.

## Benefits of using React-Query

Some of the advantages that brings us React-Query are:

- Configuring the stale, cache, retry delay time creating a <span style="background:#d3f8b6">queryClientConfig</span> object.
- Updating the stale data in the background since react-query prefetches.
- Optimizing the requests to the backend.
- With the <span style="background:#d3f8b6">refetchOnWindowFocus</span> feature, it can refetch in the background when the user changes the browser tab or when they come back to the app.

And there are more of them that we will specify later. 

<span style="background:#d3f8b6">What are the stale and cache time in the terms of React-query? </span>Maybe we can start with explaining the five query states that React-query has in its development cycle and also which we will encounter in React-Query Dev Tools. 

![kUCebMzzJyNTRfEutm8IpDOoGhv7jJ7eZksbNKEFFVL0u49yCv6FOB8Ih4enWAfVW8ee6z5oBStENLN4XViWQ1MS1PM4arlUDSaVIEJv6EF1RMbhAbz6FybniS710Pzjw aD2bD](https://cdn-cgbdj.nitrocdn.com/RbczMDpxKIrQLdqnZdHDBvZTsISICJjh/assets/desktop/optimized/rev-924eb12/_kUCebMzzJyNTRfEutm8IpDOoGhv7jJ7eZksbNKEFFVL0u49yCv6FOB8Ih4enWAfVW8ee6z5oBStENLN4XViWQ1MS1PM4arlUDSaVIEJv6EF1RMbhAbz6FybniS710Pzjw_aD2bD "Data fetching and cache maintenance with React-Query 2")

Fresh: This state is when we have the almost same data on both sides (since when we received data, possible that someone is updated at the same time) and there is no need to refetch it.

Fetching: When we initially fetch the data successfully or not.

Stale: Out of date data which we will need to re-fetch it from the backend.

Inactive: This state is used to improve the speed/UX of our applications. It is previous to the deleted state.

<span style="background:#d3f8b6">The last state is the deleted state. After the data is inactive for a while (you can configure the time) it deletes from the cache.</span>

After understanding the state of the queries we can explain the<span style="background:#d3f8b6"> stale time</span> and <span style="background:#d3f8b6">cache time</span>. <span style="background:#d3f8b6">StaleTime</span> <u>is the duration of the transition from fresh to stale state.</u> If we are in the fresh state we will get the data from the cache only, but if we are in the stale state we may do a background fetch. <span style="background:#d3f8b6">CacheTime</span> <u>is the duration until inactive queries will be removed from the cache.</u> We can configure it by passing to a QueryClientProvider component from the library or passing locally in the useQuery call.

The two hooks that the library provides us are <span style="background:#d3f8b6">useQuery</span> and <span style="background:#d3f8b6">useMutation</span>. <font color="#ffff00">useQuery is used to fetch data and useMutation is used for creating, deleting and updating the data in the server. </font>The useQuery takes a key, a function to call the api and one object to configure this call. And all the queries will be stored in the QueryCache.

```js
const { data: questions = {}, isLoading}} = useQuery("questions",getQuestions,{staleTime:5000,cacheTime:10});
```

In addition to that you can send dynamic parameters in useQuery, and it will call the service when they change. For example in the code below, when “vendors” changes in the component, it will call the service again.

```js
export const useFetchQuestions = (vendors: Array<string>,element: number) =>
 useQuery([vendors], () => FormService.getDynamicQuestions(vendors, element));
```

The useMutation will take a mutation function to a service as required, but the mutation key will be optional. All the mutations will be stored in the MutationCache. And when we need to interact with QueryCache and MutationCache we will need to access firstly to QueryClient.

```js
export const useDownloadFile = (filePath: string, fileId: number) =>
 useMutation(() => FormService.downloadFile(filePath, fileId));
```

## Conclusion

React query is a great tool to use in React applications to manage the server state, lazy loading, pagination and the cache maintenance. It has a simple approach and implementation. With its devtools support, it is clear to use also in more complex applications. After working with the projects which includes

React/Redux where all the state is in local, React-Query saves so much boilerplate code and synchronizes local state with server. I hope that this article can help to resume what React-Query can contribute to your projects. And for more advanced topics, I highly recommend you to have a look at this blog: [https://tkdodo.eu/blog/practical-react-query](https://tkdodo.eu/blog/practical-react-query) which is written by one of the biggest collaborators of this library and his articles can be a great help.

## Links of interest

[Data fetching in Redux is painful, get rid of it now](https://medium.com/@cant89/data-fetching-in-redux-is-painful-get-rid-of-it-now-2b71305268e1) by Davide Cantelli **@Medium**

[Why I Stopped Using Redux](https://dev.to/g_abud/why-i-quit-redux-1knl) by Gabriel Abud **@Dev.to**

[React Query – An Underrated State Management Tool](https://blog.bitsrc.io/react-query-an-underrated-state-management-tool-5618b7b8cb36) by Tharaka Romesh **@Bits and Pieces**

[React state management in 2022 – Return of the Redux](https://engineering.udacity.com/react-state-management-in-2022-return-of-the-redux-87218f56486b) by Kolby Sisk **@Udacity**

[Comparison | React Query vs SWR vs Apollo vs RTK Query](https://react-query.tanstack.com/comparison) **@React Query**

[RTK Query Comparision](https://redux-toolkit.js.org/rtk-query/comparison) **@Redux Toolkit**

[RTK Query: The future of data fetching and caching for Redux](https://blog.logrocket.com/rtk-query-future-data-fetching-caching-redux/) by Dylan Tientcheu **@LogRocket**

[How and Why You Should Use React Query](https://blog.bitsrc.io/how-to-start-using-react-query-4869e3d5680d) by Nathan Sebhastian **@Bits and Pieces**

[Getting Started with React-Query for Data Fetching and State Management](https://www.section.io/engineering-education/react-query-data-fetching-and-server-state-management/) by Kevin Kimani **@Section**

[React Query and management of server state](https://dev.to/rootstrap/react-query-and-management-of-server-state-8ol) by Nicolas Santos **@Dev.to**

## 2023-07-18 22:45:32
[React state management in 2022 — Return of the Redux | by Kolby Sisk | Udacity Eng & Data](https://engineering.udacity.com/react-state-management-in-2022-return-of-the-redux-87218f56486b)
# State

State is persisted information that determines how an app will be rendered.==persisted information== that determines how an app will be rendered.  
状态是确定如何呈现应用的持久信息。确定如何呈现应用的持久化信息。
<!--SR:!2023-07-22,2,248-->

## We will be discussing the following types of state:

1. **Local State**: Refers to state persisted within a React Component.
2. **Global State**: Refers to state persisted within a global store that all components have access to.
3. **Server State**: Refers to state persisted on a server. (and for the sake of this conversation — automatically managed in client cache, using a tool like React Query.)

# Redux

Redux was created in 2015 by Dan Abramov and Andrew Clark as a solution for managing and providing state across an entire React application. Redux creates a Global State named <font color="#ffff00">a Store</font>, and allows you to connect Components to the Store to gain access to the Global State. <font color="#ffff00">Redux helps prevent [prop drilling](https://kentcdodds.com/blog/prop-drilling) and makes managing state across many components much easier.</font>

![](https://miro.medium.com/v2/resize:fit:1000/1*oHD3IZN86m37lfSqanoFeQ.png)

Managing state with classic Redux

But classic Redux comes with [many pain points](https://github.com/reduxjs/redux/issues/2295) including:

- <font color="#ffff00">A steep learning curve</font>
- A [n](https://blog.jakoblind.no/reduce-redux-boilerplate/)[o](https://blog.bitsrc.io/reducing-redux-boilerplate-with-redux-actions-81f9807fed15)[to](https://leocode.com/development/how-to-reduce-redux-boilerplate/)[r](https://dev.to/yogeshdatir/react-redux-boiler-plate-39p9)[i](https://blog.theodo.com/2020/01/reduce-redux-boilerplate/)[o](https://www.reddit.com/r/reactjs/comments/7dk3s8/is_there_a_way_to_reduce_boilerplate_for_redux/)[u](https://www.reddit.com/r/javascript/comments/67gvic/i_just_dont_get_what_is_worth_the_extra/)[s](https://news.ycombinator.com/item?id=17349211) boilerplate problem
- Lack of a standard architecture — no 2 Redux implementations were the same; few were good
- Poor TypeScript support

# Redux Toolkit

In October of 2019 [Redux Toolkit 1.0 was released](https://blog.isquaredsoftware.com/2019/10/redux-starter-kit-1.0/).

> “<font color="#ffff00">Redux Toolkit</font> is our official, opinionated, batteries-included toolset for efficient Redux development. It is intended to be the standard way to write Redux logic, and we strongly recommend that you use it.”— Redux Team

Mark Erikson’s [vision for RTK](https://github.com/reduxjs/redux-toolkit/issues/82) aimed to solve the aforementioned problems, and ultimately succeeded.

The 2 big features that make RTK worthwhile in my eyes are `[createSlice](https://redux-toolkit.js.org/api/createSlice)`, and the opinionated [Style Guide](https://redux.js.org/style-guide/style-guide).

A <font color="#ffff00">slice</font> is where you define the state of a feature which ultimately gets passed to `combineReducers` when configuring your store.

```javascript
import { createSlice } from '@reduxjs/toolkit';
// 定义初始状态
const initialState: {
  mode: 'light' | 'dark';
} = {
  mode: 'light',
};
// 创建 Redux Slice
export const themeSlice = createSlice({
  name: 'theme', // Slice 的名称，用于在 Redux 状态树中标识该 Slice
  initialState, // 初始状态
  reducers: {
    toggleThemeMode: (state) => {
      // 切换主题模式的 reducer 函数
      state.mode = state.mode === 'light' ? 'dark' : 'light';
    },
  },
});
// 导出 action 和 reducer
export const { toggleThemeMode } = themeSlice.actions;
export default themeSlice.reducer;
```
代码解释：
- 使用 `import { createSlice } from '@reduxjs/toolkit';` 导入 `createSlice` 函数，该函数用于创建 Redux Slice。
- 定义了 `initialState`，它是一个包含 `mode` 属性的对象，用于存储主题模式的初始状态，初始值为 `'light'`。
- 使用 `createSlice` 函数创建 Redux Slice，传入一个配置对象。
- 在配置对象中，`name` 属性指定了 Slice 的名称，这里设置为 `'theme'`，这将成为该 Slice 在 Redux 状态树中的标识。
- `initialState` 属性指定了初始状态对象。
- `reducers` 属性是一个对象，包含了定义的 reducer 函数。这里只有一个 `toggleThemeMode` reducer 函数，用于切换主题模式。
- `toggleThemeMode` reducer 函数接收当前状态 `state`，并根据当前的 `mode` 属性值切换到相应的主题模式，将新的主题模式赋值给 `state.mode`。
- 通过 `createSlice` 函数创建的 Redux Slice，会自动生成包含了 `toggleThemeMode` action 和对应的 reducer 的对象。
- 通过 `export` 关键字分别导出 `toggleThemeMode` action 和默认的 reducer 函数。
- `toggleThemeMode` action 可以在应用的其他地方被调用和分发，用于触发主题模式的切换。
- `themeSlice.reducer` 是默认导出的 reducer 函数，可以用于构建 Redux store。
这段代码使用 Redux Toolkit 中的 `createSlice` 函数和生成的 action/reducer 函数，简化了 Redux 的创建和管理过程，提供了更简洁和可读性更高的代码结构。
希望以上注释能够帮助您理解这段代码的作用和功能。如果您还有其他问题，请随时提问！

But even with RTK, I still wasn’t sold. That is in large part because around the time RTK was released, so were the Server State tools.

# Server State Tools

In 2019 [SWR](https://swr.vercel.app/) & [React Query](https://react-query.tanstack.com/) were introduced to the React community. SWR created by Vercel, and React Query created by Tanner Linsley, both solve the same problem: fetching, caching, synchronizing, and updating Server State.

Server State aims to keep the single-source-of-truth on the server, likely persisted in a database, and remove the need for maintaining and synchronizing server derived state with Global State.

![](https://miro.medium.com/v2/resize:fit:1000/1*sefcPdD-f_74je7Hfbszqg.png)

Managing state with SWR + Context

Because of the little Global State that remains when abstracting Server State to a query tool, there is little reason to use Redux. The remaining Global State, if any, could easily be managed with the [Context](https://reactjs.org/docs/context.html). At this moment in time I was a strong advocate for avoiding Redux, in favor of a Server State tool + Context.

But then RTK responded.

# RTK Query

In June 2021 Redux Toolkit added a very powerful tool that makes Redux a more viable solution: [RTK Query](https://redux-toolkit.js.org/rtk-query/overview).

Similar to SWR & React Query, RTK Query is a data fetching and caching tool that manages Server State.

One big benefit of using RTKQ is that it integrates with your Redux Store. Every interaction with RTKQ dispatches a Redux Action. This allows every interaction to be visible by all Redux Reducers, and even the Redux DevTools. This can be incredibly powerful for any any tool that integrates with Redux, [like Sentry](https://docs.sentry.io/platforms/javascript/guides/react/configuration/integrations/redux/).

So now that RTK has a Server State solution the deciding factor comes down to how you want to manage the remaining Global State in your app. At this point you can either create a Redux Slice, or use Context. Both solutions are roughly the same amount of boilerplate. Redux does however have some benefits.

The first is out-of-the-box performance. If you’ve ever read any article about Context you’ll know it’s often [discouraged as a state management solution](https://blog.isquaredsoftware.com/2021/01/context-redux-differences/). That’s because it’s very easy to build performance problems into your app if you’re not [utilizing Context correctly](https://kentcdodds.com/blog/how-to-optimize-your-context-value).

The second is the idea of having a single `Provider` — as opposed to using Context where you’ll need a `Provider` for each feature, all of which could appear anywhere in your component tree.

# Conclusion

I can’t believe I’m saying this, but I like Redux now. Thanks to [Redux Toolkit](https://redux-toolkit.js.org/) and the newly released [RTK Query](https://redux-toolkit.js.org/rtk-query/overview), implementing Redux is actually very pleasant and you gain a lot by using it, especially in an enterprise environment.

[[React状态管理Redux]]