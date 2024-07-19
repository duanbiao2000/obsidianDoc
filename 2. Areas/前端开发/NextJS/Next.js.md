---
date created: 2024-07-19 18:42
---
## [`app` 路由约定](https://nextjs.org/docs/getting-started/project-structure#app-routing-conventions)

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
