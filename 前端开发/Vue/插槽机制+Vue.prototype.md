2023-07-13

[[../JavaScript/SCSS Versus CSS]]


### 一省:插槽机制

当一个组件需要多个插槽时，Vue.js的插槽机制提供了一种支持具名插槽和作用域插槽的方法。

1. 具名插槽

在模板中为插槽名称设置一个参数name，以便识别哪个插槽被填充：

```vue
<template>
  <div class="wrapper">
    <header><slot name="header"></slot></header>
    <main><slot></slot></main>
    <footer><slot name="footer"></slot></footer>
  </div>
</template>
```

在父组件中，我们就可以使用 `v-slot` 或 `#` 指令来分别指定相应名称的插槽内容进行填充：

```vue
<my-component>
  <template v-slot:header>
    <h1>这里是页面标题</h1>
  </template>

  <p>这里是页面主体内容</p>

  <template v-slot:footer>
    <p>&copy;2021 my site.</p>
  </template>
</my-component>
```

2. 作用域插槽

如果需要在子组件内部访问外部传入的数据，则可以使用作用域插槽。通过将插槽内容包裹在一个带有参数的标签上，定义了插槽所在范围的数据作用域：

```vue
<template>
  <ul>
    <li v-for="(item, index) in list" :key="index">
      <slot :item="item" :index="index">
        {{ item }}
      </slot>
    </li>
  </ul>
</template>
```

在父组件中，我们需要使用一个具有“`v-slot` + `name`”形式的模板来具体描述作用域插槽并为其绑定数据，将子组件中定义的 `item` 和 `index`等属性进行传递和解构：

```vue
<my-component>
  <template v-slot:list-item="props">
    <span>{{ props.index }} - {{ props.item }}</span>
  </template>
</my-component>
```

上面这个例子实现了对外部数据的引用，在一个可重复、可配置的列表项中渲染不同的内容。它为应用程序提供了更灵活和动态的UI方式，可以方便地针对各种情况进行视图展示和业务逻辑处理。

### 二省: Vue.prototype

#flashcards

`Vue.prototype`是Vue.js框架中的一个概念，在Vue实例化后会自动创建，它是一个对象。我们可以将一些常用的方法或者属性绑定到该原型对象上，使得每个Vue组件实例都能够在<mark style="background: #FF5582A6;">原型链</mark>上访问这些方法或属性。

具体来说，我们可以通过下面这行代码将一个属性绑定到 `Vue.prototype` 对象上：

```
Vue.prototype.baseUrl = 'http://localhost:8000'
```

这样，在所有的 Vue 实例中就都能通过 `this.baseUrl` 访问到这个 URL 地址了。而且，当应用数据量比较大时，使用 `Vue.prototype` 比较好，因为它不会消耗更多的内存，也比较容易管理。

总的来说，`Vue.prototype`允许开发者快速的在项目中添加公共方法或属性等功能，也为应用程序开发提供了更多自定义和扩展的可能性。



```vue
<script>
methods: {
    handleCompleteChange(id, newCompleted) {
      this.todos = this.todos.map(
        t => t.id === id
          ? { ...t, completed: newCompleted }
          : t
</script>
```

这段代码是一个方法，用于处理待办事项的完成状态变化，接收两个参数：待办事项的id和新的完成状态。具体流程如下：

1. 使用`todos`的`map()`方法遍历待办事项数组。
2. 在遍历过程中检查当前待办事项的id是否与传入的id相同，如果相同，则说明该待办事项需要更新。
3. 对需要更新的待办事项执行"展开运算符"（spread operator）操作，将其属性赋值给一个新对象，并将其`completed`属性设置为传入的新状态值。
4. 对于未被更新的待办事项，直接返回原始对象。
5. 将更新后的待办事项数组赋值给组件实例的`todos`属性。

这段代码的主要作用是修改指定待办事项的完成状态，并将修改后的待办事项列表重新赋值给`todos`属性。修改后，Vue会根据新的数据对组件进行重新渲染，从而及时反映用户的操作。

```jsx
<script>
export default {
  async mounted() {
    const { data: todos } = await this.axios.get( 
      `${this.baseUrl}/todos`)
    this.todos = todos
  }
}
</script>
```

该段代码是一个Vue组件中的逻辑代码，通过在`mounted`钩子函数中执行异步网络请求获取待办事项列表。具体流程如下：

1. 在`mounted`钩子函数中使用了ES6的解构语法，将返回结果中的`data`属性重命名为变量`todos`。
2. 发送HTTP GET请求，地址为 `${this.baseUrl}/todos`，其中 this.baseUrl 是在Vue实例上定义的全局变量（即API根路径）。
3. 使用async和await关键字确保请求完成后再执行后续操作。
4. 将返回的待办事项列表数据保存到当前组件的 `todos` 属性中，从而更新组件的状态。

<mark style="background: #FF5582A6;">通常情况下，mounted函数是Vue的生命周期方法之一</mark>。它会在组件被挂载到DOM元素上后立刻执行，用于执行初始化时需要进行的操作，例如获取数据、注册事件监听器等。本段代码中，我们利用该函数发起异步网络请求来获取待办事项列表，并将其保存到组件的状态中，以便于后续进行渲染、修改等操作。

```vue
<template functional>
  <ul>
    <li v-for="todo in props.todos" :key="todo.id">
      <slot name="todo" :todo="todo" />    </li>
  </ul>
</template>
```

该代码段是一个函数式组件的模板，用于渲染待办事项列表。由于函数式组件没有响应式数据或实例，所以无法使用普通Vue组件的方式书写模板。

具体来说，这个组件定义了以下模板结构：

1. `ul`标签，用于包裹待办事项的`li`元素，表示待办事项列表。
2. 使用 `v-for` 指令遍历 `props.todos` 数组，生成多条`li`元素，每个元素对应一个待办事项。
3. `key`属性设置为`todo.id`，可提高列表更新效率。
4. 运用插槽机制（slot），在`li`元素中插入命名插槽，用于渲染待办事项详情。插槽中的 `name="todo"` 表示插槽的名称是“todo”，可以在父组件中通过该名称来进行操作。`:todo="todo"` 则表示将当前待办事项传递给插槽，在插槽内部使用。

相比于普通Vue组件，函数式组件并不需要维护状态和交互行为，它的核心任务是接受输入参数，生成 HTML 片段，并提供下拉插槽将其封装成可复用的模块，从而简化代码的编写和维护。



>   可以将这段代码模板比喻成一个咖啡店，其中`<template functional>`定义了整个咖啡店的主体结构和装修风格。
>
>   首先是展示待办事项列表的 `<ul>` 标签，对应于咖啡店的木质桌椅和各种饮料展示架。在组件外部传入的 `props.todos` 数组就像是顾客点单的列表，每个元素都是一杯不同的咖啡或甜点。
>
>   接下来是使用 `v-for` 遍历这个点单的过程，相当于小二上菜，每个待办事项都对应着一杯咖啡。而:key="todo.id"则类似于我们给每杯咖啡贴上价格标签，以方便后续做账时的核算。
>
>   最后是通过插槽机制描绘出每杯咖啡的详细信息，例如加奶、去冰等选项，相当于是咖啡配料表。由于每杯咖啡的内容不同，因此通过命名插槽的方式设置插拔口（slot），实现不同咖啡之间的互不干扰，确保咖啡的品质和味道都能得到保证。
>
>   总的来说，这段函数式组件的技术原理将现实中的咖啡店模型化，形象地呈现了组件与插槽之间的通信机制。它扩展了 Vue 组件化模式的适用范围，让我们可以更便捷地创建单独的模块来刻画应用程序的UI。

