### Vue中的Key值

Vue 中的 `key` 属性用于以上下文中唯一标识一个 `v-for` 渲染的子元素。它有以下两个主要作用：

1. 帮助 Vue 区分每个列表项，以便在更新列表时能够高效地重新排序或重用现有元素，减少不必要的 DOM 操作。

例如，在一个简单的 TODO 应用程序中，当一个项目被删除时，如果没有设置 `key` 属性，Vue 在更新列表时无法区分哪个元素应该被移除（除非进行全量DOM 重绘），这将导致性能和用户体验受到影响。而通过设置 `key` 属性，Vue 可以忽略未变动的元素，只对增、删、移动有所影响的元素进行局部更新，提高渲染效率。

```html
<!-- 错误示例，没有使用 key -->

<!-- Todos.vue -->
<template>
  <ul>
    <li v-for="todo in todos">
      {{ todo }}
      <button @click="deleteTodo(todo)">Delete</button>
    </li>
  </ul>
</template>

<!-- 正确示例，使用 key -->

<!-- Todos.vue -->
<template>
  <ul>
    <li v-for="todo in todos" :key="todo.id">
      {{ todo }}
      <button @click="deleteTodo(todo)">Delete</button>
    </li>
  </ul>
</template>
```

2. 在 Vue 的过渡系统中，`key` 还用来提示 Vue 哪些元素可以被重复使用。在一些动画场景下（例如列表删除），Vue 可以复用相同 `key` 值的元素，从而减少不必要的动画操作。

需要注意的是，如果使用非稳定的值作为 `key`，可能会导致 Vue 重新渲染整个列表，这将影响应用程序的性能和用户体验。因此，开发人员在设置 `key` 属性时应该使用唯一的、可预测且稳定的值，比如一个 ID 或者索引值等。

#### 过滤器

在Vue中，过滤器是用来格式化文本或者实现一些简单的数据变换的功能。Vue 中分为全局过滤器和局部过滤器。下面分别列举它们的代码并逐行注释。

全局过滤器：

```javascript
// 定义一个名字为 capitalize 的全局过滤器
Vue.filter('capitalize', function (value) {
  // 进行字符串转换处理
  if (!value) return ''
  value = value.toString()
  // 首字母大写并返回处理后的字符串
  return value.charAt(0).toUpperCase() + value.slice(1)
})
```

注解：这里我们定义了一个名为`capitalize`的全局过滤器，该过滤器需要传入一个参数 `value`进行处理。首先判断传入值是否为空字符串，如果不为空，则将该值转成字符串，并将首字母转成大写。最后返回字符串。

使用该全局过滤器：

```html
<!-- 将message的值转换成首字母大写 -->
<div>{{ message | capitalize }}</div>
```

注解：在 Vue 实例内，可以使用管道符(|)调用 `capitalize` 全局过滤器，将message的值进行首字母大写转换。

局部过滤器：

```html
<!-- 定义一个名字为 currency 的局部过滤器-->
<template>
  <div>
    {{ price | currency }}
  </div>
</template>

<script>
export default {
  // 在组件选项对象中注册一个名为 currency 的局部过滤器
  filters: {
    currency(value) {
      // 实现货币单位 "￥" 前缀
      return '￥' + Number.parseFloat(value).toFixed(2)
    }
  },
  data() {
    return {
      price: 29.9
    }
  }
}
</script>
```

注解： 在上面的代码中，我们定义了一个名为 `currency` 的局部过滤器，其目的是在数字前面添加 `￥` 货币单位，并将数据保留小数点后两位。补充一个组件，通过组件显示该结果。

需要注意的是，全局过滤器的注册只需要在 Vue 实例中执行一次，适用于大部分组件内都需要使用相同过滤器的场景，而局部过滤器适合于仅在某个组件中使用的场景，以避免与其他组件可能存在冲突和性能问题。