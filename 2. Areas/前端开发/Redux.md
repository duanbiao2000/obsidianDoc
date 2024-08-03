---
aliases: null
theme: null
original: null
url: null
author: null
date created: 2024-08-03 11:28
date updated: 2024-08-03 11:28
type: null
high_priority: false
---

### 第三方数据流框架"课代表": 初探Redux

```
Redux是JavaScript状态容器, 它提供可供预测的状态管理.
```

- store是一个单一的数据源,而且是只读的
- action是对变化的描述

```jsx
const action={
  type:"ADD_ITEM",
  payload:'<li>text</li>'
}
```

- reducer 负责对变化进行分发和处理

---

### Redux是如何帮助React

Action->Reducer->Store(states)->View->Action
在Redux的整个工作过程中 ,数据流是严格单向的.

---
### 在编码的角度理解Redux工作流

使用createStore来完成store对象的创建

```jsx
//引入redux
import{createStore} from 'redux'
//创建store
const store = createStore(
  reducer,
  initial_state,
  applyMiddleware(
    middleware1,
    middleware2,
    ...)
);
```

reducer的作用是将新的state返回给store

```js
const reducer=(state,action)=>{
  //此处是各种各样的state处理逻辑
  return new_state
}
```

```js
//基于reducer创建state🤔
const store = createStore(reducer)
```

要想让State发生改变,就必须用正确的action来驱动这个改变

---

😋action的作用就是通知reducer"让改变发生"

```js
//使用dispatch派发action,action会进入到reducer里触发对应的更新
store.dispatch(action)
```


函数组件与类组件的对比:无关"优劣",只谈"不同"

- 类组件需要继承class,函数组件不需要
- 类组件可以访问生命周期方法,函数组件不能
- 类组件可以获取到实例化后的this,并基于这个this做各种各样的事情,而函数组件不可以.
- 类组件中可以定义并维护state(状态),而函数组件不可以

在React-Hooks出现之前的世界里,类组件的能力明显强于函数组件.

---

重新理解类组件:包裹在面向对象思想下的"重装战舰"

<font color="#d831a8">类组件:</font>
是面向对象编程思想的一种表征

<font color="#d831a8">封装:</font>将一类属性和方法,聚拢到一个Class里去.
![[assets/img/深入浅出React/IMG-深入浅出React-20240714124901200.png]]
对于解决许多问题来说,编写一个类组件实在是一个过于复杂的姿势,复杂的姿势必然带来高昂的理解成本.

开发者编写的逻辑在封装后是和组件粘在一起的,这就使得类组件内部的逻辑难以实现拆分和复用.
虽然强大,绝非万能.

---

`函数组件会捕获render内部的状态,这是两种组件最大的不同.`

类组件和函数组件之间,纵有千差万别但最不能被我们忽视掉的,是心智模式层面的差异.

面向对象和函数式编程思想之间的差异.

函数组件更加契合react框架的设计理念.

```jsx
UI = render(data)
或
UI = f(data)
```

==React组件本身的定位就是函数,一个吃进数据,吐出UI的函数.==

把声明式的代码转换为命令式的DOM操作,把数据层面的描述映射到用户可见的UI变化中去.

---

函数组件会捕获render内部的状态,这是两类组件最大的不同.

```js
class ProfilePage extends React.Component{
  showMessage=()=>{
    alter(
    'Followed'+this.props.user
    );
  };

  handleClick=()=>{
  setTimeout(this.showMessage,
    3000);
};

  render(){
    render<button onClick={this.handleClick}>Follow</button>;
  }

}
```

- 虽然props本身不可变的
- 但this却是可变的,this上的数据是可以被修改的.

通过setTimeout将预期中的渲染推迟了3秒,打破了this.props和渲染动作之间的这种时机上的关联.

---

```jsx
function ProfilePage(props){
  const showMessage=()=>{
    alert('Followed'+props.user);
  };
};

const handleClick=()=>{
  setTimeout(showMessage,3000);

return(
  <button onClick={handleClick}>Follow</button>
  );
}
```

"函数组件会捕获render内部的状态"  <=>  函数组件真正地数据和渲染绑定到了一起.
更有利于逻辑拆分与重用的组件表达形式.

