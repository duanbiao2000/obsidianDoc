---
aliases: null
theme: null
priority: false
date_created: 2024-12-15 05:38
date_update: null
tags: null
---

### 二省: Vue3 Composition API

当我们使用 Vue 2.x 中的选项 API 时，我们是通过组件选项来编写代码的，比如 `data`、`methods` 和 `computed` 等。为了便于代码重用和逻辑复杂度管理，我们通常会将相关的代码分解到 mixin 、指令和服务中。但这样做可能会在不同部分间造成交叉影响，增加调试和维护的难度。Vue 3 引入了 Composition API 以帮助我们解决这个问题。

Composition API 可以让我们更好地组织和复用组件内部的代码。它与 Vue 2.x 中的选项 API 不同，主要标志着一种思想：将逻辑按照功能划分到不同函数中，并通过类似 Hook 的方式将它们组合在一起。下面是一个简单示例：

```javascript
<template>
  <div>
    <p>Count: {{ count }}</p>
    <button @click="increment">Click</button>
  </div>
</template>

<script>
import { ref } from 'vue';

export default {
  name: 'MyComponent',
  setup() {
    // 定义响应式的数据变量
    const count = ref(0);

    // 定义操作该数据的函数
    function increment() {
      count.value++;
    }

    // 返回定义的数据和函数
    return {
      count,
      increment,
    }
  },
};
</script>
```

通过使用 `ref()` 函数将count变量定义为响应式变量，并使用 `setup()` 函数将count和 increment 导出，我们可以在组件中轻松的调用这些对象或方法，实现组件逻辑的复用和管理。

需要注意的是，我们不能再使用 Vue 2.x 的 Options API 中的**数据选项（例如：`data()` 和 `computed`），它们已被合并成一个名为 `setup()` 的函数**。同时，在 Composition API 中，我们不再依赖 this 关键字来访问内部组件属性和方法了。

Vue 3 与 Vue 2.x 在组件注册方面略有不同。在 Vue 3 中，我们使用 `createApp` 创建一个应用实例，并通过 `component` 方法注册组件，具体如下所示：

1. 组件全局注册

```javascript
// 1. 创建组件
const MyComponent = {
  template: `
    <div>
      <h2>{{title}}</h2>
      <p>这是一个全局组件</p>
    </div>
  `,
  data() {
    return {
      title: 'My Component',
    };
  },
};

// 2. 注册组件
const app = createApp({});
app.component('my-component', MyComponent);
```

在代码中，我们使用 `createApp()` 方法创建一个 Vue 应用实例的变量 `app`，并通过 `app.component()` 方法进行全局组件的注册。此时，该组件就可以在该 Vue 实例中的任何地方使用。

2. 局部组件注册

与全局组件不同，局部组件需要在其父组件中进行注册才能使用。下面是一个局部组件注册的示例：

```javascript
// 父组件
const AppComponent = {
  template: `
    <div>
      <h1>{{title}}</h1>
      <my-component></my-component>
    </div>
  `,
  data() {
    return {
      title: 'App Component',
    };
  },
  components: {
    // 注册子组件
    'my-component': {
      template: `
        <div>
          <h2>{{title}}</h2>
          <p>这是一个局部组件</p>
        </div>
      `,
      data() {
        return {
          title: 'My Component',
        };
      },
    },
  },
};
```

在上述代码中，我们使用 `components` 属性来注册局部子组件，注意要将其包裹在 Vue 3 的 `createApp()` 创建的应用实例内。此时，该组件就可以在父组件模板中直接使用 `<my-component>` 标签进行使用。

在 Vue 3 中，非根组件不再允许未经 Registration 的动态创建，也就是说在部署和运行时上也有了一定程度的可控性。
