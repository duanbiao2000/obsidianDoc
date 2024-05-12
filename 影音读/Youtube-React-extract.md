# React Responsive Gym Website Tutorial Using ReactJs | React js Projects for Beginners | Deploy
https://www.youtube.com/watch?v=gpqoZQ8GNK8
![[Pasted image 20230903161318.png]]
当应用程序样式中的 :root 选择器表示文档根元素，定义了可以在整个文档中使用的 CSS 变量。
```
:root {
  --lightgray: #D9D9D9;
  --gray: #9c9c9c;
  --orange: #f48915;
  --darkGrey: #u64D53;
  --caloryCard: #656565;
  --planCard: linear-gradient(210.41deg, #fa5042 1.14%, #ffa739 100.75%);
  --appColor: #3c3f45;
}
```
解释：
- `--caloryCard` 变量：代表卡片元素的颜色值（#656565）。
- `--planCard` 变量：代表计划卡片的背景线性渐变。
- `--appColor` 变量：代表整个应用程序的背景颜色。
另外，其它样式应用到 `.App` 类的元素上：
```
.App {
  background-image: url(data:image/png;base64,iVBORwOKGgoAAAANSUhEUgAAADIAAAAyCAMA);
  mix-blend-mode: overlay;
  background-color: var(--appColor);
  display: flex;
  flex-direction: column;
  gap: 6rem;
  overflow: hidden;
}
```
解释：
- `background-image`：设置元素的背景图像。
- `mix-blend-mode`：指定元素的混合模式。
- `background-color`：使用 `--appColor` 变量设置元素的背景颜色。
- `display: flex`：将元素显示为 flex 容器。
- `flex-direction: column`：在纵向列中排列 flex 子项。
- `gap: 6rem`：设置 flex 子项之间的间距。
- `overflow: hidden`：隐藏溢出的内容。

`url(data:image/png;base64,iVBORwOKGgoAAAANSUhEUgAAADIAAAAyCAMA)` 是一个用于作为背景图像的 data URI。它表示的是一个 PNG 图像的 Base64 编码。在这个例子中，Base64 编码的图像数据被直接嵌入到 CSS 中，而不是通过一个外部的图像文件来引用。
`mix-blend-mode: overlay` 是一个 CSS 混合模式，它应用于元素的背景和其父元素（或者前面的兄弟元素）的背景之间的混合效果。使用 `overlay` 混合模式，元素的背景颜色和图像将以一种叠加的方式进行混合。
这样的组合可以用于创建一些视觉效果，例如将背景图像与父元素的背景颜色混合，让图像在背景中显示出来，并以一种叠加的方式融入到背景中。效果取决于元素和其父元素的具体样式设置。
需要注意的是，由于 Base64 编码的图像数据会增加 CSS 文件的大小，因此对于较大的图像来说，这种方式可能不太适合。此外，混合模式也可能会对性能产生一定的影响，因此要谨慎使用。
![[Pasted image 20230903162837.png]]
![[Pasted image 20230903163144.png]]

例如，如果有以下 CSS 规则：

```css
.element {
  padding: 2rem;
  padding-top: 1.5rem;
}
```

那么 `padding` 属性设置的内边距为 2rem，`padding-top` 属性设置的内边距为 1.5rem。由于 `padding-top` 是在 `padding` 之后设置的，它会叠加在 `padding` 属性的基础上。

最终的效果是，元素的上内边距为 1.5rem，而其他方向的内边距（右、下、左）仍为 2rem。

这种覆盖效果适用于所有的 `padding` 相关属性，例如 `padding-bottom`、`padding-right`、`padding-left` 等。
需要注意的是，如果在同一个属性中多次设置相同的 `padding` 值，那么后面的设置将覆盖前面的设置。例如：

```css
.element {
  padding: 2rem;
  padding: 1.5rem;
}
```
在这种情况下，最终的内边距将是 1.5rem，前面的设置被后面的设置覆盖。

![[Pasted image 20230903163556.png]]
`ul>li*5`

![[Pasted image 20230903164609.png]]
![[Pasted image 20230903164722.png]]
![[Pasted image 20230903164812.png]]
![[Pasted image 20230903164905.png]]
![[Pasted image 20230903165010.png]]
![[Pasted image 20230903164922.png]]

