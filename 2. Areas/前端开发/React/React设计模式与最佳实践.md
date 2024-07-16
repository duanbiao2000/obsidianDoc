---
aliases: null
date updated: 2024-07-14 18:01
---

ESLint的extends属性非常强大,可以从Airbnb等第三方配置入手再添加自己特有的规则.
eslint-config-airbnbeslint@^2.9.0

### 函数式编程

React的[[声明式编程]]提升了代码的可读性
保持代码简洁的另一个方法是,遵循[[../../../2. Areas/前端开发/函数式编程]]风格
React领域的一个常用模式是使用高阶组件,将组件当做函数,并为他们增加一些常用行为.
[[高阶函数]]接受一个函数作为参数,也可以传入其他参数,最后返回一个另一个函数,返回的函数通常会添加一些增强的特殊行为.

```js
const add = (x, y) => x + y
const log = func =>(...args) => {
	console.log(...args)
	return func(...args)
}
const logAdd = log(add)
```

```js
let x = 0
const add = y => (x + y)
```

执行add(1)两次,得到两个不同的结果, 第一次是1,第二次是2. 尽管是用同样的参数调用同一个函数.
出现这种情况的原因在于==每次执行都修改了全局状态==.

<!--SR:!2023-07-25,5,230-->

在函数式编程中,函数不会修改变量值.而是创建新的变量,赋新值后再返回变量.操作数据的这种方式成为不可变性.

```js
const add3 = arr => arr.push(3)
const myArr = [1,2]
add3(myArr) //[1,2,3]
add3(myArr) //[1,2,3,3]
```

可以用concat方法改写函数以满足不可变性.

```js
const add3 = arr => arr.concat(3)
const myArr = [1,2]
const result1 = add3(myArr) //[1,2,3]
const result2 = add3(myArr) //[1,2,3]
```

即便运行该函数两次,myArr仍然保有初始值. (concat方法会返回新数组,并且不会修改原数组)

#### 柯里化

柯里化过程就是将多个参数函数转换成单参数函数,这些单参数函数的返回值也是函数.

```js
//old writing:
const add = (x, y) => x + y

//new
const add = x => y => x + y
const add1 = add(1)
add1(2) //3
add1(3) //4
//传入第一个参数后, 第一个值被保留起来,返回的第二个函数可以多次复用
```

#### 组合

```js
const add = (x ,y) => x + y
const square = x => x * x
//这两个函数可以组合创建一个新函数,用于两数相加,在对结果求平方.
const addAndSquare = (x, y) => square(add(x, y))
```

#### 函数式编程与UI

==可以将UI看做传入应用状态的函数.==
组件可以组合形成最后的UI.
React构建UI的方式和函数式编程原则有很多相似之处.
`UI = f(state)`

### 可复用组件
React定义组件的多种方式.
React引入的新型组件,允许将组件定义为无状态函数.
最好的学习方式是阅读代码示例.

- [ ] 函数式组件与状态组件的区别
- [ ] 状态的工作原理,何时避免使用
- [ ] 为什么定义清晰的prop类型很重要,如何根据prop用React Docgen动态生成文档
- [ ] 将耦合组件改为可复用组件的实例
- [ ] 用React Storybook创建可用的风格指南,以便为可复用组件提供文档

> 应该清楚了解prop,状态和[[生命周期]]这些概念. 

```js
class Button extends React.component {
	render(){
	return <button>{this.props.text}</button>
	}
}

Button.propTypes = {
	text: React.PropTypes.string,
}

Button.defaultProps = {
	text: 'Click me!',
}
```

#### 状态

[[React.createClass和类组件的区别]]
createClass工厂方法和extends React.Component方法的另一个重大区别是,组件初始状态的定义方式不同.

