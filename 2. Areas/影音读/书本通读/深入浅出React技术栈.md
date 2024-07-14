---
aliases:

---
20230722 1431
links:
title:
origin:
tags: #flashcards #todo #Current 

只要熟悉原生 JavaScript 并了解重要概念后，就可以很容易上手 React 应用开发。

![[assets/img/深入浅出React技术栈/IMG-深入浅出React技术栈-20240714124854181.png]]

它最大的好处其实还在于方便和其他平台集成，比如 react-native 是基于 Virtual DOM 渲染出原生控件，因为 React 组件可以映射为对应的原生控件。在输出的时候，是输出 Web DOM，还是 Android 控件，还是 iOS 控件，就由平台本身决定了。因此，react-native 有一个口号——Learn Once，Write Anywhere。

而函数式编程，对应的是声明式编程，它是人类模仿自己逻辑思考方式发明出来的。声明式编程的本质是 lambda 演算1 。试想当我们操作数组的每个元素并返回一个新数组时，如果是计算机的思考方式，则是需要一个新数组，然后遍历原数组，并计算赋值；如果是人的思考方式，则是构建一个规则，这个过程就变成构建一个 `f` 函数作用在数组上，然后返回新数组。这样，计算可以被重复利用。

在 React 中创建的虚拟元素可以分为两类，DOM 元素（DOM element）与组件元素（component element），分别对应着原生 DOM 元素与自定义元素，而 JSX 与创建元素的过程有着莫大的关联。

Button 方法其实也可以作为元素而存在，方法名对应了 DOM 元素类型，参数对应了 DOM 元素属性，那么它就具备了元素的两大必要条件，这样构建的元素就是自定义类型的元素，或称为组件元素。



```jsx
const DeleteAccount = () => (
  <div>
    <p>Are you sure?</p>
    <DangerButton>Confirm</DangerButton>
    <Button color="blue">Cancel</Button>
  </div>
);
```
我们试着将 DeleteAccount 组件通过 Babel 转译成 React 可以执行的代码：
```js
var DeleteAccount = function DeleteAccount() {
  return React.createElement(
    'div',
    null,
    React.createElement(
      'p',
      null,
      'Are you sure?'
    ),
    React.createElement(
      DangerButton,
      null,
      'Confirm'
    ),
    React.createElement(
      Button,
      { color: 'blue' },
      'Cancel'
    )
  );
};
```

