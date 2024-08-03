---
aliases: null
date updated: 2024-07-14 18:01
---

#### 4.2 容器组件与表现组件模式

React组件通常包含杂合在一起的逻辑与表现。逻辑一般指与UI无关的那些东西，如API
的调用、数据操作以及事件处理器。表现则是指渲染方法中创建元素用来显示UI的部分。
Ract有一种简洁而强大的模式，称为容器组件与表现组件，按照这种模式创建组件可以帮
助我们分离上述两个关注点。

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
- [x] react-refetch的工作原理，以及为何可以将这个有用的工具集成到项目中，从而更便捷地获取数据。



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
