---
aliases: 
categories: 
important: false
tags:
---


`@vercel/analytics/react` 是 Vercel 提供的一个轻量级的分析库，用于在 React 应用中添加网站分析功能。它可以帮助你跟踪用户的行为，比如页面访问、点击事件等，而无需集成复杂的第三方分析工具。


```bash
npm install @vercel/analytics
# 或者
yarn add @vercel/analytics
```

安装完成后，你可以将 `Analytics` 组件导入到你的应用中，并将其放置在组件树的顶层，通常是 `App.js` 或 `_app.js`（如果你使用的是 [[Next.js]]）文件中。这样可以确保所有页面和组件都能被正确地跟踪。

下面是一个简单的例子，展示如何在 React 应用中使用 `Analytics` 组件：

1. 在你的 `App.js` 或 `_app.js` 文件中导入 `Analytics` 组件：

   ```javascript
   import { Analytics } from '@vercel/analytics/react';
   ```

2. 将 `Analytics` 组件添加到你的组件树的最外层：

   ```javascript
   function App() {
     return (
       <div>
         {/* 你的其他组件 */}
         <Analytics />
       </div>
     );
   }

   export default App;
   ```

3. 如果你在使用 [[Next.js]]，那么通常你会在 `_app.js` 文件中这样做：

   ```javascript
   import '../styles/globals.css';
   import { Analytics } from '@vercel/analytics/react';

   function MyApp({ Component, pageProps }) {
     return (
       <>
         <Component {...pageProps} />
         <Analytics />
       </>
     );
   }

   export default MyApp;
   ```

通过这种方式，Vercel 的分析服务就会自动开始收集数据了。请注意，为了使分析功能正常工作，你可能需要配置一些环境变量或在 Vercel 控制台中进行设置。具体步骤可以参考 Vercel 官方文档中的相关说明。
