###  Vue HTTP请求

`this.$http.get` 是 Vue Resource 插件提供的 API，用于发送 HTTP GET 请求并获取响应数据。Vue Resource 是一个官方提供的、轻量级的 AJAX 库，它可以在 Vue.js 的应用程序中非常方便地集成和使用，支持多种数据格式的发送和接收。

一般使用方法如下：

```javascript
this.$http.get(url, config).then(response => {
  // 处理响应数据
}).catch(error => {
  // 处理错误信息
})
```

参数说明：

-   `url`: 要请求的 URL 地址。
-   `config`: 可选配置对象，包含请求头、请求参数等设置。

返回值：返回一个 Promise 对象，在该 Promise 中处理响应数据或者出错信息。

例如，向服务器请求一个 JSON 格式的数据：

```javascript
// 在 Vue 实例的生命周期钩子函数中发送 HTTP GET 请求
export default {
  created() {
    this.$http.get('/api/data.json', { params: { limit: 10 } })
      .then(response => {
        console.log(response.data)
      })
      .catch(error => {
        console.log(error)
      })
  }
}
```

上面代码中，我们在组件的 created 钩子函数中调用了 `this.$http.get()` 方法，以获取 `/api/data.json` 的响应结果，并将限制条目为 `10`，最终在控制台打印响应数据。需要注意的是，在使用 Vue Resource 发送请求之前，需要先通过 `Vue.use()` 方法将 Vue Resource 插件安装到 Vue.js 中。

同时，需要注意的是，Vue Resource 并不是 Vue.js 官方推荐的 Ajax 库。在新版本中， Vue 已经建议使用 axios 库来替代 Vue Resource 的使用。 若要使用 `axios` 发送 `GET`请求, 使用方法如下：

```javascript
//导入 axios 库
import axios from 'axios'

methods: {
  getData() {
    // 通过axios.get方法发送数据请求
    axios.get('/api/data.json', {params:{ limit:10 }})
      .then(response => {
        console.log(response.data)
      })
      .catch(error => {
        console.log(error)
      });
  }
}
```

需要注意的是, 需要在组件引用 axios 版本库，用以正常工作。