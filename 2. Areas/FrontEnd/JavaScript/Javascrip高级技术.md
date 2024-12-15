### Reflect.apply()

`Reflect.apply()` 是 JavaScript 中的一个内置函数，与 `Function.prototype.apply()` 相似，它允许你调用一个带有指定参数和 this 值的函数。不同之处在于，`Reflect.apply()` 是一个标准内置函数，而不是一个方法。
### 
`Reflect.apply()` 使用以下语法：

```
Reflect.apply(target, thisArg, argArray)
```

其中，`target` 表示要调用的目标函数；`thisArg` 是目标函数的 this 上下文；`argArray` 是传递给函数的参数数组。

例如：

```javascript
function sayHello(firstName, lastName) {
  console.log(`Hello, ${firstName} ${lastName}!`);
}

Reflect.apply(sayHello, null, ["Alice", "Smith"]); // Output: Hello, Alice Smith!
```



### effect()函数

在Vue框架中，`effect()`函数通常与Vue3的Composition API一起使用。`effect()`可以用于在Vue组件外部创建响应式的副作用函数。在这种方式下，当管理状态的响应式变量发生改变时，`effect()`函数会自动被调用。这个特性非常适合处理异步任务，比如定时器，网络请求等。

在Vue3中，我们可以在setup()函数中使用`ref()`或`reactive()`函数来创建响应式数据，然后通过`watch()`或`computed()`函数对它们进行监听。如果你需要访问外部资源（例如DOM节点或浏览器API），或你需要定义一个只在组件初始化时执行一次的副作用函数，那么你就可以使用`effect()`函数了。

以下是一个使用`effect()`函数的例子：

```javascript
import { effect, reactive } from 'vue'

export default {
  setup() {
    const state = reactive({
      count: 0
    })

    effect(() => {
      console.log(`Count is now ${state.count}`)
    })

    const increment = () => {
      state.count++
    }

    return {
      increment
    }
  }
}
```

这个例子定义了一个计数器组件，其中定义了一个响应式变量`count`和一个响应式的副作用函数，用于在`count`发生改变的时候打印出当前的值。

#### 访问器函数

访问器函数是 JavaScript 中的一种高级特性，用于访问和修改对象属性的值。它们可以通过定义 getter 和 setter 函数来实现，分别对应读取属性值和设置属性值。

以下是使用访问器函数的示例：

```javascript
const person = {
  firstName: "John",
  lastName: "Doe",
  get fullName() {
    return `${this.firstName} ${this.lastName}`;
  },
  set fullName(value) {
    const nameParts = value.split(" ");
    this.firstName = nameParts[0];
    this.lastName = nameParts[1];
  }
};

console.log(person.fullName); // Output: John Doe

person.fullName = "Jane Smith";
console.log(person.firstName); // Output: Jane
console.log(person.lastName); // Output: Smith
console.log(person.fullName); // Output: Jane Smith
```

在这个示例中，我们创建了一个拥有 `firstName` 和 `lastName` 属性的对象 `person`。然后，我们定义了 `fullName` 属性，其中包含 getter 和 setter 函数。getter 函数返回由 `firstName` 和 `lastName` 拼接而成的完整名称，setter 函数将传入的值拆分为数组，并通过更新 `firstName` 和 `lastName` 的方式修改对象属性的值。

通过使用访问器函数，我们可以在仅暴露 getter 函数时避免直接暴露属性本身，从而实现对属性值进行保护，同时也可以在需要更改属性值时进行一些逻辑控制。

#### 拦截函数

拦截函数指的是JavaScript中一个特殊的函数，可以被用于创建 Proxy 对象。 Proxy对象允许你在对JavaScript对象或函数进行操作时添加自定义逻辑。

当您创建一个 `Proxy()`对象时，您可以传递一个名为”handler”的对象。`handler`中包含一组拦截函数，用来定义在对代理对象执行各种操作时需要执行的操作。

