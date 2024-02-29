2023-07-13

#effective

当然，以下是来自 GitHub 各位开发者分享的 JavaScript 和 React 项目中，我认为精妙优雅且易于理解的代码示例。对于每个示例，我也会给出重构前不优美的代码和重构后优美的代码，并附有行注释和代码说明。

1. 示例一：使用 JavaScript 实现 debounce 函数

debounce 函数可以帮助我们限制函数的执行次数，以便防止过多的资源浪费。下面是重构前和重构后的代码：

重构前：
```javascript
function debounce(func, delay) {
  let timer;
  return function() {
    const args = arguments;
    const context = this;
    clearTimeout(timer);
    timer = setTimeout(() => {
      func.apply(context, args);
    }, delay);
  };
}
```

重构后：
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
这段优美代码质量好的原因如下：

- 对变量进行了<mark style="background: #FF5582A6;">度量衡</mark>取名，代码可读性高
- 明确表达了参数和返回类型
- 使用了清晰的缩进，使代码更容易阅读

2. 示例二: 使用 React hooks 和 propTypes 进行组件复用

React 的 hooks 和propTypes 可以让组件变得更加具有复用性。下面是重构前和重构后的代码：

重构前：

这段 React 组件代码是一个名为 `Person` 的函数组件，根据传入的 `props` 信息显示人物的姓名、年龄和所在的城市和国家。以下是逐行解释：

```jsx
import React, { Component } from 'react';
import PropTypes from 'prop-types';

class Person extends Component {
  render() {
    // 从 props 对象中获取相关属性值
    const { name, age, city, country } = this.props;
    return (
      // 返回一个内容区域包括 name, age, city, country 属性的 <div> 元素
      <div>
        <h2>Name: {name}</h2>
        <p>Age: {age}</p>
        <p>Location: {city}, {country}</p>
      </div>
    );
  }
}
```

这个组件使用了 ES6 的 `destructuring` 方法从 `props` 中提取子属性。在 `render()` 方法中返回一个包含姓名、年龄、城市和国家的文本信息的 `<div>` 元素。

下面的代码通过 `PropTypes` 来对组件的属性类型进行验证，并确保名称、年龄、城市和国家被传递时是必需的。

```jsx
Person.propTypes = {
  name: PropTypes.string.isRequired,
  age: PropTypes.number.isRequired,
  city: PropTypes.string.isRequired,
  country: PropTypes.string.isRequired
};

export default Person;
```

希望这能帮助您更好地理解该组件的功能及其语法用法。

重构后：
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
这段优美代码质量好的原因如下：

<mark style="background: #FF5582A6;">- 使用了函数组件替代了类组件，使得代码更加简洁</mark>
- 函数组件可以更加方便地使用React hooks实现复用
- 使用了更短的语法来注明propTypes属性

3. 示例三：使用 JavaScript 数组方法实现filter、map和reduce

<mark style="background: #FFF3A3A6;">JavaScript 的 map, filter 和 reduce 方法提供了一种非常优雅的方法来处理介绍到的数组。</mark> 
	
重构前:
```javascript
function getFullNames(people) {
  const fullNames = [];

  for (let i = 0; i < people.length; i++) {
    const person = people[i];
    if (person.age >= 18) {
      const fullName = `${person.firstName} ${person.lastName}`;
      fullNames.push(fullName);
    }
  }

  return fullNames;
}
```

重构后:
```javascript
function getFullNames(people) {
  return people
    .filter(person => person.age >= 18)
    .map(person => `${person.firstName} ${person.lastName}`);
}
```
这段优美代码质量好的原因如下：

- 使用了更短的、易读的语法以实现同样的功能
- <mark style="background: #FF5582A6;">避免了使用显式循环，从而减少了代码行数</mark>
- 利用了 JavaScript 数组方法中 map, reduce 和 filter 的强大能力



**示例1：JavaScript**

假设我们需要从一个对象数组中获取每个对象的某个属性并生成一个新数组。

不优美的代码：

```javascript
const objs = [
  { name: 'Tom', age: 25 },
  { name: 'Jerry', age: 22 },
  { name: 'Spike', age: 30 }
];

// 创建一个新数组，用于存储对象的名称
const names = [];

// 遍历对象数组，将每个对象的名称添加到names数组中
for (let i = 0; i < objs.length; i++) {
  names.push(objs[i].name);
}

console.log(names); // 输出: ["Tom", "Jerry", "Spike"]
```

优美的代码：

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

**示例2：React**

在这个示例中，我们有一个简单的列表组件，可以接受一个项目数组并显示它们。

不优美的代码：

```jsx
import React from 'react';

class List extends React.Component {
  constructor(props) {
    super(props);
    // 定义组件状态 state 并初始化数据为 props.items
    this.state = {
      items: props.items
    };
  }

  render() {
    return (
      // 返回一个无序列表元素 <ul>，内部渲染 items 属性中的所有数据，使用 map 方法创建多个列表项 li
      <ul>
        {this.state.items.map((item, index) => (
          <li key={index}>{item}</li>
        ))}
      </ul>
    );
  }
}

```

