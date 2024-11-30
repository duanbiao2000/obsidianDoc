---
aliases: 
tags: 
theme: 
original: 
url: 
author: 
date_created: 2024-07-14 17:02
type: 
priority: false
---
### 使用 `replacer` 函数
假设我们有一个对象，其中包含一些我们不想序列化的属性，我们可以使用 `replacer` 函数来排除这些属性。

```javascript
const obj = {
  name: 'John Doe',
  age: 30,
  email: 'john.doe@example.com',
  password: 'supersecret'
};

// 使用 replacer 函数来排除 password 属性
const replacer = function(key, value) {
  if (key === 'password') return undefined; // 不序列化 password
  return value;
};

const jsonString = JSON.stringify(obj, replacer);
console.log(jsonString);
```

### 使用 `reviver` 函数
假设我们的 JSON 字符串中包含日期，我们希望在解析时将这些字符串转换为 `Date` 对象。

```javascript
const jsonString = `
{
  "name": "John Doe",
  "age": 30,
  "birthday": "1993-01-01"
}
`;

// 使用 reviver 函数来转换日期字符串为 Date 对象
const reviver = function(key, value) {
  if (key === 'birthday' && typeof value === 'string') {
    return new Date(value);
  }
  return value;
};

const obj = JSON.parse(jsonString, reviver);
console.log(obj.birthday instanceof Date); // true
```

在这两个例子中：
- `replacer` 函数被用于从 JSON 输出中排除敏感信息。
- `reviver` 函数被用于在解析 JSON 字符串时转换特定的数据类型。

这些函数可以让你在序列化和反序列化过程中有更精细的控制，以适应特定的应用需求。