以下是一些支持拦截函数的操作名称：

- `get`: 在访问代理对象的属性时执行。通常情况下会返回属性值，但是当使用 Proxy 时，我们可以通过重写 get 拦截器来修改返回的属性值。
- `set`: 当修改代理对象的属性时执行，在这个函数里面，您可以检查设置的新值是否合法，同时也可以记录属性的修改历史等功能。
- `has`: 在检查代理对象是否包含某个属性时执行。
- `deleteProperty`: 在删除代理对象中存在的属性时执行。
- `apply`: 当你调用一个 proxy 对象时执行， 就像一个函数调用一样。
- `construct`：当你在 proxy 对象上调用 new 关键字构造一个对象时执行。

接下来是一个简单的示例演示如何使用拦截函数：

```javascript
const person = {
  name: "John Doe"
};

const handler = {
  get: function(target, prop) {
    return prop in target ? target[prop] : "Property does not exist.";
  }
};

const proxyPerson = new Proxy(person, handler);

console.log(proxyPerson.name); // Output: John Doe
console.log(proxyPerson.age); // Output: Property does not exist.
```

在这个示例中，我们创建了一个名为“person”的对象，然后使用 `Proxy()`函数创建了代理对象 `proxyPerson`。`handler` 对象中包含了一个 get 函数，用于获取对象的属性。当 `proxyPerson` 对象中存在所请求的属性时，`get()`函数会返回属性值；否则它将抛出一条错误信息告诉你该属性不存在。

需要注意的是，在使用拦截函数时，应该避免在其内部无限递归访问代理对象，以及修改代理对象自身（应该只能修改原始对象）。

#### 内部方法和内部槽

JavaScript 中的所有对象都有一些内部方法和内部槽。这些是 JavaScript 引擎内部使用的机制，开发者无法直接访问或使用它们。

以下是对象常用的内部方法：

- `[[Get]]` 方法：用于获取对象属性的值。
- `[[Set]]` 方法：用于设置对象属性的值。
- `[[Delete]]` 方法：用于删除对象的某个属性。
- `[[HasProperty]]` 方法：用于判断是否存在指定名称的属性。
- `[[OwnPropertyKeys]]` 方法：用于获取对象自身属性名称列表。（注意：这里提到的“自身属性”指的是不沿着原型链继承下来的那些属性）。

除了内部方法之外，对象还具有一些内部槽。其中一些槽用于表示对象属性（例如[[Prototype]]，它表示原型链）；其他的则用于表示内部状态（例如[[Extensible]]，它表示对象是否可扩展）。

例如，以下代码展示了如何检查对象是否具有给定的属性：

```javascript
const person = {
  name: "Tom",
  age: 25
};

if (person.hasOwnProperty("name")) {
  console.log("person has 'name' property");
} else {
  console.log("person does not have 'name' property");
}
```

这段代码使用 `hasOwnProperty()` 函数来检查对象 `person` 是否包含属性 "name"。这个函数实际上会调用 `[[HasProperty]]` 内部方法并将其返回值作为结果。由于 "name" 确实是 `person` 对象的自身属性，因此 `hasOwnProperty()` 返回 true。

需要注意的是，虽然开发者无法直接访问或使用对象的内部方法和内部槽，但可以查看参考资料来获取关于它们的更多信息。 在绝大多数情况下，了解这些内部机制是不必要的，除非你正在进行 JavaScript 引擎的编写工作或你对语言本身的具体实现方式有深入的兴趣。

下面是一个简单的JavaScript代码示例，展示了如何定义内部方法和内部槽：

```js
class MyClass {
    constructor() {
        this.data = 0;
    }

    // 内部方法
    #internalMethod1() {
        // 对象的私有数据成员，在内部方法中可以随意操作
        this.data = 10;
        this.#doSomethingElse();
    }
    
    #internalMethod2(value) {
        this.data = value;
        this.#doAnotherThing();
    }
    
    #doSomethingElse() {
        // ...
    }
    
    #doAnotherThing() {
        // ...
    }
    
    // 内部槽函数
    onButtonClicked() {
        // 处理按钮点击事件的逻辑代码
        this.#internalMethod1();
    }
}

let myObject = new MyClass();
myObject.onButtonClicked();
```

