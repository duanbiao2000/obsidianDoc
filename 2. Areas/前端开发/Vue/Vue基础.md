#Code

root: awsomevue





关键词：Snabbdom
主题：Snabbdom知识点拆解和难度评估
概念：深度思考
以下是对Snabbdom知识点拆解和难度评估的深度思考：

| 知识点 | 难度评估（5星制） | 深度思考问题 |
| ------ | -------------- | ------------ |
| Snabbdom简介 | ★★☆☆☆ | 1. Snabbdom是什么？它有什么特点和优势？2. Snabbdom和其他虚拟DOM库的区别是什么？ |
| 虚拟DOM | ★★★☆☆ | 1. 什么是虚拟DOM？它的工作原理是什么？2. Snabbdom如何实现虚拟DOM的diff算法和patch操作？3. 虚拟DOM的优缺点是什么？ |
| Snabbdom模块 | ★★★★☆ | 1. Snabbdom的核心模块有哪些？它们的作用是什么？2. 如何使用Snabbdom的模块进行元素的创建、更新和删除？3. 如何自定义和扩展Snabbdom的模块？ |
| 性能优化 | ★★★★☆ | 1. Snabbdom如何进行性能优化？2. 如何使用Snabbdom的key属性来提高更新的效率？3. 如何避免不必要的重绘和重排操作？ |
| 与其他框架的整合 | ★★★☆☆ | 1. Snabbdom可以与哪些前端框架进行整合？2. 如何将Snabbdom与其他框架（如Vue、React）结合使用？3. 使用Snabbdom的优势和注意事项是什么？ |
总结和回顾问题：
1. Snabbdom相对于其他虚拟DOM库的优势和劣势是什么？
2. 学习和使用Snabbdom的过程中你遇到的最大挑战是什么？如何克服这个挑战？
3. 你认为学习和使用Snabbdom对于前端开发有何意义？
4. 你认为Snabbdom的设计和实现原理有哪些值得学习和借鉴的地方？
5. 在实际项目中，你如何评估使用Snabbdom的合适性和可行性？
关于Snabbdom的评估和理解：
Snabbdom是一个轻量级的虚拟DOM库，它追求简单、高效和可扩展的设计，适用于构建性能优化的前端应用程序。相比其他虚拟DOM库，Snabbdom的学习曲线相对较陡，需要对虚拟DOM和diff算法有一定的了解。通过深入思考和实践，你可以逐渐掌握Snabbdom的核心概念和使用技巧，并在项目中灵活运用。使用Snabbdom可以提升前端应用的性能和开发效率，同时也可以扩展和定制化以满足特定需求。

Snabbdom的核心模块包括以下几个：
1. `init` 模块：负责初始化Snabbdom的运行环境，创建VNode和patch函数，以及定义一些工具函数。它是Snabbdom的入口模块，起到初始化的作用。
2. `h` 模块：负责创建虚拟DOM节点（VNode），提供了`h`函数用于创建VNode的语法糖。`h`函数接受标签名、属性对象和子节点作为参数，返回一个VNode对象。
3. `toVNode` 模块：负责将真实DOM节点转换为VNode对象，以便进行后续的比较和更新操作。它提供了`toVNode`函数用于将真实DOM节点转换为VNode。
4. `module` 模块：负责处理VNode的各种属性和事件，提供了一系列的模块函数用于处理不同类型的VNode属性和事件。比如，`attrs`模块用于处理HTML属性，`props`模块用于处理DOM属性，`on`模块用于处理事件等。
5. `createElement` 模块：负责根据VNode创建真实DOM节点，并将其插入到文档中。它提供了`createElement`函数用于创建真实DOM节点。
6. `patch` 模块：负责比较两个VNode，并进行更新操作。它提供了`patch`函数用于比较和更新VNode。
这些核心模块共同组成了Snabbdom的基本功能，实现了虚拟DOM的创建、更新和渲染。每个模块都承担着不同的责任，协同工作以实现高效的虚拟DOM操作。通过使用这些模块，开发者可以灵活地构建和管理应用程序的界面。



关键词：Vue
主题：Vue知识点拆解和难度评估
概念：深度思考
以下是对Vue知识点拆解和难度评估的深度思考的表格展示：

| 知识点 | 难度评估（5星制） | 深度思考问题 |
| ---- | -------------- | ------------ |
| Vue实例 | ★★☆☆☆ | 1. Vue实例是什么？它有哪些重要的属性和方法？2. 如何创建Vue实例？3. Vue实例的生命周期是什么？ |
| 模板语法 | ★★★☆☆ | 1. 模板语法有哪些常用的指令和表达式？2. 如何在模板中绑定数据？3. 如何使用条件渲染和循环渲染？ |
| 组件 | ★★★★☆ | 1. 组件是什么？如何定义和使用组件？2. 如何进行组件之间的通信？3. 组件的生命周期是什么？ |
| 路由 | ★★★★☆ | 1. Vue路由是什么？如何配置和使用路由？2. 如何进行路由的导航和传参？3. 如何实现路由的懒加载？ |
| 状态管理 | ★★★★☆ | 1. 为什么需要状态管理？2. 如何使用Vuex进行状态管理？3. 如何进行模块化的状态管理？ |
总结和回顾问题：
1. Vue的核心概念是什么？它和其他前端框架的区别是什么？
2. Vue的优点和缺点是什么？
3. 学习Vue的过程中你遇到的最大挑战是什么？如何克服这个挑战？
4. 你认为学习Vue需要具备哪些前置知识和技能？
5. 你认为学习Vue对于你未来的职业发展有何意义？
关于Vue的评估和理解：
对于初学者来说，Vue的学习曲线相对较低，但对于深入理解和运用Vue的高级特性，如状态管理和路由，可能需要更多的学习和实践。通过深度思考和不断练习，你可以逐渐掌握Vue的核心概念和技巧，并在实际项目中灵活运用。


作为一个AI助手，我没有直接学习Vue的经验，因此无法提供个人的挑战和克服方法。但是，我可以向您提供一些常见的挑战和应对策略，希望对您有所帮助。
常见的学习Vue的挑战可能包括：
1. 理解和掌握Vue的核心概念：Vue有自己的一套概念和架构，例如Vue实例、组件、指令、生命周期等，理解这些概念可能是学习Vue的一个挑战。
2. <font color="#d831a8">处理复杂的组件交互和状态管理：随着应用程序的复杂度增加，组件之间的交互和状态管理变得更加复杂。学习如何有效地管理组件之间的通信和共享状态可能是一个挑战。</font>
3. 对Vue生态系统的了解：Vue生态系统涵盖了许多相关的工具和库，<font color="#d831a8">例如Vue Router和Vuex等。</font>学习如何整合和使用这些工具可能需要额外的时间和努力。
为了克服这些挑战，您可以考虑以下策略：
1. 深入学习Vue官方文档：Vue官方文档是学习Vue的最佳资源，<font color="#d831a8">它提供了详细的指南、示例和API文档。仔细阅读文档，理解Vue的核心概念和用法，并进行实践</font>。
2. 编写和阅读示例代码：<font color="#d831a8">通过编写自己的Vue应用程序并阅读他人的示例代码，可以加深对Vue的理解和应用。</font>从简单的示例开始，逐渐扩展到更复杂的应用程序。
3. 参与Vue社区和开发者活动：加入Vue的社区，参与讨论和交流，与其他开发者分享经验和解决方案。参加Vue相关的活动和培训课程，与其他开发者互动和学习。
4. 实践和项目经验：通过实际的项目经验来应用和巩固所学的Vue知识。通过实际的开发实践，不断提升自己的技能和理解。
总之，学习Vue需要持续的学习和实践。通过不断地克服挑战，您将逐渐掌握Vue的核心概念和技能，并能够应用于实际的开发项目中。

1. 模板语法的常用指令和表达式：
    
    - `v-bind`：用于动态绑定属性，可以使用表达式或者计算属性。
    - `v-on`：用于监听DOM事件，可以执行指定的方法或者表达式。
    - `v-if`：用于条件渲染，根据表达式的真假来决定是否渲染DOM元素。
    - `v-for`：用于循环渲染，根据指定的数据源来生成多个相同结构的DOM元素。
2. 在模板中绑定数据的方法：
    
    - 使用双花括号`{{}}`：可以在模板中使用双花括号将变量或表达式包裹起来，实现数据的插值显示。
    - 使用`v-bind`指令：可以使用`v-bind`指令将属性与数据进行绑定，实现动态属性的更新。
3. 使用条件渲染和循环渲染：
    
    - 条件渲染：使用`v-if`指令，将需要进行条件判断的表达式放在`v-if`指令中，根据表达式的真假来决定是否渲染DOM元素。
    - 循环渲染：使用`v-for`指令，将需要进行循环的数据源和循环体放在`v-for`指令中，实现对数据源的遍历和渲染。


抱歉，我之前的回答并没有指明版本。上述组件生命周期钩子函数是Vue 2.x版本的生命周期。
在最新版本的Vue（Vue 3.x）中，组件的生命周期发生了一些改变。下面是Vue 3.x版本的组件生命周期钩子函数：
1. `beforeCreate`：在实例被创建之前调用。
2. `created`：在实例被创建之后调用。
3. `beforeMount`：在组件被挂载到DOM之前调用。
4. `mounted`：在组件被挂载到DOM之后调用。
5. `beforeUpdate`：在组件更新之前调用。
6. `updated`：在组件更新之后调用。
7. `beforeUnmount`：在组件被卸载之前调用。
8. `unmounted`：在组件被卸载之后调用。
需要特别注意的是，Vue 3.x版本中的生命周期钩子函数发生了一些变化。最显著的变化是将原来的`beforeDestroy`改为了`beforeUnmount`，将原来的`destroyed`改为了`unmounted`。这是为了与Vue 3.x中的新特性Composition API保持一致。
如果您使用的是Vue 3.x版本，请特别注意生命周期钩子函数的命名变化，并相应地进行调整。同时，也建议参考Vue官方文档中关于Vue 3.x版本的生命周期钩子函数的详细说明，以确保正确使用和理解生命周期。


状态管理和路由是Vue中两个重要的概念，它们分别用于管理应用的状态和导航。
状态管理（State Management）：
状态管理是指在应用中管理和共享数据的一种机制。在Vue中，常用的状态管理工具是Vuex。Vuex提供了一种集中式的状态管理模式，用于解决多个组件之间共享数据的问题。通过定义和管理全局状态，Vuex使得组件之间的数据传递和状态同步更加简单和可预测。使用Vuex可以实现数据的响应式更新、数据的持久化、数据的复杂计算等功能。
路由（Routing）：
路由是指在应用中进行页面导航和路由跳转的一种机制。在Vue中，常用的路由工具是Vue Router。Vue Router提供了一种以组件为基础的路由配置方式，用于实现单页应用程序（SPA）中的路由功能。通过定义路由和对应的组件，Vue Router使得页面之间的切换和导航更加简单和灵活。使用Vue Router可以实现路由参数传递、嵌套路由、路由守卫等功能。
状态管理和路由是Vue中常用的工具，它们可以相互配合使用，实现复杂的应用程序开发。通过合理地使用状态管理和路由，可以提高应用的可维护性、可测试性和用户体验。在学习和使用Vue时，深入理解和掌握状态管理和路由的概念和用法，对于构建高质量的Vue应用程序非常重要。

 Vuex 是一个专为 Vue.js 应用程序开发的状态管理模式。它采用集中式存储管理应用的所有组件的状态,并以相应的规则保证状态以一种可预测的方式发生变化。这是官方给出的Vuex的定义。
Vuex 解决了在 Vue 应用中多组件共享状态的问题,它具有以下几个特征:
• 集中式状态管理:将组件的共享状态抽取出来,统一放在一个地方管理。
• 状态是响应式的:当状态发生变化时,相应的视图会更新。
•  mutations 修改状态:必须通过 mutation 变更状态,并且 mutation 必须是同步函数。这保证状态的变更能够追踪,并且在 devtool 中调试。
• actions 提交 mutation:通过 action 间接修改状态,而不是直接修改。action 可以包含任意异步操作。
• getters 提供getter计算属性:类似computed计算属性的计算状态衍生值。
• modules 模块化:将 store 分割成模块(module)。每个模块拥有自己的 state、mutation、action、getter、甚至是嵌套子模块。
Vuex 通常与 Vue-Router 一起使用,实现完整的单页应用。Vuex 管理共享状态,Vue-Router 管理浏览器历史和 UI 路由。
使用 Vuex 有以下几个步骤:
1. 定义状态 state,即 data。
2. 定义 mutations,修改 state 的唯一方法。
3. 定义 actions,提交 mutation。可以在 action 中执行异步操作。
4. 获取状态:在 Vue 组件中使用 this.$store.state 获取状态,使用 this.$store.getters 获取 getter 计算值。
5. 内置 getter 计算属性,类似于 Vue 的 computed。
6. 通过 dispatch 方法分发 action,即 this.$store.dispatch('action 名', 数据)。
7. 在 mutations 中修改 state,this.$store.commit('mutation 名', 数据)。
8. 使用 modules 将 store 分割成模块。
这就是 Vuex 的基本内容,如果有任何疑问可以随时向我提问!


## 插值表达式  指令 计算属性和侦听器
插值表达式:
在Vue中，插值表达式是一种将数据绑定到模板中的方法。它使用双大括号{{}}将表达式包裹起来，并将其放置在HTML标签中。当Vue实例中的数据发生变化时，插值表达式会自动更新页面上的内容。
例如，如果有一个数据属性message: "Hello, Vue!"，可以在模板中使用插值表达式将其显示在页面上：
```js
<div>{{ message }}</div>
```
指令:
指令是Vue中的特殊属性，用于在模板中添加交互和动态行为。指令以v-开头，后面跟着指令的名称。指令可以用于控制DOM元素的显示、隐藏、样式、事件等。
例如，v-if指令用于根据条件来显示或隐藏元素：
```
<div v-if="showMessage">Hello, Vue!</div>
```
计算属性:
计算属性是Vue中一种便利的属性，用于在模板中动态计算并返回一个值。计算属性会根据依赖的数据属性自动更新，并且具有缓存功能，只有在依赖的属性发生变化时才会重新计算。
例如，有一个数据属性firstName和lastName，可以使用计算属性来动态计算fullName：
```js
data() {
  return {
    firstName: 'John',
    lastName: 'Doe'
  };
},
computed: {
  fullName() {
    return this.firstName + ' ' + this.lastName;
  }
}
```
在模板中使用计算属性：
```js
<div>{{ fullName }}</div>
```
侦听器:
侦听器是Vue中一种用于监听数据变化并执行相应逻辑的方法。可以通过使用watch选项来定义侦听器，当监听的数据发生变化时，侦听器会被触发并执行相应的函数。
例如，有一个数据属性message，可以使用侦听器来监听该属性的变化：
```js
data() {
  return {
    message: 'Hello, Vue!'
  };
},
watch: {
  message(newVal, oldVal) {
    console.log('Message changed from ' + oldVal + ' to ' + newVal);
  }
}
```
当message的值发生变化时，侦听器会打印出相应的消息。