```js
class Button extends React.Component {
	constructor(props){
		super(props)
		this.state = {
			text: 'Click me!'
		}
	render() {
		return <button>{this.state.text}</button>
	}
}

//使用类的好处在于无需使用React特有的API,直接在实例上定义属性即可.
//ES2015中,若想在子类中使用this,必须先调用super方法.React还会将props对象传给父组件.
```

#### this绑定

```js
() => this.setState()
//解决自动绑定问题的一种可能方案就是使用箭头函数 (pitfall:性能问题:在渲染方法中绑定函数会带来副作用,低效渲染)

//Babel会将以上代码转译为:
var _this = this;
(function () {
	return _this.setState();
});
```

```js
//最佳方案是构造器进行绑定操作,这样即使多次渲染组件,它也不会发生任何改变
this.handlerClick = this.handleClick.bind(this)
```

某些情况下可能需要在状态更新完成时执行一些操作,React为此提供了一个回调函数:

```js
this.setState({
	clicked:ture,
},()=>{
	console.log('the state is now', this.state)
})
```

将任意函数作为setState的第二个参数传递,状态更新完成时会触发该函数,同时组建完成渲染.

用docgen提供组件文档的用例可以参见优秀的Material UI库,其所有文档都是根据源代码自动生成的.

#### 可复用组件示例

假设组件从API路径加载一个消息集合,并在屏幕上显示列表.
这个示例很简单,但对于理解使组件可复用的必要步骤很有用.

```js
class PostList extends React.Component {
	constructor(props) {
		super(props)
		this.state = {
			posts: [],
		}
	}
componentDidMount() {
	Posts.fetch().then(posts=>{
		this.setState({posts})
		})
	}
}
```

一个空数组被赋给消息,以表示初始状态
调用componentDidMount时会触发API调用,取回的数据将保存到状态中.
这种数据获取模式相当常见, 第5章将介绍更多可用方式.
辅助类Posts用来与API通信,它的获取方法会返回一个Promise对象,请求成功后会返回消息列表.
显示消息列表部分的代码:

```js
render() {
	return (
		<ul>
			{this.state.posts.map(post => (
				<li key={post.id}>
					<h1>{post.title}</h1>
					{post.excerpt && <p>{post.excerpt}</p>}
				</li>
			))}
		</ul>
	)
}
```

> 摘要属性是可选的,如果存在,就显示在段落中.

我们再渲染一个类似的列表, 不过这次是从props而不是从状态中获取用户列表.(应对不同场景)

```js
const UserList = ({users}) => (
	<ul>
		{users.map(user=>(
			<li key={user.id}>
				<h1>{user.username}</h1>
				{user.bio && <p>{user.bio}</p>}
			</li>
		))}
	</ul>
)
```

#### 创建可复用的列表组件