在以上代码中，我们定义了一个名为`MyClass`的类，它包含了两个私有的内部方法`#internalMethod1`和`#internalMethod2`，以及两个私有函数`#doSomethingElse`和`#doAnotherThing`。

此外，我们还定义了一个名为`onButtonClicked`的公共内部槽方法。

在`onButtonClicked`方法中，我们可以调用`#internalMethod1`来处理按钮事件，因为它被声明为私有方法。同时，在ES6之后，我们可以使用`#`号来将方法与属性限制为类的私有成员。

当按钮被点击时，事件监听器会调用`onButtonClicked`函数来处理该事件。而该函数能够访问私有方法`#internalMethod1`，用于处理按钮点击事件。我们也可以通过调用`#internalMethod2`来传入参数来处理其他需要的事件。

通过使用内部方法和内部槽，我们可以轻松地在对象之间区分和识别不同的功能，并处理特定的事件或信号。

#### 私有方法, 私有函数

在面向对象编程中，私有函数和私有方法都是被限制在类的内部或子类中调用的函数。它们的主要区别在于，私有函数直接把实现细节隐藏起来，而私有方法则侧重于对类的内部进行操作。

下面是一个使用JavaScript实现的示例代码：

```js
class MyClass {
  constructor() {
    this.data = 0;
  }

  // 私有函数
  #privateFunction() {
    // 一些实现细节
    console.log("这是一个私有函数");
  }

  // 私有方法
  #privateMethod() {
    this.#privateFunction();
    this.data++;
    console.log(`私有操作之后数据变为：${this.data}`);
  }

  // 公共方法
  publicMethod() {
    this.#privateMethod();
    console.log("这是一个公共方法");
  }
}

const myObj = new MyClass();

// 调用公共方法
myObj.publicMethod();
```

在这个示例中，我们定义了一个名为`MyClass`的类，它包含一个私有函数`#privateFunction`和一个私有方法`#privateMethod`，还有一个公共方法`publicMethod`用于调用私有方法。

私有函数`#privateFunction`没有访问实例属性或方法，它只是执行一些特定任务并带有一些实现细节，它被定义为私有是因为我们不希望类的外部或子类直接访问该函数。

私有方法`#privateMethod`中调用了私有函数`#privateFunction`，并且对类的内部数据成员`data`进行增加操作。**该方法被定义为私有是因为它涉及到类的内部状态和属性，不想让类的外部或子类直接访问。**

公共方法`publicMethod`调用了私有方法`#privateMethod`，并打印一条公共消息。因此只有公共方法可在类外部使用。

总的来说，私有函数和私有方法都是用于实现隐藏类的实现细节的一种方式。其中私有函数隐藏的是其实现，而私有方法则是隐藏的类的内部状态和属性。

#### 常规对象,异质对象

在编程中，通常我们将对象分为两类：常规对象和异质对象。

常规对象是指它们都具有相同的属性和方法，这些属性和方法可以被统一访问和操作。例如，在JavaScript中，都是由Object类派生而来的对象，它们都具有相同的属性和方法，如toString(), valueOf()等等。

异质对象则是指拥有不同结构的对象，它们可能没有一个公共的接口或协议。比如，对于一个网页上的元素，它本质上是一个异质对象，因为它可能有不同的属性和方法，例如文本节点、图片元素、表单输入框等，它们之间并没有太多共同点。

常规对象在编程中是最常用的一种对象类型，它们使得代码模块化和可重用性更高，并且易于维护。异质对象则在某些场景下非常有用，例如前端开发中对于处理DOM元素时，需要区分不同类型的元素的属性和方法，这时就需要使用到异质对象。

