---
aliases: null
theme: null
tags: null
---

- [[2. Areas/前端开发/React/API数据请求.md]]
- [[2. Areas/前端开发/React/API网关.md]]
- [[2. Areas/前端开发/React/API设计模式.md]]
- [[2. Areas/前端开发/React/Findlay - React - The Road To Enterprise.pdf.md]]
- [[2. Areas/前端开发/React/Flask开发部署.md]]
- [[2. Areas/前端开发/React/GitHub Actions.md]]
- [[2. Areas/前端开发/React/Github Gist JavaScript 的精彩代码片段.md]]
- [[2. Areas/前端开发/React/Lodash.md]]
- [[2. Areas/前端开发/React/Material-UI.md]]
- [[2. Areas/前端开发/React/MVC模型.md]]
- [[2. Areas/前端开发/React/React admin.md]]
- [[2. Areas/前端开发/React/React Bootstrap.md]]
- [[2. Areas/前端开发/React/React Hooks.md]]
- [[2. Areas/前端开发/React/React Quickly, Second Edition - MEAP... (Z-Library).pdf.md]]
- [[2. Areas/前端开发/React/react-bootstrap Components.md]]
- [[2. Areas/前端开发/React/react18通用后台管理系统.md]]
- [[2. Areas/前端开发/React/ReactRouter.md]]
- [[2. Areas/前端开发/React/React代码解读0608.md]]
- [[Redux]]
- [[2. Areas/前端开发/React/React关键技术.md]]
- [[2. Areas/前端开发/React/React官方文档.md]]
- [[2. Areas/前端开发/React/React实现无线滚动加载.md]]
- [[2. Areas/前端开发/React/React实现轮播图.md]]
- [[2. Areas/前端开发/React/React插件.md]]
- [[2. Areas/前端开发/React/React测试.md]]
- [[2. Areas/前端开发/React/React状态管理Redux.md]]
- [[2. Areas/前端开发/React/React生命周期方法.md]]
- [[2. Areas/前端开发/React/React组件间通信代码示例.md]]
- [[2. Areas/前端开发/React/React表单Forms.md]]
- [[2. Areas/前端开发/React/React设计模式与最佳实践.md]]
- [[2. Areas/前端开发/React/React软件架构.md]]
- [[2. Areas/前端开发/React/React进阶实战.md]]
- [[2. Areas/前端开发/React/Typesciprt扩展.md]]
- [[2. Areas/前端开发/React/两类Web应用.md]]
- [[2. Areas/前端开发/React/状态管理/学习Redux.md]]
- [[2. Areas/前端开发/React/新手React项目.md]]

### useEffect

```js
// 定义一个名为App的函数组件
function App(){
  // 定义一个常量，用于存储本地存储的键名
  LOCAL_STORAGE_KEY="contacts";
  // 使用useState钩子函数，初始化一个空数组，用于存储联系人信息
  const {contacts, setContacts} = useState([]);

  // 定义一个函数，用于添加联系人信息
  addContactHandler =(contact)=>{
    // 将新联系人信息添加到联系人数组中
    setContacts([...contacts, contact]);
  }

  // 使用useEffect钩子函数，在组件加载时，从本地存储中获取联系人信息，并将其添加到联系人数组中
  useEffect(()=>{
    const retrieveContacts = JSON.parse(localStorage.getItem(LOCAL_STORAGE_KEY));  
    if (retrieveContacts) setContacts(retrieveContacts);
  }, [contacts])
  
  // 使用useEffect钩子函数，在联系人数组发生变化时，将联系人信息保存到本地存储中
  useEffect(()=>{
    localStorage.setItem(LOCAL_STORAGE_KEY, JSON.strigify(contacts));  
  }, [contacts]);

  // 返回一个包含Header、AddContact和ContactList组件的div元素
  return (
    <div className="ui container">
      <Header />
        <AddContact addContactHandler={addContactHandler} />
        <ContactList contacts={contacts} />
    </div>
  );
}
// 导出App组件
export default App;
```

##### localStorage.setItem()

localStorage.setItem()方法用于将数据存储在本地浏览器的localStorage中。

- LOCAL_STORAGE_KEY 是用来标识该数据的键名。它应该是一个字符串。
- JSON.stringify 是将数据对象转换成JSON字符串。
- localStorage只能存储字符串类型的数据,所以需要将对象数据先转换成字符串,这里使用了JSON.stringify方法。

```js
// 数据对象
const data = {
  name: 'John',
  age: 30
};
// 将对象转换成JSON字符串
const stringified = JSON.stringify(data); 
// 设置本地存储
localStorage.setItem(LOCAL_STORAGE_KEY, stringified);
```

一些注意点:

- LOCAL_STORAGE_KEY需要事先定义,标识该数据
- 数据对象需要先通过JSON.stringify转换成字符串
- 设置本地存储时传入的应该是字符串,而不是对象

### uuidv4

`npm i uuidv4`

```js
import {uuid} from 'uuidv4';

...
  const addContactHandler =(contact)=>{
    setContacts([...contacts, {id:uuid(), ...contact}]);
  }
...
   const removeContactHandler=(id)=>{
     const newContactList = contacts.filter((contact)=>{
       return contact.id !== id;
     });
     setContacts(newContactList);

   };

... 
<ContactList contacts={contacts} getContactId={removeContactHandler}/>

```

![[assets/img/React关键技术/IMG-React关键技术-20240714124831256.png]]

### json server

json-server 是一款快速生成模拟 REST API 的工具。

主要特性:

- 只需提供一个 JSON 文件,就可以快速生成 RESTful API。

- 支持常见的 HTTP 动词,如 GET、POST、PUT、PATCH 和 DELETE。

- 内置了路由和数据层,可以方便地进行 CRUD 操作。

- 可以用来快速构建 Mock 服务或开发和测试前端应用。

```json
//db.json
{
  "contacts":[
  {
    "id":"c4be475a-ef49-47d2",
    "name":"Nikesh",
    "email":"Nicks@gmail.com"
  },
  {
    "id":"c4be325a-65f1-41s2",
    "name":"Max",
    "email":"dipe@gmail.com"
  ]
}
```

```json
"scripts":{
  "start": "json-server -p 3006 -w db.json"
}

```

%% - 使用 json-server 命令启动服务

