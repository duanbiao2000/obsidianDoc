

[十分钟，带你了解 Vue3 的新写法 - 掘金 (juejin.cn)](https://juejin.cn/post/7225267685763907621)

###  vue3中的生命周期函数

好的，下面的代码段和注解能够解释Vue3中的生命周期函数：

**1. beforeCreate()**

这个钩子在牵扯到渲染或更改实例时最早被调用。此时，实例还未完成初始化，并且尚不可访问数据。

```javascript
const app = Vue.createApp({
  data() {
    return {
      message: 'Hello, World!'
    }
  },
  beforeCreate() {
    console.log('Before Create:', this.message) // 访问data可以读取到返回值
  }
})

app.mount('#app')
```

**2. created()**

此钩子在与模板交互之前被调用。一旦此方法被执行，您会发现 `el`，`props`，`data` 和 `computed` 属性都可以访问。

```javascript
const app = Vue.createApp({
  data() {
    return {
      message: 'Hello, World!'
    }
  },
  created() {
    console.log('Created:', this.message) // 数据已经可以访问
  }
})

app.mount('#app')
```

**3. beforeMount()**

这个钩子在元素挂载到html页面上之前被调用。在这里，你可以访问 `el` 和 `props` ，但是因为还没有渲染，所以无法访问到 `data` 或 `computed`。

```javascript
const app = Vue.createApp({
  data() {
    return {
      message: 'Hello, World!'
    }
  },
  beforeMount() {
    console.log('Before Mount:', this.$el) // 可以访问el对象，但是该元素未被插入到DOM中
  }
})

app.mount('#app')
```

**4. mounted()**

这个钩子在HTML页面上插入元素后立即被调用。您可以在此处操作 DOM 元素或使用任何需要计算属性的数据。

```javascript
const app = Vue.createApp({
  data() {
    return {
      message: 'Hello, World!'
    }
  },
  mounted() {
    console.log('Mounted:', this.$el) // el已经被插入并渲染，可以获取DOM元素对其进行操作
  }
})

app.mount('#app')
```

**5. beforeUpdate()**

Vue 实例的值在 Data 被得到更改后，在它们传递给DOM之前会被调用。这允许您读取当前的值并在更新之前执行您所需的操作。

```javascript
const app = Vue.createApp({
  data() {
    return {
      message: 'Hello, World!'
    }
  },
  beforeUpdate() {
    console.log('Before Update:', this.message) // 在更新之前可以读取data中的值
  }
})

app.mount('#app')

setTimeout(() => {
  app.message = 'New message' // 将消息更改为"New message"
}, 1000)
```

**6. updated()**

当您暴露 `data` 属性时，该函数将在组件渲染期间自动触发，类似于 DidMount ，通常用于处理己经本身存在于DOM内的组件升级时需要同步到视图上的变更。

```javascript
const app = Vue.createApp({
  data() {
    return {
      message: 'Hello, World!'
    }
  },
  updated() {
    console.log('Updated:', this.$el.textContent) // 更新后可以查看DOM元素中data是否正确渲染
  }
})

app.mount('#app')

setTimeout(() => {
  app.message = 'New message' // 将消息更改为"New message"
}, 2000)
```

**7. beforeUnmount()**

此钩子在 Vue 实例销毁之前调用。在这里解除所有事件监听器、绑定等操作。

```javascript
const Counter = {
  template: '<div>{{ count }}</div>',
  data() {
    return {
      count: 0
    }
  },
  beforeUnmount() {
    console.log('Before Unmount') // 组件将要被卸载
  }
}

const app = Vue.createApp(Counter)
app.mount('#app')
```

**8. unmounted()**

Vue 实例和其关联的 DOM 元素都已经被销毁，此函数将在 Vue 实例销毁时自动调用。做一些清理操作或置空组件。

```javascript
const Counter = {
  template: '<div>{{count}}</div>',
  data() {
    return { 
      count: 0
    }
  },
  unmounted() {
    console.log('Unmounted:', this.$el) // 可以访问el对象，但是它已经从DOM中移除了
  }
}

const app = Vue.createApp(Counter)
app.mount('#app')

setTimeout(() => {
  app.unmount() // 卸载Vue实例组件
}, 5000)
```

以上代码段和注解演示了Vue3中的生命周期函数。掌握这些函数及其钩子，可以帮助您更好地理解Vue实例在应用中的工作原理。



在Vue3中，所有的生命周期钩子函数都接收一个参数——`instance`。

下面是一段简要注释的示例代码：

```javascript
<script>
import { onBeforeMount, onMounted } from 'vue';

export default {
  name: 'MyComponent',

  // 在组件挂载前执行的钩子函数
  onBeforeMount() {
    console.log('onBeforeMount', this);
  },

  // 在组件挂载后执行的钩子函数
  onMounted() {
    console.log('onMounted', this);
  },

  render() {
    return (
      <div>Hello World</div>
    );
  }
};
</script>
```

在上面的代码示例中，我们使用了 `onBeforeMount` 和 `onMounted` 钩子函数。这两个函数都接收一个名为`instance`的参数来引用当前组件实例对象。

需要注意的是，在 Vue3 中，钩子函数已经不作为组件实例方法存在了。所以我们不能使用 `this` 访问其它组件方法或属性。如果想要访问组件方法或属性，可以通过参数 `instance` 来访问。

此外，在 Vue3 的单文件组件中，也可以使用 `import` 导入生命周期钩子函数，并在组件定义时将它们作为对象进行定义和使用。



`import` 和 `export default` 是 ES6 模块语法中的关键字，它们可以用于在 JavaScript 文件之间导入和导出模块。

- `import` 用于从其它文件中引入模块。
- `export default` 用于将模块输出为默认值。

在 Vue3 的单文件组件中，我们通常使用 `import` 来引入各种功能和库。例如：

```javascript
<script>
// 导入必要的模块和函数
import { ref } from 'vue';
import axios from 'axios';

export default {
  name: 'ExampleComponent',
  setup() {
    // 声明一个响应式变量
    const count = ref(0);
    
    // 发送异步请求
    axios.get('...')
      .then(response => {
        console.log('response', response.data);
      })
      .catch(error => {
        console.error('error', error);
      });
      
    return {
      count,
    };
  },
};
</script>
```

而 `export default` 则是用于将当前组件作为默认模块导出，在其他组件中引用时可以省略 module 标识符。例如： 

```javascript
<script>
import ExampleComponent from './ExampleComponent.vue';

export default {
  components: {
    ExampleComponent,
  },
}
</script>
```

上述代码就是在另外一个组件中引用了 `ExampleComponent` 这个默认导出组件，并注册为自己的子组件。



[[Vue3Composition API]]