下面是一个示例代码，用于说明常规对象和异质对象：

常规对象：

```js
// 常规对象
const person = {
  name: "John",
  age: 25,
  gender: "Male",
  sayHello: function() {
    console.log(`Hello, my name is ${this.name}`);
  }
};

person.sayHello(); // 输出：Hello, my name is John
```

在这个示例中，`person`是一个常规对象，它包含name、age和gender属性以及sayHello()方法。这些属性和方法都具有相同的类型，可以被统一访问和操作。

异质对象：

```js
// 异质对象
class Element {
  constructor(tagName, attributes, children) {
    this.tagName = tagName;
    this.attributes = attributes;
    this.children = children;
  }

  render() {
    // 渲染 DOM 元素
  }
}

// 不同类型的元素
const textNode = { type: "text", content: "Hello world" };
const imageElement = new Element("img", { src: "image.jpg", alt: "Image" }, []);
const inputElement = new Element("input", { type: "text", value: "" }, []);

imageElement.render();
inputElement.render();
```

在这个示例中，我们定义了一个名为Element的类，它表示一个DOM元素。而对于不同的DOM元素（文本节点、图片元素、表单输入框等），我们需要通过不同的数据结构来描述，这时就需要使用到异质对象。

这里的textNode是一个普通的JavaScript对象，它代表一个文本节点；而imageElement和inputElement则是异质对象，它们根据它们所代表的不同的元素分别拥有不同的属性和方法。在渲染处理时我们也需要根据不同的元素类型执行不同的逻辑代码。



#### JavaScript中的抽象方法实现

在JavaScript中，没有像Java等语言中的抽象类和接口这样的语言结构来支持抽象方法。但是可以使用函数、ES6中的类和原型链来实现类似于抽象方法的效果。

下面是一个使用JavaScript实现的抽象方法示例：

```js
class Shape {
  constructor(color) {
    if (this.constructor === Shape) {
      // 抛出错误，防止直接实例化Shape
      throw new Error("Can't instantiate abstract class");
    }
    this.color = color;
  }

  // 抽象方法
  area() {
    throw new Error("Method 'area()' must be implemented.");
  }
}

class Circle extends Shape {
  constructor(radius, color) {
    super(color);
    this.radius = radius;
  }

  // 实现抽象方法
  area() {
    return Math.PI * this.radius * this.radius;
  }
}

class Rectangle extends Shape {
  constructor(length, width, color) {
    super(color);
    this.length = length;
    this.width = width;
  }

  // 实现抽象方法
  area() {
    return this.length * this.width;
  }
}

const c = new Circle(10, "Red");
const r = new Rectangle(5, 7, "Blue");

console.log("Circle's area is " + c.area());
console.log("Rectangle's area is " + r.area());
```

在这个示例中，我们定义了一个抽象类Shape，它包含一个颜色属性和抽象方法area()。为了防止直接实例化Shape，我们在constructor中添加了检查逻辑。

而Circle和Rectangle都继承自Shape类，并通过实现area()方法来具体实现类的逻辑。

在调用Circle和Rectangle类的实例方法area()时，实际调用的是具体实现的area()方法，因为在父类抽象方法中抛出了一个错误，如果子类没有重写该方法，则会跑出错误。

虽然JavaScript没有严格限制抽象方法的实现方式，但是在上面的示例中，使用ES6类和继承机制可以非常方便地实现抽象方法的效果，提高代码的可读性和可维护性。

#### 数组的栈方法

在JavaScript中，数组是一种常用的数据结构类型，它提供了多种栈方法来支持对数组进行栈操作。下面列举几个常见的数组栈方法：

1. push()：向数组的末尾添加一个或多个元素，并返回新数组的长度。
```js
const arr = [1, 2, 3];
arr.push(4);
console.log(arr); // 输出: [1, 2, 3, 4]
```

