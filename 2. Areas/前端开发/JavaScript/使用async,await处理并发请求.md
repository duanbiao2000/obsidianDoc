---
aliases: 
tags: 
source: 
author: 
<<<<<<< HEAD
date_created: 2024-07-14 17:02
type: 
priority: false
=======
createdAt: 
updateAt: 2024-07-14 17:02
categories: 
status: false
>>>>>>> 93a933e (refactor(dailyNotes): update metadata structure for daily notes)
---
在JavaScript中，`async/await` 是处理异步操作的一种简洁方式，特别适合管理并发请求。下面是一个示例，展示了如何使用 `async/await` 发起多个HTTP请求（以fetch API为例），并等待所有请求完成。同时，我会提供一个简单的单元测试思路，但请注意实际的单元测试实现依赖于你选择的测试框架（如Jest、Mocha等）。

### 示例代码

```javascript
// 引入必要的库，如果使用Node.js环境可能需要`node-fetch`库
// 在浏览器环境中fetch是内置的，无需引入
// const fetch = require('node-fetch');

async function fetchUrls(urls) {
  /**
   * 并发请求所有URLs，并收集响应数据。
   * 使用Promise.all来并发执行所有的fetch请求，
   * 然后等待所有请求完成或任何一个失败。
   */
  try {
    const responses = await Promise.all(urls.map(url => fetch(url))); // 发起并发请求
    const data = await Promise.all(responses.map(r => r.ok ? r.json() : r.text())); // 等待所有响应并解析为JSON或文本
    return data;
  } catch (error) {
    console.error('One or more requests failed:', error);
    throw error; // 重新抛出错误以便上层处理
  }
}

// 示例URLs
const urls = [
  'https://api.example.com/data1',
  'https://api.example.com/data2',
  'https://api.example.com/data3',
];

(async () => {
  try {
    const results = await fetchUrls(urls);
    console.log('All requests completed:', results);
  } catch (e) {
    console.error('Error in fetching data:', e);
  }
})();
```

### 单元测试思路

为了进行单元测试，你需要模拟（mock）`fetch` 函数的行为，确保测试不依赖于真实的网络请求。以下是使用 Jest 测试框架的一个简单示例思路：

#### 安装Jest

如果你还没有安装Jest，可以通过npm或yarn进行安装：

```bash
npm install --save-dev jest
# 或者
yarn add --dev jest
```

#### 编写测试

创建一个测试文件，例如 `fetchUrls.test.js`：

```javascript
// fetchUrls.test.js
const fetchUrls = require('./your-code-file'); // 引入你的函数

// Mock fetch function
global.fetch = jest.fn();

beforeEach(() => {
  fetch.mockReset();
});

test('fetchUrls should handle concurrent requests and return data', async () => {
  // Mock responses for each URL
  fetch.mockResolvedValueOnce({ ok: true, json: () => Promise.resolve({ data: 'data1' }) });
  fetch.mockResolvedValueOnce({ ok: true, json: () => Promise.resolve({ data: 'data2' }) });
  fetch.mockResolvedValueOnce({ ok: true, json: () => Promise.resolve({ data: 'data3' }) });

  const urls = [
    'https://api.example.com/data1',
    'https://api.example.com/data2',
    'https://api.example.com/data3',
  ];

  const results = await fetchUrls(urls);

  // 验证结果
  expect(results).toEqual([{ data: 'data1' }, { data: 'data2' }, { data: 'data3' }]);
  // 验证fetch被正确调用了三次
  expect(fetch).toHaveBeenCalledTimes(urls.length);
});
```

请根据你的具体需求调整测试用例和模拟的响应。记得在你的项目中配置Jest，并运行测试（通常是通过命令行执行`jest`或在IDE中配置）。