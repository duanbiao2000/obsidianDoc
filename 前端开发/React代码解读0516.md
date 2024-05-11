### 代码1:

```javascript
const each = function each(obj, callback) {
    if (obj === null || typeof obj !== "object") throw new TypeError('obj is not a object');
    if (typeof callback !== "function") throw new TypeError('callback is not a function');
    let keys = Reflect.ownKeys(obj);
    keys.forEach(key => {
        let value = obj[key];
        // 每一次迭代，都把回调函数执行
        callback(value, key);
    });
};

/* createElement:创建虚拟DOM对象 */
export function createElement(ele, props, ...children) {
    let virtualDOM = {
        $$typeof: Symbol('react.element'),
        key: null,
        ref: null,
        type: null,
        props: {}
    };
    let len = children.length;
    virtualDOM.type = ele;
    if (props !== null) {
        virtualDOM.props = {
            ...props
        };
    }
    if (len === 1) virtualDOM.props.children = children[0];
    if (len > 1) virtualDOM.props.children = children;
    return virtualDOM;
};

/* render:把虚拟DOM变为真实DOM */
export function render(virtualDOM, container) {
    let { type, props } = virtualDOM;
    if (typeof type === "string") {
        // 存储的是标签名:动态创建这样一个标签
        let ele = document.createElement(type);
        // 为标签设置相关的属性 & 子节点
        each(props, (value, key) => {
            // className的处理：value存储的是样式类名
            if (key === 'className') {
                ele.className = value;
                return;
            }
            // style的处理：value存储的是样式对象
            if (key === 'style') {
                each(value, (val, attr) => {
                    ele.style[attr] = val;
                });
                return;
            }
            // 子节点的处理：value存储的children属性值
            if (key === 'children') {
                let children = value;
                if (!Array.isArray(children)) children = [children];
                children.forEach(child => {
                    // 子节点是文本节点：直接插入即可
                    if (/^(string|number)$/.test(typeof child)) {
                        ele.appendChild(document.createTextNode(child));
                        return;
                    }
                    // 子节点又是一个virtualDOM：递归处理
                    render(child, ele);
                });
                return;
            }
            ele.setAttribute(key, value);
        });
        // 把新增的标签，增加到指定容器中
        container.appendChild(ele);
    }
};
```



#### 代码解读2:



1. `each` 函数：遍历对象并执行回调函数。
```javascript
const each = function each(obj, callback) {
    // 判断传入的obj是否为object类型
    if (obj === null || typeof obj !== "object") throw new TypeError('obj is not a object');
    // 判断callback是否为function类型
    if (typeof callback !== "function") throw new TypeError('callback is not a function');
    // 获取变量所有键名
    let keys = Reflect.ownKeys(obj);
    // 循环变量所有键名
    keys.forEach(key => {
        let value = obj[key];
        // 每一次迭代，都把回调函数执行
        callback(value, key);
    });
};
```

2. `createElement` 函数：创建虚拟 DOM 对象。

好的，以下是从头开始重新逐行注释后的代码：

```javascript
export function createElement(ele, props, ...children) {
    // 定义一个初始值为空对象virtualDOM
    let virtualDOM = {
        // 存储虚拟DOM的类型
        $$
```



在这份代码中，我们首先定义了一个叫做 `createElement` 的函数，用于创建虚拟 DOM 对象。逐行注释如下：

1. `export function createElement(ele, props, ...children)` : 这是一个用于创建虚拟 DOM 对象的函数。它接收三个输入参数，分别是元素类型 `ele`、属性对象 `props` 和子节点 `children` ，使用了 ES6 中的 Rest Parameters 语法使得我们可以接收不定量的子节点。

2. `let virtualDOM = { ... }` : 创建一个初始值为空的虚拟 DOM 对象 `virtualDOM`，里面包含以下成员：

- `$$typeof` : 存储虚拟 DOM 的类型

 > `$$typeof` 中的两个 `$` 符号并不是有特殊含义的字符，它们只是一个普通的 JavaScript 变量名中的字符。
  >
  > 在 React 内部，采用从 Symbol 中读取一个唯一标识符（Symbol.for('react.element')）放到 `$$typeof` 这个变量中。由于 Symbol 是一种唯一性、不可变性很强的基本类型，因此保证可以区分开来几乎所有的值，并且自然保护了 `$$typeof` 的不可变性和唯一性等特点。
  >
  > 所以，`$$typeof` 中的两个 `$` 符号只是一种命名规范，表示这是一个需要注意的变量，在命名时避免与其他变量重名。双美元符号也常用来表示某个属性或方法已经是框架级的内部实现细节，应该尽量避免和外部代码混淆使用，以免破坏整个系统的稳定性。

