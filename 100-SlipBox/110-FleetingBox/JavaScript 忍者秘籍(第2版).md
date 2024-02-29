---
aliases:

---
20230816 1317
links:
title:
origin:
tags: #flashcards #todo 

![[Pasted image 20230816131911.png]]

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
这段代码展示了一个生成器函数 `NinjaGenerator` 和生成器对象 `ninjaIterator` 的使用。
- `function* NinjaGenerator(action)`：这是一个生成器函数的定义。它接受一个参数 `action`。
- `const imposter = yield ("Hattori " + action);`：这是生成器函数中的一个生成器暂停点。`yield` 关键字用于产生一个值，并暂停生成器的执行。在这里，它产生了 `"Hattori " + action` 的值，并将其赋给 `imposter` 变量。
- `assert(imposter === "Hanzo", "The generator has been infiltrated");`：这是一个断言语句，用于检查 `imposter` 变量的值是否为 `"Hanzo"`。如果断言失败，将抛出一个错误，提示“生成器已被渗透”。
- `const ninjaIterator = NinjaGenerator("skulk");`：创建了一个生成器对象 `ninjaIterator`，通过调用 `NinjaGenerator` 生成器函数并传入参数 `"skulk"` 来进行初始化。
- `const result1 = ninjaIterator.next();`：调用生成器对象的 `next` 方法，开始执行生成器函数，并将生成器暂停点的值赋给 `result1`。
- `assert(result1.value === "Hattori skulk", "Hattori is skulking");`：断言语句，用于检查 `result1.value` 是否等于 `"Hattori skulk"`。
- `const result2 = ninjaIterator.next("Hanzo");`：调用生成器对象的 `next` 方法，并传入参数 `"Hanzo"`，以恢复生成器的执行。
- `assert(result2.value === "Yoshi (Hanzo) skulk", "We have an imposter!");`：断言语句，用于检查 `result2.value` 是否等于 `"Yoshi (Hanzo) skulk"`。
这段代码演示了生成器函数的执行过程，并展示了如何使用断言语句来验证生成器函数的输出值。

在生成器函数 `NinjaGenerator` 中，`imposter` 是一个通过 `yield` 语句接收传入值的变量。在第一次调用 `ninjaIterator.next()` 时，生成器函数会执行到第一个 `yield` 语句处，并返回了 `"Hattori " + action` 的值，即 `"Hattori skulk"`。
在第二次调用 `ninjaIterator.next("Hanzo")` 时，传入的参数 `"Hanzo"` 会被赋值给上一个 `yield` 语句的左侧变量 `imposter`。这是通过将传入的参数作为 `next` 方法的参数来实现的。
因此，在第二次调用后，`imposter` 的值将为 `"Hanzo"`。
<font color="#d831a8">在生成器函数中，`yield` 语句的右侧是生成器的输出值，而左侧是生成器的输入值。通过 `yield` 语句，生成器函数能够与外部世界进行双向通信。</font>
需要注意的是，第一次调用 `ninjaIterator.next()` 时，并没有传入任何参数，因此 `imposter` 的值为 `undefined`。在第二次调用时，传入的参数 `"Hanzo"` 被赋值给 `imposter`。