复制代码往往不是最佳解决方案,React帮助代码符合DRY(don't repeat yourself,不要重复你自己)原则.

#### Storybook-风格指南

`npm install --save @kadira/react-storybook-addon`
故事文档通常放在名为stories的文件夹中,这个文件夹可以位于组建文件夹或者文件目录中任意地方.
你可以在stories文件夹下为每个组件创建一个文件.

#### 4.2 容器组件与表现组件模式

React组件通常包含杂合在一起的逻辑与表现。逻辑一般指与UI无关的那些东西，如API
的调用、数据操作以及事件处理器。表现则是指渲染方法中创建元素用来显示UI的部分。
Ract有一种简洁而强大的模式，称为容器组件与表现组件，按照这种模式创建组件可以帮
助我们分离上述两个关注点。
?
清晰地定义逻辑与表现间的界限不仅能使组件更易复用，还有很多其他好处，本节将一一
介绍。
==学习新概念的最佳方式之一就是查看实际示例==

<!--SR:!2023-07-22,2,243-->

假设我们有一个组件利用地理位置API获取用户定位，并在浏览器页面上显示经纬度。

```js
//首先，在组件文件夹下创建geolocation.js文件，并用class定义Geolocation组件：
class Geolocation extends React.Component
	//接着定义constructor方法，用于初始化内部状态并绑定事件处理器：
	constructor(props){
		super (props)
		this.state = {
		latitude:null,
		longitude:null,
		}
		this.handleSuccess this.handleSuccess.bind(this)
	}
	//现在可以用componentDidMount回调触发API请求了：
	componentDidMount ()
		if (navigator.geolocation){
			navigator.geolocation.getCurrentPosition(this.handleSuccess)
		}
		//当浏览器返回数据时，使用以下函数将结果保存在状态中：
	handleSuccess({coords}){
		this.setstate({
		latitude:coords.latitude,
		longitude:coords.longitude,
		})
	}
	//最后用render方法显示经纬度：
	render(){
		return (
			<div>
				<div>Latitude:(this.state.latitude)</div>
				<div>Longitude:(this.state.longitude)</div>
			</div>
		)
	}	
```

为了更快地迭代，将UⅡ与请求并加载位置信息的部分分开会不会更好？
抽离主组件的表现部分，可以使用Storybook在风格指南中用伪数据渲染组件，像上一章那样，这样就能享受到开发可复用组件带来的所有好处。
那么我们来看看如何通过遵循容器组件与表现组件模式来实现这个目的。
在这个模式中，每个组件都拆分成两个小组件，每个小组件各自都有清晰的职责。
容器组件包含有关组件逻辑的一切，API的调用就在容器组件中进行。此外，它还负责处理数据操作以及事件处理。
UI定义在表现组件中，并且表现组件以prop的形式从容器组件接收数据。
因为表现组件通常不含逻辑，所以可以将它创建为函数式无状态组件。
没有规则要求表现组件一定不能拥有状态。例如，UI状态就可以保存在表现组件内部。
这个示例只需要一个用于显示经纬度的组件，因此用一个简单函数来实现即可。
首先，将Geolocation组件重命名为GeolocationContainer:
`class GeolocationContainer extends React.Component`
同时将`geolocation.js`文件重命名为`geolocation-container.js`。
在容器组件名的末尾加上container, 而表现组件则采用原有名称，这项规则并不严格，却是
React社区广泛使用的最佳实践。
另外还需要更改渲染方法的实现，并移除所有UI部分，如下所示：

```js
render(){
	return
		<Geolocation (...this.state)/>
```

如以上代码段所示，我们不在容器组件的渲染方法内创建HTML元素，而是使用（接下来将会创建的)表现组件，并传入状态。
状态包含经纬度属性，默认值为null,浏览器触发回调函数后会将真正的用户位置信息赋值给它们。

```js
const Geolocation ({ latitude,longitude })=>
	<div>
		<div>Latitude:{latitude}</div>
		<div>Longitude:{longitude}</div>
	</div>
```

现在我们创建一个名为`geolocation.js`的新文件，在该文件中定义无状态函数式组件，如下所示：

无状态函数式组件就是纯粹函数，传入状态并返回元素，可以非常优雅地定义UI。
在这个示例中，函数从拥有者组件那接收经纬度数据，然后返回标记结构来显示出来。
我们当然希望能遵循最佳实践，为组件定义清晰的接口，因此用propTypes来声明组件所
需要的属性：

```js
Geolocation.propTypes =
latitude:React.PropTypes.number,
longitude:React.PropTypes.number,
```

判断容器组件和表现组件分别要包含哪些内容往往不太直观；以下几点建议可以帮你做出
判断。
容器组件：

- [x] 更关心行为部分；
- [x] 负责渲染对应的表现组件；
- [x] 发起API请求并操作数据 ;
- [x] 定义事件处理器；
- [x] 写作类的形式。

表现组件：

- [ ] 更关心视觉表现；
- [ ] 负责渲染HTML标记（或其他组件）；
- [ ] 以props的形式从父组件接收数据；
- [ ] 通常写作无状态函数式组件。

#### 高阶组件

