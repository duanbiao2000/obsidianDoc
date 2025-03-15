---
aliases:

---
20230717 1207
links:
title:
origin:
tags: #Mindset/Reflection #Action/TODO 


[Frequent 'react-bootstrap' Questions - Stack Overflow](https://stackoverflow.com/questions/tagged/react-bootstrap?tab=Frequent)

Bootstrap 5 no longer requires jQuery and is [modular](https://getbootstrap.com/docs/5.0/getting-started/javascript/#using-bootstrap-as-a-module) so you can @import it like any other JS module which makes it easier to use with React. It also means you can use Bootstrap _without_ a 3rd party library like reactstrap or react-bootstrap.

This makes it easier to use Bootstrap 5 with the React 16.8+ `useEffect` and `useState` hooks. So that we avoid direct DOM manipulation in React, get the element instance with a `useRef` hook...



[React Bootstrap 5 Example - popover, toast, collapse on Codeply](https://www.codeply.com/p/SfIG4ZsBIc)
以下是对代码块进行详细注释和知识点总结的示例：
```jsx
// 导入所需的 React Hooks 和 Bootstrap 组件
const { useState, useEffect, useRef } = React
const { Collapse, Popover, Toast } = bootstrap
// 折叠面板示例组件
function CollapseDemo() {
    // 使用 useState Hook 创建一个名为 toggle 的状态变量和修改函数
    var [toggle, setToggle] = useState(false)
    // 使用 useRef Hook 创建一个名为 collapseRef 的引用
    var collapseRef = useRef()
    // 使用 useEffect Hook 监听 toggle 状态变化
    useEffect(() => {
        // 获取 collapseRef 引用的 DOM 元素
        var myCollapse = collapseRef.current
        // 创建一个 Collapse 实例，并绑定到 myCollapse 元素上
        var bsCollapse = new Collapse(myCollapse, { toggle: false })
        // 根据 toggle 状态显示或隐藏折叠面板
        toggle ? bsCollapse.show() : bsCollapse.hide()
    })
    return (
        <div className="py-2">
            {/* 创建一个按钮，点击按钮时切换 toggle 的状态 */}
            <button className="btn btn-primary" onClick={() => setToggle(toggle => !toggle)}>
                Toggle collapse
            </button>
            {/* 创建一个折叠面板，将 collapseRef 设置为 ref 属性 */}
            <div className="collapse" ref={collapseRef}>
                This is the toggle-able content!
            </div>
        </div>
    )
}
// 弹出框示例组件
function PopoverDemo() {
    // 使用 useRef Hook 创建一个名为 popoverRef 的引用
    const popoverRef = useRef()
    // 使用 useEffect Hook 在组件挂载后初始化弹出框
    useEffect(() => {
        // 使用 popoverRef 引用的 DOM 元素创建一个 Popover 实例
        var popover = new Popover(popoverRef.current, {
            content: "Hello popover content!",
            title: "My Popover",
            trigger: 'hover'
        })
    })
    return (
        <div className="py-2">
            {/* 创建一个按钮，将 popoverRef 设置为 ref 属性 */}
            <button className="btn btn-danger" ref={popoverRef}>
                Hover for popover
            </button>
        </div>
    )
}
// 提示框示例组件
function ToastDemo() {
    // 使用 useState Hook 创建一个名为 toast 的状态变量和修改函数
    var [toast, setToast] = useState(false);
    // 使用 useRef Hook 创建一个名为 toastRef 的引用
    const toastRef = useRef();
    // 使用 useEffect Hook 监听 toast 状态变化
    useEffect(() => {
        // 获取 toastRef 引用的 DOM 元素
        var myToast = toastRef.current
        // 创建一个 Toast 实例，并绑定到 myToast 元素上
        var bsToast = new Toast(myToast)
        // 根据 toast 状态显示或隐藏提示框
        toast ? bsToast.show() : false
        // 监听提示框隐藏事件，更新 toast 状态
        myToast.addEventListener('hidden.bs.toast', () => {
            setToast(false)
        })
    })
    return (
        <div className="py-2">
            {/* 创建一个按钮，点击按钮时切换 toast 的状态 */}
            <button className="btn btn-success" onClick={() => setToast(toast => !toast)}>
                Show toast
            </button>
            {/* 创建一个提示框，将 toastRef 设置为 ref 属性 */}
            <div className="toast position-absolute top-0 end-0 m-4" role="alert" ref={toastRef}>
                <div className="toast-header">
                    <strong className="me-auto">Bootstrap 5</strong>
                    <small>11 mins ago</small>
                    <button type="button" className="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
                </div>
                <div className="toast-body">
                    Hello, world! This is a toast message.
                </div>
            </div>
        </div>
    )
}
// 应用组件
function App() {
    // 使用 useState Hook 创建一个名为 mounted 的状态变量和修改函数
    const [mounted, setMounted] = useState(true);
    return (
        <div className="container py-4">
            <h3>Bootstrap 5 React Examples</h3>
            {/* 根据 mounted 状态决定是否渲染组件 */}
            {mounted &&
                <div>
                    <PopoverDemo/>
                    <CollapseDemo/>
                    <ToastDemo/>
                </div>
            }
        </div>
    )
}
// 将 App 组件渲染到根元素中
ReactDOM.render(<App/>, document.querySelector('#root'));
```
知识点总结：
- 使用 React Hooks（useState、useEffect、useRef）来处理组件的状态和副作用。
- 使用 useRef Hook 创建引用，以获取或操作 DOM 元素。
- 使用 useEffect Hook 监听组件挂载和状态变化，并执行相应的操作。
- 使用 Collapse、Popover、Toast 等 Bootstrap 组件来实现相应的功能。
- 使用事件监听器（例如 hidden.bs.toast）来处理组件事件。
- 使用箭头函数和条件渲染来处理组件的交互和显示。
希望这些详细注释和知识点总结能够帮助您更好地理解代码的功能和实现。如果您还有其他问题，请随时提问。

bind dynamic drop using arrow function.

以下是对代码进行重构的建议：
1. 使用函数式组件代替类组件：
   - 由于该组件只有一个 `render` 方法，并且没有其他生命周期方法或状态管理，可以将其重构为函数式组件。
   - 函数式组件更简洁，易于理解和测试。
2. 使用 `map` 方法的返回值添加 `key` 属性：
   - 在 `optionTemplate` 中使用 `map` 方法时，为每个选项添加一个唯一的 `key` 属性。
   - 这有助于 React 更高效地处理列表更新。
3. 添加 `handleChange` 方法：
   - 在 `select` 元素上添加 `onChange` 事件处理程序来处理选项的变化。
   - 更新组件的状态以反映用户所选的值。
通过对以上建议进行重构，代码可以更加简洁、可读性更高。下面是重构后的代码示例：
```javascript
function BindDropDown() {
  const values = [
    { name: 'One', id: 1 },
    { name: 'Two', id: 2 },
    { name: 'Three', id: 3 },
    { name: 'Four', id: 4 }
  ];
  const [value, setValue] = React.useState('');
  const handleChange = (event) => {
    setValue(event.target.value);
  };
  const optionTemplate = values.map(v => (
    <option key={v.id} value={v.id}>{v.name}</option>
  ));
  return (
    <label>
      Pick your favorite Number:
      <select value={value} onChange={handleChange}>
        {optionTemplate}
      </select>
    </label>
  );
}
ReactDOM.render(
  <BindDropDown />,
  document.getElementById('root')
);
```
通过上述重构，我们将类组件转换为函数式组件，并添加了 `handleChange` 方法来处理选项的变化。代码更加简洁、易于理解和维护。
### [React-Bootstrap link item in a navitem](https://stackoverflow.com/questions/35687353/react-bootstrap-link-item-in-a-navitem)

以下是补充完整功能代码，并在代码块中进行了注释：
```jsx
import React from 'react';
import { Nav, NavDropdown } from 'react-bootstrap';
import { Link } from 'react-router-dom';
function Navigation(props) {
  return (
    <Nav>
      {/* 导航链接到主页 */}
      <Nav.Link as={Link} to="/home">
        Home
      </Nav.Link>
      {/* 导航链接到图书库 */}
      <Nav.Link as={Link} to="/book">
        Book Inv
      </Nav.Link>
      {/* 下拉菜单 */}
      <NavDropdown title="Authorization" id="basic-nav-dropdown">
        {/* 下拉菜单项，点击后执行 logout 方法 */}
        <NavDropdown.Item onClick={props.logout}>
          Logout
        </NavDropdown.Item>
      </NavDropdown>
    </Nav>
  );
}
export default Navigation;
```
在以上代码中，我们创建了一个 `Navigation` 组件，该组件包含一个导航栏，其中包含了主页链接、图书库链接和授权下拉菜单。在授权下拉菜单中，我们添加了一个注销选项，点击该选项会执行传递给组件的 `logout` 方法。
请注意，上述代码假设您已经正确安装了 `react-bootstrap` 和 `react-router-dom` 并进行了相应的导入。


以下是将之前的两段代码进行整合和重构的最佳实践示例：
```jsx
import React from 'react';
import { BrowserRouter, Route, Link } from 'react-router-dom';
import { Nav, NavDropdown } from 'react-bootstrap';
function Home() {
  return <h2>Home</h2>;
}
function BookInventory() {
  return <h2>Book Inventory</h2>;
}
function Logout() {
  return <h2>Logout</h2>;
}
function Navigation() {
  return (
    <Nav>
      <Nav.Link as={Link} to="/home">
        Home
      </Nav.Link>
      <Nav.Link as={Link} to="/book">
        Book Inventory
      </Nav.Link>
      <NavDropdown title="Authorization" id="basic-nav-dropdown">
        <NavDropdown.Item as={Link} to="/logout">
          Logout
        </NavDropdown.Item>
      </NavDropdown>
    </Nav>
  );
}
function App() {
  return (
    <BrowserRouter>
      <div>
        <Navigation />
        <Route path="/home" component={Home} />
        <Route path="/book" component={BookInventory} />
        <Route path="/logout" component={Logout} />
      </div>
    </BrowserRouter>
  );
}
export default App;
```
在上述代码中，我们将之前的两段代码整合到了一个单一的文件中，并应用了最佳实践：
- 将导航栏代码提取到 `Navigation` 组件中，使代码更具模块化和可复用性。
- 使用 `BrowserRouter` 包裹整个应用，并在 `Route` 组件中定义路径和对应的组件渲染。
- 使用 `Link` 组件来创建导航链接，确保导航链接与路由路径保持一致。
这样，我们实现了基于 `react-router` 和 `react-bootstrap` 的整合和重构，使代码更加清晰和易于维护。

### [Listen to keypress for document in reactjs](https://stackoverflow.com/questions/29069639/listen-to-keypress-for-document-in-reactjs)

为了在按下 Escape 键时关闭 React Bootstrap 的活动 Popover，您可以使用以下最佳实践代码：
```jsx
import React, { useRef, useEffect } from 'react';
import { Popover, OverlayTrigger } from 'react-bootstrap';
function MyComponent() {
  const popoverRef = useRef(null);
  useEffect(() => {
    const handleKeyPress = (event) => {
      if (event.key === 'Escape') {
        popoverRef.current?.hide();
      }
    };
    document.addEventListener('keydown', handleKeyPress);
    return () => {
      document.removeEventListener('keydown', handleKeyPress);
    };
  }, []);
  return (
    <OverlayTrigger
      trigger="click"
      placement="bottom"
      overlay={
        <Popover ref={popoverRef}>
          <Popover.Header>Popover Title</Popover.Header>
          <Popover.Body>Popover Content</Popover.Body>
        </Popover>
      }
    >
      <button>Show Popover</button>
    </OverlayTrigger>
  );
}
export default MyComponent;
```
在上述代码中，我们使用了 `useRef` 来创建 `popoverRef` 引用。然后，使用 `useEffect` 来监听键盘按下事件。当按下 Escape 键时，我们通过 `popoverRef.current?.hide()` 来隐藏 Popover。
在组件的返回部分，我们使用 `OverlayTrigger` 包裹了触发 Popover 的按钮，并将 Popover 作为 `overlay` 属性传递给 `OverlayTrigger`。通过设置 `trigger` 属性为 "click"，可以通过点击按钮来触发 Popover。
在 `useEffect` 中，我们使用空的依赖数组 `[]` 来确保只运行一次键盘事件监听器的绑定和解绑。
这样，您就可以在按下 Escape 键时关闭活动的 React Bootstrap Popover。
希望这个最佳实践代码能够帮助您！如果您还有其他问题，请随时提问。

当中使用到了 `react-bootstrap` 的两个组件：`Popover` 和 `OverlayTrigger`。下面是对这两个组件的功能进行讲解并附带示例：
1. `Popover` 组件：
   - `Popover` 组件用于创建一个弹出框，用于显示额外的内容或提示信息。
   - `Popover` 组件通常作为某个元素的 `overlay` 属性的值传递给其他组件（例如 `OverlayTrigger`）。
   - `Popover` 组件包含了 `Popover.Header` 和 `Popover.Body` 组件，用于定义弹出框的标题和内容。
示例使用：
```jsx
<Popover>
  <Popover.Header>Popover Title</Popover.Header>
  <Popover.Body>Popover Content</Popover.Body>
</Popover>
```
2. `OverlayTrigger` 组件：
   - `OverlayTrigger` 组件用于在触发某个事件（例如点击、悬停等）时显示和隐藏覆盖在元素上方的内容。
   - `OverlayTrigger` 组件需要一个触发元素和一个覆盖内容（通过 `overlay` 属性传递）来工作。
   - 可以通过设置 `trigger` 属性来指定触发的事件，默认为 `hover`。
示例使用：
```jsx
<OverlayTrigger
  trigger="click"
  placement="bottom"
  overlay={
    <Popover>
      <Popover.Header>Popover Title</Popover.Header>
      <Popover.Body>Popover Content</Popover.Body>
    </Popover>
  }
>
  <button>Show Popover</button>
</OverlayTrigger>
```
在上述示例中，当点击按钮时，会触发 `OverlayTrigger` 组件，显示一个带有标题和内容的 `Popover` 弹出框。
这些 `react-bootstrap` 组件提供了丰富的功能和样式，可以快速构建美观的 UI 组件。
希望对 `Popover` 和 `OverlayTrigger` 组件的功能讲解和示例有所帮助！如果您有任何其他问题，请随时提问。


