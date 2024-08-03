---
date created: 2024-08-03 10:12
---

Web应用大致分两种,带视图的传统Web应用和面向API接口的应用.

1. 带视图的传统Web应用：这种类型的Web应用通常以页面为中心，用于向用户展示信息和提供交互功能。它使用服务器端渲染（Server-side Rendering，SSR）的方式生成页面，并将页面作为响应返回给客户端。这类应用使用HTML、CSS和JavaScript来构建界面，页面通常由多个视图（View）组成，通过用户与页面的交互来实现功能。用户在浏览器中直接访问页面，与服务器进行交互。
2. 面向API接口的应用：这种类型的Web应用侧重于数据的传输和处理，通过暴露API接口供客户端调用。它通常使用客户端渲染（Client-side Rendering，CSR）的方式，将数据以JSON或其他数据格式返回给客户端，由客户端使用JavaScript来处理数据和构建界面。这类应用的前端通常是一个单页应用（Single-Page Application, SPA），通过AJAX或其他方式与后端API进行交互，实现动态加载数据和更新界面。

这两种类型的Web应用各有优势和适用场景。传统Web应用适用于需要在服务器端生成页面、对SEO友好、功能较为简单的场景。

面向API接口的应用适用于需要更高的前端交互性、更好的用户体验、更灵活的数据处理和展示的场景。

近年来，随着前端技术的发展和API的普及，面向API接口的应用越来越流行，并且与传统Web应用相比，它们更具灵活性和可扩展性。不过在实际开发中，也有很多应用将传统Web应用和面向API接口的应用结合起来，以达到更好的用户体验和功能需求。

JSONP（JSON with Padding）是一种用于解决跨域请求的方法之一，特别适用于在浏览器中进行跨域数据获取的场景。但并不是最通用的跨域解决方案，而是一种特定的技术。
JSONP利用了HTML中`<script>`标签的src属性可以跨域加载资源的特性。它通过动态创建`<script>`标签，将请求数据的回调函数作为参数传递给服务端，服务端在返回数据时将数据包裹在回调函数中返回。这样，浏览器可以通过回调函数获取到数据并进行处理。
然而，JSONP也存在一些限制和安全性的考虑：

1. 只支持GET请求：由于JSONP是通过动态创建`<script>`标签来获取数据，因此只能发送GET请求，无法支持其他请求方法（如POST、PUT等）。
2. 安全性问题：JSONP存在安全风险，因为它依赖于服务端返回的代码执行在客户端。如果服务端返回的数据中包含恶意代码，可能会导致安全漏洞。
3. 仅适用于跨域获取数据：JSONP适用于在不同域之间获取数据，但不适用于进行其他类型的跨域请求（如XMLHttpRequest）。

现在，随着浏览器的发展和Web标准的演进，CORS（Cross-Origin Resource Sharing，跨域资源共享）成为了更为通用和安全的跨域解决方案。CORS通过在服务端设置响应头来允许跨域请求，使得客户端可以直接发送跨域请求，无需依赖JSONP等技术。CORS支持各种请求方法，并提供了更细粒度的安全控制。
总结而言，虽然JSONP是一种在浏览器中进行跨域数据获取的方法，但不是最通用的跨域解决方案。<mark class="hltr-pink">在现代Web开发中，CORS已经成为更为常用和推荐的跨域解决方案，可以更灵活和安全地处理跨域请求。</mark>

以下是使用CORS解决跨域问题的示例代码：
在服务端（例如使用Express框架）设置CORS头来允许跨域请求：

```javascript
const express = require('express');
const app = express();
// 允许所有源发起的跨域请求
app.use((req, res, next) => {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type, Authorization');
  next();
});
// 处理跨域请求的路由
app.get('/api/data', (req, res) => {
  // 处理请求并返回数据
  res.json({ message: 'Data from API' });
});
app.listen(3000, () => {
  console.log('Server started on port 3000');
});
```

在客户端（例如使用JavaScript进行AJAX请求）发送跨域请求：

```javascript
fetch('http://localhost:3000/api/data')
  .then(response => response.json())
  .then(data => {
    console.log(data);
  })
  .catch(error => {
    console.error(error);
  });
```

Node.js支持多种异步方案，以下是一些常见的异步方案：

1. 回调函数（Callback）：在Node.js中，回调函数是最常见的异步编程模式。通过将一个函数作为参数传递给异步函数，当异步操作完成时，将会调用该回调函数来处理结果。

```javascript
asyncFunction(arg1, arg2, (error, result) => {
  if (error) {
    // 处理错误
  } else {
    // 处理结果
  }
});
```

2. Promise：Promise是一种用于处理异步操作的对象。它代表一个还未完成但最终会完成的操作，并可以通过链式调用`then`和`catch`方法来处理成功或失败的结果。

```javascript
asyncFunction(arg1, arg2)
  .then((result) => {
    // 处理结果
  })
  .catch((error) => {
    // 处理错误
  });
```

3. async/await：async/await是ES2017引入的一种异步编程模式，它基于Promise，并提供了更简洁的语法来处理异步操作。通过在异步函数前加上`async`关键字，可以在函数内部使用`await`关键字来等待异步操作的结果。

```javascript
async function myFunction() {
  try {
    const result = await asyncFunction(arg1, arg2);
    // 处理结果
  } catch (error) {
    // 处理错误
  }
}
```

4. 事件（EventEmitter）：Node.js内置的事件模块（EventEmitter）可以用于实现事件驱动的异步编程。通过定义事件和监听器，可以在异步操作完成时触发相应的事件，并通过监听器处理结果。

```javascript
const EventEmitter = require('events');
const emitter = new EventEmitter();
emitter.on('result', (result) => {
  // 处理结果
});
asyncFunction(arg1, arg2, (error, result) => {
  if (error) {
    // 处理错误
  } else {
    emitter.emit('result', result);
  }
});
```