整个组件由一个类定义，并继承自 React.Component，实现了一个名为 List 的类组件。在构造函数中，通过调用 super(props)，表示将 `props` 参数传递给父组件，确保继承自 `React.Component` 类的初始化代码可以正确地运行。初始化时将组件的状态 `state` 设置为带有初始数据的 `props.items`。在 `render()` 方法中，通过 JSX 语法返回一个无序列表 `<ul>` 元素，使用 `map()` 方法将所有的 `items` 数组元素映射成多个列表项 `<li>`，并分配一个唯一的键 `key`。所以最后生成的页面元素是一个无序列表，其包含若干个列表项，每个列表项上都展示了一个文本值，并显示了对应的索引号。


优美的代码：

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



## 示例 1 - 重构前

```javascript
// 统计某个数组内数字出现的频率
function arrNumFreq(arr) {
  const obj = {};
  for (let i = 0; i < arr.length; i++) {
    if (obj[arr[i]]) {
      obj[arr[i]]++;
    } else {
      obj[arr[i]] = 1;
    }
  }
  return obj;
}
```

## 示例 1 - 重构后

```javascript
// 统计某个数组内数字出现的频率
function arrNumFreq(arr) {
  return arr.reduce((acc, cur) => {
    acc[cur] = (acc[cur] || 0) + 1;
    return acc;
  }, {});
}
```

**注释:**

重构后的代码使用`reduce()`方法来遍历数组，并根据每个元素的值计算出它们出现的次数。由于reduce会创建一个累加器（`acc`），因此我们可以在其中存储出现次数。通过使用`|| 0`将项初始化为0，即使尚未处理过的项也可以在奇遇下递增。最后返回所需的统计信息。



## 示例 2 - 重构前

```jsx
import React from 'react';

class Example extends React.Component {
  constructor(props) {
    // 构造函数 super(props) 表示将 props 传递到了父组件
    super(props);
    // 初始化组件状态 state 包含值为 '' 的 value 属性
    this.state = {
      value: ''
    };
    // 重新绑定 handleChange 方法中的 this，确保正确地操作 state 和 props
    this.handleChange = this.handleChange.bind(this);
  }

  handleChange(e) {
    // 处理输入框的变化事件
    // 调用 this.setState() 方法更新状态，并提供一个新参数对象来更新 state 对象
    // 新的 value 值为 e.target.value，即用户输入的新值
    this.setState({
      value: e.target.value
    });
  }

  render() {
    return (
      // 返回一个包含输入框和当前值的 <div> 元素
      <div>
        <label>
          输入:
          <input 
            type="text" 
            // 将输入框的值设置为当前状态的 value 属性值
            value={this.state.value} 
            // 当输入框内容变化时触发 handleChange 方法
            onChange={this.handleChange} 
          />
        </label>
        // 显示当前的 value 值
        <p>{this.state.value}</p>
      </div>
    );
  }
}

```

## 示例 2 - 重构后

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

**注释:**

React Hooks现在是创建简单的类似状态功能组件的推荐方式，它可以使代码更加优雅。这里我们使用`useState()` hook来存储组件中的值，并且不再需要构造函数和`setState()`方法了。 函数式组件的另一个好处就是它们更容易测试，因为它们是纯函数并且没有任何旁效作用。

注意：为了使用Hooks，你需要确保你的React版本大于16.8.0.




### 示例 1：

重构前：

```javascript
// 如果 x 不为 0，返回 y / x，否则返回 undefined
if (x != 0) {
  return y / x;
} else {
  return undefined;
}
```

重构后：

```javascript
// 如果 x 不为 0，返回 y / x，否则返回 undefined
return x !== 0 ? y / x : undefined;
```

注释：使用了条件运算符（ternary operator）来简化 if/else 语句。

### 示例 2：

重构前：

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

注释：使用 `async/await` 简化了原本繁琐的 Promise 链式调用。

### 示例 3：

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

### 示例 4：

重构前：

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

### 示例 5：

重构前：

```js
function Comment(props) {
  return (
    <div className="comment">
      <h2 className="author">{props.author}</h2>
      <p className="body">{props.body}</p>
      <div className="actions">
        <a href="#" onClick={props.onEdit}>Edit</a>
        <span> | </span>
        <a href="#" onClick={props.onDelete}>Delete</a>
      </div>
    </div>
  );
}
```

重构后：

```js
function Comment({ author, body, onEdit, onDelete }) {
  return (
    <div className="comment">
      <h2 className="author">{author}</h2>
      <p className="body">{body}</p>
      <div className="actions">
        <a href="#" onClick={onEdit}>Edit</a>
        <span> | </span>
        <a href="#" onClick={onDelete}>Delete</a>
      </div>
    </div>
  );
}
```

注释：使用解构来取代 props 的属性访问，减少了复杂度和代码量。

以下是更多精妙优雅的 JavaScript 和 React 代码示例（附有注释）：

### 示例 1：

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

注释：使用 `reduce()` 和解构来查找最小值。

[[JS基础#Array.sort()方法]]

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

### 示例 3：

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

希望这可以为您提供更多启示并且使您在编写 JavaScript 和 React 代码时具有良好的风格。