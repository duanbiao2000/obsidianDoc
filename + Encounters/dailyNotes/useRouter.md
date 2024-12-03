---
aliases: 
theme: 
original: 
url: 
author: 
date_created: 
date_update: 
type: 
priority: false
---

## next/router 与 next/navigation 中 useRouter 的深入对比

在 Next.js 中，`useRouter` 这个 Hook 虽然名称相同，但在 `next/router` 和 `next/navigation` 中的用法和功能却存在一些细微但重要的区别，这主要是因为 Next.js 13 引入了新的 App Router 架构。

### 1. 版本兼容性

- **next/router:** 主要用于 Next.js 13 之前的版本，即传统的 Pages Router。
- **next/navigation:** 专为 Next.js 13 及更高版本设计，与 App Router 深度集成。(新)

### 2. 功能差异

| 特性                   | next/router         | next/navigation                            |
| -------------------- | ------------------- | ------------------------------------------ |
| **导航方法**             | push, replace, back | navigate                                   |
| **数据获取**             | getInitialProps     | 使用 `getServerSideProps` 或 `getStaticProps` |
| **路由参数**             | query 对象            | useSearchParams、usePathname                |
| **类型安全**             | 相对较弱                | 更强，提供更好的类型推断                               |
| **与 App Router 的集成** | 未集成                 | 深度集成，支持嵌套路由、布局等                            |
| **其他功能**             | pathname, asPath    | usePathname                                |

### 3. 使用场景

- **next/router:**
  - 适用于 Next.js 13 之前的项目。
  - 对于简单的路由操作，如页面跳转、参数传递等。
- **next/navigation:**
  - 适用于 Next.js 13 及更高版本。
  - 需要利用 App Router 的高级特性，如数据获取、嵌套路由、布局等。
  - 需要更精细的路由控制。

### 4. 示例

```js
// next/router (传统方式)
import { useRouter } from 'next/router';

const MyComponent = () => {
  const router = useRouter();

  const handleClick = () => {
    router.push('/about?id=123'); // 跳转到 /about 页面，并传递 id 参数
  };

  // ...
};

// next/navigation (App Router)
import { useRouter, useSearchParams } from 'next/navigation';

const MyComponent = () => {
  const router = useRouter();
  const searchParams = useSearchParams();

  const handleClick = () => {
    router.navigate('/products/[productId]', { params: { productId: 123 } }); // 嵌套路由，动态路由
  };

  return (
    <div>
      <p>当前产品 ID：{searchParams.get('productId')}</p>
      <button onClick={handleClick}>查看产品详情</button>
    </div>
  );
};
```

### 5. 注意事项

- **数据获取:** 在 App Router 中，数据获取主要通过 `getServerSideProps` 或 `getStaticProps` 进行。
- **类型安全性:** `next/navigation` 提供了更强的类型安全性，可以帮助你避免一些常见的错误。
- **嵌套路由:** `next/navigation` 可以更好地支持嵌套路由，使得路由结构更加清晰。
- **性能:** `next/navigation` 在某些场景下可能会有更好的性能表现。

### 总结

**next/navigation** 是 `next/router` 的升级版，它更适合 Next.js 13 及更高版本，提供了更丰富的功能和更好的开发体验。如果你正在开发新的 Next.js 项目，强烈建议使用 `next/navigation`。

**选择哪个 Hook 应该根据你的项目需求和 Next.js 版本来决定。**

**其他注意事项:**

- **useRouter** 只能在客户端组件中使用。
- **App Router** 引入了许多新的概念和特性，建议仔细阅读官方文档。
- **迁移:** 从 `next/router` 迁移到 `next/navigation` 可能需要对代码进行一些调整。



[[Clerk身份验证]]

[[TypeScript React Query]]