当高阶函数概念应用在组件上时，我们将它简称为高阶组件。
首先我们来看看高阶组件长什么样：
` const Hoc = Component => EnhancedComponent  `
高阶组件其实就是函数，它接收组件作为参数，对组件进行增强后返回。
我们通过一个很简单的示例来理解增强后的组件长什么样。

```js
const withClassName Component = props =>
	<Component {..props} className ="my-class"/>
```

一开始理解以上代码会有些困难，我们试着理解一番。
我们声明了接受Component参数的withClassName函数，然后返回另一个函数。
返回的函数是一个无状态函数式组件，它接受props参数并渲染原来的组件。整个props对
象会展开，然后和值为"my-class"的className属性一起传给组件。
高阶组件通常将组件上接收到的props对象展开，这样做的原因是尽量让它们更直观，并且
只添加新的行为。
现在我们来看看如何在组件中使用withclassName高阶组件。
首先，创建一个无状态函数式组件，它接收类名称并赋值给一个iv标签：

```js
const MyComponent =( {className })=>
	<div className={className}/

MyComponent.propTypes ={
	className: React.PropTypes.string,
}
```

我们不直接使用它，而是传递给高阶组件，如下所示：

```js
const MyComponentWithClassName = withClassName (MyComponent)
```

通过将组件封装进withClassName函数，确保该组件可以接收className属性。

#### 4.5 recompose

recompose是一个很流行的库，提供了许多有用的高阶组件，而且可以优雅地组合它们：
该库提供的高阶组件就是一些用于封装组件的小工具，可以从组件中抽离部分逻辑，使它们
更简洁、可复用性更好。
假设组件从某个API接收一个用户对象，且该对象包含很多属性。
允许组件接收任何对象的做法不太好，因为这依赖于组件了解对象长什么样，最重要的是，
一旦对象发生改变，组件就会崩溃。
从父组件接收props的更好方式是将每个属性定义为基本类型。
我们用Profile组件来显示username和age,如下所示：

```js
const Profile =({ user })=> (
	<div>
		<div>Username:{user.username)</div>
		<div>Age:{user.age)</div>
	</div>
)
Profile.propTypes = {
	user: React.PropTypes.object,
}
```

如果想要改变组件接口来接收单个prop而不是整个用户对象，可以用recompose提供的高
阶组件flattenProp来实现。
我们来看一下具体做法。
首先，修改组件来单独声明每个属性，如下所示：

```js
const Profile =(username,age })=>(
	<div>
		<div>Username:(username)</div>
		<div>Age:(age)</div>
	</div>
)
Profile.propTypes = {
	username:React.PropTypes.string,
	age:React.PropTypes.number,
}
```

然后用高阶组件进行增强：

```js
const ProfilewithFlattenUser flattenProp('user')(Profile)
```

你可能已经注意到了，此处高阶组件的用法稍有不同。实际上，这是一种==函数式编程==方式，
有些高阶组件先通过==偏函数==用法接收参数。
它们的特征如下所示：

```js
const Hoc = args => Component => EnhancedComponent
```

我们要做的就是先调用高阶组件来创建一个函数，然后用它封装原有组件：

```js
const withFlattenUser flattenProp('user')
const ProfilewithFlattenUser withFlattenUser(Profile)
```

<!--SR:!2023-07-21,1,210!2023-07-22,2,243-->

### 5. 恰当地获取数据

本章包含如下内容。

- [ ] React的单向数据流，以及它如何使应用结构更易于理解。
- [x] 子组件如何用回调函数与父组件通信。
- [x] 两个兄弟组件如何通过公有父组件通信。
- [x] 如何创建通用的高阶组件来获取任意API路径的数据。
- [x] react-refetch的工作原理，以及为何可以将这个有用的工具集成到项目中，从而更便

捷地获取数据。

#### 数据流

React推行了一种非常有趣的模式，允许数据从根节点流向叶节点。这种模式通常称作==单向
数据流==，本节将对其进行详细介绍。

