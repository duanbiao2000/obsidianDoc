`Object.defineProperty` 是一个 JavaScript 方法，用于在对象上定义新属性或修改现有属性。它接受三个参数：要定义属性的对象、属性名称和一个描述符对象。描述符对象包含了对属性的描述，如它的值、是否可枚举、是否可写等。

下面是一个简单的代码示例，演示了如何使用 `Object.defineProperty` 方法定义一个新属性：

```javascript
var obj = {}

// 使用 Object.defineProperty 定义一个新属性
Object.defineProperty(obj, 'myProperty', {
  value: 'This is my property',
  writable: true,
  enumerable: true,
  configurable: true
})

console.log(obj.myProperty) // 输出 'This is my property'
```

在上面的代码中，我们创建了一个空对象 `obj`，然后使用 `Object.defineProperty` 方法在 `obj` 上定义了一个名为 `myProperty` 的新属性。我们通过传递一个描述符对象来指定该属性的值、是否可写、是否可枚举和是否可配置。

当我们使用 `console.log(obj.myProperty)` 输出该属性的值时，可以看到它的值为 `'This is my property'`。

希望这个例子能帮助你理解 `Object.defineProperty` 方法的用法！

`Object.defineProperty` 方法常用于定义或修改对象的属性，它提供了比直接赋值更多的控制。例如，你可以使用它来定义一个只读属性，或者定义一个属性的 getter 和 setter 方法。

下面是一些使用 `Object.defineProperty` 方法的常见场景：

- 定义只读属性：你可以使用 `Object.defineProperty` 方法定义一个只读属性，即不能被修改的属性。例如：

```javascript
var obj = {}

// 定义一个只读属性
Object.defineProperty(obj, 'myProperty', {
  value: 'This is my property',
  writable: false
})

obj.myProperty = 'New value'
console.log(obj.myProperty) // 输出 'This is my property'
```

在上面的代码中，我们在 `obj` 上定义了一个名为 `myProperty` 的只读属性。当我们尝试修改该属性的值时，它并没有改变。

- 定义 getter 和 setter：你可以使用 `Object.defineProperty` 方法定义一个属性的 getter 和 setter 方法，用于在获取或设置属性值时执行特定的操作。例如：

```javascript
var obj = {
  firstName: 'John',
  lastName: 'Doe'
}

// 定义 fullName 属性的 getter 和 setter
Object.defineProperty(obj, 'fullName', {
  get: function () {   //可简写为get(){
    return this.firstName + ' ' + this.lastName
  },
  set: function (value) {
    var parts = value.split(' ')
    this.firstName = parts[0]
    this.lastName = parts[1]
  }
})

console.log(obj.fullName) // 输出 'John Doe'

obj.fullName = 'Jane Doe'
console.log(obj.firstName) // 输出 'Jane'
```

在上面的代码中，我们在 `obj` 上定义了一个名为 `fullName` 的属性，并为它定义了 getter 和 setter 方法。当我们获取 `fullName` 属性的值时，它会返回 `firstName` 和 `lastName` 属性拼接而成的字符串。当我们设置 `fullName` 属性的值时，它会将值分割为两部分，并分别赋值给 `firstName` 和 `lastName` 属性。

这些是使用 `Object.defineProperty` 方法的一些常见场景。希望对你有所帮助！