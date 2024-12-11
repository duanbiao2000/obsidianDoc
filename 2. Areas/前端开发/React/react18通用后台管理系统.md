
#### 样式初始化reset-css


```tsx
//main.tsx
import React from 'react'
import ReactDOM from 'react-dom/client'
//样式初始化一般放在App最前面.
import "reset-css"  
// UI框架的样式

//全局样式覆盖UI框架
import "./assets/styles/global.scss"
//组件的样式 (否则可能反过来被UI样式 或者初始化样式所覆盖)
import App from './App'

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
)
```


```tsx
import "@/assets/styles/global.scss"

//默认不认识@,会报错,需要进行路径别名的配置
// 在vite.config.ts添加配置 

import path from "path"
import * as path from "path"
...实现方法查百度
...另外如果需要路径别名提示,需要在tsconfig.json中的"compilerOptions"键/属性中另外进行配置 

resove:{
  alias:{
    "@":path.resolve(__dirname,'./src')
  }
}

// 引入path模块会报红,但其实我们已有node,所以就已经有path模块,只是缺少一些声明配置.
//安装关于node这个库的ts声明配置
npm i -D @types/node
```


`!在类型脚本中的含义是非空断言操作符。`
在TypeScript中,getElementById('root')的返回值类型是Element | null,表示可能返回元素节点,也可能返回null。
而createRoot方法第一个参数需要传入Element类型,不能传入null。
所以我们需要告诉TypeScript这个getElementById返回值一定不是null。这就是非空断言操作符!的作用。
##  不同功能模块导入顺序问题
一般来说,在React项目中导入模块的顺序应该遵循以下原则:
1. 样式初始化文件
样式初始化文件,如reset.css等,应该放在最前面。这些文件会重置或初始化整个页面的默认样式,比如去除浏览器默认样式等。
2. UI框架样式
使用的UI框架(如Ant Design等)提供的全局样式文件应该紧跟在后面。
3. 组件本地样式
各个组件本地的CSS/Sass/Less样式文件。
4. 组件代码
各个组件的代码文件。
5. 路由配置
路由配置文件。
6. App入口组件
App.js或App.tsx文件。
7. 其他业务逻辑
如redux、服务等其他业务逻辑文件。

> [!NOTE]
> 按这个顺序导入可以避免样式覆盖的问题:
> - 初始化样式先加载,重置默认样式
> - 框架样式再加载,应用框架样式  
> - 组件样式最后加载,不会被框架样式覆盖




