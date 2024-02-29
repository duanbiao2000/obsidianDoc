---
aliases: []
date: 2023-09-10
url: 
page-title: 
tags:
  - flashcards
  - todo
  - bookStatusOnreading
---
# 前言
建议先学redux toolkit 再学redux
我个人的建议是:
首先学习Redux Toolkit,然后再学习原生Redux。
理由如下:
1. Redux Toolkit是Redux官方的标准应用方式,它封装了常用的Redux模式,可以让你更快上手Redux。
2. Redux Toolkit隐藏了很多Redux内部的复杂性,比如action类型常量,手动合并reducer等,让你可以更专注于业务逻辑。
3. Redux Toolkit提供了一些实用工具函数,比如createSlice、createAsyncThunk等,可以极大简化Redux代码量。
4. 学习Redux Toolkit的概念和API后,再学习原生Redux可以更好地理解Redux的工作原理。
5. 目前大多数新项目都会直接使用Redux Toolkit来开发,掌握它对你学习Redux和工作都有很大帮助。
6. 以后如果需要深入研究Redux内部机制,还是可以再学习原生Redux。
所以,我的建议是:
- 先学习Redux Toolkit,掌握它的基本概念和API
- 使用Redux Toolkit开发一个小项目
- 然后再学习原生Redux的工作原理
- 需要深入了解Redux时再学习原生API
这样可以更高效地学习Redux知识。

![[Pasted image 20230910091526.png]]
![[Pasted image 20230910092258.png]]
redux中的payload是指action中携带的数据,它代表了action的目的或执行结果。
# redux payload
- action中除type外的其他信息,用于描述action的目的或执行结果
- 通常payload会包含需要更新的state数据
- 例如:
    - { type: 'ADD_TODO', payload: 'Learn Redux' }
    - { type: 'REMOVE_TODO', payload: 3 }
    - { type: 'UPDATE_TODO', payload: { id: 2, text: 'Go to the gym' } }
- reducer根据action的type和payload来更新state
- payload可以是基本类型值,对象,函数等各种类型
- 有payload的action才是有效的,只有type的action通常不会做任何改变
- 有时也会使用其他名称如data, info代替payload
![[Pasted image 20230910100603.png]]

