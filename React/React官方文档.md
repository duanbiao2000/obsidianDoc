---
aliases: 

---
20230715 1204
links: [ React文档](https://zh-hans.react.dev/learn/your-first-component)
title: React官方文档
origin:
tags: #flashcards 




你的 React 应用程序从“根”组件开始。通常，它会在启动新项目时自动创建。例如，如果你使用 [CodeSandbox](https://codesandbox.io/) 或 [Create React App](https://create-react-app.dev/)，根组件定义在 `src/App.js` 中。

如果使用 [Next.js](https://nextjs.org/) 框架，根组件定义在 `pages/index.js`中。
像 Next.js 这样的框架会做更多事情。与使用一个空白的 HTML 页面并让 React 使用 JavaScript “接手”管理页面不同，框架还会根据你的 React 组件自动生成 HTML。这使你的应用程序在加载 JavaScript 代码之前能够展示一些内容。

尽管如此，许多网站仅使用 React 来 [添加“交互性”](https://zh-hans.react.dev/learn/add-react-to-a-website)。它们有很多根组件，而不是整个页面的单个组件。你可以根据需要尽可能多或尽可能少地使用 React。

在 [Create React App](https://create-react-app.dev/) 中，你的应用应在 `src/App.js` 文件中定义。具体还需根据项目配置决定，有些根组件可能会声明在其他文件中。如果你使用的框架基于文件进行路由，如 Next.js，那你每个页面的根组件都会不一样。

组件的导出方式决定了其导入方式。当你用默认导入的方式，导入具名导出的组件时，就会报错。如下表格可以帮你更好地理解它们：

|语法|导出语句|导入语句|
|---|---|---|
|默认|`export default function Button() {}`|`import Button from './Button.js';`|
|具名|`export function Button() {}`|`import { Button } from './Button.js';`|

当使用默认导入时，你可以在 `import` 语句后面进行任意命名。比如 `import Banana from './Button.js'`，如此你能获得与默认导出一致的内容。相反，对于具名导入，导入和导出的名字必须一致。这也是为什么称其为 **具名** 导入的原因！
<!--SR:!2023-07-18,3,250-->

>**通常，文件中仅包含一个组件时，人们会选择默认导出，而当文件中包含多个组件或某个值需要导出时，则会选择具名导出。** 无论选择哪种方式，请记得给你的组件和相应的文件命名一个有意义的名字。我们不建议创建未命名的组件，比如 `export default () => {}`，因为这样会使得调试变得异常困难。
<!--SR:!2023-07-18,3,250-->

```js
const today = new Date();

function formatDate(date) {
  return new Intl.DateTimeFormat(
    'zh-CN',
    { weekday: 'long' }
  ).format(date);
}

export default function TodoList() {
  return (
    <h1>To Do List for {formatDate(today)}</h1>
  );
}
```
`To Do List for 星期六`

## 使用 “双大括号”：JSX 中的 CSS 和 对象 [](https://zh-hans.react.dev/learn/javascript-in-jsx-with-curly-braces#using-double-curlies-css-and-other-objects-in-jsx "Link for 使用 “双大括号”：JSX 中的 CSS 和 对象")

除了字符串、数字和其它 JavaScript 表达式，你甚至可以在 JSX 中传递对象。对象也用大括号表示，例如 `{ name: "Hedy Lamarr", inventions: 5 }`。因此，为了能在 JSX 中传递，你必须用另一对额外的大括号包裹对象：`person={{ name: "Hedy Lamarr", inventions: 5 }}`。

你可能在 JSX 的内联 CSS 样式中就已经见过这种写法了。React 不要求你使用内联样式（使用 CSS 类就能满足大部分情况）。但是当你需要内联样式的时候，你可以给 `style` 属性传递一个对象：
```js
export default function TodoList() {
	return (
		<ul style={{
			backgroundColor: 'black',
			color: 'pink'
		}}>
		<li>Improve the videophone</li>
		<li>Prepare aeronautics lectures</li>
		<li>Work on the alcohol-fuelled engine</li>
	);
}
```

```
- Improve the videophone
- Prepare aeronautics lectures
- Work on the alchohol-fuelled engine
```

#### 陷阱

内联 `style` 属性 使用驼峰命名法编写。例如，HTML `<ul style="background-color: black">` 在你的组件里应该写成 `<ul style={{ backgroundColor: 'black' }}>`。

## 摘要[](https://zh-hans.react.dev/learn/passing-props-to-a-component#recap "Link for 摘要")

- 要传递 props，请将它们添加到 JSX，就像使用 HTML 属性一样。
```js
//APP.js
import Avatar from './Avatar.js';

function Card({ children }) {
  return (
    <div className="card">
      {children}
    </div>
  );
}

export default function Profile() {
  return (
    <Card>
      <Avatar
        size={100}
        person={{ 
          name: 'Katsuko Saruhashi',
          imageId: 'YfeOqp2'
        }}
      />
    </Card>
  );
}



//Avarar.js
import { getImageUrl } from './utils.js';

export default function Avatar({ person, size }) {
  return (
    <img
      className="avatar"
      src={getImageUrl(person)}
      alt={person.name}
      width={size}
      height={size}
    />
  );
}


//utils.js
export function getImageUrl(person, size = 's') {
  return (
    'https://i.imgur.com/' +
    person.imageId +
    size +
    '.jpg'
  );
}
```
- 要读取 props，请使用 `function Avatar({ person, size })` 解构语法。
- 你可以指定一个默认值，如 `size = 100`，用于缺少值或值为 `undefined` 的 props 。
- 你可以使用 `<Avatar {...props} />` JSX 展开语法转发所有 props，但不要过度使用它！
- 像 `<Card><Avatar /></Card>` 这样的嵌套 JSX，将被视为 `Card` 组件的 `children` prop。
- Props 是只读的时间快照：每次渲染都会收到新版本的 props。
- 你不能改变 props。当你需要交互性时，你可以设置 state。

可以将带有 `children` prop 的组件看作有一个“洞”，可以由其父组件使用任意 JSX 来“填充”。你会经常使用 `children` prop 来进行视觉包装：面板、网格等等。
  
![A puzzle-like Card tile with a slot for "children" pieces like text and Avatar](https://zh-hans.react.dev/images/docs/illustrations/i_children-prop.png)






