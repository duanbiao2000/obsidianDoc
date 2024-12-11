### arguments和展开运算符(...)

在JavaScript中，`arguments` 和 `...` 都用于传递参数。但是它们使用方法略有不同。

`arguments`是一个类数组对象，包含函数调用时传递的所有参数。您可以使用 `arguments` 对象来访问所有参数，并以数组或类似数组的方式进行迭代和操作。例如：

```javascript
function sum() {
  let result = 0;
  
  for (let i = 0; i < arguments.length; i++) {
    result += arguments[i];
  }
  
  return result;
}

console.log(sum(1, 2, 3, 4, 5)); // 15
```

在这个示例中，我们定义了一个名为 "sum" 的函数，并使用 `arguments` 对象来获取所有传递给该函数的参数并将它们加起来。

相反，`...`（称为“展开语法”或“展开运算符”）可用于将数组、对象、函数等扩展为独立的参数列表。例如：

```javascript
const arr = [1, 2, 3, 4, 5];

console.log(...arr); // 1 2 3 4 5

function sum(x, y, z) {
  return x + y + z;
}

console.log(sum(...arr.slice(0, 3))); // 6
```

在这个示例中，我们首先使用 `...` 将 `arr` 数组的所有元素传递给 `console.log()` 函数进行打印。然后，我们使用 `...` 将 `arr.slice(0, 3)` 的结果作为三个参数传递给 `sum()` 函数，从而计算前三个元素的总和。

虽然 `arguments` 和 `...` 都用于传递参数，但它们使用起来略有不同：`arguments` 对象允许您动态获取所有传入函数的参数，而 `...` 允许您将数组或对象等数据结构展开成独立的参数。至于哪一个更好，取决于您的具体场景和需求。