![(81) Learn Redux Toolkit in 1 video with Project | React Redux Toolkit |Redux Toolkit Tutorial - YouTube](https://www.youtube.com/watch?v=A_vRvDAZuOo&t=103s)
#### configureStore
configureStore是Redux Toolkit提供的一个函数,用来配置和生成Redux store。
它的主要功能包括:
1. 应用中间件
configureStore会自动应用如Redux DevTools等常用中间件。
2. 合并reducer
可以将多个slice或reducer合并成一个总reducer。
3. 启用immer
使用immer可以简化immutable更新state的写法。
4. 启用Redux DevTools
自动集成Redux DevTools扩展,方便调试。
5. 返回store
调用后返回一个完整配置的Redux store对象。
使用configureStore可以:
- 自动应用常用中间件如DevTools等
- 简化store创建和配置过程
- 将多个reducer合并为一个
- 启用immer简化更新state
- 直接获取配置好的store对象
例如:
```js
const store = configureStore({
  reducer: rootReducer 
})
```
这相比手动创建store简单很多。
所以configureStore是Redux Toolkit提供的一个很便利的API,可以自动完成store的创建和配置,为开发提供更好的体验。


#### useSelector 和 useDispatch
![[Pasted image 20230910145729.png]]
useSelector 和 useDispatch 是来自 React-Redux 库的两个重要 Hook,它们允许 React 组件与 Redux 存储交互。
useSelector:
- 用于从 Redux 存储状态中读取数据。
- 我们传入一个选择器函数,它从存储状态中选择我们需要的具体数据。 
- 如果返回的数据变更,组件会重新渲染。
- 例如:
```js
const count = useSelector(state => state.count)
```
useDispatch:
- 用于向存储分发操作。
- 它返回存储的 dispatch 函数,允许分发操作。
- 我们调用 dispatch 触发操作创建函数来更新存储状态。
- 例如:
```js
const dispatch = useDispatch()
function handleClick() {
  dispatch(increment()) 
}
```
主要区别:
- useSelector 从存储中读取数据
- useDispatch 向存储分发操作来更新状态
它们共同允许 React 组件:
- 从存储状态中读取指定数据
- 分发操作来更新存储状态  
- 在选择的数据变更时重新渲染
这是将 React 组件与 Redux 进行集成的推荐方式。
总之,useSelector 和 useDispatch 是 React-Redux 提供的两个重要 Hook,可以方便地让组件与 Redux 存储进行交互。
#### useSelector
![[Pasted image 20230910150834.png]]

#### useDispatch
![[Pasted image 20230910151616.png]]

![[Pasted image 20230910151857.png]]

#### Slice
![[Pasted image 20230910151224.png]]
![[Pasted image 20230910152543.png]]
`export const{fetchProducts} = productSlice.actions;`
这个语法是从 Redux Toolkit 的 slice 中导出 action creator 函数。
具体分析:
1. productSlice 使用 createSlice 创建出来的 slice 对象,会定义一系列 action types 和 reducer 函数。
2. slice 对象还会定义一些默认的 action creator 函数,比如这里的 fetchProducts。
3. actions 属性下面包含了所有在这个 slice 中定义的 action creator 函数。
4. 通过解构赋值的方式,我们可以直接从 actions 对象中导出指定的 action creator。
5. export const {fetchProducts} 相当于从 productSlice.actions 对象中导出了名为 fetchProducts 的函数。
6. 后续我们就可以直接使用这个函数来分发对应的 action:
```js
import { fetchProducts } from './productSlice'
// dispatch action
dispatch(fetchProducts()) 
```
所以总结:
- 通过 slice 定义了 action creator fetchProducts
- 从 slice.actions 对象中导出这个函数
- 后续直接使用导出的函数来分发 action
这种写法可以很方便地从 slice 中抽取出需要的 action creator,避免每次都需要 productSlice.actions.fetchProducts 这样长的调用形式。
#### Store
![[Pasted image 20230910153832.png]]
 这里使用 createSlice 创建了一个产品(products)slice:
```js
//src\store\productSlice.js
// 定义产品slice
const productSlice = createSlice({
  // 命名空间为products 
  name: 'products',  
  // 初始状态
  initialState: {
    // ...
  },
  // 定义reducer函数
  reducers: {
    // fetchProducts reducer
    fetchProducts(state, action) {
      // 注释1: action 参数包含了分发的action信息
      // 注释2: state 是产品slice的状态
      // 将action的payload(载荷)赋值给state.data,更新状态
      state.data = action.payload;
      // 返回新的state
      return state;
    }
  }
})
// 导出产品slice
export default productSlice;
```
主要点:
1. 使用createSlice定义slice
2. 设置name和initialState
3. 定义reducer函数更新state
4. action参数包含分发信息
5. state是slice状态,可被更新返回
6. 导出slice供后续使用
这样可以使用Redux Toolkit更方便地创建和管理Redux状态。


![[Pasted image 20230910154946.png]]
 这里使用createAsyncThunk定义了一个异步action:
```js
// 导入createAsyncThunk
import { createAsyncThunk } from '@reduxjs/toolkit'
// 定义getProducts异步action
export const getProducts = createAsyncThunk(
  'products/get', // action type
  async () => {
    // 注释1: 异步获取产品数据
    const response = await fetch('https://fakestoreapi.com/products') 
    // 注释2: 解析json数据
    const data = await response.json()
    // 返回解析结果
    return data
  }
)
// 注释3: 后续可以在组件或其他地方分发这个action
dispatch(getProducts())  
```
主要点:
1. 使用createAsyncThunk定义异步action
2. 设置type和回调函数异步获取数据
3. 解析json数据并返回
4. 可以在任意位置分发这个action触发异步流程
5. Redux Toolkit会处理后续的loading/success状态
通过这个API可以更简单地定义Redux中的异步流程,避免手写action类型和reducer逻辑。

![[Pasted image 20230910155449.png]]
 这里使用createSlice和extraReducers来处理异步action:
```js
// 定义产品slice
const productSlice = createSlice({
  name: 'products',
  initialState: {
    data: []
  },
  reducers: {
    fetchProducts(state, action) {
      state.data = action.payload;
    } 
  },
  // 处理异步action
  extraReducers: builder => {
    // 处理getProducts异步action成功状态
    builder.addCase(getProducts.fulfilled, (state, action) => {
      // 注释1: action.payload包含解析后的数据
      state.data = action.payload;
      // 返回更新后的state  
      return state;
    })
  }
})
// 导出产品slice
export default productSlice;
```
主要点:
1. 使用createSlice定义slice和同步reducer
2. 通过extraReducers处理异步action
3. 增加getProducts.fulfilled状态匹配器
4. 更新state使用解析后的数据
5. Redux Toolkit会自动处理loading/error状态
这种方式可以很好地将异步逻辑整合到slice定义中,同步和异步action都在一个slice管理。

----



----
# Learn React Redux Toolkit with Project in 2 Hours
![(79) Learn React Redux Toolkit with Project in 2 Hours | React Redux Tutorial for Beginners - YouTube](https://www.youtube.com/watch?v=2kL28Qyw9-0)


![[Pasted image 20230909135546.png]]

![[Pasted image 20230909135642.png]]

![[Pasted image 20230909135812.png]]

![[Pasted image 20230909140146.png]]


 
| 文件夹 | 含义 |
|-|-|
| node_modules | 存放项目依赖的npm包 |
| public | 静态资源文件夹,如html,图片等 |
| src | 项目源码文件夹 |
| common | 公共样式,如变量,mixin等 |
| components | 组件文件夹 | 
| features | 功能模块文件夹,如首页,详情页等 |
| images | 图片资源文件夹 |
| App.js | 应用入口文件 |
| App.scss | 应用整体样式文件 |
| index.js | 入口js文件 |
| .gitignore | git版本控制忽略文件 |
总的来说:
- App作为整体入口
- index作为js入口
采用分层分模块的项目结构,方便redux开发。

 App作为整体入口和index作为js入口的区别:
App作为整体入口:
- App.js是整个应用的入口文件。
- 在App.js中会引入并渲染根组件(如<App/>)。
- App.js也会处理一些整体级别的逻辑,如全局状态管理等。
index作为js入口:
- index.js是JavaScript代码的入口文件。
- 它不负责渲染UI,仅作为模块的统一入口。
- index.js主要做的是导入并运行App.js。
区别在于:
- App.js负责渲染UI并作为应用整体的入口。
- index.js仅作为模块的js入口,不负责UI渲染。
使用这种结构的好处是:
- App.js专注于UI渲染和整体逻辑。
- index.js作为模块入口,不混合UI逻辑代码。
- 结构更清晰,后期维护和扩展更方便。
所以总结:
- App.js是应用整体的入口,负责UI渲染。
- index.js仅作为js模块的入口,不负责UI渲染工作。
两者职责清晰,结构更合理。

![[Pasted image 20230909154134.png]]

 await movieApi.get(`?apiKey=${APIKey}`)这行代码是为了调用一个异步API获取数据:
- movieApi可能是一个定义好的API调用对象,封装了get方法
- get方法内部使用fetch或axios发起HTTP请求
- 参数`?apiKey=${APIKey}`表示使用APIKey作为查询参数
- await关键字用于等待Promise对象返回结果
执行流程:
1. movieApi.get方法内部使用fetch或axios发起GET请求
2. 请求地址为基础URL + 参数`?apiKey=${APIKey}`
3. get方法返回一个Promise对象
4. await等待Promise对象resolve,获取响应数据
5. 数据返回并赋值给await的左值
使用await有以下好处:
- 让后续代码看起来像同步执行 
- 避免回调地狱,代码结构更清晰
- 可以直接使用返回值无需额外处理Promise
所以这行代码的含义是:
发起API请求,使用await等待响应,获取返回的数据用于后续处理。
它实现了同步调用异步API的效果。

![[Pasted image 20230909154836.png]]

![[Pasted image 20230909154929.png]]

![[Pasted image 20230909155009.png]]

![[Pasted image 20230909155043.png]]

![[Pasted image 20230909155205.png]]

![[Pasted image 20230909155238.png]]

## home.js

```js
import React, { useEffect } from "react";
import MovieListing from "../MovieListing/MovieListing";

import { useDispatch } from "react-redux";
import {
  fetchAsyncMovies,
  fetchAsyncShows,
} from "../../features/movies/movieSlice";
const Home = () => {
  const dispatch = useDispatch();
  useEffect(() => {
    dispatch(fetchAsyncMovies());
    dispatch(fetchAsyncShows());
  }, [dispatch]);
  return (
    <div>
      <div className="banner-img"></div>
      <MovieListing />
    </div>
  );
};

export default Home;
```
## home.js注释
 ```js
// Home组件
const Home = () => {
  // 使用useDispatch获取dispatch函数
  const dispatch = useDispatch();
  // 在组件挂载时执行
  useEffect(() => {
    // 分发两个异步action获取数据
    dispatch(fetchAsyncMovies()); 
    dispatch(fetchAsyncShows());
  // 依赖dispatch,只在组件挂载时调用
  }, [dispatch]);
  // 渲染视图
  return (
    <div>
      {/* 渲染banner */}
      <div className="banner-img"></div>
      
      {/* 渲染MovieListing子组件 */}
      <MovieListing />
    </div>
  );
}
// 导出Home组件
export default Home;
```
主要点:
- 使用React钩子连接Redux
- 分发action获取初始化数据  
- 只在挂载时获取数据
- 渲染子组件展示列表
这个Home容器组件负责:
- 连接Redux状态
- 加载初始化数据
- 渲染子视图组件

## App.js
```js
import React from "react";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import Home from "./components/Home/Home";
import Header from "./components/Header/Header";
import Footer from "./components/Footer/Footer";
import PageNotFound from "./components/PageNotFound/PageNotFound";
import MovieDetail from "./components/MovieDetail/MovieDetail";
import "./App.scss";

function App() {
  return (
    <div className="app">
      <Router>
        <Header></Header>
        <div className="container">
          <Switch>
            <Route path="/" exact component={Home} />
            <Route path="/movie/:imdbID" component={MovieDetail} />
            <Route component={PageNotFound} />
          </Switch>
        </div>
        <Footer />
      </Router>
    </div>
  );
}

export default App;
```
## App.js注释
 这是App组件的代码,使用React Router实现单页应用的路由:
```jsx
// 导入React和React Router
import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom'; 
// 导入各个组件
import Header from './Header';
import Home from './Home';
import MovieDetail from './MovieDetail';
import PageNotFound from './PageNotFound';
import Footer from './Footer';
function App() {
  return (
    // 使用BrowserRouter包裹整个应用
    <Router>
      <Header />
      <div className="container">
        {/* Switch只渲染第一个匹配的路由 */}
        <Switch>  
          {/* 首页路由 */}
          <Route exact path="/" component={Home} />  
          {/* 电影详情路由 */} 
          <Route path="/movie/:imdbID" component={MovieDetail}/>
          {/* 404路由 */}
          <Route component={PageNotFound} />
        </Switch>
      </div>
      <Footer />
    </Router>
  );
}
export default App;
```
实现单页应用路由的主要点:
- 使用BrowserRouter包裹整个应用
- Switch只渲染第一个匹配路由
- 定义各个路由和对应的组件

## movieSlice.js

```js
import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import movieApi from "../../common/apis/movieApi";
import { APIKey } from "../../common/apis/MovieApiKey";

export const fetchAsyncMovies = createAsyncThunk(
  "movies/fetchAsyncMovies",
  async () => {
    const movieText = "Harry";
    const response = await movieApi.get(
      `?apiKey=${APIKey}&s=${movieText}&type=movie`
    );
    return response.data;
  }
);

export const fetchAsyncShows = createAsyncThunk(
  "movies/fetchAsyncShows",
  async () => {
    const seriesText = "Friends";
    const response = await movieApi.get(
      `?apiKey=${APIKey}&s=${seriesText}&type=series`
    );
    return response.data;
  }
);

export const fetchAsyncMovieOrShowDetail = createAsyncThunk(
  "movies/fetchAsyncMovieOrShowDetail",
  async (id) => {
    const response = await movieApi.get(`?apiKey=${APIKey}&i=${id}&Plot=full`);
    return response.data;
  }
);

const initialState = {
  movies: {},
  shows: {},
  selectMovieOrShow: {},
};

const movieSlice = createSlice({
  name: "movies",
  initialState,
  reducers: {
    removeSelectedMovieOrShow: (state) => {
      state.selectMovieOrShow = {};
    },
  },
  extraReducers: {
    [fetchAsyncMovies.pending]: () => {
      console.log("Pending");
    },
    [fetchAsyncMovies.fulfilled]: (state, { payload }) => {
      console.log("Fetched Successfully!");
      return { ...state, movies: payload };
    },
    [fetchAsyncMovies.rejected]: () => {
      console.log("Rejected!");
    },
    [fetchAsyncShows.fulfilled]: (state, { payload }) => {
      console.log("Fetched Successfully!");
      return { ...state, shows: payload };
    },
    [fetchAsyncMovieOrShowDetail.fulfilled]: (state, { payload }) => {
      console.log("Fetched Successfully!");
      return { ...state, selectMovieOrShow: payload };
    },
  },
});

export const { removeSelectedMovieOrShow } = movieSlice.actions;
export const getAllMovies = (state) => state.movies.movies;
export const getAllShows = (state) => state.movies.shows;
export const getSelectedMovieOrShow = (state) => state.movies.selectMovieOrShow;
export default movieSlice.reducer;
```

## movieSlice.js 注释

```js
import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";

//导入需要的库

import movieApi from "../../common/apis/movieApi";

//导入电影api

import { APIKey } from "../../common/apis/MovieApiKey";

//导入api key

export const fetchAsyncMovies = createAsyncThunk(

  "movies/fetchAsyncMovies",

  async () => {

    //创建异步函数获取电影数据

    const movieText = "Harry";

    //设置搜索关键词为Harry

    const response = await movieApi.get(

      `?apiKey=${APIKey}&s=${movieText}&type=movie`

    );

    //使用电影api的get请求获取数据

    return response.data;

    //返回数据

  }

);

export const fetchAsyncShows = createAsyncThunk(

  "movies/fetchAsyncShows",

  async () => {

    const seriesText = "Friends";

    //设置搜索关键词为Friends

    const response = await movieApi.get(

      `?apiKey=${APIKey}&s=${seriesText}&type=series`

    );

    return response.data;

  }

);

export const fetchAsyncMovieOrShowDetail = createAsyncThunk(

  "movies/fetchAsyncMovieOrShowDetail",

  async (id) => {

    //获取电影或剧集详情的异步函数

    const response = await movieApi.get(`?apiKey=${APIKey}&i=${id}&Plot=full`);

    //使用电影api的get请求根据id获取详情

    return response.data;

  }

);

const initialState = {

  movies: {},

  shows: {},

  selectMovieOrShow: {}

};

//初始化状态

const movieSlice = createSlice({

  name: "movies",

  initialState,

  reducers: {

    removeSelectedMovieOrShow: (state) => {

      state.selectMovieOrShow = {};

    },

  },

  extraReducers: {

    [fetchAsyncMovies.pending]: () => {

      console.log("Pending");

    },

    [fetchAsyncMovies.fulfilled]: (state, { payload }) => {

      console.log("Fetched Successfully!");

      return { ...state, movies: payload };

    },

    [fetchAsyncMovies.rejected]: () => {

      console.log("Rejected!");

    },

    [fetchAsyncShows.fulfilled]: (state, { payload }) => {

      console.log("Fetched Successfully!");

      return { ...state, shows: payload };

    },

    [fetchAsyncMovieOrShowDetail.fulfilled]: (state, { payload }) => {

      console.log("Fetched Successfully!");

      return { ...state, selectMovieOrShow: payload };

    },

  },

});

export const { removeSelectedMovieOrShow } = movieSlice.actions;

//导出removeSelectedMovieOrShow的action创建函数

export const getAllMovies = (state) => state.movies.movies;

//导出选择器获取movies

export const getAllShows = (state) => state.movies.shows;

//导出选择器获取shows

export const getSelectedMovieOrShow = (state) => state.movies.selectMovieOrShow;

//导出选择器获取selectMovieOrShow

export default movieSlice.reducer;

//导出reducer
```
## createSlice, createAsyncThunk

`createSlice` 和 `createAsyncThunk` 是 Redux Toolkit 的两个主要函数，它们都是为了简化 Redux 应用程序的开发。
1. `createSlice`: 这个函数可以自动生成 action 创建函数和 reducer 函数，以便你无需手动编写这些样板代码。你需要为 `createSlice` 提供一个初始状态、一组 reducer 函数以及一个 slice 名称。它将生成一个包含 reducer、action 创建函数和 slice 名称的对象。
    ```javascript
    const mySlice = createSlice({
      name: 'mySlice',
      initialState: { value: 0 },
      reducers: {
        increment: state => {
          state.value += 1;
        },
        decrement: state => {
          state.value -= 1;
        }
      }
    });
    // 使用 auto-generated action 创建函数
    dispatch(mySlice.actions.increment());
    ```
2. `createAsyncThunk`: 这个函数用于生成处理异步请求的 thunk action 创建函数。你需要为 `createAsyncThunk` 提供一个 thunk 名称和一个返回 Promise 的函数。生成的 thunk action 创建函数会 dispatch 一个 pending action，然后运行你提供的异步函数，等待 Promise 解析，然后 dispatch 一个 fulfilled 或 rejected action，取决于 Promise 是解析还是拒绝。
    ```javascript
    const fetchUserById = createAsyncThunk(
      'users/fetchByIdStatus',
      async (userId, thunkAPI) => {
        const response = await userAPI.fetchById(userId);
        return response.data;
      }
    );
    // 使用 thunk action 创建函数
    dispatch(fetchUserById(123));
    ```
这些函数都是 Redux Toolkit 的一部分，旨在简化 Redux 的使用，并减少样板代码的数量。

## Store.js
 ```js
// 1.导入configureStore函数
import { configureStore } from "@reduxjs/toolkit"; 
// 2.导入moviesReducer
import moviesReducer from "./movies/movieSlice";
// 3.使用configureStore创建store
export const store = configureStore({
  // 4.配置reducer
  reducer: {
    // 5.movies状态使用moviesReducer
    movies: moviesReducer,
  },
});
```
主要步骤:
1.导入configureStore函数
2.导入moviesReducer
3.使用configureStore创建store
4.配置reducer
5.指定movies状态使用moviesReducer
configureStore函数可以自动:
- 应用Redux DevTools等中间件
- 合并多个reducer
- 返回一个完整配置好的store
使用它可以简化store的创建过程。

## index.js
```js
import React from "react";
import ReactDOM from "react-dom";
import { Provider } from "react-redux";
import App from "./App";
import { store } from "./features/store";

ReactDOM.render(
  <React.StrictMode>
    <Provider store={store}>
      <App />
    </Provider>
  </React.StrictMode>,
  document.getElementById("root")
);
```

## index.js注释
```jsx
// 1.导入React和ReactDOM
import React from "react";
import ReactDOM from "react-dom";

// 2.导入Provider组件
import { Provider } from "react-redux"; 

// 3.导入App组件
import App from "./App";

// 4.导入store
import { store } from "./features/store";

ReactDOM.render(
 // 5.使用Provider包裹App组件
 <Provider store={store}>  

 <App />

 </Provider>,

 // 6.渲染到根节点
 document.getElementById("root")
);
```
主要步骤:

1.导入React和ReactDOM 2.导入Provider 3.导入App组件 4.导入store 5.使用Provider包裹App组件 6.渲染到根节点

Provider组件可以:

- 让所有子组件都可以访问store
- 实现React组件与Redux的连接

这是整合React和Redux最基本的方式。

## `<Provider store={store}>`
 `<Provider store={store}>`代码块的作用是:
1. Provider组件来自react-redux库,它是连接React应用与Redux状态的组件。
2. store参数指定要使用的Redux store实例。这里传入了之前创建的store。
3. Provider会使其所有子组件都可以访问到store。
4. 子组件可以通过使用useSelector和useDispatch这些Hook来读取和修改Redux状态。
5. 这样就实现了React组件与Redux状态的连接,状态变更可以触发UI重新渲染。
举个例子:
```jsx
// App组件
function App() {
  return (
    <Provider store={store}>
      <Child 
      <ChildB />
    </Provider>
  )
}
// 子组件可以访问store
function Child const count = useSelector(state => state.count)
  // ...
} 
```
所以总结:
- Provider组件连接React与Redux
- store参数指定Redux store实例
- 子组件通过Hook访问状态
- 实现了组件与状态的连接
这是使用React-Redux的基本方式。


## reducer

![[Pasted image 20230910212015.png]]
![[Pasted image 20230910212146.png]]
![[Pasted image 20230910212425.png]]
![[Pasted image 20230910212750.png]]







---

# Redux Toolkit原理
Redux Toolkit 是 Redux 的官方工具集，它封装了一些用于简化 Redux 的 API 和最佳实践，如自动 action type 生成、action 创建函数、immutable update logic，以及处理异步流程等。
以下是 Redux Toolkit 的主要部分：
1. `configureStore`: 这个函数自动处理了 Redux 应用程序的大部分设置，包括 middleware 的设置、reducer 的组合以及 DevTools 的集成。
2. `createReducer` 和 `createSlice`: 这两个函数可以自动处理 action type 的生成和 action 创建函数的创建。
3. `createAsyncThunk`: 这个函数可以帮助你处理异步逻辑，并且自动 dispatch 相应的 action。
4. `createSelector`: 这是一个由 Reselect 库提供的函数，用于创建可记忆的 selector，有助于优化 Redux 应用程序的性能。
以下是一个使用 Redux Toolkit 的简单示例：
```javascript
import { configureStore, createSlice, createAsyncThunk } from '@reduxjs/toolkit'
// 创建一个异步 action
export const fetchUserById = createAsyncThunk(
  'users/fetchByIdStatus',
  async (userId, thunkAPI) => {
    const response = await userAPI.fetchById(userId);
    return response.data;
  }
);
// 使用 createSlice 自动创建 action 和 reducer
const userSlice = createSlice({
  name: 'user',
  initialState: { entities: [], loading: 'idle' },
  reducers: {
    // 这里我们可以定义一些同步的 action
  },
  extraReducers: builder => {
    builder.addCase(fetchUserById.pending, (state, action) => {
      state.loading = 'loading';
    });
    builder.addCase(fetchUserById.fulfilled, (state, action) => {
      state.loading = 'loaded';
      state.entities.push(action.payload);
    });
  }
});
// 自动获取 action 创建函数
export const { actions } = userSlice;
// 创建 store
const store = configureStore({
  reducer: {
     user: userSlice.reducer
  }
});
```
在此代码中：
- 我们首先使用 `createAsyncThunk` 创建了一个异步 action。这个函数接收一个 action type 作为第一个参数，接收一个返回 Promise 的函数作为第二个参数。
- 使用 `createSlice`，我们定义了一个名为 "user" 的 slice，并为其定义了一些初始状态和 reducer。
- `createSlice` 会自动为我们生成相应的 action 创建函数。
- 最后，我们使用 `configureStore` 创建了 Redux store，并将我们刚刚创建的 user reducer 添加到了 store 中。
如果我们需要将应用的状态以表格的方式表示，可以如下：

| 状态 | 说明 |
| --- | --- |
| entities | 用户实体的数组 |
| loading | 描述当前加载状态的字符串，可以是 'idle'、'loading' 或 'loaded' |
这就是 Redux Toolkit 的工作原理和简单使用方法。

```js
  extraReducers: builder => {
    builder.addCase(fetchUserById.pending, (state, action) => {
      state.loading = 'loading';
    });
    builder.addCase(fetchUserById.fulfilled, (state, action) => {
      state.loading = 'loaded';
      state.entities.push(action.payload);
    });
  }
```
`extraReducers` 是 `createSlice` 函数的一个选项，它允许你对由非这个 slice 创建的 actions 进行响应。在这里，你可以处理异步 action creators，如由 `createAsyncThunk` 创建的。
`extraReducers` 接受一个 builder 函数，这个函数可以将 action 与对应的 reducer 关联起来。你可以使用 `builder.addCase` 方法来处理特定的 action。该方法接受两个参数：一个 action creator 以及一个处理这个 action 的 reducer 函数。
在你给出的示例中，`fetchUserById.pending` 和 `fetchUserById.fulfilled` 是由 `createAsyncThunk` 自动生成的 action creators。它们分别在异步请求开始时和结束时被 dispatch。
- `fetchUserById.pending` 的 reducer 将 `loading` 状态设为 `'loading'`，表示正在进行异步请求。
- `fetchUserById.fulfilled` 的 reducer 将 `loading` 状态设为 `'loaded'`，表示异步请求已完成。同时，它还将从 action 的 payload 中获取到的用户数据加入到 `entities` 数组中。
这就是 `extraReducers` 和 builder 的工作原理。这种方式使得处理异步 actions 变得更加清晰和直观。

# Redux面试常见提问

. Redux 是什么？它的作用是什么？
   - Redux 是一个<font color="#b7dde8">用于管理应用程序状态的可预测状态容器</font>。它可以帮助我们在应用程序中更好地组织和管理数据，并提供一种统一的方式来更新和访问状态。<font color="#b7dde8">Redux 的作用是使状态管理变得可预测、可维护和可测试。</font>

2. Redux 中的三个核心原则是什么？
  ?
   - 单一数据源（Single Source of Truth）：整个应用程序的状态被存储在一个单一的 JavaScript 对象中，称为 State。
   - 状态是只读的（State is Read-Only）：不允许直接修改状态，只能通过派发 Action 来描述状态的变化。
   - 使用纯函数来执行状态修改（Changes are made with Pure Functions）：使用纯函数（Reducers）来处理 Action，并根据旧状态和 Action 返回新状态。

3. Redux 的工作流程是怎样的？
  ?
   - Redux 的工作流程可以总结为以下四个步骤：
     1. 使用 `store.dispatch(action)` 派发一个 Action。
     2. Redux Store 调用传入的 Reducer 函数，并传入当前的 State 和 Action。
     3. Reducer 函数根据 Action 的类型和数据来更新 State，并返回一个新的 State。
     4. Redux Store 保存了新的 State，并通知所有订阅了 Store 的组件进行更新。

4. 什么是 Redux 中的 Action？
   - Action 是一个简单的 JavaScript 对象，用于描述状态的变化。Action 必须包含一个 `type` 属性，表示 Action 的类型，还可以包含其他自定义的数据。
   示例代码：
   ```javascript
   const increment = {
     type: 'INCREMENT',
     payload: 1
   };
   const decrement = {
     type: 'DECREMENT',
     payload: 1
   };
   ```

5. 什么是 Redux 中的 Reducer？
  ?
   - Reducer 是一个纯函数，接收旧的 State 和 Action 作为参数，并返回一个新的 State。Reducer 根据 Action 的类型来决定如何更新 State。
   示例代码：
   ```javascript
   const initialState = {
     count: 0
   };
   const counterReducer = (state = initialState, action) => {
     switch (action.type) {
       case 'INCREMENT':
         return { count: state.count + action.payload };
       case 'DECREMENT':
         return { count: state.count - action.payload };
       default:
         return state;
     }
   };
   ```
6. 什么是 Redux 中的 Store？
  ?
   - Store 是一个包含整个应用程序状态的对象。它是唯一的，可以通过 `store.getState()` 来获取当前的状态，通过 `store.dispatch(action)` 来派发 Action，并通过 `store.subscribe(listener)` 来订阅状态的变化。
   - 在 Redux 中，Store 是一个简单的对象，它是整个应用程序的状态存储容器。它包含了应用程序的完整状态树，并提供了一些方法来访问和更新状态。
   Store 有以下职责：
   - 维持应用程序的状态
   - 提供 getState() 方法来获取当前的状态
   - 提供 dispatch(action) 方法来派发并触发状态变化
   - 提供 subscribe(listener) 方法来订阅状态的变化
  下面是一个使用 Redux 创建 Store 的示例代码：
  ```javascript
  import { createStore } from 'redux';
  // 初始状态
  const initialState = {
    count: 0,
  };
  // Reducer 函数
  const counterReducer = (state = initialState, action) => {
    switch (action.type) {
      case 'INCREMENT':
        return { count: state.count + action.payload };
      case 'DECREMENT':
        return { count: state.count - action.payload };
      default:
        return state;
    }
  };
  // 创建 Store
  const store = createStore(counterReducer);
  ```
  在上面的示例中，`createStore` 函数用于创建 Redux Store，它接受一个 Reducer 函数作为参数。我们将 `counterReducer` 作为 Reducer 函数传递给 `createStore`，并将返回的 Store 对象保存在 `store` 变量中。
  现在，我们可以通过 `store.getState()` 方法获取当前的状态，通过 `store.dispatch(action)` 方法派发 Action 来触发状态变化，以及通过 `store.subscribe(listener)` 方法订阅状态的变化。
  请注意，上述代码示例是一个简单的示例，实际上，在应用程序中可能会有更多的 Reducer 和中间件来处理更复杂的状态管理需求。
<!--SR:!2023-07-21,1,230-->

7. 什么是 Redux 中的中间件（Middleware）？它的作用是什么？
   Middleware 是 Redux 的扩展机制，用于处理异步操作、日志记录、错误处理等。它可以在 Action 被派发后到达 Reducer 之前拦截、处理和修改 Action。
   示例代码：
  ```javascript
 import { createStore, applyMiddleware } from 'redux';
 import thunk from 'redux-thunk';
 const store = createStore(
   counterReducer,
   applyMiddleware(thunk)
 );
   ```
   
8. 如何在 React 应用中使用 Redux？
   - 首先，在顶层组件中使用 `Provider` 组件包裹整个应用，将 Redux 的 Store 传递给应用程序。
   示例代码：
  ```jsx
 import { Provider } from 'react-redux';
 import store from './store';
 ReactDOM.render(
   <Provider store={store}>
     <App />
   </Provider>,
   document.getElementById('root')
 );
  ```
   - 然后，在需要访问或更新状态的组件中使用 `connect` 函数从 Redux 的 Store 中获取状态，并使用 `mapStateToProps` 和 `mapDispatchToProps` 将状态和操作映射到组件的 Props。
   示例代码：
 ```jsx
   import { useSelector, useDispatch } from 'react-redux';
   import { increment, decrement } from './actions';
   function Counter() {
     const count = useSelector(state => state.count);
     const dispatch = useDispatch();
     const handleIncrement = () => {
       dispatch(increment(1));
     };
     const handleDecrement = () => {
       dispatch(decrement(1));
     };
     return (
       <div>
         <button onClick={handleIncrement}>+</button>
         <span>{count}</span>
         <button onClick={handleDecrement}>-</button>
       </div>
     );
   }
   ```
   
9. 什么是 Redux 的异步数据流处理方式？
   - Redux 中处理异步操作的常见方式是使用中间件，如 Redux Thunk 或 Redux Saga。这些中间件允许在 Action 被派发时执行异步操作，并在异步操作完成后派发另一个 Action 来更新状态。
   示例代码（使用 Redux Thunk）：
   ```javascript
   // 异步 Action
   const fetchData = () => {
     return (dispatch) => {
       dispatch({ type: 'FETCH_START' });
       // 发起异步请求
       fetch('https://api.example.com/data')
         .then(response => response.json())
         .then(data => {
           dispatch({ type: 'FETCH_SUCCESS', payload: data });
         })
         .catch(error => {
           dispatch({ type: 'FETCH_FAILURE', payload: error });
         });
     };
   };
   // 使用异步 Action
   dispatch(fetchData());
   ```
   
10. Redux 和 React Context 之间有什么区别和联系?
  ?
  Redux 和 React Context 都是用于在 React 应用程序中管理状态的工具，但有一些区别和联系：
  - Redux 是一个独立的状态管理库，提供了更丰富的功能和工具来管理全局状态，包括中间件、调试工具等。它适用于中大型应用程序或需要复杂状态管理的场景。
  - React Context 是 React 提供的原生上下文 API，用于在组件层级之间共享状态。它可以用作简单的全局状态管理解决方案，但在处理复杂状态和性能优化方面相对有限。
  - Redux 可以与 React Context 结合使用，通过 `react-redux` 库中的 `Provider` 和 `connect` 实现 Redux 状态的传递和更新。
   示例代码（使用 React Context）：
   ```jsx
  import React, { createContext, useContext, useReducer } from 'react';
  // 创建 Context
  const CounterContext = createContext();
  // 初始状态和 Reducer
  const initialState = { count: 0 };
  const counterReducer = (state, action) => {
    switch (action.type) {
      case 'INCREMENT':
        return { count: state.count + action.payload };
      case 'DECREMENT':
        return { count: state.count - action.payload };
      default:
        return state;
    }
  };
  // 包裹组件
  const App = () => {
    const [state, dispatch] = useReducer(counterReducer, initialState);
    return (
      <CounterContext.Provider value={{ state, dispatch }}>
        <Counter />
      </CounterContext.Provider>
    );
  };
  // 子组件
  const Counter = () => {
    const { state, dispatch } = useContext(CounterContext);
    const handleIncrement = () => {
      dispatch({ type: 'INCREMENT', payload: 1 });
    };
    const handleDecrement = () => {
      dispatch({ type: 'DECREMENT', payload: 1 });
    };
    return (
      <div>
        <button onClick={handleIncrement}>+</button>
        <span>{state.count}</span>
        <button onClick={handleDecrement}>-</button>
      </div>
    );
  };
  ```



### React状态管理Redux
是的，Redux 在 React 生态系统中仍然非常常用，特别是在大型和复杂的应用程序中。Redux 提供了一种可预测的状态管理解决方案，使得应用程序的状态管理更加可控和可维护。

Redux 的使用场景包括但不限于以下情况：

1. 大型应用程序：当应用程序的状态逻辑非常复杂，或者涉及多个组件之间共享状态时，Redux 提供了一种集中管理应用程序状态的方式。
2. 时间旅行调试：Redux 提供了一个强大的调试工具，可以回放和重放应用程序中的状态变化，帮助开发人员追踪和调试问题。
3. 中间件扩展：Redux 的中间件机制允许开发人员在应用程序的状态更新过程中添加额外的逻辑，例如异步操作、日志记录、路由管理等。
  下面是一个简单的示例，展示了如何在 React 中使用 Redux：
4. 安装必要的依赖：
```bash
npm install react-redux redux
```
2. 创建 Redux store 并定义 actions 和 reducers：
```jsx
// actions.js
export const increment = () => ({
  type: 'INCREMENT',
});
export const decrement = () => ({
  type: 'DECREMENT',
});
// reducers.js
const initialState = 0;
export const counterReducer = (state = initialState, action) => {
  switch (action.type) {
    case 'INCREMENT':
      return state + 1;
    case 'DECREMENT':
      return state - 1;
    default:
      return state;
  }
};
```
3. 创建一个 React 组件来连接 Redux store：
```jsx
// Counter.js
import React from 'react';
import { connect } from 'react-redux';
import { increment, decrement } from './actions';
function Counter(props) {
  return (
    <div>
      <button onClick={props.decrement}>-</button>
      <span>{props.count}</span>
      <button onClick={props.increment}>+</button>
    </div>
  );
}
const mapStateToProps = (state) => ({
  count: state,
});
const mapDispatchToProps = {
  increment,
  decrement,
};
export default connect(mapStateToProps, mapDispatchToProps)(Counter);
```
4. 在根组件中创建 Redux store 并将组件包裹在 `<Provider>` 组件中：
```jsx
// App.js
import React from 'react';
import { createStore } from 'redux';
import { Provider } from 'react-redux';
import { counterReducer } from './reducers';
import Counter from './Counter';
const store = createStore(counterReducer);
function App() {
  return (
    <Provider store={store}>
      <Counter />
    </Provider>
  );
}
export default App;
```
在这个示例中，我们创建了一个简单的计数器应用程序。通过 Redux，我们定义了两个 actions（increment 和 decrement）和一个 reducer（counterReducer）来管理计数器的状态。然后，我们使用 `connect` 函数将 React 组件 `Counter` 连接到 Redux store，并在 `Counter` 组件中使用 Redux store 中的状态和 actions。
这只是一个简单的示例，你可以根据需要扩展和定制 Redux 的使用。
希望这个示例对你有帮助！如果还有其他问题，请随时提问。

当然，这里是另一个示例，演示如何在 React 中使用 Redux：

1. 安装必要的依赖：
```bash
npm install react-redux redux
```
2. 创建 Redux store 并定义 actions 和 reducers：
```jsx
// actions.js
export const addItem = (item) => ({
  type: 'ADD_ITEM',
  payload: item,
});
export const removeItem = (itemId) => ({
  type: 'REMOVE_ITEM',
  payload: itemId,
});
// reducers.js
const initialState = {
  items: [],
};
export const itemReducer = (state = initialState, action) => {
  switch (action.type) {
    case 'ADD_ITEM':
      return {
        ...state,
        items: [...state.items, action.payload],
      };
    case 'REMOVE_ITEM':
      return {
        ...state,
        items: state.items.filter((item) => item.id !== action.payload),
      };
    default:
      return state;
  }
};
```
在这个示例中，我们定义了两个 actions（addItem 和 removeItem）和一个 reducer（itemReducer），用于管理一个简单的物品列表。addItem 用于向列表中添加物品，removeItem 用于从列表中移除指定的物品。
3. 创建一个 React 组件来连接 Redux store：
```jsx
// ItemList.js
import React from 'react';
import { connect } from 'react-redux';
import { addItem, removeItem } from './actions';
function ItemList(props) {
  const handleAddItem = () => {
    const newItem = {
      id: Date.now(),
      name: 'New Item',
    };
    props.addItem(newItem);
  };
  const handleRemoveItem = (itemId) => {
    props.removeItem(itemId);
  };
  return (
    <div>
      <button onClick={handleAddItem}>Add Item</button>
      <ul>
        {props.items.map((item) => (
          <li key={item.id}>
            {item.name}{' '}
            <button onClick={() => handleRemoveItem(item.id)}>Remove</button>
          </li>
        ))}
      </ul>
    </div>
  );
}
const mapStateToProps = (state) => ({
  items: state.items,
});
const mapDispatchToProps = {
  addItem,
  removeItem,
};
export default connect(mapStateToProps, mapDispatchToProps)(ItemList);
```
在这个示例中，我们创建了一个简单的物品列表组件。组件中有一个“Add Item”按钮用于添加物品，并且每个物品后面有一个“Remove”按钮用于移除该物品。通过 Redux，我们使用 `connect` 函数将组件 `ItemList` 连接到 Redux store，并使用 Redux store 中的状态和 actions。
4. 在根组件中创建 Redux store 并将组件包裹在 `<Provider>` 组件中：
```jsx
// App.js
import React from 'react';
import { createStore } from 'redux';
import { Provider } from 'react-redux';
import { itemReducer } from './reducers';
import ItemList from './ItemList';
const store = createStore(itemReducer);
function App() {
  return (
    <Provider store={store}>
      <ItemList />
    </Provider>
  );
}
export default App;
```
在这个示例中，我们创建了一个简单的物品列表应用程序。通过 Redux，我们定义了一个 reducer（itemReducer）来管理物品列表的状态。然后，我们使用 `connect` 函数将 React 组件 `ItemList` 连接到 Redux store，并在 `ItemList` 组件中使用 Redux store 中的状态和 actions。


### Redux tookits


Redux Toolkit是一个官方推荐的Redux工具集，旨在简化Redux应用程序的开发过程。它提供了一组实用的函数和工具，可以帮助开发人员更快地编写Redux代码，并提供了一种更简洁、更直观的方式来定义Redux的状态管理。

下面是一个使用Redux Toolkit的简单示例：

1. 首先，确保你的项目中已经安装了Redux和Redux Toolkit。你可以使用npm或者yarn来安装它们：

```shell
npm install redux @reduxjs/toolkit
```

2. 创建一个Redux store，这是整个应用程序的状态管理中心。在这个示例中，我们将使用Redux Toolkit的`configureStore`函数来创建store：

```javascript
import { configureStore } from '@reduxjs/toolkit';
import counterReducer from './counterSlice';

const store = configureStore({
  reducer: {
    counter: counterReducer,
  },
});

export default store;
```

3. 创建一个Redux reducer，用于处理状态的变化。在这个示例中，我们将使用Redux Toolkit的`createSlice`函数来定义reducer：

```javascript
import { createSlice } from '@reduxjs/toolkit';

const counterSlice = createSlice({
  name: 'counter',
  initialState: 0,
  reducers: {
    increment: (state) => state + 1,
    decrement: (state) => state - 1,
  },
});

export const { increment, decrement } = counterSlice.actions;
export default counterSlice.reducer;
```

4. 在应用程序的组件中使用Redux store和reducer。在这个示例中，我们将使用React组件来展示计数器的值，并通过按钮来增加或减少计数器的值：

```javascript
import React from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { increment, decrement } from './counterSlice';

const Counter = () => {
  const counter = useSelector((state) => state.counter);
  const dispatch = useDispatch();

  return (
    <div>
      <h1>Counter: {counter}</h1>
      <button onClick={() => dispatch(increment())}>Increment</button>
      <button onClick={() => dispatch(decrement())}>Decrement</button>
    </div>
  );
};

export default Counter;
```

这只是一个简单的示例，演示了如何使用Redux Toolkit来创建一个基本的计数器应用程序。使用Redux Toolkit，你可以更快地编写Redux代码，并且不需要手动编写大量的模板代码。它还提供了许多其他功能，如异步操作的处理和状态持久化等。

你可以在Redux Toolkit的官方文档中找到更多关于如何使用Redux Toolkit的示例和详细信息：[Redux Toolkit官方文档](https://redux-toolkit.js.org/)。

下面是对代码块中每一行的详细注释：
```javascript
// 设置一个 HTML 元素作为我们的“用户界面”，用于显示文本内容
const valueEl = document.getElementById('value')
// 每当存储状态发生变化时，通过读取最新的存储状态来更新用户界面，显示新的数据
function render() {
  // 从存储中获取最新的状态
  const state = store.getState()
  // Update the UI with the new value
  // 使用新的值更新用户界面
  valueEl.innerHTML = state.value.toString()
}
// 使用初始数据更新用户界面
render()
// 并订阅在数据将来发生更改时进行重新绘制
store.subscribe(render)
```
上述注释提供了对代码块中每行代码的详细解释，包括代码的作用和功能。
代码的主要功能是通过存储状态的变化更新用户界面。在初始加载时，使用 `render` 函数将初始数据显示在用户界面上。然后，使用 `store.subscribe(render)` 订阅存储状态的变化，当状态发生变化时，会自动调用 `render` 函数更新用户界面。

下面是对代码块中每一行的详细注释：
```javascript
// Handle user inputs by "dispatching" action objects,
// which should describe "what happened" in the app
// 处理用户输入，通过“分发”动作对象，该对象应描述应用程序中发生的事件
// Listen for click event on 'increment' button and dispatch 'counter/incremented' action
document.getElementById('increment').addEventListener('click', function() {
  store.dispatch({ type: 'counter/incremented' })
})
// Listen for click event on 'decrement' button and dispatch 'counter/decremented' action
document.getElementById('decrement').addEventListener('click', function() {
  store.dispatch({ type: 'counter/decremented' })
})
// Listen for click event on 'incrementIfOdd' button and dispatch 'counter/incremented' action
// only if the current value in the store is odd
document.getElementById('incrementIfOdd').addEventListener('click', function() {
  // We can write logic to decide what to do based on the state
  // 可以根据状态编写逻辑来决定要执行的操作
  if (store.getState().value % 2 !== 0) {
    store.dispatch({ type: 'counter/incremented' })
  }
})
// Listen for click event on 'incrementAsync' button and dispatch 'counter/incremented' action
// after a delay of 1000 milliseconds (1 second)
document.getElementById('incrementAsync').addEventListener('click', function() {
  // We can also write async logic that interacts with the store
  // 我们还可以编写与存储交互的异步逻辑
  setTimeout(function() {
    store.dispatch({ type: 'counter/incremented' })
  }, 1000)
})
```
上述注释提供了对代码块中每行代码的详细解释，包括代码的作用和功能。
代码的主要功能是处理用户输入，并通过分发动作对象来描述应用程序中发生的事件。当用户点击不同的按钮时，会触发不同的事件处理逻辑。
- 对于 `increment` 按钮，点击时将分发一个 `{ type: 'counter/incremented' }` 的动作。
- 对于 `decrement` 按钮，点击时将分发一个 `{ type: 'counter/decremented' }` 的动作。
- 对于 `incrementIfOdd` 按钮，点击时会检查存储中的值是否为奇数，如果是，则分发一个 `{ type: 'counter/incremented' }` 的动作。
- 对于 `incrementAsync` 按钮，点击时会使用 `setTimeout` 生成一个延迟一秒的异步操作，然后分发一个 `{ type: 'counter/incremented' }` 的动作。
通过分发不同的动作，可以在存储状态中触发相应的状态更新和应用程序逻辑。

###  Redux Middleware and Side Effects

Earlier, we said that Redux reducers must never contain "side effects". **A "side effect" is any change to state or behavior that can be seen outside of returning a value from a function**. Some common kinds of side effects are things like:  
之前，我们说过 Redux 减速器绝不能包含“副作用”。 “副作用”是指除了从函数返回值之外可以看到的任何状态或行为的变化。一些常见的副作用如下：

- Logging a value to the console  
    将值记录到控制台
- Saving a file 保存文件
- Setting an async timer 设置异步计时器
- Making an AJAX HTTP request  
    发出 AJAX HTTP 请求
- Modifying some state that exists outside of a function, or mutating arguments to a function  
    修改函数外部存在的某些状态，或改变函数的参数
- Generating random numbers or unique random IDs (such as `Math.random()` or `Date.now()`)  
    生成随机数或唯一的随机 ID（例如 `Math.random()` 或 `Date.now()` ）

However, any real app will need to do these kinds of things _somewhere_. So, if we can't put side effects in reducers, where _can_ we put them?  
然而，任何真正的应用程序都需要在某个地方做这些事情。那么，如果我们不能将副作用放入减速器中，我们可以将它们放在哪里呢？

**Redux middleware were designed to enable writing logic that has side effects**.  
Redux 中间件旨在支持编写具有副作用的逻辑。

As we said [in Part 4](https://redux.js.org/tutorials/fundamentals/part-4-store#middleware-use-cases), a Redux middleware can do _anything_ when it sees a dispatched action: <u>log something, modify the action, delay the action, make an async call, and more.</u> Also, since middleware form a pipeline around the real `store.dispatch` function, this also means that we could actually pass something that _isn't_ a plain action object to `dispatch`, as long as a middleware intercepts that value and doesn't let it reach the reducers.  
正如我们在第 4 部分中所说，Redux 中间件在看到分派的操作时可以执行任何操作：记录某些内容、修改操作、延迟操作、进行异步调用等等。此外，由于中间件围绕真实的 `store.dispatch` 函数形成了一个管道，这也意味着我们实际上可以将不是普通操作对象的东西传递给 `dispatch` ，只要中间件拦截该值并且不让它到达减速器。

Middleware also have access to `dispatch` and `getState`. That means you could write some async logic in a middleware, and still have the ability to interact with the Redux store by dispatching actions.  
中间件还可以访问 `dispatch` 和 `getState` 。这意味着您可以在中间件中编写一些异步逻辑，并且仍然能够通过分派操作与 Redux 存储进行交互。

这段代码实现了两个中间件（middleware）函数：`delayedActionMiddleware` 和 `fetchTodosMiddleware`。中间件是 Redux 中用于拦截和处理 action 的函数。
下面是对代码中每一行的详细注释：
```javascript
import { client } from '../api/client'
// Middleware that delays the dispatch of an action by one second
const delayedActionMiddleware = storeAPI => next => action => {
  if (action.type === 'todos/todoAdded') {
    setTimeout(() => {
      // Delay this action by one second
      next(action)
    }, 1000)
    return
  }
  return next(action)
}
// Middleware that fetches todos from the server and dispatches an action with the received todos
const fetchTodosMiddleware = storeAPI => next => action => {
  if (action.type === 'todos/fetchTodos') {
    // Make an API call to fetch todos from the server
    client.get('todos').then(todos => {
      // Dispatch an action with the todos we received
      storeAPI.dispatch({ type: 'todos/todosLoaded', payload: todos })
    })
  }
  return next(action)
}
```
上述注释提供了对代码中每行代码的详细解释，包括代码的作用和功能。
- `delayedActionMiddleware` 是一个中间件函数，它会拦截所有的 action，并在 action 类型为 `'todos/todoAdded'` 时延迟一秒后再将 action 传给下一个中间件或 reducer。
- `fetchTodosMiddleware` 是另一个中间件函数，它会拦截所有的 action，并在 action 类型为 `'todos/fetchTodos'` 时发起一个 API 请求从服务器获取 todos 数据，并在请求成功后将获取到的 todos 数据以一个新的 action `'todos/todosLoaded'` 的形式派发给 store。
这些中间件用于在 action 被派发到 reducer 之前进行一些额外的处理，例如延迟 action 的派发或进行异步操作。
需要注意的是，中间件函数都遵循 Redux 中间件的编写规范，接受一个 `storeAPI` 参数，内部返回一个函数，该函数接受一个 `next` 参数，再返回一个函数，该函数接受一个 `action` 参数。
希望以上注释能够帮助您理解代码中的中间件功能！如果您还有其他问题，请随时提问。



用户事件：用户按下键盘、点击鼠标、滚动屏幕、缩放页面尺寸等。
服务端事件：应用程序从服务器接收到数据或错误



虚拟DOM是真实DOM的一个快速的、仅存在于内存中的映射，它是一个抽象，允许我们把JavaScript和DOM当作是反应式的。让我们看看它是如何工作的



React组件有5个属于组件更新阶段的生命周期方法：

- componentWillReceiveProps()
- shouldComponentUpdate()
- componentWillUpdate()
- render()
- componentDidUpdate()


- React.PropTypes.number：验证属性是否为数字。
- React.PropTypes.string：验证属性是否为字符串。
- React.PropTypes.bool：验证属性是否为布尔值。
- React.PropTypes.object：验证属性是否为对象。
- React.PropTypes.element：验证属性是否为React元素。


什么是单元测试？顾名思义，单元测试就是用来测试应用程序的一个单元。在应用程序中，一个单元通常是一个函数，这意味着编写单元测试主要是为函数编写测试。

单元测试的基本思想是只测试应用程序中的某个功能，通常这个功能由一个函数实现。你需要单独测试这个函数，这意味着应用程序中这个函数依赖的其他部分在测试中是用不到的。相反，它们需要在测试中被模拟。模拟一个JavaScript对象就是创建一个假对象，来模拟实际对象的行为。在单元测试中，这个假对象叫作模拟对象（mock） ，创建它的过程叫作模拟（mocking） 。

在Flux中，我们把应用的关注点分成4种逻辑模块：

- Action（动作）
- Dispatcher（分发器）
- Store（存储）
- View（视图）

动作创建之后会怎样流动呢？最终又会被哪个模块接收？答案是存储。

存储负责管理应用中的数据。它们提供了读取数据的方法，但是没有提供修改数据的方法。如果需要修改，则需要创建并==分发==一个动作来实现。
顾名思义，分发器就是用来做这个的。它负责把所有的动作分别分发到每个存储中：
<!--SR:!2023-07-23,3,250-->

它通过分发器管理注册过的回调函数。
所有的动作都会通过分发器被分发到每个存储中。
数据流如下：

Actions > Dispatcher > Stores 
可以看到，分发器在数据流中占据核心地位：所有的动作都流经它，所有的存储都向它注册。在分发器中，动作会依次被分发，换句话说，只有当上一个动作处理完毕后，下一个动作才会被分发。在Flux架构中，动作不能脱离分发器独立使用。