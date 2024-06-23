---
aliases: 
tags:
---


后端API开发参照静态API进行具体实现,数据库建模,API封装即可.

静态API实现的方式: 比如Express,Koa .  也可以采用专门的静态API框架实现,比如著名的typicode/json-server,想实现REST API, 只需要编辑db.json,然后放入数据即可.


平台工具: Electron(跨平台打包工具)
构建系统: Grunt Gulp Webpack NPM Script
模块打包器:Browserify, Webpack
生成器: vue-cli, create-react-app
模板引擎:Jade
`请注意，Jade 已经在 2016 年更名为 Pug，以避免与 Ruby 的 Jade 库发生冲突。但是，许多开发者仍然习惯性地称它为 Jade。`
[[模板引擎]]

推荐两个Electron开源项目

Statcer: Linux系统上的优化和监控软件, 基于Electron构建的
Medis: Redis客户端.  React作为前端框架, Electron作为跨平台打包工具

Gulp是Grunt的替代品: 流式构建,不会产生中间文件, Stream机制,处理大文件和内存有优势,配置简单,只要懂点JavaScript就能搞定.
Webpack+ npm scripts: 说是构建工具有点过, 两者组合勉强是, Loader和Plugin机制还是非常强大的.

后端开发指的是Web应用开发中和视图渲染无关的部分, 主要是以数据库交互为主的重业务型逻辑处理.


[[运行时环境]]

Web应用大致分两种,带视图的传统Web应用和面向API接口的应用.

1. 带视图的传统Web应用：这种类型的Web应用通常以页面为中心，用于向用户展示信息和提供交互功能。它使用服务器端渲染（Server-side Rendering，SSR）的方式生成页面，并将页面作为响应返回给客户端。这类应用使用HTML、CSS和JavaScript来构建界面，页面通常由多个视图（View）组成，通过用户与页面的交互来实现功能。用户在浏览器中直接访问页面，与服务器进行交互。
2. 面向API接口的应用：这种类型的Web应用侧重于数据的传输和处理，通过暴露API接口供客户端调用。它通常使用客户端渲染（Client-side Rendering，CSR）的方式，将数据以JSON或其他数据格式返回给客户端，由客户端使用JavaScript来处理数据和构建界面。这类应用的前端通常是一个单页应用（Single-Page Application，SPA），通过AJAX或其他方式与后端API进行交互，实现动态加载数据和更新界面。

这两种类型的Web应用各有优势和适用场景。传统Web应用适用于需要在服务器端生成页面、对SEO友好、功能较为简单的场景。

面向API接口的应用适用于需要更高的前端交互性、更好的用户体验、更灵活的数据处理和展示的场景。

近年来，随着前端技术的发展和API的普及，面向API接口的应用越来越流行，并且与传统Web应用相比，它们更具灵活性和可扩展性。不过在实际开发中，也有很多应用将传统Web应用和面向API接口的应用结合起来，以达到更好的用户体验和功能需求。

[[API设计模式]]

[[同构|同构:SSR服务端渲染]]

Koa: 专注于异步流程改进: 下一代Web框架
框架选型:保证在出现问题的时候有人能做到源码级定制.

[[API网关]]

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
以上示例代码中，服务端设置了CORS头来允许所有源发起的跨域请求。客户端使用fetch API发送GET请求到服务端的`/api/data`路径，并在控制台中打印响应数据。
请注意，上述示例代码中使用通配符`*`来允许所有源发起的跨域请求。在实际应用中，你可以根据需要配置具体的源（例如指定特定的域名）来进行更精细的跨域控制。此外，还可以设置其他CORS相关的选项，如允许带身份凭证的请求、预检请求（OPTIONS请求）等。
使用CORS解决跨域问题，可以在现代Web开发中更为灵活和安全地处理跨域请求。


NodeJs 应用场景

- 作为基础设施用于前端开发
- 作为命令行辅助工具
- 用于移动端和PC端
- 实现前端组件化,完成组件的打包构建,增加HTTP代理等功能
- 用于架构设计,实现前后端分离
- 性能优化,反爬虫与爬虫
- 实现全栈