### Class和Style绑定
在Vue中，可以使用class和style绑定来动态地添加或移除CSS类和样式。
Class绑定:
通过v-bind:class指令可以将一个对象或数组绑定到元素的class属性上。对象的属性名对应CSS类名，属性值为布尔值，决定是否应用该类。数组中的每个元素都是CSS类名，它们会被应用到元素上。
例如，有一个数据属性isRed，如果为true，则应用red类，可以使用class绑定来实现：
```html
<div v-bind:class="{ red: isRed }">This is a red div</div>
```
当isRed为true时，div元素会应用red类。
Style绑定:
通过v-bind:style指令可以将一个对象或数组绑定到元素的style属性上。对象的属性名对应CSS属性名，属性值为对应的CSS属性值。数组中的每个元素都是一个对象，包含CSS属性名和属性值。
例如，有一个数据属性fontSize，可以使用style绑定来动态改变字体大小：
```html
<div v-bind:style="{ fontSize: fontSize + 'px' }">This div has a dynamic font size</div>
```
当fontSize发生变化时，div元素的字体大小会相应地改变。
同时绑定class和style:
可以同时使用class绑定和style绑定来动态地添加CSS类和样式。
```html
<div v-bind:class="{ red: isRed }" v-bind:style="{ fontSize: fontSize + 'px' }">This is a red div with dynamic font size</div>
```
根据isRed的值，div元素会应用或移除red类；根据fontSize的值，div元素的字体大小会相应地改变。

> 实际开发中推荐Class绑定,让样式可以重用 

### 表单输入绑定

v-bind和v-on是Vue中常用的指令，用于绑定属性和处理事件。
v-bind指令用于将Vue实例中的数据属性与HTML元素的属性进行绑定。它可以动态地设置HTML元素的属性值，例如class、style、src等。通过v-bind指令，可以实现属性值的动态更新。
v-on指令用于监听HTML元素的事件，并在事件触发时执行相应的方法。它可以绑定事件处理函数，例如click、input、submit等。通过v-on指令，可以实现事件的响应和处理逻辑。
下面是v-bind、v-on和v-model的区别的表格展示：

| 指令   | 作用                                    | 用法示例                                                             |
|--------|-----------------------------------------|----------------------------------------------------------------------|
| v-bind | 将Vue实例中的数据属性与HTML属性进行绑定 | `<div v-bind:class="className"></div>`                             |
| v-on   | 监听HTML元素的事件                      | `<button v-on:click="handleClick">Click me</button>`                |
| v-model| 实现表单输入的双向绑定                    | `<input v-model="message" type="text">`                             |

这三个指令在Vue中常用于实现数据与视图的交互和动态更新。


对比项   |  Vue  |  React  
:--  |:--  |:--  
状态管理   |  vuex  |  redux   
路由管理   |  vue-router  |  react-router 
响应式系统   |  依赖观察者模式  |  使用setState() 
渲染机制   |  虚拟DOM+差异算法  |  虚拟DOM+差异算法 
组件化   |  支持  |  支持 
生命周期   |  created、mounted等  |  componentDidMount等 
语法   |  template、v-if等  |  jsx、if/else 
灵活度   |  Options API 与 Composition API 可以选择  |  Hooks提供更大的灵活度 
易用性   |  易学易用,学习曲线较低  |  技术门槛较高,需要掌握JSX和ES6 
移动端适配   |  适配性较好,可与Weex等结合使用  |  需要react-native 
SE端渲染)支持较好   |  需要一定的配置 


 以下是Vuex和Redux的对比:
 
对比项   |  Vuex  |  Redux  
:--  |:--  |:--  
状态管理方案   |  专为Vue.js开发的状态管理库  |  可与React或其他视图库结合使用的状态管理框架 
核心概念   |  State、Getter、Mutation、Action、Module   |  State、Reducer、Store、Dispatch 
状态存储   |  对象形式存储  |  一棵对象树形式存储 
核心API   |  commit mutation、dispatch action、get getters   |  dispatch action、getState、subscribe 
修改状态   |  只能通过mutation修改  |  可以通过reducer函数修改 
异步操作   |  在action中执行  |  在reducer中执行或使用中间件执行 
模块化   |  支持模块化管理  |  支持按照域拆分为多个store 
开发者工具   |  vue-devtools  |  redux-devtools 
适用场景   |  较小或中型的单页面应用  |  大型单页面应用或同构应用 
从上表可以看出,Vuex和Redux虽然都用于管理应用状态,但在实现方式、使用场景等方面有较大差异:
• Vuex是Vue生态系统中的一员,专为Vue.js开发的状态管理库,易于和Vue集成;Redux是与具体视图无关的状态管理框架,可以和React以外的其他视图库结合使用。
• Vuex的核心概念和API都比较简单易用;Redux的概念和API相对复杂,需要理解reducer、store、dispatch等。
• Vuex只允许通过mutation来修改状态;Redux可以通过reducer函数修改状态,操作更为灵活。
• Vuex更适用于中小型的单页面应用;Redux有着更强大的功能,可用于大型复杂应用的状态管理。
总体来说,Vuex是入门级的状态管理方案,易学易用,而Redux则功能更为强大,适用于复杂应用,但会复杂一些。具体使用还是根据自己的项目来选择合适的状态管理库。
如果有不理解的地方,可以随时问我。希望这份内容和对比可以帮助您更好地理解Vuex和Redux!



### Vue Router使用步骤
 Vue Router是Vue.js官方的路由管理器。它和 Vue.js 的核心深度集成,让构建单页面应用变得易如反掌。
使用Vue Router的步骤如下:
1. 安装Vue Router
使用npm安装Vue Router:
```
npm install vue-router
```
2. 创建Router实例
在项目入口文件中,创建Router实例:
```js
import VueRouter from 'vue-router'
const router = new VueRouter({
  routes: [
    { path: '/', component: Home },
    { path: '/about', component: About }
  ]
})
```
routes选项用于配置路由规则,每个规则都需要有path和component。
3. 注册Router
在创建Vue实例之前,需要使用Vue.use()方法注册路由:
```js
Vue.use(VueRouter)
```
4. 添加路由到根实例
在创建Vue根实例时,需要将router对象传递进去:
```js
const app = new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
```
5. 配置路由链接
在模板中使用`<router-link>`组件来配置路由链接:
```html
<router-link to="/">Home</router-link>
<router-link to="/about">About</router-link>
```
6. 渲染路由组件
使用`<router-view>`组件来渲染路由匹配的组件:
```html
<router-view></router-view>
```
7. 启动应用
以上步骤完成后,就可以启动Vue应用,页面会根据URL显示对应的路由组件。
使用Vue Router,可以方便地实现单页面应用的不同页面之间的切换。


### 动态路由传参
通过占位来匹配变化的位置
`path:'/detail/:id'`
路由懒加载(非首页)
路由懒加载是一种优化技术，用于按需加载路由组件。它可以减小初始加载的文件大小，提高应用的性能。
使用路由懒加载的步骤如下：
1. 安装 `@babel/plugin-syntax-dynamic-import` 插件：
   
   ```bash
   npm install @babel/plugin-syntax-dynamic-import --save-dev
   ```
2. 在 .babelrc 文件中配置插件：
   
   ```json
   {
     "plugins": ["@babel/plugin-syntax-dynamic-import"]
   }
   ```
3. 在路由配置中使用动态导入语法：
   ```js
   const Home = () => import('./views/Home.vue')
   const About = () => import('./views/About.vue')
   const router = new VueRouter({
     routes: [
       { path: '/', component: Home },
       { path: '/about', component: About }
     ]
   })
   ```
   在上述代码中，`import()` 是动态导入语法，它会返回一个 Promise 对象，当路由被访问时，才会加载对应的组件。
4. 编译和打包应用
   
   使用构建工具（如Webpack）编译和打包应用时，会自动将使用动态导入语法的路由组件拆分为单独的文件，并在需要时按需加载。
通过路由懒加载，可以将路由组件的加载延迟到实际需要时再进行，减小初始加载的文件大小，提高应用的响应速度和性能。注意，在使用路由懒加载时，确保构建工具正确配置和处理动态导入语法。

在 `index.js` 中，`const routes = []` 是定义路由规则的数组。每个路由规则对象都包含 `path` 和 `component` 属性。
以下是 `const routes = []` 的格式写法示例：
```js
import Home from './components/Home.vue'
import About from './components/About.vue'
const routes = [
  { path: '/', component: Home },
  { path: '/about', component: About }
]
export default routes
```
在上述示例中，`routes` 数组包含两个路由规则对象，一个用于根路径 `'/'`，另一个用于 `'/about'` 路径。`component` 属性指定了对应的组件，例如 `Home` 和 `About`。
可以根据项目需求，继续添加更多的路由规则对象到 `routes` 数组中。每个路由规则对象定义了一个路径和对应的组件。在创建 `VueRouter` 实例时，将 `routes` 数组作为参数传递进去，即可配置应用的路由规则。
注意：在实际项目中，可以将路由规则定义在单独的文件中，然后通过 `import` 导入并传递给 `VueRouter` 实例。这样可以更好地组织和维护路由规则。

要将 `component: About` 改为懒加载，可以使用动态导入语法和路由懒加载的方式。下面是将 `component: About` 改为懒加载的示例代码：
```js
const routes = [
  { path: '/', component: () => import('./components/Home.vue') },
  { path: '/about', component: () => import('./components/About.vue') }
]
```
在上述代码中，使用 `() => import()` 来定义懒加载的组件。当 `/about` 路径被访问时，才会动态加载 `About.vue` 组件。
通过使用懒加载，可以将路由组件的加载延迟到实际需要时再进行，以提高应用的性能和加载速度。确保构建工具正确配置和处理动态导入语法，以便将懒加载的组件拆分为单独的文件，并在需要时按需加载。


### 动态路由传参
在Vue Router中，可以通过两种方式来获取动态路由参数：使用 `$route.params` 和使用路由组件的 `props` 属性。
1. 使用 `$route.params`:
   `$route.params` 是一个包含动态路由参数的对象，可以通过访问其属性来获取具体的参数值。
   例如，如果有一个动态路由路径为 `/user/:id`，可以通过 `$route.params.id` 来获取 `id` 参数的值。
```javascript
   // 路由定义
   const routes = [
     { path: '/user/:id', component: User }
   ];
   // 在组件中获取动态路由参数
   export default {
     mounted() {
       const userId = this.$route.params.id;
       console.log('User ID:', userId);
     }
   }
   ```
   在上述示例中，通过 `this.$route.params.id` 获取了动态路由参数 `id` 的值。
2. 使用路由组件的 `props` 属性:
   可以通过将路由参数设置为组件的 `props` 属性，将参数作为组件的属性传递给路由组件。
 ```javascript
   // 路由定义
   const routes = [
     { path: '/user/:id', component: User, props: true }
   ];
   // 在组件中接收路由参数作为属性
   export default {
     props: ['id'],
     mounted() {
       console.log('User ID:', this.id);
     }
   }
   ```
   在上述示例中，将 `props` 属性设置为 `true`，表示将路由参数作为组件的属性传递。然后在组件中，可以使用 `this.id` 来获取动态路由参数的值。
这两种方式都可以用来获取动态路由参数的值，选择使用哪种方式取决于具体的需求和代码结构。使用 `$route.params` 更适合在组件内部获取和处理动态路由参数，而使用 `props` 属性更适合将参数作为组件的属性传递给子组件使用。
`推荐第二种方式- 属性传递`

### Layout

![[assets/img/Vue基础/IMG-Vue基础-20240714124833410.png]]
![[assets/img/Vue基础/IMG-Vue基础-20240714124836115.png]]
### 嵌套路由
![[assets/img/Vue基础/IMG-Vue基础-20240714124836923.png]]

### 编程式导航

编程式导航是指通过编程方式在Vue应用中进行页面跳转。Vue Router提供了一些方法来实现编程式导航。
以下是使用Vue Router进行编程式导航的示例代码：
1. 使用 `$router.push` 方法进行导航：
```javascript
// 在组件中进行导航
export default {
  methods: {
    goToAboutPage() {
      this.$router.push('/about');
    }
  }
}
```
在上述代码中，通过调用 `this.$router.push` 方法，可以导航到指定的路径，例如 `/about`。
2. 使用 `$router.replace` 方法进行导航：
```javascript
// 在组件中进行导航
export default {
  methods: {
    goToHomePage() {
      this.$router.replace('/');
    }
  }
}
```
与 `$router.push` 方法类似，`$router.replace` 方法也可以用于进行页面导航，但是它不会生成新的历史记录。
3. 使用 `$router.go` 方法进行导航：
```javascript
// 在组件中进行导航
export default {
  methods: {
    goBack() {
      this.$router.go(-1); // 返回上一页
    }
  }
}
```
通过调用 `this.$router.go` 方法，并传递一个整数参数，可以在浏览器的历史记录中前进或后退指定的步数。
通过以上方法，可以在Vue应用中实现编程式导航，根据业务需求进行页面跳转和导航操作。注意，在使用这些方法之前，确保已经正确配置和初始化了Vue Router。
![[assets/img/Vue基础/IMG-Vue基础-20240714124837326.png]]
也可以使用命名式导航
![[assets/img/Vue基础/IMG-Vue基础-20240714124837743.png]]

### History VS Hash模式
![[assets/img/Vue基础/IMG-Vue基础-20240714124838143.png]]
`Histroy模式需要服务端支持`
![[assets/img/Vue基础/IMG-Vue基础-20240714124838494.png]]
通过pushState()可以实现客户端路由(与push()对比)
#### 客户端路由
在前端开发中，客户端路由是一种在浏览器中进行页面导航和路由管理的方式。它可以通过JavaScript来控制页面的跳转，而不需要每次请求新页面的HTML。
客户端路由的工作原理如下：
1. 初始加载：当用户首次访问应用时，服务器会返回一个包含基本HTML结构和JavaScript代码的初始页面。
2. 路由配置：在JavaScript代码中，通过路由库（如Vue Router、React Router等）进行路由配置。这包括定义路由规则、注册路由组件等。
3. 导航操作：当用户点击链接或执行某些交互操作时，JavaScript代码会根据路由配置进行相应的导航操作。
4. 页面更新：根据导航操作，路由库会执行相应的逻辑，根据路由规则匹配到对应的组件并渲染到页面上，更新页面的内容。
5. URL变化：路由库会使用浏览器的History API（如pushState、replaceState）来修改URL，并将当前路由状态保存在URL中，以便用户可以直接访问或添加到书签中。
6. 前进/后退：当用户点击浏览器的前进或后退按钮时，路由库会监听浏览器的popstate事件，并根据URL的变化执行相应的导航操作。
客户端路由的优势包括：
- 单页面应用（SPA）：客户端路由适用于单页面应用，可以在不刷新整个页面的情况下实现页面切换和更新，提供更流畅的用户体验。
- 动态加载：客户端路由可以根据需要动态加载页面组件，减小初始加载的文件大小，提高应用的性能。
- 前进/后退：通过监听浏览器的前进/后退按钮，客户端路由可以实现无刷新的页面切换，使用户可以方便地导航页面历史记录。
总结起来，客户端路由是一种在浏览器中进行页面导航和路由管理的方式，通过JavaScript动态控制页面的切换和更新，以提供更好的用户体验和性能优化。
#### 其他
除了客户端路由（前端路由），还有以下几种常见的路由类型：

