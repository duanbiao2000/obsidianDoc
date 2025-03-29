

[Express 教程 3：使用数据库 (Mongoose) - 学习 Web 开发 | MDN (mozilla.org)](https://developer.mozilla.org/zh-CN/docs/Learn/Server-side/Express_Nodejs/mongoose)

model 和 schema 在 Mongoose 中的关系如下:

1. Schema - 模式定义

Schema 是 Mongoose 中定义模型属性的地方,可以定义字段名、类型、默认值、校验等。每一个 Schema 会映射到 MongoDB 中的一个 collection。
例如:

```js
const userSchema = new Schema({
  name: String,
  age: Number
});
```

2. Model - 模型类

Model 是由 Schema 编译生成的模型类。通过 Model 可以对数据库进行 CRUD 操作。
例如:

```js
const User = mongoose.model('User', userSchema);
const user = new User({name: 'John'});
user.save(); 
```

这里我们通过 Schema 生成了一个 User 模型,然后可以使用这个模型对数据库进行操作。
3. 关系

- 一个 Schema 会生成一个 Model
- 多个 Model 可以使用同一个 Schema
- Model 代表的是数据库中的集合 collection
- Schema 定义了 collection 中文档的结构

所以 Schema 和 Model 的关系是:
Schema 生成 Model, Model 负责数据库操作。Schema 定义模型结构,Model 代表集合 collection。

在 MongoDB 中,collection 表示数据库中的集合,可以理解为关系型数据库中的表。
具体来说,collection 有以下几个特点:

1. 文档的集合

collection 是存储文档(document)的集合,文档类似于关系型数据库中的记录(row)。每个 collection 包含多条文档。
2. 无模式
collection 中的文档不需要有相同的结构(schema),同一个 collection 中的文档可以有不同的字段。
3. 与数据库对应
一个数据库中可以有多个不同的 collection,我们通常根据业务需要来划分 collection。
4. 具名的
每个 collection 都有一个名字,用于标识这个 collection。
5. 有索引
MongoDB 支持对 collection 创建索引,提高查询效率。
6. 支持聚合管道
可以在 collection 上使用聚合管道(aggregation pipeline)进行复杂的聚合操作和数据处理。
所以简单来说,collection 就是 MongoDB 数据库中的一个文档集合,类似关系型数据库中的表。collection 是 MongoDB 中最基础的存储和操作单位。

```js
const breakfastSchema = new Schema({
  eggs:{
    type:Number,
    min:[6,"鸡蛋太少"],
    max:12,
  }
  drink:{
    type:String,
    enum:["咖啡","茶"]
  }
})

```

```js
const Athlete = mongoose.model("Athlete", yourSchema);

// SELECT name, age FROM Athlete WHERE sport='Tennis'
Athlete.find({ sport: "Tennis" }, "name age", function (err, athletes) {
  if (err) {
    return handleError(err);
  } // 'athletes' 中保存一个符合条件的运动员的列表
});

```

**备注：** Mongoose 中所有回调都使用 `callback(error, result)` 模式。如果查询时发生错误，则参数 `error` 将包含错误文档，`result` 为 `null`。如果查询成功，则 `error`为 `null`，查询结果将填充至 `result` 。

Next.js 可以在一定程度上取代 Pug 的作用,但两者还是有区别的:

1. Next.js 中可以使用 React 组件直接构建页面,不再需要模板引擎。这与 Pug 的作用有些类似。
2. Next.js 通过 getStaticProps / getServerSideProps 可以实现服务端渲染,这也与 Pug 的 SSR 能力类似。
3. Next.js 输出的 HTML 对 SEO 也是友好的。
4. 但 Next.js 不具备模板引擎的模板继承、混入等能力。不适合用于构建复用性很高的页面。
5. Pug 语法更简洁,更适合编写静态页面。Next.js 需要使用 React 组件。
6. Next.js 更侧重前端应用和交互,而不仅仅是生成 HTML。

所以,如果只是需要生成简单的静态 HTML, Pug 依然是更好的选择。
但如果需要构建完整的前端应用,Next.js 会是更合适的解决方案。它可以取代 Pug 生成静态页面的部分功能,但也有自己的侧重点。
需要根据项目实际需求来选择 Pug 或 Next.js。通常两者也可以很好地配合使用。

```js
// 书籍列表控制器
// 1. 使用 Book 模型查询所有书籍
// - 不指定查询条件,表示获取所有文档
// - 只返回 title 和 author 字段
Book.find({}, "title author") 
// 2. 填充 author 字段
// - 根据 author 的对象ID找到对应的作者文档
// - 将作者信息填充到 book 文档的 author 字段上 
.populate("author")  
// 3. 执行查询
.exec(function (err, list_books) {
 // 4. 处理错误
 if (err) {
   return next(err);
 }
 // 5. 渲染模板
 // - 传递标题和书籍列表
 // - 模板可以直接使用填充后的 author 信息
 res.render("book_list", { 
   title: "Book List",
   book_list: list_books 
 });
})
```

以上代码对书籍列表页面的主要逻辑进行了格式化,并添加了详细的代码注释:

1. 查询所有书籍,只返回标题和作者字段
2. 填充作者信息
3. 执行查询
4. 错误处理
5. 渲染模板,传递书籍列表

通过格式化和添加注释,可以让代码更易阅读和理解,也方便后续的维护。

```js
// 书籍副本列表控制器
// 1. 查询所有 BookInstance 文档
BookInstance.find()
// 2. 填充相关的 book 字段  
//    根据 book 对象ID找到对应的书籍信息
.populate('book')  
// 3. 执行查询
.exec(function(err, list_bookinstances) {
 // 4. 错误处理
 if (err) {
   return next(err); 
 }
 // 5. 渲染模板
 // - 传递标题
 // - 传递书籍副本列表
 // - 模板可以直接使用填充的 book 信息
 res.render('bookinstance_list', {
   title: 'Book Instance List',
   bookinstance_list: list_bookinstances
 });
});
```

上述代码实现了书籍副本列表的功能:

1. 查询所有 BookInstance 文档
2. 通过 populate 填充相关 book 字段
3. 执行查询
4. 错误处理
5. 渲染模板,传递书籍副本列表

模板可以直接使用填充的 book 信息显示书籍标题。

同样使用了 populate 来避免客户端处理,提供了清晰简洁的控制器逻辑。

```js
// 流派详情页面控制器
// 使用 async.parallel 实现并行查询
async.parallel({
 // 查询指定流派信息
 genre: function(callback) {
   Genre.findById(req.params.id).exec(callback);
 },
 // 查询该流派的所有书籍
 genre_books: function(callback) {
   Book.find({ genre: req.params.id }).exec(callback); 
 }
}, function(err, results) {
 // 错误处理
 if (err) {
   return next(err);
 }
 // 流派不存在
 if (results.genre == null) {
   var err = new Error('Genre not found');
   err.status = 404;
   return next(err);
 }
 // 渲染模板
 res.render('genre_detail', { 
   title: 'Genre Detail',
   genre: results.genre,
   genre_books: results.genre_books
 });
});
```

上述代码实现了流派详情页面的功能:

1. 使用 async.parallel 实现流派信息和该流派书籍的并行查询
2. 错误处理
3. 如果流派不存在,返回 404 错误
4. 渲染模板,传递流派信息和书籍列表

使用 async.parallel 可以有效地发挥 Node.js 的异步并发优势,避免多个查询只能顺序执行的低效情况。

在 Node.js 中设置 NODE_ENV 环境变量有以下几种方式:

1. 在启动应用时通过参数设置:

```bash
# Linux/macOS
NODE_ENV=production node app.js
# Windows cmd
set NODE_ENV=production&& node app.js
# Windows PowerShell
$env:NODE_ENV="production" 
node app.js
```

2. 在代码中设置:

```js
process.env.NODE_ENV = 'production';
```

3. 在启动脚本中设置,比如 package.json:

```json
"scripts": {
  "start": "NODE_ENV=production node app.js"
}
```

4. 通过环境变量管理工具(dotenv等)在启动时从 .env 文件中加载
5. 在系统环境变量中设置 NODE_ENV 变量
6. 在运行平台(Docker、Kubernetes等)中配置环境变量

通常情况下,建议在启动应用时设置 NODE_ENV,这样可以确保在代码运行前已被正确设置。
设置为 production 可以启用一些性能优化,比如预编译模板、跳过错误堆栈跟踪等。
