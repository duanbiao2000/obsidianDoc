### Nodejs关键技术:

请具体给出nodejs 以及 express 关键技术和对象, 函数的说明以及示例

Node.js 是一个基于 Chrome V8 引擎的 JavaScript 运行时环境。它使得开发者可以使用 JavaScript 编写服务器端应用程序。

Express 是一个基于 Node.js 的 web 应用框架，它简化了 Node.js web 应用的开发过程。

以下是一些 Node.js 和 Express 中关键技术、对象和函数的说明及示例：

1. Node.js 使用 `require` 函数来导入模块。

   示例：
   ```javascript
   const express = require('express'); // 导入 Express 模块
   ```

2. Node.js 使用 `module.exports` 和 `exports` 对象来暴露模块的公共接口。

   示例：
   ```javascript
   // greet.js
   function greet(name) {
     console.log(`Hello, ${name}!`);
   }

   module.exports = { greet }; // 暴露 greet 函数

   // app.js
   const { greet } = require('./greet'); // 导入 greet 函数
   greet('World');
   ```

3. `http.Server` 类：Node.js 内置了一个 `http` 模块，其中包含一个 `Server` 类，用于创建 HTTP 服务器实例。

   示例：
   ```javascript
   const http = require('http');

   const server = http.createServer((req, res) => {
     res.writeHead(200, { 'Content-Type': 'text/plain' });
     res.end('Hello, World!');
   });

   server.listen(3000, () => console.log('Server is listening on port 3000'));
   ```

4. 通过 `express()` 函数创建一个 Express 应用实例。

   示例：
   ```javascript
   const express = require('express');
   const app = express();
   ```

5. Express 提供了一种简洁的方式来处理不同的 HTTP 请求方法和 URL 路径。

   示例：
   ```javascript
   const express = require('express');
   const app = express();

   app.get('/', (req, res) => {
     res.send('Hello, World!');
   });

   app.listen(3000, () => console.log('Server is listening on port 3000'));
   ```

6. 中间件（Middleware）：在 Express 中，中间件是一种处理请求和响应的函数。它们可以对请求和响应进行修改，并控制执行流程。

   示例：
   ```javascript
   const express = require('express');
   const app = express();

   const loggerMiddleware = (req, res, next) => {
     console.log(`${new Date().toISOString()} - ${req.method} ${req.url}`);
     next();
   };

   app.use(loggerMiddleware);
   app.get('/', (req, res) => {
     res.send('Hello, World!');
   });

   app.listen(3000, () => console.log('Server is listening on port 3000'));
   ```

7. 请求（Request）对象：在路由处理器和中间件中，`req` 参数表示请求对象，包含与客户端发送的 HTTP 请求相关的信息。

   示例：
   ```javascript
   app.get('/greet', (req, res) => {
     const name = req.query.name || 'World';
     res.send(`Hello, ${name}!`);
   });
   ```

8. 响应（Response）对象：在路由处理器和中间件中，`res` 参数表示响应对象，包含与服务器端发送的 HTTP 响应相关的信息。

   示例：
   ```javascript
   app.get('/', (req, res) => {
     res.status(200).send('Hello, World!');
   });
   ```