| 路由类型               | 描述                                                                                                       |
|----------------------|------------------------------------------------------------------------------------------------------------|
| 服务器端路由（后端路由） | 在服务器端进行路由控制和页面渲染。当用户请求不同的URL时，服务器根据URL匹配路由规则，并返回相应的HTML页面。           |
| 嵌入式路由             | 在嵌入式系统中使用的路由方式，通常用于物联网设备、嵌入式设备等。在设备内部进行路由控制和数据交换。                       |
| 逆向代理路由           | 逆向代理服务器根据请求的URL将请求转发给不同的后端服务器，实现负载均衡和请求转发的路由方式。常见的逆向代理服务器有Nginx。 |
| VPN路由               | VPN（Virtual Private Network）路由是一种通过VPN隧道进行路由通信的方式。通过VPN连接的网络将根据路由规则进行数据传输。       |
| 隧道路由               | 隧道路由是一种在网络中通过隧道进行数据传输的路由方式。通过在网络层封装数据包，将数据从一个网络传输到另一个网络。          |
![[assets/img/Vue基础/IMG-Vue基础-20240714124838803.png]]
![[assets/img/Vue基础/IMG-Vue基础-20240714124839340.png]]

![[assets/img/Vue基础/IMG-Vue基础-20240714124839696.png]]
![[assets/img/Vue基础/IMG-Vue基础-20240714124840058.png]]

> Vue CLI 自带的web服务器已经配置好了对`history`的支持

![[assets/img/Vue基础/IMG-Vue基础-20240714124840459.png]]






<Vue.js设计与实现> 霍春阳




组件就是一组 DOM 元素的封装，这组 DOM 元素就是组件要渲染的内容，因此我们可以定义一个函数来代表组件，而函数的返回值就代表组件要渲
染的内容：
```tsx
01 const MyComponent = function () { 
02   return { 
03     tag: 'div', 
04     props: { 
05       onClick: () => alert('hello') 
06     }, 
07     children: 'click me' 
08   } 
09 }
```
例如组件一定得是函数吗？当
然不是，我们完全可以使用一个 JavaScript 对象来表达组件，

```tsx
01 // MyComponent 是一个对象 
02 const MyComponent = { 
03   render() { 
04     return { 
05       tag: 'div', 
06       props: { 
07         onClick: () => alert('hello') 
08       }, 
09       children: 'click me' 
10     } 
11   } 
12 }
```
  以我们熟悉的 .vue 文件为例，一个 .vue 文件就是一个组件

```vue
01 <template> 
02   <div @click="handler"> 
03     click me 
04   </div> 
05 </template> 
06 
07 <script> 
08 export default { 
09   data() {/* ... */}, 
10   methods: { 
11     handler: () => {/* ... */} 
12   } 
13 } 
14 </script>
```

```
其中 <template> 标签里的内容就是模板内容，编译器会把模板内容
编译成渲染函数并添加到 <script> 标签块的组件对象上，所以最终
在浏览器里运行的代码就是：
```

```jsx
01 export default { 
02   data() {/* ... */}, 
03   methods: { 
04     handler: () => {/* ... */} 
05   }, 
06   render() { 
07     return h('div', { onClick: handler }, 'click me') 
08   } 
09 }
```


## 声明式地描述UI
DOM 元素：例如是 div 标签还是 a 标签。
属性：如 a 标签的 href 属性，再如 id、class 等通用属性。
事件：如 click、keydown 等。
元素的层级结构：DOM 树的层级结构，既有子节点，又有父节
点。

- 使用 : 或 v-bind 来描述动态绑定的属性，例如 `<div :id="dynamicId"></div>；`
使用 @ 或 v-on 来描述事件，例如点击事件 `<div @click="handler"></div>`；

 除了上面这种使用模板来声明式地描述 UI 之外，我们还可以用JavaScript 对象来描述，代码如下所示：
```js
01 const title = { 
02   // 标签名称 
03   tag: 'h1', 
04   // 标签属性 
05   props: { 
06     onClick: handler 
07   }, 
08   // 子节点 
09   children: [ 
10     { tag: 'span' } 
11   ] 
12 }
```
    对应到 Vue.js 模板，其实就是：
```js
01 <h1 @click="handler"><span></span></h1>
```
 那么，使用模板和 JavaScript 对象描述 UI 有何不同呢？答案是：使用 JavaScript 对象描述 UI 更加灵活。
而使用 JavaScript 对象来描述 UI的方式，其实就是所谓的虚拟 DOM。
是虚拟 DOM，它其实就是用 JavaScript对象来描述真实的 DOM 结构。

## 第二篇 响应系统



## 组件间通信

常用的方法有：

