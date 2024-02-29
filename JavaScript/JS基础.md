 
### Array.sort()方法 
使用 JavaScript 的 Array.sort() 方法可以对数组进行排序。基本语法是:
```js
array.sort(compareFunction);
```
这个 compareFunction 是一个可选的比较函数,用来定义排序逻辑。
以下是一些常见的使用 sort 排序的方法:
**数字排序:**
```js
let numbers = [4, 1, 8, 3];
numbers.sort((a, b) => a - b); // [1, 3, 4, 8]
```
从小到大排序数字,compareFunction 中返回 a - b。
**字符串排序:**
```js
let words = ["banana", "apple", "orange"];
words.sort(); // ["apple", "banana", "orange"]  
```
默认是按字母表顺序排序。
**对象数组排序:**
```js
let products = [{price: 4}, {price: 2}, {price: 3}];
products.sort((a, b) => a.price - b.price);
```
compareFunction 中比较 price 属性。
**逆序排序:**
```js
numbers.sort((a, b) => b - a); // 逆序排序
```
返回 b - a 来交换排序顺序。
所以通过传入不同的 compare  Function,可以实现对数字、字符串、对象数组等各种排序需求。

#### 遍历对象的属性和值
要遍历对象的属性和值，可以使用多种方法，以下是几种常见的方法：
1. `for...in` 循环：使用 `for...in` 循环可以遍历对象的所有可枚举属性。在循环中，可以通过对象的键来访问对应的属性值。
```javascript
const obj = {
  name: "John",
  age: 30,
  city: "New York"
};
for (let key in obj) {
  console.log(key + ": " + obj[key]);
}
```
2. `Object.keys()` 方法：`Object.keys(obj)` 方法返回一个包含对象所有可枚举属性的数组。您可以对该数组使用 `forEach` 或 `for...of` 循环来遍历属性，并通过键访问对应的属性值。
```javascript
const obj = {
  name: "John",
  age: 30,
  city: "New York"
};
Object.keys(obj).forEach(key => {
  console.log(key + ": " + obj[key]);
});
```
3. `Object.entries()` 方法：`Object.entries(obj)` 方法返回一个包含对象所有可枚举属性和值的数组。您可以对该数组使用 `forEach` 或 `for...of` 循环来遍历属性和值。
```javascript
const obj = {
  name: "John",
  age: 30,
  city: "New York"
};
Object.entries(obj).forEach(([key, value]) => {
  console.log(key + ": " + value);
});
```
4. `Object.getOwnPropertyNames()` 方法：`Object.getOwnPropertyNames(obj)` 方法返回一个包含对象所有属性（包括不可枚举属性）的数组。您可以对该数组使用 `forEach` 或 `for...of` 循环来遍历属性，并通过键访问对应的属性值。
```javascript
const obj = {
  name: "John",
  age: 30,
  city: "New York"
};
Object.getOwnPropertyNames(obj).forEach(key => {
  console.log(key + ": " + obj[key]);
});
```
这些方法都可以用于遍历对象的属性和值，选择使用哪种方法取决于您的需求和偏好。
希望以上解释能够帮助您遍历对象的属性和值！如果您还有其他问题，请随时提问。


#### for迭代

`for...in`、`forEach`和`for...of`是 JavaScript 中用于循环迭代的不同语法结构，它们在用途和行为上有一些区别。
以下是它们的区别：
1. `for...in` 循环：
- 用于迭代对象的可枚举属性。
- 枚举的是对象的键（属性名），而不是属性值。
- 可以用于普通对象、数组和其他可迭代对象。
- 不保证属性的顺序，因此不适用于对属性顺序有严格要求的情况。
2. `forEach` 方法：
- 用于迭代数组的每个元素。
- 不能用于普通对象，只能用于数组和其他可迭代对象。
- 提供一个回调函数来处理每个元素，回调函数接收当前元素、索引和整个数组作为参数。
- 不支持 `break` 或 `continue` 语句，无法提前终止或跳过迭代。
3. `for...of` 循环：
- 用于迭代可迭代对象的值。
- 可以用于数组、字符串、Set、Map 等可迭代对象。
- 提供一个变量来接收每个值，可以直接访问值而不需要通过索引或键。
- 支持 `break` 和 `continue` 语句，可以提前终止或跳过迭代。
这些循环结构在不同场景下都有各自的适用性。选择使用哪个取决于您要迭代的数据类型以及您对循环控制的需求。
需要注意的是，`for...in` 循环和 `forEach` 方法只能用于可迭代对象，而 `for...of` 循环更加通用，可以用于遍历各种可迭代对象的值。

