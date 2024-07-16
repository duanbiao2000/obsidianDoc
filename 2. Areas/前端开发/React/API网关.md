以下是一个简单的Express框架下使用API网关的示例代码：
首先，安装必要的依赖包：
```bash
npm install express body-parser
```
然后，创建一个Express应用，设置API网关的路由和功能：
```javascript
const express = require('express');
const bodyParser = require('body-parser');
const app = express();
app.use(bodyParser.json());
// API网关路由
app.get('/api/users', (req, res) => {
  // 处理用户列表请求
  // ...
});
app.post('/api/users', (req, res) => {
  // 处理创建用户请求
  // ...
});
app.put('/api/users/:id', (req, res) => {
  // 处理更新用户请求
  // ...
});
app.delete('/api/users/:id', (req, res) => {
  // 处理删除用户请求
  // ...
});
// 启动服务器
app.listen(3000, () => {
  console.log('API Gateway server started on port 3000');
});
```
