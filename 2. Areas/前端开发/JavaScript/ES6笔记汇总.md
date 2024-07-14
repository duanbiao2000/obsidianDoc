在ES6中，对象字面量有两种简写形式：属性简写和方法简写。

属性简写允许我们在定义对象属性时省略属性名和变量名相同的属性值。例如：

```javascript
let x = 1;
let y = 2;

// 没有使用属性简写
let obj1 = { x: x, y: y };

// 使用属性简写
let obj2 = { x, y };
```

方法简写允许我们在定义对象方法时省略`function`关键字。例如：

```javascript
// 没有使用方法简写
let obj1 = {
  sayHello: function() {
    console.log('Hello!');
  }
};

// 使用方法简写
let obj2 = {
  sayHello() {
    console.log('Hello!');
  }
};
```

您还想了解什么？

箭头函数是ES6中新增的一种函数定义方式。它与普通函数有以下几点区别：

1. 语法不同：箭头函数使用`=>`符号定义，语法更简洁。
2. `this`指向不同：箭头函数内部的`this`是词法作用域，由上下文确定；普通函数内部的`this`指向调用该函数的对象。
3. 箭头函数不能用作构造函数，不能使用`new`关键字调用。
4. 箭头函数没有自己的`arguments`对象，可以访问外层函数的`arguments`对象。

下面是两个示例，分别展示了普通函数和箭头函数的定义和使用：

```javascript
// 示例1: 定义和使用普通函数
function add(x, y) {
  return x + y;
}

let result = add(1, 2);
console.log(result); // 3

// 示例2: 定义和使用箭头函数
let add = (x, y) => x + y;

let result = add(1, 2);
console.log(result); // 3
```

在示例1中，我们使用`function`关键字定义了一个普通函数。在示例2中，我们使用箭头函数定义了一个等效的函数。