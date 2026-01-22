---
view-count: 8
tags:
  - vue-testing
  - vue-performance
  - vue
  - react
---

## 🧠 Vue.js 选择题测试（共 50 题，每题 2 分，总分 100 分）

---

### ✅ 基础语法与核心机制（1–10）

**5. Vue 响应式系统的底层依赖是？**  
A. Object.defineProperty  
B. Proxy  
C. Reflect.setPrototype  
D. WeakMap  
**答案：B**

**6. `v-if` 和 `v-show` 的主要区别在于？**  
A. 是否支持条件渲染  
B. 是否销毁 DOM  
C. 是否触发 watch  
D. 是否触发 computed  
**答案：B**


---

### 🔧 Composition API（11–20）

**11. Composition API 中用于声明响应式变量的函数是？**  
A. `useState`  
B. `reactive()`  
C. `watch()`  
D. `computed()`  
**答案：B**

**12. `ref()` 返回的对象中实际数据存储在哪个属性？**  
A. value  
B. data  
C. state  
D. content  
**答案：A**

**13. 使用 `computed()` 创建的属性是？**  
A. 静态值  
B. 响应式函数  
C. 异步变量  
D. 只读对象  
**答案：B**

**14. 在 `setup()` 中使用 props 的正确方式是？**  
A. `this.props`  
B. 通过函数参数 `props` 接收  
C. 直接访问全局变量  
D. 使用 `getProps()` 获取  
**答案：B**

**15. `watch()` 的主要作用是？**  
A. 创建响应式变量  
B. 跟踪某个值的变化并执行副作用  
C. 替代生命周期函数  
D. 执行异步 API  
**答案：B**

**16. `reactive()` 和 `ref()` 的关键区别在于？**  
A. reactive 是深层响应式，ref 是基本值响应式  
B. ref 无法跟踪对象  
C. reactive 用于模板渲染  
D. ref 无法绑定 DOM  
**答案：A**


**18. Composition API 中要在模板中使用 `ref`，应使用其哪部分？**  
A. 变量本身  
B. `.value`  
C. 绑定函数  
D. `ref.get()`  
**答案：B**



---

### 🧩 组件与通信（21–30）


**23. 在 Vue 组件通信中使用 `provide/inject` 的作用是？**  
A. 跨层级组件数据传递  
B. 双向绑定  
C. 管理事件流  
D. 实现插槽机制  
**答案：A**


**26. `v-bind="$attrs"` 的主要用途是？**  
A. 动态绑定所有属性  
B. 过滤 class 和 style  
C. 全局指令注入  
D. 控制生命周期  
**答案：A**

**27. `defineExpose()` 的作用是？**  
A. 显示组件状态  
B. 向父组件暴露内部方法或属性  
C. 提供组件名称  
D. 触发页面跳转  
**答案：B**

**28. 哪个函数可以在子组件访问 DOM？**  
A. onSetup  
B. mounted  
C. beforeCreate  
D. created  
**答案：B**

**29. Vue 中通过 `slots` 插入内容时，可以传递哪些类型？**  
A. 数值  
B. 组件结构  
C. 字符串  
D. 以上皆可  
**答案：D**



---

### 🧭 路由与状态管理（31–40）

**34. 在 `<router-view />` 中渲染的是？**  
A. 模板字符串  
B. 当前路由组件  
C. 路由路径  
D. 插槽内容  
**答案：B**


**40. Vue Router 中动态参数访问方式为？**  
A. `$route.param.id`  
B. `$route.params.id`  
C. `$params.id`  
D. `route.id`  
**答案：B**

---

### 🚀 性能与工程实践（41–50）

**41. Vue 的模板编译是在？**  
A. 构建阶段  
B. 编译阶段（由 compiler 编译为 render 函数）  
C. 浏览器运行时  
D. Webpack 之后  
**答案：B**

**42. 以下哪个指令可用于延迟渲染组件？**  
A. `v-if`  
B. `v-pre`  
C. `v-show`  
D. `v-lazy`  
**答案：A**

**43. `v-once` 指令的作用是？**  
A. 只绑定一次事件  
B. 渲染一次后静态化  
C. 防止重新计算  
D. 持久缓存  
**答案：B**



**46. 使用 defineAsyncComponent 的目的？**  
A. 创建 ref  
B. 延迟加载组件  
C. 导出插件  
D. 实现动态样式  
**答案：B**

**47. SSR 模式下 Vue 推荐使用的框架是？**  
A. Vuepress  
B. Nuxt.js  
C. Vite  
D. Quasar  
**答案：B**

**48. Vue 项目中实现服务端预渲染的必要条件包括？**  
A. 状态同步  
B. DOM 访问控制  
C. 同构数据流  
D. 以上皆是  
**答案：D**

**49. 使用 `keep-alive` 的作用是？**  
A. 保持组件状态缓存  
B. 提高性能  
C. 避免卸载  
D. 以上皆是  
**答案：D**


