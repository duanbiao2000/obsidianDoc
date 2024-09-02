---
aliases: []
date: 
url: 
page-title: 
tags:
  - flashcards
  - todo
modified date: 2023-09-29T20:55
---

# React Router v6
React Router v6相对v5有一些重要变化,可以用表格进行对比:
 
| 项目 | v5 | v6 |
|-|-|-|
| 路由器 | BrowserRouter/HashRouter | Router |
| Link组件 | `<Link>` | `<Link> `|  
| NavLink组件 | `<NavLink>` | `<NavLink>` |
| Route组件 | `<Route> `| `<Route>` |
| Switch组件 | `<Switch> `| 移除 |
| useHistory | history.push() | useNavigate() |
| useLocation | location对象 | useLocation() |
| useParams | match.params | useParams() |  
| useRouteMatch | match对象 | useRouteMatch() |
| Context | withRouter | useOutletContext() |
| Lazy Loading | React.lazy | React.lazy() |
| SSR | StaticRouter | StaticRouter |

主要变化:
- 统一Router组件
- 移除Switch组件 
- 引入Hook函数取代匹配对象
- Context相关功能升级
- Lazy Loading语法调整
- SSR支持保持不变
总体来说,v6的改动主要是为了更好支持Hook,简化API调用,但功能大体保持一致,两者可以平稳迁移。



# 常见面试提问
以下是一些经常会被问到的 React Router 相关问题：

1. React Router 是什么？它的作用是什么？
2. React Router 中的路由有哪些常用的组件？
3. 什么是动态路由？如何在 React Router 中创建动态路由？
4. 如何在 React Router 中进行编程式导航？
5. 什么是路由守卫？React Router 中如何实现路由守卫？
6. React Router 中的 NavLink 和 Link 有什么区别？
7. 如何在 React Router 中传递参数给路由组件？
8. React Router 中的 Switch 组件有什么作用？
9. 如何在 React Router 中处理 404 页面或路由未匹配情况？
10. React Router v5 和 v6 有什么重要的变化？



当回答前三个问题时，请注意我的回答如下：
1. React Router 是什么？它的作用是什么？
   - React Router 是一个用于在 React 应用程序中实现客户端路由的库。它允许开发者在单页面应用程序中定义不同的路由，以便根据不同的 URL 或路径显示不同的组件。<font color="#2DC26B">React Router 通过管理 URL 和组件之间的映射关系，实现了页面之间的无缝切换和导航</font>。
2. React Router 中的路由有哪些常用的组件？
   - React Router 中有几个常用的路由组件：
     - `<BrowserRouter>`：用于为应用程序提供基于 HTML5 history API 的路由功能。
     - `<Route>`：用于定义路由和相应的组件映射关系。
     - `<Switch>`：用于在多个路由中选择第一个匹配的路由。
     - `<Link>`：用于创建导航链接，允许用户点击链接进行路由导航。
     - `<NavLink>`：类似于 `<Link>`，但允许根据当前路由状态添加类名或样式。
     - `<Redirect>`：用于在路由匹配失败时进行重定向。
3. 什么是动态路由？如何在 React Router 中创建动态路由？
   - 动态路由是一种根据 URL 中的参数或特定的路径模式来动态匹配和渲染组件的路由。在 React Router 中，可以使用冒号 (`:`) 作为参数占位符来创建动态路由。
   
   以下是在 React Router 中创建动态路由的示例代码：
   ```jsx
   import { BrowserRouter, Route } from 'react-router-dom';
   function App() {
     return (
       <BrowserRouter>
         <Route path="/users/:id" component={UserDetails} />
       </BrowserRouter>
     );
   }
   function UserDetails({ match }) {
     const { id } = match.params;
     return (
       <div>
         User ID: {id}
       </div>
     );
   }
   ```
   在上面的示例中，通过在路由路径中使用 `:id` 的形式创建了一个动态路由。当用户访问类似于 "/users/123" 的 URL 时，`UserDetails` 组件将被渲染，并通过 `match.params` 属性获取到动态的 `id` 值，以便在组件中使用。
请注意，这只是一个简单的示例，演示了如何在 React Router 中创建和使用动态路由。实际应用中，你可以根据具体的需求和路由结构，创建更复杂的动态路由。


4. 如何在 React Router 中进行编程式导航？
   在 React Router 中，可以使用 `useHistory` 钩子函数来访问路由历史对象，并进行编程式导航。
   示例代码如下：
   ```jsx
   import { useHistory } from 'react-router-dom';
   function MyComponent() {
     const history = useHistory();
     const handleClick = () => {
       history.push('/new-route');
     };
     return (
       <button onClick={handleClick}>Go to New Route</button>
     );
   }
   ```
   在上面的示例中，通过调用 `useHistory` 钩子函数获取到路由历史对象 `history`，然后在处理函数 `handleClick` 中使用 `history.push('/new-route')` 进行编程式导航。当按钮被点击时，应用程序将跳转到路径为 "/new-route" 的新路由。
5. 什么是路由守卫？React Router 中如何实现路由守卫？
   路由守卫是一种在进入或离开路由时执行特定操作的机制。在 React Router 中，可以使用 `<Route>` 组件的 `render` 属性或 `useEffect` 钩子函数来实现路由守卫。
   示例代码如下：
   ```jsx
   import { Route, useHistory } from 'react-router-dom';
   function PrivateRoute({ component: Component, ...rest }) {
     const history = useHistory();
     const isAuthenticated = checkIfUserIsAuthenticated(); // 检查用户是否已认证
     return (
       <Route
         {...rest}
         render={(props) =>
           isAuthenticated ? (
             <Component {...props} />
           ) : (
             history.push('/login') // 未认证，重定向到登录页面
           )
         }
       />
     );
   }
   ```
   上面的示例代码是一个自定义的 `PrivateRoute` 组件，它用于保护需要认证的路由。该组件通过检查用户是否已认证，决定渲染原始组件或重定向到登录页面。
   在 `<Route>` 组件的 `render` 属性中，根据 `isAuthenticated` 的值，决定渲染 `<Component {...props} />` 或调用 `history.push('/login')` 进行路由重定向。
请注意，这只是一个简单的示例，演示了如何实现路由守卫。在实际应用中，你可以根据具体的需求和认证逻辑，创建更复杂的路由守卫机制。

