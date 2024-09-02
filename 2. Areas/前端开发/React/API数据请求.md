### API数据请求



在 React 中处理异步请求有多种方式，以下是一些常用的方法：

1. 使用回调函数：可以将回调函数作为参数传递给异步请求方法，在请求完成后调用回调函数来处理返回的数据。
```jsx
import React, { useState } from 'react';
import axios from 'axios';
function MyComponent() {
  const [data, setData] = useState(null);
  const fetchData = () => {
    axios.get('https://api.example.com/data')
      .then(response => {
        setData(response.data);
      })
      .catch(error => {
        console.error(error);
      });
  };
  return (
    <div>
      <button onClick={fetchData}>Fetch Data</button>
      {data && <p>{data}</p>}
    </div>
  );
}
export default MyComponent;
```
在这个示例中，我们定义了一个 `fetchData` 函数，它使用 axios 发起异步请求，并在请求成功后将返回的数据存储到 `data` 状态中。在组件的返回 JSX 中，我们使用一个按钮来触发 `fetchData` 函数，并根据 `data` 的值渲染相应的内容。
2. 使用 async/await：可以将异步请求方法定义为 async 函数，并使用 await 关键字等待请求完成后获取返回的数据。
```jsx
import React, { useState } from 'react';
import axios from 'axios';
function MyComponent() {
  const [data, setData] = useState(null);
  const fetchData = async () => {
    try {
      const response = await axios.get('https://api.example.com/data');
      setData(response.data);
    } catch (error) {
      console.error(error);
    }
  };
  return (
    <div>
      <button onClick={fetchData}>Fetch Data</button>
      {data && <p>{data}</p>}
    </div>
  );
}
export default MyComponent;
```
在这个示例中，我们使用 `async` 关键字将 `fetchData` 函数定义为异步函数。在函数体内，我们使用 `await` 关键字等待 axios 的 GET 请求完成，并使用返回的数据更新 `data` 状态。
3. 使用第三方库：还可以使用第三方库（如 redux-thunk、redux-saga 或 react-query）来管理和处理异步请求。这些库提供了更多的功能和灵活性，以处理复杂的异步操作和状态管理。


### 回调&Promise
当涉及到异步代码时，JavaScript 提供了两种常用的处理方式：回调函数（Callbacks）和 Promise。以下是一个相同的示例，分别使用这两种方法来执行异步操作，假设我们要模拟加载用户数据的情况：

1. **使用回调函数（Callbacks）：**

```javascript
function getUserData(callback) {
  setTimeout(function () {
    const userData = { id: 1, username: "exampleUser" };
    callback(null, userData); // 第一个参数是错误，第二个参数是数据
  }, 1000); // 模拟1秒的延迟
}

getUserData(function (error, data) {
  if (error) {
    console.error("Error:", error);
  } else {
    console.log("User Data:", data);
  }
});
```

在这个示例中，`getUserData` 函数接受一个回调函数作为参数，一秒钟后模拟异步操作完成并调用回调函数，传递用户数据或错误。

2. **使用 Promise：**

```javascript
function getUserData() {
  return new Promise(function (resolve, reject) {
    setTimeout(function () {
      const userData = { id: 1, username: "exampleUser" };
      resolve(userData); // 异步操作成功
      // 如果有错误，可以使用 reject(error) 来拒绝 Promise
    }, 1000); // 模拟1秒的延迟
  });
}

getUserData()
  .then(function (data) {
    console.log("User Data:", data);
  })
  .catch(function (error) {
    console.error("Error:", error);
  });
```

在这个示例中，`getUserData` 返回一个 Promise 对象，当异步操作完成时，它会调用 `resolve` 来传递用户数据或调用 `reject` 来传递错误。然后，通过使用 `.then` 方法来处理成功的情况，使用 `.catch` 方法来处理错误的情况。
