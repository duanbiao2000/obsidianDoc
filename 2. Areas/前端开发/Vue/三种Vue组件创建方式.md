###  三种组件创建方式

在 Vue.js 中，组件是构建应用程序的基本单元。组件可以包含自己的数据和模板，可以嵌套在其他组件中，并且可以让您更好地组织代码和逻辑。Vue.js 支持三种组件创建方式：

1. 全局注册

这种方式需要使用 Vue.component() 方法全局注册组件。仅需在应用程序入口文件（如 main.js 或 app.js）中引入组件并定义名字即可。全局注册组件后，它就可以在整个项目的任何组件模板中使用。

```javascript
// 定义一个全局组件
Vue.component('my-button', {
  template: '<button>Click Me</button>'
})
```

2. 局部注册

对于只在指定组件内部使用的组件，可以使用局部注册。在组件的 components 选项中注册组件。这样就只能在父级组件模板中使用该组件，而在其他组件模板中无法使用。

```javascript
var myButton = {
  template: '<button>Click Me</button>'
}

new Vue({
  el: '#app',
  components: {
    'my-button': myButton
  }
})
```

3. 单文件组件

单文件组件是一种将 HTML 模板、JavaScript 代码和 CSS 样式组合在一个文件中的组件，常用的扩展名为 `.vue`。单文件组件使得组件代码更清晰、更易维护，在引入 Vue CLI 的情况下可以使用这种方式。

单文件组件有三部分组成：template（模板）、script（逻辑）和 style（CSS 样式）。下面是一个简单的单文件组件示例：

```vue
<template>
  <button v-on:click="increment">
    Clicked {{ count }} times.
  </button>
</template>

<script>
export default {
  data() {
    return {
      count: 0
    };
  },
  methods: {
    increment() {
      this.count++;
    }
  }
};
</script>

<style>
button {
  font-size: 14px;
  color: #2c3e50;
}
</style>
```

单文件组件可以通过 import 或 require 方法导入引用，在 Vue.js 的工程化开发中已经成为了必不可少的一部分。


#### 作用域
在 Vue.js 中，有三种作用域，即全局作用域、组件作用域和插槽作用域。

1. 全局作用域

Vue.js 中的全局作用域是指在应用程序中定义的所有变量和方法都可以在任何组件中访问。这种方式定义的数据和方法可以被该Vue应用程序内任意组件调用，但会引起🤡单一状态树(state tree)难以维护的问题。因此，建议使用 Vuex 等全局管理状态工具来更好地处理全局数据。

2. 组件作用域

组件作用域意味着在组件范围内定义的变量和方法仅在该组件中可用，并不会影响其他组件或全局作用域。在组件中定义的数据和方法只能被该组件的实例所调用。

Vue 组件内数据与函数都需要定义在组件选项中：

```javascript
export default{
    data() {
        return {
            message: 'Hello World'
        }
    },
    methods: {
        sayHello(){
            console.log(`Message is ${this.message}`)
        }
    }
};
```

3. 插槽作用域

插槽是 Vue.js 很强大的特性之一，在许多场景下可以很方便地解决复杂的布局或交互需求，而<font color="#ff0000">插槽作用域则允许将插槽内部的内容传递到组件之外</font>。

在组件中，可以使用 `v-bind` 指令来将数据或方法传入插槽中，在插槽模板中使用 `$props` 对象访问到这些数据。

```vue
<template>
  <div>
    <h1>Parent Component</h1>
    <child-component v-slot="slotProps" :name="parentName">
      {{ slotProps.message }} - {{ slotProps.slotData }} 🤣
    </child-component>
  </div>
</template>

<script>
import ChildComponent from './ChildComponent.vue';

export default {
  components: { ChildComponent },
  data() {
    return {
      parentName: 'Tom'
    };
  }
};
</script>
```

在子组件中，可以通过 `<slot>` 标签定义插槽，并通过 `$emit()` 方法向父组件传递需要的数据。

```vue
<template>
  <div>
    <h2>Child Component</h2>
    <!-- 定义一个名称为default的插槽 -->
    <slot name="default" v-bind:slot-data="data">
      <!-- 使用$slots.default渲染默认插槽内容 -->
      {{$slots.default}}
    </slot>
  </div>
</template>

<script>
export default{
  data() {
    return {
      message: 'Hello World',
      data: 'This is slot data.'
    }
  }
}
</script>
```
详细内容请参考Vue.js官方文档。



#### 扩展和注册

在 Vue.js 中，有两个重要的概念——扩展和注册，它们是使用 Vue 插件的基础。

1. 扩展

Vue.js 可以通过插件来扩展其功能。一个 Vue 插件可以添加全局方法或 property、指令和过滤器等。我们可以使用 `Vue.extend()` 或 `Vue.mixin()` 方法来实现 Vue 组件的扩展。例如：

```javascript
// Global Mixin
Vue.mixin({
  created() {
    console.log('Global mixin - Created hook called');
  }
});

// Component-specific Mixin
var myMixin = {
  created() {
    console.log('Local mixin - Created hook called');
  }
};

// Create a component
Vue.component('my-component', {
  mixins: [myMixin], // Use component-specific mixin
  created() {
    console.log('Component - Created hook called');
  }
});
```

2. 注册

当您在应用程序中使用第三方库或自己编写的 Vue 插件时，需要将其注册到应用程序中。Vue.js 支持全局和局部注册。

- 全局注册：可以使用 `Vue.use()` 方法来全局注册一个插件。

```javascript
// Register a global plugin
Vue.use(YourPlugin);
```

- 局部注册：只能在组件中使用并且只存在于该组件内的插件可以通过在组件选项中注册来使用。

```javascript
import YourPlugin from './YourPlugin';

export default{
  data() {
    return {
      message: 'Hello World'
    };
  },
  plugins: [
    YourPlugin
  ]
};
```

总的来说，扩展和注册是 Vue 插件使用的重要概念。在开发或使用 Vue 插件时，请务必熟悉这些概念。

#### 类数组

下面是几个常见的类数组对象：

1. DOM 元素集合

```javascript
const divList = document.getElementsByTagName('div')

console.log(divList.length)    // 5
console.log(divList[0])        // <div>Element 1</div>
```

DOM 元素集合是一个有序的集合，它返回了匹配选择器的所有元素。然而，这不是真正数组，因为它没有数组的方法和属性。

2. 函数参数 arguments 对象

```javascript
function sum() {
  let total = 0
  for (let i = 0; i < arguments.length; i++) {
    total += arguments[i]
  }
  return total
}

console.log(sum(1, 2, 3))    // 6
```

arguments 对象是函数内部的一个变量，它包含了函数调用时传递给函数的参数列表。虽然它具有 length 属性，并且可以按索引访问其中的元素，但它不具备数组的大部分实例方法和属性。

3. 字符串

```javascript
const str = "hello world"

console.log(str.length)     // 11
console.log(str.charAt(4))  // o
```

字符串也是一种类数组类型，它的每个字符都可以像数组那样通过索引来访问，同时具有 length 属性，但它不属于 JavaScript 数组类型，也不具有数组的实例方法和属性。

虽然这些数据结构在形式和操作方式上与真正的数组相似，但它们并不能像数组那样自由的转换、操作。需要注意处理这些数据类型时要特别小心，以免出现错误。