2023-07-13



当然，以下是来自 GitHub 各位开发者分享的 JavaScript 和 React 项目中，我认为精妙优雅且易于理解的代码示例。对于每个示例，我也会给出重构前不优美的代码和重构后优美的代码，并附有行注释和代码说明。

1. 示例一：使用 JavaScript 实现 debounce 函数

debounce 函数可以帮助我们限制函数的执行次数，以便防止过多的资源浪费。下面是重构前和重构后的代码：


```javascript
function debounce(fn, delay) {
  let timeoutId;

  // Return the debounced function
  return function debounced(...args) {
    if (timeoutId) {
      clearTimeout(timeoutId);
    }
    timeoutId = setTimeout(() => {
      fn.apply(this, args);
    }, delay);
  };
}
```

```jsx
import React from 'react';
import PropTypes from 'prop-types';

function Person({ name, age, city, country }) {
  return (
    <div>
      <h2>Name: {name}</h2>
      <p>Age: {age}</p>
      <p>Location: {city}, {country}</p>
    </div>
  );
}

Person.propTypes = {
  name: PropTypes.string.isRequired,
  age: PropTypes.number.isRequired,
  city: PropTypes.string.isRequired,
  country: PropTypes.string.isRequired
};

export default Person;
```

```javascript
function getFullNames(people) {
  return people
    .filter(person => person.age >= 18)
    .map(person => `${person.firstName} ${person.lastName}`);
}
```

```javascript
const objs = [
  { name: 'Tom', age: 25 },
  { name: 'Jerry', age: 22 },
  { name: 'Spike', age: 30 }
];

// 使用Array.prototype.map()获取所有对象的名称
const names = objs.map(obj => obj.name);

console.log(names); // 输出: ["Tom", "Jerry", "Spike"]
```


```jsx
import React from 'react';

// 将List组件转换为函数式组件，以简化代码结构和提高性能
const List = ({ items }) => (
  <ul>
    {/* 使用项目内容作为key，可以避免使用索引 */}
    {items.map(item => (
      <li key={item}>{item}</li>
    ))}
  </ul>
);
```


```javascript
// 统计某个数组内数字出现的频率
function arrNumFreq(arr) {
  return arr.reduce((acc, cur) => {
    acc[cur] = (acc[cur] || 0) + 1;
    return acc;
  }, {});
}
```



```jsx
// 引入 React 库和 useState 钩子
import React, { useState } from 'react';

function Example() {
  // 声明一个名为 value 的状态变量，并初始化为空字符串
  const [value, setValue] = useState('');

  function handleChange(e) {
    // 处理输入框中的输入值改变事件，将新值更新到 value 变量中
    setValue(e.target.value);
  }

  return (
    // 返回一个 <div> 元素作为 React 组件的根元素
    <div>
      <label>
        输入:
        <input 
          // 定义一个类型为 text 的输入框，值为变量 value 的当前值，
          // 并在输入框的内容发生变化时调用 handleChange 函数更新 value 变量
          type="text" 
          value={value} 
          onChange={handleChange} 
        />
      </label>
      // 显示当前 value 变量的值
      <p>{value}</p>
    </div>
  );
}
```



```javascript
// 如果 x 不为 0，返回 y / x，否则返回 undefined
return x !== 0 ? y / x : undefined;
```

注释：使用了条件运算符（ternary operator）来简化 if/else 语句。


## 使用 `async/await` 简化了繁琐的 Promise 链式调用
```javascript
function loadPage() {
  console.log('Loading...');
  // 发送 GET 请求获取页面内容
  fetch('/api/page')
    .then(function(response) {
      return response.text();
    })
    .then(function(text) {
      // 将请求到的内容插入页面
      document.querySelector('#content').innerHTML = text;
      console.log('Finished loading.');
    })
    .catch(function(err) {
      console.error(err);
    });
}
```

重构后：