#### 疑问

每个子组件都能保存内部状态,也可以将状态作为自身嵌套组件的prop?
?
是的，React组件可以有内部状态（state）来保存和管理组件的数据。可以使用`useState`钩子或者类组件中的`this.state`来定义和更新组件的内部状态。
另外，React组件之间可以通过props来传递数据。父组件可以将状态作为prop传递给子组件，子组件可以通过props来访问和使用这些数据。
如果子组件需要修改父组件的状态，可以通过在子组件中定义回调函数并将其作为prop传递给子组件，子组件可以调用该回调函数来通知父组件更新状态。
这种通过props来传递状态和回调函数的方式使得React中的组件可以实现数据的上下文传递和交互。
当使用函数组件时，可以使用`useState`钩子来定义和更新组件的内部状态。下面是一个简单的示例：

```jsx
import React, { useState } from 'react';
function ChildComponent(props) {
  const [count, setCount] = useState(0); // 定义内部状态 count
  const handleClick = () => {
    setCount(count + 1); // 更新内部状态 count
  };
  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={handleClick}>Increment</button>
    </div>
  );
}
function ParentComponent() {
  return (
    <div>
      <h2>Parent Component</h2>
      <ChildComponent />
    </div>
  );
}
export default ParentComponent;
```

在这个示例中，==父组件==没有传递任何props给子组件，但是你可以通过==props==将状态作为prop传递给子组件，然后在子组件中使用。
在类组件中实现相同的功能也是类似的，你可以使用`this.state`来定义和更新组件的内部状态。以下是相同功能的类组件示例：

```jsx
import React, { Component } from 'react';
class ChildComponent extends Component {
  constructor(props) {
    super(props);
    this.state = {
      count: 0, // 定义内部状态 count
    };
  }
  handleClick = () => {
    this.setState({ count: this.state.count + 1 }); // 事件处理器:更新内部状态 count
  };
  render() {
    return (
      <div>
        <p>Count: {this.state.count}</p>
        <button onClick={this.handleClick}>Increment</button>
      </div>
    );
  }
}
class ParentComponent extends Component {
  render() {
    return (
      <div>
        <h2>Parent Component</h2>
        <ChildComponent />
      </div>
    );
  }
}
export default ParentComponent;
```

无论是函数组件还是类组件，都可以在组件层次结构中灵活地使用组件状态和props来管理和传递数据。

<!--SR:!2023-07-21,1,223-->

#### 疑问(保留)

如果子组件需要修改父组件的状态，可以通过==在子组件中定义回调函数==并将其作为prop传递给子组件，子组件可以调用该回调函数来通知父组件更新状态。
?
当子组件需要修改父组件的状态时，可以通过==在父组件中定义一个回调函数==，并将其作为prop传递给子组件。子组件可以调用该回调函数，将需要更新的数据作为参数传递给父组件。
下面是一个示例：

```jsx
import React, { useState } from 'react';
function ChildComponent(props) {
  const handleClick = () => {  //事件处理器:
    props.updateParentState('Updated from child component'); // 调用父组件传递的回调函数并传递需要更新的数据
  };
  return (
    <div>
      <button onClick={handleClick}>Update Parent State</button>
    </div>
  );
}
function ParentComponent() {
  const [parentState, setParentState] = useState('');
  const handleUpdateParentState = (data) => {
    setParentState(data); // 更新父组件的状态
  };
  return (
    <div>
      <h2>Parent Component</h2>
      <p>Parent State: {parentState}</p>
      <ChildComponent updateParentState={handleUpdateParentState} />
    </div>
  );
}
export default ParentComponent;
```

