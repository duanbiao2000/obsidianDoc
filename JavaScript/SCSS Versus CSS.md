#Vue 

[十分钟，带你了解 Vue3 的新写法 - 掘金 (juejin.cn)](https://juejin.cn/post/7225267685763907621)

### 三省: SCSS Versus CSS

 SCSS和普通CSS的主要区别如下:
1. 变量
SCSS支持使用$变量,可以为颜色、尺寸等定义变量,方便重复使用。
2. 嵌套规则
SCSS允许选择器嵌套,可以更清晰地定义元素层次关系。
3. 导入
SCSS支持@import导入其他SCSS文件规则。
4. 混合(mixin) 
SCSS定义的混合规则可以被重复调用,实现代码复用。
5. 继承
SCSS支持选择器继承其他选择器的属性。
6. 函数
SCSS提供了许多内置函数用于处理颜色、数字等。
7.运算
SCSS支持基本的数学运算符用于计算值。
8.注释
SCSS支持标准CSS注释以外,还支持//注释和/*!*/注释。
9.编译
SCSS需要通过预处理器编译为标准CSS,以便浏览器解析。
总体来说:
- SCSS支持变量、嵌套、导入、mixin、继承等CSS预处理器特性。
- SCSS需要预处理编译为CSS,CSS直接被浏览器解析。
- SCSS使CSS更强大和可维护。
所以SCSS相比CSS增加了很多CSS预处理器特性,但需要额外的编译步骤。


 这里举几个SCSS的例子来说明它与普通CSS的主要区别:
1. 变量
SCSS:
```scss
$font-size: 12px;
$color: #fff;
body {
  font-size: $font-size;
  color: $color; 
}
```
CSS没有变量的概念。
2. 嵌套规则
SCSS: 
```scss
nav {
  ul {
    margin: 0;
    padding: 0;
    list-style: none;
  }
  li {
    display: inline-block;
  }
}
```
CSS需要重复写选择器:
```css
nav ul {
  margin: 0;
  padding: 0;
  list-style: none;
}
nav li {
  display: inline-block;
}
```
3. 混合
SCSS:
```scss
@mixin center {
  display: flex;
  align-items: center;
  justify-content: center;
}
.btn {
  @include center;
}
.icon {
  @include center;
}
```
CSS没有混合的概念。
4. 继承
SCSS:
```scss
.message {
  border: 1px solid #ccc;
  padding: 10px;
  color: #333;
}
.success {
  @extend .message;
  border-color: green;
}
```
CSS无法实现继承。
所以通过这些例子可以看出SCSS相比CSS提供了更强大的功能。




以下是 SCSS 相比 CSS 的一些好处：

1. 变量

   SCSS 支持变量，可以定义多次使用的颜色、字体大小等属性的值，并在整个 SCSS 文件中引用。这使得样式表更易于维护和修改。

   ```scss
   $primary-color: #007bff;
   .button {
     background-color: $primary-color;
   }
   ```

2. 嵌套规则

   SCSS 允许嵌套规则，可以将内部选择器作为其他选择器的子项来编写样式规则，并且可以避免重复编写选择器。这使得代码更简洁和易读。

   ```scss
   .nav {
     ul {
       margin: 0;
       padding: 0;
       list-style: none;

       li {
         display: inline-block;
         margin: 0 10px;

         a {
           color: #333;
           text-decoration: none;
         }
       }
     }
   }
   ```

3.  混合器

   SCSS 允许创建混合器，以便在样式表中重复使用一组 CSS 属性。混合器类似于函数，可以传递参数，并且可以在 CSS 规则中任何位置调用。

   ```scss
   @mixin border-radius($radius) {
     -webkit-border-radius: $radius;
     -moz-border-radius: $radius;
     -ms-border-radius: $radius;
     border-radius: $radius;
   }

   .box {
     @include border-radius(10px);
   }
   ```

4. 集成

   SCSS 文件可以包含普通的 CSS 代码，并且大部分现有的 CSS 样式表都可以重用和集成到 SCSS 中。这使得 SCSS 更加开放和灵活。

   ```scss
   // 导入 Bootstrap 样式库
   @import "~bootstrap/scss/bootstrap";

   // 普通的 CSS 规则
   body {
     background-color: #f8f9fa;
   }
   ```

综上所述，SCSS 可以让我们编写更加高效、灵活和易于维护的样式表。尽管学习曲线较陡峭，但它的优点还是非常明显的。

