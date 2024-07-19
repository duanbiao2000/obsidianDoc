---
aliases: 
tags: 
theme: 
original: 
url: 
author: 
created_date: 
date updated: 2024-07-14 17:02
type: 
high priority: false
---
以下是关于 `JSON.parse` 和 `JSON.stringify` 方法的关键要点列表：

### JSON.stringify
1. 将 JavaScript 值转换为 JSON 字符串。
2. 可以接受一个[[`replacer` 和 `reviver` 函数|replacer]]函数或数组作为第二个参数，用于定制序列化过程。
3. 可以接受一个 spaces 参数，用于指定输出的缩进空格数，便于阅读。
4. 会忽略函数和符号(Symbol)类型的属性。
5. 无法序列化循环引用的数据结构，会抛出错误或忽略循环部分。
6. 不会序列化对象的原型链上的属性，仅序列化实例属性。

### JSON.parse
1. 将 JSON 字符串转换回 JavaScript 值。
2. 可以接受一个[[`replacer` 和 `reviver` 函数|reviver]]函数作为第二个参数，用于定制反序列化过程。
3. 如果 JSON 字符串格式不正确，会抛出 `SyntaxError`。
4. 能够解析基本类型、数组和对象，但不能解析函数或正则表达式。
5. 解析的结果是全新的对象或值，不共享原始数据的引用。

这些要点概括了 `JSON.stringify` 和 `JSON.parse` 的主要功能和限制。