6. React Router 中的 NavLink 和 Link 有什么区别？
   - `NavLink` 和 `Link` 都是用于创建导航链接的组件，它们之间的区别在于 `NavLink` 具有额外的功能来处理当前路由状态的样式和激活状态。
   - `Link` 组件是最基本的导航链接组件，它用于在点击时进行路由导航，但没有提供任何状态处理功能。
   - `NavLink` 组件除了具有 `Link` 的导航功能外，还可以根据当前路由状态添加类名或样式。它可以接收一个 `activeClassName` 属性，当链接与当前路由匹配时，会自动添加指定的类名。也可以使用 `activeStyle` 属性，为激活状态的链接添加样式对象。
   示例代码如下：
   ```jsx
   import { NavLink } from 'react-router-dom';
   function Navigation() {
     return (
       <nav>
         <NavLink to="/" activeClassName="active">Home</NavLink>
         <NavLink to="/about" activeClassName="active">About</NavLink>
         <NavLink to="/contact" activeClassName="active">Contact</NavLink>
       </nav>
     );
   }
   ```
   在上面的示例中，使用了 `NavLink` 组件创建了几个导航链接。当某个链接与当前路由匹配时，会自动添加 `active` 类名，从而可以为当前链接应用特定的样式。
7. 如何在 React Router 中传递参数给路由组件？
   - 在 React Router 中，可以通过 `:param` 形式在路由路径中定义参数占位符，并在路由组件中通过 `useParams` 钩子函数或通过 `props.match.params` 获取传递的参数。
   示例代码如下：
   ```jsx
   import { BrowserRouter, Route, useParams } from 'react-router-dom';
   function App() {
     return (
       <BrowserRouter>
         <Route path="/users/:id" component={UserDetails} />
       </BrowserRouter>
     );
   }
   function UserDetails() {
     const { id } = useParams();
     return (
       <div>
         User ID: {id}
       </div>
     );
   }
   ```
   在上面的示例中，通过在路由路径中使用 `:id` 的形式创建了一个参数占位符。当用户访问类似于 "/users/123" 的 URL 时，`UserDetails` 组件将被渲染，并通过 `useParams` 钩子函数获取到传递的 `id` 参数。在组件中，可以使用 `id` 参数展示特定用户的详细信息。
请注意，这只是一个简单的示例，演示了如何在 React Router 中传递参数给路由组件。在实际应用中，你可以根据具体的需求和路由结构，传递不同类型的参数或多个参数给路由组件。

当回答最后三个问题时，请注意我的回答如下：
8. React Router 中的 Switch 组件有什么作用？
   - `Switch` 组件是用于在多个路由中选择第一个匹配的路由。它将遍历子 `Route` 组件，并在找到第一个匹配的路由后停止匹配。
   示例代码如下：
   ```jsx
   import { BrowserRouter, Route, Switch } from 'react-router-dom';
   function App() {
     return (
       <BrowserRouter>
         <Switch>
           <Route exact path="/" component={Home} />
           <Route path="/about" component={About} />
           <Route path="/contact" component={Contact} />
           <Route component={NotFound} />
         </Switch>
       </BrowserRouter>
     );
   }
   ```
   在上面的示例中，`Switch` 组件将遍历其子组件，并根据路由路径选择第一个匹配的路由。如果没有匹配的路由，可以使用 `Route` 组件的 `component` 属性指定一个默认的 `NotFound` 组件，用于处理 404 页面或路由未匹配的情况。
9. 如何在 React Router 中处理 404 页面或路由未匹配情况？
   - 在 React Router 中，可以使用一个不带 `path` 属性的 `<Route>` 组件，作为默认的路由组件，来处理 404 页面或路由未匹配的情况。
   示例代码如下：
   ```jsx
   import { BrowserRouter, Route, Switch } from 'react-router-dom';
   function App() {
     return (
       <BrowserRouter>
         <Switch>
           <Route exact path="/" component={Home} />
           <Route path="/about" component={About} />
           <Route path="/contact" component={Contact} />
           <Route component={NotFound} />
         </Switch>
       </BrowserRouter>
     );
   }
   ```
   在上面的示例中，如果用户访问的路径不匹配任何已定义的路由，`Switch` 组件将匹配到没有 `path` 属性的最后一个 `<Route>` 组件，并渲染 `NotFound` 组件。这样可以处理 404 页面或路由未匹配的情况。
10. React Router v5 和 v6 有什么重要的变化？
   - React Router v6 是 React Router 的下一个主要版本，与 v5 相比有一些重要的变化：
     - 在 v6 中，用于路由配置的组件从 `<Route>` 改为 `<Routes>`，用于导航链接的组件从 `<Link>` 改为 `<Link to>`。
     - v6 中引入了新的 `<Outlet>` 组件，用于在父级路由组件中渲染子路由组件。
     - 在 v6 中，不再使用 `exact` 属性来确保精确匹配，而是使用 `*` 作为通配符匹配。
     - v6 中的嵌套路由定义方式发生了变化，使用嵌套的 `<Route>` 组件来定义子路由。
     - v6 中取消了 `withRouter` 高阶组件的使用，改为使用 `useLocation`、`useParams` 等钩子函数来获取路由信息。
   请注意，React Router v6 目前还处于 beta 版本，与 v5 在 API 和用法上存在较大差异。在开发应用程序时，根据所使用的版本来选择相应的文档和示例代码。






## Client Side Routing 客户端路由

React Router enables "client side routing".  
React Router 启用“客户端路由”。

In traditional websites, the browser requests a document from a web server, downloads and evaluates CSS and JavaScript assets, and renders the HTML sent from the server. When the user clicks a link, it starts the process all over again for a new page.  
在传统网站中，浏览器从 Web 服务器请求文档，下载并评估 CSS 和 JavaScript 资源，并呈现从服务器发送的 HTML。当用户单击链接时，它会在新页面上重新启动该过程。

Client side routing allows your app to update the URL from a link click without making another request for another document from the server. Instead, your app can immediately render some new UI and make data requests with `fetch` to update the page with new information.  
客户端路由允许您的应用程序通过链接点击更新 URL，而无需从服务器再次请求另一个文档。相反，您的应用可以立即呈现一些新的 UI 并使用 `fetch` 发出数据请求，以使用新信息更新页面。

```jsx
import * as React from "react";
import { createRoot } from "react-dom/client";
import {
  createBrowserRouter,
  RouterProvider,
  Route,
  Link,
} from "react-router-dom";

const router = createBrowserRouter([
  {
    path: "/",
    element: (
      <div>
        <h1>Hello World</h1>
        <Link to="about">About Us</Link>
      </div>
    ),
  },
  {
    path: "about",
    element: <div>About</div>,
  },
]);

createRoot(document.getElementById("root")).render(
  <RouterProvider router={router} />
);
```

##   Nested Routes 嵌套路由