|方案|父组件向子组件|子组件向父组件|对应章节传送门|
|---|---|---|---|
|props / emits|props|emits|[点击查看](https://vue3.chengpeiquan.com/communication.html#props-emits)|
|v-model / emits|v-model|emits|[点击查看](https://vue3.chengpeiquan.com/communication.html#v-model-emits)|
|ref / emits|ref|emits|[点击查看](https://vue3.chengpeiquan.com/communication.html#ref-emits)|
|provide / inject|provide|inject|[点击查看](https://vue3.chengpeiquan.com/communication.html#provide-inject)|
|EventBus|emit / on|emit / on|[点击查看](https://vue3.chengpeiquan.com/communication.html#eventbus-new)|
|Reative State|-|-|[点击查看](https://vue3.chengpeiquan.com/communication.html#reative-state-new)|
|Vuex|-|-|[点击查看](https://vue3.chengpeiquan.com/communication.html#vuex-new)|
|Pinia|-|-|[点击查看](https://vue3.chengpeiquan.com/pinia.html)|

 
 
 
 createApp 和 defineComponent 在 Vue3 中的联系和区别:
- createApp 是用来创建一个 Vue 应用实例的,它返回一个应用实例对象。
- defineComponent 是用来定义一个组件选项对象的,它返回一个组件定义对象。
联系:
- createApp 返回的应用实例可以使用 app.component 方法注册组件。
- defineComponent 定义的组件可以直接传给 createApp,作为应用实例的根组件使用。
区别:
- createApp 是创建整个 Vue 应用实例,defineComponent 只是定义一个组件。
- createApp 返回应用实例对象,defineComponent 返回组件定义对象。
- createApp 需要手动调用 app.mount 挂载应用,defineComponent 不需要。
使用示例:
```js
// 定义组件
const app = defineComponent({
  // 组件定义
})
// 创建应用实例并挂载组件
createApp(app).mount('#app')
```
所以总结:
- createApp 创建应用实例
- defineComponent 定义组件
- 两者可以结合使用来创建一个基于定义组件的 Vue 应用

defineComponent 是 Vue 3 中定义组件的新方法。
### defineComponent 的主要作用:
- 定义一个组件选项对象,等同于 Vue.component 或 new Vue() 中的组件定义对象。
- 它可以更好地支持 TypeScript,提供类型定义文件。
### 定义组件的方式:
```ts
import { defineComponent } from 'vue'
export default defineComponent({
  // 组件选项
})
```
### 与 Vue.component 对比:
- Vue.component 返回值是组件构造函数,defineComponent 返回值是组件定义对象。
- defineComponent 可以获得更好的 TS 支持,如 prop 类型检查。
- 它不需要手动调用 Vue.component 注册组件。
### 使用场景:
- 定义全局组件时,使用 Vue.component() 
- 定义单文件组件时,使用 defineComponent
- 在组件内定义子组件时,使用 defineComponent
所以总之,defineComponent 是 Vue3 中定义组件的主要方法,它可以获得更好的 TS 支持,是推荐的组件定义方式。


## 插槽[​](https://vue3.chengpeiquan.com/component.html#%E6%8F%92%E6%A7%BD)

Vue 在使用子组件的时候，子组件在 template 里类似一个 HTML 标签，可以在这个子组件标签里传入任意模板代码以及 HTML 代码，这个功能就叫做 “插槽” 。


#### 钩子函数[​](https://vue3.chengpeiquan.com/component.html#%E9%92%A9%E5%AD%90%E5%87%BD%E6%95%B0)

和 [组件的生命周期](https://vue3.chengpeiquan.com/component.html#%E7%BB%84%E4%BB%B6%E7%9A%84%E7%94%9F%E5%91%BD%E5%91%A8%E6%9C%9F-new) 类似，自定义指令里的逻辑代码也有一些特殊的调用时机，在这里称之为钩子函数：

|钩子函数|调用时机|
|---|---|
|created|在绑定元素的 attribute 或事件侦听器被应用之前调用|
|beforeMount|当指令第一次绑定到元素并且在挂载父组件之前调用|
|mounted|在绑定元素的父组件被挂载后调用|
|beforeUpdate|在更新包含组件的 VNode 之前调用|
|updated|在包含组件的 VNode 及其子组件的 VNode 更新后调用|
|beforeUnmount|在卸载绑定元素的父组件之前调用|
|unmounted|当指令与元素解除绑定且父组件已卸载时，只调用一次|

#### 了解 Vue 3[​](https://vue3.chengpeiquan.com/component.html#%E4%BA%86%E8%A7%A3-vue-3-1)

在 Vue 3 的组合式 API 写法， `watch` 是一个可以接受 3 个参数的函数（保留了 Vue 2 的 `this.$watch` 这种用法），在使用层面上简单了很多。

```ts
import { watch } from 'vue'

// 一个用法走天下
watch(
  source, // 必传，要侦听的数据源
  callback // 必传，侦听到变化后要执行的回调函数
  // options // 可选，一些侦听选项
)
```

下面的内容都基于 Vue 3 的组合式 API 用法展开讲解。

在 Vue 3 则灵活了很多，可以使用普通函数、 Class 类、箭头函数、匿名函数等等进行声明，可以将其写在 `setup` 里直接使用，也可以抽离在独立的 `.js` / `.ts` 文件里再导入使用。

需要在组件创建时自动执行的函数，其执行时机需要遵循 Vue 3 的生命周期，需要在模板里通过 `@click`、`@change` 等行为触发，和变量一样，需要把函数名在 `setup` 里进行 `return` 出去。

下面是一个简单的例子，方便开发者更直观地了解：

``` vue
<template>
  <p>{{ msg }}</p>

  <!-- 在这里点击执行 `return` 出来的方法 -->
  <button @click="updateMsg">修改MSG</button>
</template>

<script lang="ts">
import { defineComponent, onMounted, ref } from 'vue'

export default defineComponent({
  setup() {
    const msg = ref<string>('Hello World!')

    // 这个要暴露给模板使用，必须 `return` 才可以使用
    function updateMsg() {
      msg.value = 'Hi World!'
    }

    // 这个要在页面载入时执行，无需 `return` 出去
    const init = () => {
      console.log('init')
    }

    onMounted(() => {
      init()
    })

    return {
      msg,
      updateMsg,
    }
  },
})
</script>
```


```tsx
// 这里导入的 `ref` 是一个响应式 API
import { defineComponent, ref } from 'vue'

export default defineComponent({
  setup() {
    // 通过响应式 API 创建的变量具备了响应性
    const msg = ref<string>('Hello World!')
  },
})
```


## 组件选项
组件选项是指在定义 Vue 组件时可以配置的各种属性和钩子函数。
主要的组件选项包括:
- el:字符串,用于挂载元素选择器或元素引用
- data:函数,返回一个对象用于定义组件的数据
- props:数组或对象,用于定义组件接受的外部属性
- computed:对象,用于定义计算属性
- methods:对象,用于定义组件的方法
- watch:对象,用于定义监听的属性 
- template:字符串或模板函数,用于定义组件的模板
- render:函数,用于自定义渲染逻辑
- components:对象,用于注册子组件
- mixins:数组,用于混入其他组件
- directives:对象,用于注册自定义指令
- filters:对象,用于注册过滤器
- beforeCreate、created等生命周期钩子
- provide/inject:提供注入其他组件
所以组件选项主要包括组件相关的配置、数据、方法、生命周期等属性,这些选项定义了组件的功能和行为。
正确使用组件选项可以让组件具备更强大的功能,比如数据、方法的封装,生命周期管理等。


[了解前端工程化 | Vue3 入门指南与实战案例 (chengpeiquan.com)](https://vue3.chengpeiquan.com/engineering.html)

工程化后的项目结构非常清晰和统一，以 Vue 项目来说，通过脚手架创建一个新项目之后，它除了提供能直接运行 Hello World 的基础代码之外，还具备了如下的统一目录结构：

- `src` 是源码目录
- `src/main.ts` 是入口文件
- `src/views` 是路由组件目录
- `src/components` 是子组件目录
- `src/router` 是路由目录

 路由组件目录和路由配置目录在Vue项目中有以下区别:
路由组件目录:
- 存放各个路由对应的组件代码。
- 通常放在src/views目录下。
- 每个路由组件是一个单独的Vue组件文件。
- 路由匹配到组件后渲染对应的组件视图。
路由配置目录:
- 存放路由匹配规则和配置的地方。
- 通常放在src/router/index.js文件。
- 通过routes配置路由表,定义各个路由路径。 
- 通过组件来源映射,将路由路径关联到组件文件。
区别在于:
- 路由组件目录存放各路由对应的组件代码实现。
- 路由配置目录定义路由规则,映射路由到组件上。
两者结合使用:
- 路由配置引入并映射组件来源。
- 匹配到路径后渲染组件,实现组件间切换。
所以简单来说,路由组件目录存放组件代码,路由配置目录定义路由规则。两者配合使用实现单页应用路由功能。
```vue
<template>
  <div class="list">
    <!-- 这个循环模板有很多属性 -->
    <div class="item" :class="{ `top-${index + 1}`: index < 3 }" v-for="(item, index)
    in list" :key="item.id" @click="handleClick(item.id)">
      <span>{{ item.text }}</span>
    </div>
    <!-- 这个循环模板有很多属性 -->
  </div>
</template>
```
而工程化配合统一的代码格式化规范，可以让不同人维护的代码，最终提交到 Git 上的时候，风格都保持一致，并且类似这种很多属性的地方，都会自动帮格式化为一个属性一行，维护起来就很方便：
```vue
<template>
  <div class="list">
    <!-- 这个循环模板有很多属性 -->
    <div
      class="item"
      :class="{ `top-${index + 1}`: index < 3 }"
      v-for="(item, index) in list"
      :key="item.id"
      @click="handleClick(item.id)"
    >
      <span>{{ item.text }}</span>
    </div>
    <!-- 这个循环模板有很多属性 -->
  </div>
</template>
```

在工程化项目这些问题都可以交给程序去处理，在书写代码的时候，开发者可以先按照自己的习惯书写，然后再执行命令进行格式化，或者是在提交代码的时候配合 Git Hooks 自动格式化，都可以做到统一风格。


#### 团队开发效率高[​](https://vue3.chengpeiquan.com/engineering.html#%E5%9B%A2%E9%98%9F%E5%BC%80%E5%8F%91%E6%95%88%E7%8E%87%E9%AB%98)

在前后端合作环节，可以提前 Mock 接口与后端工程师同步开发，如果遇到跨域等安全限制，也可以进行本地代理，不受跨域困扰。

Vue 的这种编程方式，称之为 “数据驱动” 编程。
Vue 3.0 版本还引入了组合式 API 的概念，更符合软件工程 “高内聚，低耦合” 的思想，让开发者可以更灵活的管理自己的逻辑代码，更方便的进行抽离封装再复用，不管是大型项目还是流水线业务，开箱即用的逻辑代码都是提升开发效率的利器。

Vue.js 是一个框架，框架除了简化编码过程中的复杂度之外，面对不同的业务需求还提供了通用的解决方案，而这些解决方案，通常是将前端工程化里的很多种技术栈组合起来串成一条条技术链，一环扣一环，串起来就是一个完整的工程化项目。

Vue 提供了 Vue Router 实现路由功能，利用 [History API](https://developer.mozilla.org/zh-CN/docs/Web/API/History_API) 实现单页面模式（可在 [现代化的开发概念](https://vue3.chengpeiquan.com/engineering.html#%E7%8E%B0%E4%BB%A3%E5%8C%96%E7%9A%84%E5%BC%80%E5%8F%91%E6%A6%82%E5%BF%B5) 部分了解区别），在一个 HTML 页面里也可以体验 “页面跳转” 这样的体验，但如果页面很多，所有代码都堆积在一个 HTML 页面里，就很难维护。
借助前端工程化的构建工具，开发者可以编写 `.vue` 单组件文件，将多个页面的代码根据其功能模块进行划分，可拆分到多个单组件文件里维护并进行合理复用，最终通过构建工具编译再合并，最终生成浏览器能访问的 HTML / CSS / JS 文件，这样的开发过程，用户体验没有影响，但开发体验大大提升。
类似这样一个个业务场景会积少成多，把 Vue 和工程化结合起来，处理问题更高效更简单。

```tsx
TIP

网页的 TKD 三要素是指一个网页的三个关键信息，含义如下：

T ，指 Title ，网站的标题，即网页的 `<title>网站的标题</title>` 标签。

K ，指 Keywords ，网站的关键词，即网页的 `<meta name="Keywords" content="关键词1,关键词2,关键词3" />` 标签。

D ，指 Description ，网站的描述，即网页的 `<meta name="description" content="网站的描述" />` 标签。

这三个要素标签都位于 HTML 文件的 `<head />` 标签内。
```
如果是基于 PHP 等非前端语言开发，工作量通常更是压在一名开发者身上，无法做到前后端分离来利用好跨岗位协作。

```tsx
TIP

此处列举的多页面应用问题均指传统开发模式下的多页面，之所以特地说明，是因为后文还会有新的技术栈来实现多页面应用，但实现原理和体验并不一样。
```
SPA 单页面应用是现代化的网站体验，与 MPA 相反，不论站点内有多少个页面，在 SPA 项目实际上只有一个 HTML 文件，也就是 `index.html` 首页文件。

它只有第一次访问的时候才需要经历一次完整的页面请求过程，之后的每个内部跳转或者数据更新操作，都是通过 AJAX 技术来获取需要呈现的内容并只更新指定的网页位置。
```tsx
TIP

AJAX 技术（ Asynchronous JavaScript and XML ）是指在不离开页面的情况下，通过 JavaScript 发出 HTTP 请求，让网页通过增量更新的方式呈现给用户界面，而不需要刷新整个页面来重新加载，是一种 “无刷体验” 。
```
SPA 在页面跳转的时候，地址栏也会发生变化，主要有以下两种方式：

```tsx
1. 通过修改 [Location:hash](https://developer.mozilla.org/zh-CN/docs/Web/API/Location/hash) 修改 URL 的 Hash 值（也就是 `#` 号后面部分），例如从 `https://example.com/#/foo` 变成 `https://example.com/#/bar`
2. 通过 History API 的 [pushState](https://developer.mozilla.org/zh-CN/docs/Web/API/History/pushState) 方法更新 URL ，例如从 `https://example.com/foo` 变成 `https://example.com/bar`
```

```tsx
TIP

Vue Router 默认提供了这两种 URL 改变方式的支持，分别是 `createWebHashHistory` 的 Hash 模式和 `createWebHistory` 对应的 History 模式，在 [路由的使用](https://vue3.chengpeiquan.com/router.html) 一章可以学习更多 Vue 路由的使用。
```

这两个方式的共同特点是更新地址栏 URL 的时候，均不会刷新页面，只是单纯的变更地址栏的访问地址，而网页的内容则通过 AJAX 更新，配合起来就形成了一种网页的 “前进 / 后退” 等行为效果。

理解了实现原理之后，可以把 SPA 的请求过程简化为如下步骤：
```tsx
# SPA 页面跳转过程

从用户点击跳转开始：
---> 浏览器通过 `pushState` 等方法更新 URL
---> 请求接口数据（如果有涉及到前后端交互）
---> 通过 JavaScript 处理数据，拼接 HTML 片段
---> 把 HTML 片段渲染到指定位置，完成页面的 “刷新”
```

##### SPA 的优点[​](https://vue3.chengpeiquan.com/engineering.html#spa-%E7%9A%84%E4%BC%98%E7%82%B9)

从上面的实现原理已经能总结出它的优势了：

- 只有一次完全请求的等待时间（首屏加载）
- 用户体验好，内部跳转的时候可以实现 “无刷切换”
- 因为不需要重新请求整个页面，所以切换页面的时候速度更快
- 因为没有脱离当前页面，所以 “页” 与 “页” 之间在切换过程中支持动画效果
- 脱离了页面跳页面的框架，让整个网站形成一个 Web App ，更接近原生 App 的访问体验
- 开发效率高，前后端分离，后端负责 API 接口，前端负责界面和联调，同步进行缩短工期

这也是为什么短短几年时间， SPA 的体验模式成为前端领域的主流。

##### SPA 的缺点[​](https://vue3.chengpeiquan.com/engineering.html#spa-%E7%9A%84%E7%BC%BA%E7%82%B9)

虽然 SPA 应用在使用过程中的用户体验非常好，但也有自身的缺点存在：

- 首屏加载相对较慢

由于 SPA 应用的路由是由前端控制， SPA 在打开首页后，还要根据当前的路由再执行一次内容渲染，相对于 MPA 应用从服务端直出 HTML ，首屏渲染所花费的时间会更长。

- 不利于 SEO 优化

由于 SPA 应用全程是由 JavaScript 控制内容的渲染，因此唯一的一个 HTML 页面 `index.html` 通常是一个空的页面，只有最基础的 HTML 结构，不仅无法设置每个路由页面的 TDK ，页面内容也无法呈现在 HTML 代码里，因此对搜索引擎来说，网站的内容再丰富，依然只是一个 “空壳” ，无法让搜索引擎进行内容爬取。

### CSR 与 SSR[​](https://vue3.chengpeiquan.com/engineering.html#csr-%E4%B8%8E-ssr)

在了解了 MPA 与 SPA 之后，先了解另外两个有相关联的名词： CSR 与 SSR ，同样的，这一对也是代表着相反的开发模式和用户体验，它们的全称和中文含义如下：

|名词|全称|中文|
|---|---|---|
|CSR|Client-Side Rendering|客户端渲染|
|SSR|Server-Side Rendering|服务端渲染|

正如它们的名称，这两者代表的是渲染网页过程中使用到的技术栈。

既然原来的技术方案无法完美满足项目需求，因此在结合 MPA 的优点和 SPA 的优点之后，一种新的技术随之诞生，这就是 SSR 服务端渲染。

#### 服务端渲染[​](https://vue3.chengpeiquan.com/engineering.html#%E6%9C%8D%E5%8A%A1%E7%AB%AF%E6%B8%B2%E6%9F%93)

和传统的 MPA 使用 PHP / JSP 等技术栈做服务端渲染不同，现代前端工程化里的 SSR 通常是指使用 Node.js 作为服务端技术栈。
```tsx
TIP

在 [工程化神器 Node.js]一节会介绍 Node ，以及它对前端工程化带来的重大变化，现代前端工程化发展离不开它的存在。
```
传统的服务端渲染通常由后端开发者一起维护前后端代码，需要写后端语言支持的模板、 JavaScript 代码维护成本也比较高；而 SSR 服务端渲染则是交给前端开发者来维护，利用 Node 提供的能力进行同构渲染，由于本身前后端都使用 JavaScript 编写，维护成本也大大的降低。

SSR 技术利用的同构渲染方案（ Isomorphic Rendering ），指的是一套代码不仅可以在客户端运行，也可以在服务端运行，在一些合适的时机先由服务端完成渲染（ Server-Side Rendering ）再直出给客户端激活（ Client-Side Hydration ），这种开发模式带来了：

- 更好的 SEO 支持，解决了 SPA 单页面应用的痛点
- 更快的首屏加载速度，保持了 MPA 多页面应用的优点
- 和 SPA 一样支持前后端分离，开发效率依然很高
- 有更好的客户端体验，当用户完全打开页面后，本地访问过程中也可以保持 SPA 单页面应用的体验
- 统一的心智模型，由于支持同构，因此没有额外的心智负担

![使用 Pkg 构建后的程序运行截图](https://vue3.chengpeiquan.com/assets/img/screenshot-pkg-dark.jpg)

使用 Pkg 构建后的程序运行截图

在这里推荐一个工具 [Pkg](https://github.com/vercel/pkg) ，它可以把 Node 项目打包为一个可执行文件，支持 Windows 、 macOS 、 Linux 等多个平台，它的打包机制和 Electron 打包的思路类似，也是通过把 Node 一起打包，让用户可以在不安装 Node 环境的情况下也可以直接运行脚本程序。

## 实践工程化的流程[​](https://vue3.chengpeiquan.com/engineering.html#%E5%AE%9E%E8%B7%B5%E5%B7%A5%E7%A8%8B%E5%8C%96%E7%9A%84%E6%B5%81%E7%A8%8B)

基于 Vue 3 的项目，最主流的工程化组合拳有以下两种：

|常用方案|Runtime|构建工具|前端框架|
|---|---|---|---|
|方案一|Node|Webpack|Vue|
|方案二|Node|Vite|Vue|

方案一是比较传统并且过去项目使用最多的方案组合，但从 2021 年初随着 Vite 2.0 的发布，伴随着更快的开发体验和日渐丰富的社区生态，新项目很多都开始迁移到方案二，因此本书秉着面向当下与未来的原则，会侧重 Vite 的使用来开展讲解，包括一些 demo 的创建等等。

### 什么是 Runtime[​](https://vue3.chengpeiquan.com/engineering.html#%E4%BB%80%E4%B9%88%E6%98%AF-runtime)

Runtime ，可以叫它 “运行时” 或者 “运行时环境” ，这个概念是指，项目的代码在哪里运行，哪里就是运行时。

传统的 JavaScript 只能跑在浏览器上，每个浏览器都为 JS 提供了一个运行时环境，可以简单的把浏览器当成一个 Runtime ，明白了这一点，相信就能明白什么是 Node 。

Node 就是一个让 JS 可以脱离浏览器运行的环境，当然，这里并不是说 Node 就是浏览器。

### 为什么要使用构建工具[​](https://vue3.chengpeiquan.com/engineering.html#%E4%B8%BA%E4%BB%80%E4%B9%88%E8%A6%81%E4%BD%BF%E7%94%A8%E6%9E%84%E5%BB%BA%E5%B7%A5%E5%85%B7)

目前已经有很多流行的构建工具，例如： [Grunt](https://github.com/gruntjs/grunt) 、 [Gulp](https://github.com/gulpjs/gulp) 、 [Webpack](https://github.com/webpack/webpack) 、 [Snowpack](https://github.com/FredKSchott/snowpack) 、 [Parcel](https://github.com/parcel-bundler/parcel) 、 [Rollup](https://github.com/rollup/rollup) 、 [Vite](https://github.com/vitejs/vite) … 每一个工具都有自己的特色。

如上面列举的构建工具，虽然具体到某一个工具的时候，是 “一个” 工具，但实际上可以理解为是 “一套” 工具链、工具集，构建工具通常集 “语言转换 / 编译” 、 “资源解析” 、 “代码分析” 、 “错误检查” 、 “任务队列” 等非常多的功能于一身。

构建方面，为了更好的加载体验，以及 Tree Shaking 按需打包 、懒加载和 Chunk 分割利于缓存，两者都需要进行打包；但由于 Vite 是面向现代浏览器，所以如果的项目有兼容低版本浏览器的需求的话，建议还是用 Webpack 来打包，否则， Vite 是目前的更优解。

```jsx
TIP
在 CJS 和 ESM ，一个独立的文件就是一个模块，该文件内部的变量必须通过导出才能被外部访问到，而外部文件想访问这些变量，需要导入对应的模块才能生效。
```
```jsx
hello-node
│ # 源码文件夹
├─src
│ │ # 业务文件夹
│ └─cjs
│   │ # 入口文件
│   ├─index.cjs
│   │ # 模块文件
│   └─module.cjs
│ # 项目清单
└─package.json
```

这是一个常见的 Node 项目目录结构，通常源代码都会放在 `src` 文件夹里面统一管理。

接下来再修改一下 package.json 里面的 scripts 部分，改成如下：
```json
{
  "scripts": {
    "dev:cjs": "node src/cjs/index.cjs"
  }
}
```

后面在命令行执行 `npm run dev:cjs` 命令，就可以测试刚刚添加的 CJS 模块了


# 模块化设计

### CommonJS 模块化
#### 命名导出和导入[​](https://vue3.chengpeiquan.com/guide.html#%E5%91%BD%E5%90%8D%E5%AF%BC%E5%87%BA%E5%92%8C%E5%AF%BC%E5%85%A5)

默认导出的时候，一个模块只包含一个值，有时候如果想把很多相同分类的函数进行模块化集中管理，例如想做一些 utils 类的工具函数文件、或者是维护项目的配置文件，全部使用默认导出的话，会有非常多的文件要维护。

那么就可以用到命名导出，这样既可以导出多个数据，又可以统一在一个文件里维护管理，命名导出是先声明多个变量，然后通过 `{}` 对象的形式导出。

再来修改一下 `src/cjs/module.cjs` 文件，这次改成如下：

js

```
// src/cjs/module.cjs
function foo() {
  console.log('Hello World from foo.')
}

const bar = 'Hello World from bar.'

module.exports = {
  foo,
  bar,
}
```

这个时候通过原来的方式去拿模块的值，会发现无法直接获取到函数体或者字符串的值，因为打印出来的也是一个对象。


```js

// src/cjs/index.cjs
const m = require('./module.cjs')
console.log(m)
```

控制台输出：

```bash
npm run dev:cjs

> demo@1.0.0 dev:cjs
> node src/cjs/index.cjs

{ foo: [Function: foo], bar: 'Hello World from bar.' }
```

需要通过 `m.foo()` 、 `m.bar` 的形式才可以拿到值。

此时可以用一种更方便的方式，利用 ES6 的对象解构来直接拿到变量：


```js
// src/cjs/index.cjs
const { foo, bar } = require('./module.cjs')
foo()
console.log(bar)
```

这样子才可以直接调用变量拿到对应的值。

#### 导入时重命名[​](https://vue3.chengpeiquan.com/guide.html#%E5%AF%BC%E5%85%A5%E6%97%B6%E9%87%8D%E5%91%BD%E5%90%8D)

以上都是基于非常理想的情况下使用模块，有时候不同的模块之间也会存在相同命名导出的情况，来看看模块化是如何解决这个问题的。

`src/cjs/module.cjs` 文件保持不变，依然导出这两个变量：

```js
// src/cjs/module.cjs
function foo() {
  console.log('Hello World from foo.')
}

const bar = 'Hello World from bar.'

module.exports = {
  foo,
  bar,
}
```

这次在入口文件里也声明一个 `foo` 变量，在导入的时候对模块里的 `foo` 进行了重命名操作。

```js
// src/cjs/index.cjs
const {
  foo: foo2,  // 这里进行了重命名
  bar,
} = require('./module.cjs')

// 就不会造成变量冲突
const foo = 1
console.log(foo)

// 用新的命名来调用模块里的方法
foo2()

// 这个不冲突就可以不必处理
console.log(bar)
```

再次运行 `npm run dev:cjs` ，可以看到打印出来的结果完全符合预期：

```bash
npm run dev:cjs

> demo@1.0.0 dev:cjs
> node src/cjs/index.cjs

1
Hello World from foo.
Hello World from bar.
```

这是利用了 ES6 解构对象的 [给新的变量名赋值](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment#%E7%BB%99%E6%96%B0%E7%9A%84%E5%8F%98%E9%87%8F%E5%90%8D%E8%B5%8B%E5%80%BC) 技巧。

以上是针对命名导出时的重命名方案，如果是默认导出，那么在导入的时候用一个不冲突的变量名来声明就可以了。

## 用ES Module设计模块

ES Module 是新一代的模块化标准，它是在 ES6（ ECMAScript 2015 ）版本推出的，是原生 JavaScript 的一部分。

不过因为历史原因，如果要直接在浏览器里使用该方案，在不同的浏览器里会有一定的兼容问题，需要通过 Babel 等方案进行代码的版本转换

因此一般情况下都需要借助构建工具进行开发，工具通常会提供开箱即用的本地服务器用于开发调试，并且最终打包的时候还可以抹平不同浏览器之间的差异。

随着 ESM 的流行，很多新推出的构建工具都默认只支持该方案（ e.g. Vite 、 Rollup ），如果需要兼容 CJS 反而需要另外引入插件单独配置。除了构建工具，很多语言也是默认支持 ESM ，例如 TypeScript ，因此了解 ESM 非常重要。

一样的，先调整一下目录结构：

```tsx
1. 在 `src` 文件夹里面创建一个 `esm` 文件夹
2. 在 `esm` 文件夹里面创建两个 MJS 文件： `index.mjs` 和 `module.mjs`
hello-node
│ # 源码文件夹
├─src
│ │ # 上次用来测试 CommonJS 的相关文件
│ ├─cjs
│ │ ├─index.cjs
│ │ └─module.cjs
│ │
│ │ # 这次要用的 ES Module 测试文件
│ └─esm
│   │ # 入口文件
│   ├─index.mjs
│   │ # 模块文件
│   └─module.mjs
│
│ # 项目清单
└─package.json
```
然后再修改一下 package.json 里面的 scripts 部分，参照上次配置 CJS 的格式，增加一个 ESM 版本的 script ，改成如下：



``` json
{
  "scripts": {
    "dev:cjs": "node src/cjs/index.cjs",
    "dev:esm": "node src/esm/index.mjs"
  }
}
```

后面在命令行执行 `npm run dev:esm` 就可以测试的 ESM 模块了。


#  认识组件化设计

![[assets/img/Vue基础/IMG-Vue基础-20240714124840929.png]]
常见的组件有：页头、页脚、导航栏、侧边栏… 甚至小到一个用户头像也可以抽离成组件，因为头像可能只是尺寸、圆角不同而已。

每个组件都有自己的 “作用域” ， JavaScript 部分利用 [模块化](https://vue3.chengpeiquan.com/guide.html#%E5%AD%A6%E4%B9%A0%E6%A8%A1%E5%9D%97%E5%8C%96%E8%AE%BE%E8%AE%A1) 来实现作用域隔离， HTML 和 CSS 代码则借助 [Style Scoped](https://vue3.chengpeiquan.com/component.html#style-scoped) 来生成独有的 hash ，避免全局污染，这些方案组合起来，使得组件与组件之间的代码不会互相影响。

### 如何实现组件化[​](https://vue3.chengpeiquan.com/guide.html#%E5%A6%82%E4%BD%95%E5%AE%9E%E7%8E%B0%E7%BB%84%E4%BB%B6%E5%8C%96)

在 Vue ，是通过 Single-File Component （简称 SFC ， `.vue` 单文件组件）来实现组件化开发。

一个 Vue 组件是由三部分组成的：

```vue
<template>
  <!-- HTML 代码 -->
</template>

<script>
// JavaScript 代码
</script>

<style scoped>
/* CSS 代码 */
</style>
```

在后面的 [单组件的编写](https://vue3.chengpeiquan.com/component.html) 一章中，会详细介绍如何编写一个 Vue 组件。

### 什么是包[​](https://vue3.chengpeiquan.com/guide.html#%E4%BB%80%E4%B9%88%E6%98%AF%E5%8C%85)

在 Node 项目里，包可以简单理解为模块的集合，一个包可以只提供一个模块的功能，也可以作为多个模块的集合集中管理。

## 包和模块
```jsx
// src/esm/index.mjs
import md5 from 'md5'

const before = 'Hello World'
const after = md5(before)
console.log({ before, after })
```

在命令行输入 `npm run dev:esm` ，可以在控制台看到输出了这些内容，成功获得了转换后的结果：



```bash
npm run dev:esm

> demo@1.0.0 dev:esm
> node src/esm/index.mjs

{ before: 'Hello World', after: 'b10a8db164e0754105b7a99be72e3fe5' }
```

是不是非常简单，其实包的用法和在导入模块的用法可以说是完全一样的，区别主要在于，包是需要安装了才能用，而模块是需要自己编写。



# TypeScript 

1. [typescript](https://www.npmjs.com/package/typescript) 这个包是用 TypeScript 编程的语言依赖包
2. [ts-node](https://www.npmjs.com/package/ts-node) 是让 Node 可以运行 TypeScript 的执行环境


```bash
npm install -D typescript ts-node
```

然后修改 scripts 字段，增加一个 `dev:ts` 的 script ：
```json
{
  "name": "hello-node",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "dev:cjs": "node src/cjs/index.cjs",
    "dev:esm": "node src/esm/index.mjs",
    "dev:ts": "ts-node src/ts/index.ts",
    "compile": "babel src/babel --out-dir compiled",
    "serve": "node server/index.js"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "dependencies": {
    "md5": "^2.3.0"
  },
  "devDependencies": {
    "ts-node": "^10.7.0",
    "typescript": "^4.6.3"
  }
}
```

```jsx
TIP
请注意， `dev:ts` 这个 script 是用了 `ts-node` 来代替原来在用的 `node` ，因为使用 `node` 无法识别 TypeScript 语言。
```

### 原始数据类型[​](https://vue3.chengpeiquan.com/typescript.html#%E5%8E%9F%E5%A7%8B%E6%95%B0%E6%8D%AE%E7%B1%BB%E5%9E%8B)

[原始数据类型](https://developer.mozilla.org/zh-CN/docs/Glossary/Primitive) 是一种既非对象也无方法的数据，刚才演示代码里，函数的入参使用的字符串 String 就是原始数据类型之一。

除了 String ，另外还有数值 Number 、布尔值 Boolean 等等，它们在 TypeScript 都有统一的表达方式，列个表格对比，能够更直观的了解：

|原始数据类型|JavaScript|TypeScript|
|---|---|---|
|字符串|String|string|
|数值|Number|number|
|布尔值|Boolean|boolean|
|大整数|BigInt|bigint|
|符号|Symbol|symbol|
|不存在|Null|null|
|未定义|Undefined|undefined|

![[assets/img/Vue基础/IMG-Vue基础-20240714124841385.png]]
笔者最常用的就是 `string[]` 这样的格式，只需要追加一个方括号 `[]` ，另外一种写法是基于 TS 的泛型 `Array<T>` ，两种方式定义出来的类型其实是一样的。

```tsx
// 字符串数组
const strs: string[] = ['Hello World', 'Hi World']
// 数值数组
const nums: number[] = [1, 2, 3]
// 布尔值数组
const bools: boolean[] = [true, true, false]
```
在实际的编程过程中，如果的数组一开始就有初始数据（数组长度不为 0 ），那么 TypeScript 也会根据数组里面的项目类型，正确自动帮推导这个数组的类型，这种情况下也可以省略类型定义：

```ts
// 这种有初始项目的数组， TS 也会推导它们的类型
const strs = ['Hello World', 'Hi World']
const nums = [1, 2, 3]
const bools = [true, true, false]
```

但是！如果一开始是 `[]` ，那么就必须显式的指定数组类型（取决于的 [tsconfig.json](https://vue3.chengpeiquan.com/typescript.html#%E4%BA%86%E8%A7%A3-tsconfig-json) 的配置，可能会引起报错）：
```ts
// 这个时候会认为是 any[] 或者 never[] 类型
const nums = []

// 这个时候再 push 一个 number 数据进去，也不会使其成为 number[]
nums.push(1)
```
而对于复杂的数组，比如数组里面的 item 都是对象，其实格式也是一样，只不过把原始数据类型换成 [对象的类型](https://vue3.chengpeiquan.com/typescript.html#%E5%AF%B9%E8%B1%A1-%E6%8E%A5%E5%8F%A3) 即可，例如 `UserItem[]` 表示这是一个关于用户的数组列表

### 对象（接口）[​](https://vue3.chengpeiquan.com/typescript.html#%E5%AF%B9%E8%B1%A1-%E6%8E%A5%E5%8F%A3)

看完了数组，接下来看看对象的用法，对象也是引用类型，在 [数组](https://vue3.chengpeiquan.com/typescript.html#%E6%95%B0%E7%BB%84) 的最后提到了一个 `UserItem[]` 的写法，这里的 `UserItem` 就是一个对象的类型定义。

如果熟悉 JavaScript ，那么就知道对象的 “键值对” 里面的值，可能是由原始数据、数组、对象组成的，所以在 TypeScript ，类型定义也是需要根据值的类型来确定它的类型，因此定义对象的类型应该是第一个比较有门槛的地方。

#### 如何定义对象的类型[​](https://vue3.chengpeiquan.com/typescript.html#%E5%A6%82%E4%BD%95%E5%AE%9A%E4%B9%89%E5%AF%B9%E8%B1%A1%E7%9A%84%E7%B1%BB%E5%9E%8B)

对象的类型定义有两个语法支持： `type` 和 `interface` 。

先看看 `type` 的写法：
```ts
type UserItem = {
  // ...
}
```

再看看 `interface` 的写法：
```ts
interface UserItem {
  // ...
}
```

可以看到它们表面上的区别是一个有 = 号，一个没有，事实上在一般的情况下也确实如此，两者非常接近，但是在特殊的时候也有一定的区别。

为了降低学习门槛，统一使用 `interface` 来做入门教学，它的写法与 Object 更为接近，事实上它也被用的更多。

```tsx
// 定义用户对象的类型
interface UserItem {
  name: string
  age: number
}

// 在声明变量的时候将其关联到类型上
const petter: UserItem = {
  name: 'Petter',
  age: 20,
}
```

#### 接口的继承[​](https://vue3.chengpeiquan.com/typescript.html#%E6%8E%A5%E5%8F%A3%E7%9A%84%E7%BB%A7%E6%89%BF)

接口还可以继承，比如要对用户设置管理员，管理员信息也是一个对象，但要比普通用户多一个权限级别的属性，那么就可以使用继承，它通过 `extends` 来实现：

```tsx
interface UserItem {
  name: string
  age: number
  enjoyFoods: string[]
  friendList: UserItem[]
}

// 这里继承了 UserItem 的所有属性类型，并追加了一个权限等级属性
interface Admin extends UserItem {
  permissionLevel: number
}

const admin: Admin = {
  name: 'Petter',
  age: 18,
  enjoyFoods: ['rice', 'noodle', 'pizza'],
  friendList: [
    {
      name: 'Marry',
      age: 16,
      enjoyFoods: ['pizza', 'ice cream'],
      friendList: [],
    },
    {
      name: 'Tom',
      age: 20,
      enjoyFoods: ['chicken', 'cake'],
      friendList: [],
    }
  ],
  permissionLevel: 1,
}
```

如果觉得这个 `Admin` 类型不需要记录这么多属性，也可以在继承的过程中舍弃某些属性，通过 `Omit` 帮助类型来实现，`Omit` 的类型如下：

```tsx
type Omit<T, K extends string | number | symbol>
```

```tsx
interface UserItem {
  name: string
  age: number
  enjoyFoods: string[]
  friendList?: UserItem[]
}

// 这里在继承 UserItem 类型的时候，删除了两个多余的属性
interface Admin extends Omit<UserItem, 'enjoyFoods' | 'friendList'> {
  permissionLevel: number
}

// 现在的 admin 就非常精简了
const admin: Admin = {
  name: 'Petter',
  age: 18,
  permissionLevel: 1,
}
```

### 类[​](https://vue3.chengpeiquan.com/typescript.html#%E7%B1%BB)

类是 JavaScript ES6 推出的一个概念，通过 `class` 关键字，可以定义一个对象的模板，如果对类还比较陌生的话，可以先阅读一下阮一峰老师的 ES6 文章：[Class 的基本语法](https://es6.ruanyifeng.com/#docs/class) 。

在 TypeScript ，通过类得到的变量，它的类型就是这个类，可能这句话看起来有点难以理解，来看个例子，可以在 demo 里运行它：

```tsx
// 定义一个类
class User {
  // constructor 上的数据需要先这样定好类型
  name: string

  // 入参也要定义类型
  constructor(userName: string) {
    this.name = userName
  }

  getName() {
    console.log(this.name)
  }
}

// 通过 new 这个类得到的变量，它的类型就是这个类
const petter: User = new User('Petter')
petter.getName() // Petter
```

事实上由于 TypeScript 会推导函数类型，所以很少会显式的去写出来，除非在给对象定义方法：



```ts
// 对象的接口
interface Obj {
  // 上面的方法就需要显式的定义出来
  sum: (x: number, y: number) => number  //=>后面的number是函数类型
}

// 声明一个对象
const obj: Obj = {
  sum(x: number, y: number): number {
    return x + y
  }
}
```

```jsx
// 对单人或者多人打招呼
function greet(name: string | string[]): string | string[] {
  if (Array.isArray(name)) {
    return name.map((n) => `Welcome, ${n}!`)
  }
  return `Welcome, ${name}!`
}

// 单个问候语
const greeting = greet('Petter')
console.log(greeting) // Welcome, Petter!

// 多个问候语
const greetings = greet(['Petter', 'Tom', 'Jimmy'])
console.log(greetings)
// [ 'Welcome, Petter!', 'Welcome, Tom!', 'Welcome, Jimmy!' ]
```

此时，利用 TypeScript 的函数重载就非常有用！来看一下具体如何实现：

```ts
// 这一次用了函数重载
function greet(name: string): string  // TS 类型
function greet(name: string[]): string[]  // TS 类型
function greet(name: string | string[]) {
  if (Array.isArray(name)) {
    return name.map((n) => `Welcome, ${n}!`)
  }
  return `Welcome, ${name}!`
}

// 单个问候语，此时只有一个类型 string
const greeting = greet('Petter')
console.log(greeting) // Welcome, Petter!

// 多个问候语，此时只有一个类型 string[]
const greetings = greet(['Petter', 'Tom', 'Jimmy'])
console.log(greetings)
// [ 'Welcome, Petter!', 'Welcome, Tom!', 'Welcome, Jimmy!' ]
```

上面是利用函数重载优化后的代码，可以看到一共写了 3 行 `function greet …` ，区别如下：
第 1 行是函数的 TS 类型，告知 TypeScript ，当入参为 `string` 类型时，返回值也是 `string` ;
第 2 行也是函数的 TS 类型，告知 TypeScript ，当入参为 `string[]` 类型时，返回值也是 `string[]` ;
第 3 行开始才是真正的函数体，这里的函数入参需要把可能涉及到的类型都写出来，用以匹配前两行的类型，并且这种情况下，函数的返回值类型可以省略，因为在第 1 、 2 行里已经定义过返回类型了。

这是因为缺少 md5 这个包的类型定义，根据命令行的提示，安装 `@types/md5` 这个包。

这是因为这些包是很早期用 JavaScript 编写的，因为功能够用作者也没有进行维护更新，所以缺少相应的 TS 类型，因此开源社区推出了一套 @types 类型包，专门处理这样的情况。

@types 类型包的命名格式为 `@types/<package-name>` ，也就是在原有的包名前面拼接 `@types` ，日常开发要用到的知名 npm 包都会有相应的类型包，只需要将其安装到 package.json 的 `devDependencies` 里即可解决该问题。

### 编译单个文件

```jsx
"build": "tsc src/ts/index.ts --outDir dist",
```

这样在命令行运行 `npm run build` 的时候，就会把 `src/ts/index.ts` 这个 TS 文件编译，并输出到项目下与 src 文件夹同级的 dist 目录下。

其中 `tsc` 是 TypeScript 用来编译文件的命令， `--outDir` 是它的一个选项，用来指定输出目录，如果不指定，则默认生成到源文件所在的目录下面。

把之前在 [函数的重载](https://vue3.chengpeiquan.com/typescript.html#%E5%87%BD%E6%95%B0%E7%9A%84%E9%87%8D%E8%BD%BD) 用过的这个例子放到 `src/ts/index.ts` 文件里，因为它是一段比较典型的、包含了多个知识点的 TypeScript 代码：


```ts

// 对单人或者多人打招呼
function greet(name: string): string
function greet(name: string[]): string[]
function greet(name: string | string[]) {
  if (Array.isArray(name)) {
    return name.map((n) => `Welcome, ${n}!`)
  }
  return `Welcome, ${name}!`
}

// 单个问候语
const greeting = greet('Petter')
console.log(greeting)

// 多个问候语
const greetings = greet(['Petter', 'Tom', 'Jimmy'])
console.log(greetings)
```

可以先执行 `npm run dev:ts` 测试它的可运行性，当然，如果期间的代码运行有问题，在编译阶段也会给报错。

现在来编译它，现在在命令行输入 `npm run build` 并回车执行。

可以看到多了一个 dist 文件夹，里面多了一个 `index.js` 文件。

```bash
hello-node
│ # 构建产物
├─dist
│ │ # 编译后的 JS 文件
│ └─index.js
│ # 依赖文件夹
├─node_modules
│ # 源码文件夹
├─src
│ # 锁定安装依赖的版本号
├─package-lock.json
│ # 项目清单
└─package.json
```

`index.js` 文件里面的代码如下：
```jsx
function greet(name) {
  if (Array.isArray(name)) {
    return name.map(function (n) {
      return 'Welcome, '.concat(n, '!')
    })
  }
  return 'Welcome, '.concat(name, '!')
}
// 单个问候语
var greeting = greet('Petter')
console.log(greeting)
// 多个问候语
var greetings = greet(['Petter', 'Tom', 'Jimmy'])
console.log(greetings)
```

可以看到已经成功把 TypeScript 代码编译成 JavaScript 代码了。

在命令行执行 `node dist/index.js` ，像之前测试 JS 文件一样使用 `node` 命令，运行 dist 目录下的 `index.js` 文件，它可以正确运行：

```bash
node dist/index.js
Welcome, Petter!
[ 'Welcome, Petter!', 'Welcome, Tom!', 'Welcome, Jimmy!' ] 
```
### 编译多个模块[​](https://vue3.chengpeiquan.com/typescript.html#%E7%BC%96%E8%AF%91%E5%A4%9A%E4%B8%AA%E6%A8%A1%E5%9D%97)

刚才只是编译一个 `index.ts` 文件，如果 `index.ts` 里引入了其他模块，此时 `index.ts` 是作为入口文件，入口文件 `import` 进来使用的模块也会被 TypeScript 一并编译。

拆分一下模块，把 `greet` 函数单独抽离成一个模块文件 `src/ts/greet.ts` ：

ts

```
// src/ts/greet.ts
function greet(name: string): string
function greet(name: string[]): string[]
function greet(name: string | string[]) {
  if (Array.isArray(name)) {
    return name.map((n) => `Welcome, ${n}!`)
  }
  return `Welcome, ${name}!`
}

export default greet
```

在 `src/ts/index.ts` 这边，把这个模块导进来：

ts

```
// src/ts/index.ts
import greet from './greet'

// 单个问候语
const greeting = greet('Petter')
console.log(greeting)

// 多个问候语
const greetings = greet(['Petter', 'Tom', 'Jimmy'])
console.log(greetings)
```

的 build script 无需修改，依然只编译 `index.ts` ，但因为导入了 `greet.ts` ，所以 TypeScript 也会一并编译，来试一下运行 `npm run build` ， 现在 dist 目录下有两个文件了：

bash

```
hello-node
│ # 构建产物
├─dist
│ ├─greet.js  # 多了这个文件
│ └─index.js
│
│ # 其他文件这里省略...
└─package.json
```

来看看这一次的编译结果：

先看看 `greet.js` ：

js

```
// dist/greet.js
'use strict'
exports.__esModule = true
function greet(name) {
  if (Array.isArray(name)) {
    return name.map(function (n) {
      return 'Welcome, '.concat(n, '!')
    })
  }
  return 'Welcome, '.concat(name, '!')
}
exports['default'] = greet
```

再看看 `index.js` ：

js

```
// dist/index.js
'use strict'
exports.__esModule = true
var greet_1 = require('./greet')
// 单个问候语
var greeting = (0, greet_1['default'])('Petter')
console.log(greeting)
// 多个问候语
var greetings = (0, greet_1['default'])(['Petter', 'Tom', 'Jimmy'])
console.log(greetings)
```

这个代码风格有没有觉得似曾相识？是的，就是前面提到的 [CommonJS](https://vue3.chengpeiquan.com/typescript.html#%E7%94%A8-commonjs-%E8%AE%BE%E8%AE%A1%E6%A8%A1%E5%9D%97) 模块代码。

其实在 [编译单个文件](https://vue3.chengpeiquan.com/typescript.html#%E7%BC%96%E8%AF%91%E5%8D%95%E4%B8%AA%E6%96%87%E4%BB%B6) 代码的时候，它也是 CommonJS ，只不过因为只有一个文件，没有涉及到模块化，所以第一眼看不出来。

还是在命令行执行 `node dist/index.js` ，虽然也是运行 dist 目录下的 `index.js` 文件，但这次它的作用是充当一个入口文件了，引用到的 `greet.js` 模块文件也会被调用。

这次一样可以得到正确的结果：

bash

```
node dist/index.js
Welcome, Petter!
[ 'Welcome, Petter!', 'Welcome, Tom!', 'Welcome, Jimmy!' ]
```

### 修改编译后的 JS 版本[​](https://vue3.chengpeiquan.com/typescript.html#%E4%BF%AE%E6%94%B9%E7%BC%96%E8%AF%91%E5%90%8E%E7%9A%84-js-%E7%89%88%E6%9C%AC)

还可以修改编译配置，让 TypeScript 编译成不同的 JavaScript 版本。

修改 package.json 里的 build script ，在原有的命令后面增加一个 `--target` 选项：

json

```
{
  // ...
  "scripts": {
    // ...
    "build": "tsc src/ts/index.ts --outDir dist --target es6"
  }
  // ...
}
```

`--target` 选项的作用是控制编译后的 JavaScript 版本，可选的值目前有： `es3` ， `es5` ， `es6` ， `es2015` ， `es2016` ， `es2017` ， `es2018` ， `es2019` ， `es2020` ， `es2021` ， `es2022` ， `esnext` ，分别对应不同的 JS 规范（所以未来的可选值会根据 JS 规范一起增加）。

之前编译出来的 JavaScript 是 [CommonJS 规范](https://vue3.chengpeiquan.com/typescript.html#%E7%94%A8-commonjs-%E8%AE%BE%E8%AE%A1%E6%A8%A1%E5%9D%97) ，本次配置的是 `es6` ，这是支持 [ES Module 规范](https://vue3.chengpeiquan.com/typescript.html#%E7%94%A8-es-module-%E8%AE%BE%E8%AE%A1%E6%A8%A1%E5%9D%97) 的版本。

TIP

通常还需要配置一个 `--module` 选项，用于决定编译后是 CJS 规范还是 ESM 规范，但如果缺省，会根据 `--target` 来决定。

再次在命令行运行 `npm run build` ，这次看看变成了什么：

先看看 `greet.js` ：

js

```
// dist/greet.js
function greet(name) {
  if (Array.isArray(name)) {
    return name.map((n) => `Welcome, ${n}!`)
  }
  return `Welcome, ${name}!`
}
export default greet
```

再看看 `index.js` ：

js

```
// dist/index.js
import greet from './greet'
// 单个问候语
const greeting = greet('Petter')
console.log(greeting)
// 多个问候语
const greetings = greet(['Petter', 'Tom', 'Jimmy'])
console.log(greetings)
```

这次编译出来的都是基于 ES6 的 JavaScript 代码，因为涉及到 ESM 模块，所以不能直接在 node 运行它了，可以手动改一下扩展名，改成 `.mjs` （包括 index 文件里 `import` 的 greet 文件名也要改），然后再运行 `node dist/index.mjs` 。

### 其他事项[​](https://vue3.chengpeiquan.com/typescript.html#%E5%85%B6%E4%BB%96%E4%BA%8B%E9%A1%B9)

在尝试 [编译单个文件](https://vue3.chengpeiquan.com/typescript.html#%E7%BC%96%E8%AF%91%E5%8D%95%E4%B8%AA%E6%96%87%E4%BB%B6) 和 [编译多个模块](https://vue3.chengpeiquan.com/typescript.html#%E7%BC%96%E8%AF%91%E5%A4%9A%E4%B8%AA%E6%A8%A1%E5%9D%97) 的时候，相信各位开发者应该没有太大的疑问，但是来到 [修改编译后的 JS 版本](https://vue3.chengpeiquan.com/typescript.html#%E4%BF%AE%E6%94%B9%E7%BC%96%E8%AF%91%E5%90%8E%E7%9A%84-js-%E7%89%88%E6%9C%AC) 这里，事情就开始变得复杂了起来，应该能感觉到编译的选项和测试成本都相应的增加了很多。

事实上刚才编译的 JS 文件，因为涉及到 ESM 模块化，是无法通过普通的 `<script />` 标签在 HTML 页面里使用的（单个文件可以，因为没有涉及模块），不仅需要加上 ESM 模块所需的 `<script type="module" />` 属性，本地开发还需要启动本地服务器通过 HTTP 协议访问页面，才允许在浏览器里使用 ESM 模块（详见： [在浏览器里访问 ESM](https://vue3.chengpeiquan.com/guide.html#%E5%9C%A8%E6%B5%8F%E8%A7%88%E5%99%A8%E9%87%8C%E8%AE%BF%E9%97%AE-esm) 一节）。

因此在实际的项目开发中，需要借助 [构建工具](https://vue3.chengpeiquan.com/typescript.html#%E5%B7%A5%E7%A8%8B%E5%8C%96%E7%9A%84%E6%9E%84%E5%BB%BA%E5%B7%A5%E5%85%B7) 来处理很多编译过程中的兼容性问题，降低开发成本。

而刚才用到的诸如 `--target` 这样的选项，可以用一个更简单的方式来管理，类似于 package.json 项目清单， TypeScript 也有一份适用于项目的配置清单，请看 [了解 tsconfig.json](https://vue3.chengpeiquan.com/typescript.html#%E4%BA%86%E8%A7%A3-tsconfig-json) 部分。

## 了解 tsconfig.json[​](https://vue3.chengpeiquan.com/typescript.html#%E4%BA%86%E8%A7%A3-tsconfig-json)

TypeScript 项目一般都会有一个 tsconfig.json 文件，放置于项目的根目录下，这个文件的作用是用来管理 TypeScript 在编译过程中的一些选项配置。

在开始之前，需要全局安装一下 TypeScript ：

bash

```
npm install -g typescript
```

这样就可以使用 TypeScript 提供的全局功能，可以直接在命令行里使用 `tsc` 命令了（之前本地安装的时候，需要封装成 package.json 的 script 才能调用它）。

依然是用的 [Hello TypeScript](https://vue3.chengpeiquan.com/typescript.html#hello-typescript) demo ，记得先通过 `cd` 命令进入项目所在的目录。

在命令行输入 `tsc --init` ，这是 TypeScript 提供的初始化功能，会生成一个默认的 tsconfig.json 文件。



```bash
tsc --init

Created a new tsconfig.json with:
  target: es2016
  module: commonjs
  strict: true
  esModuleInterop: true
  skipLibCheck: true
  forceConsistentCasingInFileNames: true


You can learn more at https://aka.ms/tsconfig.json
```

现在的目录结构是这样子，多了一个 tsconfig.json 文件：



```bash
hello-node
│ # 构建产物
├─dist
│ # 依赖文件夹
├─node_modules
│ # 源码文件夹
├─src
│ # 锁定安装依赖的版本号
├─package-lock.json
│ # 项目清单
├─package.json
│ # TypeScript 配置
└─tsconfig.json
```

每一个 `tsc` 的命令行的选项，都可以作为这个 JSON 的一个字段来管理，例如刚才的 `--outDir` 和 `--target` 选项，在这个 JSON 文件里对应的就是：

```json
{
  "compilerOptions": {
    "target": "es6",
    "module": "es6",
    "outDir": "./dist"
  }
}
```

可以直接在生成的 tsconfig.json 上面修改。

来试试效果，这一次不需要用到 package.json 里的 build script 了，直接在命令行运行 `tsc` ，它现在会根据配置的 tsconfig.json 文件，按照的要求来编译。

可以看到它依然按照要求在 dist 目录下生成编译后的 JS 文件，而且这一次的编译结果，和在 build script 里使用的 `tsc src/ts/index.ts --outDir dist --target es6` 这一长串命令是一样的。

所以正常工作中，都是使用 tsconfig.json 来管理 TypeScript 的配置的。

完整的选项可以查看 TypeScript 官网： [tsconfig - typescriptlang](https://www.typescriptlang.org/tsconfig/)

不过实际工作中的项目都是通过一些脚手架创建的，例如 [Vue CLI](https://github.com/vuejs/vue-cli) ，或者现在的 [Create Vue](https://github.com/vuejs/create-vue) 或者 [Create Preset](https://github.com/awesome-starter/create-preset) ，都会在创建项目模板的时候，提前配置好通用的选项，只需要在不满足条件的情况下去调整。



# Vue3入门教程


### 使用 Vue 2[​](https://vue3.chengpeiquan.com/upgrade.html#%E4%BD%BF%E7%94%A8-vue-2)

如果还需要使用 Vue 2 ，则在安装的时候需要手动指定 Tag 为 `legacy` 或者 `v2-latest` 才能安装到 Vue 2 ：



```bash
# 安装 2.6.x 的最新版本
npm i vue@legacy

# 安装 2.7.x 的最新版本
npm i vue@v2-latest
```

```tsx
TIP

Vue 2.7 系列是在 Vue 2 的基础上，对标 Vue 3 的功能支持所作的升级，主要是面向想使用 Vue 3 的新特性、但顾虑于产品对旧浏览器的支持而无法贸然升级的开发者。
```

如果之前使用了 `latest` 标签或 `*` 从 npm 安装 Vue 或其他官方库，请确保项目下的 package.json 文件能够明确使用兼容 Vue 2 的版本。


```diff
{
  "dependencies": {
-   "vue": "latest",
+   "vue": "^2.6.14",
-   "vue-router": "latest",
+   "vue-router": "^3.5.3",
-   "vuex": "latest"
+   "vuex": "^3.6.2"
  },
  "devDependencies": {
-   "vue-loader": "latest",
+   "vue-loader": "^15.9.8",
-   "@vue/test-utils": "latest"
+   "@vue/test-utils": "^1.3.0"
  }
}
```
```jsx
TIP

上方代码块里的 `-` 号代表移除， `+` 号代表新增，这是一种 Diff 风格的排版，表明修改前后的变化，后文如有类似的代码风格同理。
```

### Pre-Rendering 与 SSG[​](https://vue3.chengpeiquan.com/engineering.html#pre-rendering-%E4%B8%8E-ssg)

在介绍了 SSR 服务端渲染技术后，读者可能会想到一个问题，就是 SSR 的开发成本总归比较高，如果本身项目比较简单，例如一个静态博客，或者静态官网、落地页等内容不多，仅需要简单的 SEO 支持的项目需求，是否有更简便的方案呢？

以下两种方案正是用于满足这类需求的技术：

|名词|全称|中文|
|---|---|---|
|Pre-Rendering|Pre-Rendering|预渲染|
|SSG|Static-Site Generation|静态站点生成|





[十分钟，带你了解 Vue3 的新写法 - 掘金 (juejin.cn)](https://juejin.cn/post/7225267685763907621)

[[Vue Route]]




### 一省: Vue构件类型

Vue.js 是一个基于 MVVM 设计模式构建的现代 Web 框架，它由多个不同的构件组成。

以下是 Vue.js 中最常见的构件类型：

1. 组件

   组件（Component）是 Vue.js 的核心构件之一，用于将页面拆分成可重复使用的独立部分。Vue.js 通过组件系统来实现页面与数据的解耦，方便复杂视图的管理和维护。

2. 指令

   指令（Directive）是 Vue.js 的另一个核心构件，可以在 HTML 元素上添加特殊功能。例如 `v-model` 实现双向数据绑定、`v-if` 和 `v-else` 控制渲染条件等等。

3. 过滤器

   过滤器（Filter）允许格式化文本内容，以便更好地呈现给用户。Vue.js 提供了几个预制过滤器可供使用，还可以创建自定义过滤器，如格式化金额或时间值。

4. 插件

   插件（Plugin）通常是一些可重用的代码包，提供了额外的功能和工具。例如，Vuex 状态管理库就是一个 Vue.js 的插件。

5. 路由器

   路由器（Router）在单页应用程序中管理网页的导航。Vue.js 路由器 (Vue Router) 是 Vue.js 官方提供的路由管理工具。

6. 状态管理

   状态管理（State Management）是 Vue.js 应用程序中非常重要的部分，通常使用 Vuex 来实现。Vuex 提供了一个集中式的状态管理模式，在应用程序中共享数据状态，并处理应用程序中各个组件之间的复杂通信逻辑。

以上这些构件类型都是 Vue.js 开发过程中非常重要的一部分。掌握和理解它们的优缺点以及如何合理使用会帮助开发者更加得心应手地完成开发项目。

当然可以。这里给出一些 Vue.js 中构件类型的代码示例：

1. 组件：

   ```html
   <template>
     <div>
       <h2>{{ title }}</h2>
       <p>{{ message }}</p>
     </div>
   </template>

   <script>
   export default {
     name: "HelloWorld",
     props: {
       title: String,
       message: String
     }
   };
   </script>
   ```

   以上是一个简单的 Vue.js 组件示例，定义了两个属性 `title` 和 `message`，并在模板中渲染。

2. 指令：

   ```html
   <template>
     <div v-if="show">
       <button v-on:click="clickHandler">点击我</button>
     </div>
   </template>

   <script>
   export default {
     data: function () {
       return {
         show: true
       };
     },
     methods: {
       clickHandler: function () {
         this.show = false;
       }
     }
   };
   </script>
   ```

   以上示例演示了使用 `v-if` 指令来控制元素是否在页面上呈现，并使用 `v-on:click` 指令绑定事件处理程序。

3. 过滤器：

   ```html
   <template>
     <div>
       <p>{{ message | capitalize }}</p>
     </div>
   </template>

   <script>
   export default {
     data: function () {
       return {
         message: 'hello world'
       };
     },
     filters: {
       capitalize: function (value) {
         if (!value) return '';
         value = value.toString();
         return value.charAt(0).toUpperCase() + value.slice(1);
       }
     }
   };
   </script>
   ```

   以上示例定义了一个过滤器 `capitalize`，用于将字符串首字母大写，并在模板中应用到 `message` 上。

4. 插件：

   ```js
   const MyPlugin = {
     install: function (Vue, options) {
       // 扩展 Vue.js 的功能
       Vue.myGlobalMethod = function () {
         console.log("这是一个全局方法");
       };

       // 添加自定义指令
       Vue.directive('my-directive', {
         bind(el, binding, vnode) {
           el.innerHTML =
             'Hello ' + binding.value + ', this is a custom directive';
         }
       });

       // 添加实例方法
       Vue.prototype.$myMethod = function (methodOptions) {
         console.log("这是一个实例方法");
       };
     }
   };
   export default MyPlugin;
   ```

   以上示例演示了如何创建一个 Vue.js 插件，并在其中添加全局方法、自定义指令和实例方法等功能。

5. 路由器：

   ```js
   import Vue from "vue";
   import VueRouter from "vue-router";
   import Home from "./views/Home.vue";

   Vue.use(VueRouter);

   const routes = [
     {
       path: "/",
       name: "home",
       component: Home,
     },
     {
       path: "/about",
       name: "about",
       component: () =>
         import(/* webpackChunkName: "about" */ "./views/About.vue"),
     },
   ];

   const router = new VueRouter({
     mode: "history",
     base: process.env.BASE_URL,
     routes,
   });

   export default router;
   ```

   以上示例展示了如何使用 Vue Router 创建一个单页应用程序的路由器，并在路由中定义不同页面的组件和路径。

6. 状态管理：

   ```js
   import Vue from "vue";
   import Vuex from "vuex";

   Vue.use(Vuex);

   export default new Vuex.Store({
     state: {
       count: 0,
     },
     mutations: {
       increment(state) {
         state.count++;
       },
       decrement(state) {
         state.count--;
       },
     },
     actions: {},
     modules: {},
   });
   ```

   以上示例实现了一个简单的状态管理模块，包括 `count` 状态和对其进行增减操作的 `mutations`。将这个 Vuex 存储引入 Vue.js 应用程序即可进行全局数据状态管理。

### Day2: 1省:

要快速掌握Vue 3.0，你可以遵循以下策略：

1. 熟悉基础知识：首先了解前端开发的基础知识，包括HTML、CSS和JavaScript。这些是学习任何前端框架的基础。

2. 学习Vue基础：在学习Vue 3.0之前，建议先了解Vue的核心概念，如组件、模板、指令、事件处理、表单处理等。你可以通过阅读Vue官方文档或观看相关的视频教程来快速入门。

3. 了解Vue 3.0新特性：Vue 3.0引入了许多新特性，如Composition API、Teleport组件、Fragment、Suspense等。了解这些新特性以及它们与Vue 2.x的差异，有助于你更好地理解Vue 3.0。

4. 实践项目：通过实际项目来提高技能是最有效的方法。为了快速掌握Vue 3.0，尝试使用Vue 3.0构建一个简单的实际项目，如待办事项应用、购物车等。在实践过程中，遇到问题时不要怕查阅文档或求助于社区。

5. 学习生态系统：除了Vue本身，还需要了解其生态系统中的相关库和工具，如Vuex（状态管理）、Vue Router（路由）、Axios（HTTP客户端）等。这些工具将帮助你更高效地开发Vue应用。

6. 代码阅读与优化：阅读和分析其他人编写的Vue代码示例和开源项目，可以让你了解到不同的编程实践和技巧。同时，尝试对自己的项目进行优化，提高代码质量和性能。

7. 参与社区：加入Vue相关的论坛、QQ群或微信群，与其他开发者互动，询问问题或分享经验。参与社区有助于拓展知识面，也能获得更多的资源和帮助。

8. 持续学习：前端领域总是不断更新的，要保持关注Vue和前端技术的最新动态，随时学习新知识，以适应行业发展。

遵循以上策略，并且付诸实践，相信你会在较短的时间内掌握Vue 3.0。祝你学习顺利！

### Day2: 2省:

基于每天4小时的学习时间，以下是一份为期两周的Vue基础学习计划表：

第1周：

- 第1天：了解Vue.js框架和环境搭建
  - 了解Vue.js的优势及使用场景
  - 学习如何在项目中引入Vue.js
  - 使用Vue CLI搭建Vue开发环境

- 第2天：Vue实例与数据绑定
  - 学习Vue实例的创建与使用
  - 了解Vue实例的属性和方法
  - 学习数据绑定语法（插值、属性绑定等）

- 第3天：指令与事件处理
  - 学习常用指令（v-if, v-show, v-for, v-bind, v-on 等）
  - 了解事件处理及事件修饰符
  - 练习：创建一个简单的列表应用，实现添加、删除、筛选功能

- 第4天：组件化开发
  - 学习组件的基本概念和使用
  - 了解组件的属性和方法
  - 学习组件间通信（props、自定义事件、父子组件关系等）

- 第5天：表单处理与过滤器
  - 学习表单绑定（v-model）及表单修饰符
  - 了解表单验证方法
  - 学习过滤器的使用

- 第6-7天：实践项目
  - 使用所学知识构建一个简单的实际项目（如待办事项应用）

第2周：

- 第1天：Vue Router
  - 学习Vue Router的基本概念
  - 了解路由配置、路由传参、嵌套路由等
  - 实现一个简单的多页面应用

- 第2天：Vuex
  - 学习Vuex的基本概念（state, getters, mutations, actions, modules）
  - 了解Vuex的使用场景及与组件通信的方法
  - 练习：在实践项目中引入Vuex进行状态管理

- 第3天：HTTP通信与API调用
  - 学习如何使用Axios库发送HTTP请求
  - 了解API调用的基本流程
  - 练习：在实践项目中实现数据持久化存储（如调用后端接口）

- 第4天：动画与过渡效果
  - 学习Vue中的过渡组件（transition、transition-group）
  - 了解CSS动画与JS动画的实现     
- ..........

### Day2: 3省:

以下是近两年内出版的一些广受欢迎的Vue 3.0图书推荐：

1.《Vue 3 in Action》（作者：Erik Hanchett，Manning出版社）

2.《Vue.js 3 Cookbook》（作者：Andrea Passaglia，Packt出版社）

3.《Fullstack Vue: The Complete Guide to Vue.js》（作者：Hassan Djirdeh等人，New Riders出版社）

4.《The Majesty of Vue.js 3》（作者：Alex Kyriakidis等人，Packt出版社）

以下是一些较近两年内出版、评分较高的中文Vue 3.0图书推荐：

1.《Vue.js 3 实战教程》（作者：梁灏，出版社：电子工业出版社）  

豆瓣评分：8.9

2.《Vue.js 3.0 权威指南》（作者：付斌，出版社：人民邮电出版社） 

豆瓣评分：8.7

3.《Vue.js 3 组件精讲》（作者：万伟涛，出版社：机械工业出版社）

豆瓣评分：8.4

4.《Vue.js 3 技术揭秘》（作者：木易杨，出版社：电子工业出版社）

豆瓣评分：8.3

这些图书都是较为权威和深入的Vue 3.0教程，能够帮助您系统性地学习Vue 3.0的各项特性和技术。同时也请注意，一些较早的版本可能并未考虑到Vue 3.0的新特性，建议在选择时仔细查看书籍信息以确保符合需求。

Vue.js有五个主要特征：
1. 组件：组件是Vue.js最强大的特性之一。组件是基础HTML元素的拓展，可方便地自定义其数据与行为 ¹。
2. 模板：Vue.js使用基于HTML的模板语法，允许开发者将DOM元素与底层Vue.js实例中的数据相绑定 ¹。
3. 响应式设计：响应式网络设计（RWD/AWD）的出现，目的是为移动设备提供更好的体验，用技术来使网页适应从小到大（甚至超大）的不同分辨率的屏幕 ¹。
4. 过渡效果：Vue.js在插入、更新或者移除DOM时，提供了多种不同方式的应用过渡效果 ¹。
5. 单文件组件：Vue.js支持以.vue为扩展名的文件来定义一个完整组件，用以替代使用Vue.component注册组件的方式。开发者可以使用Webpack或Browserify等构建工具来打包单文件组件 ¹。



Vue.js中有两个常用的简写形式。v-bind指令的简写形式是`:`，例如`:href="url"`等同于`v-bind:href="url"`。v-on指令的简写形式是`@`，例如`@click="doSomething"`等同于`v-on:click="doSomething"` ¹。

(2) vue中常用的缩写_vue 缩写_林迦叶的博客-CSDN博客. https://blog.csdn.net/maple_leaf_red/article/details/109358649 Accessed 4/25/2023.
(3) Vue自定义指令-Vue自定义指令简写-Vue自定义指令简写语法-嗨客网. https://haicoder.net/vue/vue-custom-directive-simplified.html Accessed 4/25/2023.
(4) Vue3 教程 | 菜鸟教程. https://www.runoob.com/vue3/vue3-tutorial.html Accessed 4/25/2023.

当然。下面是两个箭头函数的示例：

```javascript
// 示例1: 将数组中的每个元素乘以2
let numbers = [1, 2, 3, 4];
let doubledNumbers = numbers.map(number => number * 2);
console.log(doubledNumbers); // [2, 4, 6, 8]

// 示例2: 过滤数组中的偶数
let evenNumbers = numbers.filter(number => number % 2 === 0);
console.log(evenNumbers); // [2, 4]
```

在Vue.js中，`el`是创建新的Vue实例时可以使用的选项。它指定了一个DOM元素来挂载Vue实例。在Vue.js中，有两种方法可以编写`el`：

1. 作为一个字符串，指定一个DOM元素中的CSS选择器。例如：`el: '#app'`将在具有`id`为`app`的元素上挂载Vue实例。
2. 作为对DOM元素的引用。例如：`el: document.getElementById('app')`将在具有`id`为`app`的元素上挂载Vue实例。



当然。下面是两个Vue.js组件的示例：

```javascript
// 示例1: 注册一个全局组件
Vue.component('my-component', {
  template: '<div>这是我的第一个全局组件！</div>'
});

// 示例2: 注册一个局部组件
var Child = {
  template: '<div>这是我的第一个局部组件！</div>'
};

new Vue({
  el: '#app',
  components: {
    'my-child': Child
  }
});
```

在示例1中，我们使用`Vue.component`方法注册了一个全局组件，可以在任何Vue实例中使用。在示例2中，我们注册了一个局部组件，只能在指定的Vue实例中使用。

除了使用`el`选项，您还可以使用`$mount`方法来手动挂载Vue实例。这种方法允许您在实例化Vue对象后再挂载它。例如，您可以这样写：

```javascript
var vm = new Vue({
  data: {
    message: 'Hello'
  }
})
vm.$mount('#app')
```

上面的代码将创建一个新的Vue实例，并在稍后使用`$mount`方法将其挂载到具有`id`为`app`的元素上。这种方法在您需要延迟挂载Vue实例时非常有用。

在Vue.js中，`data`选项可以用来存储组件的数据。`data`选项可以是一个对象或一个函数。

**对象式:**当`data`选项是一个对象时，它定义了组件的初始数据。例如：

```javascript
new Vue({
  el: '#app',
  data: {
    message: 'Hello Vue!'
  }
});
```

**函数式:**当`data`选项是一个函数时，它应该返回一个对象，该对象定义了组件的初始数据。这种写法常用于定义可复用的组件，以防止多个组件实例共享同一份数据。例如：

```javascript
Vue.component('my-component', {
  data: function () {
    return {
      message: 'Hello Vue!'
    }
  },
  template: '<div>{{ message }}</div>'
});
```

**#落地:**

当`data`选项是一个对象时，它定义了组件的初始数据。这种写法适用于根Vue实例，因为根Vue实例只会被创建一次。

当`data`选项是一个函数时，它应该返回一个对象，该对象定义了组件的初始数据。这种写法常用于定义可复用的组件，以防止多个组件实例共享同一份数据。每当创建一个新的组件实例时，`data`函数都会被调用一次，返回一个新的数据对象。

总之，对于根Vue实例，可以使用对象形式的`data`选项；对于可复用的组件，应该使用函数形式的`data`选项。

当然。下面是两个示例，分别展示了`data`选项的两种写法：

```javascript
// 示例1: 使用对象形式的data选项
new Vue({
  el: '#app',
  data: {
    message: 'Hello Vue!'
  },
  template: '<div>{{ message }}</div>'
});

// 示例2: 使用函数形式的data选项
Vue.component('my-component', {
  data: function () {  //这里可简写为data(){
    return {
      message: 'Hello Vue!'
    }
  },
  template: '<div>{{ message }}</div>'
});

new Vue({
  el: '#app'
});
```

在示例1中，我们使用对象形式的`data`选项定义了根Vue实例的初始数据。在示例2中，我们使用函数形式的`data`选项定义了一个可复用的组件，每当创建一个新的组件实例时，都会返回一个新的数据对象。

在 Vue 中，`options` 是指创建 Vue 实例时传递给构造函数的选项对象。它包含了各种选项，用于配置 Vue 实例的行为。

例如，下面是一个简单的 Vue 实例，它接受一个 `options` 对象作为参数：

```javascript
var vm = new Vue({
  el: '#app',
  data: {
    message: 'Hello Vue!'
  },
  methods: {
    reverseMessage: function () {
      this.message = this.message.split('').reverse().join('')
    }
  }
})
```

在上面的代码中，我们创建了一个 Vue 实例，并传递了一个 `options` 对象作为参数。`options` 对象包含了 `el`、`data` 和 `methods` 等选项。

- `el` 选项用于指定 Vue 实例要挂载的元素。
- `data` 选项用于定义 Vue 实例的数据。
- `methods` 选项用于定义 Vue 实例的方法。

除了上面提到的这些选项，Vue 还支持许多其他选项，如 `computed`、`watch`、`components` 等。你可以在 Vue 的文档中查看所有可用的选项。

总之，`options` 是创建 Vue 实例时传递给构造函数的一个重要参数，它包含了各种选项，用于配置 Vue 实例的行为。

`showInfo` 不是 Vue 中的一个特定概念。它可能是一个自定义方法的名称，用于在 Vue 组件中显示信息。

例如，下面是一个简单的 Vue 组件，它定义了一个名为 `showInfo` 的方法：

```javascript
Vue.component('my-component', {
  template: '<button @click="showInfo">Show Info</button>',
  methods: {
    showInfo: function () {
      alert('This is some info.')
    }
  }
})
```

在上面的代码中，我们定义了一个名为 `my-component` 的 Vue 组件，并在其 `methods` 对象中定义了一个名为 `showInfo` 的方法。当我们点击组件模板中的按钮时，它会调用 `showInfo` 方法并弹出一个警告框。

当然，这只是一个示例。实际上，`showInfo` 方法的具体实现和功能取决于你的需求。

如果你想了解更多关于 Vue 组件和方法的信息，可以查看 Vue 的文档。

数据劫持是 Vue 实现响应式系统的一种技术。它通过使用 `Object.defineProperty` 方法来劫持数据对象的属性，从而能够在数据发生变化时触发视图的更新。

当你在 Vue 实例的 `data` 选项中定义数据时，Vue 会使用数据劫持技术来监视数据的变化。它会遍历 `data` 对象中的所有属性，并使用 `Object.defineProperty` 方法将它们转换为 getter 和 setter。这样，当你访问或修改数据时，Vue 就能够拦截这些操作并执行相应的逻辑。

例如，当你修改一个数据属性的值时，Vue 会拦截这个操作，并通知依赖于该属性的所有组件更新视图。这就是为什么当你修改数据时，视图会自动更新的原因。

总之，数据劫持是 Vue 实现响应式系统的一种重要技术。它能够让 Vue 在数据发生变化时自动更新视图，从而提供了一种简单、高效的方式来构建用户界面。

在 Vue 中，修饰符是一种特殊的后缀，用于指示指令应该以特定方式绑定。它们可以用来修饰事件处理器或 `v-model` 指令。

例如，下面是一个简单的 Vue 组件，它使用了 `.prevent` 修饰符来阻止表单提交事件的默认行为：

```html
<template>
  <form @submit.prevent="onSubmit">
    <!-- 表单内容 -->
  </form>
</template>

<script>
export default {
  methods: {
    onSubmit() {
      // 处理表单提交
    }
  }
}
</script>
```

在上面的代码中，我们在 `@submit` 指令后面添加了 `.prevent` 修饰符。这表示当表单提交事件触发时，Vue 会调用 `event.preventDefault()` 方法来阻止事件的默认行为。

除了 `.prevent` 修饰符，Vue 还支持许多其他修饰符，如 `.stop`、`.capture`、`.self` 等。你可以在 Vue 的文档中查看所有可用的修饰符。

总之，修饰符是 Vue 中一种很有用的特性，它能够让我们更方便地控制指令的绑定方式。

---

在Vue中，事件修饰符主要有以下几种：`.stop`，`.prevent`，`.capture`，`.self`，`.once`和`.passive`。其中，`.stop`用于防止事件冒泡，等同于JavaScript中的event.stopPropagation()；`.prevent`用于防止执行预设的行为，等同于JavaScript中的event.preventDefault()；`.capture`用于捕获冒泡；`.self`将事件绑定到自身，只有自身才能触发；`.once`只触发一次；`.passive`不阻止事件的默认行为¹⁴。

下面是一个示例代码，演示了如何使用`.stop`和`.prevent`修饰符：
```html
<!-- 阻止冒泡 -->
<div @click="shout (2)">
  <button @click.stop="shout (1)">ok</button>
</div>

<!-- 阻止默认行为 -->
<form v-on:submit.prevent="onSubmit"></form>
```

下面是一些常见的Vue事件修饰符的示例代码：

- `.stop`：防止事件冒泡
```html
<div @click="shout (2)">
  <button @click.stop="shout (1)">ok</button>
</div>
```

- `.prevent`：防止执行预设的行为
```html
<form v-on:submit.prevent="onSubmit"></form>
```

- `.once`：只触发一次
```html
<button @click.once="onceFunc">你只能点击一次</button>
```

- `.self`：将事件绑定到自身，只有自身才能触发
```html
<div @click.self="doThat">...</div>
```

捕获阶段和冒泡阶段是DOM事件流中的两个阶段。当一个事件被触发时，它会经历三个阶段：捕获阶段、目标阶段和冒泡阶段。

在捕获阶段，事件从文档的根节点开始向下传播，直到到达目标元素。然后，在目标阶段，事件在目标元素上被触发。最后，在冒泡阶段，事件从目标元素开始向上传播，直到到达文档的根节点。

在Vue中，可以使用`.capture`修饰符来在捕获阶段触发事件监听器：
```html
<div @click.capture="doThis">...</div>
```

捕获阶段是由外往内,冒泡阶段是由内往外,先捕获再冒泡.

下面是一个简单的示例，演示了捕获阶段和冒泡阶段的顺序：

```html
<div id="outer" @click="outerHandler" @click.capture="outerCaptureHandler">
  Outer
  <div id="inner" @click="innerHandler" @click.capture="innerCaptureHandler">
    Inner
  </div>
</div>
```

```js
new Vue({
  el: '#app',
  methods: {
    outerHandler() {
      console.log('Outer handler (bubble phase)');
    },
    outerCaptureHandler() {
      console.log('Outer handler (capture phase)');
    },
    innerHandler() {
      console.log('Inner handler (bubble phase)');
    },
    innerCaptureHandler() {
      console.log('Inner handler (capture phase)');
    }
  }
});
```

当点击内部元素时，事件处理程序的执行顺序如下：
1. `outerCaptureHandler`（捕获阶段，由外往内）
2. `innerCaptureHandler`（捕获阶段，由外往内）
3. `innerHandler`（冒泡阶段，由内往外）
4. `outerHandler`（冒泡阶段，由内往外）

可以看到，在捕获阶段，事件处理程序是由外往内执行的；而在冒泡阶段，事件处理程序是由内往外执行的。

`.self`修饰符用于将事件绑定到元素本身，只有当事件在该元素本身（而不是子元素）触发时才会触发回调。

下面是一个简单的示例，演示了如何使用`.self`修饰符：

```html
<div id="app">
  <div @click.self="divHandler">
    Outer
    <button @click="buttonHandler">Inner</button>
  </div>
</div>
```

```js
new Vue({
  el: '#app',
  methods: {
    divHandler() {
      console.log('Div handler');
    },
    buttonHandler() {
      console.log('Button handler');
    }
  }
});
```

在这个示例中，当点击内部按钮时，只有`buttonHandler`会被触发；而当点击外部`div`元素时，只有`divHandler`会被触发。



`@`是`v-on`指令的简写。`v-on`指令用于在Vue中监听DOM事件，并在事件触发时执行对应的JavaScript代码。

例如，下面两种写法是等价的：
```html
<button v-on:click="handler">Click me</button>
<button @click="handler">Click me</button>
```

在这个示例中，当按钮被点击时，都会触发`handler`方法。



![image-20230510211121281](/image-20230510211121281.png)

# 内置指令

[内置指令 | Vue.js (vuejs.org)](https://cn.vuejs.org/api/built-in-directives.html)

- v-text

- v-html

- v-show

- v-if

- v-else

- v-else-if

- v-for

- v-on 给元素绑定事件监听器 缩写: `@`

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

  ```vue
  <!-- 具名插槽 -->
  <BaseLayout>
    <template v-slot:header>
      Header content
    </template>
  
    <template v-slot:default>
      Default slot content
    </template>
  
    <template v-slot:footer>
      Footer content
    </template>
  </BaseLayout>
  
  <!-- 接收 prop 的具名插槽 -->
  <InfiniteScroll>
    <template v-slot:item="slotProps">
      <div class="item">
        {{ slotProps.item.text }}
      </div>
    </template>
  </InfiniteScroll>
  
  <!-- 接收 prop 的默认插槽，并解构 -->
  <Mouse v-slot="{ x, y }">
    Mouse position: {{ x }}, {{ y }}
  </Mouse>
  ```

  

- v-pre

- v-once

- v-memo

- v-cloak

在 Vue 中，数据代理是指通过 Vue 实例来访问其 `data` 对象中的属性。这样做的好处是可以更方便地访问数据，而不需要每次都写 `this.data.propertyName`。

例如，假设我们有一个 Vue 实例，其 `data` 对象中有一个名为 `message` 的属性：

```javascript
var vm = new Vue({
  el: '#app',
  data: {
    message: 'Hello Vue!'
  }
})
```

由于 Vue 实例实现了数据代理，所以我们可以直接通过 `vm.message` 来访问 `data` 对象中的 `message` 属性，而不需要写成 `vm.data.message`。

数据代理的使用场景主要是在组件内部访问数据时。由于组件内部的方法和计算属性都是定义在 Vue 实例上的，所以我们可以直接使用 `this.propertyName` 来访问 `data` 对象中的属性。

例如，在下面的代码中，我们定义了一个计算属性 `reversedMessage`，它会返回 `message` 属性的反转字符串：

```javascript
var vm = new Vue({
  el: '#app',
  data: {
    message: 'Hello Vue!'
  },
  computed: {
    reversedMessage: function () {
      return this.message.split('').reverse().join('')
    }
  }
})
```

在上面的代码中，我们直接使用了 `this.message` 来访问 `data` 对象中的 `message` 属性。这样做更加方便，而且代码也更加简洁易读。

总之，数据代理是 Vue 中一种很有用的特性，它可以让我们更方便地访问组件内部的数据。