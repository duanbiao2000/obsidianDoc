
==除此之外，ES6及以后版本还新增了诸多新的原生API，如Symbol、Map、Set、WeakMap、WeakSet、Proxy、Reflect支持更多的功能和语言特性。==
- ES6新增常用API以及简洁实例代码：
6. 类和继承class和extends关键字：
```javascript
class Animal {
    constructor(name) {
        this.name = name;
    }
    speak() {
        console.log(`${this.name} makes a noise.`);
    }
}
class Dog extends Animal {
    constructor(name) {
        super(name);
    }
    speak() {
        console.log(`${this.name} barks.`);
    }
}
const dog = new Dog('Rufus');
dog.speak();
```
7. Promise API：
```javascript
function myAsyncFunction() {
  return new Promise((resolve, reject) => {
    setTimeout(() => resolve("resolved"), 1000)
  });
}
myAsyncFunction().then((data) => {
  console.log(data);
}).catch((error) => {
  console.log(error);
});
```
8. Symbol类型：
```javascript
const id1 = Symbol('id');
const id2 = Symbol('id');
console.log(id1 === id2); // false
```
9. Map 和 Set数据结构：
```javascript
// Map 定义与查询
const myMap = new Map();
myMap.set("one", 1);
myMap.set("two", 2);
console.log(myMap.get("one"));
// Set 
const mySet = new Set([1, 2, 3, 3, 4, 5]);
console.log([...mySet]); // [1, 2, 3, 4, 5]
```


1. DOM API
- document.querySelector(selector): 返回符合CSS选择器指定的第一个元素或null
```javascript
const myElement = document.querySelector('#my-element');
```
- document.createElement(tagName): 创建指定类型的HTML元素并返回该元素
```javascript
const newElement = document.createElement('h1');
newElement.innerHTML = 'New Content';
```
- element.addEventListener(event, handler, useCapture): 添加事件监听器并执行回调函数
```javascript
myElement.addEventListener('click', () => {
  console.log('clicked!');
});
```
- element.classList.add(class1, class2, ...): 为元素添加类名
```javascript
myElement.classList.add('active', 'highlighted');
```
- element.innerHTML: 获取或设置元素的HTML内容
```javascript
console.log(myElement.innerHTML);
myElement.innerHTML = 'New Content';
```
- element.style.property = value: 设置元素的样式属性
```javascript
myElement.style.color = 'red';
```
- element.setAttribute(name, value): 设置元素的自定义属性
```javascript
myElement.setAttribute('data-id', '123');
```

3. String API
- string.substr(startIndex, length): 返回字符串的一个子串
```javascript
const myString = "Hello World";
console.log(myString.substr(6, 5)); // 输出 World
```


4. Array API
- array.forEach(callback): 遍历数组并执行回调函数
```javascript
const myArray = [1, 2, 3];
myArray.forEach(item => console.log(item));
```
- array.map(callback): 遍历数组并返回新数组
```javascript
const myArray = [1, 2, 3];
const newArray = myArray.map(num => num * 2);
console.log(newArray); // 输出 [2, 4, 6]
```
- array.filter(callback): 创建一个新数组，其中包含原始数组根据条件筛选后的元素
```javascript
const myArray = [1, 2, 3, 4, 5];
const newArray = myArray.filter(num => num > 3);
console.log(newArray); // 输出 [4, 5]
```
- array.reduce(callback, initialValue): 将数组元素计算为单个值
```javascript
const myArray = [1, 2, 3];
const sum = myArray.reduce((a, b) => a + b, 0);
console.log(sum); // 输出 6
```
- array.sort(): 排序数组
```javascript
const myArray = [5, 3, 2, 1, 4];
myArray.sort();
console.log(myArray); // 输出 [1, 2, 3, 4, 5]
```
- array.splice(startIndex, deleteCount, item1, item2, ...): 修改数组，并向/从数组添加/删除元素
```javascript
const myArray = [1, 2, 3, 4, 5];
myArray.splice(1, 2);
console.log(myArray); // 输出 [1, 4, 5]
```
- array.concat(array2): 返回新数组，其中包含原始数组与另一个或多个数组连接的结果。
```javascript
const array1 = [1, 2];
const array2 = [3, 4];
const array3 = array1.concat(array2);
console.log(array3); // 输出 [1, 2, 3, 4]
```

6. Date API
- new Date(): 创建当前日期对象
```javascript
const myDate = new Date();
```
- date.getTime(): 获取从1970年1月1日至今毫秒数的时间戳
```javascript
console.log(myDate.getTime());
```
- date.getFullYear(): 获取当前日期的年份
```javascript
console.log(myDate.getFullYear());
```
- date.getMonth(): 获取当前日期的月份（0-11）
```javascript
console.log(myDate.getMonth());
```
- date.getDate(): 获取当前日期的日数
```javascript
console.log(myDate.getDate());
```
- date.getHours(): 获取当前日期的小时数（0-23）
```javascript
console.log(myDate.getHours());
```
- date.getMinutes(): 获取当前日期的分钟数（0-59）
```javascript
console.log(myDate.getMinutes());
```
2. [[Lodash]]
Lodash是一个流行的JavaScript实用程序库，提供了许多方便的功能来简化开发人员的编码。
安装： `npm install [[Lodash]]`
```javascript
import _ from 'lodash';
_.chunk(['a', 'b', 'c', 'd'], 2); // => [['a', 'b'], ['c', 'd']]
_.map([1, 2, 3], x => x * 2); // => [2, 4, 6]
_.filter([1, 2, 3], x => x % 2 === 0); // => [2]
const user = {
  name: 'Alice',
  age: 28,
  email: 'alice@example.com'
};
_.omit(user, ['email']); // => {name: 'Alice', age: 28}
```
3. Moment.js
Moment.js是一个流行的日期处理库，提供了许多方便的功能来轻松解析、验证、操作和格式化日期。
安装： `npm install moment`
```javascript
import moment from 'moment';
// 解析日期字符串
const date = moment('2016-03-05');
// 格式化日期对象
console.log(date.format('YYYY-MM-DD')); // 输出 '2016-03-05'
// 将本地时间转换为GMT时间
console.log(moment.utc('2016-03-05').format('YYYY-MM-DD')); // 输出 '2016-03-05'
// 计算两个日期之间的天数
const start = moment('2021-01-01');
const end = moment('2021-02-01');
console.log(end.diff(start, 'days')); // 输出 31
```
