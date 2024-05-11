#### vue组件间通信代码示例

在这里，我将为您提供一个简单的Vue.js组件间通信示例。我们将使用两个组件：`ParentComponent` 和 `ChildComponent`。通过父子组件之间的传递属性（props）和自定义事件（emit），实现基本的组件间通信。

1. 安装 Vue.js:

```bash
npm install -g vue
```

2. 创建一个新的Vue项目：

```bash
vue create example-project
cd example-project
```

3. 在 `src/components` 目录下，创建两个文件：`ParentComponent.vue` 和 `ChildComponent.vue`。

4. 编辑 `ParentComponent.vue` 文件：

```html
<template>
  <div class="parent-component">
    <h1>Parent Component</h1>
    <child-component :message="parentMessage" @changeMessage="updateMessage"></child-component>
  </div>
</template>

<script>
import ChildComponent from './ChildComponent.vue';

export default {
  components: {
    ChildComponent
  },
  data() {
    return {
      parentMessage: 'Hello from Parent'
    };
  },
  methods: {
    updateMessage(newMessage) {
      this.parentMessage = newMessage;
    }
  }
};
</script>
```

5. 编辑 `ChildComponent.vue` 文件：

```html
<template>
  <div class="child-component">
    <h2>Child Component</h2>
    <p>{{ message }}</p>
    <button @click="changeMessage">Change Message</button>
  </div>
</template>

<script>
export default {
  props: {
    message: String
  },
  methods: {
    changeMessage() {
      this.$emit('changeMessage', 'Hello from Child');
    }
  }
};
</script>
```

在这个示例中，我们使用 `props` 将数据从父组件传递给子组件。同时，当子组件的按钮被点击时，我们通过 `$emit` 触发一个自定义事件（`changeMessage`），然后在父组件中监听该事件，并使用更新函数（`updateMessage`）来更新父组件的数据。

要查看此示例，请将 `App.vue` 中的内容替换为以下内容：

```html
<template>
  <div id="app">
    <parent-component></parent-component>
  </div>
</template>

<script>
import ParentComponent from './components/ParentComponent.vue';

export default {
  name: 'App',
  components: {
    Parent
[Network Error]
```