在上面的示例中，`ParentComponent`定义了一个内部状态`parentState`，并且定义了一个回调函数`handleUpdateParentState`来更新该状态。
`ChildComponent`是子组件，它接收一个名为`updateParentState`的prop，该prop是父组件的回调函数。当子组件的按钮被点击时，它会调用`updateParentState`并传递一个字符串作为参数。
当子组件调用`updateParentState`时，父组件中的`handleUpdateParentState`函数会被调用，将子组件传递的数据更新到父组件的状态`parentState`中。最后，父组件会重新渲染，并将更新后的状态传递给子组件。
通过这种方式，子组件可以通知父组件更新状态，并实现组件之间的数据交互。

<!--SR:!2023-07-22,2,243-->

> 在实现子组件修改父组件状态的功能时，通常是在父组件中定义回调函数并将其作为prop传递给子组件。

这是因为父组件拥有需要更新的状态数据，而子组件需要通过回调函数来通知父组件进行状态更新。父组件根据子组件的操作来更新自己的状态，然后再将更新后的状态通过props传递给子组件进行重新渲染。
这种方式使得父组件成为了数据的“单一真相来源”，子组件通过调用父组件的回调函数来请求状态更新，确保数据的一致性和可追踪性。
当然，在某些情况下，你也可以在子组件中定义回调函数，并将其作为prop传递给父组件。这种情况通常是子组件中的操作需要在父组件中进行处理，但是父组件不需要更新自己的状态，而是需要执行其他的逻辑操作。
总的来说，通常情况下，在父组件中定义回调函数来处理子组件的状态更新是最常见的做法。但根据具体的需求和业务逻辑，也可以在子组件中定义回调函数并传递给父组件。

#数据
撰写本书时，Chrome和Firefox已经原生实现了获取函数。如果需要支持不同的浏览器，可
以使用GitHub开发的获取腻子脚本（fetch polyfill)。
我们还将使用GitHub的公共API来加载数据。向以下路径传递用户名会返回gist列表：
<https://api.github.com/users/:username/gists>.
gst就是一些便于开发人员共享的代码片段。
我们要构建的第一个组件是一个简单的gist列表，其中包含由用户gaearon（Dan Abramov)
创建的gist。

用于获取数据的代码可以放在两个生命周期钩子中：componentwillMount和component-
DidMounto
前者会在组件首次渲染前触发，后者则在组件挂载完成后立即触发。
使用前者似乎是正确的做法，毕竟我们希望尽快加载数据，不过需要注意一点。
实际上，服务端渲染和客户端渲染都会触发componentwillMount函数。

#### 获取gaearon的gist的代码示例

下面是使用 React 类组件和函数组件的形式获取 gaearon 的 gist 列表的示例代码：
使用类组件的形式：

```jsx
import React, { Component } from 'react';
class GistList extends Component {


  constructor(props) {
    super(props);
    this.state = {
    gists: [] // 初始化 gist 列表为空数组
    };
  }

  componentDidMount() { //也叫钩子,确保只在浏览器端调用API请求
    fetch('https://api.github.com/users/gaearon/gists')
      .then(response => response.json())
      .then(data => {
        // 获取 gaearon 的 gist 列表,返回一个Promise对象(response)
        //console.log(data);
        this.setState({ gists: data }); // 更新 gist 列表的状态
      })
      .catch(error => {
        console.error('获取 gist 列表时出错:', error);
      });
  }
  
  render() {
    return (
	  const { gists } = this.state;
      <div>
        <h2>Gist List</h2>
        {/* 渲染获取到的 gist 列表 */}
        <ul>
          {gists.map(gist => (
            <li key={gist.id}>{gist.description}</li>
          ))}
		</ul>
      </div>
    );
  }
}
export default GistList;
```

使用函数组件的形式：

