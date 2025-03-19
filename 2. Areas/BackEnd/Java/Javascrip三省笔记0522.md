
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
- API示例代码
好的，以下是对每个API给出的代码示例：
1. DOM API：
```javascript
// 获取元素并修改内容
const myElement = document.querySelector('#my-element');
myElement.innerHTML = 'New Content';
// 添加事件监听器
myElement.addEventListener('click', () => {
  console.log('clicked!');
});
```
2. BOM API：
```javascript
// 获取浏览器信息
console.log(navigator.userAgent);
// 重定向页面
window.location.href = "http://example.com";
```
3. String API：
```javascript
// 截取字符串子串
const myString = "Hello World";
console.log(myString.substring(6, 11)); // 输出 World
// 查询字符索引值
console.log(myString.indexOf("W")); // 输出 6
console.log(myString.charAt(1)); // 输出 e
```
4. Array API：
```javascript
// 排序数组
const myArray = [1, 5, 2, 4, 3];
myArray.sort();
console.log(myArray); // [1, 2, 3, 4, 5]
// 合并两个数组
const array1 = [1, 2];
const array2 = [3, 4];
const array3 = array1.concat(array2);
console.log(array3); // [1, 2, 3, 4]
// 切割数组
const myArray = [1, 2, 3, 4, 5];
const slicedArray = myArray.slice(1, 4);
console.log(slicedArray); // [2, 3, 4]
```
5. Math API：
```javascript
// 取绝对值
console.log(Math.abs(-10)); // 输出 10
// 取随机数
console.log(Math.floor(Math.random() * 10)); // 输出一个 0~9 的随机整数
// 取最大值和最小值
console.log(Math.max(1, 2, 3)); // 输出 3
console.log(Math.min(1, 2, 3)); // 输出 1
```
6. Date API：
```javascript
const myDate = new Date();
console.log(myDate.getDate()); // 获取日，输出当天是几号
console.log(myDate.getMonth()); // 获取月，输出当前月份（0-11）
console.log(myDate.getFullYear()); // 获取年，输出当前年份
```
7. JSON API：
```javascript
// 将对象转换为JSON格式字符串
const myObject = {name: 'Alice', age: 28};
const jsonString = JSON.stringify(myObject);
console.log(jsonString); // 输出 {"name":"Alice","age":28}
// 将JSON格式字符串转换为对象
const parsedObject = JSON.parse(jsonString);
console.log(parsedObject.age); // 输出 28
```
8. Promise API：
```javascript
function myAsyncFunction() {
  return new Promise((resolve, reject) => {
    const random_boolean = Math.random() < 0.5;
    if (random_boolean) {
      setTimeout(() => resolve("resolved"), 1000)
    } else {
      reject(new Error("rejected"));
    }
  });
}
myAsyncFunction().then((data) => {
  console.log(data);
}).catch((error) => {
  console.log(error);
}).finally(() => {
  console.log('done');
});
```
### 15
好的，以下是每个类别重要性排前7的关键API及其代码实例和行注解：
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
2. BOM API
- window.navigator.userAgent: 获取浏览器相关信息
```javascript
console.log(window.navigator.userAgent);
```
- window.location.href: 重定向页面
```javascript
window.location.href = "http://example.com";
```
- window.alert(message): 弹出一个带有一条消息的警告框。
```  javascript
window.alert("Hello world!");
```
- window.prompt(message, defaultText): 弹出一个提示框，并要求用户输入文本。
```javascript
const name = window.prompt("Please enter your name:", "");
```
- window.setInterval(callback, delay): 每隔指定时间执行回调函数
```javascript
setInterval(() => {
  console.log('tick');
}, 1000);
```
- window.setTimeout(callback, delay): 延迟指定时间后执行回调函数。
```javascript
setTimeout(() => {
  console.log('done');
}, 2000);
```
- window.history.back(): 在浏览历史中向后移动一个步骤
```javascript
window.history.back();
```
3. String API
- string.substr(startIndex, length): 返回字符串的一个子串
```javascript
const myString = "Hello World";
console.log(myString.substr(6, 5)); // 输出 World
```
- string.indexOf(str): 返回字符串第一次出现在该字符串中的索引位置，如果不存在则返回-1。
```javascript
const myString = "Hello World";
console.log(myString.indexOf("W")); // 输出 6
```
- string.charAt(index): 返回给定索引处的字符
```javascript
const myString = "Hello World";
console.log(myString.charAt(1)); // 输出 e
```
- string.replace(searchValue, newValue): 将字符串中的searchValue替换为newValue
```javascript
const myString = "Hello World";
console.log(myString.replace('World', 'Alice')); // Hello Alice
```
- string.split(separator): 分割字符串成新的字符串数组
```javascript
const myString = "one,two,three,four";
const arr = myString.split(",");
console.log(arr[1]); // 输出 two
```
- string.trim(): 删除字符串前后的空格
```javascript
const myString = "  Hello World  ";
console.log(myString.trim()); // 输出 Hello World
```
- string.toUpperCase(): 将字符串全部转为大写
```javascript
const myString = "Hello World";
console.log(myString.toUpperCase()); // 输出 HELLO WORLD
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
5. Math API
- Math.abs(x): 返回指定数字的绝对值
```javascript
console.log(Math.abs(-10)); // 输出 10
```
- Math.random(): 返回一个介于0（包括）和1（不包括）之间的随机数
```javascript
console.log(Math.random()); // 输出介于0到1之间的一个小数
```
- Math.floor(x): 返回小于或等于一个给定数字的最大整数。
```javascript
console.log(Math.floor(2.5)); // 输出 2
```
- Math.ceil(x): 返回大于或等于给定数字的最小整数。
```javascript
console.log(Math.ceil(2.5)); // 输出 3
```
- Math.min(nums): 返回传递的一组数字中最小的值
```javascript
console.log(Math.min(1, -1, 5, 10)); // 输出 -1
```
- Math.max(nums): 返回传递的一组数字中最大的值
```javascript
console.log(Math.max(1, -1, 5, 10)); // 输出 10
```
- Math.round(x): 将一个数字四舍五入为最接近的整数。
```javascript
console.log(Math.round(2.4)); // 输出 2
console.log(Math.round(2.6)); // 输出 3
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
7. JSON API
- JSON.stringify(object): 将对象转换为JSON格式字符串
```javascript
const myObject = {name: 'Alice', age: 28};
const jsonString = JSON.stringify(myObject);
console.log(jsonString); // 输出 {"name":"Alice","age":28}
```
- JSON.parse(jsonString): 将符合JSON规范的字符串解析成对象
```javascript
const parsedObject = JSON.parse('{"name":"Alice","age":28}');
console.log(parsedObject.age); // 输出 28
```
- JSON.stringify()和JSON.parse()用于将数据从JavaScript对象转换为可存储的JSON字符串，以及从JSON字符串转换回JavaScript对象
- JSON.parse()方法可以接受第二个参数，用于查看属性和值之间的映射关系。

