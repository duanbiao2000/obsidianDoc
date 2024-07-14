
# 过滤器

在Vue中，过滤器是用来格式化文本或者实现一些简单的数据变换的功能。Vue 中分为全局过滤器和局部过滤器。下面分别列举它们的代码并逐行注释。

全局过滤器：

```javascript
// 定义一个名字为 capitalize 的全局过滤器
Vue.filter('capitalize', function (value) {
  // 进行字符串转换处理
  if (!value) return ''
  value = value.toString()
  // 首字母大写并返回处理后的字符串
  return value.charAt(0).toUpperCase() + value.slice(1)
})
```

注解：这里我们定义了一个名为`capitalize`的全局过滤器，该过滤器需要传入一个参数 `value`进行处理。首先判断传入值是否为空字符串，如果不为空，则将该值转成字符串，并将首字母转成大写。最后返回字符串。

使用该全局过滤器：

```html
<!-- 将message的值转换成首字母大写 -->
<div>{{ message | capitalize }}</div>
```

注解：在 Vue 实例内，可以使用管道符(|)调用 `capitalize` 全局过滤器，将message的值进行首字母大写转换。

局部过滤器：

```html
<!-- 定义一个名字为 currency 的局部过滤器-->
<template>
  <div>
    {{ price | currency }}
  </div>
</template>

<script>
export default {
  // 在组件选项对象中注册一个名为 currency 的局部过滤器
  filters: {
    currency(value) {
      // 实现货币单位 "￥" 前缀
      return '￥' + Number.parseFloat(value).toFixed(2)
    }
  },
  data() {
    return {
      price: 29.9
    }
  }
}
</script>
```

注解： 在上面的代码中，我们定义了一个名为 `currency` 的局部过滤器，其目的是在数字前面添加 `￥` 货币单位，并将数据保留小数点后两位。补充一个组件，通过组件显示该结果。

需要注意的是，全局过滤器的注册只需要在 Vue 实例中执行一次，适用于大部分组件内都需要使用相同过滤器的场景，而局部过滤器适合于仅在某个组件中使用的场景，以避免与其他组件可能存在冲突和性能问题。