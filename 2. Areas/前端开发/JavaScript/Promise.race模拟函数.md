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
`Promise.race` 是一个 Promise 静态方法，它接收一个 Promise 对象的数组作为参数，一旦数组中的某个 Promise 解决或拒绝，`Promise.race` 就会立即以相同的解决值或拒绝原因返回一个新的 Promise。


```javascript
function race(promises) {
    return new Promise((resolve, reject) => {
        if (!Array.isArray(promises)) {
            throw new TypeError('promises must be an array');
        }

        promises.forEach((promise, index) => {
            if (typeof promise !== 'object' || typeof promise.then !== 'function') {
                reject(new TypeError(`promise at index ${index} is not an object or does not have a then function`));
                return;
            }

            promise.then(resolve, reject);
        });
    });
}

// 使用示例
const p1 = new Promise((resolve) => setTimeout(() => resolve('Promise 1 resolved'), 2000));
const p2 = new Promise((resolve) => setTimeout(() => resolve('Promise 2 resolved'), 1000));
const p3 = new Promise((resolve, reject) => setTimeout(() => reject('Promise 3 rejected'), 500));

race([p1, p2, p3])
    .then(result => console.log('Resolved:', result))
    .catch(error => console.error('Rejected:', error));
```

这段代码中定义的 `race` 函数接受一个 Promise 数组作为参数。对于数组中的每个 Promise，我们通过调用其 `then` 方法注册解决和拒绝的回调。这样，不论哪个 Promise 最先完成（无论是解决还是拒绝），都会调用相应的回调，并且 `race` 返回的 Promise 也会以相同的状态结束。如果传入的参数不是数组或者数组中的元素不是 Promise 对象，则会抛出错误。