---
aliases: 
theme: 
original: 
url: 
author: 
date_created: 2024-08-05T12:03:00
date_updated: 2024-08-05T12:05:00
type: 
high_priority: false
---


**`this` 的指向完全取决于函数的调用方式，而不是函数声明的位置。**

### 为什么这么说？

- **`this` 指向的是调用函数的对象。**

  - **作为对象的方法调用：** 当函数作为某个对象的方法被调用时，`this` 指向这个对象。
  - **作为构造函数调用：** 当函数使用 `new` 关键字调用时，`this` 指向新创建的对象。
  - **作为普通函数调用：** 在严格模式下，`this` 指向 `undefined`；在非严格模式下，`this` 指向全局对象（通常是 `window`）。
  - **通过 `apply` 或 `call` 方法调用：** 可以手动指定 `this` 的值。
- **函数声明位置不影响 `this`：** 函数声明的位置，无论是全局作用域、函数内部还是对象属性，都不会直接影响 `this` 的绑定。

### 举例说明

JavaScript

```
// 全局函数
function foo() {
  console.log(this); // 在非严格模式下指向window
}

// 对象方法
const obj = {
  name: 'Alice',
  sayHello: function() {
    console.log(this.name); // 指向obj
  }
};

// 构造函数
function Person(name) {
  this.name = name;
}
const person = new Person('Bob'); // this指向person

// apply/call
function bar() {
  console.log(this);
}
bar.call({ name: 'Charlie' }); // this指向{ name: 'Charlie' }
```

### 总结

- `this` 的绑定是动态的，在函数执行时才确定。
- 函数的调用方式决定了 `this` 的指向。
- 函数声明的位置对 `this` 的绑定没有直接影响。

### 影响 `this` 的因素

- **调用方式：** 直接调用、作为方法调用、作为构造函数调用、`apply` 或 `call` 调用。
- **执行上下文：** 严格模式或非严格模式。
- **箭头函数：** 箭头函数的 `this` 指向是词法作用域中的 `this`。

### 常见误区

- **认为 `this` 总是指向当前对象：** 只有在函数作为对象的方法调用时，`this` 才指向当前对象。
- **认为 `this` 在函数定义时就确定了：** ==`this` 的绑定是在函数执行时才确定的。==

### 拓展

- **箭头函数中的 `this`：** 箭头函数没有自己的 `this`，它的 `this` 指向的是定义它时所在的作用域的 `this`。
- **`bind` 方法：** 可以创建一个新的函数，将 `this` 永久绑定到某个对象。

**理解 `this` 的绑定是掌握 JavaScript 核心概念的关键。**

**想深入了解哪些方面呢？** 比如：

- `this` 在不同上下文中的指向
- `bind`、`call`、`apply` 的区别
- 箭头函数中的 `this`
- `this` 在异步编程中的应用

## JavaScript 中 `this` 的指向：一个详细的解释

**`this` 是 JavaScript 中一个非常特殊的关键字，它的值在运行时动态决定，并且会随着执行环境的不同而发生变化。**

### `this` 的指向取决于什么？

- **调用方式：** 函数的调用方式直接决定了 `this` 的指向。
- **执行上下文：** 严格模式和非严格模式下，`this` 的默认指向不同。

### `this` 在不同上下文中的指向

#### 1. **全局上下文**

- **非严格模式下：** `this` 指向全局对象（通常是 `window` 对象）。
- **严格模式下：** `this` 为 `undefined`。

JavaScript

```
console.log(this); // 非严格模式下输出 window，严格模式下输出 undefined
```

#### 2. **作为对象的方法调用**

- `this` 指向调用该方法的对象。

JavaScript

```
const person = {
  name: 'Alice',
  sayHello: function() {
    console.log(this.name); // 输出 Alice
  }
};
person.sayHello();
```

#### 3. **作为构造函数调用**

- `this` 指向新创建的对象。

JavaScript

```
function Person(name) {
  this.name = name;
}
const person = new Person('Bob');
console.log(person.name); // 输出 Bob
```

#### 4. **作为普通函数调用**

- **非严格模式下：** `this` 指向全局对象。
- **严格模式下：** `this` 为 `undefined`。

JavaScript

```
function foo() {
  console.log(this);
}
foo(); // 非严格模式下输出 window，严格模式下输出 undefined
```

#### 5. **apply、call 和 bind 方法**

- **apply、call：** 可以手动指定 `this` 的指向。
- **bind：** 创建一个新函数，将 `this` 永久绑定到某个对象。

JavaScript

```
function bar(a, b) {
  console.log(this.name + ": " + (a + b));
}
const obj = {name: "test"};
bar.call(obj, 2, 3); // 输出：test: 5
```

### 箭头函数中的 `this`

- 箭头函数没有自己的 `this`，它的 `this` 指向的是定义它时所在的作用域的 `this`。

JavaScript

```
const person = {
  name: 'Alice',
  greet: function() {
    const arrow = () => {
      console.log(this.name); // 指向 person
    };
    arrow();
  }
};
```

### 总结

- `this` 的指向是动态的，在函数执行时才确定。
- `this` 的值取决于函数的调用方式和执行上下文。
- 箭头函数的 `this` 指向是静态的，由其定义时所在的作用域决定。

### 常见误区与注意事项

- `this` 不总是指向当前对象，它的指向取决于调用方式。
- 箭头函数没有自己的 `this`，它的 `this` 指向是词法作用域中的 `this`。
- 在异步编程中，`this` 的指向可能发生变化，需要特别注意。

### 进一步学习

- **`bind`、`call`、`apply` 的区别和用法**
- **箭头函数的 `this` 的详细解释**
- **`this` 在异步编程中的应用**
- **`this` 在类中的使用**

**希望这份详细的解释能帮助你更好地理解 JavaScript 中的 `this`！**

**如果你还有其他问题，欢迎随时提问。**

**想深入了解哪个方面呢？** 比如：

- `this` 在异步编程中的行为
- `this` 和闭包的关系
- `bind`、`call`、`apply` 的实际应用场景

**请告诉我你的需求，我会尽力为你解答。**
