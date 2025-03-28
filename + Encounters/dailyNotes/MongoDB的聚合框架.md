---
aliases: 
categories: 
high_priority: false
tags:
---
MongoDB 的聚合框架是一个强大的工具，用于处理和分析数据。它允许你对文档进行复杂的操作，如过滤、分组、排序、计算等。聚合框架使用管道（pipeline）的概念，每个阶段（stage）都对前一个阶段的结果进行操作，最终输出所需的数据。
### 基本概念
1. **Pipeline**：聚合操作由一系列的阶段（stages）组成，这些阶段按顺序执行。
2. **Stages**：每个阶段都是一个特定的操作，例如 `$match` 用于过滤文档，`$group` 用于分组文档，`$sort` 用于排序文档等。
3. **Operators**：每个阶段可以使用各种操作符来实现具体的功能，例如 `$eq` 用于相等比较，`$sum` 用于求和等。
### 常见的聚合阶段
假设我们有一个 `users` 集合，包含用户的姓名、年龄和兴趣爱好。我们希望找到所有年龄大于 18 岁的用户，按年龄降序排序，然后随机选取 10 个用户，并计算他们的平均年龄。
```javascript
const result = await User.aggregate([
  // 过滤出年龄大于 18 岁的用户
  {
    $match: {
      age: { $gt: 18 }
    }
  },
  // 按年龄降序排序
  {
    $sort: {
      age: -1
    }
  },
  // 随机选取 10 个用户
  {
    $sample: {
      size: 10
    }
  },
  // 计算这 10 个用户的平均年龄
  {
    $group: {
      _id: null,
      averageAge: { $avg: "$age" },
      users: { $push: "$$ROOT" } // 将原始文档推入数组
    }
  }
]);
console.log(result);
```
是的，你提供的代码使用了 MongoDB 的聚合框架来随机选取 10 个与指定用户 `_id` 不同的用户。具体来说：
- `$match` 阶段用于过滤出 `_id` 不等于 `userId` 的文档。
- `$sample` 阶段用于从上一个阶段的结果中随机选取 10 个文档。
### 随机选取
```javascript
const users = await User.aggregate([
  {
    $match: {
      _id: { $ne: userId },
    },
  },
  { $sample: { size: 10 } },
]);
```
这段代码确实是从符合条件的用户中随机选取 10 个用户。
### 其他选取方式
除了随机选取外，还有其他几种常见的选取方式，例如按条件排序、分页等。以下是一些示例：
#### 1. 按某个字段排序并选取前 N 个
假设你想按用户的注册时间（`createdAt` 字段）降序排列，并选取最新的 10 个用户：
```javascript
const users = await User.aggregate([
  {
    $match: {
      _id: { $ne: userId },
    },
  },
  { $sort: { createdAt: -1 } }, // 按 createdAt 降序排列
  { $limit: 10 }, // 选取前 10 个
]);
```
#### 2. 分页选取
假设你想实现分页功能，每页显示 10 个用户，当前是第 2 页：
```javascript
const page = 2; // 当前页码
const pageSize = 10; // 每页显示的用户数量
const skip = (page - 1) * pageSize;
const users = await User.aggregate([
  {
    $match: {
      _id: { $ne: userId },
    },
  },
  { $skip: skip }, // 跳过前面的记录
  { $limit: pageSize }, // 选取接下来的 10 个
]);
```
#### 3. 按地理位置距离选取
假设你想根据用户的地理位置信息（如 `location` 字段），选取离某个坐标最近的 10 个用户：
```javascript
const location = { type: "Point", coordinates: [longitude, latitude] };
const users = await User.aggregate([
  {
    $match: {
      _id: { $ne: userId },
      location: {
        $near: {
          $geometry: location,
          $maxDistance: 5000, // 最大距离为 5000 米
        },
      },
    },
  },
  { $limit: 10 }, // 选取前 10 个
]);
```
### 总结
- **随机选取**：使用 `$sample` 阶段。
- **按条件排序**：使用 `$sort` 阶段。
- **分页选取**：使用 `$skip` 和 `$limit` 阶段。
- **按特定条件筛选**：使用 `$match` 阶段。
- **按地理位置距离选取**：使用 `$near` 操作符。
根据你的具体需求，可以选择适合的选取方式。希望这些示例对你有所帮助！