- `key` : 存储每个元素自己所声明的 key 属性

- `ref` : 存储每个元素自己所声明的 ref 属性

- `type` : 存储要创建的标签类型名 (div、button 等)

- `props` : 存储其他属性和子节点信息

3. `let len = children.length` : 获取子节点的长度。

4. `virtualDOM.type = ele` : 将传入 `createElement` 函数的 `ele` 参数（即要创建的标签类型）存储到 virtualDom 对象的 type 属性中。

5. `if (props !== null) { virtualDOM.props = { ...props } }` : 如果 `props` 不为null，则将其赋值给 `virtualDom.props`。这里使用了 JavaScript 的展开语法来实现浅层克隆对象。

6. `if (len === 1) {...} else (if len > 1) {...}` : 如果只有一个子节点，则直接赋值；否则按顺序存储到 `virtualDom.props.children` 数组中。

7. `return virtualDOM` : 将刚创建的虚拟 DOM 对象作为函数结果返回。

3. `render` 函数：把虚拟 DOM 变为真实 DOM。

好的，以下是逐行注释后的代码：



```javascript
export function render(virtualDOM, container) {
    // 将 virtualDOM 中的 type 和 props 解构出来
    let { type, props } = virtualDOM;

    if (typeof type === "string") {
        // 如果 type 是字符串，则创建一个元素节点，标签名为 type
        let ele = document.createElement(type);

        // 遍历 props 对象
        each(props, (value, key) => {
            // 如果 key 为 className，设置该节点的 class 属性，并返回
            if (key === 'className') {
                ele.className = value;
                return;
            }
            // 如果 key 为 style，设置该节点的样式属性，并返回
            if (key === 'style') {
                each(value, (val, attr) => {
                    ele.style[attr] = val;
                });
                return;
            }
            // 如果 key 为 children，遍历它并递归渲染子节点
            if (key === 'children') {
                let children = value;
                if (!Array.isArray(children)) {
                    children = [children];
                }

                children.forEach(child => {
                    if (/^(string|number)$/.test(typeof child)) {
                        // 如果子节点只是文本，则创建文本节点并添加到父节点下
                        ele.appendChild(document.createTextNode(child));
                        return;
                    }
                    // 如果子节点是虚拟 DOM 对象，则递归渲染该子节点
                    render(child, ele);
                });

                return;
            }
            // 如果其他属性，则将其设置为该节点的属性
            ele.setAttribute(key, value);
        });

        // 最后，将新创建的节点插入到 container 中
        container.appendChild(ele);
    }
};
```

在这份代码中，我们定义了一个名为 `render` 的函数，它用于将虚拟 DOM 转换成真实的 DOM 并插入到 container 中。

逐行注释如下：

1. `export function render(virtualDOM, container)` : 定义一个名为 `render` 的函数，它接收两个参数：虚拟 DOM 对象 `virtualDOM` 和目标容器 `container`，并没有直接返回值，而是通过调整 container 树来间接完成渲染的操作。

2. `let { type, props } = virtualDOM;` : 使用对象解构来获取 `virtualDOM` 对象中的 `type` 和 `props` 属性，便于后面进行操作。

3. `if (typeof type === "string") {...}` : 判断传入的元素类型是否为字符串，如果是，则新建一个对应标签名的元素节点。

4. `each(props, (value, key) => {...})` : 遍历传入的 props 对象，并调用 each 函数处理不同的情况。该函数存在于具体项目中，应该是根据传入的参数针对key-value列表进行遍历操作。

5. 如果当前遍历到的键为 `className`，则将其值设置为元素节点的类名；

6. 如果当前遍历到的键为 `style`，则将其值作为样式对象并迭代修改元素节点的样式属性；

7. 如果当前遍历到的键为 `children`，则将其值设置为子元素并遍历该列表中的每个子节点，针对文本类型和虚拟DOM类型分别进行不同的处理：

- 如果子元素是文本，则将其创建为文本节点并添加到父节点下；
- 如果子元素是虚拟 DOM，则递归调用 `render()` 函数并将子节点加入到父节点。