```javascript
async function loadPage() {
  console.log('Loading...');
  try {
    // 使用 async/await 异步获取页面内容
    const response = await fetch('/api/page');
    const text = await response.text();
    // 将请求到的内容插入页面
    document.querySelector('#content').innerHTML = text;
    console.log('Finished loading.');
  } catch (err) {
    console.error(err);
  }
}
```



##  `Object.assign()`

重构前：

```javascript
// 获取 ID 为 myId 的元素，设置其背景色、文字颜色、字号和 padding 样式
var element = document.getElementById('myId');
element.style.backgroundColor = '#f00';
element.style.color = 'white';
element.style.fontSize = '24px';
element.style.padding = '10px';
```

重构后：

```javascript
// 获取 ID 为 myId 的元素，并将多个样式属性对象合并到一个新对象中进行设置
var element = document.getElementById('myId');
Object.assign(element.style, {
  backgroundColor: '#f00',
  color: 'white',
  fontSize: '24px',
  padding: '10px'
});
```

注释：使用 `Object.assign()` 合并了重复的代码行。



## `Object.values()`

```javascript
// 获取 obj 对象的所有键名，并加入 values 数组返回
var keys = Object.keys(obj);
var values = [];
for (var i = 0; i < keys.length; i++) {
  var key = keys[i];
  values.push(obj[key]);
}
```

重构后：

```javascript
// 获取 obj 对象的所有值，返回包含所有值的数组
var values = Object.values(obj);
```

注释：使用 `Object.values()` 简化了原本繁琐的遍历操作。



##  使用 `reduce()` 和解构来查找最小值

重构前：

```javascript
var users = [
  { name: 'Alice', age: 22 },
  { name: 'Bob', age: 21 },
  { name: 'Charlie', age: 25 }
];

// 通过从年龄属性逆序排序来获取最年轻的用户
var youngestUser = users.sort(function(a, b) {
  return b.age - a.age;
})[0];
```

重构后：

```javascript
const users = [
  { name: 'Alice', age: 22 },
  { name: 'Bob', age: 21 },
  { name: 'Charlie', age: 25 }
];

// 使用解构和 Math.min 获得年龄最小的用户
const youngestUser = users.reduce((acc, cur) => {
  return cur.age < acc.age ? cur : acc;
});
```



### 示例 2：

重构前：

```javascript
function getList() {
  // 获取列表数据，将其返回给调用者
  return fetch('/api/list').then(function(response) {
    return response.json();
  }).then(function(data) {
    return data.items;
  });
}
```

重构后：

```javascript
async function getList() {
  // 异步获取并返回列表数据
  const response = await fetch('/api/list');
  const { items } = await response.json();
  return items;
}
```

注释：使用 `async/await` 简化了原本繁琐的 Promise 链式调用。

##  可选链运算符（optional chaining）和空值合并运算符（nullish coalescing operator）

重构前：

```javascript
var a = 0;
var b = 'default';
if (params) {
  if (params.a) {
    a = params.a;
  }
  if (params.b) {
    b = params.b;
  }
}
```

重构后：

```javascript
const a = params?.a ?? 0;
const b = params?.b ?? 'default';
```

注释：使用了可选链运算符（optional chaining）和空值合并运算符（nullish coalescing operator）。

### 示例 4：

重构前：

```javascript
const minDate = startDate ? new Date(startDate) : new Date('1970-01-01');
```

重构后：

```javascript
const minDate = new Date(startDate ?? '1970-01-01');
```

注释：使用空值合并运算符（nullish coalescing operator）简化代码。

### 示例 5：

重构前：

```js
class Person extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      name: props.name,
      age: props.age,
      city: props.city
    };
  }

  render() {
    return (
      <div>
        <h2>{this.state.name}</h2>
        <p>{this.state.city}, {this.props.country}</p>
        <p>Age: {this.state.age}</p>
      </div>
    );
  }
}
```

重构后：

```js
function Person({ name, age, city, country }) {
  return (
    <div>
      <h2>{name}</h2>
      <p>{city}, {country}</p>
      <p>Age: {age}</p>
    </div>
  );
}
```

注释：使用函数组件和解构来简化代码，同时避免了状态的复杂性。