- 监听端口为 3006
- 数据源文件为 db.json
- 当 db.json 文件修改后,服务会自动重新加载数据 %%

`fetch the data from the json server`

`npm i --save axios`

---

在React项目中，"views"文件夹通常用来存放高级组件或页面级组件，这些组件通常关联着一个特定的路由或页面。这些组件负责承担整个页面的结构和布局，并且通常会包含其他可复用的子组件。
以下是一些常见的组件类型，可以放置在"views"文件夹中：

1. 页面组件（Page Components）：这些组件对应着应用程序的不同页面或路由。它们负责处理路由参数、接收数据、调用API等。页面组件通常包含其他可复用的子组件，以构建页面的整体结构。
2. 容器组件（Container Components）：这些组件承担着与数据逻辑相关的任务，如数据获取、状态管理和数据处理等。它们将数据传递给展示组件，处理交互逻辑，并可能与Redux等状态管理库进行集成。
3. 高阶组件（Higher-Order Components）：这些组件是用来增强其他组件功能的组件。它们可以用于处理共享的逻辑、提供额外的功能或修改组件的行为，例如身份认证、访问控制等。

请注意，这只是一种常见的组织方式，并没有固定的规则，具体的项目结构可以根据团队的偏好和项目需求进行调整。
以下是一个示例项目结构，以展示"views"文件夹的典型用法：

```
/src
  /components
    /common
      Button.js
      ...
    /user
      UserCard.js
      ...
  /views
    Home.js
    About.js
    /user
      UserProfile.js
      UserSettings.js
  /services
    api.js
    ...
  /store
    actions.js
    reducers.js
    ...
  App.js
  index.js
```

在这个示例中，"views"文件夹用于存放不同页面的组件，而在"components"文件夹中存放可复用的子组件。同时还有"services"文件夹用于封装API请求，以及"store"文件夹用于Redux状态管理。

## 两种路由写法

在 React 16 和 React 18 时期，最常用的路由库是 React Router。下面是 React 16 和 React 18 时期的路由写法示例：
React Router v5 示例（适用于 React 16 和 React 18）：

```jsx
import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Home from './components/Home';
import About from './components/About';
import NotFound from './components/NotFound';
function App() {
  return (
    <Router>
      <Switch>
        <Route exact path="/" component={Home} />
        <Route path="/about" component={About} />
        <Route component={NotFound} />
      </Switch>
    </Router>
  );
}
export default App;
```

在上述示例中，我们使用了 `react-router-dom` 的 `BrowserRouter` 组件进行路由的包裹，`Route` 组件来定义路由规则，`Switch` 组件用于匹配第一个符合条件的路由。

React Router v6 示例（适用于 React 18）：

```jsx
import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Home from './components/Home';
import About from './components/About';
import NotFound from './components/NotFound';
function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
        <Route path="*" element={<NotFound />} />
      </Routes>
    </Router>
  );
}
export default App;
```

#### React Router v6 Tips

如果你想在 React Router v6 中使用 `<Route />` 组件将根路径（"/"）重定向到 "/home"，你可以使用 `<Navigate />` 组件作为 `element` 属性的值。下面是示例代码：

```jsx
import React from 'react';
import { BrowserRouter as Router, Route, Routes, Navigate } from 'react-router-dom';
function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Navigate to="/home" />} />
        <Route path="/home" element={<Home />} />
        {/* 其他的路由配置 */}
      </Routes>
    </Router>
  );
}
export default App;
```

在上述示例中，我们使用 `<Route />` 组件来定义路由规则。对于根路径（"/"），我们将 `element` 属性设置为 `<Navigate to="/home" />`，它会将页面重定向到 "/home" 路径。
请注意，在 React Router v6 中，我们使用了 `<Routes />` 组件来包裹所有的 `<Route />` 组件。这个组件是 React Router v6 中的新概念，用于定义整个应用的路由配置。
希望这个示例代码可以帮助你实现根路径重定向到 "/home" 的功能。如果还有其他问题，请随时提问。

### ??和||的区别在于

- ||是逻辑或运算符,用于判断值是否为false
- ??是空值合并运算符,用于判断值是否为null或undefined

具体区别:

1. 判断标准不同

||判断是否为false,||两边如果有一个值为true,则为true
??判断是否为null/undefined,??左边如果不是null/undefined,则返回该值
2. 返回值不同
||返回第一个true值,其他值忽略
??返回第一个非null/undefined值,其他值作为备选返回
3. 接受数据类型不同
||只接受布尔值,其他类型会自动转为布尔值
??可以判断所有数据类型是否为null/undefined
4. 使用场景不同
||一般用于逻辑判断
??一般用于默认值设置
例如:

```js
// || 返回第一个true值
a || b 
// ??返回第一个非null/undefined值  
a ?? b
```

所以总结:

- ||用于逻辑判断,||两边如果有一个true则为true
- ??用于设置默认值,??左边如果不是null/undefined则返回该值

二者都可以用来设置默认值,但??更适用于判断null/undefined情况。

从阅读官网文档的角度学习 React 生态链,我推荐的学习顺序和相关链接如下:

1. 学习 React 基础知识

- React 官网:<https://zh-hans.reactjs.org/docs/getting-started.html>
- 包含 React 基础语法、组件、props、状态等核心概念

2. 学习 React Hooks

- React Hooks 官网:<https://zh-hans.reactjs.org/docs/hooks-intro.html>
- 可以替代 class 组件的函数组件编程方式

3. 学习 React Router

- React Router 官网:<https://reactrouter.com/en/main>
- 在 React 应用中实现路由和导航的库

4. 学习 Redux

