
## Suspense,Suspenselist组件
Suspense 是 React 中的一个功能，它可以在加载完成之前阻塞显示图像、CSS 和字体，但不会阻塞流媒体和并发渲染。[1](about:blank#sjevt%7CDiscover.Chat.SydneyClickPageCitation%7Cadpclick%7C0%7C5b5fd0db-5090-468b-976b-b74d1f713379)这可以帮助避免视觉上的 popcorning 现象，即视觉效果的突然出现和布局的变化。[2](about:blank#sjevt%7CDiscover.Chat.SydneyClickPageCitation%7Cadpclick%7C1%7C5b5fd0db-5090-468b-976b-b74d1f713379)

使用 Suspense 的一种方法是配合 React.lazy 来进行代码拆分，这样可以在加载组件时显示一个 fallback 的界面。例如：

```jsx
const ProfilePage = React.lazy(() => import('./ProfilePage'));
<Suspense fallback={<Spinner />}>
  <ProfilePage />
</Suspense>
```

[你可以参考这篇文章](https://juejin.cn/post/6994674140825272334)[1](https://juejin.cn/post/6994674140825272334)[了解更多关于 Suspense 的用法和特性。](https://juejin.cn/post/6994674140825272334)[1](https://juejin.cn/post/6994674140825272334): [React 18 新特性（二）：Suspense & SuspenseList - 掘金](https://juejin.cn/post/6994674140825272334)
早在 React 16 版本，就可以使用 `React.lazy` 配合 `Suspense` 来进行代码拆分，我们来回顾一下之前的用法。
User.jsx
```jsx
import React, { useState, useEffect } from 'react';

// 网络请求，获取 user 数据
const requestUser = id =>
    new Promise(resolve =>
        setTimeout(() => resolve({ id, name: `用户${id}`, age: 10 + id }), id * 1000)
    );

const User = props => {
    const [user, setUser] = useState({});

    useEffect(() => {
        requestUser(props.id).then(res => setUser(res));
    }, [props.id]);
 
    return <div>当前用户是: {user.name}</div>;
};

export default User;

```
在 App 组件中通过 `React.lazy` 的方式加载 `User` 组件（使用时需要用 `Suspense` 组件包裹起来哦）
App.jsx
```jsx
import React from "react";
import ReactDOM from "react-dom";

const User = React.lazy(() => import("./User"));

const App = () => {
    return (
        <>
            <React.Suspense fallback={<div>Loading...</div>}>
                <User id={1} />
            </React.Suspense>
        </>
    );
};

ReactDOM.createRoot(document.getElementById("root")).render(<App />);

```

fallback 是一个 React 组件，它会在 Suspense 组件加载的过程中显示。当 Suspense 组件的子组件还没有加载完成时，fallback 组件会被显示。当子组件加载完成后，fallback 组件会被卸载。

---
```jsx
const requestUser = id =>
    new Promise(resolve =>
        setTimeout(() => resolve({ id, name: `用户${id}`, age: 10 + id }), id * 1000)
    );
```
这是一个函数，它接受一个 id 参数并返回一个 Promise。这个 Promise 会在 id * 1000 毫秒后 resolve，返回一个对象，包含 id、name 和 age 三个属性。你可以使用 async/await 或者 Promise.then() 来获取这个对象。

```javascript
const requestUser = async (id) => {
  const user = await new Promise(resolve =>
    setTimeout(() => resolve({ id, name: `用户${id}`, age: 10 + id }), id * 1000)
  );
  return user;
};

// 或者使用 Promise.then()
const requestUser = (id) => {
  return new Promise(resolve =>
    setTimeout(() => resolve({ id, name: `用户${id}`, age: 10 + id }), id * 1000)
  );
};

requestUser(1).then(user => console.log(user));
```

这里有一篇关于 Promise 的文章，你可以参考一下： : [Promise - JavaScript | MDN](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Promise)

### 新版 User 组件编写方式

```jsx
const User = async (props) => {
    const user = await requestUser(props.id);
    return <div>当前用户是: {user.name}</div>;
};

```
多希望 `User` 组件能这样写，省去了很多冗余的代码，并且能够在请求完成之前统一展示 `fallback`

但是我们又不能直接使用 `async`、`await` 去编写组件。这时候怎么办呢？

结合上面我们讲述的 `Suspense` 实现原理，那我们可以封装一层 `promise`，请求中，我们将 `promise` 作为异常抛出，请求完成展示结果。

`wrapPromise` 函数的含义：

- 接受一个 `promise` 作为参数
    
- 定义了 `promise` 状态和结果
    
- 返回一个包含 `read` 方法的对象
    
- 调用 `read` 方法时，会根据 `promise` 当前的状态去判断抛出异常还是返回结果。
    
```jsx
function wrapPromise(promise) {
    let status = "pending";
    let result;
    let suspender = promise.then(
        (r) => {
            status = "success";
            result = r;
        },
        (e) => {
            status = "error";
            result = e;
        }
    );
    return {
        read() {
            if (status === "pending") {
                throw suspender;
            } else if (status === "error") {
                throw result;
            } else if (status === "success") {
                return result;
            }
        },
    };
}

```

### 使用 `wrapPromise` 重新改写一下 `User` 组件

```jsx
// 网络请求，获取 user 数据
const requestUser = (id) =>
    new Promise((resolve) =>
        setTimeout(
            () => resolve({ id, name: `用户${id}`, age: 10 + id }),
            id * 1000
        )
    );

const resourceMap = {
    1: wrapPromise(requestUser(1)),
};

const User = (props) => {
    const resource = resourceMap[props.id];
    const user = resource.read();
    return <div>当前用户是: {user.name}</div>;
};

```
这时候可以看到界面首先展示 `loading`，请求结束后，直接将数据展示出来。不需要编写副作用代码，也不需要在组件内进行 `loading` 的判断。

### SuspenseList

上面我们讲述了 `Suspense` 的用法，那如果有多个 `Suspense` 同时存在时，我们想控制他们的展示顺序以及展示方式，应该怎么做呢？

React 中也提供了一个新的组件：`SuspenseList`

#### SuspenseList 属性

`SuspenseList` 组件接受三个属性

- `revealOrder`: 子 `Suspense` 的加载顺序
    
    - forwards: 从前向后展示，无论请求的速度快慢都会等前面的先展示
        
    - Backwards: 从后向前展示，无论请求的速度快慢都会等后面的先展示
        
    - together: 所有的 Suspense 都准备好之后同时显示
        
- tail: 指定如何显示 `SuspenseList` 中未准备好的 `Suspense`
    
    - 不设置：默认加载所有 Suspense 对应的 fallback
        
    - collapsed：仅展示列表中下一个 Suspense 的 fallback
        
    - hidden: 未准备好的项目不限时任何信息
        
- children: 子元素
    
    - 子元素可以是任意 React 元素
        
    - **当子元素中包含非 `Suspense` 组件时，且未设置 `tail` 属性，那么此时所有的 `Suspense` 元素必定是同时加载，设置 `revealOrder` 属性也无效。当设置 `tail` 属性后，无论是 `collapsed` 还是 `hidden`，`revealOrder` 属性即可生效**
        
    - 子元素中多个 `Suspense` 不会相互阻塞

#### SuspenseList 使用

`User` 组件
```jsx
import React from "react";

function wrapPromise(promise) {
    let status = "pending";
    let result;
    let suspender = promise.then(
        (r) => {
            status = "success";
            result = r;
        },
        (e) => {
            status = "error";
            result = e;
        }
    );
    return {
        read() {
            if (status === "pending") {
                throw suspender;
            } else if (status === "error") {
                throw result;
            } else if (status === "success") {
                return result;
            }
        },
    };
}

// 网络请求，获取 user 数据
const requestUser = (id) =>
    new Promise((resolve) =>
        setTimeout(
            () => resolve({ id, name: `用户${id}`, age: 10 + id }),
            id * 1000
        )
    );

const resourceMap = {
    1: wrapPromise(requestUser(1)),
    3: wrapPromise(requestUser(3)),
    5: wrapPromise(requestUser(5)),
};

const User = (props) => {
    const resource = resourceMap[props.id];
    const user = resource.read();
    return <div>当前用户是: {user.name}</div>;
};

export default User;

```
App组件
```jsx
import React from "react";
import ReactDOM from "react-dom";

const User = React.lazy(() => import("./User"));
// 此处亦可以不使用 React.lazy()，直接使用以下 import 方式引入也可以
// import User from "./User"

const App = () => {
    return (
        <React.SuspenseList revealOrder="forwards" tail="collapsed">
            <React.Suspense fallback={<div>Loading...</div>}>
                <User id={1} />
            </React.Suspense>
            <React.Suspense fallback={<div>Loading...</div>}>
                <User id={3} />
            </React.Suspense>
            <React.Suspense fallback={<div>Loading...</div>}>
                <User id={5} />
            </React.Suspense>
        </React.SuspenseList>
    );
};

ReactDOM.createRoot(document.getElementById("root")).render(<App />);

```


## startTransition
[startTransition 是 React 18 的一个新特性，它可以让你更新状态而不会阻塞 UI。startTransition 函数可以将状态更新标记为过渡。当你在 startTransition 函数中更新状态时，React 会立即执行这个函数，并将所有在执行期间发生的状态更新标记为过渡。这些过渡不会阻塞 UI，也不会显示不必要的加载指示器](https://react.dev/reference/react/startTransition)[1](https://react.dev/reference/react/startTransition)。

```jsx
import { startTransition } from 'react';

function TabContainer() {
  const [tab, setTab] = useState('about');

  function selectTab(nextTab) {
    startTransition(() => {
      setTab(nextTab);
    });
  }

  // ...
}
```



## 什么是并发 React？ [](https://react.docschina.org/blog/2022/03/29/react-v18#what-is-concurrent-react "Link for 什么是并发 React？")

React 18 中最重要的更新内容是我们希望你永远不会考虑的：并发。我们认为这对于应用开发者而言是一件非常好的事情，尽管这对于库的维护者来说可能有点复杂。

并发渲染本身并不是一个功能。它是一个新的底层机制，使得 React 能够同时准备多个版本的 UI。你可以把并发视为一种底层实现的细节——它解锁了许多新功能因而非常有价值。React 在底层实现上使用了非常复杂的技术，如**优先队列和多级缓冲**。但是你不会在任何公共 API 中感知到这些。

并发模式 React 比典型的实现细节更重要──它是 React 核心渲染模型的基础性更新。因此，尽管了解并发渲染底层工作原理不是很重要，但如果是为了追求更高的技术层次，倒是值得去了解它。

并发模式的一个关键特性是渲染可中断。当首次升级到 React 18，在加入任何并发功能之前，更新内容渲染的方式和 React 之前的版本一样——通过一个单一的且不可中断的同步事务进行处理。同步渲染意味着，一旦开始渲染就无法中断，直到用户可以在屏幕上看到渲染结果。

在并发渲染中，情况并不总是如此。React 可能开始渲染一个更新，然后中途挂起，稍后又继续。它甚至可能完全放弃一个正在进行的渲染。React 保证即使渲染被中断，UI 也会保持一致。为了实现这一点，它会在整个 DOM 树被计算完毕前一直等待，完毕后再执行 DOM 变更。这样做，React 就可以在后台提前准备新的屏幕内容，而不阻塞主线程。这意味着用户输入可以被立即响应，即使存在大量渲染任务，也能有流畅的用户体验。

**另一个例子是可重用状态。并发 React 可以从屏幕中移除部分 UI，然后在稍后将它们再添加回来，并重用之前的状态。例如，当用户来回切换标签页，React 应该能够立即将屏幕恢复到它先前的状态。在即将到来的次要版本中，我们计划添加一个新的名为 `<Offscreen>` 的组件，它实现了这种模式。同样地，你将能够使用 Offscreen 在后台准备新的 UI，在显示前就准备完毕以便快速响应。**

并发渲染是一个 React 中非常强大的工具，并且我们大多数新功能都是利用了它的优势来创建的，包括 Suspense，transition 和流式服务端渲染。但是在并发渲染这个方向，React 18 也仅仅只是实现我们最终目标的第一步。
你可以在开发环境中使用 [`<StrictMode>`](https://react.docschina.org/reference/react/StrictMode) 以利于暴露并发模式相关的问题。严格模式是不影响生产环境的，但是在开发环境中它将会记录额外的警告日志，**并且被视为幂等的函数将被调用两次**。这没办法捕获所有异常，但是能够有效预防大部分常见的错误类型。
在升级到 React 18 后，可以立即开始使用并发模式的功能。例如，你可以使用 `startTransition` 在屏幕内容之间进行导航，而不会阻塞用户输入；或者使用 `useDeferredValue` 来节流处理开销巨大的重新渲染。

## 自动批处理
```jsx
// 以前: 只有 React 事件会被批处理。  
setTimeout(() => {  

setCount(c => c + 1);  

setFlag(f => !f);  

// React 会渲染两次，每次更新一个状态（没有批处理）  

}, 1000);  

  

// 现在: 超时，promise，本机事件处理程序  

// 原生应用时间处理程序或者任何其他时间都被批处理了  

setTimeout(() => {  

setCount(c => c + 1);  

setFlag(f => !f);  

// 最终，React 将仅会重新渲染一次（这就是批处理！）  

}, 1000);`
```

## 过渡更新
过渡（transition）更新是 React 中一个新的概念，用于区分紧急和非紧急的更新。

- **紧急更新** 对应直接的交互，如输入，点击，按压等。
- **过渡更新** 将 UI 从一个视图过渡到另一个。

像输入，点击，按压等紧急更新，需要立刻响应以符合人们对物理对象行为的预期。否则，他们就会觉得“不对劲”。但是，过渡更新不太一样，因为用户对感知到屏幕上的每一个中间值这件事是没有预期的。

举个例子，当我们在一个下拉菜单中选择了一个过滤器，你期望的是这个过滤器按钮在你点击的时候立即就能响应。然而，实际结果可能是不连贯的过渡。这样一个较短的延迟是难以察觉的，而且这往往也是能符合预期的。并且如果你在渲染完成之前，再次改变了过滤器，你需要关心的其实只是最新的结果。

通常情况下，为了更好的用户体验，一个用户输入应该同时产生一个紧急更新和一个过渡更新。你可以在一个输入事件中使用 `startTransition` API 告诉 React 哪些更新是紧急更新，哪些又是过渡更新：

```jsx
import { startTransition } from 'react';  

// 紧急更新: 显示输入的内容  
setInputValue(input);  

// 将任何内部的状态更新都标记为过渡更新  
startTransition(() => {  
  // 过渡更新: 展示结果  
  setSearchQuery(input);  
});
```

被包裹在 `startTransition` 中的更新会被处理为过渡更新，如果有紧急更新出现，比如点击或者按键，则会中断过渡更新。如果一个过渡更新被用户中断（比如，快速输入多个字符），React 将会抛弃未完成的渲染结果，然后仅渲染最新的内容。

- `useTransition`： 一个用于开启过渡更新的 hook，用于跟踪待定转场状态。
- `startTransition`： 当 hook 不能使用时，用于开启过渡的方法。

并发渲染中将会加入过渡更新，允许更新被中断。如果更新内容被重新挂起，过渡机制也会告诉 React 在后台渲染过渡内容时继续展示当前内容（查看 [Suspense 意见征求](https://github.com/reactjs/rfcs/blob/main/text/0213-suspense-in-react-18.md) 了解更多信息）。

## 新的 Suspense 特性
Suspense 允许你声明式地为一部分还没有准备好被展示的组件树指定加载状态：

```jsx
<Suspense fallback={<Spinner />}>
  <Comments />
</Suspense>
```

Suspense 使得“UI 加载状态”成为了 React 编程模型中最高级的声明式概念。我们基于此能够构建更高级的功能。

几年前，我们推出了一个受限制版的 Suspense。但是唯一支持的场景就是用 `React.lazy` 拆分代码，而且在服务端渲染时完全没有作用。

在 React 18 中，我们已经支持了服务端 Suspense，并且使用并发渲染特性扩展了其功能。

React 18 中的 Suspense 在与 transition API 结合时效果最好。如果你在 transition 期间挂起，React 不会让已显示的内容被之前的内容取代。相反，React 会延迟渲染，直到有足够的数据，以防止出现加载状态错误。

## 新的客户端和服务端渲染 APIs
我们利用这次版本更新的机会，重新设计了我们为在客户端和服务端进行渲染所暴露的 API。这些更改允许用户在升级到 React 18 使用新的 API 时，也能继续使用 React 17 中的旧 API。
#### React DOM Client [](https://react.docschina.org/blog/2022/03/29/react-v18#react-dom-client "Link for React DOM Client")
这些新的 API 现在可以从 `react-dom/client` 中导出：

- `createRoot`：为 `render` 或者 `unmount` 创建根节点的新方法。请用它替代 `ReactDOM.render`。如果没有它，React 18 中的新功能就无法生效。

```jsx
import { createRoot } from 'react-dom';

const container = document.getElementById('root');
const root = createRoot(container);
root.render(<App />);
```

- `hydrateRoot`：hydrate 服务端渲染的应用的新方法。使用它来替代 `ReactDOM.hydrate` 与新的 React DOM 服务端 API 一起使用。如果没有它，React 18 中的新功能就无法生效。
```jsx
import { hydrateRoot } from 'react-dom';

const container = document.getElementById('root');
const root = hydrateRoot(container);
root.render(<App />);
```
`createRoot` 和 `hydrateRoot` 都能接受一个新的可选参数叫做 `onRecoverableError`，它能在 React 在渲染或者 hydrate 过程发生错误后又恢复时，做日志记录对你进行通知。默认情况下，React 会使用 [`reportError`](https://developer.mozilla.org/en-US/docs/Web/API/reportError)，如果在老旧版本浏览器中，则会使用 `console.error`。
[参阅 React DOM Client 的文档](https://react.docschina.org/reference/react-dom/client)。

#### React DOM Server [](https://react.docschina.org/blog/2022/03/29/react-v18#react-dom-server "Link for React DOM Server")

这些新的 API 现在可以从 `react-dom/server` 中导出，并且在服务端端完全支持流式 Suspense：

- `renderToPipeableStream`：用于 Node 环境中的流式渲染。
- `renderToReadableStream`：对新式的非主流运行时环境，比如 Deno 和 Cloudflare workers。

现有的 `renderToString` 方法仍然可以使用，但是并不推荐这样做。

<font color="#00b050">流式渲染</font>是 React 18 的一个新特性，它允许你并行地分发 HTML 片段。这样可以让渲染出的首字节有意义的内容给用户速度更快。相对于 renderToString，流是异步的。这个可以让你的 Node.js 服务一次性渲染多个请求，并且保持在高请求压力环境下的及时响应。在一个持续的时间内，如果网络阻塞了，它可以停止 React 的渲染，并且不会因为重的网络请求影响其他轻请求1。

你可以参考这篇文章了解更多关于 React 18 的新特性： [React 18 新特性（一）：Concurrent Mode - 掘金](https://juejin.cn/post/6994674140825272334)。

```jsx
import { renderToPipeableStream } from 'react-dom/server';

const stream = renderToPipeableStream(<App />);
stream.pipe(response);
```
[1](https://juejin.cn/post/7064759195710521381): [React----React应用程序流式服务端渲染 - yellman - 博客园](https://www.cnblogs.com/xunxing/p/39481f7f8b0afea05b78fff25529f005.html)

## 新的严格模式行为 [](https://react.docschina.org/blog/2022/03/29/react-v18#new-strict-mode-behaviors "Link for 新的严格模式行为")

**在未来，我们希望新增一个功能，允许 React 在保留状态的同时添加和移除 UI。例如，当一个用户标签页切出又切回时，React 应该能够立即将之前的页面内容恢复到它先前的状态。为了实现这一点，React 将在卸载后又重新挂载组件树时，复用之前的状态。**

这个功能将给 React 应用带来更好的开箱即用能力，但要求组件能够灵活应对多次安装和销毁的副作用。对于大多数副作用不需要任何改动也依然能够生效，但是部分副作用需要保证它们只进行一次挂载或销毁。

为了利于暴露这些问题，React 18 为严格模式下的开发环境引入了一个新的检查机制。每当组件第一次挂载时，这个检查机制将自动卸载又重新挂载每个组件，并在第二次挂载时复用先前的状态。

在这个变更之前，React 是在挂载组件时产生一些副作用：

```
* React 装载组件
  * layout effect 创建
  * effect 创建
```

在 React 18 的严格模式下，React 在开发模式下将会模拟组件的卸载和挂载：

```
* React 挂载组件
  * layout effect 创建
  * effect 创建
* React 模拟卸载组件
  * layout effect 销毁
  * effect 销毁
* React 模拟挂载组件，并复用之前的状态
  * layout effect 创建
  * effect 创建
```
[参阅确保状态可复用的文档](https://react.docschina.org/reference/react/StrictMode#fixing-bugs-found-by-re-running-effects-in-development)。

#### 新的 Hook [](https://react.docschina.org/blog/2022/03/29/react-v18#new-hooks "Link for 新的 Hook")

#### useId [](https://react.docschina.org/blog/2022/03/29/react-v18#useid "Link for useId")

`useId` 是一个新的 hook，用于生成在客户端和服务端两侧都独一无二的 id，避免 hydrate 后两侧内容不匹配。它主要用于需要唯一 id 的，具有集成 API 的组件库。这个更新不仅解决了一个在 React 17 及更低版本中的存在的问题，而且它会在 React 18 中发挥更重要的作用，因为新的流式服务端渲染响应 HTML 的方式将是无序的，需要独一无二的 id 作为索引。[参阅文档](https://react.docschina.org/reference/react/useId)。

> Note
> `useId` **不是** 为了生成 [列表中的 key](https://react.docschina.org/learn/rendering-lists#where-to-get-your-key)。key 应该根据你的数据生成。

#### useTransition [](https://react.docschina.org/blog/2022/03/29/react-v18#usetransition "Link for useTransition")

`useTransition` 和 `startTransition` 让你能够将一些状态更新标记为过渡更新。默认情况下，状态更新都被视为紧急更新。React 将允许紧急更新（例如，更新一个文本输入内容）打断过渡更新（例如，渲染一个搜索结果列表）。[参阅文档](https://react.docschina.org/reference/react/useTransition)。

#### useDeferredValue [](https://react.docschina.org/blog/2022/03/29/react-v18#usedeferredvalue "Link for useDeferredValue")

`useDeferredValue` 允许推迟渲染树的非紧急更新。这和防抖操作非常相似，但是有一些改进。它没有固定的延迟时间，React 会在第一次渲染在屏幕上出现后立即尝试延迟渲染。延迟渲染是可中断的，它不会阻塞用户输入。[参阅文档](https://react.docschina.org/reference/react/useDeferredValue)。

#### useSyncExternalStore [](https://react.docschina.org/blog/2022/03/29/react-v18#usesyncexternalstore "Link for useSyncExternalStore")

`useSyncExternalStore` 是一个新的 hook，允许使用第三方状态管理来支持并发模式，并且能通过对 store 进行强制更新实现数据同步。对第三方数据源的订阅能力的实现上，消除了对 `useEffect` 的依赖，推荐任何 React 相关的第三方状态管理库使用这个新特性。[参阅文档](https://react.docschina.org/reference/react/useSyncExternalStore)。

> Note
> `useSyncExternalStore` 旨在供库使用，而不是应用程序代码。

#### useInsertionEffect [](https://react.docschina.org/blog/2022/03/29/react-v18#useinsertioneffect "Link for useInsertionEffect")

`useInsertionEffect` 是一个新的 Hook ，允许 CSS-in-JS 库解决在渲染中注入样式的性能问题。除非你已经建立了一个 CSS-in-JS 库，否则我们不希望你使用它。这个 hook 将在 DOM 变更发生后，在 layout effect 获取新布局之前运行。这个功能不仅解决了一个在 React 17 及以下版本中已经存在的问题，而且在 React 18 中更加重要，因为 React 在并发渲染时会为浏览器让步，给它一个重新计算布局的机会。[参阅文档](https://react.docschina.org/reference/react/useInsertionEffect)。

> Note
> `useInsertionEffect` 旨在供库使用，而不是应用程序代码。

[在 React 中，hydrate 是指在服务端渲染时，去复用原本已经存在的 DOM 节点，减少重新生成节点以及删除原本 DOM 节点的开销，来加速初次渲染的功能。主要使用场景是服务端渲染或者像 prerender 等情况。](https://react.jokcy.me/book/features/hydrate.html)
[1](https://react.jokcy.me/book/features/hydrate.html)[: https://react.jokcy.me/book/features/hydrate.html](https://www.zhihu.com/question/66068748) 


# React 16
- `setState` callback (second argument) now fires immediately after `componentDidMount` / `componentDidUpdate` instead of after all components have rendered.  
    `setState` 回调（第二个参数）现在在 `componentDidMount` / `componentDidUpdate` 之后立即触发，而不是在所有组件呈现之后触发。
- Calling `setState` directly in render always causes an update. This was not previously the case. Regardless, you should not be calling `setState` from render.  
    在渲染中直接调用 `setState` 总是会导致更新。以前的情况并非如此。无论如何，您不应该从渲染中调用 `setState` 。

###  React v16.3.0: New lifecycles and context API
Version 16.3 introduces a new context API that is more efficient and supports both static type checking and deep updates.  
版本 16.3 引入了新的上下文 API，该 API 更加高效，并且支持静态类型检查和深度更新。

Here is an example illustrating how you might inject a “theme” using the new context API:  
下面的示例说明了如何使用新的上下文 API 注入“主题”：

```jsx
// 创建一个名为ThemeContext的上下文对象，初始值为'light'
const ThemeContext = React.createContext('light');

// ThemeProvider组件，用于提供主题信息
class ThemeProvider extends React.Component {
  state = { theme: 'light' }; // 组件的状态，初始值为'light'

  render() {
    return (
      // 使用ThemeContext.Provider包裹子组件，并将当前的主题信息作为value传递
      <ThemeContext.Provider value={this.state.theme}>
        {this.props.children}
      </ThemeContext.Provider>
    );
  }
}

// ThemedButton组件，根据当前主题展示不同样式的按钮
class ThemedButton extends React.Component {
  render() {
    return (
      // 使用ThemeContext.Consumer订阅主题信息，并将主题信息作为参数传递给回调函数
      <ThemeContext.Consumer>
        {theme => <Button theme={theme} />}
      </ThemeContext.Consumer>
    );
  }
}

```
以上注释对代码块中的功能进行了解释，其中包括创建了一个主题上下文对象`ThemeContext`，以及使用`ThemeProvider`组件提供主题信息，`ThemedButton`组件根据主题信息展示不同样式的按钮。
[Learn more about the new context API here.  
在此处了解有关新上下文 API 的更多信息。](https://legacy.reactjs.org/docs/context.html)
Provider和Consumer是React的Context API中的两个关键组件，用于在组件树中传递和访问共享的数据。
- Provider: Provider是一个高阶组件，用于提供共享的数据给其后代组件。它通过`value`属性将数据传递给后代组件。Provider组件应该被放置在组件树的顶层，以便其后代组件能够访问到共享的数据。
```jsx
<ThemeContext.Provider value={theme}>
  {children}
</ThemeContext.Provider>
```
- Consumer: Consumer是一个用于订阅共享数据的组件。它通过<font color="#00b050">一个函数作为子组件</font>（也称为"render prop"）的方式，接收来自Provider的数据，并在组件内部进行处理和渲染。Consumer组件可以在组件树的任何地方使用，它会自动找到最近的Provider并获取共享数据。
```jsx
<ThemeContext.Consumer>
  {theme => <Button theme={theme} />}
</ThemeContext.Consumer>
```
Provider和Consumer配合使用，可以实现数据在组件树中的上下文传递。Provider负责提供数据，而Consumer负责订阅数据并在组件内部使用。
示例中的代码展示了一个简单的主题切换功能。ThemeProvider组件作为Provider，提供了当前的主题信息给它的后代组件。ThemedButton组件作为Consumer，订阅了主题信息并在组件内部根据主题展示不同样式的按钮。
这种使用方式可以避免在组件之间通过props逐层传递数据，而是通过Provider和Consumer实现数据的共享和订阅。

Version 16.3 adds a new option for managing refs that offers the convenience of a string ref without any of the downsides:  
版本 16.3 添加了一个用于管理引用的新选项，它提供了字符串引用的便利性，但没有任何缺点：

这段代码定义了一个名为`MyComponent`的类组件。它创建了一个`inputRef`引用，用于引用`<input>`元素。
在`render`方法中，`<input>`元素被渲染，并将`this.inputRef`赋值给`ref`属性，以便在其他生命周期方法中可以访问到该`<input>`元素。
在`componentDidMount`生命周期方法中，`this.inputRef.current.focus()`被调用，使得组件挂载后自动将焦点设置在输入框上。
以下是代码的解释：
```jsx
class MyComponent extends React.Component {
  constructor(props) {
    super(props);
    this.inputRef = React.createRef(); // 创建一个引用对象，初始化为null
  }
  render() {
    return <input type="text" ref={this.inputRef} />; // 将引用对象赋值给input元素的ref属性
  }
  componentDidMount() {
    this.inputRef.current.focus(); // 在组件挂载后，将焦点设置在input元素上
  }
}
```
这段代码展示了在React中使用`ref`的常见模式。通过使用`ref`，我们可以在类组件中获取DOM元素的引用，并在需要时操作DOM元素或访问其属性和方法。
希望这个解释对你有所帮助！如果还有其他问题，请随时提问。

You don’t need to replace callback refs in your components. They are slightly more flexible, so they will remain as an advanced feature.  
您不需要替换组件中的回调引用。它们稍微灵活一些，因此它们将保留为高级功能。