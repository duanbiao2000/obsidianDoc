
![(79) MVC Explained in 4 Minutes - YouTube](https://www.youtube.com/watch?v=DUg2SWWK18I&list=PLZlA0Gpn_vH8jbFkBjOuFjhxANC63OmXM&index=4)


### MVC模型

![[IMG-Full Stack Web Development Course-20240719191749499.png]]
![[IMG-Full Stack Web Development Course-20240719191749845.png]]
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



app.set VS  app.use
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