---

## Hooks的本质: 一套能够使函数组件更强大,更灵活的"钩子"

- 如果说函数组件是一台轻巧的快艇
- 那么React-Hooks就是一个内容丰富的零部件箱.
- 允许你自由地选择和使用你需要的哪些能力

---

## 构建对React-Hooks的整体认知

对比类组件中的一"批"状态,在函数组件中state是一个状态(对应某一个属性).

```js
tihs.state{
  text:"初始文本",
  length: 10000,
  author: ["xiuyan","cuicui","yisi"]
}
```

---

useEffect():  允许函数组件执行副作用操作

- 在一定程度上弥补了生命周期的缺席
- 过去我们习惯放在componentDidMount,componentDidUpdate和componentWillUnmount三个生命周期里来做的事,现在可以放在useEffect里来做.

---

useEffect和生命周期之间的"替换"关系

```jsx
import React,{useState,useEffect} from 'react';
//定义函数组件
function IncreasingTodoList(){
  //创建count状态及其对应的状态修改函数
  const [count,setCount] = useState(0);

  //此处的定位与componentDidMount和componentDidUpdate相似
  useEffect(()=>{
    //每次count增加时,都增加对应的代办项
    const todoList=document.getElementById("todoList");
    const newItem=document.createElement("li");
    newItem.innerHTML=`我是第${count}个代办项`;
    todoList.append(newItem);
  });
  //编写UI逻辑
  return(
    <div>
      <p>当前共计{count}个todo item</p>
      <ul id="todoList"></ul>
      <button onClick={()=>setCount(count+1)}>点我增加一个代办项</button>
    </div>
  );
}
```

## ![[assets/img/深入浅出React/IMG-深入浅出React-20240714124901294.png]]

有时候,我们必须学会忘记旧的知识,才能够更好地拥抱新的知识.
useEffect是用于为函数组件引入副作用的钩子.
`useEffect(callBack,[])`

- 仅在挂在阶段执行一次的副作用: 传入回调函数,且这个函数的返回值不是一个函数,同时传入一个空数组.

```jsx
useEffect(()=>{
//这里是业务逻辑
},[])
```

- 仅在挂在阶段和卸载阶段执行的副作用:传入回调函数,且这个函数的返回值是一个函数,同时传入一个空数组.

```jsx
useEffect(()=>{
//这里时A的业务逻辑

//返回一个函数记为B (清除函数)
return ()=>{
  }
},[])
```

useEffect回调中返回的函数被称为"清除函数".

- 每一次渲染都触发,且卸载阶段也会被触发的副作用:传入回调函数,且这个函数的返回值是一个函数,同时不传第二个参数.

```jsx
useEffect(()=>{
//这里时A的业务逻辑

//返回一个函数记为B (清除函数)
return ()=>{
  }
})
```

- 根据一定的依赖条件来触发的副作用:传入回调函数,同时传入一个非空的数组.

```jsx
useEffect(()=>{
  //若xxx是一个函数,则xxx会在组件卸载时被触发
  return xxx
},[num1,num2,num3])
```

---

Why React-Hooks: Hooks如何帮助我们升级工作模式

1. 告别难以理解的Class
   - this
   - 生命周期
2. 解决业务逻辑难以拆分的问题
   - 逻辑曾经一度与生命周期耦合在一起
   - 按照逻辑关联拆分到不同的函数组件里
   - Hooks帮助实现业务逻辑的聚合,避免复杂的组件和冗余的代码
3. 使状态逻辑复用变得简单可行
   - 过去靠HOC和Render Props这些组件设计模式,在实现逻辑复用的同时,也破坏着组件的结构-"嵌套地狱"现象
4. 函数组件从设计思想上来看更加契合React的理念

---

保持清醒: Hooks 并非万能

- Hooks暂时还不能完全地为函数组件补全类组件的能力
- 轻量的基因不能很好地消化复杂
- Hooks在使用层面有着严格的规则约束

---

## 深入React-Hooks工作机制:"原则"的背后是"原理"

React-Hooks的使用原则

- 只在React函数中调用Hook
- 不要在循环,条件或嵌套函数中调用Hook-要确保Hooks在每次渲染时都保持同样的执行顺序
- 若不保证Hooks执行顺序,会带来什么麻烦?

