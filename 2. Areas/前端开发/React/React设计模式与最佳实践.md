---
aliases: 
<<<<<<< HEAD
date_created: 2024-07-14 18:01
=======
updateAt: 2024-07-14 18:01
>>>>>>> 93a933e (refactor(dailyNotes): update metadata structure for daily notes)
---

#### 4.2 容器组件与表现组件模式

React组件通常包含杂合在一起的逻辑与表现。逻辑一般指与UI无关的那些东西，如API
的调用、数据操作以及事件处理器。表现则是指渲染方法中创建元素用来显示UI的部分。
Ract有一种简洁而强大的模式，称为容器组件与表现组件，按照这种模式创建组件可以帮
助我们分离上述两个关注点。

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