2. pop(): 删除数组最后一个元素，并返回这个元素。
```js
const arr = [1, 2, 3];
const lastItem = arr.pop();
console.log(lastItem); // 输出: 3
console.log(arr); // 输出: [1, 2]
```

3. unshift(): 向数组的开头添加一个或多个元素，并返回新数组的长度。
```js
const arr = [1, 2, 3];
arr.unshift(0);
console.log(arr); // 输出: [0, 1, 2, 3]
```

4. shift(): 删除数组的第一个元素，并返回这个元素。
```js
const arr = [1, 2, 3];
const firstItem = arr.shift();
console.log(firstItem); // 输出: 1
console.log(arr); // 输出: [2, 3]
```

除此之外，还有一些其他常用的数组栈方法，如slice()、splice()、concat()等。使用数组的这些栈方法可以方便地操作数组，使得开发者可以更加灵活和高效地编写和管理JavaScript代码。

#### 命名视图组件

命名视图组件是 Vue Router 中的一项重要功能，允许我们为同一个路由添加多个命名视图。通过命名视图，我们可以方便地在同一个页面上同时渲染多个组件，极大地提高了业务设计的灵活性。

要为路由定义一个命名视图，我们需要将组件配置对象（Component Object）中的 `components` 属性设置为一个键值对对象。每个键都代表一个命名视图，其值则是该视图关联的组件。

例如：

```js
const router = new VueRouter({
  routes: [
    {
      path: '/',
      components: {
        default: Home,
        header: Header,
        footer: Footer
      }
    }
  ]
})
```

以上代码定义了 `/` 路由，并为它指定了三个命名视图：`default`、`header` 和 `footer`。分别使用 Home、Header 和 Footer 组件渲染这三个视图。

下面是一个示例模板，展示了如何在一个单文件组件中使用命名视图：

```html
<template>
  <div>
    <header><router-view name="header"></router-view></header>
    <main><router-view></router-view></main>
    <footer><router-view name="footer"></router-view></footer>
  </div>
</template>

<script>
export default {
  name: 'MyAppLayout'
}
</script>
```

在上面的代码中，我们定义了一个名为 `MyAppLayout` 的组件，它包含了三个 `<router-view>` 元素，分别用于加载三个命名视图。其中，`name` 属性指定了使用哪一个命名视图。

通过命名视图，我们能够完成很多灵活的业务设计，比如实现多语言布局、不同设备上的适配等。


[[React关键技术]]

#### symbol对象

非symbol对象指的是JavaScript语言中除了Symbol类型之外的所有数据类型，包括：

1. 原始数据类型：Undefined、Null、Boolean、Number和String
2. 引用数据类型：Object、Array、Function等


Symbol对象是一种新的原始数据类型，它可以通过全局函数Symbol()来创建。每个通过Symbol()创建的Symbol对象都是唯一的，并且不能与其他任何值相等，包括其他的Symbol对象。

在JavaScript中，Symbol对象通常用于作为对象的属性名（key），这样就可以避免由于属性名冲突而造成的意外覆盖或错误访问的问题。

下面是一些Symbol对象的常见应用场景：

1. 作为对象属性名（key）使用
```js
const obj = {
   [Symbol("foo")]: "foo",
   [Symbol("bar")]: "bar"
}
console.log(obj[Symbol("foo")]); // undefined
console.log(obj[Symbol("bar")]); // undefined
// 因为每个Symbol对象都是唯一的，因此无法通过不同的Symbol对象访问到相同的属性值
```

2. 使用内置符号（Well-known Symbol）操作对象
```js
const toStringSymbol = Symbol.toStringTag;
const arr = [1, 2, 3];
console.log(arr[toStringSymbol]);// "Array"
// 这里使用了内置符号Symbol.toStringTag来获取arr对象的默认标签值"Array"，从而更准确地表示arr对象的类型信息
```

