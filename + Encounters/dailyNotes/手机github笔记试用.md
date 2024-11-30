---
aliases: 
theme: 
priority: false
tags:
---
# Mobile gh Notes sync with WuKong journey

package.json  server

```json
"jscripts":{
 "start": "node bin/www",
  "prd":"pm2 start bin/www"
 
}

dependencies: {
 "pug": "^2.0.0",
 "koa":"^2.7.0",
 "crypto-js":"^4.0.0",
}
```

src下文件夹: config, lib, models, routes, server, views

config: 配置文件, lib: 公共模块, models: 数据库模型, routes: 路由, server: 服务器, views: 模板

```js
config: default.js
// 数据库配置参数
// 表属性字段
// 导出
module.exports = config;
```

```js
utils.js
// 导入lodash模块
// setCookies函数: 设置cookie
 // encodeURIComponent函数
// destroyCookie函数: 销毁cookie
```

models
---

```js
answers.js

// 导出Answer模型的定义函数
module.exports = (sequelize, DataTypes) => {
  /**
   * 定义Answer模型的属性
   */
  const Answer = sequelize.define('answers', {
    id: {
      type: DataTypes.INTEGER.UNSIGNED,
      primaryKey: true,
      autoIncrement: true,
      comment: '答案ID'
    },
    creatorId: {
      type: DataTypes.INTEGER,
      comment: '创建者ID'
    },
    content: {
      type: DataTypes.TEXT,
      comment: '答案内容'
    },
    excerpt: {
      type: DataTypes.CHAR,
      comment: '答案摘要'
    },
    type: {
      type: DataTypes.INTEGER,
      comment: '答案类型'
    },
    targetid: {
      type: DataTypes.INTEGER,
      comment: '目标ID'
    },
    createAt: {
      type: DataTypes.DATE,
      comment: '创建时间'
    },
    updateAt: {
      type: DataTypes.DATE,
      comment: '更新时间'
    }
  });

  /**
   * 关联Answer模型与其他模型
   * @param {Object} models - 包含所有模型的对象
   */
  Answer.associate = (models) => {
    // 定义Answer属于users模型的关系
    Answer.belongsTo(models.users, {
      foreignKey: 'creatorId',
      as: 'author'
    });
  };

  // 返回Answer模型
  return Answer;
}

---
article.js
---
// 与answers.js类似
comments.js
// 与answers.js类似
index.js
// 导入fs,path, sequelize, db模块
const config = require('../config/default');
const {db} = config;
const basename = path.basename(__filename);

const {database, username, password} =db;
// 创建一个Sequelize实例，用于连接数据库
const sequelize= new Sequelize(database, username, password, db.options)

// 读取当前目录下的所有文件
fs.readdirSync(__dirname)
// 留下不以 '.' 开头、名称不等于 basename 且扩展名为 .js 的文件
.filter((file)=>{
 return(file.indexOf('.')!==0)&&(file!==basename)&&(file.slice(-3)==='.js');
})
// 遍历过滤后的文件
.forEach((file)=>{
 // 导入文件
 const model = sequelize.import(path.join(__dirname,file));
 // 将导入的文件添加到db对象中
 db[model.name]=model;
});

// 遍历db对象中的所有键
Object.keys(db).forEach((modelName)=>{
 // 如果db对象中的某个键的值有assocaite属性
 if (db[modelName].assocaite){
  // 调用该键的值中的assocaite方法，并传入db对象
  db[modelName].assocaite(db);
 }
});

db.sequelize=sequelize;
db.Sequelize=Sequelize;
module.exports=db;

question.js
//与answers.js类似
statuses.js
// 与answers.js类似
users.js
//与answers.js类似
```

## associate 函数示例

---

```js
const User = sequelize.define('User', {
  // 用户模型属性
});

const Post = sequelize.define('Post', {
  // 帖子模型属性
});

User.associate = function(models) {
  // 定义User和其他模型的关系
  User.hasMany(models.Post, {
    foreignKey: 'userId'
  });
};

Post.associate = function(models) {
  // 定义Post和其他模型的关系
  Post.belongsTo(models.User, {
    foreignKey: 'userId'
  });
};

```

## dir: server

```js
routes.js
congst fs = require('fs');

const addMapping = (router, mapping) => {
 // 遍历mapping中的每一个url
 for (const url in mapping){
  // 通过 startsWith 方法判断 URL 是以 GET、POST、PUT 还是 DELETE 开头。
  // 如果url以'GET'开头
  if(url.startsWith('GET')){
   // 从url中截取从第4个字符开始到末尾的字符串，赋值给path
const path = url.substring(4);
   // 获取路由路径
   router.get(path,mapping[url]);
  // 如果url以'POST'开头
  } else if(url.startsWith('POST')){
  const path = url.substring(5);
  router.post(path,mapping[url]);
  // 如果url以'PUT'开头
  } else if(url.startsWith('PUT')){
  const path = url.substring(4);
  router.put(path,mapping[url]);  
  // 如果url以'DELETE'开头
  } else if(url.startsWith('DELETE')){
  const path = url.substring(7);
 // 如果url不以'GET'、'POST'、'PUT'、'DELETE'开头
  } else {
  console.log(`invalid URL: ${url}`);
 }
 }
}

const addControllers = (router,dir)=>{
 fs.readdirSync(__dirname+'/'+dir).filter((f)=>{
  return f.endsWith('.js');
 }).forEach((f)=>{
  console.log(`process controller: ${f}...`);
  
  let mapping = require(__dirname+'/'+dir+'/'+f);
  addMapping(router, mapping);
 })
 }
 
module.exports =(dir)=>{
 const controllers_dir = dir || "./../routes";
 const router= require("koa-router")();
 addControllers(router, controller_dir);
 return router.routes();
}
```

## views

```pug
error.pug
extends layout
block content
 h1=message
 h2=error.status
 pre #(error.stack)

index.pug

extends layout

block content
 h1 = title
 p Welcome to #{title}

layout.pug

doctype html
html
 head
  // 设置网页标题
  title = title
  // 引入外部样式表
  link(rel='stylesheet', href='/stylesheets/style.css')
  body
   // 填充网页内容
   block content
```

## 后端app.js

```js
const Koa = require('koa');
const app = new Koa();
const views = require('koa-views');
const json = require('koa-json');
const onerror = require('koa-onerror');
const koaBody = require('koa-body');
const logger = require('koa-logger');

const routes=require('./src/server/routes')

onerror(app)

//middlewares
app.use(koaBody({
 multipart:true,
 strict:false,
 formidable:{
  maxFileSize:20*1024*1024// 设置上传文件大小最大限制，默认2M
 }
}))

app.use(json())
app.use(logger())
app.use(require('koa-static')(__dirname + '/public'))

//静态文件模板
app.use(views(__dirname + '/views', {
 extension:'pug'
}))

//logger
// 使用async函数定义中间件，ctx为上下文对象，next为下一个中间件
app.use(async (ctx, next) => {
 // 记录请求开始时间
 const start = new Date()
 // 执行下一个中间件
 await next()
 // 计算请求耗时
 const ms = new Date() - start
 // 打印请求方法、URL和耗时
 const.log(`${ctx.method} ${ctx.url} - ${ms}ms`)
})

//routes
app.use(routes())

//error-handling
app.on('error', (err, ctx) => {
 console.error('server error', err, ctx)
});
console.log('=======================================');

console.log('Fakezhihu-server');
console.log('---------------------------------------');
console.log('Starting at port 3000');
console.log(`Up time: ${new Date().toString()}`);
console.log('=======================================');

module.exports = app

```
