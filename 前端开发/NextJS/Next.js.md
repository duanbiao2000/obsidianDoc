
---
aliases:

---
20230721 1454
links: [Docs | Next.js (nextjs.org)](https://nextjs.org/docs) [Introduction | Learn Next.js (nextjs.org)](https://nextjs.org/learn/foundations/about-nextjs) [Elliott-Chong/quizmify (github.com)](https://github.com/Elliott-Chong/quizmify)
title:
origin:
tags: #flashcards #todo 


##  [主要特点](https://nextjs.org/docs#main-features)

Next.js 的一些主要功能包括：

|特征|描述|
|---|---|
|[路由](https://nextjs.org/docs/app/building-your-application/routing)|基于文件系统的路由器构建在服务器组件之上，支持布局、嵌套路由、加载状态、错误处理等。|
|[渲染](https://nextjs.org/docs/app/building-your-application/rendering)|使用客户端和服务器组件进行客户端和服务器端渲染。使用 Next.js 在服务器上进一步优化静态和动态渲染。在 Edge 和 Node.js 运行时上进行流式传输。|
|[数据获取](https://nextjs.org/docs/app/building-your-application/data-fetching)|通过 React 组件中的 async/await 支持以及与 React 和 Web 平台保持一致的 `fetch()` API 简化了数据获取。|
|[造型](https://nextjs.org/docs/app/building-your-application/styling)|支持您喜欢的样式方法，包括 CSS 模块、Tailwind CSS 和 CSS-in-JS|
|[优化](https://nextjs.org/docs/app/building-your-application/optimizing)|图像、字体和脚本优化，以改善应用程序的核心网络生命和用户体验。|
|[TypeScript](https://nextjs.org/docs/app/building-your-application/configuring/typescript)|改进了对 TypeScript 的支持，提供更好的类型检查和更高效的编译，以及自定义 TypeScript 插件和类型检查器。|
|[API参考](https://nextjs.org/docs/app/api-reference)|更新了整个 Next.js 的 API 设计。有关新 API，请参阅 API 参考部分。|

首先，检查安装。如果您不熟悉 React 或服务器组件，我们建议您阅读 [[React Essentials]]页面

为了充分利用我们的文档，建议您对 HTML、CSS 和 React 有基本的了解。如果您需要温习 React 技能，请查看以下资源：

- [React：官方 React 文档](https://react.dev/learn)
-  [React要点](https://nextjs.org/docs/getting-started/react-essentials)

## Next.js 项目结构

此页面概述了 Next.js 项目的文件和文件夹结构。它涵盖 `app` 和 `pages` 目录中的顶级文件和文件夹、配置文件以及路由约定。

##  [顶级文件](https://nextjs.org/docs/getting-started/project-structure#top-level-files)

| | |
|---|---|
|**Next.js**| |
|[`next.config.js`](https://nextjs.org/docs/app/api-reference/next-config-js) | Next.js 的配置文件|
|[`middleware.ts`](https://nextjs.org/docs/app/building-your-application/routing/middleware)|Next.js 请求中间件|
|[`instrumentation.ts`](https://nextjs.org/docs/app/building-your-application/optimizing/instrumentation)|开放遥测和仪器|
|[`.env`](https://nextjs.org/docs/app/building-your-application/configuring/environment-variables)|环境变量|
|[`.env.local`](https://nextjs.org/docs/app/building-your-application/configuring/environment-variables)|本地环境变量|
|[`.env.production`](https://nextjs.org/docs/app/building-your-application/configuring/environment-variables)|生产环境变量|
|[`.env.development`](https://nextjs.org/docs/app/building-your-application/configuring/environment-variables)|开发环境变量|
|`.next-env.d.ts`|Next.js 的 TypeScript 声明文件|

| | |
|---|---|
|**生态系统**||
|[`package.json`](https://nextjs.org/docs/getting-started/installation#manual-installation)|项目依赖和脚本|
|`.gitignore`|要忽略的 Git 文件和文件夹|
|`tsconfig.json`|TypeScript 的配置文件|
|`jsconfig.json`|JavaScript 的配置文件|
|[`.eslintrc.json`](https://nextjs.org/docs/app/building-your-application/configuring/eslint)|ESLint 的配置文件|

##  [顶级文件夹](https://nextjs.org/docs/getting-started/project-structure#top-level-folders)

| | |
|---|---|
|[`app`](https://nextjs.org/docs/app/building-your-application/routing)|应用路由|
|[`pages`](https://nextjs.org/docs/pages/building-your-application/routing)|页面路由|
|[`public`](https://nextjs.org/docs/getting-started/installation#the-public-folder-optional)|static assets|
|[`src`](https://nextjs.org/docs/app/building-your-application/configuring/src-directory)|可选的应用程序源文件夹|

## [`app` 路由约定](https://nextjs.org/docs/getting-started/project-structure#app-routing-conventions)

###  [路由文件](https://nextjs.org/docs/getting-started/project-structure#routing-files)

| | | |
|---|---|---|
|[`layout`](https://nextjs.org/docs/app/api-reference/file-conventions/layout)|`.js` `.jsx` `.tsx`|布局|
|[`page`](https://nextjs.org/docs/app/api-reference/file-conventions/page)|`.js` `.jsx` `.tsx`|页|
|[`loading`](https://nextjs.org/docs/app/api-reference/file-conventions/loading)|`.js` `.jsx` `.tsx`|加载用户界面|
|[`not-found`](https://nextjs.org/docs/app/api-reference/file-conventions/not-found)|`.js` `.jsx` `.tsx`|未找到用户界面|
|[`error`](https://nextjs.org/docs/app/api-reference/file-conventions/error)|`.js` `.jsx` `.tsx`|错误用户界面|
|[`global-error`](https://nextjs.org/docs/app/api-reference/file-conventions/error#global-errorjs)|`.js` `.jsx` `.tsx`|全局错误用户界面|
|[`route`](https://nextjs.org/docs/app/api-reference/file-conventions/route)|`.js` `.ts`|API端点|
|[`template`](https://nextjs.org/docs/app/api-reference/file-conventions/template)|`.js` `.jsx` `.tsx`|重新渲染布局|
|[`default`](https://nextjs.org/docs/app/api-reference/file-conventions/default)|`.js` `.jsx` `.tsx`|并行路由默认页面|

###  [嵌套路由](https://nextjs.org/docs/getting-started/project-structure#nested-routes)

| | |
|---|---|
|[`folder`](https://nextjs.org/docs/app/building-your-application/routing#route-segments)|航线段|
|[`folder/folder`](https://nextjs.org/docs/app/building-your-application/routing#nested-routes)|嵌套路由段|

###  [动态路由](https://nextjs.org/docs/getting-started/project-structure#dynamic-routes)

| | |
|---|---|
|[`[folder]`](https://nextjs.org/docs/app/building-your-application/routing/dynamic-routes#convention)|动态路由|
|[`[...folder]`](https://nextjs.org/docs/app/building-your-application/routing/dynamic-routes#catch-all-segments)|Catch-all segments|
|[`[[...folder]]`](https://nextjs.org/docs/app/building-your-application/routing/dynamic-routes#optional-catch-all-segments)|Optional包罗万象的部分|

### [Router group和Private folders](https://nextjs.org/docs/getting-started/project-structure#route-groups-and-private-folders)

| | |
|---|---|
|[`(folder)`](https://nextjs.org/docs/app/building-your-application/routing/route-groups#convention)|对路由进行分组而不影响路由|
|[`_folder`](https://nextjs.org/docs/app/building-your-application/routing/colocation#private-folders)|选择文件夹和所有子段不参与路由|

### [Parallel和Intercepted的路由](https://nextjs.org/docs/getting-started/project-structure#parallel-and-intercepted-routes)

| | |
|---|---|
|[`@folder`](https://nextjs.org/docs/app/building-your-application/routing/parallel-routes#convention)|命名槽|
|[`(.)folder`](https://nextjs.org/docs/app/building-your-application/routing/intercepting-routes#convention)|拦截同级|
|[`(..)folder`](https://nextjs.org/docs/app/building-your-application/routing/intercepting-routes#convention)|拦截上面一层|
|[`(..)(..)folder`](https://nextjs.org/docs/app/building-your-application/routing/intercepting-routes#convention)|拦截上面两层|
|[`(...)folder`](https://nextjs.org/docs/app/building-your-application/routing/intercepting-routes#convention)|从根拦截|

### [元数据文件约定](https://nextjs.org/docs/getting-started/project-structure#metadata-file-conventions)

####  [应用程序图标](https://nextjs.org/docs/getting-started/project-structure#app-icons)

| | | |
|---|---|---|
|[`favicon`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons#favicon)|`.ico`|文件图标|
|[`icon`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons#icon)|`.ico` `.jpg` `.jpeg` `.png` `.svg`|应用程序图标文件|
|[`icon`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons#generate-icons-using-code-js-ts-tsx)|`.js` `.ts` `.tsx`|生成的应用程序图标|
|[`apple-icon`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons#apple-icon)|`.jpg` `.jpeg` , `.png`|苹果应用程序图标文件|
|[`apple-icon`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons#generate-icons-using-code-js-ts-tsx)|`.js` `.ts` `.tsx`|生成的苹果应用程序图标|

#### [打开图谱和 Twitter 图片](https://nextjs.org/docs/getting-started/project-structure#open-graph-and-twitter-images)

| || |
|---|---|---|
|[`opengraph-image`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image#opengraph-image)|`.jpg` `.jpeg` `.png` `.gif`|打开图形图像文件|
|[`opengraph-image`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image#generate-images-using-code-js-ts-tsx)|`.js` `.ts` `.tsx`|生成的 Open Graph 图像|
|[`twitter-image`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image#twitter-image)|`.jpg` `.jpeg` `.png` `.gif`|推特图像文件|
|[`twitter-image`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image#generate-images-using-code-js-ts-tsx)|`.js` `.ts` `.tsx`|生成的 Twitter 图片|

#### [SEO](https://nextjs.org/docs/getting-started/project-structure#seo)

| | | |
|---|---|---|
|[`sitemap`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/sitemap#static-sitemapxml)|`.xml`|站点地图文件|
|[`sitemap`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/sitemap#generate-a-sitemap)|`.js` `.ts`|生成的站点地图|
|[`robots`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/robots#static-robotstxt)|`.txt`|机器人文件|
|[`robots`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/robots#generate-a-robots-file)|`.js` `.ts`|生成的机器人文件|

## [`pages` 路由约定](https://nextjs.org/docs/getting-started/project-structure#pages-routing-conventions)

###  [特殊文件](https://nextjs.org/docs/getting-started/project-structure#special-files)

| || |
|---|---|---|
|[`_app`](https://nextjs.org/docs/pages/building-your-application/routing/custom-app)|`.js` `.jsx` `.tsx`|定制应用程序|
|[`_document`](https://nextjs.org/docs/pages/building-your-application/routing/custom-document)|`.js` `.jsx` `.tsx`|定制文件|
|[`_error`](https://nextjs.org/docs/pages/building-your-application/routing/custom-error#more-advanced-error-page-customizing)|`.js` `.jsx` `.tsx`|自定义错误页面|
|[`404`](https://nextjs.org/docs/pages/building-your-application/routing/custom-error#404-page)|`.js` `.jsx` `.tsx`|404错误页面|
|[`500`](https://nextjs.org/docs/pages/building-your-application/routing/custom-error#500-page)|`.js` `.jsx` `.tsx`|500 错误页面|

###  [路由](https://nextjs.org/docs/getting-started/project-structure#routes)

| | | |
|---|---|---|
|**文件夹约定**|||
|[`index`](https://nextjs.org/docs/pages/building-your-application/routing/pages-and-layouts#index-routes)|`.js` `.jsx` `.tsx`|主页|
|[`folder/index`](https://nextjs.org/docs/pages/building-your-application/routing/pages-and-layouts#index-routes)|`.js` `.jsx` `.tsx`|嵌套页面|
|**文件约定**|||
|[`index`](https://nextjs.org/docs/pages/building-your-application/routing/pages-and-layouts#index-routes)|`.js` `.jsx` `.tsx`|主页|
|[`file`](https://nextjs.org/docs/pages/building-your-application/routing/pages-and-layouts)|`.js` `.jsx` `.tsx`|嵌套页面|


# React Essentials 反应要点

To build applications with Next.js, it helps to be familiar with React's newer features such as Server Components.<font color="#b7dde8"> This page will go through the differences between Server and Client Components, when to use them, and recommended patterns.</font>
- [React Tutorial 反应教程](https://react.dev/learn/tutorial-tic-tac-toe)
- [Thinking in React 在 React 中思考](https://react.dev/learn/thinking-in-react)
- [Learn React 学习反应](https://react.dev/learn/describing-the-ui)

## [Server Components 服务器组件](https://nextjs.org/docs/getting-started/react-essentials#server-components)

Server and Client Components allow developers to build applications that span the server and client, combining the rich interactivity of client-side apps with the improved performance of traditional server rendering.

Instead of React rendering your whole application client-side (such as in the case of Single-Page Applications), React now gives you the flexibility to choose where to render your components based on their purpose.  
React 现在使您可以根据组件的用途灵活地选择在何处渲染组件，而不是在客户端渲染整个应用程序（例如在单页应用程序的情况下）。

![[assets/img/Next.js/IMG-Next.js-20240502184325613.webp]]

If we were to split the page into smaller components, you'll notice that the majority of components are <font color="#92d050">non-interactive and can be rendered on the server as Server Components.</font> For smaller pieces of interactive UI, we can _sprinkle in_ Client Components. This aligns with Next.js server-first approach.

Server Components allow developers to better leverage server infrastructure. For example,<font color="#d831a8"> you can move data fetching to the server, closer to your database, and keep large dependencies that previously would impact the client JavaScript bundle size on the server</font>, leading to improved performance.

With Server Components, the initial page load is faster, and the client-side JavaScript bundle size is reduced. The base client-side runtime is **cacheable** and **predictable** in size, and does _not_ increase as your application grows. <font color="#d831a8">Additional JavaScript is _only added_ as client-side interactivity is used in your application through Client Components</font>

To make the transition to Server Components easier, all components inside the [App Router](https://nextjs.org/docs/app/building-your-application/routing#the-app-router) are <font color="#d831a8">Server Components by default</font>, including [special files](https://nextjs.org/docs/app/building-your-application/routing#file-conventions) and [colocated components](https://nextjs.org/docs/app/building-your-application/routing#colocation). This allows you to automatically adopt them with no extra work, and achieve great performance out of the box. You can also optionally opt-in to Client Components using the ['use client' directive](https://nextjs.org/docs/getting-started/react-essentials#the-use-client-directive).

### [Client Components 客户组件](https://nextjs.org/docs/getting-started/react-essentials#client-components)

Client Components enable you to add client-side interactivity to your application. In Next.js, they are [pre-rendered](https://nextjs.org/docs/app/building-your-application/rendering#component-level-client-and-server-rendering) on the server and [hydrated](https://nextjs.org/docs/app/building-your-application/rendering#component-level-client-and-server-rendering) on the client. You can think of Client Components as how components in the [Pages Router](https://nextjs.org/docs/pages) have always worked.

#### [The "use client" directive](https://nextjs.org/docs/getting-started/react-essentials#the-use-client-directive)
The [`"use client"` directive](https://github.com/reactjs/rfcs/pull/227) is a convention to declare a boundary between a Server and Client Component module graph.


Once `"use client"` is defined in a file, all other modules imported into it, including child components, are considered part of <font color="#d831a8">the client bundle.</font>

Since Server Components are the default, all components are part of the Server Component module graph unless defined or imported in a module that starts with the `"use client"` directive.

- `"use client"` does **not** need to be defined in every file. The Client module boundary only needs to be defined once, at the "entry point", for all modules imported into it to be considered a Client Component.  
    `"use client"` 不需要在每个文件中定义。客户端模块边界只需在“入口点”定义一次，所有导入其中的模块都将被视为客户端组件。

### [When to use Server and Client Components?](https://nextjs.org/docs/getting-started/react-essentials#when-to-use-server-and-client-components)

To simplify the decision between Server and Client Components, we recommend using Server Components (default in the `app` directory) until you have a use case for a Client Component.

This table summarizes the different use cases for Server and Client Components:

| What do you need to do?                                                            | Server Component | Client Component |
| ---------------------------------------------------------------------------------- |:----------------:|:----------------:|
| Fetch data.                                                                        |        1         |                  |
| Access backend resources (directly)                                                |        1         |                  |
| Keep sensitive information on the server (access tokens, API keys, etc)            |        1         |                  |
| Keep large dependencies on the server / Reduce client-side JavaScript              |        1         |                  |
| Add interactivity and event listeners (`onClick()`, `onChange()`, etc)             |                  |        2         |
| Use State and Lifecycle Effects (`useState()`, `useReducer()`, `useEffect()`, etc) |                  |        2         |
| Use browser-only APIs                                                              |                  |        2         |
| Use custom hooks that depend on state, effects, or browser-only APIs               |                  |        2         |
| Use [React Class components](https://react.dev/reference/react/Component)          |                  |        2         |

##  [图案](https://nextjs.org/docs/getting-started/react-essentials#patterns)

### [将客户端组件移至叶子](https://nextjs.org/docs/getting-started/react-essentials#moving-client-components-to-the-leaves)

为了提高应用程序的性能，我们建议尽可能将客户端组件移动到组件树的叶子。

例如，您可能有一个包含静态元素（例如徽标、链接等）的布局和一个使用状态的交互式搜索栏。

不要将整个布局设置为客户端组件，而是将交互逻辑移至客户端组件（例如 `<SearchBar />` ）并将布局保留为服务器组件。这意味着您不必将布局的所有组件 Javascript 发送到客户端。

//app/layout.tsx
 ```tsx

// SearchBar是一个客户端组件
import SearchBar from './searchbar'
// Logo是一个服务端组件  
import Logo from './logo'
// Layout默认是一个服务端组件
export default function Layout({ children }: { children: React.ReactNode }) {
  return (
    <>
      <nav>
        <Logo /> 
        <SearchBar /> 
      </nav>
      
      <main>{children}</main>
    </>
  )
}
```
这个示例中:
- SearchBar 是一个客户端组件,会在浏览器端渲染
- Logo 是一个服务端组件,会在服务端渲染
- Layout 默认也是一个服务端组件,会在服务端渲染
客户端组件通常包含交互逻辑,需要访问浏览器 API 等,需要在客户端执行。
服务端组件通常只包含展示逻辑,可以在服务端渲染为 HTML 字符串,加快首屏渲染速度。
Layout 作为页面框架,默认也会服务端渲染,但其子组件 SearchBar 会在客户端重新渲染。
Next.js 通过区分组件类型,实现混合服务器端渲染和客户端渲染,以融合两者优点。
 ```jsx
// TypeScript类型定义
export default function Layout({ children }: { children: React.ReactNode }) {
  // 函数实现
  return (
    <>
      <header>
        // 头部导航
      </header>
      <main>
        {children} 
      </main>
      <footer>
        // 页脚
      </footer>
    </>
  )
}
```
这是一个使用TypeScript类型定义的Layout组件示例。
`children` props被指定为`React.ReactNode`类型,这意味着`children`可以传入任意合法的React节点。
组件返回一个Fragment,包含通用页面的header、main、footer布局结构。
`main`部分渲染`children`传递进来的页面内容。
这样就可以传入任意页面内容到Layout中,实现一个通用的页面框架结构。
TypeScript类型定义让组件API一目了然,很好地结合了TypeScript静态类型系统的优势。
 你问的非常好,两个 children 确实有细微区别:
```jsx
export default function Layout({ children }: { children: React.ReactNode })
```
这里的 `{ children }` 是函数参数的解构赋值语法。它表示该函数接收一个名为 `children` 的参数。
`: { children: React.ReactNode }` 是 TypeScript 的类型注解语法,用于指明 `children` 参数的类型为 `React.ReactNode`。
也就是说:
- `{ children }` 是函数参数,表示实际传入的 `children` 值。
- `{ children: React.ReactNode }` 是类型注解,表示 `children` 参数的期望类型。
函数参数和类型注解中的 `children` 看上去一样,但含义不同:
- 前者是实际的值
- 后者是类型
这在 TypeScript 中是很常见的用法,用于参数和类型的对应。
所以两个 `children` 虽然写法相似,但代表的意义不同,一个是真实值,一个是类型。

#### [组合客户端和服务器组件](https://nextjs.org/docs/getting-started/react-essentials#composing-client-and-server-components)

服务器和客户端组件可以组合在同一组件树中。

在幕后，React 按如下方式处理渲染：

- 在服务器上，React 在将结果发送到客户端之前渲染所有服务器组件。
    - 这包括嵌套在客户端组件内的服务器组件。
    - 跳过此阶段遇到的客户端组件。
- 在客户端，React 渲染客户端组件并插入服务器组件的渲染结果中，合并服务器和客户端上完成的工作。
    - 如果任何服务器组件嵌套在客户端组件内，则它们呈现的内容将正确放置在客户端组件内。

> 值得注意的是：在 Next.js 中，在初始页面加载期间，上述步骤中服务器组件和客户端组件的渲染结果都以 HTML 形式在服务器上预渲染，以产生更快的初始页面加载。

### [将服务器组件嵌套在客户端组件内](https://nextjs.org/docs/getting-started/react-essentials#nesting-server-components-inside-client-components)
#### [不支持的模式：将服务器组件导入客户端组件](https://nextjs.org/docs/getting-started/react-essentials#unsupported-pattern-importing-server-components-into-client-components)

#### [推荐模式：将服务器组件作为 Props 传递给客户端组件](https://nextjs.org/docs/getting-started/react-essentials#recommended-pattern-passing-server-components-to-client-components-as-props)

相反，在设计客户端组件时，您可以使用 React props 来标记服务器组件的“槽”。

Server Component会在服务端渲染，当Client Component在客户端渲染时，“slot”就会被Server Component的渲染结果填充。
一种常见的模式是使用 React `children` 属性来创建“槽”。我们可以重构 `<ExampleClientComponent>` 以接受通用 `children` 属性，并将 `<ExampleClientComponent>` 的导入和显式嵌套移至父组件。

```tsx
// app/example-client-component.tsx
'use client'
import { useState } from 'react'
 
export default function ExampleClientComponent({
  children,
}: {
  children: React.ReactNode
}) {
  const [count, setCount] = useState(0)
 
  return (
    <>
      <button onClick={() => setCount(count + 1)}>{count}</button>
      {children}
    </>
  )
}
```
现在， `<ExampleClientComponent>` 不知道 `children` 是什么。它不知道 `children` 最终将由服务器组件的结果填充。

`ExampleClientComponent` 唯一的责任是决定 `children` 最终放置的位置。

在父服务器组件中，您可以导入 `<ExampleClientComponent>` 和`<ExampleServerComponent>` 并将 `<ExampleServerComponent>` 作为 `<ExampleClientComponent>` 的子组件传递：

```tsx
// app/page.tsx
// This pattern works:
// You can pass a Server Component as a child or prop of a
// Client Component.
import ExampleClientComponent from './example-client-component'
import ExampleServerComponent from './example-server-component'
 
// Pages in Next.js are Server Components by default
export default function Page() {
  return (
    <ExampleClientComponent>
      <ExampleServerComponent />
    </ExampleClientComponent>
  )
}
```

###  [数据获取](https://nextjs.org/docs/getting-started/react-essentials#data-fetching)

虽然可以在客户端组件中获取数据，但我们建议在服务器组件中获取数据，除非您有在客户端上获取数据的特定原因。将数据获取转移到服务器可以带来更好的性能和用户体验。

###  [第三方包](https://nextjs.org/docs/getting-started/react-essentials#third-party-packages)

由于服务器组件是新的，生态系统中的第三方包刚刚开始将 `"use client"` 指令添加到使用仅客户端功能的组件，例如 `useState` 、 `useEffect` 和 `createContext` 。

 ```jsx
'use client'
import { useState } from 'react'
import { Carousel } from 'acme-carousel'
export default function Gallery() {
  let [isOpen, setIsOpen] = useState(false)
  return (
    <div>
      <button onClick={() => setIsOpen(true)}>View pictures</button>
      {/* 适用于客户端组件内使用 Carousel */}  
      {isOpen && <Carousel />}
    </div>
  )
}
```
这个组件使用了 `'use client'` 指令,表示它是一个客户端组件。
在客户端组件中,可以放心使用其他客户端组件,比如这里的 `<Carousel />`。
因为客户端组件只在浏览器中渲染执行,可以安全地使用浏览器 API 或其他需要运行在客户端的代码。
而服务器组件在构建时会执行,不能使用客户端组件或浏览器 API。
Next.js 通过区分组件类型,实现混合服务端渲染和客户端渲染。`'use client'` 使得组件明确运行在客户端,可以避免很多潜在问题。
所以在 Next.js 中,要根据组件功能和需要选择合适的组件类型,从而发挥 Next.js 的最大优势。
 您问得好,Carousel 是一个常见的网页组件,用来展示图片或卡片的轮播图。
在这个例子中,Carousel 是一个假定的第三方组件库中的组件,用于展示图片轮播图。
Carousel 需要访问浏览器的 DOM 和其他 API 来实现轮播效果,所以它是一个客户端组件,只能在浏览器中使用。
如果在服务端渲染的组件中直接使用 Carousel,会导致错误。
而这个组件使用了 `'use client'` 指令,明确说明它是一个客户端组件。
所以在这个客户端组件中,可以放心导入和使用 Carousel 组件,不必担心服务端渲染的问题。
总结一下:
- Carousel 是用于图片轮播的组件
- 它必须运行在浏览器中,是客户端组件
- 本例中通过 `'use client'` 指定是一个客户端组件
- 所以可以在这个组件中安全使用 Carousel
这体现了 Next.js 通过区分组件类型来实现混合服务器端渲染和客户端渲染的思想。
 好的,下面是一个使用 React 实现 Carousel 组件的示例代码:
```jsx
// Carousel.js

import { useState, useRef, useEffect } from 'react';

function Carousel({ children, autoPlay = false, interval = 3000 }) {

  const [activeIndex, setActiveIndex] = useState(0);
  const [paused, setPaused] = useState(!autoPlay);

  const slidesRef = useRef(null);
  const prevButtonRef = useRef();
  const nextButtonRef = useRef();

  useEffect(() => {
    const interval = setInterval(() => {
      if (!paused) {
        handleNextClick();
      }
    }, interval);
    return () => clearInterval(interval);
  });

  function handlePrevClick() {
    if (activeIndex > 0) {
      setActiveIndex(activeIndex - 1);
    }
  }

  function handleNextClick() { 
    if (activeIndex < children.length - 1) {
      setActiveIndex(activeIndex + 1);
    }
  }

  return (
    <div className="carousel">
      <button ref={prevButtonRef} onClick={handlePrevClick}>Prev</button>
      
      <div ref={slidesRef} className="carousel-slides">
        {children.map((child, index) => (
          <div 
            className={index === activeIndex ? 'active' : ''}
            key={index}
          >
            {child}  
          </div>
        ))}
      </div>

      <button ref={nextButtonRef} onClick={handleNextClick}>Next</button>
    </div>
  );
}

export default Carousel;

```
主要特点:
- 用 state 管理当前激活的图片索引
- 用 ref 获取下一张、上一张按钮的引用
- 点击按钮时改变 activeIndex,切换图片
- 用 className 区分轮播图区域和按钮
这只是一个简单示例,实际组件还需要实现自动轮播、过渡动画、图片懒加载等功能。
但基本结构是获取激活索引、切换图片、样式区分等。可以根据需要进行扩展。
主要添加了:
- autoPlay、interval 参数
- useEffect 实现自动轮播
- slidesRef 获取轮播内容区域
- active 类名控制当前显示的图片
- 限制索引不能超出范围
这样 Carousel 的基础功能就基本实现了。后续可以继续优化体验。
 这段Carousel组件代码的实现逻辑是:
1. 使用useState管理当前展示的图片索引activeIndex,初始化为0,即第一张图片。
2. 使用useRef获取下一张、上一张按钮的引用,以及图片内容区域的引用。
3. 使用useEffect注册一个interval,基于传入的autoPlay和interval参数来决定是否自动轮播,以及轮播间隔时间。
4. handlePrevClick函数在点击上一张按钮时,如果索引不为0,则减少索引展示上一张。
5. handleNextClick函数在点击下一张按钮时,如果索引不为最后一张,则索引加1展示下一张。
6. 返回的JSX中,通过数组map方法循环渲染图片内容,如果索引等于activeIndex,则添加active类名用于控制显示样式。
7. 点击上一张/下一张按钮时,调用相应的handle函数切换索引、图片。
8. 通过className区分轮播图区域和按钮样式。
9. 通过useRef、useState、useEffect组合实现轮播逻辑和效果。
10. 支持自定制自动轮播、轮播间隔等功能。
这样通过管理currentIndex状态,配合条件渲染和样式控制,即可实现一个图片轮播的基本结构和交互。后续可进行功能扩展,提升体验。
#### 后续优化和功能扩展

 好的,我们可以对Carousel组件进行一些功能扩展和优化:
1. 添加过渡动画
可以在图片切换时添加淡入淡出等CSS过渡或动画,提升视觉效果。
2. 懒加载图片
只加载可视区域内的图片,其他图片滚动到可视区时再加载,加快初始化速度。
3. 自动播放控制
添加播放/暂停按钮,控制自动轮播的开始和停止。
4. 指示器导航
添加小点作为指示器,显示当前图片的索引,点击可快速切换。 
5. 无限循环
修改切换逻辑,使图片索引超过两端时循环显示,实现无限循环效果。
6. 自动调整轮播速度
根据图片数量自动调整轮播间隔时间,避免轮播过快或过慢。
7. 多种切换模式
支持常用的滑动切换、渐隐渐显切换等多种模式。
8. 可配置化
轮播相关的参数支持配置化,而不是硬编码在组件内。
9. TypeScript重构
使用TypeScript可改善代码质量和健壮性。
10. 测试
编写单元测试和集成测试,确保组件稳定可靠。
以上是一些可以考虑的优化方向,使Carousel组件成为一个健壮、可配置、高性能的组件。

 好的,针对之前的讨论,我尝试给出一些优化后的Carousel组件代码示例:
```tsx
// Carousel.tsx
import { useState, useRef, useEffect } from 'react';
// 定义组件接受的props类型
interface Props {
  images: string[]; // 图片地址数组
  autoPlay?: boolean; // 是否自动轮播
  interval?: number; // 自动轮播时间间隔
} 
// 接收props
function Carousel({images, autoPlay = false, interval = 5000}: Props) {
  // 当前展示图片的索引
  const [activeIndex, setActiveIndex] = useState(0);
  // 获取滑块容器dom元素
  const slidesRef = useRef<HTMLDivElement>(null);
  // 自动轮播逻辑
  useEffect(() => {
    // 计时器句柄
    let timer: number;
    if(autoPlay) {
      // 开启自动轮播
      timer = setInterval(() => {
        handleNextClick(); // 每interval触发下一张
      }, interval);
    }
    // 组件卸载时清除计时器
    return () => clearInterval(timer);
  }, [autoPlay, interval]);
  // 切换到下一张
  function handleNextClick() {
    // 实现无限循环
    setActiveIndex(prev => 
      prev < images.length - 1 ? prev + 1 : 0
    );
  }
  return (
    <div className="carousel">
      // 指示器按钮 
      <div className="indicators">
        {images.map((_, index) =>
          <button
            className={activeIndex === index ? 'active' : ''}
            onClick={() => setActiveIndex(index)}  
          />
        )}
      </div>
      // 轮播滑块
      <div ref={slidesRef} className="slides">
        {images.map((src, index) => (
          <div
            key={src} 
            className={index === activeIndex ? 'slide active' : 'slide'}  
          >
            <img src={src} />
          </div>
        ))}
      </div>
    </div>
  );
}
export default Carousel;
```
详细的注释可以让其他开发者更容易理解组件的逻辑和设计。提高组件代码的可读性和可维护性。
```
主要改进:
- TypeScript 静态类型
- images、interval 等参数化 
- 无限循环的切换逻辑
- 指示器导航区
- CSS类控制滑块切换动画
可以继续丰富功能和测试等。但这展示了一些改进方向,使组件更强大、可定制和健壮。
```

|Feature|Description|
|---|---|
|[Routing](https://nextjs.org/docs/app/building-your-application/routing)|A file-system based router built on top of Server Components that supports layouts, nested routing, loading states, error handling, and more.|
|[Rendering](https://nextjs.org/docs/app/building-your-application/rendering)|Client-side and Server-side Rendering with Client and Server Components. Further optimized with Static and Dynamic Rendering on the server with Next.js. Streaming on Edge and Node.js runtimes.|
|[Data Fetching](https://nextjs.org/docs/app/building-your-application/data-fetching)|Simplified data fetching with async/await in Server Components, and an extended `fetch` API for request memoization, data caching and revalidation.|
|[Styling](https://nextjs.org/docs/app/building-your-application/styling)|Support for your preferred styling methods, including CSS Modules, Tailwind CSS, and CSS-in-JS|
|[Optimizations](https://nextjs.org/docs/app/building-your-application/optimizing)|Image, Fonts, and Script Optimizations to improve your application's Core Web Vitals and User Experience.|
|[TypeScript](https://nextjs.org/docs/app/building-your-application/configuring/typescript)|Improved support for TypeScript, with better type checking and more efficient compilation, as well as custom TypeScript Plugin and type checker.|

![[assets/img/Next.js/IMG-Next.js-20240502184325861.png]]
If we were to split the page into smaller components, you'll notice that the majority of components are non-interactive and can be rendered on the server as Server Components. For smaller pieces of interactive UI, we can _sprinkle in_ Client Components. This aligns with Next.js server-first approach.
When a route is loaded with Next.js, the initial HTML is rendered on the server. This HTML is then **progressively enhanced** in the browser, allowing the client to take over the application and add interactivity, by asynchronously loading the Next.js and React client-side runtime.
To make the transition to Server Components easier, all components inside the [App Router](https://nextjs.org/docs/app/building-your-application/routing#the-app-router) are Server Components by default, You can also optionally opt-in to Client Components using the ['use client' directive](https://nextjs.org/docs/getting-started/react-essentials#the-use-client-directive).

|                                                                                                         |                                                                                                                  |
| ------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| [`layout`](https://nextjs.org/docs/app/building-your-application/routing/pages-and-layouts#layouts)     | Shared UI for a segment and its children                                                                         |
| [`page`](https://nextjs.org/docs/app/building-your-application/routing/pages-and-layouts#pages)         | Unique UI of a route and make routes publicly accessible                                                         |
| [`loading`](https://nextjs.org/docs/app/building-your-application/routing/loading-ui-and-streaming)     | Loading UI for a segment and its children                                                                        |
| [`not-found`](https://nextjs.org/docs/app/api-reference/file-conventions/not-found)                     | Not found UI for a segment and its children                                                                      |
| [`error`](https://nextjs.org/docs/app/building-your-application/routing/error-handling)                 | Error UI for a segment and its children                                                                          |
| [`global-error`](https://nextjs.org/docs/app/building-your-application/routing/error-handling)          | Global Error UI                                                                                                  |
| [`route`](https://nextjs.org/docs/app/building-your-application/routing/route-handlers)                 | Server-side API endpoint                                                                                         |
| [`template`](https://nextjs.org/docs/app/building-your-application/routing/pages-and-layouts#templates) | Specialized re-rendered Layout UI                                                                                |
| [`default`](https://nextjs.org/docs/app/api-reference/file-conventions/default)                         | Fallback UI for [Parallel Routes](https://nextjs.org/docs/app/building-your-application/routing/parallel-routes) |





当使用 Next.js 与 React 和 Tailwind CSS 配合使用时，可以按照以下步骤进行配置和实现：
1. 创建一个 Next.js 项目：
```
npx create-next-app my-app
cd my-app
```
2. 安装所需的依赖包：
```
npm install tailwindcss postcss autoprefixer
```
3. 创建并配置 Tailwind CSS：
```
npx tailwindcss init -p
```
这将在项目根目录下创建一个 `tailwind.config.js` 文件。
4. 在 `styles/globals.css` 文件中引入 Tailwind CSS 样式：
```css
@import 'tailwindcss/base';
@import 'tailwindcss/components';
@import 'tailwindcss/utilities';
```
5. 在 `_app.js` 文件中配置全局样式：
```jsx
import '../styles/globals.css';
function MyApp({ Component, pageProps }) {
  return <Component {...pageProps} />;
}
export default MyApp;
```
6. 在页面组件中使用 Tailwind CSS 样式：
```jsx
import React from 'react';
function Home() {
  return (
    <div className="bg-gray-200 p-4">
      <h1 className="text-2xl font-bold">Welcome to Next.js!</h1>
      <p className="text-gray-700 mt-2">This is a sample page.</p>
      <button className="bg-blue-500 text-white px-4 py-2 mt-4">Click me</button>
    </div>
  );
}
export default Home;
```
在上述代码中，我们使用 Tailwind CSS 提供的类名来定义样式。例如，`bg-gray-200` 表示背景颜色为灰色，`text-2xl` 表示文本大小为2倍大，`font-bold` 表示文本加粗，`px-4` 表示水平内边距为4个单位，`py-2` 表示垂直内边距为2个单位，等等。
通过以上配置和代码示例，你可以在 Next.js 中使用 React 和 Tailwind CSS 来创建动态的、具有响应式布局的网页。