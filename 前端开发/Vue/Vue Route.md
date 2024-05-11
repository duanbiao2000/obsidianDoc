#Vue 

[十分钟，带你了解 Vue3 的新写法 - 掘金 (juejin.cn)](https://juejin.cn/post/7225267685763907621)

### Router-view

`<router-view>` 是 Vue.js 中官方提供的一个组件，用来动态渲染匹配到的路由组件。

在应用中使用了 Vue.js 的官方路由插件`Vue Router`。
下面是一个在 Vue.js 应用程序中使用 `<router-view>` 的例子：

```vue
<template>
  <div id="app">
    <nav>
      <router-link to="/">首页</router-link>
      <router-link to="/about">关于</router-link>
      <router-link to="/contact">联系我们</router-link>
    </nav>

    <router-view></router-view>
  </div>
</template>

<script>
import { createRouter, createWebHistory } from 'vue-router'

// 导入组件
import Home from './views/Home.vue'
import About from './views/About.vue'
import Contact from './views/Contact.vue'

// 创建路由对象实例
const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', component: Home },
    { path: '/about', component: About },
    { path: '/contact', component: Contact }
  ]
})

export default {
  router
}
</script>
```

在这里，我们定义了三个路由地址 `/`、`/about` 和 `/contact` 分别对应三个页面组件 `Home`、`About`和`Contact`。在 `<template>` 模板中，使用了 `<router-link>` 标签作为路由跳转的链接入口。在`<router-view>`标签中完成当前路由地址所匹配到的页面组件的展示。

这样，当用户点击任意一个路由标签时，就会动态地加载相应的页面组件并展示在页面上。`<router-view>` 的作用就是在这种场景下承载动态内容所需要的占位标记。

[[Vue组件方法]]

### 三省: Vue Router的基本用法

Vue Router 是 Vue.js 官方路由管理插件，用于在单页应用中实现路由功能。通过 Vue Router 可以将多个页面组合成一个完整的 SPA（Single Page Application）。 

以下是基本的使用步骤：

1. 安装 Vue Router

   在命令行界面中执行以下命令来安装 `vue-router` 模块：

   ```
   npm install vue-router
   ```

2. 注册路由

   在 Vue 的入口文件（例如 `main.js`）中，引入 `vue-router` 包并注册：

   ```javascript
   import VueRouter from 'vue-router'
   // 导入所有页面组件
   import Home from './components/Home.vue'
   import About from './components/About.vue'

   const router = new VueRouter({
     routes: [
       {
         path: '/',
         component: Home
       },
       {
         path: '/about',
         component: About
       }
     ]
   })

   // 创建 Vue 实例并启动路由
   new Vue({
     router
   }).$mount('#app')
   ```

   上述代码中，我们先导入了 `vue-router` 模块并使用 `Vue.use()` 方法来让 Vue.js 知道我们要使用该插件。接着定义了两个简单的路由，其中 `path` 属性是指定我们选定的 URL（例如 `/about`），而 `component` 属性则告诉 Vue.js 如何渲染该组件。

3. 创建组件

   接下来，需要创建每个页面或视图组件。这些组件只需普通的 Vue 组件即可。例如：

   ```html
   <template>
     <h1>Welcome to Home page!</h1>
   </template>

   <script>
   export default {
     name: 'Home'
   }
   </script>
   ```

   当用户访问 '/about' 路径时，Vue Router 会自动渲染位于 `About.vue` 中的组件，并显示在页面上。

4. 使用 `<router-link>` 标签

   在模板视图中使用 `<router-link>` 标签来导航到其他路由，例如：

   ```html
   <router-link to="/">Home</router-link>
   <router-link to="/about">About</router-link>
   ```

   注意 `to` 属性是设置为路由路径 (`'/about'`) 的字符串，这会告诉 Vue.js 到哪个 URL 去渲染。

5. 完成

   至此，我们已经成功地实现了一个简单的基于 Vue Router 的单页应用程序。你可以通过修改 `routes` 对象来添加更多的路由，或者配置不同的选项来自定义路由行为。

以上是 Vue Router 最基本的使用方法，它支持各种类型的路由（包括动态路由、嵌套路由和命名视图等）。如果想了解更多高级特性，请查看 Vue Router 官方文档。

### 一省: Vue3动态路由

在 Vue3 中，我们可以通过 `createRouter` 方法创建路由实例并通过 `router.addRoute` 方法动态添加路由。

下面是一个示例代码：

```javascript
import { createRouter, createWebHashHistory } from 'vue-router' // 导入 Vue Router 的相关模块

const router = createRouter({ // 创建路由实例并传入路由配置对象
  history: createWebHashHistory(), // 设置路由的 history 模式，使用 hash 模式
  routes: [ // 定义初始的路由配置
    {
      path: '/', // 路由路径
      name: 'Home', // 路由名称，可用于跳转和命名视图组件
      component: Home // 路由所对应的视图组件
    }
  ]
})

// 定义需要动态添加的路由配置
const dynamicRoutes = [
  {
    path: '/about', // 路由路径
    name: 'About', // 路由名称，可用于跳转和命名视图组件
    component: () => import('../views/About.vue') // 路由所对应的视图组件，使用动态导入的方式加载
  },
  {
    path: '/contact', // 路由路径
    name: 'Contact', // 路由名称，可用于跳转和命名视图组件
    component: () => import('../views/Contact.vue') // 路由所对应的视图组件，使用动态导入的方式加载
  }
]

// 在合适的时机，调用router.addRoute方法添加路由
router.isReady().then(() => { // 等待路由实例准备就绪后再执行动态路由添加操作
  dynamicRoutes.forEach(route => {
    router.addRoute(route) // 添加路由
  })
})

```

在这个示例中，我们首先使用 `createRouter` 方法创建了一个路由实例并定义了初始的路由配置。然后，在需要动态添加路由的地方，我们定义了一个数组 `dynamicRoutes` 来存储要添加的路由配置。最后，当路由实例准备就绪时，我们通过 `router.addRoute` 方法将每个动态路由添加到路由实例中。

需要注意的是，`addRoute` 方法必须在路由实例准备就绪后才能调用，因此我们通过 `router.isReady()` 方法返回 Promise 对象，等待路由实例准备就绪后再进行动态路由的添加。

