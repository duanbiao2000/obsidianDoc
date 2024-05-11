
### 需要学习哪些Vue.js框架相关知识点？

**Vue.js 安装、Vue.js 目录结构、Vue.js 起步、Vue.js 模板语法、Vue.js 条件语句、Vue.js 循环语句、Vue.js 计算属性、Vue.js 监听属性、Vue.js 样式绑定、Vue.js 事件处理器、Vue.js 表单、Vue.js 组件、Vue.js 组件自定义事件、Vue.js 自定义指令、Vue.js 路由、Vue.js 过渡& 动画、Vue.js 混入、Vue.js Ajax(axios)、Vue.js Ajax(vue-resource)、Vue.js 响应接口、Vue.js 实例等。**

[内置指令 | Vue.js (vuejs.org)](https://cn.vuejs.org/api/built-in-directives.html)

  ```vue
  <!-- 方法处理函数 -->
  <button v-on:click="doThis"></button>
  
  <!-- 动态事件 -->
  <button v-on:[event]="doThis"></button>
  
  <!-- 内联声明 -->
  <button v-on:click="doThat('hello', $event)"></button>
  
  <!-- 缩写 -->
  <button @click="doThis"></button>
  
  <!-- 使用缩写的动态事件 -->
  <button @[event]="doThis"></button>
  
  <!-- 停止传播 -->
  <button @click.stop="doThis"></button>
  
  <!-- 阻止默认事件 -->
  <button @click.prevent="doThis"></button>
  
  <!-- 不带表达式地阻止默认事件 -->
  <form @submit.prevent></form>
  
  <!-- 链式调用修饰符 -->
  <button @click.stop.prevent="doThis"></button>
  
  <!-- 按键用于 keyAlias 修饰符-->
  <input @keyup.enter="onEnter" />
  
  <!-- 点击事件将最多触发一次 -->
  <button v-on:click.once="doThis"></button>
  
  <!-- 对象语法 -->
  <button v-on="{ mousedown: doThis, mouseup: doThat }"></button>
  ```

  

- v-bind  动态的绑定一个或多个 attribute，也可以是组件的 prop。

  - **缩写：**`:` 或者 `.` (当使用 `.prop` 修饰符)

  ```vue
  <!-- 绑定 attribute -->
  <img v-bind:src="imageSrc" />
  
  <!-- 动态 attribute 名 -->
  <button v-bind:[key]="value"></button>
  
  <!-- 缩写 -->
  <img :src="imageSrc" />
  
  <!-- 缩写形式的动态 attribute 名 -->
  <button :[key]="value"></button>
  
  <!-- 内联字符串拼接 -->
  <img :src="'/path/to/images/' + fileName" />
  
  <!-- class 绑定 -->
  <div :class="{ red: isRed }"></div>
  <div :class="[classA, classB]"></div>
  <div :class="[classA, { classB: isB, classC: isC }]"></div>
  
  <!-- style 绑定 -->
  <div :style="{ fontSize: size + 'px' }"></div>
  <div :style="[styleObjectA, styleObjectB]"></div>
  
  <!-- 绑定对象形式的 attribute -->
  <div v-bind="{ id: someProp, 'other-attr': otherProp }"></div>
  
  <!-- prop 绑定。“prop” 必须在子组件中已声明。 -->
  <MyComponent :prop="someThing" />
  
  <!-- 传递子父组件共有的 prop -->
  <MyComponent v-bind="$props" />
  
  <!-- XLink -->
  <svg><a :xlink:special="foo"></a></svg>
  ```

  

- v-model 在表单输入元素或组件上创建双向绑定。

- v-slot 用于声明具名插槽或是期望接收 props 的作用域插槽。

  - **缩写：**`#`

- v-pre

- v-once

- v-memo

- v-cloak


[[MVVM模式]]

[[Vue3中的变化]]