8. 如果当前遍历到的键名称为其他名称，则将该属性以 key-value 的形式设置给新建的元素节点。

9. 在上述所有操作执行完成后，将新建的元素节点插入到指定的容器节点中。

总体来说， `render()` 函数对应的是 React 中的 `ReactDOM.render()` 方法，是将虚拟 DOM 转化为浏览器可识别的 HTML 元素的关键所在。


#### 代码2:

这段代码涵盖了 React 应用程序中的一些核心概念，以下是逐行注释后的代码：

```jsx
import React from 'react'; // 引入 React 库
import ReactDOM from 'react-dom/client'; // 引入 ReactDOM 库中的客户端 API
import { createElement, render } from './jsxHandle'; // 引入自定义函数用于生成虚拟 DOM

const root = ReactDOM.createRoot(document.getElementById('root')); // 创建一个根节点对象并将其连接到 HTML 中指定的元素

let styObj = { // 创建一个样式对象
    color: 'red',
    fontSize: '16px'
};
let x = 10; // 定义变量x，并赋初始值10
let y = 20; // 定义变量y，并赋初始值20

// 在 Root 组件上调用render函数以渲染页面
/*
root.render(
    <div className='container'>
        <h2 className="title" style={styObj}>珠峰培训</h2>
        <div className="box">
            <span>{x}</span>
            <span>{y}</span>
        </div>
    </div>
);
*/

// 使用自定义的函数createElement生成虚拟DOM对象
let jsxObj = createElement(
    "div",
    { className: "container" },
    createElement(
        "h2", // 创建一个H2标签元素
        { className: "title", style: styObj }, // 将样式对象传递给H2标签元素
        "\u73E0\u5CF0\u57F9\u8BAD" // 将文本传递给H2标签元素
    ),
    createElement(
        "div",  // 创建一个DIV标签元素
        { className: "box" }, // 给DIV元素添加class
        createElement("span", null, x), // 创建一个SPAN标签元素，将x的值传递给该标签元素
        createElement("span", null, y) // 创建一个SPAN标签元素，将y的值传递给该标签元素
    )
);

// 调用自定义处理函数render，将虚拟DOM对象转换成真实DOM对象，并插入到HTML中指定的元素节点中
render(jsxObj, document.getElementById('root'));
```

这段代码示例中，采用了两种方法，一种是使用 JSX 语法创建虚拟 DOM 对象，并调用 React 提供的 `render()` 函数将其渲染到页面上；另一种方式是手写 React 中 `createElement()` 函数模拟 JSX 的实现方式，巧妙利用 JavaScript 的函数特性完成同样的目标。

在本示例中，最核心的函数是 `render()`，它用于将虚拟 DOM 对象转换为真实 DOM 元素并插入到指定位置上，帮助我们在页面上“渲染”React应用程序。

#### 概念: 单双闭合调用

双闭合调用和单闭合调用代表了 jsx 在 React 中的不同的语法形式，两种写法本质上是相同的，都可以表达同一种意思。

以之前提供的代码为例：

双闭合调用方式：

```jsx
root.render(
    <div className='container'>
        <h2 className="title" style={styObj}>珠峰培训</h2>
        <div className="box">
            <span>{x}</span>
            <span>{y}</span>
        </div>
    </div>
);
```

单闭合调用方式:

```jsx
root.render(
    React.createElement("div", {className:'container'},
        React.createElement("h2", {className:"title", style:styObj},"珠峰培训"),
        React.createElement("div", {className:"box"},
            React.createElement("span", null, x),
            React.createElement("span", null,y)
        )
    )
);
```

在双闭合调用中，我们直接使用 JSX 语法书写，从而更加清晰易读。但是它需要通过 Babel 转译器进行转换，因此会增加一定的开销。

在单闭合调用中，我们并未使用 JSX 语法，而是手动构造了元素对象，所以它的开销相对较小。

### 代码2:



```jsx
import PropTypes from 'prop-types'; // 引入PropTypes库，用于设置属性的数据类型规则
import React from 'react'; // 引入React库

const DemoOne = function DemoOne(props) { // 定义名为DemoOne的函数组件（也可以使用箭头函数定义）
    let { title, x, children } = props; // 使用解构赋值获取props中对应的参数
    // 下面语句块通过使用React.Children 对象中提供的相关方法，对children进行了处理，以处理出各种情况下的子元素并以数组方式统一处理
    /* 要对children的类型做处理
     * 可以基于 React.Children 对象中提供的方法，对props.children做处理：count\forEach\map\toArray...
     * 好处：在这些方法的内部，已经对children的各种形式做了处理 */
    children = React.Children.toArray(children);
    let headerSlot = [], // 头插槽数组
        footerSlot = [], // 尾插槽数组
        defaultSlot = []; // 默认插槽数组
    children.forEach(child => {
        // 传递进来的插槽信息，都是编译为virtualDOM后传递进来的「而不是传递的标签」
        let { slot } = child.props; // 获取每个子元素的slot属性
        if (slot === 'header') { // 判断当前child的slot值是否是header类型
            headerSlot.push(child); // 如果是header则加入头插槽数组
        } else if (slot === 'footer') { // 判断当前child的slot值是否是footer类型
            footerSlot.push(child); // 如果是footer则加入尾插槽数组
        } else {
            defaultSlot.push(child); // 否则加入默认插槽数组
        }
    });

    // 最终将处理好的子组件展示在页面上（headerSlot、defaultSlot和footerSlot)
    return <div className="demo-box">
        {headerSlot}
        <br />

        <h2 className="title">{title}</h2>
        <span>{x}</span>

        <br />
        {footerSlot}
    </div>;
};
/* 设置属性的校验规则 */
DemoOne.defaultProps = {
    x: 0 // 将参数x的默认值设置为0
};
DemoOne.propTypes = {
    title: PropTypes.string.isRequired, // 定义props中 title 必填且必须为字符串类型
    x: PropTypes.number // 定义props中 x 属性需为数字类型，但不是必需的
};

export default DemoOne; // 导出 DemoOne 组件
```

### 代码3:

这段 TypeScript 代码定义了一个名为 `handlerMenu` 的事件处理函数。它的作用是当用户单击菜单时，获取当前菜单项的路径和所在的子菜单展开情况，并通过 URL 导航、sessionStorage 存储等方式更新应用程序状态和界面显示。

具体来说，该函数的实现步骤如下：

1. `const keyPath = e.keyPath`：将参数 `e` 的 `keyPath` 属性值赋给名为 `keyPath` 的常量，表示用户选择的菜单项路径。
2. `const copyKeyPath = JSON.parse(JSON.stringify(keyPath))`：使用 JSON 序列化和反序列化方法，复制 `keyPath` 常量数组中的元素并保存在名为 `copyKeyPath` 的常量中。
3. `console.log(copyKeyPath.slice(1))`：将 `copyKeyPath` 常量剪切掉第一个元素（即菜单的根路径），然后将其输出到控制台。
4. `setopenKeys(copyKeyPath.slice(1))`：调用父组件传递进来的 `MenuProps` 接口中包含的 `setopenKeys()` 函数，将 `keyPath` 数组去除第一个元素后的部分作为参数传入。这样就设置了当前展开的所有子菜单项。
5. `const router = keyPath.reverse().join("/")`：使用数组 `reverse()` 反转原来的 `keyPath` 常量数组，然后拼接成字符串，并将结果保存在 `router` 常量中。这个过程的目的是为了获得当前菜单项的路由地址。
6. `navigate('/' + router)`：调用 `navigate()` 函数，将指定的 URL 路径 `/` 和 `router` 变量（即当前选中的菜单项路径）连接起来构成完整的 URL 地址。然后进行页面导航，使其跳转到新页面并更新路由地址。
7. `sessionStorage.setItem('setSelectKeys',e.key)`：存储当前选中的菜单项路径到 `sessionStorage` 中，便于在页面刷新或重新加载时仍能保持状态。这里使用键 `"setSelectKeys"` 来存储值 `e.key`。
8. `setSelectKeys(e.key)`：调用父组件传递进来的 `MenuProps` 接口中包含的 `setSelectKeys()` 函数，将当前选中的菜单项路径作为参数传入。这样就标记了菜单中被用户所选中的选项。



### 代码4:

