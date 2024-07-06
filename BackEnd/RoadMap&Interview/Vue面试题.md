
### What are the lifecycle methods of VueJS?

Lifecycle hooks are a window into how the library you’re using works behind-the-scenes. By using these hooks, you will know when your component is created, added to the DOM, updated, or destroyed. Let's look at lifecycle diagram before going to each lifecycle hook in detail,
![[Pasted image 20230831140512.png]]

### What are the conditional directives?

VueJS provides set of directives to show or hide elements based on conditions. The available directives are: **v-if, v-else, v-else-if and v-show**

### What is vue instance?

Every Vue application works by creating a new Vue instance with the Vue function. Generally the variable vm (short for ViewModel) is used to refer Vue instance. You can create vue instance as below,↳

```js
var vm = new Vue({
  // options
})
```

