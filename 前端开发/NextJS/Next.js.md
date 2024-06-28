
##  [主要特点](https://nextjs.org/docs#main-features)

N                                      

## Next.js 项目结构

##  [顶级文件夹](https://nextjs.org/docs/getting-started/project-structure#top-level-folders)

| | |
|---|---|
|[`app`](https://nextjs.org/docs/app/building-your-application/routing)|应用路由|
|[`pages`](https://nextjs.org/docs/pages/building-your-application/routing)|页面路由|
|[`public`](https://nextjs.org/docs/getting-started/installation#the-public-folder-optional)|static assets|
|[`src`](https://nextjs.org/docs/app/building-your-application/configuring/src-directory)|可选的应用程序源文件夹|

## [`app` 路由约定](https://nextjs.org/docs/getting-started/project-structure#app-routing-conventions)

###  [路由文件](https://nextjs.org/docs/getting-started/project-structure#routing-files)

|                                                                                                   |                     |          |
| ------------------------------------------------------------------------------------------------- | ------------------- | -------- |
| [`layout`](https://nextjs.org/docs/app/api-reference/file-conventions/layout)                     | `.js` `.jsx` `.tsx` | 布局       |
| [`page`](https://nextjs.org/docs/app/api-reference/file-conventions/page)                         | `.js` `.jsx` `.tsx` | 页        |
| [`loading`](https://nextjs.org/docs/app/api-reference/file-conventions/loading)                   | `.js` `.jsx` `.tsx` | 加载用户界面   |
| [`not-found`](https://nextjs.org/docs/app/api-reference/file-conventions/not-found)               | `.js` `.jsx` `.tsx` | 未找到用户界面  |
| [`error`](https://nextjs.org/docs/app/api-reference/file-conventions/error)                       | `.js` `.jsx` `.tsx` | 错误用户界面   |
| [`global-error`](https://nextjs.org/docs/app/api-reference/file-conventions/error#global-errorjs) | `.js` `.jsx` `.tsx` | 全局错误用户界面 |
| [`route`](https://nextjs.org/docs/app/api-reference/file-conventions/route)                       | `.js` `.ts`         | API端点    |
| [`template`](https://nextjs.org/docs/app/api-reference/file-conventions/template)                 | `.js` `.jsx` `.tsx` | 重新渲染布局   |
| [`default`](https://nextjs.org/docs/app/api-reference/file-conventions/default)                   | `.js` `.jsx` `.tsx` | 并行路由默认页面 |

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

|                                                                                                                                   |                                     |             |
| --------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------- | ----------- |
| [`favicon`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons#favicon)                                | `.ico`                              | 文件图标        |
| [`icon`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons#icon)                                      | `.ico` `.jpg` `.jpeg` `.png` `.svg` | 应用程序图标文件    |
| [`icon`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons#generate-icons-using-code-js-ts-tsx)       | `.js` `.ts` `.tsx`                  | 生成的应用程序图标   |
| [`apple-icon`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons#apple-icon)                          | `.jpg` `.jpeg` , `.png`             | 苹果应用程序图标文件  |
| [`apple-icon`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons#generate-icons-using-code-js-ts-tsx) | `.js` `.ts` `.tsx`                  | 生成的苹果应用程序图标 |

#### [打开图谱和 Twitter 图片](https://nextjs.org/docs/getting-started/project-structure#open-graph-and-twitter-images)

|                                                                                                                                               |                              |                   |
| --------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------- | ----------------- |
| [`opengraph-image`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image#opengraph-image)                      | `.jpg` `.jpeg` `.png` `.gif` | 打开图形图像文件          |
| [`opengraph-image`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image#generate-images-using-code-js-ts-tsx) | `.js` `.ts` `.tsx`           | 生成的 Open Graph 图像 |
| [`twitter-image`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image#twitter-image)                          | `.jpg` `.jpeg` `.png` `.gif` | 推特图像文件            |
| [`twitter-image`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image#generate-images-using-code-js-ts-tsx)   | `.js` `.ts` `.tsx`           | 生成的 Twitter 图片    |


#### [SEO](https://nextjs.org/docs/getting-started/project-structure#seo)

| | | |
|---|---|---|
|[`sitemap`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/sitemap#static-sitemapxml)|`.xml`|站点地图文件|
|[`sitemap`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/sitemap#generate-a-sitemap)|`.js` `.ts`|生成的站点地图|
|[`robots`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/robots#static-robotstxt)|`.txt`|机器人文件|
|[`robots`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/robots#generate-a-robots-file)|`.js` `.ts`|生成的机器人文件|

## [`pages` 路由约定](https://nextjs.org/docs/getting-started/project-structure#pages-routing-conventions)

###  [特殊文件](https://nextjs.org/docs/getting-started/project-structure#special-files)

| | | |
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

 这段Carousel组件代码的实现逻辑是:
1. 使用useState管理当前展示的图片索引activeIndex,初始化为0,即第一张图片。
<font color="#ff0000">2. 使用useRef获取下一张、上一张按钮的引用,以及图片内容区域的引用。</font>
3. 使用useEffect注册一个interval,基于传入的autoPlay和interval参数来决定是否自动轮播,以及轮播间隔时间。
4. handlePrevClick函数在点击上一张按钮时,如果索引不为0,则减少索引展示上一张。
5. handleNextClick函数在点击下一张按钮时,如果索引不为最后一张,则索引加1展示下一张。
6. 返回的JSX中,通过数组map方法循环渲染图片内容,如果索引等于activeIndex,则添加active类名用于控制显示样式。
7. 点击上一张/下一张按钮时,调用相应的handle函数切换索引、图片。
8. 通过className区分轮播图区域和按钮样式。
9. 通过useRef、useState、useEffect组合实现轮播逻辑和效果。
10. 支持自定制自动轮播、轮播间隔等功能。
这样通过管理currentIndex状态,配合条件渲染和样式控制,即可实现一个图片轮播的基本结构和交互。后续可进行功能扩展,提升体验。



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