```js
import Menu from "./Menu";

function aside() {
  // 声明路由状态变量和更新方法
  const [router, setRouter] = useState(router_item);

  // 声明选择的菜单项状态变量和更新方法
  const [selectKeys, setSelectKeys] = useState<string>(
    sessionStorage.getItem("setSelectKeys")
  );

  // 声明展开的菜单项状态变量和更新方法
  const [openKeys, setOpenKeys] = useState(
    JSON.parse(sessionStorage.getItem("setopenkeys"))
  );

  // 声明点击菜单时的事件处理函数
  const handlerMenu: IMenuProps["onClick"] = (e) => {
    // 获取用户点击的菜单项路径
    const keyPath = e.keyPath;
// 更新展开的菜单项状态
setOpenKeys(keyPath.slice(1));

// 将菜单路径拼接成完整路由
const router = keyPath.reverse().join("/");

// 进行页面导航
navigate("/" + router);

// 将所选中的菜单项路径存储到 sessionStorage 中
sessionStorage.setItem("setSelectKeys", e.key);

// 更新当前选择的菜单项状态
setSelectKeys(e.key);
  };

  return (
    <div>
      {/* 渲染侧边栏菜单 */}
      <Menu onClick={handlerMenu} selectedKeys={[selectKeys]} openKeys={openKeys} />
    </div>
  );
}

export default aside;
```






### 代码10:

以下是一个比上面的示例复杂1.5倍的，几乎涵盖了 React 中的所有概念的代码示例：

```js
import React, { useState, useEffect, useMemo, useCallback } from 'react';

const App = () => {
  const [count, setCount] = useState(0);
  const [message, setMessage] = useState('');

  const handleClick = useCallback(() => {
    setCount(count + 1);
  }, [count]);

  useEffect(() => {
    if (count > 5) {
      setMessage('Count is greater than 5.');
    } else {
      setMessage('');
    }
  }, [count]);

  const doubledCount = useMemo(() => count * 2, [count]);

  return (
    <div>
      <h1>Hello, world!</h1>
      <p>You clicked {count} times. {message}</p>
      <p>Doubled count: {doubledCount}</p>
      <button onClick={handleClick}>Click me</button>
    </div>
  );
};

export default App;
```

这个应用程序包含了一些重要的 React 概念，并且在前面的示例中没有完全涉及到。

首先我们使用 `useState` 钩子来添加两个状态变量 `count` 和 `message`，并声明修改该状态的两个函数 `setCount` 和 `setMessage`。然后，在点击"Click me"按钮时，我们会调用 `handleClick` 函数来更新 `count` 状态变量。

针对副作用，我们使用 `useEffect` 钩子来监听 `count` 变量的变化。当 `count` 的值大于 5 时，我们将消息字符串 `message` 设置为 "Count is greater than 5."，否则清空消息字符串。

对于性能优化方面，我们使用 `useMemo` 钩子来缓存计算结果。在本例中，我们将 `count` 的值乘以 2，并将结果存储在 `doubledCount` 变量中。

最后，使用 `useCallback` 钩子来创建 `handleClick` 函数的 memoized 版本，以避免在每次重新渲染组件时重新定义该函数。

在上述示例中，我们涵盖了 React 中的 Hooks、状态管理、副作用、问题处理和性能优化等的主要概念。

```jsx
import React, { useState, useEffect, useMemo, useCallback } from 'react';

const App = () => {
  const [count, setCount] = useState(0); // 使用 useState 钩子声明 count 状态变量和修改状态的函数 setCount。
  const [message, setMessage] = useState(''); // 定义 message 状态变量及其修改函数。

  const handleClick = useCallback(() => { // 定义一个 memoized 回调函数 handleClick，在 count 变量更新时被调用。
    setCount(count + 1); // 更新 count 状态变量的值。
  }, [count]); // 当 count 依赖发生变化时，重新定义这个回调。

  useEffect(() => { // 使用 useEffect 钩子来管理 componentDidMount 和 componentDidUpdate 周期的处理逻辑。
    if (count > 5) {
      setMessage('Count is greater than 5.'); // 如果 count 的值大于 5，则设置消息字符串变量为 "Count is greater than 5."
    } else {
      setMessage(''); // 否则，清空消息字符串变量。
    }
  }, [count]); // 当 count 发生变化时，重新渲染。

  const doubledCount = useMemo(() => count * 2, [count]); // 定义 memoized 计算结果，并将起始值设置为 count 的两倍。

  return (
    <div>
      <h1>Hello, world!</h1>
      <p>You clicked {count} times. {message}</p> // 在页面渲染中展示 count 和 message 的值。
      <p>Doubled count: {doubledCount}</p> // 展示计算结果的内容。
      <button onClick={handleClick}>Click me</button> // 为新增事件监听器并将其绑定在 handleClick 上，当点击按钮时，会更新 count 的值。
    </div>
  );
};

export default App; // 导出组件以供其他文件使用。
```

