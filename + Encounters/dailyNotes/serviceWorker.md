---
aliases: 
theme: 
priority: false
tags:
---
`navigator.serviceWorker` 是浏览器提供的一个 API，它允许网页或 web 应用程序与 Service Worker 进行交互。Service Worker 本身是一个运行在后台的脚本，可以拦截和处理网络请求、缓存资源、发送推送通知等。`navigator.serviceWorker` 提供了注册、更新、卸载 Service Worker 以及控制相关事件的方法。

以下是 `navigator.serviceWorker` 的一些主要方法和属性：

1. **register(scriptURL, options)**:
   - 用于注册一个新的 Service Worker。
   - `scriptURL` 是 Service Worker 脚本的 URL。
   - `options` 可以包含 `scope` 属性，定义 Service Worker 控制的范围，默认是脚本所在的目录及其子目录。

2. **getRegistrations()**:
   - 返回一个 Promise，解析为当前域下所有已注册的 Service Worker 注册对象数组。

3. **getRegistration(clientURL)**:
   - 返回一个 Promise，解析为给定客户端 URL 的 Service Worker 注册对象，如果没有找到则返回 `null`。

4. **controller**:
   - 当前页面的 Service Worker 控制器。如果页面被 Service Worker 控制，则这个属性会指向该 Service Worker；否则为 `null`。

5. **oncontrollerchange**:
   - 事件处理器，在 Service Worker 控制器发生变化时触发。

6. **ready**:
   - 返回一个 Promise，当 Service Worker 已经安装并激活后解析。

### 示例代码

以下是如何使用 `navigator.serviceWorker` 来注册一个 Service Worker，并处理相关的生命周期事件：

```javascript
if ('serviceWorker' in navigator && process.env.NODE_ENV === 'production') {
  window.addEventListener('load', () => {
    // 注册 Service Worker
    navigator.serviceWorker.register('/service-worker.js')
      .then(registration => {
        console.log('Service Worker registered with scope:', registration.scope);

        // 监听 Service Worker 更新事件
        if (registration.installing) {
          console.log('Service worker installing');
        } else if (registration.waiting) {
          console.log('Service worker installed and waiting to activate');
        } else if (registration.active) {
          console.log('Service worker active');
        }

        // 检查是否有新的 Service Worker 在等待激活
        if (navigator.serviceWorker.controller) {
          navigator.serviceWorker.addEventListener('controllerchange', function() {
            console.log('A new service worker is available.');
            // 你可以在这里提示用户刷新页面以应用新的 Service Worker
          });
        }
      })
      .catch(error => {
        console.error('Service Worker registration failed:', error);
      });

    // 监听 Service Worker 状态变化
    navigator.serviceWorker.ready.then(() => {
      console.log('Service Worker is ready.');
    });

    // 获取当前控制器
    if (navigator.serviceWorker.controller) {
      console.log('Current controller:', navigator.serviceWorker.controller);
    }
  });
}
```

在这个示例中，我们首先检查浏览器是否支持 Service Worker 并且当前环境是生产环境。然后，在页面加载完成后，我们尝试注册一个 Service Worker，并监听其状态变化。此外，还监听了 `controllerchange` 事件，以便在有新的 Service Worker 可用时进行处理。

通过这些方法和属性，开发者可以有效地管理和控制 Service Worker，从而提升 web 应用程序的性能和用户体验。