以下是使用 `for...in` 循环、`forEach` 方法和 `for...of` 循环的代码示例：
```javascript
// 示例对象
const obj = {
  name: "John",
  age: 30,
  city: "New York"
};
// 使用 for...in 循环迭代对象的属性
for (let key in obj) {
  console.log(`${key}: ${obj[key]}`);
}
// 使用 forEach 方法迭代数组的元素
const arr = [1, 2, 3];
arr.forEach((element, index) => {
  console.log(`Element at index ${index}: ${element}`);
});
// 使用 for...of 循环迭代可迭代对象的值
const iterable = "Hello";
for (let value of iterable) {
  console.log(value);
}
```
在上述示例中，我们使用了不同的迭代方式来遍历不同的数据类型。
1. 使用 `for...in` 循环遍历对象的属性：我们使用 `for...in` 循环迭代 `obj` 对象的属性，通过 `key` 访问属性名，通过 `obj[key]` 访问属性值。
2. 使用 `forEach` 方法遍历数组的元素：我们使用 `arr.forEach()` 方法迭代数组 `arr` 的每个元素，并通过回调函数访问每个元素的值和索引。
3. 使用 `for...of` 循环遍历可迭代对象的值：我们使用 `for...of` 循环迭代字符串 `iterable` 的每个字符，通过 `value` 直接访问每个字符的值。
这些示例展示了不同的迭代方式和用途，您可以根据需要选择适合的迭代方法。
希望以上示例对您有帮助！如果您还有其他问题，请随时提问。

#### for of迭代数组和对象

在 JavaScript 中，`for...of` 循环主要用于迭代可迭代对象的值，包括数组、字符串、Set、Map 等。
对于数组的迭代，`for...of` 循环会遍历数组的元素值，而不是索引或键。以下是迭代数组的示例：
```javascript
const arr = [1, 2, 3];
for (let value of arr) {
  console.log(value);
}
```
在上述示例中，`for...of` 循环遍历了数组 `arr` 的每个元素，将每个元素的值分别输出到控制台。
对于对象的迭代，由于对象不是可迭代对象，因此不能直接使用 `for...of` 循环来遍历对象的属性。但是，可以通过将对象转换为可迭代对象（如使用 `Object.entries()` 方法或 `Object.keys()` 方法）来实现类似的效果。以下是迭代对象的示例：
```javascript
const obj = { name: "John", age: 30 };
// 使用 Object.entries() 方法将对象转换为可迭代对象，并迭代键值对
for (let [key, value] of Object.entries(obj)) {
  console.log(`${key}: ${value}`);
}
// 或者使用 Object.keys() 方法迭代对象的属性
for (let key of Object.keys(obj)) {
  console.log(`${key}: ${obj[key]}`);
}
```
在上述示例中，我们使用 `for...of` 循环和解构赋值来迭代对象的键值对。通过 `Object.entries(obj)` 将对象转换为可迭代对象后，我们可以使用 `for...of` 循环来遍历键值对。另外，我们还可以使用 `Object.keys(obj)` 方法来迭代对象的属性，然后通过键访问对应的值。
需要注意的是，对象的属性遍历顺序不是固定的，它可能根据 JavaScript 引擎的实现而有所不同。