3. 定义内部插件和框架
```js
const myPlugin = {
    [Symbol.for("pluginName")]: "myPlugin",
    // 省略其他属性和方法
};
// 让其他开发者使用myPlugin时，可以通过Symbol.for("pluginName")来获取插件名称，而无需担心该属性名会被意外覆盖或修改
```



#### Reflect.ownKeys()`方法

`Reflect.ownKeys()`方法是ES6新增的一个静态方法，用于返回一个包含对象自身所有属性键（不论是否可枚举）的数组。

与`Object.keys()`和`Object.getOwnPropertyNames()`相比，`Reflect.ownKeys()`可以获取到对象自身所有类型的属性键（包括 Symbol 类型）。

语法如下：
```
Reflect.ownKeys(target)
```

参数说明：
- target：目标对象

返回值：一个由目标对象自身的属性键所组成的数组。

示例：
```
const obj = {
  a: 1,
  [Symbol.for('b')]: 'B',
  [Symbol.for('c')]: 'C'
};

console.log(Object.getOwnPropertyNames(obj)); // ["a"]
console.log(Object.getOwnPropertySymbols(obj)); // [Symbol(b), Symbol(c)]

const keys = Reflect.ownKeys(obj);
console.log(keys); // ["a", Symbol(b), Symbol(c)]
```
在上述示例中，我们定义了一个obj对象，它包含了一个普通属性'a'和两个 Symbol 属性。通过 Object.keys() 和 Object.getOwnPropertySymbols() 分别无法获取到完整的属性列表，但是通过使用 `Reflect.ownKeys()` 方法，我们可以获取到包含所有属性键的数组 ['a', Symbol(b), Symbol(c)]。





#### 代码解读

```javascript
Array.prototype.BB = 200;
let arr = [10,20];
arr[Symbol('AA')] = 100;
let keys = Reflect.ownKeys(arr);
keys.forEach(key =>
  console.log(`key:${String(key)}, value=${arr[key]}`)
);
```
这段代码首先在 Array.prototype 上添加了属性 BB，然后创建一个包含两个元素和一个 Symbol 属性的数组 arr。接下来通过 `Reflect.ownKeys()` 方法获取了 arr 的所有键名，并使用 forEach() 循环遍历这些键名并输出每个属性的名称和对应值。

在控制台中运行上述代码会输出以下结果：
```
key:0, value=10
key:1, value=20
key:Symbol(AA), value=100
```

需要注意的是，在使用 Symbol 类型作为属性键时，无法使用点操作符或者中括号操作符来访问这个属性，只能通过 `Reflect.ownKeys()` 或者 `Object.getOwnPropertySymbols()` 方法来获取它的键名，然后使用中括号操作符来访问属性。

[[React关键技术]]

[[vue组件间通信代码示例]]
[[React组件间通信代码示例]]

#### React性能分析工具

React Addon Perf是一个React的性能分析工具，它可以帮助你分析和调试React组件以提高性能。你可以使用Perf来找出慢速组件或有昂贵渲染的更新方式，并及时针对这些问题进行性能优化。

要使用React Addon Perf，请按照以下步骤：

1. 首先，在你的React应用程序中引入Perf。你可以从React包中导入它：

```javascript
import Perf from 'react-addons-perf';
```

2. 接下来，需要在浏览器环境下启用Perf选项（例如，放在开发模式下）：
```javascript
window.Perf = Perf;
```

3. 然后，在需要分析性能的地方，调用以下代码：

```javascript
Perf.start();
// Perform your operation here...
Perf.stop();
Perf.printWasted();
```

上面的代码会记录开始和结束时间，并打印出浪费时间最多的组件的列表。

注意，Perf只应该在开发模式下使用，并且不应该在部署到生产环境之前留在代码中。在生产环境中，Perf会影响应用程序的性能。

总之，使用React Addon Perf作为React性能分析工具可以帮助你识别和解决性能问题，从而提高应用程序的质量和用户体验。

[[React关键技术]]