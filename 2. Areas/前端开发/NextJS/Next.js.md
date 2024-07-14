

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


##  [图案](https://nextjs.org/docs/getting-started/react-essentials#patterns)

### [将客户端组件移至叶子](https://nextjs.org/docs/getting-started/react-essentials#moving-client-components-to-the-leaves)

为了提高应用程序的性能，我们建议尽可能将客户端组件移动到组件树的叶子。

例如，您可能有一个包含静态元素（例如徽标、链接等）的布局和一个使用状态的交互式搜索栏。

不要将整个布局设置为客户端组件，而是将交互逻辑移至客户端组件（例如 `<SearchBar />` ）并将布局保留为服务器组件。这意味着您不必将布局的所有组件 JavaScript 发送到客户端。

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