上述代码示例中使用了 React 中的一些重要概念和 API：

- `useState`：用来声明和修改状态变量。
- `useEffect`：用来管理组件的副作用，在组件的生命周期（挂载、更新、卸载）发生变化时执行相应的操作。
- `useMemo`：用来缓存计算结果，避免无必要的重新计算。
- `useCallback`：用来创建 memoized 版本的回调函数，优化性能。

通过定义状态变量、事件处理函数，渲染视图等，逐行分析该例子使得我们更深入地理解 React 框架的使用。



### 代码11:

```js

function ProductCategoryRow({ category }) {
  return (
    <tr>
      <th colSpan="2">{category}</th>
    </tr>
  );
}

function ProductRow({ product }) {
  const name = product.stocked ? (
    product.name
  ) : (
    <span style={{ color: "red" }}>{product.name}</span>
  );

  return (
    <tr>
      <td>{name}</td>
      <td>{product.price}</td>
    </tr>
  );
}

function ProductTable({ products }) {
  const rows = [];
  let lastCategory = null;

  products.forEach((product) => {
    if (product.category !== lastCategory) {
      rows.push(
        <ProductCategoryRow
          category={product.category}
          key={product.category}
        />
      );
    }
    rows.push(<ProductRow product={product} key={product.name} />);
    lastCategory = product.category;
  });

  return (
    <table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Price</th>
        </tr>
      </thead>
      <tbody>{rows}</tbody>
    </table>
  );
}

function SearchBar() {
  return (
    <form>
      <input type="text" placeholder="Search..." />
      <label>
        <input type="checkbox" /> Only show products in stock
      </label>
    </form>
  );
}

function FilterableProductTable({ products }) {
  return (
    <div>
      <SearchBar />
      <ProductTable products={products} />
    </div>
  );
}

const PRODUCTS = [
  { category: "Fruits", price: "$1", stocked: true, name: "Apple" },
  { category: "Fruits", price: "$1", stocked: true, name: "Dragonfruit" },
  { category: "Fruits", price: "$2", stocked: false, name: "Passionfruit" },
  { category: "Vegetables", price: "$2", stocked: true, name: "Spinach" },
  { category: "Vegetables", price: "$4", stocked: false, name: "Pumpkin" },
  { category: "Vegetables", price: "$1", stocked: true, name: "Peas" }
];

export default function App() {
  return <FilterableProductTable products={PRODUCTS} />;
}

```

这是一个React组件，显示了一个可筛选的产品列表。 用户可以输入搜索词并选择只显示现有库存的产品。 它由以下四个组件组成： 

1. SearchBar：显示一个文本框和一个复选框，用户可以在文本框中输入搜索参数，并使用复选框过滤掉已下架商品。

2. ProductTable: 显示整个产品列表，每个商品被呈现为一个行。 行都分为两列，以显示商品名称和价格。

3. ProductCategoryRow: 显示一行，用于显示产品类别名称。

4. ProductRow: 商品列表中的一个单独商品行，它包含该商品的基本信息，如名称和价格。

此代码还定义了一个PRODUCTS常量数组，包含我们要显示的示例产品。 最后，FilterableProductTable是组件树的顶层组件，将SearchBar和ProductTable组合在一起。

当然可以，以下是代码的 Typescript 版本：

