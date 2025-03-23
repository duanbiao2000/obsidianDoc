---
aliases: 

categories: 
high_priority: false

tags:
---
在使用 Jest 进行测试时，`@jest/globals` 提供了全局的 Jest 测试工具，包括 `expect`、`test`（或 `it`）、`describe` 等。这些工具可以帮助你编写和运行单元测试。下面是一个简单的示例，展示如何使用 `expect` 和其他 Jest 工具来编写测试。

### 1. 安装 Jest

如果你还没有安装 Jest，可以使用 npm 或 yarn 来安装：

```bash
npm install --save-dev jest
# 或者
yarn add --dev jest
```

### 2. 配置 Jest

通常情况下，Jest 会自动查找 `src` 目录下的测试文件（如 `*.test.js` 或 `*.spec.js`）。如果你需要自定义配置，可以在项目根目录下创建一个 `jest.config.js` 文件。

```javascript
// jest.config.js
module.exports = {
  testEnvironment: 'jsdom', // 如果你在测试 React 组件
  setupFilesAfterEnv: ['<rootDir>/src/setupTests.js'], // 如果你需要设置全局的测试环境
};
```

### 3. 编写测试

假设你有一个简单的 JavaScript 函数，你想为它编写测试。以下是一个示例函数和相应的测试代码。

#### 示例函数

```javascript
// src/math.js
export function add(a, b) {
  return a + b;
}
```

#### 测试文件

```javascript
// src/math.test.js
import { expect } from '@jest/globals';
import { add } from './math';

describe('add function', () => {
  it('should add two numbers correctly', () => {
    const result = add(2, 3);
    expect(result).toBe(5);
  });

  it('should handle negative numbers', () => {
    const result = add(-2, 3);
    expect(result).toBe(1);
  });

  it('should handle floating point numbers', () => {
    const result = add(0.1, 0.2);
    expect(result).toBeCloseTo(0.3); // 使用 toBeCloseTo 处理浮点数精度问题
  });
});
```

### 4. 运行测试

你可以使用以下命令来运行你的测试：

```bash
npx jest
# 或者
yarn test
```

### 5. 使用 Mock Service Worker (MSW) 进行 API 模拟

如果你还想结合 MSW 来模拟后端 API，可以按照以下步骤进行：

#### 安装 MSW

```bash
npm install msw --save-dev
# 或者
yarn add msw --dev
```

#### 创建 Mock 服务器

```javascript
// src/mocks/server.js
import { rest } from 'msw';
import { setupServer } from 'msw/node';

const handlers = [
  rest.get('/api/users', (req, res, ctx) => {
    return res(
      ctx.status(200),
      ctx.json([
        { id: 1, name: 'John Doe' },
        { id: 2, name: 'Jane Smith' },
      ])
    );
  }),
];

export const server = setupServer(...handlers);
```

#### 在测试中使用 MSW

在 `setupTests.js` 中启动 mock 服务器：

```javascript
// src/setupTests.js
import { server } from './mocks/server';

beforeAll(() => server.listen());
afterEach(() => server.resetHandlers());
afterAll(() => server.close());
```

#### 编写带有 API 模拟的测试

```javascript
// src/api.test.js
import { expect } from '@jest/globals';
import fetch from 'node-fetch'; // 如果你在 Node.js 环境中使用 fetch

describe('API tests with MSW', () => {
  it('should fetch users successfully', async () => {
    const response = await fetch('/api/users');
    const data = await response.json();

    expect(response.status).toBe(200);
    expect(data).toEqual([
      { id: 1, name: 'John Doe' },
      { id: 2, name: 'Jane Smith' },
    ]);
  });
});
```

### 总结

通过上述步骤，你可以使用 Jest 和 MSW 来编写和运行单元测试，并且可以模拟后端 API 以确保前端代码在开发和测试过程中能够独立于实际后端服务运行。这样可以提高开发效率，并确保代码的正确性。