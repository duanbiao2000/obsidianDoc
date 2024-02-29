### 省二: vue3中的变化

在 Vue 3 中，相较于 Vue 2.x，有很多重大的改变和升级。

以下是 Vue 3 中的一些最显著的变化或升级：

1. Composition API: Vue 3 中引入了 React Hooks 风格的 Composition API，使组件逻辑更易于抽象组合。开发者们可以通过 ref、reactive、computed、watchEffect 等函数来管理组件状态和副作用。

2. 响应式系统升级：Vue 3 对响应系统进行了大幅升级，并使用 Proxy 替代 Object.defineProperty 来提高响应式对象的性能。

3. 改动的组件实例概念：组件实例在 Vue 3 中被拆分成两个部分——setup 和 render 函数。这种分离允许更容易地阅读和测试组件代码。

4. Teleport（传送门）API: Vue 3 添加了 Teleport API，可以很方便地将组件渲染到DOM结构的任何位置。

5. 缩小的包大小：由于 Vue 3 中删除了带有重复逻辑的代码并采用了 Tree-shaking 技术，因此Vue 3 的生产版本的体积大大缩小了。

6. 更好的 TypeScript 集成：Vue 3 设计时就考虑了项目中使用TypeScript的场景，并提供了更好的类型声明支持。

总之，Vue 3 的升级对于一些使用了 Vue 2.x 的开发者们来说可能需要熟悉一段时间，但是这些变化可以让我们更容易编写更灵活和性能更好的 Vue 应用。