Nested Routing is the general idea of coupling segments of the URL to component hierarchy and data. React Router's nested routes were inspired by the routing system in Ember.js circa 2014. The Ember team realized that in nearly every case, segments of the URL determine:  
嵌套路由是将 URL 段耦合到组件层次结构和数据的总体思想。 React Router 的嵌套路由受到 2014 年左右 Ember.js 中路由系统的启发。Ember 团队意识到，几乎在所有情况下，URL 的各个部分都决定：

- The layouts to render on the page  
    要在页面上呈现的布局
- The data dependencies of those layouts  
    这些布局的数据依赖性

React Router embraces this convention with APIs for creating nested layouts coupled to URL segments and data.  
React Router 通过 API 拥抱这一约定，用于创建与 URL 段和数据耦合的嵌套布局。

```jsx
// Configure nested routes with JSX
createBrowserRouter(
  createRoutesFromElements(
    <Route path="/" element={<Root />}>
      <Route path="contact" element={<Contact />} />
      <Route
        path="dashboard"
        element={<Dashboard />}
        loader={({ request }) =>
          fetch("/api/dashboard.json", {
            signal: request.signal,
          })
        }
      />
      <Route element={<AuthLayout />}>
        <Route
          path="login"
          element={<Login />}
          loader={redirectIfUser}
        />
        <Route path="logout" action={logoutUser} />
      </Route>
    </Route>
  )
);

// Or use plain objects
createBrowserRouter([
  {
    path: "/",
    element: <Root />,
    children: [
      {
        path: "contact",
        element: <Contact />,
      },
      {
        path: "dashboard",
        element: <Dashboard />,
        loader: ({ request }) =>
          fetch("/api/dashboard.json", {
            signal: request.signal,
          }),
      },
      {
        element: <AuthLayout />,
        children: [
          {
            path: "login",
            element: <Login />,
            loader: redirectIfUser,
          },
          {
            path: "logout",
            action: logoutUser,
          },
        ],
      },
    ],
  },
]);
```

