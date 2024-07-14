
![(79) MVC Explained in 4 Minutes - YouTube](https://www.youtube.com/watch?v=DUg2SWWK18I&list=PLZlA0Gpn_vH8jbFkBjOuFjhxANC63OmXM&index=4)


### MVC模型

![[assets/img/Full Stack Web Development Course/IMG-Full Stack Web Development Course-20240714124833044.png]]
![[assets/img/Full Stack Web Development Course/IMG-Full Stack Web Development Course-20240714124835559.png]]
MVC是Model-View-Controller的缩写,是一种软件架构模式,用于分离表示层(View)、业务逻辑层(Model)和控制层(Controller)。
Model:
- 业务数据模型,用于处理应用程序的数据逻辑和状态。
- 包含实体类、数据访问对象等。
View: 
- 表示层,负责与用户的交互,如页面显示。
- 只负责展示,不包含任何业务逻辑。
Controller:
- 控制层,作用是接收用户输入并更新模型,选择视图并向视图返回响应。
- 处理用户输入并更新模型状态,选择合适的视图响应用户。
工作流程:
1. 用户通过视图发送请求到控制器
2. 控制器处理请求,更新模型数据
3. 模型通知视图有关状态的变化 
4. 视图重新渲染自身,向用户返回响应
优点:
- 分离了业务逻辑、数据和表现层,降低了耦合度
- 易于单独测试和维护每个层次
- 符合单一职责原则
- 视图独立于业务规则,易于定制
所以MVC是一种常用的软件设计模式。

`npm i express ejs express-ejs-layouts`
`npm i nodemon`
- express: 一个非常流行的Node.js Web应用开发框架。
- ejs:一款用于生成动态网页的模板引擎,与express配合使用。
- express-ejs-layouts: 一个Express中间件,用于实现EJS模板的布局功能。
这三个模块一起使用可以实现:
1. 使用Express框架快速构建Web服务器和API。
2. 使用EJS模板引擎渲染动态HTML页面。
3. 通过express-ejs-layouts实现EJS模板的布局功能,比如头部、底部、导航等公共部分。
所以这行命令的目的是:
一键安装Express+EJS+布局中间件,为后续使用EJS开发Express项目奠定基础。
大大提高了项目初始化的效率。

#### process.env
 这里有一个使用process.env的代码示例:
```js
// 设置环境变量
process.env.NODE_ENV = 'production';
// 读取环境变量
const env = process.env.NODE_ENV;
// 根据环境变量做不同处理
if(env === 'production') {
  // 生产环境配置
  app.use(compression());
} else {
  // 开发环境配置
  app.use(morgan('dev'));
}
// 读取自定义环境变量
const port = process.env.PORT || 3000;
app.listen(port, () => {
  console.log(`App listening on port ${port}`)
});
// 读取敏感数据
const dbPassword = process.env.DB_PASSWORD;
// 也可以在.env文件中定义
// NODE_ENV=production
// PORT=3000
// DB_PASSWORD=123456
```
主要展示:
- 设置和读取内置或自定义环境变量
- 根据环境变量进行条件判断
- 从环境变量中读取敏感数据
- 在.env文件中定义环境变量
通过process.env可以方便地管理应用的运行环境和配置。



####  require('dotenv').load() VS process.env.parse()
 require('dotenv').load() 和 process.env.parse()的区别和联系:
  - require('dotenv').load():
    用于加载.env文件中的环境变量定义到process.env对象中。
    .env文件用来定义环境变量,不会直接暴露到process.env中。
    load()可以解析.env文件,将变量加载到process.env方便使用。
  - process.env.parse():
    直接解析字符串或Buffer中的环境变量定义,加载到process.env中。
    不依赖.env文件,可以直接解析字符串定义的环境变量。
  联系:
  - 都用于将环境变量定义加载到process.env中使用
  - dotenv提供了从.env文件加载的功能
  - parse()可以直接解析字符串定义的变量
  区别:  
  - load()从.env文件加载
  - parse()直接解析字符串/Buffer定义的变量
  使用场景:
  - load():常用于开发时从.env文件加载变量
  - parse():用于不依赖.env文件的场景,直接解析字符串定义的变量
  所以require('dotenv')主要用于加载.env文件定义的变量,process.env.parse()直接解析变量定义字符串。

  这里是使用dotenv和process.env.parse()的代码示例:
使用dotenv加载.env文件:
```js
// .env文件
DB_HOST=localhost
DB_USER=root
// app.js
require('dotenv').config() 
const host = process.env.DB_HOST 
const user = process.env.DB_USER
console.log(host, user) // localhost, root
```
直接解析字符串定义的变量:
```js
const dotenv = require('dotenv')
// 字符串定义
const envConfig = `
  DB_HOST=127.0.0.1
  DB_PORT=3306
`
dotenv.parse(envConfig)
const host = process.env.DB_HOST
const port = process.env.DB_PORT
console.log(host, port) // 127.0.0.1, 3306
```
直接解析Buffer:
```js 
const buf = Buffer.from(envConfig)
dotenv.parse(buf)
// 使用变量
```
主要展示了dotenv和process.env.parse()的使用方式。
前者从文件加载,后者直接解析字符串或Buffer定义的环境变量。

#### get VS post
 router.get和router.post的主要区别和使用:
**区别:**
- router.get:处理HTTP GET请求
- router.post:处理HTTP POST请求 
GET用于获取资源,POST用于创建或更新资源。
**示例:**
```js
// 定义路由
const router = express.Router()
// GET 请求首页
router.get('/', (req, res) => {
  res.send('Home page')
})
// POST 提交数据
router.post('/submit', (req, res) => {
  // 获取表单数据
  const data = req.body
  // 保存数据
  db.collection.insertOne(data)
  res.send('Data submitted')
})
// GET 查询数据列表 
router.get('/list', (req, res) => {
  const list = db.collection.find()
  res.json(list)
})
// 导出路由
module.exports = router
```
主要区别在于请求方法的不同,GET用于获取,POST用于提交。
通过给router绑定不同方法可以实现不同功能的路由处理。

app.set VS  app.use
![[assets/img/Full Stack Web Development Course/IMG-Full Stack Web Development Course-20240714124835641.png]]
- app.set(name, value):
设置应用程序的设置值。
- app.use(function): 
加载中间件函数,对每个请求执行。
- db.on(event, callback):
为数据库事件绑定回调函数,事件多次触发都会调用。
- db.once(event, callback): 
为数据库事件绑定回调函数,事件只触发一次调用。
举例:
```
// 设置视图路径
app.set('views', './views'); 
// 使用静态文件中间件
app.use(express.static('public'));
// 连接成功回调
db.on('', () => {
  console.log('数据库连接成功');
});
// 只执行一次的连接回调
db.once('', () => {
  // 初始化数据
});
```
区别总结:
- app.set/app.use 设置应用程序属性和加载中间件
- db.on绑定重复执行的数据库事件回调 
- db.once绑定只执行一次的数据库事件回调
用于设置应用属性,加载中间件,处理数据库连接事件等不同场景。