1. axios
Axios是一个基于Promise处理HTTP请求的库。它支持浏览器和Node.js，并且具有易用性和广泛的社区支持。
安装：`npm install axios`
```javascript
import axios from 'axios';
// 设置默认请求头
axios.defaults.headers.common['Authorization'] = 'Bearer TOKEN'
// 发送GET请求
axios.get('https://api.example.com/data')
  .then(response => {
    console.log(response.data);
  })
  .catch(error => {
    console.error(error);
  });
// 发送POST请求
axios.post('https://api.example.com/data', { name: 'Alice', age: 28 })
  .then(response => {
    console.log(response.data);
  })
  .catch(error => {
    console.error(error);
  });
```
2. Lodash
Lodash是一个流行的JavaScript实用程序库，提供了许多方便的功能来简化开发人员的编码。
安装： `npm install lodash`
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
4. D3.js
D3.js是一个流行的数据可视化库，用于创建漂亮且交互性强的图表和可视化效果。
安装： `npm install d3`
```javascript
import * as d3 from 'd3';
// 创建SVG元素并设置大小
const svg = d3.create('svg')
  .attr('viewBox', [0, 0, 800, 600]);
// 渲染圆形
svg.append('circle')
  .attr('cx', 400)
  .attr('cy', 300)
  .attr('r', 100)
  .style('fill', 'blue');
// 渲染矩形
svg.append('rect')
  .attr('x', 200)
  .attr('y', 200)
  .attr('width', 400)
  .attr('height', 200)
  .style('fill', 'green');
// 将SVG添加到文档中
document.body.appendChild(svg.node());
```
5. Chart.js
Chart.js是一个流行的JavaScript图表库，用于创建各种类型的漂亮图表。
安装：`npm install chart.js`
```javascript
import Chart from 'chart.js/auto';
const data = {
  labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
  datasets: [
    {
      label: 'Sales',
      data: [65, 59, 80, 81, 56, 55, 40],
      fill: false,
      borderColor: 'rgb(75, 192, 192)',
      tension: 0.1
    }
  ]
};
const config = {
  type: 'line',
  data: data,
  options: {}
};
const myChart = new Chart(
  document.getElementById('myChart'),
  config
);
```
