---
aliases: 
date: 2025-03-15 10:36
update: 2025-03-15 10:37
categories: 
rating:
---

### 推荐的工具

**[Jest](https://facebook.github.io/jest/)** 是一个 JavaScript 测试运行器。它允许你使用 [`jsdom`](https://zh-hans.legacy.reactjs.org/docs/testing-environments.html#mocking-a-rendering-surface) 操作 DOM 。尽管 jsdom 只是对浏览器工作表现的一个近似模拟，对测试 React 组件来说它通常也已经够用了。Jest 有着十分优秀的迭代速度，同时还提供了若干强大的功能，比如它可以模拟 [modules](https://zh-hans.legacy.reactjs.org/docs/testing-environments.html#mocking-modules) 和 [timers](https://zh-hans.legacy.reactjs.org/docs/testing-environments.html#mocking-timers) 让你更精细的控制代码如何执行。
**[React 测试库](https://testing-library.com/react)** 是一组能让你不依赖 React 组件具体实现对他们进行测试的辅助工具。它让重构工作变得轻而易举，还会推动你拥抱有关无障碍的最佳实践。虽然它不能让你省略子元素来浅（shallowly）渲染一个组件，但像 Jest 这样的测试运行器可以通过 [mocking](https://zh-hans.legacy.reactjs.org/docs/testing-recipes.html#mocking-modules) 让你做到。
这一章节被划分成了两页内容：

- [技巧](https://zh-hans.legacy.reactjs.org/docs/testing-recipes.html)：为 React 组件编写测试时的常见模式。
- [环境](https://zh-hans.legacy.reactjs.org/docs/testing-environments.html)：为 React 组件搭建测试环境的时候有哪些要考虑的东西。

# 测试环境

### 测试运行器

使用 [Jest](https://jestjs.io/)，[mocha](https://mochajs.org/)，[ava](https://github.com/avajs/ava) 等测试运行器能像编写 JavaScript 一样编写测试套件，并将其作为开发过程的环节运行。此外，测试套件也将作为持续集成的环节运行。

- Jest 与 React 项目广泛兼容，支持诸如模拟 [模块](https://zh-hans.legacy.reactjs.org/docs/testing-environments.html#mocking-modules)、[计时器](https://zh-hans.legacy.reactjs.org/docs/testing-environments.html#mocking-timers) 和 [`jsdom`](https://zh-hans.legacy.reactjs.org/docs/testing-environments.html#mocking-a-rendering-surface) 等特性。**如果你使用 Create React App，[Jest 已经能够开箱即用](https://facebook.github.io/create-react-app/docs/running-tests)且包含许多实用的默认配置。**
- 像 [mocha](https://mochajs.org/#running-mocha-in-the-browser) 这样的库在真实浏览器环境下运行良好，并且可以为明确需要它的测试提供帮助。
- 端对端测试用于测试跨多个页面的长流程，并且需要[不同的设置](https://zh-hans.legacy.reactjs.org/docs/testing-environments.html#end-to-end-tests-aka-e2e-tests)。

### 模拟渲染表面

测试通常在无法访问真实渲染表面（如浏览器）的环境中运行。对于这些环境，我们建议使用 [`jsdom`](https://github.com/jsdom/jsdom) 来模拟浏览器，这是一个在 Node.js 内运行的轻量级浏览器实现。
如果您正在编写一个主要测试浏览器特定行为的库，并且需要布局或真实输入等原生浏览器行为，那么你可以使用像 [mocha](https://mochajs.org/) 这样的框架。

### Events

我们建议在 DOM 元素上触发真正的 DOM 事件，然后对结果进行断言。考虑一个 `Toggle` 组件：

```jsx
// toggle.js
import React, { useState } from "react";
export default function Toggle(props) {
  const [state, setState] = useState(false);
  return (
    <button
      onClick={() => {
        setState(previousState => !previousState);
        props.onChange(!state);
      }}
      data-testid="toggle"
    >
      {state === true  "Turn off" : "Turn on"}
    </button>
  );
}
```

我们可以为它编写测试：

```jsx
// toggle.test.js
import React from "react";
import { render, unmountComponentAtNode } from "react-dom";
import { act } from "react-dom/test-utils";
import Toggle from "./toggle";
let container = null;
beforeEach(() => {
  // 创建一个 DOM 元素作为渲染目标
  container = document.createElement("div");
  document.body.appendChild(container);});
afterEach(() => {
  // 退出时进行清理
  unmountComponentAtNode(container);
  container.remove();
  container = null;
});
it("点击时更新值", () => {
  const onChange = jest.fn();
  act(() => {
    render(<Toggle onChange={onChange} />, container);
  });
  // 获取按钮元素，并触发点击事件
  const button = document.querySelector("[data-testid=toggle]");
  expect(button.innerHTML).toBe("Turn on");
  act(() => {
    button.dispatchEvent(new MouseEvent("click", { bubbles: true }));
  });
  expect(onChange).toHaveBeenCalledTimes(1);
  expect(button.innerHTML).toBe("Turn off");
  act(() => {
    for (let i = 0; i < 5; i++) {
      button.dispatchEvent(new MouseEvent("click", { bubbles: true }));
    }  });
  expect(onChange).toHaveBeenCalledTimes(6);
  expect(button.innerHTML).toBe("Turn on");
});
```