This [visualization](https://remix.run/_docs/routing) might be helpful.  
这种可视化可能会有所帮助。

## Dynamic Segments 动态片段

Segments of the URL can be dynamic placeholders that are parsed and provided to various apis.  
URL 的片段可以是动态占位符，它们被解析并提供给各种 api。

```
<Route path="projects/:projectId/tasks/:taskId" />
```

The two segments with `:` are dynamic, and provided to the following APIs:  
带有 `:` 的两个段是动态的，并提供给以下 API：

```jsx
// If the current location is /projects/abc/tasks/3
<Route
  // sent to loaders
  loader={({ params }) => {
    params.projectId; // abc
    params.taskId; // 3
  }}
  // and actions
  action={({ params }) => {
    params.projectId; // abc
    params.taskId; // 3
  }}
  element={<Task />}
/>;

function Task() {
  // returned from `useParams`
  const params = useParams();
  params.projectId; // abc
  params.taskId; // 3
}

function Random() {
  const match = useMatch(
    "/projects/:projectId/tasks/:taskId"
  );
  match.params.projectId; // abc
  match.params.taskId; // 3
}
```

##   Ranked Route Matching 排名路线匹配

When matching URLs to routes, React Router will rank the routes according to the number of segments, static segments, dynamic segments, splats, etc. and pick the _most specific_ match.  
当将 URL 与路由匹配时，React Router 会根据段数、静态段、动态段、splats 等对路由进行排名，并选择最具体的匹配。

For example, consider these two routes:  
例如，考虑以下两条路线：

```jsx
<Route path="/teams/:teamId" />
<Route path="/teams/new" />
```

Now consider the URL is [http://example.com/teams/new](http://example.com/teams/new).  
现在考虑 URL 是 http://example.com/teams/new。

Even though both routes technically match the URL (`new` could be the `:teamId`), you intuitively know that we want the second route (`/teams/new`) to be picked. React Router's matching algorithm knows that, too.  
尽管两条路由在技术上都与 URL 匹配（ `new` 可能是 `:teamId` ），但您直观地知道我们希望选择第二条路由（ `/teams/new` ）。 React Router 的匹配算法也知道这一点。

With ranked routes, you don't have to worry about route ordering.  
有了排名路线，您就不必担心路线排序问题。

## Active Links 活跃链接

Most web apps have persistent navigation sections at the top of the UI, the sidebar, and often multiple levels. Styling the active navigation items so the user knows where they are (`isActive`) or where they're going (`isPending`) in the app is done easily with `<NavLink>`.  
大多数网络应用程序在 UI 顶部、侧边栏以及通常多个级别都有固定的导航部分。使用 `<NavLink>` 可以轻松设置活动导航项的样式，以便用户知道它们在应用程序中的位置 ( `isActive` ) 或要去往的位置 ( `isPending` ) 。

```jsx
<NavLink
  style={({ isActive, isPending }) => {
    return {
      color: isActive ? "red" : "inherit",
    };
  }}
  className={({ isActive, isPending }) => {
    return isActive ? "active" : isPending ? "pending" : "";
  }}
/>
```

You can also [`useMatch`](https://reactrouter.com/en/main/hooks/use-match) for any other "active" indication outside of links.  
您还可以 `useMatch` 获取链接之外的任何其他“活动”指示。

```
function SomeComp() {
  const match = useMatch("/messages");
  return <li className={Boolean(match) ? "active" : ""} />;
}
```

See: 看：

- [`NavLink`](https://reactrouter.com/en/main/components/nav-link)
- [`useMatch`](https://reactrouter.com/en/main/hooks/use-match)

## Relative Links 相对链接

Like HTML `<a href>`, `<Link to>` and `<NavLink to>` can take relative paths, with enhanced behavior with nested routes.  
与 HTML `<a href>` 一样， `<Link to>` 和 `<NavLink to>` 可以采用相对路径，并通过嵌套路由增强行为。

Given the following route config:  
给出以下路由配置：

```
<Route path="home" element={<Home />}>
  <Route path="project/:projectId" element={<Project />}>
    <Route path=":taskId" element={<Task />} />
  </Route>
</Route>
```

Consider the url [https://example.com/home/project/123](https://example.com/home/project/123), which renders the following route component hierarchy:  

```
<Home>
  <Project />
</Home>
```

If `<Project />` renders the following links, the hrefs of the links will resolve like so:  


|In `<Project>` @ `/home/project/123` |Resolved `<a href>` |
|---|---|
|`<Link to="abc">`|`/home/project/123/abc`|
|`<Link to=".">`|`/home/project/123`|
|`<Link to="..">`|`/home`|
|`<Link to=".." relative="path">`|`/home/project`|

Note that the first `..` removes both segments of the `project/:projectId` route. By default, the `..` in relative links traverse the route hierarchy, not the URL segments. Adding `relative="path"` in the next example allows you to traverse the path segments instead.  


Relative links are always relative to the route path they are _rendered in_, not to the full URL. That means if the user navigates deeper with `<Link to="abc">` to `<Task />` at the URL `/home/project/123/abc`, the hrefs in `<Project>` will not change (contrary to plain `<a href>`, a common problem with client side routers).  
相对链接始终相对于它们呈现的路由路径，而不是相对于完整的 URL。这意味着，如果用户在 URL `/home/project/123/abc` 处使用 `<Link to="abc">` 更深地导航到 `<Task />` ，则 `<Project>` 中的 href 不会更改（与普通 `<a href>` ，客户端路由器的常见问题）。

## Data Loading 数据加载

Because URL segments usually map to your app's persistent data, React Router provides conventional data loading hooks to initiate data loading during a navigation. Combined with nested routes, all of the data for multiple layouts at a specific URL can be loaded in parallel.  
由于 URL 段通常映射到应用程序的持久数据，因此 React Router 提供了传统的数据加载挂钩来在导航期间启动数据加载。与嵌套路由相结合，可以并行加载特定 URL 处的多个布局的所有数据。

```
<Route
  path="/"
  loader={async ({ request }) => {
    // loaders can be async functions
    const res = await fetch("/api/user.json", {
      signal: request.signal,
    });
    const user = await res.json();
    return user;
  }}
  element={<Root />}
>
  <Route
    path=":teamId"
    // loaders understand Fetch Responses and will automatically
    // unwrap the res.json(), so you can simply return a fetch
    loader={({ params }) => {
      return fetch(`/api/teams/${params.teamId}`);
    }}
    element={<Team />}
  >
    <Route
      path=":gameId"
      loader={({ params }) => {
        // of course you can use any data store
        return fakeSdk.getTeam(params.gameId);
      }}
      element={<Game />}
    />
  </Route>
</Route>
```

Data is made available to your components through `useLoaderData`.  
您的组件可以通过 `useLoaderData` 获取数据。

```
function Root() {
  const user = useLoaderData();
  // data from <Route path="/">
}

function Team() {
  const team = useLoaderData();
  // data from <Route path=":teamId">
}

function Game() {
  const game = useLoaderData();
  // data from <Route path=":gameId">
}
```

When the user visits or clicks links to [https://example.com/real-salt-lake/45face3](https://example.com/real-salt-lake/45face3), all three route loaders will be called and loaded in parallel, before the UI for that URL renders.  
当用户访问或单击指向 https://example.com/real-salt-lake/45face3 的链接时，将在呈现该 URL 的 UI 之前并行调用并加载所有三个路由加载器。

##  重定向

While loading or changing data, it's common to [redirect](https://reactrouter.com/en/main/fetch/redirect) the user to a different route.  
加载或更改数据时，通常会将用户重定向到不同的路线。

```
<Route
  path="dashboard"
  loader={async () => {
    const user = await fake.getUser();
    if (!user) {
      // if you know you can't render the route, you can
      // throw a redirect to stop executing code here,
      // sending the user to a new route
      throw redirect("/login");
    }

    // otherwise continue
    const stats = await fake.getDashboardStats();
    return { user, stats };
  }}
/>
```

```
<Route
  path="project/new"
  action={async ({ request }) => {
    const data = await request.formData();
    const newProject = await createProject(data);
    // it's common to redirect after actions complete,
    // sending the user to the new record
    return redirect(`/projects/${newProject.id}`);
  }}
/>
```

See: 看：

- [`redirect`](https://reactrouter.com/en/main/fetch/redirect)
- [Throwing in Loaders 扔进装载机](https://reactrouter.com/en/main/route/loader#throwing-in-loaders)
- [`useNavigate`](https://reactrouter.com/en/main/hooks/use-navigate)

## Pending Navigation UI 待定导航用户界面

When users navigate around the app, the data for the next page is loaded before the page is rendered. It's important to provide user feedback during this time so the app doesn't feel like it's unresponsive.  
当用户在应用程序中导航时，下一页的数据会在页面呈现之前加载。在此期间提供用户反馈非常重要，这样应用程序就不会感觉没有响应。

```
function Root() {
  const navigation = useNavigation();
  return (
    <div>
      {navigation.state === "loading" && <GlobalSpinner />}
      <FakeSidebar />
      <Outlet />
      <FakeFooter />
    </div>
  );
}
```

See: 看：

- [`useNavigation`](https://reactrouter.com/en/main/hooks/use-navigation)

## [](https://reactrouter.com/en/main/start/overview#skeleton-ui-with-suspense)Skeleton UI with `<Suspense>`  
带有 `<Suspense>` 的骨架 UI

Instead of waiting for the data for the next page, you can [`defer`](https://reactrouter.com/en/main/utils/defer) data so the UI flips over to the next screen with placeholder UI immediately while the data loads.  
您可以 `defer` 数据，而不是等待下一页的数据，以便在数据加载时 UI 立即翻转到带有占位符 UI 的下一个屏幕。

```
<Route
  path="issue/:issueId"
  element={<Issue />}
  loader={async ({ params }) => {
    // these are promises, but *not* awaited
    const comments = fake.getIssueComments(params.issueId);
    const history = fake.getIssueHistory(params.issueId);
    // the issue, however, *is* awaited
    const issue = await fake.getIssue(params.issueId);

    // defer enables suspense for the un-awaited promises
    return defer({ issue, comments, history });
  }}
/>;

function Issue() {
  const { issue, history, comments } = useLoaderData();
  return (
    <div>
      <IssueDescription issue={issue} />

      {/* Suspense provides the placeholder fallback */}
      <Suspense fallback={<IssueHistorySkeleton />}>
        {/* Await manages the deferred data (promise) */}
        <Await resolve={history}>
          {/* this calls back when the data is resolved */}
          {(resolvedHistory) => (
            <IssueHistory history={resolvedHistory} />
          )}
        </Await>
      </Suspense>

      <Suspense fallback={<IssueCommentsSkeleton />}>
        <Await resolve={comments}>
          {/* ... or you can use hooks to access the data */}
          <IssueComments />
        </Await>
      </Suspense>
    </div>
  );
}

function IssueComments() {
  const comments = useAsyncValue();
  return <div>{/* ... */}</div>;
}
```

See

- [Deferred Data Guide 延期数据指南](https://reactrouter.com/en/main/guides/deferred)
- [`defer`](https://reactrouter.com/en/main/utils/defer)
- [`Await`](https://reactrouter.com/en/main/components/await)
- [`useAsyncValue`](https://reactrouter.com/en/main/hooks/use-async-value)

## [](https://reactrouter.com/en/main/start/overview#data-mutations)Data Mutations 数据突变

HTML forms are navigation events, just like links. React Router supports HTML form workflows with client side routing.  
HTML 表单是导航事件，就像链接一样。 React Router 支持带有客户端路由的 HTML 表单工作流。

When a form is submitted, the normal browser navigation event is prevented and a [`Request`](https://developer.mozilla.org/en-US/docs/Web/API/Request), with a body containing the [`FormData`](https://developer.mozilla.org/en-US/docs/Web/API/FormData) of the submission, is created. This request is sent to the `<Route action>` that matches the form's `<Form action>`.  
提交表单时，会阻止正常的浏览器导航事件，并创建一个 `Request` ，其正文包含提交的 `FormData` 。该请求被发送到与表单的 `<Form action>` 匹配的 `<Route action>` 。

Form elements's `name` prop are submitted to the action:  
表单元素的 `name` 属性被提交给操作：

```
<Form action="/project/new">
  <label>
    Project title
    <br />
    <input type="text" name="title" />
  </label>

  <label>
    Target Finish Date
    <br />
    <input type="date" name="due" />
  </label>
</Form>
```

The normal HTML document request is prevented and sent to the matching route's action (`<Route path>` that matches the `<form action>`), including the `request.formData`.  
正常的 HTML 文档请求被阻止并发送到匹配路由的操作（与 `<form action>` 匹配的 `<Route path>` ），包括 `request.formData` 。

```
<Route
  path="project/new"
  action={async ({ request }) => {
    const formData = await request.formData();
    const newProject = await createProject({
      title: formData.get("title"),
      due: formData.get("due"),
    });
    return redirect(`/projects/${newProject.id}`);
  }}
/>
```

## [](https://reactrouter.com/en/main/start/overview#data-revalidation)Data Revalidation 数据重新验证

Decades old web conventions indicate that when a form is posted to the server, data is changing and a new page is rendered. That convention is followed in React Router's HTML-based data mutation APIs.  
几十年前的 Web 约定表明，当将表单发布到服务器时，数据会发生变化并呈现新页面。 React Router 的基于 HTML 的数据突变 API 遵循该约定。

After route actions are called, the loaders for all of the data on the page is called again to ensure the UI stays up-to-date with the data automatically. No cache keys to expire, no context providers to reload.  
调用路由操作后，将再次调用页面上所有数据的加载器，以确保 UI 自动保持最新数据。没有缓存密钥会过期，没有上下文提供程序要重新加载。

See: 看：

- [Tutorial "Creating Contacts"  
    教程“创建联系人”](https://reactrouter.com/en/main/start/tutorial#creating-contacts)

## [](https://reactrouter.com/en/main/start/overview#busy-indicators)Busy Indicators  忙碌指示器

When forms are being submitted to route actions, you have access to the navigation state to display busy indicators, disable fieldsets, etc.  
当表单提交给路由操作时，您可以访问导航状态以显示繁忙指示器、禁用字段集等。

```jsx
function NewProjectForm() {
  const navigation = useNavigation();
  const busy = navigation.state === "submitting";
  return (
    <Form action="/project/new">
      <fieldset disabled={busy}>
        <label>
          Project title
          <br />
          <input type="text" name="title" />
        </label>

        <label>
          Target Finish Date
          <br />
          <input type="date" name="due" />
        </label>
      </fieldset>
      <button type="submit" disabled={busy}>
        {busy ? "Creating..." : "Create"}
      </button>
    </Form>
  );
}
```

See: 看：

- [`useNavigation`](https://reactrouter.com/en/main/hooks/use-navigation)

## [](https://reactrouter.com/en/main/start/overview#optimistic-ui)Optimistic UI 乐观的用户界面

Knowing the [`formData`](https://developer.mozilla.org/en-US/docs/Web/API/FormData) being sent to an [action](https://reactrouter.com/en/main/route/action) is often enough to skip the busy indicators and render the UI in the next state immediately, even if your asynchronous work is still pending. This is called "optimistic UI".  
了解发送到某个操作的 `formData` 通常足以跳过忙碌指示器并立即将 UI 呈现在下一个状态，即使您的异步工作仍处于挂起状态。这称为“乐观 UI”。

```jsx
function LikeButton({ tweet }) {
  const fetcher = useFetcher();

  // if there is `formData` then it is posting to the action
  const liked = fetcher.formData
    ? // check the formData to be optimistic
      fetcher.formData.get("liked") === "yes"
    : // if its not posting to the action, use the record's value
      tweet.liked;

  return (
    <fetcher.Form method="post" action="toggle-liked">
      <button
        type="submit"
        name="liked"
        value={liked ? "yes" : "no"}
      />
    </fetcher.Form>
  );
}
```

(Yes, HTML buttons can have a `name` and a `value`).  
（是的，HTML 按钮可以有 `name` 和 `value` ）。

While it is more common to do optimistic UI with a [`fetcher`](https://reactrouter.com/en/main/hooks/use-fetcher), you can do the same with a normal form using [`navigation.formData`](https://reactrouter.com/en/main/hooks/use-navigation#navigationformdata).  
虽然使用 `fetcher` 实现乐观 UI 更为常见，但您可以使用 `navigation.formData` 对普通表单执行相同的操作。

## [](https://reactrouter.com/en/main/start/overview#data-fetchers)Data Fetchers 数据获取器

HTML Forms are the model for mutations but they have one major limitation: you can have only one at a time because <font color="#2DC26B">a form submission is a navigation</font>.  
HTML 表单是突变模型，但它们有一个主要限制：一次只能有一个表单，因为表单提交是一种导航。

Most web apps need to allow for multiple mutations to be happening at the same time, like a list of records where each can be independently deleted, marked complete, liked, etc.  
大多数网络应用程序需要允许同时发生多个突变，例如一个记录列表，其中每个记录都可以独立删除、标记为完整、喜欢等。

[Fetchers](https://reactrouter.com/en/main/hooks/use-fetcher) allow you to interact with the route [actions](https://reactrouter.com/en/main/route/action) and [loaders](https://reactrouter.com/en/main/route/loader) without causing a navigation in the browser, but still getting all the conventional benefits like error handling, revalidation, interruption handling, and race condition handling.  
Fetchers 允许您与路由操作和加载器进行交互，而不会在浏览器中引起导航，但仍然可以获得所有传统的好处，例如错误处理、重新验证、中断处理和竞争条件处理。

Imagine a list of tasks:  
想象一下任务列表：

```jsx
function Tasks() {
  const tasks = useLoaderData();
  return tasks.map((task) => (
    <div>
      <p>{task.name}</p>
      <ToggleCompleteButton task={task} />
    </div>
  ));
}
```

Each task can be marked complete independently of the rest, with its own pending state and without causing a navigation with a [fetcher](https://reactrouter.com/en/main/hooks/use-fetcher):  
每个任务都可以独立于其余任务标记为完成，具有自己的挂起状态，并且不会导致使用获取器进行导航：

```jsx
function ToggleCompleteButton({ task }) {
  const fetcher = useFetcher();

  return (
    <fetcher.Form method="post" action="/toggle-complete">
      <fieldset disabled={fetcher.state !== "idle"}>
        <input type="hidden" name="id" value={task.id} />
        <input
          type="hidden"
          name="status"
          value={task.complete ? "incomplete" : "complete"}
        />
        <button type="submit">
          {task.status === "complete"
            ? "Mark Incomplete"
            : "Mark Complete"}
        </button>
      </fieldset>
    </fetcher.Form>
  );
}
```

See: 看：

- [`useFetcher`](https://reactrouter.com/en/main/hooks/use-fetcher)

## [](https://reactrouter.com/en/main/start/overview#race-condition-handling)Race Condition Handling 竞态条件处理

React Router will cancel stale operations and only commit fresh data automatically.  
React Router 将取消过时的操作并仅自动提交新数据。

Any time you have asynchronous UI you have the risk of race conditions: when an async operation starts after but completes before an earlier operation. The result is a user interface that shows the wrong state.  
任何时候你有异步 UI 时，你都会面临竞争条件的风险：当异步操作在较早的操作之后开始但在较早的操作之前完成时。结果是用户界面显示错误的状态。

Consider a search field that updates a list as the user types:  
考虑一个在用户键入时更新列表的搜索字段：

```
?q=ry    |---------------|
                         ^ commit wrong state
?q=ryan     |--------|
                     ^ lose correct state
```

Even though the query for `q?=ryan` went out later, it completed earlier. If not handled correctly, the results will briefly be the correct values for `?q=ryan` but then flip over the incorrect results for `?q=ry`. Throttling and debouncing are not enough (you can still interrupt the requests that get through). You need cancellation.  
尽管 `q?=ryan` 的查询稍后发出，但它更早完成。如果处理不当，结果将暂时是 `?q=ryan` 的正确值，但随后会翻转 `?q=ry` 的错误结果。限制和去抖动是不够的（您仍然可以中断通过的请求）。您需要取消。

If you're using React Router's data conventions you avoid this problem completely and automatically.  
如果您使用 React Router 的数据约定，您可以完全自动地避免这个问题。

```
?q=ry    |-----------X
                     ^ cancel wrong state when
                       correct state completes earlier
?q=ryan     |--------|
                     ^ commit correct state
```

Not only does React Router handle race conditions for a navigation like this, it also handles it for many other cases like loading results for an autocomplete or performing multiple concurrent mutations with [`fetcher`](https://reactrouter.com/en/main/hooks/use-fetcher) (and its automatic, concurrent revalidations).  
React Router 不仅处理像这样的导航的竞争条件，它还处理许多其他情况，例如加载自动完成的结果或使用 `fetcher` 执行多个并发突变（及其自动并发重新验证）。

## [](https://reactrouter.com/en/main/start/overview#error-handling)Error Handling 错误处理

The vast majority of your application errors are handled automatically by React Router. It will catch any errors that are thrown while:  
绝大多数应用程序错误都是由 React Router 自动处理的。它将捕获在以下情况下引发的任何错误：

- rendering 渲染
- loading data 加载数据中
- updating data 更新数据

In practice, this is pretty much every error in your app except those thrown in event handlers (`<button onClick>`) or `useEffect`. React Router apps tend to have very few of either.  
实际上，这几乎是应用程序中的所有错误，除了事件处理程序 ( `<button onClick>` ) 或 `useEffect` 中引发的错误。 React Router 应用程序往往两者都很少。

When an error is thrown, instead of rendering the route's [`element`](https://reactrouter.com/en/main/route/route#element), the [`errorElement`](https://reactrouter.com/en/main/route/error-element) is rendered.  
当抛出错误时，不会渲染路由的 `element` ，而是渲染 `errorElement` 。

```
<Route
  path="/"
  loader={() => {
    something.that.throws.an.error();
  }}
  // this will not be rendered
  element={<HappyPath />}
  // but this will instead
  errorElement={<ErrorBoundary />}
/>
```

If a route doesn't have an `errorElement`, the error will <font color="#2DC26B">bubble</font> to the nearest parent route with an `errorElement`:  
如果路由没有 `errorElement` ，错误将冒泡到最近的带有 `errorElement` 的父路由：

```jsx
<Route
  path="/"
  element={<HappyPath />}
  errorElement={<ErrorBoundary />}
>
  {/* Errors here bubble up to the parent route */}
  <Route path="login" element={<Login />} />
</Route>
```

See: 看：

- [`<Route errorElement>`](https://reactrouter.com/en/main/route/error-element)
- [`useRouteError`](https://reactrouter.com/en/main/hooks/use-route-error)

## [](https://reactrouter.com/en/main/start/overview#scroll-restoration)Scroll Restoration 卷轴复原

React Router will emulate the browser's scroll restoration on navigation, waiting for data to load before scrolling. This ensures the scroll position is restored to the right spot.  
React Router 将在导航时模拟浏览器的滚动恢复，在滚动之前等待数据加载。这可确保滚动位置恢复到正确的位置。

You can also customize the behavior by restoring based on something other than locations (like a url pathname) and preventing the scroll from happening on certain links (like tabs in the middle of a page).  
您还可以通过基于位置以外的内容（例如 url 路径名）进行恢复来自定义行为，并防止滚动发生在某些链接（例如页面中间的选项卡）上。

See: 看：

- [`<ScrollRestoration>`](https://reactrouter.com/en/main/components/scroll-restoration)

## [](https://reactrouter.com/en/main/start/overview#web-standard-apis)Web Standard APIs

React Router is built on web standard APIs. [Loaders](https://reactrouter.com/en/main/route/loader) and [actions](https://reactrouter.com/en/main/route/action) receive standard Web Fetch API [`Request`](https://developer.mozilla.org/en-US/docs/Web/API/Request) objects and can return [`Response`](https://developer.mozilla.org/en-US/docs/Web/API/Response) objects, too. Cancellation is done with [Abort Signals](https://developer.mozilla.org/en-US/docs/Web/API/AbortSignal), search params are handled with [`URLSearchParams`](https://developer.mozilla.org/en-US/docs/Web/API/URLSearchParams), and data mutations are handled with [HTML Forms](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/form).  
React Router 是基于 Web 标准 API 构建的。加载器和操作接收标准 Web Fetch API `Request` 对象，也可以返回 `Response` 对象。取消是通过中止信号完成的，搜索参数是通过 `URLSearchParams` 处理的，数据突变是通过 HTML 表单处理的。

When you get better at React Router, you get better at the web platform.  



# Tutorial

We'll be using [Vite](https://vitejs.dev/guide/) for our bundler and dev server for this tutorial. You'll need [Node.js](https://nodejs.org/) installed for the `npm` command line tool.

```sh
npm create vite@latest name-of-your-project -- --template react
# follow prompts
cd <your new project directory>
npm install react-router-dom localforage match-sorter sort-by
npm run dev
```


This tutorial will be creating, reading, searching, updating, and deleting data. A typical web app would probably be talking to an API on your web server, but we're going to use browser storage and fake some network latency to keep this focused.

在`main.jsx`中创建并渲染浏览器路由器.
```jsx
//main.jsx
import * as React from "react";
import * as ReactDOM from "react-dom/client";
import {
  createBrowserRouter,
  RouterProvider,
} from "react-router-dom";
import "./index.css";

const router = createBrowserRouter([
  {
    path: "/",
    element: <div>Hello world!</div>,
  },
]);

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>
);
```

以下是对给定代码进行格式化和详细注释的结果：
```jsx
import Root, {
  loader as rootLoader,
  action as rootAction,
} from "./routes/root";
const router = createBrowserRouter([
  {
    path: "/", // 路由路径
    element: <Root />, // 渲染的组件
    errorElement: <ErrorPage />, // 错误时渲染的组件
    loader: rootLoader, // 路由加载器
    action: rootAction, // 路由动作
    children: [
      {
        path: "contacts/:contactId", // 子路由路径
        element: <Contact />, // 子路由对应的组件
      },
    ],
  },
]);
```
详细注释如下：
1. 引入 `Root` 组件以及命名为 `rootLoader` 和 `rootAction` 的别名，这些别名是从 `./routes/root` 模块中导入的。
2. 定义一个名为 `router` 的变量，并调用 `createBrowserRouter` 函数来创建一个路由器。
3. 路由器配置包含一个对象，该对象定义了一个根路由的配置信息。
4. `path: "/"` 表示根路由的路径为根目录。
5. `element: <Root />` 表示渲染的组件为 `Root` 组件。
6. `errorElement: <ErrorPage />` 表示当路由出现错误时渲染的组件为 `ErrorPage` 组件。
7. `loader: rootLoader` 表示根路由的加载器为 `rootLoader`。
8. `action: rootAction` 表示根路由的动作为 `rootAction`。
9. `children` 数组包含一个对象，该对象定义了一个子路由的配置信息。
10. `path: "contacts/:contactId"` 表示子路由的路径为 "contacts/:contactId"，其中 `:contactId` 是一个参数占位符。
11. `element: <Contact />` 表示当匹配到子路由时，渲染的组件为 `Contact` 组件。
这段代码的功能是创建一个路由器，并定义了一个根路由和一个子路由的配置信息。根路由是根据路径渲染 `Root` 组件，并在遇到错误时渲染 `ErrorPage` 组件。子路由是当路径匹配到 "contacts/:contactId" 时，渲染 `Contact` 组件。

在给定的代码中，`loader` 和 `action` 是用于路由配置的属性。
1. `loader`：`loader` 是一个用于异步加载路由组件的函数。它可以用于在路由被激活之前，动态地加载组件所需的资源。通常情况下，当路由被访问时，`loader` 函数会被调用，然后它会返回一个 Promise 对象，该 Promise 对象会在加载完成后解析为路由组件。
   在示例代码中，`rootLoader` 是一个用于根路由的加载器函数。它会在根路由被激活时动态加载 `Root` 组件所需的资源。
2. `action`：`action` 是一个用于处理路由的函数。它可以执行一些额外的操作，例如数据获取、状态更新等。通常情况下，当路由被激活时，`action` 函数会被调用。
   在示例代码中，`rootAction` 是一个用于根路由的动作函数。它会在根路由被激活时执行一些额外的操作。
这些属性可以根据具体的路由需求进行定义和使用。`loader` 和 `action` 可以提供更加灵活和高级的路由控制，例如按需加载组件、数据预取和状态管理等。它们使得在路由被访问时可以进行更多的自定义操作，以实现更复杂的路由行为和功能。

#### Promise对象

Promise 对象是用于处理异步操作的 JavaScript 对象。它代表一个尚未完成但最终会完成（或失败）的操作，并可以在操作成功或失败后返回结果或错误。
Promise 对象有三种状态：
1. Pending（进行中）：初始状态，表示操作正在进行中，尚未完成或失败。
2. Fulfilled（已成功）：表示操作已成功完成。
3. Rejected（已失败）：表示操作已失败。
创建 Promise 对象时，我们可以通过传递一个执行器函数，该函数接受两个参数：`resolve` 和 `reject`，用于在操作完成（或失败）时分别将 Promise 对象标记为 Fulfilled 或 Rejected 状态。
```javascript
const myPromise = new Promise((resolve, reject) => {
  // 异步操作
  // 如果操作成功，调用 resolve(result)
  // 如果操作失败，调用 reject(error)
});
```
我们可以通过调用 `then` 方法来注册成功处理程序，并通过调用 `catch` 方法来注册失败处理程序，以便在 Promise 对象状态变为 Fulfilled 或 Rejected 时执行相应的代码。
```javascript
myPromise.then(result => {
  // 操作成功时的处理代码
}).catch(error => {
  // 操作失败时的处理代码
});
```
通过这种方式，我们可以利用 Promise 对象来处理异步操作，并以更清晰、可读性更高的方式编写异步代码。
Promise 对象是 JavaScript 异步编程中的重要概念，它提供了更强大的处理异步操作的能力，避免了回调地狱（callback hell）的问题，使得异步代码更易于理解和维护。































```jsx
//src/routers/contact.jsx
import { Form, useLoaderData } from "react-router-dom";
import { getContact } from "../contacts";

export async function loader({ params }) {
  const contact = await getContact(params.contactId);
  return { contact };
}

export default function Contact() {
  const { contact } = useLoaderData();
  // existing code
}
```



Wire the action up to the route


```jsx
// src/main.jsx
/* existing code */
import EditContact, {
  action as editAction,
} from "./routes/edit";

const router = createBrowserRouter([
  {
    path: "/",
    element: <Root />,
    errorElement: <ErrorPage />,
    loader: rootLoader,
    action: rootAction,
    children: [
      {
        path: "contacts/:contactId",
        element: <Contact />,
        loader: contactLoader,
      },
      {
        path: "contacts/:contactId/edit",
        element: <EditContact />,
        loader: contactLoader,
        action: editAction,
      },
    ],
  },
]);

/* existing code */
```
在给定的代码中，`path: "contacts/:contactId"` 和 `path: "contacts/:contactId/edit"` 是两个不同的路由路径配置。
1. `path: "contacts/:contactId"`：表示一个路由路径模式，其中 `:contactId` 是一个参数占位符。这个路由路径模式可以匹配形如 "contacts/123" 的路径，其中 `123` 是实际的联系人ID。这个路由路径用于渲染 `<Contact />` 组件。
2. `path: "contacts/:contactId/edit"`：也表示一个路由路径模式，同样使用 `:contactId` 作为参数占位符。这个路由路径模式可以匹配形如 "contacts/123/edit" 的路径，其中 `123` 是实际的联系人ID。这个路由路径用于渲染 `<EditContact />` 组件，表示编辑特定联系人的页面。
这两个路径模式的区别在于后缀部分。第一个路径模式只匹配 "contacts/:contactId" 形式的路径，而第二个路径模式匹配 "contacts/:contactId/edit" 形式的路径。这样设计可以让我们在应用中根据不同的路径来渲染不同的组件，并进行相应的操作。
在路由配置中，我们可以使用参数占位符来提取 URL 中的动态部分，并将其作为参数传递给相应的组件或操作函数。这样可以实现根据不同的路径和参数来动态地渲染不同的内容，实现更灵活和可扩展的路由功能。

```jsx
import {
  Outlet,
  NavLink,
  useLoaderData,
  Form,
  redirect,
} from "react-router-dom";

export default function Root() {
  return (
    <>
      <div id="sidebar">
        {/* other code */}

        <nav>
          {contacts.length ? (
            <ul>
              {contacts.map((contact) => (
                <li key={contact.id}>
                  <NavLink
                    to={`contacts/${contact.id}`}
                    className={({ isActive, isPending }) =>
                      isActive
                        ? "active"
                        : isPending
                        ? "pending"
                        : ""
                    }
                  >
                    {/* other code */}
                  </NavLink>
                </li>
              ))}
            </ul>
          ) : (
            <p>{/* other code */}</p>
          )}
        </nav>
      </div>
    </>
  );
}
```

给定的代码是一个名为 `Root` 的函数组件，它使用了 `react-router-dom` 库中的一些导入模块和组件，并渲染了一个具有导航菜单的根组件。
代码解析如下：
1. 导入了 `react-router-dom` 库中的一些模块和组件，包括 `Outlet`, `NavLink`, `useLoaderData`, `Form`, 和 `redirect`。这些模块和组件用于实现路由功能和相关的组件。
2. `Root` 组件是一个默认导出的函数组件，它接受没有任何参数。它是一个 React 组件，用于渲染根组件的内容。
3. 组件返回了一个 JSX 元素，使用了 React Fragments (`<>...</>`) 包裹了整个内容，以便返回多个子元素而无需创建额外的 DOM 节点。
4. 在返回的 JSX 元素中，有一个 `div` 元素，其 `id` 属性为 "sidebar"。这可能是一个侧边栏的容器。
5. `div` 元素内部有一个 `nav` 元素，用于包含导航菜单。
6. 在导航菜单中，使用了条件渲染。如果 `contacts` 数组有元素，就渲染一个有序列表，并使用 `map` 方法遍历 `contacts` 数组生成多个 `li` 元素。
7. 每个 `li` 元素中使用了 `NavLink` 组件，用于创建导航链接。`to` 属性使用了模板字符串，动态生成了链接目标路径，这里是 `contacts/:contact.id`，其中 `:contact.id` 是一个占位符，表示联系人的ID。
8. `NavLink` 组件的 `className` 属性使用了一个函数，用于根据当前路由状态动态设置类名。<font color="#2DC26B">如果当前链接处于活动状态（即与当前路由匹配），则类名为 "active"，如果链接正在等待加载，则类名为 "pending"。</font>
9. 在 `NavLink` 组件中，可以添加其他的子元素或文本内容，用于显示导航链接的标签或其他信息。
10. 如果 `contacts` 数组为空，就渲染一个段落元素，可能用于显示一些默认的内容或提示信息。
这段代码的作用是渲染一个根组件，其中包含一个导航菜单，根据 `contacts` 数组动态生成导航链接。每个链接都可以根据当前的路由状态应用不同的类名和样式，以提供一种用户导航的体验。

#### React Router常用钩子函数
是的，`useLoaderData` 和 `useSubmit` 都是 React Router 中的钩子函数。React Router 提供了许多常用的钩子函数，用于处理路由相关的逻辑和状态。以下是一些常用的 React Router 钩子函数及其作用和用法，以 Markdown 形式展示：
### `useParams`
- 作用：用于获取当前路由参数。
- 用法：
```jsx
import { useParams } from 'react-router-dom';
function MyComponent() {
  const { id } = useParams();
  return (
    <div>
      Current ID: {id}
    </div>
  );
}
```
### `useLocation`
- 作用：用于获取当前的路由位置信息。
- 用法：
```jsx
import { useLocation } from 'react-router-dom';
function MyComponent() {
  const location = useLocation();
  return (
    <div>
      Current Pathname: {location.pathname}
    </div>
  );
}
```
### `useHistory`
- 作用：用于访问路由历史对象，以进行导航和操作。
- 用法：
```jsx
import { useHistory } from 'react-router-dom';
function MyComponent() {
  const history = useHistory();
  const handleClick = () => {
    history.push('/new-route');
  };
  return (
    <button onClick={handleClick}>Go to New Route</button>
  );
}
```
### `useRouteMatch`
- 作用：用于获取当前路由匹配的信息。
- 用法：
```jsx
import { useRouteMatch } from 'react-router-dom';
function MyComponent() {
  const match = useRouteMatch('/users/:id');
  return (
    <div>
      Path: {match.path}
      <br />
      URL: {match.url}
    </div>
  );
}
```
### `useNavigate`
- 作用：用于进行编程式导航。
- 用法：
```jsx
import { useNavigate } from 'react-router-dom';
function MyComponent() {
  const navigate = useNavigate();
  const handleClick = () => {
    navigate('/new-route');
  };
  return (
    <button onClick={handleClick}>Go to New Route</button>
  );
}
```
这些是一些常用的 React Router 钩子函数，它们提供了灵活和方便的方式来处理路由相关的逻辑和状态。你可以根据具体的需求选择适合的钩子函数来使用，并结合 React Router 提供的其他功能来构建强大的路由应用程序。

[[../../BackEnd/RoadMap&Interview/面试答疑]]




















