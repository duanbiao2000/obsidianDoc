
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

### Why do you need to use key attribute on for directive?

In order to track each node’s identity, and thus reuse and reorder existing elements, you need to provide a unique `key` attribute for each item with in `v-for` iteration. An ideal value for key would be the unique id of each item.

Let us take an example usage,

```js
<div v-for="item in items" :key="item.id">
  {{item.name}}
</div>
```

Hence, It is always recommended to provide a key with v-for whenever possible, unless the iterated DOM content is simple.↳
**Note:** You shouldn’t use non-primitive values like objects and arrays as v-for keys. Use string or numeric values instead.

### What are the array detection mutation methods?

As the name suggests, mutation methods modifies the original array.

Below are the list of array mutation methods which trigger view updates.↳

1. push()
2. pop()
3. shift()
4. unshift()
5. splice()
6. sort()
7. reverse()

If you perform any of the above mutation method on the list then it triggers view update. For example, push method on array named 'items' trigger a view update,

### What are the array detection non-mutation methods?

The methods which do not mutate the original array but always return a new array are called non-mutation methods.

Below are the list of non-mutation methods,

1. filter()
2. concat()
3. slice()

For example, lets take a todo list where it replaces the old array with new one based on status filter,↳

```js
vm.todos = vm.todos.filter(function (todo) {
  return todo.status.match(/Completed/)
})
```

This approach won't re-render the entire list due to VueJS implementation.

### What are the caveats of object changes detection?

Vue cannot detect changes for the object in property addition or deletion.

Lets take an example of user data changes,

```js
var vm = new Vue({
  data: {
    user: {
      name: 'John'
    }
  }
})

// `vm.name` is now reactive

vm.user.email = john@email.com // `vm.user.email` is NOT reactive
```

You can overcome this scenario using the Vue.set(object, key, value) method or Object.assign(),

```js
Vue.set(vm.user, 'email', 'john@email.com');
// (or)
vm.user = Object.assign({}, vm.user, {
  email: john@email.com
})
```

### How do you implement two-way binding?

You can use the `v-model` directive to create two-way data bindings on form input, textarea, and select elements.

Lets take an example of it using input component,

```html
<input v-model="message" placeholder="Enter input here">
<p>The message is: {{ message }}</p>
```

Remember, v-model will ignore the initial `value`, `checked` or `selected` attributes found on any form elements. So it always use the Vue instance data as the source of truth.

### What are props?

Props are custom attributes you can register on a component. When a value is passed to a prop attribute, it becomes a property on that component instance. You can pass those list of values as props option and use them as similar to data variables in template.

```js
Vue.component('todo-item', {
  props: ['title'],
  template: '<h2>{{ title }}</h2>'
})
```

Once the props are registered, you can pass them as custom attributes.

```html
<todo-item title="Learn Vue conceptsnfirst"></todo-item>
```

### When component needs a single root element?

In VueJS 2.x, every component must have a single root element **when template has more than one element**. In this case, you need to wrap the elements with a parent element.

```html
<template>
   <div class="todo-item">
       <h2>{{ title }}</h2>
       <div v-html="content"></div>
   </div>
</template>
```

Otherwise there will an error throwing, saying that "Component template should contain exactly one root element...".

Whereas in 3.x, components now can have multiple root nodes. This way of adding multiple root nodes is called as fragments.

```html
<template>
     <h2>{{ title }}</h2>
     <div v-html="content"></div>
</template>
```

### How do you communicate from child to parent using events?

If you want child wants to communicate back up to the parent, then emit an event from child using `$emit` object to parent,

```js
Vue.component('todo-item', {
  props: ['todo'],
  template: `
    <div class="todo-item">
      <h3>{{ todo.title }}</h3>
      <button v-on:click="$emit('increment-count', 1)">
        Add
      </button>
      <div v-html="todo.description"></div>
    </div>
  `
})
```

Now you can use this todo-item in parent component to access the count value.

```html
<ul v-for="todo in todos">
  <li>
    <todo-item
      v-bind:key="todo.id"
      v-bind:todo="todo"
      v-on:increment-count="total += 1"
    /></todo-item>
  </li>
</ul>
<span> Total todos count is {{total}}</span>
```