`const fs = require('fs')` 是Node.js中用于引入文件系统模块的代码。fs模块是Node.js的核心模块之一，提供了对文件系统进行读写操作的功能。
使用`fs`模块，你可以在Node.js环境中读取、写入、修改和删除文件，以及进行文件夹的操作。以下是一些常见的`fs`模块的使用示例：
1. 读取文件内容：
```javascript
const fs = require('fs');
fs.readFile('file.txt', 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
```
2. 写入文件内容：
```javascript
const fs = require('fs');
const content = 'This is the content that will be written to the file.';
fs.writeFile('file.txt', content, 'utf8', (err) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log('File has been written successfully.');
});
```
3. 创建和删除文件夹：
```javascript
const fs = require('fs');
// 创建文件夹
fs.mkdir('myFolder', (err) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log('Folder created successfully.');
});
// 删除文件夹
fs.rmdir('myFolder', (err) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log('Folder deleted successfully.');
});
```
以上示例演示了`fs`模块的一些常见用法，但还有更多的功能和方法可供使用，如重命名文件、复制文件、监听文件变化等。你可以根据具体需求和场景，查阅Node.js官方文档或相关资源来学习和使用`fs`模块的更多功能。

`ctx.body =`ctx.body` 是Koa框架中用于设置响应体的属性。通过设置`ctx.body`，可以将指定的内容作为响应体发送给客户端。
以下是一个使用Koa框架设置响应体的示例代码：
```javascript
const Koa = require('koa');
const app = new Koa();
app.use(async (ctx) => {
  ctx.body = 'Hello Koa';
});
app.listen(3000, () => {
  console.log('Server started on port 3000');
});
```
在上述示例中，当收到请求时，中间件函数会将`Hello Koa`赋值给`ctx.body`属性。Koa框架会自动将`ctx.body`的内容作为响应体发送给客户端。
请注意，Koa框架中的`ctx.body`属性是对Node.js原生的`res`对象的封装，它提供了更简洁的方式来设置响应体。在实际应用中，你可以根据具体的需求和业务逻辑，动态设置`ctx.body`的内容，并根据需要设置响应的格式、编码等。

下面是对代码块中注释的解释：
```javascript
const fs = require('fs');
const Koa = require('koa');
const app = new Koa();
app.use(ctx => {
  if (ctx.path == '/good') {
    return ctx.body = 'good'; // 如果请求路径是 '/good'，返回响应内容为 'good'
  }
  fs.readFile('somefile.txt', function (err, data) { // 读取文件 'somefile.txt'
    try {
      if (err) throw err; // 如果出现错误，抛出异常
      console.log(data); // 打印文件内容
      ctx.body = 'Hello Koa'; // 将响应内容设置为 'Hello Koa'
    } catch (e) {
      console.log(e); // 捕获异常，并打印错误信息
    } finally {
      console.log('离开 try/catch'); // 无论是否发生异常，都会执行的代码块
    }
  });
});
```
这段代码使用Koa框架处理HTTP请求，并根据请求路径返回相应的内容。如果请求路径是 '/good'，则直接返回 'good'；否则，异步读取文件 'somefile.txt'，如果读取成功，则将文件内容作为响应内容返回；如果读取失败，则会抛出异常，并通过try-catch语句进行捕获，打印错误信息。无论是否发生异常，finally块中的代码都会被执行，并打印 '离开 try/catch'。

PM2 是一个流行的用于管理和监控 Node.js 应用程序的进程管理工具。它提供了许多功能，帮助开发者轻松管理 Node.js 进程，如启动、停止、重启应用程序，以及监控应用程序的状态、日志记录等。
以下是 PM2 的一些常用功能和用法：
1. 启动应用程序：
```bash
pm2 start app.js
```
2. 停止应用程序：
```bash
pm2 stop app
```
3. 重启应用程序：
```bash
pm2 restart app
```
4. 监视应用程序状态：
```bash
pm2 status
```
5. 查看应用程序日志：
```bash
pm2 logs app
```
6. 监控应用程序的 CPU 和内存使用情况：
```bash
pm2 monit
```
PM2 还提供了许多其他功能，如自动重启、负载均衡、集群模式等。它可以通过配置文件进行进一步的定制和扩展，以适应不同的应用场景。
使用 PM2 可以有效地管理和监控 Node.js 应用程序，提高应用程序的稳定性和可靠性。它在生产环境中广泛使用，并被认为是一个强大而实用的工具。

Node.js 被称为单线程，但这并不意味着它不能处理并发操作。这里的“单线程会死”可能是一种误解或过度简化的说法。让我们来详细解释一下。
1. **单线程事件循环**: Node.js 主要使用单线程来执行 JavaScript 代码。这意味着在任何给定时间，只有一个操作在主线程上执行。但是，Node.js 还使用了一个称为事件循环的机制，它允许非阻塞 I/O 操作，如网络请求、文件读取等。
2. **非阻塞 I/O**: Node.js 的非阻塞 I/O 操作允许它在等待某些操作（如读取文件、查询数据库等）完成时继续执行其他任务。这是通过将这些操作委托给底层的系统线程来实现的，从而使主线程能够继续执行其他任务。
3. **线程池**: 尽管 JavaScript 代码在单线程上执行，但 Node.js 还使用了一个线程池来处理一些计算密集型或阻塞的任务。这意味着某些操作可以在后台的多个线程上并行执行。
4. **可扩展性**: 通过使用集群模块，Node.js 可以在多个 CPU 核心上运行多个进程，从而充分利用多核系统的能力。这进一步增强了其并发处理能力。
因此，尽管 Node.js 在执行 JavaScript 代码时使用了单线程模型，但通过事件循环、非阻塞 I/O 和线程池等机制，它能够高效地处理并发操作。所以说 Node.js "单线程会死" 是一种伪命题，可能是对其工作原理的误解或过度简化。

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
以上是一些常见的Node.js异步方案，根据实际情况选择适合的方案来处理异步操作。


异步流程控制是Node.js编程的核心,掌握之后就剩API需要学习了.

![[Pasted image 20230803213630.png]]
![[Pasted image 20230803213850.png]]
`call`和`apply`是JavaScript中用于调用函数的方法，它们的作用是在指定的作用域中调用函数，并可以指定函数的上下文及参数。
`call`和`apply`的区别在于参数的传递方式和接收方式：
- `call`方法接收的参数是一个一个地传递给函数，通过逗号分隔。
- `apply`方法接收的参数是一个数组或类数组对象，通过数组的方式传递。

下面是使用`call`和`apply`的示例：
```javascript
function greet(name) {
  console.log(`Hello, ${name}!`);
}
greet.call(null, 'Alice'); // 输出：Hello, Alice!
greet.apply(null, ['Bob']); // 输出：Hello, Bob!
```
在上面的示例中，`call`和`apply`方法都将`greet`函数在`null`作用域中调用，并传递了一个参数。
同时，`call`和`apply`方法还可以用于改变函数的上下文，即函数内部的`this`指向的对象。例如：
```javascript
const person = {
  name: 'John',
  greet: function() {
    console.log(`Hello, ${this.name}!`);
  }
};
const anotherPerson = {
  name: 'Alice'
};
person.greet.call(anotherPerson); // 输出：Hello, Alice!
person.greet.apply(anotherPerson); // 输出：Hello, Alice!
```
在上面的示例中，`call`和`apply`方法将`person`对象中的`greet`函数在`anotherPerson`对象上下文中调用，从而改变了函数内部的`this`指向。
需要注意的是，如果第一个参数传递为`null`或`undefined`，`call`和`apply`方法将会在全局作用域中调用函数。
不，ES7并没有淘汰`bind`方法的写法。`bind`方法是用于创建一个新函数，并将其绑定到指定的对象上。绑定后的函数将永久地绑定到指定的对象上，无论在哪里调用该函数，它都会以绑定的对象作为上下文。
`bind`方法的写法在ES7中仍然有效，并没有被淘汰。你仍然可以使用`bind`方法来创建绑定函数。
下面是使用`bind`方法的示例：
```javascript
const person = {
  name: 'John',
  greet: function() {
    console.log(`Hello, ${this.name}!`);
  }
};
const greetFunction = person.greet.bind(person);
greetFunction(); // 输出：Hello, John!
```
在上面的示例中，我们使用`bind`方法将`person`对象中的`greet`函数绑定到`person`对象上，并创建了一个新的函数`greetFunction`。当调用`greetFunction`时，它会以`person`对象作为上下文，输出相应的结果。
因此，`bind`方法仍然是一个有用的函数绑定工具，可以在需要时使用它来创建绑定函数。

In JavaScript, the expression `arg !== arg` is a way to check if a value is NaN (Not-a-Number). NaN is a special value in JavaScript that represents an invalid number.
The expression `arg !== arg` will evaluate to `true` when `arg` is NaN, and `false` otherwise. This is because NaN is the only value in JavaScript that is not equal to itself.
Here's an example:
```javascript
const arg = NaN;
console.log(arg !== arg); // Output: true
```
In the above example, `arg` is set to NaN, and the expression `arg !== arg` evaluates to `true` because NaN is not equal to itself.





