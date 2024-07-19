---
aliases:

---
 ```mermaid
graph TD
A[浏览器请求] -- 请求 --> B(控制器)
B -- 处理逻辑 --> C[模型]
C -- 操作数据库 --> D{数据}
D -- 返回数据 --> B
B -- 返回视图 --> E[视图] 
E -- 渲染视图 --> F[浏览器响应]
```



 React属于MVVM(Model-View-ViewModel)设计模式:
- Model: 数据模型,如state、props等
- View: 视图组件 
- ViewModel: 组件本身
特点:
- React组件即View和ViewModel的结合体
- state和props对应Model层数据
- 组件通过setState等方法更新UI
- UI变化驱动数据流向



这里给一个React使用MVVM设计模式的简单计数器实例:
**Model(数据模型)**
```js
// count.js
export default {
  count: 0
}
```
**ViewModel(组件)**
```jsx
// Counter.jsx
import Model from './count'
export default class Counter extends React.Component {
  constructor() {
    this.state = {
      count: Model.count
    }
  }
  render() {
    return (
      <div>
        <p>You clicked {this.state.count} times</p>
        <button onClick={() => this.increment()}>
          Increment
        </button>
      </div>  
    )
  }
  increment() {
    Model.count++
    this.setState({
      count: Model.count
    })
  }
}
```
**View(组件渲染)**
```jsx
// App.jsx 
import Counter from './Counter'
function App() {
  return <Counter />
}
```

**Model(数据模型)**
```js
// data.js
export default {
  getData() {
    return fetch('/api/data')
      .then(res => res.json()) 
  }
}
```
**ViewModel(组件)**
```jsx
// Component.jsx
import Model from './data'
export default class Component extends React.Component {
  state = {
    data: null
  }
  componentDidMount() {
    Model.getData()
      .then(data => {
        this.setState({
          data
        })  
      })
  }
  render() {
    return (
      <div>
        {this.state.data && 
          <Presenation data={this.state.data} />
        }
      </div>
    )
  }
}
```
**View(展示组件)** 
```jsx
// Presentation.jsx
export default function Presentation({ data }) {
  return (
    <div>
      {/* 渲染数据 */}
    </div>
  )
}
```
在这个例子中:
- Model负责从API获取数据
- ViewModel调用Model,获取数据后更新状态
- View根据状态更新展示
这样就实现了MVVM模式下,从后端获取数据的流程。Model负责数据逻辑,ViewModel协调View和Model。


 这里给一个经过功能细分的完整文件结构示例:
```
project
|-- src
   |-- components  
   |-- layouts
   |-- pages  
   |-- routers
   |-- models
   |-- services  
   |-- stores
   |-- constants
   |-- utils  
   |-- assets
   |-- App.js
   |-- index.js
|-- public
|-- tests   
   |-- components  
   |-- services
   |-- stores
   |-- utils
|-- docs
|-- build 
|-- .gitignore
|-- package.json
|-- README.md
```
细分后各文件夹功能:
- components: 公共组件
- layouts: 布局组件 
- pages: 页面组件
- routers: 路由配置
- models: 数据模型
- services: 数据服务
- stores: 状态管理
- constants: 常量
- utils: 公共工具
- assets: 静态资源
- tests: 测试文件
- docs: 文档
- build: 构建脚本
此外还可以根据需求细分:
- api: 接口定义
- hooks: 自定义 Hooks
- plugins: 插件
- mock: mock 数据
- types: TypeScript 类型定义


 根据MVVM思想,这里给出一个高效开发React应用的设计思路:
1. 数据模型层:
- 定义接口获取数据的Model类
- 封装数据操作逻辑,提供统一接口
2. 状态管理层: 
- 使用Redux/Mobx等状态管理库
- 集中管理公共状态数据
3. ViewModel层:
- 使用函数组件和Hook封装业务逻辑
- 处理数据和状态,渲染UI视图
4. UI组件层:
- 使用原子化、可复用组件开发
- 通过props接收数据进行渲染
5. 路由层:
- 使用React Router管理路由
- 动态渲染对应的ViewModel
6. 工具层: 
- 封装常用工具函数
- 提供请求、校验等功能
7. 项目配置:
- 使用Webpack等构建工具
- 配置依赖管理、打包部署等
8. 代码规范:
- 采用ESLint统一代码风格  
- 使用Prettier自动格式化
9. 测试支持:
- 使用Jest编写单元测试
- 测试重要组件和功能
10. 文档支持:
- 使用Markdown记录API文档
- 提供使用文档
这可以实现组件解耦、高内聚的开发模式。



前端功能需求分析是指在开发前端功能时，对需求进行分析和梳理，明确功能的具体要求和实现方式。以下是一些关于前端功能需求分析的信息和链接：

1. 前端功能需求分析的步骤：
   - 确定需求：与产品经理、设计师等沟通，明确功能需求。
   - 拆分功能：将大的功能需求拆分为小的子功能，便于开发和测试。
   - 确定优先级：根据需求的重要性和紧急性，确定功能的优先级。
   - 制定规范：定义功能的输入、输出、交互方式等规范。
   - 编写文档：撰写功能需求文档，明确功能的具体实现和测试要求。

2. 前端功能需求分析的工具：
   - 用户故事地图：用于整理和可视化需求，帮助团队理解和分析功能。
   - 流程图和时序图：用于描述功能的流程和交互过程，帮助开发者理清思路。
   - 原型设计工具：用于创建交互原型，模拟功能的使用场景和操作流程。
