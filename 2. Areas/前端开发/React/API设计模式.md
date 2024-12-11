

Node.js框架示例：
1. Express框架的路由模式示例：
```javascript
const express = require('express');
const app = express();
// 获取用户列表数据
app.get('/users', (req, res) => {
    // 处理请求，发送用户列表数据给客户端
    // ...
});
// 创建新用户
app.post('/users', (req, res) => {
    // 处理请求，创建新用户并返回结果给客户端
    // ...
});
// 更新用户信息
app.put('/users/:id', (req, res) => {
    const userId = req.params.id;
    // 处理请求，根据用户ID更新用户信息并返回结果给客户端
    // ...
});
// 删除用户
app.delete('/users/:id', (req, res) => {
    const userId = req.params.id;
    // 处理请求，根据用户ID删除用户并返回结果给客户端
    // ...
});
app.listen(3000, () => {
    console.log('Server started on port 3000');
});
```
2. Koa框架的中间件模式示例：
```javascript
const Koa = require('koa');
const app = new Koa();
// 日志中间件
app.use(async (ctx, next) => {
    console.log(`${ctx.method} ${ctx.url}`);
    await next();
});
// 路由中间件
app.use(async (ctx, next) => {
    if (ctx.path === '/users') {
        // 处理用户列表请求
        ctx.body = { message: 'User List' };
    } else if (ctx.path === '/products') {
        // 处理产品列表请求
        ctx.body = { message: 'Product List' };
    } else {
        // 处理其他路由
        ctx.body = { message: 'Not Found' };
    }
    await next();
});
app.listen(3000, () => {
    console.log('Server started on port 3000');
});
```