---

## 从源码调用用流程看原理:Hooks的正常运作,在底层依赖于顺序链表

- 强调"源码流程" 而非 "源码"
- 目前仍然处于基础夯实阶段,盲目啃源码在这个阶段来说没有意义
- 原理 !== 源码,阅读源码只是掌握原理的一种手段. 而React-Hooks的源码链路相对来说比较长学习成本比较高,学习效果也难以保证.
- 不建议你在对Fiber底层实现没有认知的前提下,去和Hooks源码死磕.
- 重要的并不是去细抠每一行代码到底都做了什么,而是要搞清楚整个调用链路是什么样的

---

以useState为例,分析React-Hooks的调用链路

- useState->通过resolveDispatcher获取dispatcher->调用dispatcher.useState->*调用mountState->返回目标数组(如[state,useState])
- updateState 按顺序去遍历之前构建好的链表取出对应的数据信息进行渲染
- mountState(首次渲染) 构建链表并渲染
- updateState依次遍历链表并渲染

> hooks的渲染是通过"依次遍历"来定位每个hooks内容的.如果前后两次读到的链表在顺序上出现差异,那么渲染的结果自然是不可控的.
> Hooks的本质是链表.

---

## 历史长河中的DOM操作解决方案

#### 原生JS支配下的"人肉DOM"时期

前端页面"展示"的属性远远强于其"交互"的属性. JS只是辅助. 大量时间实现静态DOM,待一切结束后,再补充少量JS.

#### 解放生产力的先导阶段: jQuery时期

## 大量DOM操作需求带来前端工作开发工作量的激增

jQuery受限解决的就是"API不好使"这个问题
将DOM API封装为相对简单和优雅的形式,同时一口气做掉了跨浏览器兼容工作,并且提供了链式API调用,插件扩展等一系列能力用于进一步解放生产力.

#### 民智初启:早期模板引擎方案

jQuery并不能从根本上解决DOM操作量过大情况下的前端侧压力

> 模板引擎方案,正是"扫地机器人"的雏形

---

模板语法使用示例

这段代码似乎是使用了一种模板语言（可能是类似于 Liquid 或 Nunjucks）来生成 HTML 表格。

```html
<table>
  {% staff.forEach(function(person){ %}
  <tr>
    <td>{{ person.name }}</td>
    <td>{{ person.age }}</td>
  </tr>
  {% }); %}
</table>
```

在修正后的代码中，我们使用了双花括号 `{{ }}` 来表示模板变量
这段代码的目的是遍历一个名为 `staff` 的数组，并为每个员工（person）生成一个包含姓名和年龄的表格行。生成的 HTML 结构将包含一个 `<table>` 元素和多个 `<tr>` 元素，每个 `<tr>` 元素包含两个 `<td>` 元素，用于展示员工的姓名和年龄。
需要注意的是，这段代码仅展示了模板的逻辑部分，实际的渲染过程需要使用相应的模板引擎来解析和渲染模板。具体的实现可能会根据使用的模板引擎和上下文有所不同。

```js
//数据和模板融合初HTML代码
var targetDOM = template({data:person})
//添加到页面中去
document.body.appendChild(targetDOM)
```

1. 读取HTML模板并解析它,分离出其中的JS信息
2. 将解析出的内容拼接成字符串,动态生成JS代码
3. 运行动态生成的JS代码,吐出"目标HTML"
4. 将"目标HTML"赋值给innerHTML,触发渲染流水线,完成真实DOM的渲染

## 使用模板引擎方案来渲染数据需要关注的仅仅是数据和数据变化本身.

模板引擎实际的应用场景: "实现高效的字符串拼接"这一点上,因此不能指望它去做太复杂的事情.

- 性能上也并不尽如人意
- 本课时"模板引擎"概念,指的是虚拟DOM思想推而广之以前,相对原始的一类模板引擎.
- 和React"数据驱动视图"的思想如出一辙.

## ![[assets/img/深入浅出React/IMG-深入浅出React-20240714124903188.png]]

![[assets/img/深入浅出React/IMG-深入浅出React-20240714124905011.png]]

