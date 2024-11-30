---
aliases: 
theme: 
priority: false
tags:
---
Mock Service Worker (MSW) 是一个用于前端应用的 API 模拟库。它允许你在开发环境中拦截和模拟网络请求，而无需依赖实际的后端服务。MSW 可以在浏览器、Node.js 以及测试环境中使用，非常适合前端开发中的 API 模拟。

以下是如何使用 MSW 来模拟后端 API 的步骤：

### 1. 安装 MSW

首先，你需要安装 MSW 和它的相关依赖。你可以使用 npm 或 yarn 来安装：

```bash
npm install msw --save-dev
# 或者
yarn add msw --dev
```

### 2. 创建 Mock 服务器

创建一个文件来定义你的 mock 服务器。通常这个文件会放在 `src/mocks` 目录下，例如 `src/mocks/server.js`。

```javascript
// src/mocks/server.js
import { setupServer } from 'msw/node';

const handlers = [
  // 这里定义你的 mock 处理程序
  // 例如，模拟一个 GET 请求
  {
    method: 'GET',
    path: '/api/users',
    response: () => ({
      status: 200,
      json: [
        { id: 1, name: 'John Doe' },
        { id: 2, name: 'Jane Smith' },
      ],
    }),
  },

  // 模拟一个 POST 请求
  {
    method: 'POST',
    path: '/api/users',
    response: (req, res, ctx) => {
      const { name } = req.body;
      return res(
        ctx.status(201),
        ctx.json({
          id: 3,
          name,
        })
      );
    },
  },
];

// 创建并导出 mock 服务器
export const server = setupServer(...handlers);
```

### 3. 配置 MSW 在开发环境和测试环境中运行

#### 开发环境

为了在开发环境中启用 MSW，你需要在项目的入口文件中引入并启动 mock 服务器。通常这个文件是 `public/index.html` 或 `src/index.js`。

在 `public/index.html` 中添加 MSW 的 worker 脚本：

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>My App</title>
  <script src="/mockServiceWorker.js"></script>
</head>
<body>
  <div id="root"></div>
  <script src="/src/main.js"></script>
</body>
</html>
```

然后在 `src/mocks/browser.js` 中设置浏览器环境下的 MSW：

```javascript
// src/mocks/browser.js
import { setupWorker } from 'msw';
import { handlers } from './server';

export const worker = setupWorker(...handlers);

worker.start();
```

确保在 `src/index.js` 或 `src/main.js` 中导入 `src/mocks/browser.js`：

```javascript
import './mocks/browser';
```

#### 测试环境

如果你使用的是 Jest 进行单元测试，可以在测试配置文件中（如 `setupTests.js`）引入并启动 mock 服务器：

```javascript
// src/setupTests.js
import { server } from './mocks/server';

beforeAll(() => server.listen());
afterEach(() => server.resetHandlers());
afterAll(() => server.close());
```

并在 `package.json` 中配置 Jest 使用 `setupTests.js`：

```json
{
  "jest": {
    "setupFilesAfterEnv": ["<rootDir>/src/setupTests.js"]
  }
}
```

### 4. 使用 MSW 模拟 API

现在你已经设置好了 MSW，可以在你的应用中像往常一样发送网络请求。MSW 会自动拦截这些请求，并返回你在 `handlers` 中定义的响应。

例如，在 React 组件中使用 `fetch` 发送请求：

```javascript
// src/components/UserList.js
import React, { useEffect, useState } from 'react';

function UserList() {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    fetch('/api/users')
      .then((response) => response.json())
      .then((data) => setUsers(data))
      .catch((error) => console.error('Error fetching users:', error));
  }, []);

  return (
    <ul>
      {users.map((user) => (
        <li key={user.id}>{user.name}</li>
      ))}
    </ul>
  );
}

export default UserList;
```

通过上述步骤，你就可以使用 MSW 在开发和测试环境中模拟后端 API 了。这样可以大大提高开发效率，尤其是在后端服务尚未完成或不稳定的情况下。