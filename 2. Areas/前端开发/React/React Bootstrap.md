---
aliases:

---
20230717 0932
links: [React Bootstrap | React Bootstrap (react-bootstrap.github.io)](https://react-bootstrap.github.io/)
title:
origin:
tags: #flashcards #todo 


[Spark - Bootstrap 5 Admin & Dashboard Template (bootlab.io)](https://spark.bootlab.io/ui-cards)

页面结构
  
  | 中文                            | 英文                     |
  | ------------------------------- | ------------------------ |
  | 默认首页(Dashboard)             | Default dashboard        |
  | 分析首页(Analytics dashboard)   | Analytics dashboard      |
  | 电商首页(E-commerce Dashboard)  | E-commerce Dashboard     |
  | 登录页(Sign In page)            | Sign In page             |
  | 注册页(Sign Up page)            | Sign Up page             |
  | 重置密码页(Reset Password page) | Reset Password page      |
  | 设置页(Settings page)           | Settings page            |
  | 客户页(Clients page)            | Clients page             |
  | 价格页( page)                   | Pricing page             |
  | 发票页(Invoice page)            | Invoice page             |
  | 任务页(Tasks page)              | Tasks page               |
  | 聊天页(Chat page)               | Chat page                |
  | 404页                           | 404 page                 |
  | 500页                           | 500 page                 |
  | 空白页(Blank page)              | Blank page               |
  | Alert组件                       | Alerts components        |
  | Button组件                      | Buttons components       |
  | Card组件                        | Cards components         |
  | 布局组件                        | General components       |
  | 表格组件                        | Grid components          |
  | 模态框组件                      | Modals components        |
  | 通知组件                        | Notifications components |
  | Offcanvas组件                   | Offcanvas components     |
  | 占位组件                        | Placeholder components   |
  | Tab组件                         | Tabs components          |
  | Typography组件                  | Typography components    |
  | Chart图表组件                   | Chart.js charts          |
  | 表单组件                        | Form layouts             |
  | Icons图标组件                   | Icons                    |
  | 地图组件                        | Maps                     |
  | 表格组件                        | Tables                   |

  增加几列放入关键代码和库的表格如下:
  
| 中文                            | 英文                 | 关键代码            | 主要库                     |     |
| ------------------------------- | -------------------- | ------------------- | -------------------------- | --- |
| 默认首页(Dashboard)             | Default dashboard    | useState, useEffect | React, Chart.js            |     |
| 分析首页(Analytics dashboard)   | Analytics dashboard  | useState, useEffect | React, Apex                |     |
| 电商首页(E-commerce Dashboard)  | E-commerce Dashboard | useState, useEffect | React, React-table         |     |
| 登录页(Sign In page)            | Sign In page         | useState, useRef    | React, Formik              |     |
| 注册页(Sign Up page)            | Sign Up page         | useState, useRef    | React, Formik              |     |
| 重置密码页(Reset Password page) | Reset Password page  | useState, useRef    | React, Formik              |     |
| 设置页(Settings page)           | Settings page        | useState, useEffect | React, React-hook-form     |     |
| 客户页(Clients page)            | Clients page         | useState, useEffect | React, React-table         |     |
| 价格页( page)                   | Pricing page         | useState            | React                      |     |
| 发票页(Invoice page)            | Invoice page         | useState, useEffect | React, React-pdf           |     |
| 任务页(Tasks page)              | Tasks page           | useState, useEffect | React, React-beautiful-dnd |     |
| 聊天页( page)                   | Chat page            | useState, useEffect | React, Socket.io           |     |
| 404页                           | 404 page             | -                   | React                      |     |
| 500页                           | 500 page             | -                   | React                      |     |
| 空白页(Blank page)              | Blank page           | -                   | React                      |     |
| Alert组件                       | Alerts components    | -                   | React                      |     |
| Button组件                      | Buttons components   | -                   | React                      |     |
| Card组件                        | Cards components     | -                   | React                      |     | 

增加了关键代码和库列,可以更清晰了解每个模板或组件的实现。 

  | 功能 | 说明 |
  |-|-|
  | 🎨 主题功能 | |
  | 3种颜色主题 | 默认主题、深色主题、浅色主题 |
  | Create React App | 脚手架 |
  | Redux | 状态管理 |
  | React Router 4 | 路由 |
  | Async Loading | 异步加载 |
  | Code Splitting | 代码分割 |
  | Babel, ES6 & Eslint | 语法支持 |
  | Responsive design | 响应式设计 |
  | 易定制化 | 便于个性化定制 |
  | CSS动画 | 动画效果 |  
  | Bootstrap 4 | UI框架 |
  | Webpack | 打包构建 |
  | Font Awesome | 字体图标 |
  | Ion Icons | 图标库 |
  | Feather Icons | 图标库 |
  | DataTables | 数据表格 |
  | Google Maps | 地图 |
  | jQuery Vector Maps | 地图 |
  | Markdown Editor | Markdown编辑器 |
  | Quill Editor | 富文本编辑器 |
  | To知组件 |
  | ChartJS | 图表 |
  | Apex | 图表 |
  | Drag & Drop | 拖拽 |
  以表格形式整理主题功能项,便于浏览和理解。

```CSS
 col-12 col-md-6 col-lg-4
```

含义
   col-12 col-md-6 col-lg-4这个class组合代表的含义:
  - col-12:针对extra small设备(<576px),列占整行。
  - col-md-6:针对中等设备(≥576px),列占一半行。 
  - col-lg-4:针对大设备(≥992px),列占1/3行。
  这三个class组合在不同尺寸下设置列(column)的宽度:
  - extra small设备下,列占整行宽度
  - 中等设备及以上,列占一半行宽度  
  - 大设备及以上,列占1/3行宽度
  通过设置不同尺寸下的col-*,可以实现响应式布局。
  一般情况下:
  - col-设置列宽
  - 数字代表宽度占比
  - 小屏幕类优先级高
  所以这个class组合可以实现元素在不同屏幕下自动调整列宽的响应式布局。
  它通常用于前端框架如Bootstrap中的栅格系统。


代码片段赏析
  
  ```html
    <div class="col-12 col-lg-6"> <!-- 外层容器,响应式栅格 -->
  
   <div class="card"> <!-- 卡片容器 -->
  
   <div class="card-header"> <!-- 头部区域 -->
  
     <ul class="nav nav-tabs card-header-tabs pull-right" role="tablist"> <!-- 选项卡导航 -->
  
     <li class="nav-item" role="presentation"> <!-- 单个选项卡 -->
  
       <a class="nav-link active" data-bs-toggle="tab" href="#tab-1" aria-selected="true" role="tab">Active</
  
       <!-- .nav-link样式定义链接样式
        active类定义当前选中状态
        data-bs-toggle定义点击行为
        href定义链接地址
        aria-selected定义无障碍访问属性 -->
  
     </li>
  
     <li class="nav-item" role="presentation"> <!-- 单个选项卡 -->  
  
       <a class="nav-link" data-bs-toggle="tab" href="#tab-2" aria-selected="false" tabindex="-1" role="tab">Link</a>
  
       <!-- 同上 -->
  
     </li>
  
     <li class="nav-item" role="presentation"> <!-- 单个选项卡 -->
  
       <a class="nav-link disabled" data-bs-toggle="tab" href="#tab-3" aria-selected="false" tabindex="-1" role="tab">Disabled</
  
       <!-- disabled类定义禁用状态 -->
  
     </li>
  
     </ul>
  
     <!-- nav-tabs定义表格样式
      card-header-tabs定义位置
      pull-right定义对齐方式 -->
  
   </div>
  
   ...
  
   </div>
  
  </div>
  
  ```
  

useRoutes是一个React Router的Hook,用于动态地渲染一组嵌套路由。
使用方式:
```jsx
const element = (
  <Routes>
    <Route path="/" element={<Layout />}>
      {element} 
    </Route>
  </Routes>
)
const routes = useRoutes([
  {
    path: '/',
    element: <HomePage />
  },
  {
    path: 'users',
    element: <UsersPage />,
    children: [
      {
        path: ':userId',
        element: <User />
      }
    ]
  }
])
function Layout() {
  return (
    <div>
      <nav>...</nav>
      {routes}
    </div>
  )
}
```
主要特点:
- 通过数组定义路由配置
- 支持嵌套子路由
- 自动渲染路由匹配组件
- 简化了路由配置的书写
使用useRoutes可以:
- 声明式定义路由结构
- 动态渲染路由组件
- 避免手动渲染`<Route>`
- 适用于需要动态加载路由的场景
它使路由配置变得更加简洁和声明式。


useRoutes与使用JSX方式定义路由的主要区别:
**使用JSX方式:**
- 需要手动在Routes组件中渲染每个Route
- 路由配置嵌套不够直观
- 需要为每个Route单独定义element
- 难以动态加载路由
```jsx
<Routes>
  <Route path="/" element={<Layout />}>
    <Route index element={<HomePage />} />
    <Route path="users" element={<UsersPage />}>
      <Route path=":userId" element={<User />} /> 
    </Route>
  </Route>
</Routes>
```
**使用useRoutes:**
- 自动渲染匹配的路由组件  
- 通过数组清晰定义嵌套结构
- element统一定义在配置对象中
- 支持动态加载路由
```jsx
const routes = useRoutes([
  {
    path: '/',
    element: <Layout />,
    children: [
      {
        index: true,
        element: <HomePage />
      },
      {
        path: 'users',
        element: <UsersPage />, 
        children: [
          {
            path: ':userId',
            element: <User />
          }
        ]
      }
    ]
  }
])
```
总体来说,useRoutes使路由配置更简洁,动态性更强,是定义路由的推荐方式。








### Rebuilt with React

React-Bootstrap replaces the Bootstrap JavaScript. Each component has been built from scratch as a true React component, without unneeded dependencies like jQuery.



### Bootstrap at its core

Built with compatibility in mind, we embrace our bootstrap core and strive to be compatible with the world's largest UI ecosystem.

By relying entirely on the Bootstrap stylesheet, React-Bootstrap just works with the thousands of Bootstrap themes you already love.

Docs

- [Getting Started](https://react-bootstrap.github.io/docs/getting-started/introduction)
- [Layout](https://react-bootstrap.github.io/docs/layout/breakpoints)
- [Forms](https://react-bootstrap.github.io/docs/forms/overview)
- [Components](https://react-bootstrap.github.io/docs/components/accordion)
- [Utilities](https://react-bootstrap.github.io/docs/utilities/transitions)

Community

- [Stack Overflow](https://stackoverflow.com/questions/tagged/react-bootstrap)
- [Discord](https://discord.gg/AKfs9vpvRW)

# Getting-started 

`npm install react-bootstrap bootstrap `

Doing so pulls in only the specific components that you use, which can significantly reduce the amount of code you end up sending to the client.
```jsx
import Button from 'react-bootstrap/Button';

// or less ideally
import { Button } from 'react-bootstrap';
```

### Browser globals[​](https://react-bootstrap.github.io/docs/getting-started/introduction/#browser-globals "Direct link to Browser globals")

We provide `react-bootstrap.js` and `react-bootstrap.min.js` bundles with all components exported on the `window.ReactBootstrap` object. These bundles are available on [jsDelivr](https://www.jsdelivr.com/package/npm/react-bootstrap), as well as in the npm package.

```js
<script src="https://cdn.jsdelivr.net/npm/react/umd/react.production.min.js" crossorigin></script>  
  
<script  
src="https://cdn.jsdelivr.net/npm/react-dom/umd/react-dom.production.min.js"  
crossorigin></script>  
  
<script  
src="https://cdn.jsdelivr.net/npm/react-bootstrap@next/dist/react-bootstrap.min.js"  
crossorigin></script>
```

## Examples[​](https://react-bootstrap.github.io/docs/getting-started/introduction/#examples "Direct link to Examples")

React-Bootstrap has started a repo with a few basic CodeSandbox examples. [Click here](https://github.com/react-bootstrap/code-sandbox-examples/blob/master/README.md) to check them out.

## Stylesheets[​](https://react-bootstrap.github.io/docs/getting-started/introduction/#stylesheets "Direct link to Stylesheets")

Because React-Bootstrap doesn't depend on a very precise version of Bootstrap, we don't ship with any included CSS. However, some stylesheet **is required** to use these components.

### CSS[​](https://react-bootstrap.github.io/docs/getting-started/introduction/#css "Direct link to CSS")

```
{  /* The following line can be included in your src/index.js or App.js file */}import 'bootstrap/dist/css/bootstrap.min.css';
```

How and which Bootstrap styles you include is up to you, but the simplest way is to include the latest styles from the CDN. A little more information about the benefits of using a CDN can be found [here](https://www.w3schools.com/bootstrap/bootstrap_get_started.asp).

```js
<link  rel="stylesheet"  href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css"  integrity="sha384-9ndCyUaIbzAi2FUVXJi0CjmCapSmO7SnpJef0486qhLnuZ2cdeRhO02iuK6FUUVM"  crossorigin="anonymous"/>
```

### Sass[​](https://react-bootstrap.github.io/docs/getting-started/introduction/#sass "Direct link to Sass")

In case you are using **Sass** the simplest way is to include the Bootstrap’s source Sass files in your main Sass file and then require it on your `src/index.js` or `App.js` file. This applies to a typical `create-react-app` application in other use cases you might have to setup the bundler of your choice to compile Sass/SCSS stylesheets to CSS.

```
/* The following line can be included in a src/App.scss */@import '~bootstrap/scss/bootstrap';
```

```
/* The following line can be included in your src/index.js or App.js file */import './App.scss';
```

#### Customize Bootstrap[​](https://react-bootstrap.github.io/docs/getting-started/introduction/#customize-bootstrap "Direct link to Customize Bootstrap")

If you wish to customize the Bootstrap theme or any Bootstrap variables you can create a custom Sass file:

```js
/* The following block can be included in a custom.scss *//* make the customizations */
$theme-colors: (  'info': tomato,  'danger': teal);
/* import bootstrap to set changes */@import '~bootstrap/scss/bootstrap';
```

... And import it on the main Sass file.

```
/* The following line can be included in a src/App.scss */@import 'custom';
```

### Advanced usage[​](https://react-bootstrap.github.io/docs/getting-started/introduction/#advanced-usage "Direct link to Advanced usage")

See [the Bootstrap docs](https://getbootstrap.com/docs/5.3/customize/overview) for more advanced use cases and details about customizing stylesheets.

## `as` Prop API[​](https://react-bootstrap.github.io/docs/getting-started/introduction/#as-prop-api "Direct link to as-prop-api")

With certain React-Bootstrap components, you may want to modify the component or HTML tag that is rendered.

If you want to keep all the styling of a particular React-Bootstrap component but switch the component that is finally rendered (whether it's a different React-Bootstrap component, a different custom component, or a different HTML tag) you can use the `as` prop to do so.

The example below passes an anchor to the `as` prop in a `Button` component. This ultimately causes a `a` tag to be rendered but with the same styles as a `Button` component.

<Stack direction="horizontal" gap={2}>
  <Button as="a" variant="primary">
    Button as link1
  </Button>
  <Button as="a" variant="success">
    Button as link2
  </Button>
</Stack>
```js
<Stack direction="horizontal" gap={2}>
  <Button as="a" variant="primary">
    Button as link1
  </Button>
  <Button as="a" variant="success">
    Button as link2
  </Button>
</Stack>;
```

Below is an illustration of passing a React Bootstrap component. It contains a `Badge` component and a `Button` component that have been supplied to the `as` prop. This finally results in the rendering of a `Button` component with the same styles as a `Badge` component.

``` jsx
import Badge from 'react-bootstrap/Badge';
import Button from 'react-bootstrap/Button';

function Example() {
  return (
    <div>
      <h1>
        Example heading
        <Badge bg="secondary" as={Button}>
          New
        </Badge>
      </h1>
    </div>
  );
}

export default Example;
```

Methods and events using jQuery is done imperatively by directly manipulating the DOM.  
In contrast, React uses updates to the state to update the virtual DOM. In this way, React-Bootstrap provides a more reliable solution by incorporating Bootstrap functionality into React's virtual DOM.
Below are a few examples of how React-Bootstrap components differ from Bootstrap.

### Bootstrap[​](https://react-bootstrap.github.io/docs/getting-started/why-react-bootstrap#bootstrap "Direct link to Bootstrap")

```js
import * as React from 'react';

function Example() {
  return (
    <div class="alert alert-danger alert-dismissible fade show" role="alert">
      <strong>Oh snap! You got an error!</strong>
      <p>Change this and that and try again.</p>
      <button
        type="button"
        class="close"
        data-dismiss="alert"
        aria-label="Close"
      >
        <span aria-hidden="true">&times;</span>
      </button>
    </div>
  );
}
```

### React-Bootstrap[​](https://react-bootstrap.github.io/docs/getting-started/why-react-bootstrap#react-bootstrap "Direct link to React-Bootstrap")

```js
import * as React from 'react';
import Alert from 'react-bootstrap/Alert';

function Example() {
  return (
    <Alert dismissible variant="danger">
      <Alert.Heading>Oh snap! You got an error!</Alert.Heading>
      <p>Change this and that and try again.</p>
    </Alert>
  );
}
```

## Bootstrap with state[​](https://react-bootstrap.github.io/docs/getting-started/why-react-bootstrap#bootstrap-with-state "Direct link to Bootstrap with state")

Since React-Bootstrap is built with React Javascript, state can be passed within React-Bootstrap components as a prop. It also makes it easier to manage the state as updates are made using React’s state instead of directly manipulating the state of the DOM. This also gives a lot of flexibility when creating more complex components.

### React-bootstrap
```jsx
import { useState } from 'react';
import Alert from 'react-bootstrap/Alert';
import Button from 'react-bootstrap/Button';

function AlertDismissible() {
  const [show, setShow] = useState(true);

  return (
    <>
      <Alert show={show} variant="success">
        <Alert.Heading>My Alert</Alert.Heading>
        <p>
          Duis mollis, est non commodo luctus, nisi erat porttitor ligula, eget
          lacinia odio sem nec elit. Cras mattis consectetur purus sit amet
          fermentum.
        </p>
        <hr />
        <div className="d-flex justify-content-end">
          <Button onClick={() => setShow(false)} variant="outline-success">
            Close me
          </Button>
        </div>
      </Alert>

      {!show && <Button onClick={() => setShow(true)}>Show Alert</Button>}
    </>
  );
}

export default AlertDismissible;
```

### Bootstrap[​](https://react-bootstrap.github.io/docs/getting-started/why-react-bootstrap#bootstrap-1 "Direct link to Bootstrap")

```js
<div class="alert alert-success alert-dismissible fade show firstCollapsible" role="alert">
  <strong>How's it going?!</strong>
  <p>
    Duis mollis, est non commodo luctus, nisi erat porttitor ligula,
    eget lacinia odio sem nec elit. Cras mattis consectetur purus sit
    amet fermentum.
  </p>
  <hr/>
  <div class="d-flex justify-content-end">
    <button type="button" class="btn btn-outline-success">Close me ya'll!</button>
  </div>
</div>
<div class="d-flex justify-content-start alert fade show">
    <button type="button" class="btn btn-primary d-none secondCollapsible">Show Alert</button>
</div>
```

```js
$('.btn-outline-success').on('click', function(e) {
    $('.firstCollapsible').addClass('d-none');
    $('.secondCollapsible').removeClass('d-none');
})

$('.btn-primary').on('click', function(e) {
    $('.firstCollapsible').removeClass('d-none');
    $('.secondCollapsible').addClass('d-none');
})
```

# Theming and customizing styles
```js
import Button from 'react-bootstrap/Button';

function VariantsExample() {
  return (
    <>
      <style type="text/css">
        {`
    .btn-flat {
      background-color: purple;
      color: white;
    }

    .btn-xxl {
      padding: 1rem 1.5rem;
      font-size: 1.5rem;
    }
    `}
      </style>

      <Button variant="flat" size="xxl">
        flat button
      </Button>
    </>
  );
}

export default VariantsExample;
```

```js
import ThemeProvider from 'react-bootstrap/ThemeProvider';
import Button from 'react-bootstrap/Button';

function PrefixesExample() {
  return (
    <>
      {/* Hint: inspect the markup to see how the classes differ */}
      <ThemeProvider prefixes={{ btn: 'my-btn' }}>
        <Button variant="primary">My Button</Button>
      </ThemeProvider>
      <Button bsPrefix="super-btn" variant="primary">
        Super button
      </Button>
    </>
  );
}

export default PrefixesExample;
```

# Color modes

Bootstrap v5.3 now supports color modes such as dark mode. Color modes can be toggled globally on the `<html>` element, or on specific components and elements, thanks to the `data-bs-theme` attribute.
```jsx
import Dropdown from 'react-bootstrap/Dropdown';
import DropdownButton from 'react-bootstrap/DropdownButton';

function Example() {
  return (
    <Stack direction="horizontal" gap={3}>
      <DropdownButton
        id="dropdown-button-dark-example2"
        variant="secondary"
        title="Light dropdown"
        className="mt-2"
        data-bs-theme="light"   //Color Modes
      >
        <Dropdown.Item href="#/action-1" active>
          Action
        </Dropdown.Item>
        <Dropdown.Item href="#/action-2">Another action</Dropdown.Item>
        <Dropdown.Item href="#/action-3">Something else</Dropdown.Item>
        <Dropdown.Divider />
        <Dropdown.Item href="#/action-4">Separated link</Dropdown.Item>
      </DropdownButton>

      <DropdownButton
        id="dropdown-button-dark-example2"
        variant="secondary"
        title="Dark dropdown"
        className="mt-2"
	        data-bs-theme="dark"//Color Modes
      >
        <Dropdown.Item href="#/action-1" active>
          Action
        </Dropdown.Item>
        <Dropdown.Item href="#/action-2">Another action</Dropdown.Item>
        <Dropdown.Item href="#/action-3">Something else</Dropdown.Item>
        <Dropdown.Divider />
        <Dropdown.Item href="#/action-4">Separated link</Dropdown.Item>
      </DropdownButton>
    </Stack>
  );
}

export default ColorMode;
```
# Getting help

Stay up to date on the development of React-Bootstrap and reach out to the community with these helpful resources.

## Stack Overflow[​](https://react-bootstrap.github.io/docs/getting-started/support#stack-overflow "Direct link to Stack Overflow")

[Ask questions](http://stackoverflow.com/questions/ask) about specific problems you have faced, including details about what exactly you are trying to do. Make sure you tag your question with `react-bootstrap`. You can also read through [existing React-Bootstrap questions](http://stackoverflow.com/questions/tagged/react-bootstrap).

## Chat rooms[​](https://react-bootstrap.github.io/docs/getting-started/support#chat-rooms "Direct link to Chat rooms")

Discuss questions in the `#react-bootstrap` channel on the [Reactiflux Discord](https://discord.gg/AKfs9vpvRW).

## GitHub issues[​](https://react-bootstrap.github.io/docs/getting-started/support#github-issues "Direct link to GitHub issues")

The issue tracker is the preferred channel for bug reports, features requests and submitting pull requests. See more about how we use issues in the [contribution guidelines](https://github.com/react-bootstrap/react-bootstrap/blob/master/CONTRIBUTING.md#issues).

# Server-side Rendering

React-Bootstrap automatically generates an `id` for some components (such as `DropdownToggle`) if they are not provided. This is done for accessibility purposes.

In server-side rendered applications, a `SSRProvider` must wrap the application in order to ensure that the auto-generated ids are consistent between the server and client.

```js
import SSRProvider from 'react-bootstrap/SSRProvider';
<SSRProvider>
	<App />
</SSRProvider>;
```

## Available breakpoints[​](https://react-bootstrap.github.io/docs/layout/breakpoints#available-breakpoints "Direct link to Available breakpoints")

Bootstrap includes six default breakpoints, sometimes referred to as _grid tiers_, for building responsively. These breakpoints can be customized if you’re using our source Sass files.

|Breakpoint|Class infix|Dimensions|
|---|---|---|
|X-Small|_None_|<576px|
|Small|`sm`|≥576px|
|Medium|`md`|≥768px|
|Large|`lg`|≥992px|
|Extra large|`xl`|≥1200px|
|Extra extra large|`xxl`|≥1400px|

## Custom breakpoints[​](https://react-bootstrap.github.io/docs/layout/breakpoints#custom-breakpoints "Direct link to Custom breakpoints")

If you are looking to use custom breakpoints, you must wrap your application with a theme provider and use the `breakpoints` prop to specify the breakpoints you will use. This ensures that components such as `Row` or `Col` can parse the correct custom breakpoint props.

```js
<ThemeProvider
  breakpoints={['xxxl', 'xxl', 'xl', 'lg', 'md', 'sm', 'xs', 'xxs']}
  minBreakpoint="xxs"
>
  <div>Your app...</div>
</ThemeProvider>;
```

## API[​](https://react-bootstrap.github.io/docs/layout/breakpoints#api "Direct link to API")

### ThemeProvider[​](https://react-bootstrap.github.io/docs/layout/breakpoints#themeprovider "Direct link to ThemeProvider")

```js
import ThemeProvider from 'react-bootstrap/ThemeProvider'
```

# Layout 
[[../CSS/CSS-TRICKS]]
## Flexbox 
[A Complete Guide to Flexbox | CSS-Tricks - CSS-Tricks](https://css-tricks.com/snippets/css/a-guide-to-flexbox/#flexbox-background)
![css-flexbox-poster.png (7200×10800) (css-tricks.com)](https://css-tricks.com/wp-content/uploads/2022/02/css-flexbox-poster.png)

## Grid system

Bootstrap’s grid system uses a series of containers, rows, and columns to layout and align content. It’s built with [flexbox](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Flexible_Box_Layout/Using_CSS_flexible_boxes) and is fully responsive. Below is an example and an in-depth look at how the grid comes together.

**New to or unfamiliar with flexbox?** [Read this CSS Tricks flexbox guide](https://css-tricks.com/snippets/css/a-guide-to-flexbox/#flexbox-background) for background, terminology, guidelines, and code snippets.


```jsx
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';

function ContainerExample() {
  return (
    <Container>
      <Row>
        <Col>1 of 1</Col>
      </Row>
    </Container>
  );
}

export default ContainerExample;
```

### Fluid Container[​](https://react-bootstrap.github.io/docs/layout/grid#fluid-container "Direct link to Fluid Container")

You can use `<Container fluid />` for width: 100% across all viewport and device sizes.

```jsx
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';

function ContainerFluidExample() {
  return (
    <Container fluid>
      <Row>
        <Col>1 of 1</Col>
      </Row>
    </Container>
  );
}

export default ContainerFluidExample;
```
You can set breakpoints for the `fluid` prop. Setting it to a breakpoint (`sm, md, lg, xl, xxl`) will set the `Container` as fluid until the specified breakpoint.
```jsx
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';

function ContainerFluidBreakpointExample() {
  return (
    <Container fluid="md">
      <Row>
        <Col>1 of 1</Col>
      </Row>
    </Container>
  );
}

export default ContainerFluidBreakpointExample;
```

### Auto-layout columns[​](https://react-bootstrap.github.io/docs/layout/grid#auto-layout-columns "Direct link to Auto-layout columns")

When no column widths are specified the `Col` component will render equal width columns
```jsx
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';

function AutoLayoutExample() {
  return (
    <Container>
      <Row>
        <Col>1 of 2</Col>
        <Col>2 of 2</Col>
      </Row>
      <Row>
        <Col>1 of 3</Col>
        <Col>2 of 3</Col>
        <Col>3 of 3</Col>
      </Row>
    </Container>
  );
}

export default AutoLayoutExample;
```

### Setting one column width

```jsx
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';

function AutoLayoutSizingExample() {
  return (
    <Container>
      <Row>
        <Col>1 of 3</Col>
        <Col xs={6}>2 of 3 (wider)</Col>
        <Col>3 of 3</Col>
      </Row>
      <Row>
        <Col>1 of 3</Col>
        <Col xs={5}>2 of 3 (wider)</Col>
        <Col>3 of 3</Col>
      </Row>
    </Container>
  );
}

export default AutoLayoutSizingExample;
```


### Variable width content[​](https://react-bootstrap.github.io/docs/layout/grid#variable-width-content "Direct link to Variable width content")

Set the column value (for any breakpoint size) to `auto` to size columns based on the natural width of their content.

```jsx
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';

function AutoLayoutVariableExample() {
  return (
    <Container>
      <Row className="justify-content-md-center">
        <Col xs lg="2">
          1 of 3
        </Col>
        <Col md="auto">Variable width content</Col>
        <Col xs lg="2">
          3 of 3
        </Col>
      </Row>
      <Row>
        <Col>1 of 3</Col>
        <Col md="auto">Variable width content</Col>
        <Col xs lg="2">
          3 of 3
        </Col>
      </Row>
    </Container>
  );
}

export default AutoLayoutVariableExample;
```

You can also mix and match breakpoints to create different grids depending on the screen size.

```jsx
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';

function ResponsiveExample() {
  return (
    <Container>
      {/* Stack the columns on mobile by making one full-width and the other half-width */}
      <Row>
        <Col xs={12} md={8}>
          xs=12 md=8
        </Col>
        <Col xs={6} md={4}>
          xs=6 md=4
        </Col>
      </Row>

      {/* Columns start at 50% wide on mobile and bump up to 33.3% wide on desktop */}
      <Row>
        <Col xs={6} md={4}>
          xs=6 md=4
        </Col>
        <Col xs={6} md={4}>
          xs=6 md=4
        </Col>
        <Col xs={6} md={4}>
          xs=6 md=4
        </Col>
      </Row>

      {/* Columns are always 50% wide, on mobile and desktop */}
      <Row>
        <Col xs={6}>xs=6</Col>
        <Col xs={6}>xs=6</Col>
      </Row>
    </Container>
  );
}

export default ResponsiveExample;
```

The `Col` breakpoint props also have a more complicated `object` prop form: `{span: number, order: number, offset: number}` for specifying offsets and ordering effects.

You can use the `order` property to control the **visual order** of your content.

```jsx
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';

function OrderingExample() {
  return (
    <Container>
      <Row>
        <Col xs>First, but unordered</Col>
        <Col xs={{ order: 12 }}>Second, but last</Col>
        <Col xs={{ order: 1 }}>Third, but second</Col>
      </Row>
    </Container>
  );
}

export default OrderingExample;
```

## Stacks

Shorthand helpers that build on top of our flexbox utilities to make component layout faster and easier than ever.
### Vertical[​](https://react-bootstrap.github.io/docs/layout/stack#vertical "Direct link to Vertical")

Stacks are vertical by default and stacked items are full-width by default. Use the `gap` prop to add space between items.

```jsx
import Stack from 'react-bootstrap/Stack';

function VerticalExample() {
  return (
    <Stack gap={3}>
      <div className="p-2">First item</div>
      <div className="p-2">Second item</div>
      <div className="p-2">Third item</div>
    </Stack>
  );
}

export default VerticalExample;
```

### Horizontal[​](https://react-bootstrap.github.io/docs/layout/stack#horizontal "Direct link to Horizontal")

Use `direction="horizontal"` for horizontal layouts. Stacked items are vertically centered by default and only take up their necessary width. Use the `gap` prop to add space between items.

```jsx
import Stack from 'react-bootstrap/Stack';

function HorizontalExample() {
  return (
    <Stack direction="horizontal" gap={3}>
      <div className="p-2">First item</div>
      <div className="p-2">Second item</div>
      <div className="p-2">Third item</div>
    </Stack>
  );
}

export default HorizontalExample;
```

Use a vertical `Stack` to stack buttons and other elements:
```jsx
import Button from 'react-bootstrap/Button';
import Stack from 'react-bootstrap/Stack';

function ButtonsExample() {
  return (
    <Stack gap={2} className="col-md-5 mx-auto">
      <Button variant="secondary">Save changes</Button>
      <Button variant="outline-secondary">Cancel</Button>
    </Stack>
  );
}

export default ButtonsExample;
```
Create an inline form with a horizontal `Stack`:
```jsx
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import Stack from 'react-bootstrap/Stack';

function FormExample() {
  return (
    <Stack direction="horizontal" gap={3}>
      <Form.Control className="me-auto" placeholder="Add your item here..." />
      <Button variant="secondary">Submit</Button>
      <div className="vr" />
      <Button variant="outline-danger">Reset</Button>
    </Stack>
  );
}

export default FormExample;
```
# Forms 

## Overview[​](https://react-bootstrap.github.io/docs/forms/overview#overview "Direct link to Overview")

The `<FormControl>` component renders a form control with Bootstrap styling. The `<FormGroup>` component wraps a form control with proper spacing, along with support for a label, help text, and validation state. To ensure accessibility, set `controlId` on `<FormGroup>`, and use `<FormLabel>` for the label.

```jsx
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';

function BasicExample() {
  return (
    <Form>
      <Form.Group className="mb-3" controlId="formBasicEmail">
        <Form.Label>Email address</Form.Label>
        <Form.Control type="email" placeholder="Enter email" />
        <Form.Text className="text-muted">
          We'll never share your email with anyone else.
        </Form.Text>
      </Form.Group>

      <Form.Group className="mb-3" controlId="formBasicPassword">
        <Form.Label>Password</Form.Label>
        <Form.Control type="password" placeholder="Password" />
      </Form.Group>
      <Form.Group className="mb-3" controlId="formBasicCheckbox">
        <Form.Check type="checkbox" label="Check me out" />
      </Form.Group>
      <Button variant="primary" type="submit">
        Submit
      </Button>
    </Form>
  );
}

export default BasicExample;
```

# Form controls

Give textual form controls like `<input>`s and `<textarea>`s an upgrade with custom styles, sizing, focus states, and more.
以下是对代码块进行详细注释的补充：
```jsx
import React from 'react';
import Form from 'react-bootstrap/Form';
function TextControlsExample() {
  return (
    <Form>
      {/* 表单组 - 输入框 */}
      <Form.Group className="mb-3" controlId="exampleForm.ControlInput1">
        <Form.Label>Email address</Form.Label>
        {/* 表单控件 - 输入框 */}
        <Form.Control type="email" placeholder="name@example.com" />
      </Form.Group>
      {/* 表单组 - 文本域 */}
      <Form.Group className="mb-3" controlId="exampleForm.ControlTextarea1">
        <Form.Label>Example textarea</Form.Label>
        {/* 表单控件 - 文本域 */}
        <Form.Control as="textarea" rows={3} />
      </Form.Group>
    </Form>
  );
}
export default TextControlsExample;
```
在上述代码中，我们使用了 `react-bootstrap` 的 `Form` 组件来创建表单。下面是对代码中各个部分的详细注释：
- `Form` 组件：用于创建一个表单。
- `Form.Group` 组件：将相关表单元素组合在一起，并提供样式和布局。
  - `className` 属性用于指定样式类名，这里使用了 `"mb-3"` 来添加底部的外边距。
  - `controlId` 属性用于指定组件的唯一标识，用于关联 `Form.Label` 和 `Form.Control`。
- `Form.Label` 组件：用于创建表单元素的标签。
- `Form.Control` 组件：用于创建不同类型的表单控件。
  - `type` 属性用于指定输入框的类型，这里使用了 `"email"`。
  - `placeholder` 属性用于指定输入框的占位符文本。
  - `as` 属性用于指定控件的类型，这里使用了 `"textarea"` 来创建文本域。
  - `rows` 属性用于指定文本域的行数。
通过使用 `react-bootstrap` 的 `Form`、`Form.Group`、`Form.Label` 和 `Form.Control` 组件，我们可以方便地创建具有样式和布局的表单。

```jsx
import Form from 'react-bootstrap/Form';

function InputSizesExample() {
  return (
    <>
      <Form.Control size="lg" type="text" placeholder="Large text" />
      <br />
      <Form.Control type="text" placeholder="Normal text" />
      <br />
      <Form.Control size="sm" type="text" placeholder="Small text" />
    </>
  );
}

export default InputSizesExample;
```

```jsx
import Form from 'react-bootstrap/Form';

function FormControlDisabledExample() {
  return (
    <>
      <Form.Control
        type="text"
        placeholder="Disabled input"
        aria-label="Disabled input example"
        disabled
        readOnly
      />
      <br />
      <Form.Control
        type="text"
        placeholder="Disabled readonly input"
        aria-label="Disabled input example"
        readOnly
      />
    </>
  );
}

export default FormControlDisabledExample;
```

## File input

```jsx
import Form from 'react-bootstrap/Form';

function FormFileExample() {
  return (
    <>
      <Form.Group controlId="formFile" className="mb-3">
        <Form.Label>Default file input example</Form.Label>
        <Form.Control type="file" />
      </Form.Group>
      <Form.Group controlId="formFileMultiple" className="mb-3">
        <Form.Label>Multiple files input example</Form.Label>
        <Form.Control type="file" multiple />
      </Form.Group>
      <Form.Group controlId="formFileDisabled" className="mb-3">
        <Form.Label>Disabled file input example</Form.Label>
        <Form.Control type="file" disabled />
      </Form.Group>
      <Form.Group controlId="formFileSm" className="mb-3">
        <Form.Label>Small file input example</Form.Label>
        <Form.Control type="file" size="sm" />
      </Form.Group>
      <Form.Group controlId="formFileLg" className="mb-3">
        <Form.Label>Large file input example</Form.Label>
        <Form.Control type="file" size="lg" />
      </Form.Group>
    </>
  );
}

export default FormFileExample;
```
## Color 

```jsx
import Form from 'react-bootstrap/Form';

function ColorPickerExample() {
  return (
    <>
      <Form.Label htmlFor="exampleColorInput">Color picker</Form.Label>
      <Form.Control
        type="color"
        id="exampleColorInput"
        defaultValue="#563d7c"
        title="Choose your color"
      />
    </>
  );
}

export default ColorPickerExample;
```


下面是使用 Markdown 表格格式列出 React Bootstrap 常用的 Form API：

|API|描述|
|---|---|
|`<Form>`|表单组件，用于创建表单|
|`<Form.Group>`|表单组组件，用于将相关表单元素组合在一起|
|`<Form.Label>`|表单标签组件，用于创建表单元素的标签|
|`<Form.Control>`|表单控件组件，用于创建不同类型的表单控件|
|`<Form.Text>`|表单文本组件，用于提供与表单相关的辅助性文本|
|`<Form.Check>`|表单选择框组件，用于创建单选框、复选框和开关按钮|
|`<Form.File>`|文件上传组件，用于创建文件上传表单控件|
|`<Form.Switch>`|开关按钮组件，用于创建开关按钮表单控件|
|`<Form.Range>`|范围选择器组件，用于创建范围选择器表单控件|
|`<Form.Select>`|下拉选择器组件，用于创建下拉选择器表单控件|
|`<Form.Textarea>`|文本域组件，用于创建多行文本输入框表单控件|
|`<Form.Control.Feedback>`|反馈组件，用于在表单控件下方提供验证错误反馈消息|
|`<Form.Control.FeedbackTooltip>`|工具提示反馈组件，用于在表单控件下方提供验证错误工具提示|
|`<Form.Row>`|行组件，用于创建表单的行，将多个列组合在一起|
|`<Form.Col>`|列组件，用于创建表单的列，通常与 `<Form.Row>` 一起使用|

这些是 React Bootstrap 中常用的 Form 组件和 API。您可以根据需要使用这些组件来创建功能丰富的表单。 希望这个表格能够帮助您快速了解 React Bootstrap 的常用 Form API！如果您还有其他问题，请随时提问。

下面是 React Bootstrap 中 `<Form.Control>` 组件的常用 API：
以下是 `<Form.Control>` 组件的常用 API 以及可选的类型：

|API|描述|类型可选值|
|---|---|---|
|`id`|唯一标识符，用于关联 `<Form.Label>` 和 `<Form.Control>`|字符串|
|`type`|输入框类型，例如 `"text"`、`"email"`、`"password"` 等|`"text"`, `"email"`, `"password"`, `"number"`, `"file"`, `"range"`, `"select"`, `"textarea"` 等|
|`value`|输入框的值|任意类型|
|`defaultValue`|输入框的默认值|任意类型|
|`placeholder`|输入框的占位符文本|字符串|
|`disabled`|是否禁用输入框|布尔值|
|`readOnly`|是否只读输入框|布尔值|
|`required`|是否为必填字段|布尔值|
|`onChange`|值变化时触发的事件处理函数|函数|
|`onBlur`|失去焦点时触发的事件处理函数|函数|
|`isValid`|是否为有效的输入|布尔值|
|`isInvalid`|是否为无效的输入|布尔值|
|`plaintext`|是否以纯文本形式显示输入框内容|布尔值|
|`as`|指定渲染的标签类型，例如 `"select"` 将渲染为 `<select>`|字符串|
|`size`|控制输入框的尺寸，可选值为 `"sm"` 和 `"lg"`|`"sm"`, `"lg"`|
|`rows`|文本域的行数（仅适用于文本域类型）|数字|
|`cols`|文本域的列数（仅适用于文本域类型）|数字|
|`maxLength`|输入框的最大字符数限制|数字|
|`min`|输入框可接受的最小值（仅适用于数值类型）|数字|
|`max`|输入框可接受的最大值（仅适用于数值类型）|数字|
|`step`|输入框的步长（仅适用于数值类型）|数字|
|`pattern`|正则表达式，用于验证输入的格式|字符串|
|`autoComplete`|控制自动完成的行为，例如 `"on"`（启用自动完成）或 `"off"`（禁用自动完成）|`"on"`, `"off"`|

这些是 `<Form.Control>` 组件的常用属性以及可选的类型。您可以根据需要使用这些属性来设置输入框的行为、样式和验证，同时根据类型可选值来选择合适的类型。 希望这个扩展了的 API 列表能够帮助您更全面地了解 `<Form.Control>` 组件的属性和可选类型！如果您还有其他问题，请随时提问。

# Form text

```jsx
import Form from 'react-bootstrap/Form';

function FormTextExample() {
  return (
    <>
      <Form.Label htmlFor="inputPassword5">Password</Form.Label>
      <Form.Control
        type="password"
        id="inputPassword5"
        aria-describedby="passwordHelpBlock"
      />
      <Form.Text id="passwordHelpBlock" muted>
        Your password must be 8-20 characters long, contain letters and numbers,
        and must not contain spaces, special characters, or emoji.
      </Form.Text>
    </>
  );
}

export default FormTextExample;
```

# Select

Customize the native `<select>` with custom CSS that changes the element’s initial appearance.


```jsx
import Form from 'react-bootstrap/Form';

function SelectBasicExample() {
  return (
    <Form.Select aria-label="Default select example">
      <option>Open this select menu</option>
      <option value="1">One</option>
      <option value="2">Two</option>
      <option value="3">Three</option>
    </Form.Select>
  );
}

export default SelectBasicExample;

```

```jsx

import Form from 'react-bootstrap/Form';

function SelectSizesExample() {
  return (
    <>
      <Form.Select size="lg">
        <option>Large select</option>
      </Form.Select>
      <br />
      <Form.Select>
        <option>Default select</option>
      </Form.Select>
      <br />
      <Form.Select size="sm">
        <option>Small select</option>
      </Form.Select>
    </>
  );
}

export default SelectSizesExample;
```


以下是对给定代码进行详细注释的补充：
```jsx
import React from 'react';
import Form from 'react-bootstrap/Form';
function CheckExample() {
  return (
    <Form>
      {['checkbox', 'radio'].map((type) => (
        <div key={`default-${type}`} className="mb-3">
          {/* 表单复选框或单选框 - 默认样式 */}
          <Form.Check
            type={type}
            id={`default-${type}`}
            label={`default ${type}`}
          />
          {/* 表单复选框或单选框 - 禁用状态 */}
          <Form.Check
            disabled
            type={type}
            label={`disabled ${type}`}
            id={`disabled-default-${type}`}
          />
        </div>
      ))}
    </Form>
  );
}
export default CheckExample;
```
在上述代码中，我们使用了 `react-bootstrap` 的 `Form` 和 `Form.Check` 组件来创建一组复选框和单选框。下面是对代码中各个部分的详细注释：
- `Form` 组件：用于创建一个表单。
- `{['checkbox', 'radio'].map((type) => ... )}`：使用 JavaScript 的 `map` 方法遍历一个包含 `'checkbox'` 和 `'radio'` 的数组，动态生成复选框和单选框。
- `<div key={`default-${type}`} className="mb-3">`：用于包裹每个复选框或单选框，并设置外边距样式。
- `<Form.Check type={type} id={`default-${type}`} label={`default ${type}`} />`：创建一个默认样式的表单复选框或单选框。
  - `type` 属性指定复选框或单选框的类型。
  - `id` 属性为复选框或单选框指定唯一标识符。
  - `label` 属性设置复选框或单选框的标签文本。
- <Form.Check disabled type={type} label={`disabled ${type}`} id={`disabled-default-${type}`} />`：创建一个禁用状态的表单复选框或单选框。
  - `disabled` 属性设置复选框或单选框为禁用状态。
通过使用 `react-bootstrap` 的 `Form` 和 `Form.Check` 组件，我们可以方便地创建默认样式和禁用状态的复选框和单选框。
希望这个补充了详细注释的代码能够帮助您理解 `CheckExample` 组件的功能！如果您还有其他问题，请随时提问。

```jsx
//Switches
import Form from 'react-bootstrap/Form';

function SwitchExample() {
  return (
    <Form>
      <Form.Check // prettier-ignore
        type="switch"
        id="custom-switch"
        label="Check this switch"
      />
      <Form.Check // prettier-ignore
        disabled
        type="switch"
        label="disabled switch"
        id="disabled-custom-switch"
      />
    </Form>
  );
}

export default SwitchExample;
```
[Checks and radios | React Bootstrap (react-bootstrap.github.io)](https://react-bootstrap.github.io/docs/forms/checks-radios)
#### Form Check 

```jsx
import Form from 'react-bootstrap/Form';

function CheckApiExample() {
  return (
    <Form>
      {['checkbox', 'radio'].map((type) => (
        <div key={type} className="mb-3">
          <Form.Check type={type} id={`check-api-${type}`}>
            <Form.Check.Input type={type} isValid />
            <Form.Check.Label>{`Custom api ${type}`}</Form.Check.Label>
            <Form.Control.Feedback type="valid">
              You did it!
            </Form.Control.Feedback>
          </Form.Check>
        </div>
      ))}
    </Form>
  );
}

export default CheckApiExample;
```
## Tooltips[​](https://react-bootstrap.github.io/docs/forms/validation#tooltips "Direct link to Tooltips") 

If your form layout allows it, you can use the `tooltip` prop to display validation feedback in a styled tooltip. Be sure to have a parent with `position: relative` on it for tooltip positioning. In the example below, our column classes have this already, but your project may require an alternative setup.

以下是对给定代码进行详细注释的补充：
```jsx
import React from 'react';
import Button from 'react-bootstrap/Button';
import Col from 'react-bootstrap/Col';
import Form from 'react-bootstrap/Form';
import InputGroup from 'react-bootstrap/InputGroup';
import Row from 'react-bootstrap/Row';
import * as formik from 'formik';
import * as yup from 'yup';
function FormExample() {
  const { Formik } = formik;
  // 使用 yup 定义表单校验规则
  const schema = yup.object().shape({
    firstName: yup.string().required(),
    lastName: yup.string().required(),
    username: yup.string().required(),
    city: yup.string().required(),
    state: yup.string().required(),
    zip: yup.string().required(),
    file: yup.mixed().required(),
    terms: yup.bool().required().oneOf([true], 'terms must be accepted'),
  });
  return (
    // 使用 Formik 组件包装表单，并设置校验规则、提交处理函数和初始值
    <Formik
      validationSchema={schema}
      onSubmit={console.log}
      initialValues={{
        firstName: 'Mark',
        lastName: 'Otto',
        username: '',
        city: '',
        state: '',
        zip: '',
        file: null,
        terms: false,
      }}
    >
      {({ handleSubmit, handleChange, values, touched, errors }) => (
        <Form noValidate onSubmit={handleSubmit}>
          {/* 第一行表单项 */}
          <Row className="mb-3">
            <Form.Group
              as={Col}
              md="4"
              controlId="validationFormik101"
              className="position-relative"
            >
              <Form.Label>First name</Form.Label>
              <Form.Control
                type="text"
                name="firstName"
                value={values.firstName}
                onChange={handleChange}
                isValid={touched.firstName && !errors.firstName}
              />
              <Form.Control.Feedback tooltip>Looks good!</Form.Control.Feedback>
            </Form.Group>
            {/* 其他表单项略 */}
          </Row>
          {/* 其他行表单项略 */}
          <Form.Group className="position-relative mb-3">
            <Form.Label>File</Form.Label>
            <Form.Control
              type="file"
              required
              name="file"
              onChange={handleChange}
              isInvalid={!!errors.file}
            />
            <Form.Control.Feedback type="invalid" tooltip>
              {errors.file}
            </Form.Control.Feedback>
          </Form.Group>
          <Form.Group className="position-relative mb-3">
            <Form.Check
              required
              name="terms"
              label="Agree to terms and conditions"
              onChange={handleChange}
              isInvalid={!!errors.terms}
              feedback={errors.terms}
              feedbackType="invalid"
              id="validationFormik106"
              feedbackTooltip
            />
          </Form.Group>
          <Button type="submit">Submit form</Button>
        </Form>
      )}
    </Formik>
  );
}
export default FormExample;
```
在上述代码中，我们使用了 `react-bootstrap` 的组件来创建一个表单。下面是对代码中各个部分的详细注释：
- `Formik` 组件：用于包装表单，提供表单校验、提交处理函数和初始值等功能。
- `yup`：使用 `yup` 库来定义表单校验规则，根据规则生成一个 `schema` 对象。
- `validationSchema={schema}`：通过 `validationSchema` 属性将校验规则应用到 `Formik` 组件。
- `onSubmit={console.log}`：设置表单提交处理函数，这里简单地打印表单数据到控制台。
- `initialValues`：设置表单的初始值，包括 `firstName`、`lastName`、`username` 等字段。
- `handleSubmit, handleChange, values, touched, errors`：这些是通过解构赋值从 `Formik` 组件传递过来的属性和方法，用于处理表单的提交、值的改变以及获取表单的值、触摸状态和错误信息。
- `<Form.Group>`：用于包裹每个表单项，提供布局和样式控制。
- `<Form.Control>`：创建各种类型的表单控件，例如文本输入框、下拉框等。
  - `type` 属性指定表单控件的类型。
  - `name` 属性指定表单控件的名称，与 `initialValues` 中的字段对应。
  - `value` 属性设置表单控件的值。
  - `onChange` 属性指定值改变时的处理函数。
  - `isValid` 属性用于设置表单控件的有效状态。
  - `isInvalid` 属性用于设置表单控件的无效状态。
  - `feedback` 属性用于显示表单控件的错误信息。
- `<Button type="submit">Submit form</Button>`：创建一个提交按钮，用于触发表单提交动作。
通过使用 `react-bootstrap` 的组件以及 `Formik` 和 `yup` 库，我们可以方便地创建具有校验规则和动态交互的表单。
希望这个补充了详细注释的代码能够帮助您理解 `FormExample` 组件的功能！如果您还有其他问题，请随时提问。

# Accordion

Build vertically collapsing accordions in combination with the Collapse component
```jsx
import Accordion from 'react-bootstrap/Accordion';

function BasicExample() {
  return (
    <Accordion defaultActiveKey="0">
      <Accordion.Item eventKey="0">
        <Accordion.Header>Accordion Item #1</Accordion.Header>
        <Accordion.Body>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
          eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad
          minim veniam, quis nostrud exercitation ullamco laboris nisi ut
          aliquip ex ea commodo consequat. Duis aute irure dolor in
          reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
          pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
          culpa qui officia deserunt mollit anim id est laborum.
        </Accordion.Body>
      </Accordion.Item>
      <Accordion.Item eventKey="1">
        <Accordion.Header>Accordion Item #2</Accordion.Header>
        <Accordion.Body>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
          eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad
          minim veniam, quis nostrud exercitation ullamco laboris nisi ut
          aliquip ex ea commodo consequat. Duis aute irure dolor in
          reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
          pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
          culpa qui officia deserunt mollit anim id est laborum.
        </Accordion.Body>
      </Accordion.Item>
    </Accordion>
  );
}

export default BasicExample;
```
## Alerts

Provide contextual feedback messages for typical user actions with the handful of available and flexible alert messages.
```jsx
import Alert from 'react-bootstrap/Alert';

function BasicExample() {
  return (
    <>
      {[
        'primary',
        'secondary',
        'success',
        'danger',
        'warning',
        'info',
        'light',
        'dark',
      ].map((variant) => (
        <Alert key={variant} variant={variant}>
          This is a {variant} alert—check it out!
        </Alert>
      ))}
    </>
  );
}

export default BasicExample;
```

### Dismissing[​](https://react-bootstrap.github.io/docs/components/alerts#dismissing "Direct link to Dismissing")

Add the `dismissible` prop to add a functioning dismiss button to the Alert.
```jsx
import { useState } from 'react';
import Alert from 'react-bootstrap/Alert';
import Button from 'react-bootstrap/Button';

function AlertDismissibleExample() {
  const [show, setShow] = useState(true);

  if (show) {
    return (
      <Alert variant="danger" onClose={() => setShow(false)} dismissible>
        <Alert.Heading>Oh snap! You got an error!</Alert.Heading>
        <p>
          Change this and that and try again. Duis mollis, est non commodo
          luctus, nisi erat porttitor ligula, eget lacinia odio sem nec elit.
          Cras mattis consectetur purus sit amet fermentum.
        </p>
      </Alert>
    );
  }
  return <Button onClick={() => setShow(true)}>Show Alert</Button>;
}

export default AlertDismissibleExample;
```

## Pill badges[​](https://react-bootstrap.github.io/docs/components/badge#pill-badges "Direct link to Pill badges")

Use the `pill` modifier class to make badges more rounded (with a larger `border-radius`). Useful if you miss the badges from v3.
```jsx
import Badge from 'react-bootstrap/Badge';
import Stack from 'react-bootstrap/Stack';

function PillExample() {
  return (
    <Stack direction="horizontal" gap={2}>
      <Badge pill bg="primary">
        Primary
      </Badge>
      <Badge pill bg="secondary">
        Secondary
      </Badge>
      <Badge pill bg="success">
        Success
      </Badge>
      <Badge pill bg="danger">
        Danger
      </Badge>
      <Badge pill bg="warning" text="dark">
        Warning
      </Badge>
      <Badge pill bg="info">
        Info
      </Badge>
      <Badge pill bg="light" text="dark">
        Light
      </Badge>
      <Badge pill bg="dark">
        Dark
      </Badge>
    </Stack>
  );
}

export default PillExample;
```
## Breadcrumbs

Indicate the current page’s location within a navigational hierarchy that automatically adds separators via Css-tricks.com 

```jsx
import Breadcrumb from 'react-bootstrap/Breadcrumb';

function BreadcrumbExample() {
  return (
    <Breadcrumb>
      <Breadcrumb.Item href="#">Home</Breadcrumb.Item>
      <Breadcrumb.Item href="https://getbootstrap.com/docs/4.0/components/breadcrumb/">
        Library
      </Breadcrumb.Item>
      <Breadcrumb.Item active>Data</Breadcrumb.Item>
    </Breadcrumb>
  );
}

export default BreadcrumbExample;
```
## Button group

```jsx
import Button from 'react-bootstrap/Button';
import ButtonGroup from 'react-bootstrap/ButtonGroup';
import Dropdown from 'react-bootstrap/Dropdown';
import DropdownButton from 'react-bootstrap/DropdownButton';

function VerticalExample() {
  return (
    <ButtonGroup vertical>
      <Button>Button</Button>
      <Button>Button</Button>

      <DropdownButton
        as={ButtonGroup}
        title="Dropdown"
        id="bg-vertical-dropdown-1"
      >
        <Dropdown.Item eventKey="1">Dropdown link</Dropdown.Item>
        <Dropdown.Item eventKey="2">Dropdown link</Dropdown.Item>
      </DropdownButton>

      <Button>Button</Button>
      <Button>Button</Button>

      <DropdownButton
        as={ButtonGroup}
        title="Dropdown"
        id="bg-vertical-dropdown-2"
      >
        <Dropdown.Item eventKey="1">Dropdown link</Dropdown.Item>
        <Dropdown.Item eventKey="2">Dropdown link</Dropdown.Item>
      </DropdownButton>

      <DropdownButton
        as={ButtonGroup}
        title="Dropdown"
        id="bg-vertical-dropdown-3"
      >
        <Dropdown.Item eventKey="1">Dropdown link</Dropdown.Item>
        <Dropdown.Item eventKey="2">Dropdown link</Dropdown.Item>
      </DropdownButton>
    </ButtonGroup>
  );
}

export default VerticalExample;
```

[[react-bootstrap Components]]














