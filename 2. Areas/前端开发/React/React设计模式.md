---
aliases: 
date: 
url: https://www.bilibili.com/video/BV18a411C74j/?p=6&spm_id_from=pageDriver&vd_source=7038f96b6bb3b14743531b102b109c43
page-title: 
tags:
  - "#算法"
established: 2023-10-22T12:01:00
updated: 
isFinished: false
---

![React: 设计模式【中英字幕 React: Design Patterns】_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV18a411C74j/?spm_id_from=333.788.recommend_more_video.1&vd_source=7038f96b6bb3b14743531b102b109c43)
![[assets/img/React设计模式/IMG-React设计模式-20240714124854073.png]]
![[IMG-React设计模式-20240719192334838.png]]

![[IMG-React设计模式-20240719192335175.png]]
# 1. DESIGN PATTERNS
![[IMG-React设计模式-20240719192335416.png]]

![[IMG-React设计模式-20240719192335774.png]]
The patterns we cover here are effective solutions to some extremely common challenges in React.
![[IMG-React设计模式-20240719192336073.png]]
# 2. LAYOUT component

![[IMG-React设计模式-20240719192336365.png]]

![[IMG-React设计模式-20240719192336996.png]]

![[IMG-React设计模式-20240719192337294.png]]


# 3.  Split-screen component

![[IMG-React设计模式-20240719192337462.png]]

![[IMG-React设计模式-20240719192337624.png]]

![[IMG-React设计模式-20240719192337809.png]]

![[IMG-React设计模式-20240719192337997.png]]

![[IMG-React设计模式-20240719192339166.png]]


# 4.  Split-screen component improvements

![[IMG-React设计模式-20240719192339729.png]]

![[IMG-React设计模式-20240719192341330.png]]
# 5. Lists and List Items

![[IMG-React设计模式-20240719192342330.png]]

# 6. Creating Different List Types


![[IMG-React设计模式-20240719192342741.png]]
这段代码定义了一个React组件 `RegularList`，它接受一些属性并渲染一个包含列表项的列表。让我为您解释一下这段代码的主要部分：

- `RegularList` 是一个函数式组件，接受一些属性作为参数。
- `items` 属性是一个包含列表项的数组，它将在列表中渲染。
- `resourceName` 属性是一个字符串，表示每个列表项的资源名称。
- `itemComponent` 属性是一个React组件，用于渲染每个列表项。

在组件的返回部分，它使用了React的**fragment**（`<></>`）来包装多个子元素。然后，它使用`map`函数遍历 `items` 数组，并为每个列表项渲染一个 `<div>` 元素。

在每个 `<div>` 元素内部，它显示一个标题 `<h3>`，标题显示了列表项的序号（从1开始）。

接着，它使用 `ItemComponent` 渲染列表项。通过将列表项作为属性传递给 `ItemComponent`，可以让 `ItemComponent` 访问和显示与每个列表项相关的信息。

最终，您可以将此组件用于渲染不同类型的列表，只需传递不同的属性和 `ItemComponent`。这使得它非常灵活，适用于各种列表渲染需求。


```
itemComponent: ItemComponent 和 <ItemComponent {...{ [resourceName]: item }} /> 部分没有看懂
```


1. `itemComponent: ItemComponent`：这是组件的一个属性，其中 `itemComponent` 是属性名称，而 `ItemComponent` 是属性的值。在这个上下文中，`itemComponent` 期望接收一个React组件作为值。这个属性用于指定要用来渲染每个列表项的React组件。

2. `<ItemComponent {...{ [resourceName]: item }} />`：这是在组件中的实际渲染部分。在这里，`ItemComponent` 是一个React组件，它将用于渲染每个列表项。这行代码的作用是渲染 `ItemComponent` 并传递一个属性给它。

   - `{...}`：这是JavaScript的对象扩展运算符，它允许您将一个对象的所有属性和值解构到一个新对象中。
   - `[resourceName]: item`：这是一个JavaScript对象的属性设置语法。它创建一个具有属性名称 `resourceName`（来自组件属性）和属性值 `item`（来自列表中的当前项）的新对象。

   因此，`<ItemComponent {...{ [resourceName]: item }} />` 的目的是将 `item` 作为属性传递给 `ItemComponent`，属性的名称是 `resourceName`，这意味着在 `ItemComponent` 中，您可以通过 `props.resourceName` 来访问 `item` 的值。

   这种方法使得 `RegularList` 组件可以灵活地使用不同的 `ItemComponent` 来渲染不同类型的列表项，并将相应的数据传递给 `ItemComponent`。例如，如果 `resourceName` 是 "user"，那么 `ItemComponent` 可以在内部访问 `props.user` 来获取每个列表项的数据。

![[IMG-React设计模式-20240719192343003.png]]


# 7. Modal Components

![[IMG-React设计模式-20240719192343284.png]]

![[IMG-React设计模式-20240719192343735.png]]

![[IMG-React设计模式-20240719192343926.png]]

![[IMG-React设计模式-20240719192344215.png]]

![[IMG-React设计模式-20240719192344416.png]]


## Styled-component 

`import styled from 'styled-components'` 是导入React中用于创建样式化组件的 `styled-components` 库。`styled-components` 是一种在React中创建和应用CSS样式的强大方法，它使用标签模板字符串语法来定义和附加样式到组件。

以下是如何使用 `styled-components` 创建和应用样式的基本示例：

```
npm install styled-components
```

```javascript
import styled from 'styled-components';

// 创建一个样式化组件
const Button = styled.button`
  background-color: blue;
  color: white;
  font-size: 16px;
  padding: 10px 20px;
`;

// 在React组件中使用样式化组件
function App() {
  return (
    <div>
      <Button>Click me</Button>
    </div>
  );
}
```

`styled-components` 的强大之处在于，您可以将CSS样式与React组件紧密集成，以创建可复用的、模块化的样式化组件，而不必担心全局污染或类名冲突问题。这使得它成为在React应用程序中管理样式的流行工具之一。


# 8. Container Component

![[IMG-React设计模式-20240719192344508.png]]

![[IMG-React设计模式-20240719192344598.png]]

![[IMG-React设计模式-20240719192344693.png]]

![[IMG-React设计模式-20240719192344772.png]]



# 9. Server Instructions



# 10. CurrentUserLoader Component

# 11. UserLoader Component

# 12. ResourceLoader Component

# 13. Loading Data from LocalStorage

# 14. Controlled vs Uncontrolled Component

![[IMG-React设计模式-20240719192344881.png]]

# 15. Controlled modals
# 16. Uncontrolled onboarding flows
# 17. Collecting onboarding data
# 18. Controlled onboarding flows
# 19. What are higher-order components
# 20. Printing props with HOCs
# 21. Loading data with HOCs
# 22. Modifying data with HOCs
# 23. Creating forms with HOCs
# 24. Higher-order component improvements
# 25. What are custom Hooks gCyci
# 26. useCurrentUser Hook
# 27. useUser Hook
# 28. useResource Hook
# 29. useDataSource Hook
# 30. What is functional programming
# 31. Recursive components
# 32. Component composition
# 33. Partially applied components
