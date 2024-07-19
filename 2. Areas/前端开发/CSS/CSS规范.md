## CSS规范
在 CSS 中，有一些属性是可以继承的，意味着子元素会继承父元素的属性值。然而，也有一些属性是不可继承的，子元素不会继承父元素的属性值。下面是一些常见的可继承属性和不可继承属性的示例：
可继承属性：

| 可继承属性                | 描述                                                                 |
|--------------------------|----------------------------------------------------------------------|
| font-family              | 字体系列                                                             |
| font-size                | 字号                                                                 |
| font-weight              | 字体粗细                                                             |
| text-align               | 文本对齐方式                                                         |
| color                    | 文本颜色                                                             |
| line-height              | 行高                                                                 |
| margin                   | 外边距                                                               |
| padding                  | 内边距                                                               |
| border                   | 边框                                                                 |
| background               | 背景属性，如背景颜色、背景图片等                                     |
不可继承属性：

| 不可继承属性              | 描述                                                                 |
|--------------------------|----------------------------------------------------------------------|
| width                    | 宽度                                                                 |
| height                   | 高度                                                                 |
| display                  | 显示方式                                                             |
| position                 | 定位方式                                                             |
| float                    | 浮动方式                                                             |
| z-index                  | 层级                                                                 |
| overflow                 | 溢出处理方式                                                         |
| text-decoration          | 文本修饰，如下划线、删除线等                                         |
| box-sizing               | 盒模型属性，如内容盒、边框盒、外边距盒等                             |
| background-position      | 背景位置                                                             |
请注意，这只是一些常见的可继承属性和不可继承属性的示例，实际上还有其他属性也有不同的继承行为。在编写 CSS 样式时，了解属性的继承性质非常重要，以确保样式的正确应用。

在 CSS 中，`..` 是一个特殊的选择器，被称为通用选择器。它可以匹配任何元素。这意味着 `..special` 选择器将选择文档中所有具有 `class` 属性为 `special` 的元素，并将它们的文本颜色设置为蓝色。
下面是一个示例，说明如何使用 `..special` 选择器：
HTML 代码：
```html
<p class="special">这是一个特殊的段落。</p>
<div class="special">这是一个特殊的 div。</div>
<span class="special">这是一个特殊的 span。</span>
```
CSS 代码：
```css
..special {
  color: blue;
}
```
在上面的示例中，所有具有 `class` 属性为 `special` 的元素，无论是 `<p>`、`<div>` 还是 `<span>`，都会应用蓝色的文本颜色。
需要注意的是，通用选择器 `..` 可以匹配任何元素，但它不是常用的选择器，更常见的选择器有类选择器（`.class`）和标签选择器（`tag`）等。


CSSPlayCopy to Clipboard

```
.wrapper {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  grid-template-rows: 100px 100px;
  grid-gap: 10px;
}
```

HTMLPlayCopy to Clipboard

```
<div class="wrapper">
  <div class="box1">One</div>
  <div class="box2">Two</div>
  <div class="box3">Three</div>
  <div class="box4">Four</div>
  <div class="box5">Five</div>
  <div class="box6">Six</div>
</div>
```


```css
.wrapper {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  grid-template-rows: 100px 100px;
  grid-gap: 10px;
}

.box1 {
  grid-column: 2 / 4;
  grid-row: 1;
}

.box2 {
  grid-column: 1;
  grid-row: 1 / 3;
}

.box3 {
  grid-row: 2;
  grid-column: 3;
}

```

这段代码使用了 CSS Grid 布局，定义了三个具有不同位置的盒子（box）。
.box1 的样式规则为：
- `grid-column: 2 / 4;` 表示该盒子跨越从第 2 列到第 4 列。
- `grid-row: 1;` 表示该盒子位于第 1 行。
.box2 的样式规则为：
- `grid-column: 1;` 表示该盒子位于第 1 列。
- `grid-row: 1 / 3;` 表示该盒子跨越从第 1 行到第 3 行。
.box3 的样式规则为：
- `grid-row: 2;` 表示该盒子位于第 2 行。
- `grid-column: 3;` 表示该盒子位于第 3 列。
通过这些样式规则，可以将这三个盒子放置在一个 CSS Grid 布局中的不同位置。这是一种强大的布局技术，可以在网页中创建灵活的网格结构。


`article:nth-of-type(3)` 是一个 CSS 选择器，用于选择文档中第三个出现的 `<article>` 元素。
具体解释如下：
- `article` 是选择器的元素类型，表示选择 `<article>` 元素。
- `:nth-of-type(3)` 是伪类选择器，表示选择第三个出现的该类型的元素。
这个选择器可以用于选择文档中特定位置的 `<article>` 元素，例如选择第三个出现的 `<article>` 元素。
需要注意的是，CSS 选择器中的索引是从 1 开始的，而不是从 0 开始。所以 `:nth-of-type(3)` 表示选择第三个出现的 `<article>` 元素，而不是第二个。
举个例子，如果文档中有如下 HTML 结构：
```html
<article>第一个 article 元素</article>
<article>第二个 article 元素</article>
<article>第三个 article 元素</article>
<article>第四个 article 元素</article>
```
那么 `article:nth-of-type(3)` 将会选择 `<article>第三个 article 元素</article>` 这个元素。