- Redux 官网:<https://redux.js.org/introduction/getting-started>
- 状态管理库,可以与 React 结合使用
  [[React状态管理Redux#Redux面试常见提问]]

5. 学习 React 测试

- 测试 React 应用:<https://zh-hans.reactjs.org/docs/testing.html>
- 常用的 React 测试工具和方法
  [[React测试#React测试面试常见提问]]

6. 学习 Next.js

- Next.js 官网:<https://nextjs.org/docs/getting-started>
- React 服务端渲染框架,可以加快应用加载速度
  [[../NextJS/Next.js]]

7. 学习 React Native

- React Native 官网:<https://reactnative.dev/docs/getting-started>
- 使用 React 开发原生移动应用的框架

## 在实际的 React 开发中，以下是一些常见的问题和讨论点

4. 如何处理异步操作？- 讨论使用回调函数、Promise、async/await 或使用第三方库（如 Redux-Saga、Redux-Thunk）来管理异步操作。
5. 如何处理表单的状态和验证？- 讨论使用本地状态管理来处理表单状态、使用第三方库（如 Formik、React Hook Form、Yup）来处理表单验证。
6. 如何优化渲染性能？- 讨论使用 React 的虚拟 DOM 和 diff 算法来最小化重新渲染的次数，以及使用控制台工具（如 React DevTools）来分析性能问题。
7. 如何处理组件的样式？- 讨论使用 CSS-in-JS 库（如 styled-components、Emotion）或 CSS 预处理器（如 Sass、Less）来处理组件样式。
8. 如何进行单元测试和集成测试？- 讨论使用测试框架（如 Jest、Enzyme）和测试工具来编写和运行组件的单元测试和集成测试。
9. 如何进行组件的复用和抽象？- 讨论使用高阶组件（HOC）、Render Props 模式、自定义 Hook 或组件库来实现组件的复用和抽象。

使用上下文（Context）进行跨层级组件通信：

```jsx
const MyContext = React.createContext();
function Parent() {
  return (
    <MyContext.Provider value="Hello World">
      <Child />
    </MyContext.Provider>
  );
}
function Child() {
  return (
    <MyContext.Consumer>
      {value => <p>{value}</p>}
    </MyContext.Consumer>
  );
}
```

使用全局状态管理库进行组件通信：

```jsx
import { useSelector, useDispatch } from 'react-redux';
import { increment } from './actions';
function Counter() {
  const count = useSelector(state => state.count);
  const dispatch = useDispatch();
  const handleIncrement = () => {
    dispatch(increment());
  };
  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={handleIncrement}>Increment</button>
    </div>
  );
}
```

4. 如何处理异步操作？

使用回调函数：

```jsx
class MyComponent extends React.Component {
  fetchData() {
    fetchDataFromAPI(result => {
      // 处理数据
    });
  }
  render() {
    return (
      <button onClick={() => this.fetchData()}>
        Fetch Data
      </button>
    );
  }
}
```

使用 Promise 和 async/await：

```jsx
class MyComponent extends React.Component {
  async fetchData() {
    const result = await fetchDataFromAPI();
    // 处理数据
  }
  render() {
    return (
      <button onClick={() => this.fetchData()}>
        Fetch Data
      </button>
    );
  }
}
```

使用第三方库（如 Redux-Saga、Redux-Thunk）来管理异步操作较为复杂，这里无法提供完整示例代码，但你可以查阅官方文档来了解更多信息。
5. 如何处理表单的状态和验证？
使用本地状态管理处理表单状态：

```jsx
function MyForm() {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  
  const handleSubmit = e => {
    e.preventDefault();
    // 处理表单提交逻辑
  };
  return (
    <form onSubmit={handleSubmit}>
      <input type="text" value={name} onChange={e => setName(e.target.value)} />
      <input type="email" value={email} onChange={e => setEmail(e.target.value)} />
      <button type="submit">Submit</button>
    </form>
  );
}
```

使用第三方库（如 Formik、React Hook Form、Yup）处理表单验证的示例超出了字符限制，你可以查阅这些库的官方文档来了解更多信息。
这些示例代码涵盖了 React 开发中的一些常见问题和解决方案，希望对你有所帮助。如果你有其他具体的问题，欢迎继续提问。

3. 如何处理组件的样式？

使用 CSS-in-JS 库（如 styled-components、Emotion）：

```jsx
import styled from 'styled-components';
const Button = styled.button`
  color: white;
  background-color: blue;
`;
function MyComponent() {
  return (
    <div>
      <Button>Click me</Button>
    </div>
  );
}
```

使用 CSS 预处理器（如 Sass、Less）：

```jsx
import './styles.scss';
function MyComponent() {
  return (
    <div>
      <button className="my-button">Click me</button>
    </div>
  );
}
```

4. 如何进行单元测试和集成测试？

使用 Jest 进行单元测试：

```jsx
import { render, screen } from '@testing-library/react';
import MyComponent from './MyComponent';
test('renders component correctly', () => {
  render(<MyComponent />);
  const textElement = screen.getByText(/Hello World/i);
  expect(textElement).toBeInTheDocument();
});
```

使用 Enzyme 进行集成测试：

```jsx
import { shallow } from 'enzyme';
import MyComponent from './MyComponent';
test('renders component correctly', () => {
  const wrapper = shallow(<MyComponent />);
  expect(wrapper.find('.my-component')).toHaveLength(1);
});
```

5. 如何进行组件的复用和抽象？

使用高阶组件（HOC）：

```jsx
function withLogger(Component) {
  return function WithLogger(props) {
    console.log('Component props:', props);
    return <Component {...props} />;
  };
}
const EnhancedComponent = withLogger(MyComponent);
```

使用 Render Props 模式：

```jsx
class MouseTracker extends React.Component {
  render() {
    return (
      <div onMouseMove={e => this.props.render(e)}>
        Track mouse position
      </div>
    );
  }
}
function App() {
  return (
    <div>
      <MouseTracker render={mousePosition => (
        <p>Mouse position: {mousePosition}</p>
      )} />
    </div>
  );
}
```

使用自定义 Hook：

```jsx
import { useState, useEffect } from 'react';
function useWindowWidth() {
  const [windowWidth, setWindowWidth] = useState(window.innerWidth);
  useEffect(() => {
    const handleResize = () => {
      setWindowWidth(window.innerWidth);
    };
    window.addEventListener('resize', handleResize);
    return () => {
      window.removeEventListener('resize', handleResize);
    };
  }, []);
  return windowWidth;
}
```

使用组件库（如 Material-UI、Ant Design）：

```jsx
import { Button } from 'antd';
function MyComponent() {
  return <Button>Click me</Button>;
}
```

以下是带副作用的函数的完整代码示例，并提供了一些测试用例：

1. 发送网络请求的函数：

```javascript
function fetchData(url, data) {
  return fetch(url, {
    method: 'POST',
    body: JSON.stringify(data),
    headers: {
      'Content-Type': 'application/json'
    }
  })
  .then(response => response.json())
  .catch(error => console.error(error));
}
// 测试用例
fetchData('https://api.example.com', { id: 1 })
  .then(response => console.log(response))
  .catch(error => console.error(error));
```

2. 文件读写函数：

```javascript
const fs = require('fs');
function writeFile(filePath, data) {
  fs.writeFile(filePath, data, err => {
    if (err) {
      console.error(err);
    } else {
      console.log('File written successfully.');
    }
  });
}
// 测试用例
writeFile('/path/to/file.txt', 'Hello, world!');
```

3. 修改全局变量的函数：

```javascript
let counter = 0;
function increment() {
  counter++;
}
// 测试用例
console.log(counter); // 输出: 0
increment();
console.log(counter); // 输出: 1
```

4. 执行数据库操作的函数：

```javascript
const mysql = require('mysql');
function insertDataIntoDatabase(data) {
  const connection = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: 'password',
    database: 'mydatabase'
  });
  connection.connect();
  const query = 'INSERT INTO users SET ?';
  connection.query(query, data, (error, results) => {
    if (error) {
      console.error(error);
    } else {
      console.log('Data inserted successfully.');
    }
  });
  connection.end();
}
// 测试用例
const data = { name: 'John', age: 30 };
insertDataIntoDatabase(data);
```

5. 执行副作用操作的函数：

```javascript
function showAlert(message) {
  alert(message);
}
// 测试用例
showAlert('Hello, world!');
```

这些完整的代码示例展示了带副作用的函数以及相应的测试用例。请注意，示例中使用了适当的库和依赖项来执行特定的操作，例如发送网络请求、文件操作、数据库连接等。

#### Ant Design

Ant Design中常用的组件、模板和工具如下：

1. 组件：Ant Design提供了丰富的UI组件，包括按钮、表格、表单、布局、菜单、弹窗、标签、图表等，用户可以根据项目需求自由选择使用。

2. 模板：Ant Design Pro是一个基于Ant Design框架开发的React后台管理系统模板，提供了常见的后台管理功能组件（用户管理、订单管理、数据分析等），可快速搭建后台管理系统。

3. 工具：Ant Design的工具包括antd-init、babel-plugin-import、webpack-config-antd等，可以在项目中快捷地使用Ant Design的组件、按需加载等特性。此外，Ant Motion是Ant Design的另一个重要工具，提供了丰富的动画效果，能够让Web应用更加生动有趣。

总之，Ant Design提供了完善的组件库、模板和工具，可以大大提高前端开发效率，使得开发人员可以更加专注于业务逻辑实现。

#### React Hook

React Hook是React16.8版本中新增的特性，用于解决类组件在复杂情况下（如状态共享、逻辑复用等）代码重复、难以维护等问题。React Hook提供了一些可复用的 React 逻辑，如useState、useEffect、useContext等，可以让函数式组件拥有类似于类组件的特性。

- useState(): 用来声明一个状态变量和setter方法，并且返回当前状态和修改状态值的方法。
- useEffect(): 相当于生命周期函数，可用于处理副作用效果（如异步请求、定时器等），在组件渲染后或者更新后执行
- useContext(): 用于获取一个 React 上下文 Context 的当前值，相当于类组件中this.context使用方式。

使用Hook后，我们不再需要编写类组件，并避免产生大量的繁琐代码，提高了代码的可读性和维护性。同时，使用Hook还可以更好地实现各个组件间的逻辑复用，使得开发更加方便和灵活。

#### Time Travel

在前端开发中，时间旅行（Time Travel）是一种调试技术，它允许开发人员回溯和查看应用程序在过去某个时间点的状态。

通常情况下，我们在浏览器控制台或调试器中进行调试时，只能够查看当前代码执行环境的状态。但是使用时间旅行技术，我们可以从过去的某个时间点开始重放应用程序的状态，就像回到过去一样，这样可以更好地理解代码的执行流程和状态变化。

在实现上，时间旅行通常与Redux等状态管理库结合使用。Redux允许将应用程序的状态保存在单一的存储中，并且提供了回溯和重放相关状态更新的API。借助Redux DevTools等工具，我们可以轻松地查看应用程序在不同时间点的状态以及状态之间的变化，从而更快速地识别并修复潜在的问题。

总的来说，时间旅行技术对于前端开发中的调试非常有用，特别是在涉及到复杂状态管理的场景下，它可以帮助开发人员更快速、更准确地检测和解决问题。

#### 组件间通信

在前端开发中，组件间的通信是非常重要的一个概念。在大型应用程序中，用户界面往往会被拆分为多个小组件，每个组件都有自己的状态和逻辑。这些组件之间需要互相协作、通信以实现复杂的功能。

下面列举一些常见的组件间通信方式：

1. props：父组件可以通过props属性向子组件传递数据，子组件可以通过props接收数据。这是React框架中最基础也最常见的组件间通信方式。

2. state lifting：如果两个或多个兄弟组件（没有直接父子关系）需要共享同一个状态，可以将该状态保存在它们公共的祖先组件的state中，并将其作为props从祖先组件传递到这些组件中。这样，当某个组件改变状态时，其他组件也会同时更新。

3.事件机制：可以在组件之间触发自定义事件来完成通信，这种机制常常使用在跨级别的组件通信上。我们对祖先组件添加一个自定义事件处理函数，在需要的地方使用$emit()触发事件，而监听该事件的组件则可以通过$on()方法注册相应的事件处理函数进行响应。

4.订阅/发布模式：是一种更加灵活的组件通信模式。其中一个组件作为消息发布者，另外一个或多个组件则可以订阅该消息，当消息发布者发送消息时，所有已经订阅该消息的组件都会收到通知，并进行相应的处理。

总的来说，在组件间通信中选择合适的方式非常关键，不同场景使用不同通信方式可以提高代码可维护性和开发效率。

### localStorage

localStorage是HTML5中新增的一种客户端存储方式,它可以让JavaScript通过键值对的形式将数据存储在浏览器中。localStorage的一些主要特点包括:

1. 数据存储在浏览器端,即使关闭浏览器,数据仍然存在。
2. 存储的数据没有过期时间,除非手动删除,否则永久保存。
3. 存储空间较大,Chrome一般为5MB左右。
4. API简单,常用的有setItem、getItem和removeItem。
5. 数据以键值对形式存储,键值均为字符串类型。
6. 存储的数据针对当前域名,不同域名间不能共享localStorage。
7. 支持事件通知存储内容的修改。
8. localStorage与sessionStorage的区别在于,localStorage数据会永久存储,sessionStorage数据只存在于当前会话。

总结:
localStorage提供了在浏览器端进行数据持久化存储的能力,是Web存储的重要方式之一。它的简单易用性让其在Web应用中广泛应用,如保存用户设置、缓存数据、状态管理等。需要注意它仅在当前域名内可访问。
好的,这里是一个使用localStorage的简单代码示例:

1. 保存数据:

```js
// 保存单个数据
localStorage.setItem('key', 'value'); 
// 保存多个数据
localStorage.setItem('testObject', JSON.stringify({a: 1, b: 2}));
```

2. 读取数据:

```js
let value = localStorage.getItem('key');
let obj = JSON.parse(localStorage.getItem('testObject'));
```

3. 删除数据:

```js
localStorage.removeItem('key');
```

4. 清空所有数据:

```js
localStorage.clear();
```

5. 监听storage事件:

```js
window.addEventListener('storage', event => {
  // 当存储数据变化时,会触发该事件
  console.log(event); 
});
```

这样,我们就可以通过这些简单的API对localStorage进行增删改查和监听,实现数据的持久化存储和同步。localStorage可以用来保存很多应用场景下的必要数据。

## 事件处理函数

### 事件处理函数的位置

在实际开发中，React组件中的时间处理函数可以根据具体情况放置在应用程序的不同位置。这取决于项目的规模、组件的复用性以及开发团队的偏好。以下是两种常见的做法及其优点：

1. 将时间处理函数集中放在应用程序的顶层组件（通常是App组件）中：
   - 优点：
     - 一致性：将所有时间处理函数集中放置在一个地方，可以提高代码的可读性和可维护性。开发人员可以更轻松地查找和修改这些函数。
     - 共享状态：如果多个组件需要访问相同的时间处理逻辑或共享状态，将这些函数放在顶层组件中可以更方便地共享这些逻辑和状态。
     - 性能优化：将时间处理函数放在顶层组件中可以避免在组件之间频繁传递回调函数，从而提高性能。

2. 将事件处理函数放在各自的组件中：
   - 优点：
     - 组件独立性：将时间处理函数放在各自的组件中可以使组件更加独立和可重用。这样，组件可以更容易地被其他项目或团队使用。
     - 可读性：将时间处理函数与其相关的组件放在一起，可以提高代码的可读性。开发人员可以更容易地理解组件的功能和行为。
     - 组件级别的状态：如果时间处理函数需要访问组件级别的状态，将其放在组件中可以更方便地访问和更新该状态。

需要注意的是，无论选择哪种方式，都应该遵循单一职责原则和组件化原则。确保时间处理函数的逻辑清晰、可测试，并且与组件的其他功能相互独立。此外，可以使用React的生命周期方法或React Hook来处理时间相关的逻辑，具体取决于你使用的React版本和项目的需求。

### 常见的事件处理函数

当涉及到React组件中最常用的事件处理函数时，以下是一个常见的示例代码段，其中包含了关键行注释：

```jsx
import React, { useState } from 'react';

const MyComponent = () => {
  const [count, setCount] = useState(0);

  // 处理点击事件的函数
  const handleClick = () => {
    setCount(count + 1); // 更新count状态
  };

  // 处理表单输入变化的函数
  const handleChange = (event) => {
    const inputValue = event.target.value;
    // 执行其他逻辑...
  };

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={handleClick}>Increase Count</button>
      <input type="text" onChange={handleChange} />
    </div>
  );
};

export default MyComponent;
```

在上述代码中，我们定义了两个常见的事件处理函数：

1. `handleClick`函数用于处理按钮的点击事件。当按钮被点击时，它会调用`setCount`函数来更新`count`状态的值。

2. `handleChange`函数用于处理输入框的变化事件。每当输入框的值发生变化时，它会被调用，并通过`event.target.value`获取输入框的当前值。

这个代码段展示了如何在React组件中使用事件处理函数来响应用户的交互。通过使用`onClick`和`onChange`属性，我们将事件处理函数与相应的DOM元素关联起来，以便在特定事件发生时执行相应的逻辑。

在React中，还有许多其他常用的事件处理函数可以用于处理不同类型的用户交互。以下是一些常见的事件处理函数：

1. `onSubmit`: 用于处理表单的提交事件。
2. `onKeyDown`, `onKeyPress`, `onKeyUp`: 用于处理键盘按键事件。
3. `onFocus`, `onBlur`: 用于处理元素获取焦点和失去焦点事件。
4. `onMouseEnter`, `onMouseLeave`: 用于处理鼠标进入和离开元素的事件。
5. `onMouseMove`, `onMouseDown`, `onMouseUp`, `onClick`: 用于处理鼠标在元素上移动、按下、释放和点击的事件。
6. `onScroll`: 用于处理滚动事件。
7. `onResize`: 用于处理窗口大小调整事件。
8. `onLoad`, `onError`: 用于处理图片或其他资源的加载和加载错误事件。
9. `onDragStart`, `onDrag`, `onDragEnd`: 用于处理拖拽操作的开始、进行中和结束事件。
10. `onTouchStart`, `onTouchMove`, `onTouchEnd`: 用于处理触摸设备上的触摸事件。

当涉及到React组件中的其他常见事件处理函数时，以下是一些示例代码和代码块注释：

```jsx
import React, { useState } from 'react';

const MyComponent = () => {
  const [inputValue, setInputValue] = useState('');

  // 处理表单提交事件
  const handleSubmit = (event) => {
    event.preventDefault();
    // 执行提交表单的逻辑...
  };

  // 处理键盘按下事件
  const handleKeyDown = (event) => {
    if (event.key === 'Enter') {
      // 执行按下回车键的逻辑...
    }
  };

  // 处理元素获取焦点事件
  const handleFocus = () => {
    // 执行获取焦点的逻辑...
  };

  // 处理元素失去焦点事件
  const handleBlur = () => {
    // 执行失去焦点的逻辑...
  };

  // 处理鼠标进入元素事件
  const handleMouseEnter = () => {
    // 执行鼠标进入元素的逻辑...
  };

  // 处理鼠标离开元素事件
  const handleMouseLeave = () => {
    // 执行鼠标离开元素的逻辑...
  };

  // 处理滚动事件
  const handleScroll = () => {
    // 执行滚动的逻辑...
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <input type="text" value={inputValue} onChange={(event) => setInputValue(event.target.value)} />
        <button type="submit">Submit</button>
      </form>
      <div
        onKeyDown={handleKeyDown}
        onFocus={handleFocus}
        onBlur={handleBlur}
        onMouseEnter={handleMouseEnter}
        onMouseLeave={handleMouseLeave}
        onScroll={handleScroll}
        style={{ height: '200px', overflow: 'scroll', border: '1px solid black' }}
      >
        Scrollable Content
      </div>
    </div>
  );
};

export default MyComponent;
```

在上述代码中，我们展示了如何在React组件中使用其他常见的事件处理函数。这些事件处理函数包括：

1. `handleSubmit`函数用于处理表单的提交事件。在这个示例中，我们使用`event.preventDefault()`来阻止表单的默认提交行为，并执行相应的提交逻辑。

2. `handleKeyDown`函数用于处理键盘按下事件。在这个示例中，我们检查按下的键是否是回车键，并在按下回车键时执行相应的逻辑。

3. `handleFocus`函数用于处理元素获取焦点事件。在这个示例中，我们执行获取焦点的逻辑。

4. `handleBlur`函数用于处理元素失去焦点事件。在这个示例中，我们执行失去焦点的逻辑。

5. `handleMouseEnter`函数用于处理鼠标进入元素事件。在这个示例中，我们执行鼠标进入元素的逻辑。

6. `handleMouseLeave`函数用于处理鼠标离开元素事件。在这个示例中，我们执行鼠标离开元素的逻辑。

7. `handleScroll`函数用于处理滚动事件。在这个示例中，我们执行滚动的逻辑。

通过在相应的元素上添加相应的事件处理函数，我们可以捕获用户的交互行为，并在事件发生时执行相应的逻辑。

React 是一个非常流行的 JavaScript 库，可以与许多其他三方库和工具结合使用来创建强大的应用程序。以下是一些类似的 React 和其他三方库的组合应用的示例：

1. React + Redux：Redux 是一个用于管理应用程序状态的库，与 React 结合使用可以创建可预测的状态管理方案。

2. React + Vue：尽管 React 和 Vue 是两个不同的框架，但它们可以在同一个应用程序中共存。这种组合可以使用 React 来管理整个应用程序的结构，同时使用 Vue 组件来处理特定的功能和 UI 细节。

3. React + GraphQL：GraphQL 是一种用于查询和管理数据的查询语言和运行时。React 可以通过 GraphQL 查询数据并将其显示在组件中，从而实现高度灵活的数据获取和管理。

   下面是一个使用 React 和 GraphQL 的示例应用程序：

   1. 安装所需的依赖包：

   ```bash
   npx create-react-app react-graphql-app
   cd react-graphql-app
   npm install graphql apollo-boost react-apollo
   ```

   2. 在 `src/index.js` 文件中配置 Apollo 客户端：

   ```jsx
   import React from 'react';
   import ReactDOM from 'react-dom';
   import { ApolloProvider } from 'react-apollo';
   import ApolloClient from 'apollo-boost';
   import App from './App';
   const client = new ApolloClient({
     uri: 'https://api.example.com/graphql', // 替换为实际的 GraphQL API 地址
   });
   ReactDOM.render(
     <ApolloProvider client={client}>
       <App />
     </ApolloProvider>,
     document.getElementById('root')
   );
   ```

   3. 创建一个 GraphQL 查询组件：

   ```jsx
   import React from 'react';
   import { Query } from 'react-apollo';
   import gql from 'graphql-tag';
   const GET_BOOKS = gql`
     query GetBooks {
       books {
         id
         title
         author
       }
     }
   `;
   const BookList = () => (
     <Query query={GET_BOOKS}>
       {({ loading, error, data }) => {
         if (loading) return <p>Loading...</p>;
         if (error) return <p>Error :(</p>;
         return (
           <ul>
             {data.books.map((book) => (
               <li key={book.id}>
                 <h3>{book.title}</h3>
                 <p>{book.author}</p>
               </li>
             ))}
           </ul>
         );
       }}
     </Query>
   );
   export default BookList;
   ```

   在上述代码中，我们使用 `react-apollo` 提供的 `Query` 组件来执行 GraphQL 查询，并根据查询结果渲染数据。
   4. 在 `App.js` 文件中使用 GraphQL 查询组件：

   ```jsx
   import React from 'react';
   import BookList from './BookList';
   function App() {
     return (
       <div>
         <h1>My Bookshelf</h1>
         <BookList />
       </div>
     );
   }
   export default App;
   ```

   在上述代码中，我们将 `BookList` 组件嵌入到 `App` 组件中，并在页面上显示图书列表。
   通过以上示例代码，你可以在 React 应用程序中使用 GraphQL 来获取数据，并使用 `react-apollo` 库来管理 GraphQL 查询和状态。请确保将示例代码中的 GraphQL API 地址替换为实际可用的地址。

4. React + Firebase：Firebase 是一个由 Google 提供的后端开发平台，它包含了许多功能模块，例如实时数据库、身份验证和存储。React 可以与 Firebase 集成，以实现实时数据同步、用户身份验证和云存储等功能。

   下面是一个使用 React 和 Firebase 的示例应用程序：

   1. 创建一个新的 React 应用程序并安装 Firebase：

   ```bash
   npx create-react-app react-firebase-app
   cd react-firebase-app
   npm install firebase
   ```

   2. 在 Firebase 控制台中创建一个新的项目，并获取你的 Firebase 配置信息。
   3. 在 `src/index.js` 文件中配置 Firebase：

   ```jsx
   import React from 'react';
   import ReactDOM from 'react-dom';
   import firebase from 'firebase/app';
   import 'firebase/firestore';
   import App from './App';
   // 替换为你的 Firebase 配置信息
   const firebaseConfig = {
     apiKey: 'YOUR_API_KEY',
     authDomain: 'YOUR_AUTH_DOMAIN',
     projectId: 'YOUR_PROJECT_ID',
     storageBucket: 'YOUR_STORAGE_BUCKET',
     messagingSenderId: 'YOUR_MESSAGING_SENDER_ID',
     appId: 'YOUR_APP_ID',
   };
   firebase.initializeApp(firebaseConfig);
   ReactDOM.render(
     <React.StrictMode>
       <App />
     </React.StrictMode>,
     document.getElementById('root')
   );
   ```

   4. 创建一个 `Firebase.js` 文件，用于导出 Firebase 实例和其他相关配置：

   ```jsx
   import firebase from 'firebase/app';
   import 'firebase/firestore';
   const firebaseConfig = {
     // 替换为你的 Firebase 配置信息
     apiKey: 'YOUR_API_KEY',
     authDomain: 'YOUR_AUTH_DOMAIN',
     projectId: 'YOUR_PROJECT_ID',
     storageBucket: 'YOUR_STORAGE_BUCKET',
     messagingSenderId: 'YOUR_MESSAGING_SENDER_ID',
     appId: 'YOUR_APP_ID',
   };
   firebase.initializeApp(firebaseConfig);
   // 初始化 Firebase Firestore 实例
   const db = firebase.firestore();
   export { db };
   ```

   5. 创建一个 `AddTodo.js` 组件，用于添加待办事项到 Firebase Firestore：

   ```jsx
   import React, { useState } from 'react';
   import { db } from './Firebase';
   const AddTodo = () => {
     const [todo, setTodo] = useState('');
     const handleInputChange = (e) => {
       setTodo(e.target.value);
     };
     const handleSubmit = (e) => {
       e.preventDefault();
       db.collection('todos').add({
         text: todo,
         completed: false,
       });
       setTodo('');
     };
     return (
       <form onSubmit={handleSubmit}>
         <input type="text" value={todo} onChange={handleInputChange} />
         <button type="submit">Add Todo</button>
       </form>
     );
   };
   export default AddTodo;
   ```

   在上述代码中，我们使用了 `db` 导入自 `Firebase.js`，并在提交表单时使用 `db.collection('todos').add()` 将待办事项添加到 Firestore 集合中。
   6. 创建一个 `TodoList.js` 组件，用于从 Firestore 获取待办事项列表：

   ```jsx
   import React, { useEffect, useState } from 'react';
   import { db } from './Firebase';
   const TodoList = () => {
     const [todos, setTodos] = useState([]);
      // 使用useEffect钩子函数，在组件挂载时订阅数据库中的todos集合，并在组件卸载时取消订阅
      useEffect(() => {
            // 订阅数据库中的todos集合
            const unsubscribe = db.collection('todos').onSnapshot((snapshot) => {
              // 将订阅到的数据转换为数组
              const todosData = snapshot.docs.map((doc) => ({
                id: doc.id,
                ...doc.data(),
              }));
              // 将数据存储到组件的状态中
              setTodos(todosData);
            });
            // 返回一个函数，在组件卸载时取消订阅
            return () => {
              unsubscribe();
            };
      }, []); // 在依赖项数组中传递一个空数组 []，确保只在组件加载时执行一次。这样做是因为我们只想在组件加载时订阅一次，而不是在每次组件重新渲染时都订阅一次。

   //如果在依赖项数组中传递其他变量，例如 [todos]，那么每当 todos 发生变化时，useEffect 都会重新执行。这可能会导致多次订阅和取消订阅，而不是我们所期望的只在组件加载和卸载时执行一次。
     return (
       <ul>
         {todos.map((todo) => (
           <li key={todo.id}>{todo.text}</li>
         ))}
       </ul>
     );
   };
   export default TodoList;
   ```

   在上述代码中，我们使用了 `db` 导入自 `Firebase.js`，并使用 `onSnapshot()` 方法监听 Firestore 集合中的变化，并将数据保存在本地状态中。
   7. 创建一个 `App.js` 组件，使用 `AddTodo` 和 `TodoList` 组件：

   ```jsx
   import React from 'react';
   import AddTodo from './AddTodo';
   import TodoList from './TodoList';
   function App() {
     return (
       <div>
         <h1>Todo App</h1>
         <AddTodo />
         <TodoList />
       </div>
     );
   }
   export default App;
   ```

在上述代码中，我们将 `AddTodo` 组件和 `TodoList` 组件嵌入到 `App` 组件中。
通过以上示例代码，你可以在 React 应用程序中使用 Firebase 来实现待办事项的添加和展示功能。请确保将示例代码中的 Firebase 配置信息替换为你自己项目的配置。

5. React + D3：D3 是一个用于创建数据可视化的 JavaScript 库。React 可以与 D3 结合使用，以在 React 组件中呈现和更新 D3 图表和可视化效果。

6. React + Material-UI：Material-UI 是一个用于构建美观的 Material Design 风格 UI 的 React 组件库。通过使用 Material-UI，可以方便地创建具有一致外观和动画效果的 React 应用程序。

这只是一些常见的组合示例，实际上，React 可以与许多其他库和工具结合使用，以满足不同应用程序的需求。选择合适的组合取决于你的项目要求和个人偏好。

React 和 Material-UI 是一个非常流行的组合，Material-UI 是一个提供了 Material Design 风格的 React UI 组件库。下面是一个在 React 中使用 Material-UI 的示例：

1. 首先，创建一个新的 React 应用程序：

```bash
npx create-react-app react-material-ui-app
cd react-material-ui-app
```

2. 安装 Material-UI 的核心库以及它的图标库：

```bash
npm install @material-ui/core @material-ui/icons
```

3. 创建一个简单的 Material-UI 组件：

```jsx
import React from 'react';
import { Button } from '@material-ui/core';
const App = () => {
  return (
    <div>
      <h1>Hello Material-UI</h1>
      <Button variant="contained" color="primary">
        Click me
      </Button>
    </div>
  );
};
export default App;
```

在上述代码中，我们导入了 Material-UI 的 `Button` 组件，并在组件中使用它。`variant="contained"` 和 `color="primary"` 是一些常用的属性，用于设置按钮的样式。
4. 运行应用程序：

```bash
npm start
```

现在你应该能够在浏览器中看到一个带有 "Hello Material-UI" 标题和一个按钮的页面。
这只是一个简单的示例，Material-UI 还提供了许多其他的组件和功能，例如 AppBar、Drawer、Typography 等。你可以在 Material-UI 的官方文档中找到更多的组件和用法示例：<https://mui.com/>

React 和 Ant Design 是另一个常用的组合，Ant Design 是一个基于 React 的企业级 UI 组件库。下面是一个在 React 中使用 Ant Design 的示例：

1. 首先，创建一个新的 React 应用程序：

```bash
npx create-react-app react-ant-design-app
cd react-ant-design-app
```

2. 安装 Ant Design 的依赖：

```bash
npm install antd
```

3. 在项目的根组件中引入 Ant Design 的样式和组件：

```jsx
import React from 'react';
import { Button } from 'antd';
import 'antd/dist/antd.css';
const App = () => {
  return (
    <div>
      <h1>Hello Ant Design</h1>
      <Button type="primary">Click me</Button>
    </div>
  );
};
export default App;
```

在上述代码中，我们导入了 Ant Design 的 `Button` 组件，并在组件中使用它。`type="primary"` 是一个常用的属性，用于设置按钮的样式。
4. 运行应用程序：

```bash
npm start
```

现在你应该能够在浏览器中看到一个带有 "Hello Ant Design" 标题和一个按钮的页面。
Ant Design 还提供了许多其他的组件和功能，例如表单、布局、导航等。你可以在 Ant Design 的官方文档中找到更多的组件和用法示例：<https://ant.design/components/>

使用 Ant Design 进行表单验证可以通过 `Form` 组件和 `Form.Item` 组件来实现。下面是一个示例，演示了如何在 Ant Design 中进行表单验证：

```jsx
import React from 'react';
import { Form, Input, Button } from 'antd';
const App = () => {
  const onFinish = (values) => {
    console.log('Form values:', values);
  };
  return (
    <div>
      <h1>Form Validation with Ant Design</h1>
      <Form
        name="basic"
        initialValues={{ remember: true }}
        onFinish={onFinish}
      >
        <Form.Item
          label="Username"
          name="username"
          rules={[
            { required: true, message: 'Please input your username!' },
            { min: 4, message: 'Username must be at least 4 characters!' },
          ]}
        >
          <Input />
        </Form.Item>
        <Form.Item
          label="Password"
          name="password"
          rules={[
            { required: true, message: 'Please input your password!' },
            { min: 6, message: 'Password must be at least 6 characters!' },
          ]}
        >
          <Input.Password />
        </Form.Item>
        <Form.Item>
          <Button type="primary" htmlType="submit">
            Submit
          </Button>
        </Form.Item>
      </Form>
    </div>
  );
};
export default App;
```

在上述代码中，我们使用了 `Form` 组件来创建表单。每个表单项都被包装在一个 `Form.Item` 组件中，其中设置了相应的验证规则。`rules` 属性接受一个数组，其中可以包含多个验证规则。
当用户提交表单时，如果验证规则通过，`onFinish` 回调函数将被触发，我们可以在这个函数中处理表单数据。如果验证规则失败，Ant Design 会自动显示错误信息。
这只是一个简单的示例，Ant Design 还提供了更多复杂的验证规则和自定义验证功能。你可以在 Ant Design 的官方文档中找到更多关于表单验证的详细信息：<https://ant.design/components/form/#components-form-demo-validate-static>

当使用 Ant Design 的布局组件时，你可以使用 `Layout`、`Grid` 和 `Space` 组件来构建页面布局。下面是一些示例代码，展示了如何使用这些布局组件：

1. 使用 `Layout` 组件进行基本的页面布局：

```jsx
import React from 'react';
import { Layout } from 'antd';
const { Header, Content, Footer } = Layout;
const App = () => {
  return (
    <Layout>
      <Header>Header</Header>
      <Content>Content</Content>
      <Footer>Footer</Footer>
    </Layout>
  );
};
export default App;
```

2. 使用 `Grid` 组件进行响应式布局：

```jsx
import React from 'react';
import { Row, Col } from 'antd';
const App = () => {
  return (
    <Row>
      <Col span={12}>Column 1</Col>
      <Col span={12}>Column 2</Col>
    </Row>
  );
};
export default App;
```

3. 使用 `Space` 组件进行间距控制：

```jsx
import React from 'react';
import { Space, Button } from 'antd';
const App = () => {
  return (
    <Space>
      <Button type="primary">Button 1</Button>
      <Button type="primary">Button 2</Button>
      <Button type="primary">Button 3</Button>
    </Space>
  );
};
export default App;
```

这些示例展示了如何使用 Ant Design 的布局组件来构建基本的页面布局。你可以根据自己的需求进一步自定义、嵌套和组合这些布局组件。
更多关于 Ant Design 的布局组件的详细信息，你可以参考官方文档：<https://ant.design/components/layout/>

#### 组件间通信

在前端开发中，组件间的通信是非常重要的一个概念。在大型应用程序中，用户界面往往会被拆分为多个小组件，每个组件都有自己的状态和逻辑。这些组件之间需要互相协作、通信以实现复杂的功能。

下面列举一些常见的组件间通信方式：

1. props：父组件可以通过props属性向子组件传递数据，子组件可以通过props接收数据。这是React框架中最基础也最常见的组件间通信方式。

2. state lifting：如果两个或多个兄弟组件（没有直接父子关系）需要共享同一个状态，可以将该状态保存在它们公共的祖先组件的state中，并将其作为props从祖先组件传递到这些组件中。这样，当某个组件改变状态时，其他组件也会同时更新。

3.事件机制：可以在组件之间触发自定义事件来完成通信，这种机制常常使用在跨级别的组件通信上。我们对祖先组件添加一个自定义事件处理函数，在需要的地方使用$emit()触发事件，而监听该事件的组件则可以通过$on()方法注册相应的事件处理函数进行响应。

4.订阅/发布模式：是一种更加灵活的组件通信模式。其中一个组件作为消息发布者，另外一个或多个组件则可以订阅该消息，当消息发布者发送消息时，所有已经订阅该消息的组件都会收到通知，并进行相应的处理。

总的来说，在组件间通信中选择合适的方式非常关键，不同场景使用不同通信方式可以提高代码可维护性和开发效率。
