---
aliases: 
theme: 
high_priority: false
tags:
---
# Mongoose标准流程
Mongoose 提供了一系列强大的功能来与 MongoDB 数据库交互。这里列举一些 Mongoose 中常用的数据库操作示例，包括创建、读取、更新和删除（CRUD）数据等。

### 1. 定义 Schema 和 Model
首先需要定义一个 schema 来描述你的文档结构，并基于该 schema 创建一个 model。

```javascript
const mongoose = require('mongoose');
const { Schema } = mongoose;

// 定义一个Schema
const userSchema = new Schema({
    name: String,
    email: { type: String, unique: true },
    password: String,
    age: Number,
    createdAt: { type: Date, default: Date.now }
});

// 基于Schema创建Model
const User = mongoose.model('User', userSchema);
```

### 2. 插入文档 (Create)
使用 `save()` 方法或 `create()` 方法插入新文档。

```javascript
// 使用 save()
const newUser = new User({ name: 'John Doe', email: 'john@example.com', password: 'secret' });
await newUser.save();

// 或者使用 create()
await User.create({ name: 'Jane Doe', email: 'jane@example.com', password: 'password' });
```

### 3. 查询文档 (Read)
使用 `find()`, `findOne()`, `findById()` 等方法查询文档。

```javascript
// 查找所有用户
const users = await User.find();

// 根据条件查找单个用户
const user = await User.findOne({ email: 'john@example.com' });

// 根据ID查找用户
const specificUser = await User.findById(someUserId);
```

### 4. 更新文档 (Update)
使用 `updateOne()`, `updateMany()`, `findOneAndUpdate()` 等方法更新文档。

```javascript
// 更新第一个匹配到的用户
await User.updateOne({ email: 'john@example.com' }, { $set: { name: 'Johnny Doe' } });

// 更新所有符合条件的用户
await User.updateMany({ age: { $gt: 18 } }, { $set: { status: 'adult' } });

// 找到并更新一条记录，并返回更新后的文档
const updatedUser = await User.findOneAndUpdate(
    { email: 'john@example.com' },
    { $set: { name: 'John Smith' } },
    { new: true } // 返回更新后的文档
);
```

### 5. 删除文档 (Delete)
使用 `deleteOne()`, `deleteMany()`, `findByIdAndDelete()` 等方法删除文档。

```javascript
// 删除第一个匹配到的用户
await User.deleteOne({ email: 'john@example.com' });

// 删除所有符合条件的用户
await User.deleteMany({ age: { $lt: 18 } });

// 根据ID删除用户
await User.findByIdAndDelete(someUserId);
```

### 6. 分页与排序
可以结合 `skip()` 和 `limit()` 进行分页处理，并用 `sort()` 对结果进行排序。

```javascript
// 获取第2页的数据，每页显示10条记录
const perPage = 10;
const page = 2;
const users = await User.find()
    .skip((page - 1) * perPage)
    .limit(perPage)
    .sort({ createdAt: -1 }); // 按创建时间降序排列
```

### 7. 聚合管道
Mongoose 支持 MongoDB 的聚合框架，可以用来执行复杂的查询和转换操作。

```javascript
const result = await User.aggregate([
    { $match: { age: { $gte: 18 } } }, // 匹配年龄大于等于18岁的用户
    { $group: { _id: '$status', count: { $sum: 1 } } } // 按状态分组并计算每个状态下的用户数量
]);
```

以上是一些基本的 Mongoose 操作示例。Mongoose 功能非常强大，支持更复杂的数据模型定义、中间件、虚拟属性等功能。对于更详细的信息，建议查阅官方文档。
