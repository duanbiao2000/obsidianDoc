---
aliases: null
theme: null
original: null
url: null
author: null
date_created: 2024-08-03 14:36
date_updated: null
type: null
high_priority: false
tags: null
---
下面是一些关于 React 测试的常见面试问题，以及相应的回答：
1. 为什么要进行 React 测试
- React 测试可以帮助我们确保代码的质量和正确性，减少 bug 和错误的出现。它提供了一种自动化的方式来验证组件的行为和功能，以及确保组件在不同环境和使用场景下的正常工作。
2. React 测试的工具有哪些
- React 测试常用的工具有 Jest、Enzyme、React Testing Library 和 Cypress 等。
- 
- Jest 是一个功能强大的测试框架，而 Enzyme 和 React Testing Library 是用于测试 React 组件的工具库。Cypress 则是一个用于进行端到端测试的工具。
3. 什么是单元测试什么是集成测试
   - 单元测试是对应用程序中最小可测试单元（如函数、方法、组件）进行测试的过程，目的是确保这些单元按预期方式工作。它通常是在隔离的环境中进行的，通过模拟依赖并进行断言来验证代码行为。
   - 集成测试是对多个组件或模块之间的交互进行测试的过程，目的是确保这些组件或模块能够正确协同工作。它通常涉及多个单元之间的协调和交互，并验证它们在集成环境中的行为。
4. 如何进行 React 组件的单元测试
   - React 组件的单元测试可以使用工具库如 Enzyme 或 React Testing Library 来模拟组件的渲染和交互，并对组件的输出进行断言。
   示例代码（使用 React Testing Library）：
   ```javascript
   import { render, screen, fireEvent } from '@testing-library/react';
   import Counter from './Counter';
   test('Counter 组件能够正确渲染并响应点击事件', () => {
     render(<Counter />);
     const counterElement = screen.getByText(/Count:/i);
     expect(counterElement).toBeInTheDocument();
     const incrementButton = screen.getByText('+');
     const decrementButton = screen.getByText('-');
     expect(screen.getByText(/Count: 0/i)).toBeInTheDocument();
     fireEvent.click(incrementButton);
     expect(screen.getByText(/Count: 1/i)).toBeInTheDocument();
     fireEvent.click(decrementButton);
     expect(screen.getByText(/Count: 0/i)).toBeInTheDocument();
   });
   ```
5. 如何测试 React 组件的异步操作
   - 对于 React 组件中的异步操作，可以使用 Jest 的异步测试特性或者使用 `async/await` 来处理。可以模拟异步请求，等待 Promise 的解析，然后进行断言验证。
   示例代码（使用 Jest 的异步测试特性）：
   ```javascript
   import { render, screen, waitFor } from '@testing-library/react';
   import CommentList from './CommentList';
   import { fetchComments } from './api';
   jest.mock('./api'); // 模拟 API 请求
   test('CommentList 组件能够正确渲染评论列表', async () => {
     const comments = [
       { id: 1, text: 'First comment' },
       { id: 2, text: 'Second comment' },
     ];
     fetchComments.mockResolvedValue(comments); // 模拟异步请求返回数据
     render(<CommentList />);
     expect(screen.getByText('Loading...')).toBeInTheDocument();
     await waitFor(() => {
       expect(screen.getByText('First comment')).toBeInTheDocument();
       expect(screen.getByText('Second comment')).toBeInTheDocument();
     });
   });
   ```

[测试概览 – React (reactjs.org)](https://zh-hans.legacy.reactjs.org/docs/testing.html)
现在有许多种测试 React 组件的方法。大体上可以被分为两类：
- **渲染组件树** 在一个简化的测试环境中渲染组件树并对它们的输出做断言检查。
- **运行完整应用** 在一个真实的浏览器环境中运行整个应用（也被称为“端到端（end-to-end）”测试）。
本章节主要专注于第一种情况下的测试策略。虽然完整的端到端测试在防止对重要工作流的多次回归方面很有价值，但对 React 组件来说这类测试并不怎么需要关注，因此不在本章节的讨论范围之内。
### 权衡
当挑选测试工具的时候，有些细节值得我们权衡考虑：
- **迭代速度 vs 真实环境：** 一些工具在做出改动和看到结果之间提供了非常快速的反馈循环，但没有精确的模拟浏览器的行为。另一些工具，也许使用了真实的浏览器环境，但却降低了迭代速度，而且在持续集成服务器中不太可靠。
- **mock 到什么程度：** 对组件来说，“单元测试”和“集成测试”之间的差别可能会很模糊。如果你在测试一个表单，用例是否应该也测试表单里的按钮呢一个按钮组件又需不需要有他自己的测试套件重构按钮组件是否应该影响表单的测试用例
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