当使用原生JavaScript来创建响应式页面时，可以使用以下示例代码。我将对每个代码块进行详细的注释说明。
```javascript
// 获取需要操作的 DOM 元素
const container = document.getElementById("container"); // 获取 id 为 "container" 的元素
const button = document.getElementById("button"); // 获取 id 为 "button" 的元素
// 定义响应式数据
let count = 0; // 定义一个变量 count，初始值为 0
// 定义更新UI的函数
function updateUI() {
  container.innerHTML = `Count: ${count}`; // 更新 container 元素的内容为当前 count 的值
}
// 初始化UI
updateUI(); // 初始化页面的 UI，显示初始的 count 值
// 监听按钮点击事件
button.addEventListener("click", function() {
  // 更新数据
  count++; // 每次按钮点击时，count 值加一
  // 更新UI
  updateUI(); // 更新页面的 UI，显示更新后的 count 值
});
// 监听窗口大小改变事件
window.addEventListener("resize", function() {
  // 更新UI
  updateUI(); // 当窗口大小改变时，更新页面的 UI，显示当前的 count 值
});
```
在上述示例中，我们首先通过 `document.getElementById()` 方法获取了需要操作的 DOM 元素，分别是一个容器元素和一个按钮元素。然后定义了一个响应式数据变量 `count`，并初始化为 0。接下来定义了一个 `updateUI()` 函数，用于更新页面的 UI，即将 `count` 的值显示在容器元素中。在初始化阶段，我们调用 `updateUI()` 函数来展示初始的 `count` 值。
然后，我们使用 `addEventListener()` 方法监听了按钮的点击事件，每次点击按钮时，`count` 值会增加，然后调用 `updateUI()` 函数来更新页面的 UI。
另外，我们还使用 `addEventListener()` 方法监听了窗口大小改变事件，每次窗口大小改变时，也会调用 `updateUI()` 函数来更新页面的 UI。
这个示例演示了如何使用原生JavaScript创建一个简单的响应式页面，通过监听事件和更新UI函数，实现了在页面上展示响应式数据。

## 内置构造函数
 JavaScript中的内置构造函数是一些预定义的函数，它们用于创建特定类型的新对象。这些构造函数通常与特定的数据类型相关联，并且提供了创建和操作这些类型实例的方法。以下是一些常见的JavaScript内置构造函数：

1. **Object()**：
   创建一个新的空对象，或者根据传入的参数创建一个具有特定属性的对象。

```javascript
   let obj = new Object(); // 创建一个空对象
   let person = new Object({ name: "Alice", age: 30 }); // 创建一个带有属性的对象
   ```

2. **Array()**：
   创建一个新的数组实例。

```javascript
   let arr = new Array(); // 创建一个空数组
   let numbers = new Array(1, 2, 3, 4, 5); // 创建一个包含元素的数组
   ```

3. **String()**：
   创建一个新的字符串对象。

   ```javascript
   let str = new String("Hello"); // 创建一个字符串对象
   ```

4. **Number()**：
   创建一个新的数字对象。

```javascript
   let num = new Number(10); // 创建一个数字对象
   ```

5. **Boolean()**：
   创建一个新的布尔值对象。

```javascript
   let bool = new Boolean(true); // 创建一个布尔对象
   ```

6. **Date()**：
   创建一个新的日期对象。

```javascript
   let date = new Date(); // 创建当前日期和时间的日期对象
   let specificDate = new Date("2023-02-20"); // 创建特定日期的日期对象
   ```

7. **RegExp()**：
   创建一个新的正则表达式对象。

```javascript
   let pattern = new RegExp("^[a-zA-Z]"); // 创建一个正则表达式对象
   ```

8. **Function()**：
   创建一个新的函数对象。这个构造函数通常不直接使用，因为JavaScript中的函数声明和函数表达式提供了更简洁的创建函数的方式。

```javascript
   let func = new Function("x", "y", "return x + y"); // 创建一个匿名函数
   ```

9. **Math()**：
   数学对象，提供数学常量和函数。

```javascript
   let pi = Math.PI; // 获取圆周率
   let sqrt = Math.sqrt(16); // 计算平方根
```

10. **JSON()**：
用于处理JSON数据的全局对象。
```javascript
   let json = JSON.stringify({ name: "Alice", age: 30 }); // 将对象转换为JSON字符串
   let parsedJson = JSON.parse('{ "name": "Alice", "age": 30 }'); // 将JSON字符串解析为对象
```

11. **Error()**：
创建一个新的错误对象。

```javascript
let error = new Error("An error occurred"); // 创建一个错误对象
```

12. **Promise()**：
用于异步操作的构造函数，创建一个Promise对象。

```js
let promise = new Promise((resolve, reject) => {
  // 异步操作
  if (/* 条件 */) {
    resolve("Success");
  } else {
    reject("Failure");
  }
});
```

这些内置构造函数是JavaScript语言的核心部分，它们提供了丰富的功能，使得开发者能够创建和操作各种类型的数据结构。通过这些构造函数，你可以轻松地创建和管理复杂的应用程序。


[[响应式设计]]

[[模块系统]]