```jsx
import React, { useState, useEffect } from 'react';
function GistList() {
  const [gists, setGists] = useState([]);

  useEffect(() => {
    fetch('https://api.github.com/users/gaearon/gists')
      .then(response => response.json())
      .then(data => {
        // 获取 gaearon 的 gist 列表
       //console.log(data);
        setGists(data); // 更新 gist 列表的状态
      })
      .catch(error => {
        console.error('获取 gist 列表时出错:', error);
      });
  }, []);
  return (
    <div>
      <h2>Gist List</h2>
      {/* 渲染获取到的 gist 列表 */}
	 <ul>
          {gists.map(gist => (
            <li key={gist.id}>{gist.description}</li>
          ))}
	</ul>

    </div>
  );
}
export default GistList;
```

在上述代码中，无论是类组件还是函数组件，我们都使用 `componentDidMount`（类组件）或 `useEffect`（函数组件）来在组件挂载后发起请求。在请求的成功回调中，我们可以处理返回的数据，这里只是简单的使用 `console.log` 打印到控制台。
需要注意的是，在函数组件中使用 `useEffect` 时，我们传递了一个空的依赖数组 `[]`，这表示只在组件挂载时执行一次请求。如果需要根据特定的依赖项来触发请求的更新，可以在依赖数组中指定相应的变量。
这样，你就可以在 React 类组件或函数组件中获取 gaearon 的 gist 列表并进行相应的处理了。

想要从组件中移除数据逻辑并在整个应用中复用,其中一个解决方案就是==创建高阶组件==.

<!--SR:!2023-07-22,2,243-->

我们先通过偏函数写法接受其他参数,然后将实际组件作为第二个参数:
`const withData = url => Component => (...)`

#### react-refetch

`react-refetch` 是一个用于数据获取和管理的 React 库。它提供了一个高阶组件（Higher-Order Component，HOC）和钩子函数，使得在 React 组件中进行数据请求变得简单和可组合。
以下是一个介绍 `react-refetch` 的基本概念和一个代码示例：
**基本概念：**

- **请求描述符（Request Descriptor）**：描述一个数据请求的对象，包含了请求的 URL、HTTP 方法、请求体等信息。
- **响应渲染器（Response Renderer）**：用于渲染数据请求的状态，例如加载中、成功或失败的状态。
- **高阶组件（HOC）和钩子函数**：`react-refetch` 提供了 `connect` 高阶组件和 `useRefetch` 钩子函数来连接组件与数据请求。

**代码示例：**
以下是一个使用 `react-refetch` 进行数据请求的示例代码：

```jsx
import React from 'react';
import { connect, PromiseState } from 'react-refetch';
// 请求描述符
const fetchData = () => ({
  dataResponse: {
    url: 'https://api.example.com/data',
    method: 'GET',
  },
});
// 展示组件
function DataComponent(props) {
  const { dataResponse } = props;
  if (dataResponse.pending) {
    return <div>Loading...</div>;
  } else if (dataResponse.rejected) {
    return <div>Error: {dataResponse.reason}</div>;
  } else if (dataResponse.fulfilled) {
    const data = dataResponse.value;
    return (
      <div>
        <h1>Data Component</h1>
        <ul>
          {data.map((item) => (
            <li key={item.id}>{item.name}</li>
          ))}
        </ul>
      </div>
    );
  } else {
    return null;
  }
}
// 使用 connect 高阶组件连接组件与数据请求
export default connect(fetchData)(DataComponent);
```

在上述示例中，我们首先定义了一个请求描述符 `fetchData`，它返回一个包含请求信息的对象。然后，我们创建了一个 `DataComponent` 组件，它展示了从服务器获取的数据。最后，通过使用 `connect` 高阶组件将 `fetchData` 和 `DataComponent` 连接起来，使得数据请求和渲染逻辑能够在组件中生效。
在 `DataComponent` 中，我们根据数据请求的状态（`dataResponse`）进行不同的渲染。如果请求正在进行中，我们显示 "Loading..."；如果请求被拒绝，我们显示错误信息；如果请求成功，我们展示获取到的数据。根据请求的状态，`dataResponse` 对象提供了不同的属性来访问请求的结果。
希望这个简单的示例能够帮助您了解 `react-refetch` 的基本概念和使用方法。


