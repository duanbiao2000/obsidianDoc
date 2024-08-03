---
aliases:

---
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





