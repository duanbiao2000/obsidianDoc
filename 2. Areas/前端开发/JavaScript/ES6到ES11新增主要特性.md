## ES6到ES11新增主要特性:

**ES6**

- let和const
```js
let name = 'John';
const age = 20;
```
- 箭头函数
```js 
let func = (a, b) => a + b;
```
- 模板字符串
```js
let str = `Hello ${name}`; 
```
- 扩展运算符
```js
let arr2 = [...arr1, 4, 5, 6];
```
- Promise
```js
let promise = new Promise((resolve, reject) => {
  // ...
});
```
**ES7** 
- includes()
```js
let arr = [1, 2, 3];
arr.includes(2); // true
```
**ES8**
- async/await
```js
async function test() {
  let data = await fetch(url);
  let json = await data.json();
}
```
**ES9**
- 对象扩展运算符
```js
let obj1 = { a: 1 };
let obj2 = { b: 2, ...obj1 }; 
```
**ES10**
- flat()和flatMap()
```js
[1, [2, 3]].flat(); // [1, 2, 3]
```
**ES11** 
- 可选链操作符
```js
let name = user?.name; 
```
- 空值合并运算符
```js
let name = user ?? 'Anonymous';
```
 
 这里给出几个实用的 ES6 - ES11 的代码示例:
**1. 数组去重**

```js
// ES6
function unique(arr) {
  return Array.from(new Set(arr));
}
// ES11
function unique(arr) {
  return [...new Set(arr)];
}
```
**2. 动态属性名**
```js
// ES6
let prop = 'name';
let obj = {
  [prop]: 'John'
};
// ES11
let obj = {
  name
};
```
**3. 可选链调用**
```js
// ES11
let name = user?.profile?.name;
```
**4. 合并对象**
```js 
// ES6
Object.assign(obj1, obj2);
// ES11
let merged = {...obj1, ...obj2};
```
**5. 异步函数**
```js
// ES8
async function fetchData() {
  let res = await fetch(url);
  let data = await res.json();
  return data; 
}
```

**默认参数**

```js
function foo(x = 2) {
  return x; 
}
foo(); // 2
```
**rest参数**
```js 
function sum(...numbers) {
  return numbers.reduce((a, b) => a + b);
}
sum(1, 2, 3); // 6
```
**for...of循环**
```js
for (let num of [1, 2, 3]) {
  console.log(num);
}
```
**Promise.all**
```js
Promise.all([p1, p2]).then(values => {
  // ...
});
```
**正则扩展 - 具名组匹配**
```js
const regex = /(?<year>\d{4})-(?<month>\d{2})/;
const match = regex.exec('2022-01');
match.groups.year; // '2022'
match.groups.month; // '01'
```
**BigInt**
```js
const bigint = 1234567890123456789012345678901234567890n; 
```
**可选链操作符**
```js
let name = user?.profile?.name;
```
