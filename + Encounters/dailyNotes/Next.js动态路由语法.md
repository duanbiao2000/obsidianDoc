---
aliases: 
source: C:\Users\Danny\Documents\Mycodes\React\fractal
author: 
createdAt: 
updateAt: 
type: 
high_priority: false
tags:
---

### [slug] **用法**

在Next.js中，`[slug]`是一种动态路由语法，用于创建动态页面。`[slug]`文件夹中的`page.tsx`文件将根据URL中的动态部分渲染内容。例如：

- `/categories/[slug]/products`：当访问`/categories/electronics/products`时，`[slug]`将被替换为`electronics`，`page.tsx`文件将渲染与`electronics`类别相关的商品页面。
- `/products/[slug]`：当访问`/products/product-name`时，`[slug]`将被替换为`product-name`，`page.tsx`文件将渲染与`product-name`相关的商品详情页面。

这种动态路由方式使得Next.js能够灵活地处理不同URL路径下的内容。

### 可选动态路由

```
sign-in
  └── [[...sign-in]]
      └── page.tsx
```

- [[...sign-in]]是一个可选的动态路由，当访问/sign-in或/sign-in/step1/step2时，sign-in将被替换为[]或['step1', 'step2']，page.tsx文件将渲染相应的登录页面。

### 总结

- ()：用于创建路由组，不影响URL路径。

- []：用于创建动态路由，捕获URL中的特定部分。

- [[...]]：用于创建可选的动态路由，捕获URL中的多个段。

这些符号使得Next.js的路由系统非常灵活，能够满足各种复杂的URL结构需求。
