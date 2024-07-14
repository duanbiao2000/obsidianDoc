---
aliases:

---

![[assets/img/JavaScript 忍者秘籍(第2版)/IMG-JavaScript 忍者秘籍(第2版)-20240714145113571.png]]

以下是经过格式化和注释的代码：
```javascript
function* NinjaGenerator(action) {
  const imposter = yield ("Hattori " + action);
  
  // 断言: 检查 imposter 是否等于 "Hanzo"
  assert(imposter === "Hanzo", "The generator has been infiltrated");
  
  yield ("Yoshi (" + imposter + ") " + action);
}
// 创建一个 NinjaGenerator 生成器对象
const ninjaIterator = NinjaGenerator("skulk");
// 调用生成器的 next 方法，开始执行生成器函数
const result1 = ninjaIterator.next();
// 断言: 检查 result1.value 是否等于 "Hattori skulk"
assert(result1.value === "Hattori skulk", "Hattori is skulking");
// 调用生成器的 next 方法，并传入参数 "Hanzo"
const result2 = ninjaIterator.next("Hanzo");
// 断言: 检查 result2.value 是否等于 "Yoshi (Hanzo) skulk"
assert(result2.value === "Yoshi (Hanzo) skulk", "We have an imposter!");
```

<font color="#d831a8">在生成器函数中，`yield` 语句的右侧是生成器的输出值，而左侧是生成器的输入值。通过 `yield` 语句，生成器函数能够与外部世界进行双向通信。</font>