```typescript
import React from "react";

interface Product {
  category: string;
  price: string;
  stocked: boolean;
  name: string;
}

interface Props {
  products: Product[];
}

function ProductCategoryRow({ category }: { category: string }) {
  return (
    <tr>
      <th colSpan={2}>{category}</th>
    </tr>
  );
}

function ProductRow({ product }: { product: Product }) {
  const name = product.stocked ? (
    product.name
  ) : (
    <span style={{ color: "red" }}>{product.name}</span>
  );

  return (
    <tr>
      <td>{name}</td>
      <td>{product.price}</td>
    </tr>
  );
}

function ProductTable({ products }: Props) {
  const rows: JSX.Element[] = [];
  let lastCategory: string | null = null;

  products.forEach((product) => {
    if (product.category !== lastCategory) {
      rows.push(
        <ProductCategoryRow
          category={product.category}
          key={product.category}
        />
      );
    }
    rows.push(<ProductRow product={product} key={product.name} />);
    lastCategory = product.category;
  });

  return (
    <table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Price</th>
        </tr>
      </thead>
      <tbody>{rows}</tbody>
    </table>
  );
}

function SearchBar() {
  return (
    <form>
      <input type="text" placeholder="Search..." />
      <label>
        <input type="checkbox" /> Only show products in stock
      </label>
    </form>
  );
}

export default function FilterableProductTable({ products }: Props) {
  return (
    <div>
      <SearchBar />
      <ProductTable products={products} />
    </div>
  );
}

const PRODUCTS: Product[] = [
  { category: "Fruits", price: "$1", stocked: true, name: "Apple" },
  { category: "Fruits", price: "$1", stocked: true, name: "Dragonfruit" },
  { category: "Fruits", price: "$2", stocked: false, name: "Passionfruit" },
  { category: "Vegetables", price: "$2", stocked: true, name: "Spinach" },
  { category: "Vegetables", price: "$4", stocked: false, name: "Pumpkin" },
  { category: "Vegetables", price: "$1", stocked: true, name: "Peas" },
];
```

这里添加了一些 interfaces，它们代表了组件所需的 props 和商品对象类型。此外，我们还需要将函数组件的参数声明为接口，以便 Typescript 可以进行类型推断。

可以的，这里是使用 React Hook 重构后的代码：

```js
import React, { useState } from "react";

interface Product {
  category: string;
  price: string;
  stocked: boolean;
  name: string;
}

interface Props {
  products: Product[];
}

function ProductCategoryRow({ category }: { category: string }) {
  return (
    <tr>
      <th colSpan={2}>{category}</th>
    </tr>
  );
}

function ProductRow({ product }: { product: Product }) {
  const name = product.stocked ? (
    product.name
  ) : (
    <span style={{ color: "red" }}>{product.name}</span>
  );

  return (
    <tr>
      <td>{name}</td>
      <td>{product.price}</td>
    </tr>
  );
}

function ProductTable({ products }: Props) {
  const [searchValue, setSearchValue] = useState("");
  const [showInStockOnly, setShowInStockOnly] = useState(false);

  let lastCategory: string | null = null;

  const rows = products.reduce<JSX.Element[]>((acc, product) => {

    if (!product.name.toLowerCase().includes(searchValue.toLowerCase())) {
      return acc;
    }

    if (showInStockOnly && !product.stocked) {
      return acc;
    }

    if (product.category !== lastCategory) {
      acc.push(
        <ProductCategoryRow
          category={product.category}
          key={product.category}
        />
      );
    }

    acc.push(<ProductRow product={product} key={product.name} />);
    lastCategory = product.category;
    return acc;
  }, []);

  function handleSearchChange(event: React.ChangeEvent<HTMLInputElement>) {
    setSearchValue(event.target.value);
  }

  function handleCheckboxChange() {
    setShowInStockOnly(!showInStockOnly);
  }

  return (
    <table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Price</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td colSpan={2}>
            <input
              type="text"
              placeholder="Search..."
              value={searchValue}
              onChange={handleSearchChange}
            />
            <label>
              <input
                type="checkbox"
                checked={showInStockOnly}
                onChange={handleCheckboxChange}
              />{" "}
              Only show products in stock
            </label>
          </td>
        </tr>
        {rows}
      </tbody>
    </table>
  );
}

export default function FilterableProductTable({ products }: Props) {
  return <ProductTable products={products} />;
}

const PRODUCTS: Product[] = [
  { category: "Fruits", price: "$1", stocked: true, name: "Apple" },
  { category: "Fruits", price: "$1", stocked: true, name: "Dragonfruit" },
  { category: "Fruits", price: "$2", stocked: false, name: "Passionfruit" },
  { category: "Vegetables", price: "$2", stocked: true, name: "Spinach" },
  { category: "Vegetables", price: "$4", stocked: false, name: "Pumpkin" },
  { category: "Vegetables", price: "$1", stocked: true, name: "Peas" },
];

```

这个版本将组件从类组件转换为函数组件，利用了 React Hook 来管理 state，包括搜索值和 “只显示在售商品” 复选框。同时我们也增加了一些相关的事件处理程序，用于更新页面状态。最终，ProductTable组件将始终呈现整个表格，因此FilterableProductTable不再需要，并且搜索和复选框状态管理的逻辑与ProductTable组件中实现。