- 用函数名指代过程更专业
- 虚拟DOM和Redux一样,不依附于任何具体的框架
- 学习React必须了解虚拟DOM

<https://github.com/Matt-Esch/virtual-dom>

- 开发者体验:研发体验/研发效率(虚拟DOM)
- 性能问题属于前端领域复杂度比较高的问题
- 量化性能的时候要结合各种要素来作分情况的讨论

---

## 全量更新 VS 差量更新

![[assets/img/深入浅出React/IMG-深入浅出React-20240714124906242.png]]
特例: 数据内容变化非常大(或者说整个发生了改变),促使差量更新计算出来的结果和全量更新极为接近(或者说完全一样)

- 虚拟DOM的劣势主要在于JS计算的耗时
- DOM操作的能耗和JS计算的能耗根本不在一个量级
- 每次setState的时候只修改少量的数据(模板渲染和虚拟DOM之间的DOM操作量级的差距就完全拉开了,虚拟DOM将在性能上具备绝对优势)
- 性能问题不能一概而论,jQuery,原生DOM在思维模式上来说和虚拟DOM截然不同,强行比较意义不大.
- ==虚拟DOM的价值不在性能,而在别处==

---

站在"虚拟DOM解决了哪些关键问题"的视角和你分享一些业内关于虚拟DOM的共识

- 研发体验/研发效率的问题
- 跨平台的问题

![[assets/img/深入浅出React/IMG-深入浅出React-20240714124907688.png]]

- "批量更新": 在通用虚拟DOM库里是由batch函数来处理的
- batch的作用是缓冲每次生成的补丁集
- diff : 指的是对比两颗虚拟DOM树之间的差异的过程
- 不同的框架对diff过程有着不同的实现思路

---

## 第10讲 |React中的"协调和Stack Reconciler" 过程是怎样的?

==学习知识需要建立必要且完整的上下文==

如果不能确切地把握React15的局限性,就无法从根本上理解React16大改版背后的设计动机.

追寻时代潮流之前,必须要学好历史.

---

## 调和(Reconciliation)过程与Diff算法

"调和" 和 "Diff"

- 调和: Virtual DOM是一种编程概念. 在这个概念里,UI是一种理想化的,或者说"虚拟的"表现形式被保存在内存中,并<font color="#d831a8">通过如ReactDOM等类库使之与"真实的"DOM同步</font>.这一过程叫做<u>协调</u>(调和).

调和过程不能和Diff划等号

- 调和是"使一致"的过程
- Diff是"找不同"的过程

React将源码划分为:

- Core
- Renderer
- Reconciler  (src/renderers/shared/stack/reconciler) 这个路径调和器所做的工作包括组件的挂载,卸载,更新等过程.

---

如今大众认知里,当我们讨论调和的时候,其实就是在讨论Diff

==Diff确实是调和过程中最具代表性的一环.==

要想找出两个树结构之间的不同:

- 传统: 通过循环递归进行树节点的一一对比       O(n<sup>3</sup>)--意味着性能灾难

## ![[assets/img/深入浅出React/IMG-深入浅出React-20240714124908871.png]]

## ![[assets/img/深入浅出React/IMG-深入浅出React-20240714124908957.png]]

## Diff策略的设计思想

- 若两个组件属于同一个类型,它们将拥有相同的DOM树形结构
- 处于同一层接的一组子节点,可用通过设置key作为唯一标识,从而维持各个节点在不同渲染过程中的稳定性
- DOM节点之间的跨层级操作并不多,同层级操作是主流(Diff过程只针对相同层级的节点作对比)

## ![[assets/img/深入浅出React/IMG-深入浅出React-20240714124910452.png]]

### 把握三个"要点",图解Diff逻辑

Diff逻辑的拆分与解读

1. Diff算法性能突破的关键点在于"分层对比"

- 将传统树对比算法优化为分层对比, 分层递归运转

2. 类型一致的节点才有继续对比的必要性
3. key属性的设置,可以帮我们尽可能重用同一层级内的节点

---

减少递归的"一刀切"策略: 类型的一致性决定递归的必要性

"若两个组件属于同一个类型,那么它们就将拥有相同的DOM树形结构"
