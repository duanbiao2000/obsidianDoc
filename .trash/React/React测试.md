
---
aliases:

---
20230720 1736
links:  [Introduction | Testing Library (testing-library.com)](https://testing-library.com/docs/)
title:
origin:
tags: #flashcards #todo 


## React测试面试常见提问

下面是一些关于 React 测试的常见面试问题，以及相应的回答：
1. 为什么要进行 React 测试？
  ?
   - React 测试可以帮助我们确保代码的质量和正确性，减少 bug 和错误的出现。它提供了一种自动化的方式来验证组件的行为和功能，以及确保组件在不同环境和使用场景下的正常工作。
2. React 测试的工具有哪些？
  ?
   - React 测试常用的工具有 Jest、Enzyme、React Testing Library 和 Cypress 等。Jest 是一个功能强大的测试框架，而 Enzyme 和 React Testing Library 是用于测试 React 组件的工具库。Cypress 则是一个用于进行端到端测试的工具。
3. 什么是单元测试？什么是集成测试？
   - 单元测试是对应用程序中最小可测试单元（如函数、方法、组件）进行测试的过程，目的是确保这些单元按预期方式工作。它通常是在隔离的环境中进行的，通过模拟依赖并进行断言来验证代码行为。
   - 集成测试是对多个组件或模块之间的交互进行测试的过程，目的是确保这些组件或模块能够正确协同工作。它通常涉及多个单元之间的协调和交互，并验证它们在集成环境中的行为。
4. 如何进行 React 组件的单元测试？
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
5. 如何测试 React 组件的异步操作？
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
以上是一些关于 React 测试的常见面试问题及回答。在准备面试时，建议你熟悉常用的测试工具和测试技术，并能够根据需求选择合适的测试工具和编写测试代码。同时，也要注意编写清晰、可读性强的测试用例，并对组件的不同方面进行全面的测试，以确保代码的质量和稳定性。

## 模拟对话

Sure! Here's a simulated conversation between colleagues during a React testing project. The conversation involves two to three people and will be conducted in both English and Chinese to meet the language requirements:
Person A: Hey everyone, I've just finished writing unit tests for the login component. Can someone review them and provide feedback?
Person B: Sure, I can take a look. Let me pull up the code on my machine.
Person C: 我也可以帮忙看一下。这是测试文件吗？
Person A: Yes, these are the test files. I've covered the basic functionality and edge cases. Please let me know if you find any issues or if there's anything I missed.
Person B: Alright, let me go through the tests. By the way, have you considered testing for error handling scenarios as well?
Person A: Yes, I've included some tests for error handling, but I'm open to suggestions if you think there's something more we should cover.
Person C: 我看了一下你的测试代码，看起来很不错。但是我觉得我们还可以添加一些异步测试，以确保登录请求的正确性。
Person A: That's a good point. I'll add some async tests to validate the login request. Thanks for the suggestion.
Person B: I've reviewed the tests, and overall, they look good. However, I noticed a couple of test cases that can be optimized for better readability. Let me share my suggestions with you.
Person A: Thanks for reviewing, Person B. I appreciate your feedback. Please go ahead and share your suggestions, and we can discuss any changes that need to be made.
Person C: 还有一件事我想提醒大家，在每次提交代码前，我们应该运行一遍所有的测试，以确保没有破坏现有的功能。
Person A: 是的，非常重要。我们可以将测试脚本集成到我们的持续集成流程中，以便自动运行测试并进行检查。
Person B: 非常同意。我们可以使用工具如Jenkins或Travis CI来实现自动化测试。
Person C: 好的，那我们就遵循这些步骤，确保我们的代码质量和稳定性。
Person A: 没问题，非常感谢大家的合作和建议。让我们继续努力，保持团队的高效和协作。
Person B: Absolutely! Let's keep up the good work and deliver a robust and reliable application. If anyone needs further assistance or has any questions, feel free to reach out.
Person C: 好的，大家一起加油吧！
This simulated conversation demonstrates how colleagues communicate during a React testing project, discussing code reviews, suggestions, and best practices. The conversation is conducted in English and Chinese, meeting the language requirements of IELTS or above.

>1. Unit tests: Tests that are written to validate the smallest testable parts of the code, such as functions or components. They help ensure the correctness of individual units of code.
>2. Test files: Files containing test cases and assertions used for testing the code.
>3. Error handling: A process of capturing and managing errors that occur during the execution of the code. Testing for error handling ensures that the code handles error conditions correctly.
>4. Async tests: Tests that involve asynchronous operations, such as API requests or Promises. These tests ensure the correctness of code that relies on asynchronous behavior.
>5. Continuous integration: The practice of merging code changes frequently and automatically running tests to ensure the stability and correctness of the software.
>6. Jenkins/Travis CI: Popular continuous integration tools used for automatically building, testing, and deploying software.
>7. Robustness: The ability of the software to handle unexpected inputs, errors, or edge cases, and continue functioning properly.
>8. Reliable application: An application that performs consistently and predictably, without unexpected crashes, errors, or data corruption.
>9. Assumptions: Statements or beliefs taken for granted during the conversation, such as assuming the availability of testing tools or the importance of running tests before code submission.
>10. Teamwork: Collaborative efforts and cooperation among team members to achieve common goals and objectives

[测试概览 – React (reactjs.org)](https://zh-hans.legacy.reactjs.org/docs/testing.html)
现在有许多种测试 React 组件的方法。大体上可以被分为两类：

- **渲染组件树** 在一个简化的测试环境中渲染组件树并对它们的输出做断言检查。
- **运行完整应用** 在一个真实的浏览器环境中运行整个应用（也被称为“端到端（end-to-end）”测试）。
本章节主要专注于第一种情况下的测试策略。虽然完整的端到端测试在防止对重要工作流的多次回归方面很有价值，但对 React 组件来说这类测试并不怎么需要关注，因此不在本章节的讨论范围之内。

### 权衡

当挑选测试工具的时候，有些细节值得我们权衡考虑：

- **迭代速度 vs 真实环境：** 一些工具在做出改动和看到结果之间提供了非常快速的反馈循环，但没有精确的模拟浏览器的行为。另一些工具，也许使用了真实的浏览器环境，但却降低了迭代速度，而且在持续集成服务器中不太可靠。
- **mock 到什么程度：** 对组件来说，“单元测试”和“集成测试”之间的差别可能会很模糊。如果你在测试一个表单，用例是否应该也测试表单里的按钮呢？一个按钮组件又需不需要有他自己的测试套件？重构按钮组件是否应该影响表单的测试用例？


### 推荐的工具

**[Jest](https://facebook.github.io/jest/)** 是一个 JavaScript 测试运行器。它允许你使用 [`jsdom`](https://zh-hans.legacy.reactjs.org/docs/testing-environments.html#mocking-a-rendering-surface) 操作 DOM 。尽管 jsdom 只是对浏览器工作表现的一个近似模拟，对测试 React 组件来说它通常也已经够用了。Jest 有着十分优秀的迭代速度，同时还提供了若干强大的功能，比如它可以模拟 [modules](https://zh-hans.legacy.reactjs.org/docs/testing-environments.html#mocking-modules) 和 [timers](https://zh-hans.legacy.reactjs.org/docs/testing-environments.html#mocking-timers) 让你更精细的控制代码如何执行。

**[React 测试库](https://testing-library.com/react)**是一组能让你不依赖 React 组件具体实现对他们进行测试的辅助工具。它让重构工作变得轻而易举，还会推动你拥抱有关无障碍的最佳实践。虽然它不能让你省略子元素来浅（shallowly）渲染一个组件，但像 Jest 这样的测试运行器可以通过 [mocking](https://zh-hans.legacy.reactjs.org/docs/testing-recipes.html#mocking-modules) 让你做到。

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
      {state === true ? "Turn off" : "Turn on"}
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

[MDN](https://developer.mozilla.org/en-US/docs/Web/API/MouseEvent)描述了不同的 DOM 事件及其属性。注意，你需要在创建的每个事件中传递 `{ bubbles: true }` 才能到达 React 监听器，因为 React 会自动将事件委托给 root。

>注意：
React 测试库为触发事件提供了一个[更简洁 helper](https://testing-library.com/docs/dom-testing-library/api-events)。

`DOM Testing Library` works with any environment that provides DOM APIs, such as Jest, Mocha + JSDOM, or a real browser.

### What you should avoid with Testing Library

You may want to avoid the following implementation details:↳

1. Internal state of a component
2. Internal methods of a component
3. Lifecycle methods of a component
4. Child components

Testing Library helper methods

|Type of Query|0 Matches|1 Match|>1 Matches|Retry (Async/Await)|
|---|---|---|---|:-:|
|**Single Element**|||||
|`getBy...`|Throw error|Return element|Throw error|No|
|`queryBy...`|Return `null`|Return element|Throw error|No|
|`findBy...`|Throw error|Return element|Throw error|Yes|
|**Multiple Elements**|||||
|`getAllBy...`|Throw error|Return array|Return array|No|
|`queryAllBy...`|Return `[]`|Return array|Return array|No|
|`findAllBy...`|Throw error|Return array|Return array|Yes|

```jsx
<body>
  <div id="app">
    <label for="username-input">Username</label>
    <input id="username-input" />
  </div>
</body>
```
You can use a query to find an element (byLabelText, in this case):↳

```jsx
import {screen, getByLabelText} from '@testing-library/dom'

// With screen:
const inputNode1 = screen.getByLabelText('Username')

// Without screen, you need to provide a container:
const container = document.querySelector('#app')
const inputNode2 = getByLabelText(container, 'Username')
```
上述代码示例演示了如何使用 `@testing-library/dom` 库来通过关联的标签访问输入元素。

在第一个示例中，使用 `screen.getByLabelText` 函数直接通过关联的标签访问输入元素。这里使用的标签文本是 "用户名"。`screen` 对象是 `@testing-library/dom` 提供的一个抽象层，可以方便地查询 DOM 元素，无需提供容器。

在第二个示例中，没有使用 `screen` 对象。在这种情况下，需要显式地提供一个容器元素。容器元素通过使用 `document.querySelector` 选择具有 id 为 "app" 的元素来获取。然后，使用容器和标签文本 "Username" 调用 `getByLabelText` 函数来访问输入元素。

这两个示例实现了相同的结果，即获取具有指定标签文本的输入元素的引用。使用 `screen` 还是提供容器的选择取决于测试设置和个人偏好。


```html
<div>Hello World</div>
```

```jsx
// Matching a string:
screen.getByText('Hello World') // full string match
screen.getByText('llo Worl', {exact: false}) // substring match
screen.getByText('hello world', {exact: false}) // ignore case

// Matching a regex:
screen.getByText(/World/) // substring match
screen.getByText(/world/i) // substring match, ignore case
screen.getByText(/^hello world$/i) // full string match, ignore case
screen.getByText(/Hello W?oRlD/i) // substring match, ignore case, searches for "hello world" or "hello orld"

// Matching with a custom function:
screen.getByText((content, element) => content.startsWith('Hello'))
```


### `screen.logTestingPlaygroundURL()`

```jsx
import {screen} from '@testing-library/dom'  
  
document.body.innerHTML = `  
<button>test</button>  
<span>multi-test</span>  
<div>multi-test</div>  
`  
  
// log entire document to testing-playground  
screen.logTestingPlaygroundURL()  
// log a single element  
screen.logTestingPlaygroundURL(screen.getByText('test'))
```

 [testing-playground.com](https://testing-playground.com/)

# ByRole

> getByRole, queryByRole, getAllByRole, queryAllByRole, findByRole, findAllByRole

```jsx
getByRole(
  // If you're using `screen`, then skip the container argument:
  container: HTMLElement,
  role: string,
  options?: {
    hidden?: boolean = false,
    name?: TextMatch,
    description?: TextMatch,
    selected?: boolean,
    busy?: boolean,
    checked?: boolean,
    pressed?: boolean,
    suggest?: boolean,
    current?: boolean | string,
    expanded?: boolean,
    queryFallbacks?: boolean,
    level?: number,
    value?: {
      min?: number,
      max?: number,
      now?: number,
      text?: TextMatch,
    }
  }): HTMLElement
```

```jsx
<body>  
<main aria-hidden="true">  
<button>Open dialog</button>  
</main>  
<div role="dialog">  
<button>Close dialog</button>  
</div>  
</body>
```

```jsx
<body>  
<div role="tablist">  
<button role="tab" aria-selected="true">Native</button>  
<button role="tab" aria-selected="false">React</button>  
<button role="tab" aria-selected="false">Cypress</button>  
</div>  
</body>
```

```jsx
<body>  
<section>  
<div role="alert" aria-busy="false">Login failed</div>  
<div role="alert" aria-busy="true">Error: Loading message...</div>  
</section>  
</body>
```

```jsx
<body>  
<section>  
<button role="checkbox" aria-checked="true">Sugar</button>  
<button role="checkbox" aria-checked="false">Gummy bears</button>  
<button role="checkbox" aria-checked="false">Whipped cream</button>  
</section>  
</body>
```

```jsx
<body>  
<nav>  
<a href="current/page" aria-current="true">👍</a>  
<a href="another/page">👎</a>  
</nav>  
</body>
```

```jsx
<body>  
<ul>  
<li role="alertdialog" aria-describedby="notification-id-1">  
<div><button>Close</button></div>  
<div id="notification-id-1">You have unread emails</div>  
</li>  
<li role="alertdialog" aria-describedby="notification-id-2">  
<div><button>Close</button></div>  
<div id="notification-id-2">Your session is about to expire</div>  
</li>  
</ul>  
</body>
```

```jsx
getByRole('alertdialog', {description: 'Your session is about to expire'})
```

`getByPlaceholderText` 函数是 `@testing-library/dom` 库中的一个函数，用于通过占位文本获取元素。

函数签名如下所示：
```javascript
getByPlaceholderText(
  container: HTMLElement,
  text: TextMatch,
  options?: {
    exact?: boolean = true,
    normalizer?: NormalizerFn,
  }
): HTMLElement
```

该函数接受三个参数：

1. `container`：必需参数，表示要在其中查找元素的容器元素。它是一个 `HTMLElement` 类型的对象，可以是任何包含待测元素的 DOM 容器。
    
2. `text`：必需参数，表示要匹配的占位文本。可以是一个字符串或一个正则表达式。
    
3. `options`：可选参数，表示该函数的选项配置。它是一个包含两个属性的对象：
    
    - `exact`：布尔类型，表示是否精确匹配，默认为 `true`。如果为 `true`，则只查找占位文本与给定文本完全相等的元素；如果为 `false`，则匹配部分文本也可以。
        
    - `normalizer`：函数类型，用于对待测元素的占位文本和给定文本进行规范化处理。这可以用于去除文本中的空格或其他格式化操作。
        

函数的返回值类型为 `HTMLElement`，表示找到的具有匹配占位文本的元素。
请注意，如果你使用 `screen` 对象进行测试，可以省略 `container` 参数，直接使用 `screen.getByPlaceholderText` 进行调用。


# Firing Events

```jsx
// <button>Submit</button>
fireEvent(  
  getByText(container, 'Submit'),
  new MouseEvent('click', {
    bubbles: true, 
    cancelable: true,  }),)
```

## `fireEvent[eventName]`[​](https://testing-library.com/docs/dom-testing-library/api-events#fireeventeventname "Direct link to heading")

```jsx
fireEvent[eventName](node: HTMLElement, eventProperties: Object)
```

Convenience methods for firing DOM events. Check out [src/event-map.js](https://github.com/testing-library/dom-testing-library/blob/master/src/event-map.js) for a full list as well as default `eventProperties`.

**target**: When an event is dispatched on an element, the event has the subjected element on a property called `target`. As a convenience, if you provide a `target` property in the `eventProperties` (second argument), then those properties will be assigned to the node which is receiving the event.

This is particularly useful for a change event:

以下是关于事件的代码示例：
```javascript
fireEvent.change(getByLabelText(/username/i), { target: { value: 'a' } });
// 注意：尝试手动设置 HTMLInputElement 的 files 属性会导致错误，因为 files 属性是只读的。
// 这个特性通过使用 Object.defineProperty 来绕过这个问题。
fireEvent.change(getByLabelText(/picture/i), {
  target: {
    files: [
      new File(['(⌐□_□)'], 'chucknorris.png', { type: 'image/png' }),
    ],
  },
});
// 注意：当在类型为 "date" 的输入框上触发 change 事件时，'value' 属性必须使用 ISO 8601 格式。
// 否则，元素将不能正确反映更改后的值。
// 无效示例：
fireEvent.change(input, { target: { value: '24/05/2020' } });
// 有效示例：
fireEvent.change(input, { target: { value: '2020-05-24' } });
```
上述代码演示了使用 `fireEvent.change` 函数触发不同类型的事件，并传递不同的 `target` 对象来模拟事件的触发。
第一个示例中，通过 `getByLabelText` 获取到带有匹配标签文本的元素，然后使用 `fireEvent.change` 函数模拟对该元素的值进行改变，将值设为 'a'。
第二个示例中，通过 `getByLabelText` 获取到带有匹配标签文本的元素，然后使用 `fireEvent.change` 函数模拟对该元素的文件选择，将一个新的文件对象赋值给 `files` 属性。
最后两个示例中，针对不同类型的输入框，通过 `fireEvent.change` 函数模拟对输入框的值进行改变。注意，对于类型为 "date" 的输入框，要使用 ISO 8601 格式的日期来触发 change 事件。
使用 `fireEvent.change` 函数可以方便地模拟各种事件，并验证组件对事件的响应情况。




**dataTransfer**: Drag events have a `dataTransfer` property that contains data transferred during the operation. As a convenience, if you provide a `dataTransfer` property in the `eventProperties` (second argument), then those properties will be added to the event.

This should predominantly be used for testing drag and drop interactions.
以下是一个关于拖放事件的代码示例：
```javascript
fireEvent.drop(getByLabelText(/drop files here/i), {
  dataTransfer: {
    files: [
      new File(['(⌐□_□)'], 'chucknorris.png', { type: 'image/png' }),
    ],
  },
});
```
上述代码演示了如何使用 `fireEvent.drop` 函数模拟拖放事件。
通过 `getByLabelText` 获取到具有匹配标签文本的元素，然后使用 `fireEvent.drop` 函数模拟在该元素上执行拖放操作。在 `dataTransfer` 属性中，可以提供要传递的文件列表，这里使用了一个包含一个文件对象的数组。
使用 `fireEvent.drop` 函数可以方便地测试拖放操作的交互行为和组件的响应情况。


**Keyboard events**: There are three event types related to keyboard input - `keyPress`, `keyDown`, and `keyUp`. When firing these you need to reference an element in the DOM and the key you want to fire.

以下是关于键盘事件的代码示例：
```javascript
fireEvent.keyDown(domNode, { key: 'Enter', code: 'Enter', charCode: 13 });
fireEvent.keyDown(domNode, { key: 'A', code: 'KeyA' });
```
上述代码演示了如何使用 `fireEvent.keyDown` 函数模拟键盘按下事件。
通过传递 `domNode`（DOM 节点）和键盘事件的属性对象，可以模拟在指定的 DOM 节点上按下键盘按键。在第一个示例中，按下了 Enter 键，属性对象中的 `key`、`code` 和 `charCode` 属性都设置为与 Enter 键对应的值。在第二个示例中，按下了 A 键，同样设置了相关的属性值。
使用 `fireEvent.keyDown` 函数可以方便地模拟键盘事件，测试组件对键盘输入的响应情况。

You can find out which key code to use at [https://www.toptal.com/developers/keycode](https://www.toptal.com/developers/keycode).

## `createEvent[eventName]`[​](https://testing-library.com/docs/dom-testing-library/api-events#createeventeventname "Direct link to heading")

```jsx
createEvent[eventName](node: HTMLElement, eventProperties: Object)
```

Convenience methods for creating DOM events that can then be fired by `fireEvent`, allowing you to have a reference to the event created: this might be useful if you need to access event properties that cannot be initiated programmatically (such as `timeStamp`).

 以下是一个使用 `createEvent` 函数创建事件对象的示例:
```javascript
const myEvent = createEvent.click(node, { button: 2 });
fireEvent(node, myEvent);
// myEvent.timeStamp 可以像其他属性一样访问
// 注意:对 `createEvent` 创建的事件的访问基于原生事件 API,
// 因此,HTMLEvent 对象的原生属性(例如 `timeStamp`、`cancelable`、`type`)
// 应该使用 Object.defineProperty 来设置。 
// 有关更多信息,请参阅:https://developer.mozilla.org/en-US/docs/Web/API/Event
```
上述代码演示了如何使用 `createEvent` 函数创建事件对象,然后使用 `fireEvent` 函数触发该事件。
首先,通过调用 `createEvent.click(node, { button: 2 })` 创建一个点击事件对象,其中 `button` 属性的值设置为 2。这将返回一个事件对象,这里命名为 `myEvent`。
然后,使用 `fireEvent(node, myEvent)` 函数在 `node` 元素上触发 `myEvent` 事件对象。
请注意,通过 `createEvent` 创建的事件对象基于原生事件 API,因此需要使用 `Object.defineProperty` 来设置原生事件属性,如 `timeStamp`、`cancelable` 和 `type` 等。
使用 `createEvent` 和 `fireEvent` 函数的组合,可以创建自定义的事件对象并触发事件,以测试组件对特定事件属性的响应情况。这为事件模拟和测试提供了更大的灵活性。

You can also create generic events:

 以下是一个使用 `createEvent` 模拟 input 事件的示例:
```js
// 在文件输入框上模拟 'input' 事件
fireEvent(
  input,
  createEvent('input', input, {
    target: { files: inputFiles },
    ...init
  })
);
```
上述代码通过 `createEvent` 函数创建一个 'input' 事件,并在一个文件输入框元素上触发该事件。
`createEvent` 的第一个参数是事件类型 'input',第二个参数是事件目标元素 input,第三个参数是事件属性对象。
在事件属性对象中,设置了 `target.files` 为 `inputFiles` 变量,来模拟选择了文件。同时可以通过 `...init` 传递其他需要的事件属性。
最后,使用 `fireEvent` 触发在 input 元素上创建的 'input' 事件。
这样可以方便地模拟文件选择的 input 事件,测试组件对文件选择的响应。

## Using Jest Function Mocks[​](https://testing-library.com/docs/dom-testing-library/api-events#using-jest-function-mocks "Direct link to heading")

[Jest's Mock functions](https://jestjs.io/docs/en/mock-functions) can be used to test that a component will call its bound callback in response to a particular event.

- React

 这是一个使用 Jest 模拟函数测试 React 组件点击回调的示例:
```jsx
import { render, screen, fireEvent } from '@testing-library/react';

const Button = ({ onClick, children }) => (
  <button onClick={onClick}>{children}</button>
);
test('calls onClick prop when clicked', () => {
  const handleClick = jest.fn();
  
  render(<Button onClick={handleClick}>Click Me</Button>);
  
  fireEvent.click(screen.getByText(/click me/i));
  
  expect(handleClick).toHaveBeenCalledTimes(1);
});
```
在这个示例中,我们渲染了一个 Button 组件,它接受 onClick 回调函数作为 props。
使用 Jest 的 jest.fn() 来创建一个模拟函数 handleClick。
然后通过 fireEvent.click 来模拟点击事件,点击带有 "Click Me" 文本的按钮。
最后,通过 expect 来断言 handleClick 这个模拟函数是否被调用了一次。
这样可以方便地测试组件的点击事件是否正确调用了传递的回调函数。

该网页是 `@testing-library/dom` 库的官方文档中关于事件（events）的部分，提供了与事件相关的 API 和用法说明。
以下是该网页内容的概要：
1. **[`fireEvent`](https://testing-library.com/docs/dom-testing-library/api-events/#fireevent)**：用于触发各种事件的函数，例如点击、输入、提交等。
2. **[`waitFor`](https://testing-library.com/docs/dom-testing-library/api-events/#waitfor)**：用于等待事件触发或状态变化的函数，可以用于在测试中等待异步事件的完成。
3. **[`userEvent`](https://testing-library.com/docs/dom-testing-library/api-events/#userevent)**：提供了更逼真的用户交互模拟，如键盘输入、鼠标悬停、选择选项等。
4. **[`mockEventSource`](https://testing-library.com/docs/dom-testing-library/api-events/#mockeventsource)**：模拟事件源，用于测试与事件源交互的组件。
5. **[`Event`](https://testing-library.com/docs/dom-testing-library/api-events/#event)**：关于事件对象的一些说明，如事件类型、属性和方法等。
6. **[`SyntheticEvent`](https://testing-library.com/docs/dom-testing-library/api-events/#syntheticevent)**：关于合成事件对象的一些说明，如常用的事件属性和方法等。
7. **[`fireEvent.*`](https://testing-library.com/docs/dom-testing-library/api-events/#fireevent-namespace-functions)**：各种特定事件的 `fireEvent` 命名空间函数，如 `fireEvent.click`、`fireEvent.change` 等。
8. **[`userEvent.*`](https://testing-library.com/docs/dom-testing-library/api-events/#userevent-namespace-functions)**：各种特定用户交互模拟的 `userEvent` 命名空间函数，如 `userEvent.type`、`userEvent.hover` 等。
该网页提供了详细的文档和示例，帮助开发人员在测试中模拟和处理各种事件。通过使用这些事件相关的 API，可以更准确地测试交互行为和组件的状态变化。

 ```js
function waitFor<T>(
  callback: () => T | Promise<T>, 
  options?: {
    container?: HTMLElement
    timeout?: number
    interval?: number
    onTimeout?: (error: Error) => Error
    mutationObserverOptions?: MutationObserverInit
  }
): Promise<T>
```
这个是 `waitFor` 函数的类型定义,它可以用来等待回调函数的结果。
`callback` 参数是一个函数,该函数的返回值可以是 Promise 或非 Promise。
`options` 是可选的参数,可以设置:
- `container`: 限制在某个容器内查询元素
- `timeout`: 超时时间 
- `interval`: 轮询间隔
- `onTimeout`: 超时后的回调函数
- `mutationObserverOptions`: 观察 DOM 变动的配置
`waitFor` 函数返回一个 Promise,Promise 的 resolve 值就是 `callback` 的返回值。
这个函数常用于在测试中等待某些异步操作完成,比如等待元素呈现、等待状态更新等。利用回调函数和可选的配置参数,可以实现灵活的等待机制。

Here is an example where the promise resolves because the element is removed:

 这是一个使用 `waitForElementToBeRemoved` 的示例:
```js
const el = document.querySelector('div.getOuttaHere');
waitForElementToBeRemoved(document.querySelector('div.getOuttaHere')).then(() => 
  console.log('Element no longer in DOM')
);
el.setAttribute('data-neat', true);
// 其他变动会被忽略...
el.parentElement.removeChild(el); 
// 日志打印 'Element no longer in DOM'
```
这里选中了一个 `div.getOuttaHere` 元素,然后使用 `waitForElementToBeRemoved` 来等待这个元素被移除。
`waitForElementToBeRemoved` 返回一个 Promise,当这个元素被移除时 Promise 会 resolve。
然后我们在这个元素上设置了一个属性,不过这个变动会被忽略。
最后使用 `parentElement.removeChild` 把这个元素从 DOM 中删除。
这个时候 `waitForElementToBeRemoved` 返回的 Promise 会 resolve,然后打印日志:'Element no longer in DOM'。
这样可以实现等待特定元素被删除的效果,在测试中可以用来确保某些异步操作导致的 DOM 更新完成。

`waitForElementToBeRemoved` throws an error if the first argument is `null` or an empty array:

 ```js
waitForElementToBeRemoved(null).catch(err => 
  console.log(err) 
);
// Error: Expected to receive an element or NodeList but got: null
waitForElementToBeRemoved(queryByText(/not here/i)).catch(err =>  
  console.log(err)
); 
// Error: Unable to find an element with the text: /not here/i
waitForElementToBeRemoved(queryAllByText(/not here/i)).catch(err =>   
  console.log(err)
);
// Error: Unable to find any elements with the text: /not here/i
waitForElementToBeRemoved(() => getByText(/not here/i)).catch(err =>    
  console.log(err)  
);
// Error: Unable to find an element with the text: /not here/i
// Error: The element(s) given to waitForElementToBeRemoved are already removed. waitForElementToBeRemoved requires that the element(s) exist(s) before waiting for removal.
```
这些示例展示了不同参数使用 `waitForElementToBeRemoved` 时产生的错误信息。
- 传入 null 会报错期望接收到元素或节点列表
- 使用查询不到的文本会报错找不到元素 
- 使用回调函数查询不到也会报相应错误
- 如果元素本来就已经被移除了,会报元素已被移除的错误
这样可以帮助我们 debugging 并理解 `waitForElementToBeRemoved` 的使用限制。

## Considerations for fireEvent

## Interactions vs. events

- fireEvent.mouseOver(element)
- fireEvent.mouseMove(element)
- fireEvent.mouseDown(element)
- element.focus() (if that element is focusable)
- fireEvent.mouseUp(element)
- fireEvent.click(element)

## Using Fake Timers

In some cases, when your code uses timers (`setTimeout`, `setInterval`, `clearTimeout`, `clearInterval`), your tests may become unpredictable, slow and flaky.

 这是在Jest中使用假定时器(fake timers)的示例代码:
在每个测试开始前,使用`jest.useFakeTimers()`来启用假定时器。这将替换掉`setTimeout`,`setInterval`,`clearTimeout`, `clearInterval`等方法的默认实现,这样定时器可以被随意控制而不会真正等待时间流逝。
```jsx
// 在每个测试开始前启用假定时器
beforeEach(() => {
  jest.useFakeTimers(); 
});
```
在每个测试结束后,使用`jest.runOnlyPendingTimers()`来执行所有挂起的定时器,然后使用`jest.useRealTimers()`来恢复真实定时器的实现。
```jsx
// 在每个测试结束后执行pending定时器并恢复真实定时器
afterEach(() => {
  jest.runOnlyPendingTimers();
  jest.useRealTimers();
});
```
这样可以在测试中自由控制时间的流逝,从而测试那些依赖定时器的代码逻辑。并且在测试结束后恢复正常的定时器行为。
jest.runOnlyPendingTimers()会先运行当前pending状态的定时器,清空定时器列表后再切换到真实定时器jest.useRealTimers(),避免真实定时器被pending定时器影响。
这是Jest中模拟定时器的常用方式,可以很好地测试异步代码。


```jsx
import {getRoles} from '@testing-library/dom'

const nav = document.createElement('nav')
nav.innerHTML = `
<ul>
  <li>Item 1</li>
  <li>Item 2</li>
</ul>`
console.log(getRoles(nav))

// Object {
//   navigation: [<nav />],
//   list: [<ul />],
//   listitem: [<li />, <li />]
// }
```


```jsx
//test-utils.js
const domTestingLib = require('@testing-library/dom')
const {queryHelpers} = domTestingLib

export const queryByTestId = queryHelpers.queryByAttribute.bind(
  null,
  'data-test-id',
)
export const queryAllByTestId = queryHelpers.queryAllByAttribute.bind(
  null,
  'data-test-id',
)

export function getAllByTestId(container, id, ...rest) {
  const els = queryAllByTestId(container, id, ...rest)
  if (!els.length) {
    throw queryHelpers.getElementError(
      `Unable to find an element by: [data-test-id="${id}"]`,
      container,
    )
  }
  return els
}

export function getByTestId(container, id, ...rest) {
  // result >= 1
  const result = getAllByTestId(container, id, ...rest)
  if (result.length > 1) {
    throw queryHelpers.getElementError(
      `Found multiple elements with the [data-test-id="${id}"]`,
      container,
    )
  }
  return result[0]
}

// re-export with overrides
module.exports = {
  ...domTestingLib,
  getByTestId,
  getAllByTestId,
  queryByTestId,
  queryAllByTestId,
}
```

 这段代码实现了基于 `data-test-id` 属性的查询助手,可以用来查找测试环境中的元素。
它首先导入了 `@testing-library/dom` 库,并从中获取 `queryHelpers`。
然后定义了 `queryByTestId` 和 `queryAllByTestId` 方法,它们调用 `queryHelpers` 中的 `queryByAttribute` 和 `queryAllByAttribute` 方法,以 `data-test-id` 作为属性进行查询。
接下来定义了 `getByTestId` 和 `getAllByTestId` 方法,用于获取单个或多个 `data-test-id` 匹配的元素。在获取不到元素时,它们会抛出错误。
最后通过重新导出的方式,包装了 `@testing-library/dom` 库,以包含自定义的基于 `data-test-id` 的查询助手。
这样可以非常方便地在测试环境中标记元素,并通过 `data-test-id` 属性精确查询。这种方式可以避免测试对内部实现细节的过度依赖。
在测试中,可以通过 `getByTestId`、`getAllByTestId` 等 helper 函数查询元素,使测试代码更简洁清晰。

 ```js
// 查询工具:
import {
  getByLabelText, 
  getByText,
  getByTestId,
  queryByTestId,
  // 提示:所有查询也在一个对象“queries”上暴露,你也可以在这里导入
  waitFor,  
} from '@testing-library/dom'
// 添加特殊的匹配器,如toHaveTextContent
import '@testing-library/jest-dom'  
function getExampleDOM() {
  // 这只是一个设置一些DOM的原始示例
  // 我们可以和它交互。用你选择的UI框架替换它
  const div = document.createElement('div') 
  div.innerHTML = `
    <label for="username">用户名</label>
    <input id="username" />
    <button>打印用户名</button>
  `
  const button = div.querySelector('button')
  const input = div.querySelector('input')
  button.addEventListener('click', () => {
    // 假装这是发出一个服务器请求,所以它是异步的
    // (你会想在单元测试中模拟这个想象中的请求)...
    setTimeout(() => {
      const printedUsernameContainer = document.createElement('div')
      printedUsernameContainer.innerHTML = `
        <div data-testid="printed-username">${input.value}</div>
      `
      
      div.appendChild(printedUsernameContainer)
    }, Math.floor(Math.random() * 200))
  })
  return div
}
test('一些例子', async () => {
  const famousProgrammerInHistory = 'Ada Lovelace'
  const container = getExampleDOM()
  // 通过标签文本获取表单元素
  // 如果找不到会抛出错误(无障碍性优先!)
  const input = getByLabelText(container, '用户名')
  input.value = famousProgrammerInHistory
  // 像真正的用户一样根据文本获取元素
  getByText(container, '打印用户名').click()
  await waitFor(() =>
    expect(queryByTestId(container, 'printed-username')).toBeTruthy(),
  )
  
  // getByTestId 和 queryByTestId 是获取元素的后门
  // 通过测试id(也可以尝试通过文本获取这个元素)
  expect(getByTestId(container, 'printed-username')).toHaveTextContent(
    famousProgrammerInHistory
  )
  
  // jest快照与常规DOM节点非常配!
  expect(container).toMatchSnapshot()
})
```
这里演示了一些使用`@testing-library`查询和匹配DOM的示例,包括:

- 根据标签文本查询
- 根据元素文本查询
- 使用`getByTestId/queryByTestId`根据`data-testid`查询
- 配合`waitFor`处理异步
- 使用`jest-dom`的匹配器断言元素属性
- 创建DOM快照

这样可以编写出非侵入式、关注可访问性的测试,测试代码会模拟用户交互。

[Cheatsheet | Testing Library (testing-library.com)](https://testing-library.com/docs/dom-testing-library/cheatsheet)

## React Testing Library


 ```jsx
// import dependencies
import React from 'react';
// import API mocking utilities from Mock Service Worker
import { rest } from 'msw'; 
import { setupServer } from 'msw/node';
// import react-testing methods
import { render, fireEvent, screen } from '@testing-library/react';
// add custom jest matchers from jest-dom
import '@testing-library/jest-dom';
// the component to jest
import Fetch from '../fetch';
// 创建一个msw server to mock an API request that our tested component makes
// declare which API requests to mock
const server = setupServer(
  // capture "GET /greeting" requests
  rest.get('/greeting', (req, res, ctx) => {
  // respond using a mocked JSON body
    return res(ctx.json({greeting: 'hello there'})); 
  })
);

// establish API mocking before all tests
// 启动msw server
beforeAll(() => server.listen());
// 每个测试后重置处理程序 reset any request handlers that are declared as a part of our tests
// (i.e. for testing one-time error scenarios)
afterEach(() => server.resetHandlers());  
// 关闭msw server  clean up once the tests are done
afterAll(() => server.close());
test('loads and displays greeting', async () => {
  render(<Fetch url="/greeting" />);
  
  // 模拟点击按钮
  fireEvent.click(screen.getByText('Load Greeting'));
  
  // 等待标题出现
  await screen.findByRole('heading');
  // 断言页面内容 
  expect(screen.getByRole('heading')).toHaveTextContent('hello there');
  expect(screen.getByRole('button')).toBeDisabled();
});
test('handles server error', async () => {
  // 模拟服务器报错 Arrange
  server.use(
    //override the the initial "GET /greeing" request handler
    // to return a 500 Server Error
    rest.get('/greeting', (req, res, ctx) => {
      return res(ctx.status(500));
    })
  );
  render(<Fetch url="/greeting" />);
  fireEvent.click(screen.getByText('Load Greeting'));
  // 等待警告出现 Act
  await screen.findByRole('alert');
  // 断言页面内容 Assert
  expect(screen.getByRole('alert')).toHaveTextContent('Oops, failed to fetch!');
  expect(screen.getByRole('button')).not.toBeDisabled();  
});
```
这是使用msw和react testing library模拟API调用进行组件测试的示例。通过msw服务器可以拦截请求,模拟不同响应测试组件的不同状态。配合queries, waitFor, fireEvent等可以实现端到端的UI交互测试。







```js
#index.js
const root = ReactDOM.createRoot(document.getElementById('root'))
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
)

```

```js
# App.js
import React, {useState, useEffect} from 'react'

export const App = () =>{
  const [users, setUsers] = useState(null)
  const [error, setError] = useState(null)

  useEffect(()=>{
    const fetchAllUsers = async()=>{
      try{
        const response = await fetch('https://jsonplaceholder.typicode.com/users')
        const data = await response.json()
        setUsers(data)
      } catch (err) {
        setError('Something went wrong!')
      }
    }
    fetchAllUsers()
  },[])
  
  return (
  <>
    <h1> List of Users</h1>
    {error && <div>{error}</div>}
    {users ? (
      <ul>
        {users.map((user)=>(
          <li key={user.id}>{user.name}</li>
        ))}
       </ul> 
       ) : (
       <p>No users found</p>
      )}
    </>
  )
}
```

```js
#test/App.test.js
import React from 'react'
import {render, screen} from '@testing-library/react'

import {App} from 'src/App.js'

describe('App',()=>{
  beforeEach(()=>{
    fetchMock.resetMocks()
  })
test('renders users when API call succeeds', async ()=>{
  const fakeUsers = [
    {id: 1, name:'Joe'},
    {id: 2, name:'Tony'},
  ]
  fetchMock.mockResolvedValue({status:200, json: jest.fn(()=>fakeUsers)})

  render(<App />)

  expect(screen.getByRole('heading')).toHaveTextContent('List of Users')
  
  expect(await screen.findByText('Joe')).toBeInTheDocument()
  expect(await screen.findByText('Tony')).toBeInTheDocument()

  expect(screen.queryByText('No users found')).not.toBeInTheDocument()
})
test('renders error when API call fails', async()=>{})
})





```