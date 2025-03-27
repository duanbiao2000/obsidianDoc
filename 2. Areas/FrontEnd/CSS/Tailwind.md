
**问题1：在`styles`对象中，`innerWidth` 属性的主要目的是什么？**
?
A. 设置元素的内部垂直边距。
B. 限定内容的最大宽度为1280px，并在不同屏幕尺寸下调整宽度。
C. 定义元素之间的间距宽度。
D. 使元素在水平和垂直方向上都居中。

**问题2：`flexCenter` 样式使用了哪组Tailwind CSS类来实现垂直和水平居中？**
?
A. `flex justify-start items-start`
B. `flex justify-center items-start`
C. `flex justify-center items-center`
D. `flex justify-end items-center`

**问题3：在 `x` 样式中，`sm:px-16` 这个类名的含义是什么？**
?
A. 在小屏幕（sm）及以上尺寸，设置左右内边距为16px。
B. 在小屏幕（sm）及以上尺寸，设置左右内边距为Tailwind间距单位的16（通常是4rem）。
C. 在小屏幕（sm）及以上尺寸，设置最小宽度为16px。
D. 在小屏幕（sm）及以上尺寸，设置左右外边距为16px。

**问题4：根据 `heroHeading` 的样式定义，哪个Tailwind类名用于设置标题文本为粗体？**
?
A. `uppercase`
B. `text-white`
C. `font-bold`
D. `lg:text-[144px]`

**问题5：`export default styles;` 这行代码的作用是什么？**
?
A. 仅在当前文件中定义和使用 `styles` 对象。
B. 将 `styles` 对象导出，以便应用程序的其他部分或文件可以导入并使用这些预定义的样式。
C. 自动将这些样式应用到所有的HTML元素上。
D. 将 `styles` 对象中的类名与Tailwind的默认样式合并。

**问题6：`heroDText` 样式中 `rounded-r-[50px]` 类名的作用是什么？**
?
A. 设置元素所有角的圆角半径为50px。
B. 设置元素左侧的圆角半径为50px。
C. 设置元素右侧的圆角半径为50px。
D. 设置元素的边框宽度为50px。

---
**答案：**
1. B
2. C
3. B
4. C
5. B
6. C

#### Sources:
- [Tailwind](obsidian://open?vault=obsidianDoc&file=Tailwind)
- [flowbite-react](obsidian://open?vault=obsidianDoc&file=flowbite-react)
- [cn函数](obsidian://open?vault=obsidianDoc&file=cn%E5%87%BD%E6%95%B0)
- [实际项目中,对于卡片鼠标悬浮会添加那些样式@20250325_114053](obsidian://open?vault=obsidianDoc&file=%E5%AE%9E%E9%99%85%E9%A1%B9%E7%9B%AE%E4%B8%AD%2C%E5%AF%B9%E4%BA%8E%E5%8D%A1%E7%89%87%E9%BC%A0%E6%A0%87%E6%82%AC%E6%B5%AE%E4%BC%9A%E6%B7%BB%E5%8A%A0%E9%82%A3%E4%BA%9B%E6%A0%B7%E5%BC%8F%4020250325_114053)

 ```js
// 1. 定义样式对象
const styles = {
  // 2. 内容宽度
  // 限定内容最大宽度为1280px,响应式设计
  innerWidth: '2xl:max-w-[1280px] w-full',   
  // 3. 间距宽度
  // 中间容器80%宽度,响应式100%宽度  
  interWidth: 'lg:w-[80%] w-[100%]',
  // 4. 边距
  // 小屏幕padding为12px,其他为8px
  paddings: 'sm: py-12',
  // 5. Y轴边距 
  // 小屏幕下边距为16px,其他为12px
  y: 'sm:py-16 xs:py-8 py-12',
  // 6. X轴边距
  // 小屏幕左边距为16px,其他为6px
  x: 'sm:px-16 px-6',
  // 7. 上边距
  // 小屏幕上边距为16px,其他为12px  
  top: 'sm:pt-16 xs:pt-8 pt-12',
  // 8. 下边距
  // 小屏幕下边距为16px,其他为12px
  bottom: 'sm:-16 xs:-8 pb-12',
  // 9. 垂直居中
  // 垂直和水平居中
  flexCenter: 'flex justify-center items-center',
  // 10. 左对齐
  // 左对齐顶部
  flexStart: 'flex justify-start items-start',
  // 11. 右对齐
  // 右对齐
  flexEnd: 'flex justify-end',
  // 12. 导航栏边距
  // 上边距98px
  navPadding: 'pt-[98px]',
  // 13. 标题样式
  heroHeading: '...',
  // 14. 文字样式
  heroDText: '...'
}
// 15. 导出样式
export default styles;
```
完整注释了每个样式类的含义。
 ```js
// 13. 标题样式
heroHeading: '
  // 粗体大标题
  // 小屏幕60px标题,其他依次放大
  // 大屏幕144px
  // 首字母大写 
  font-bold lg:text-[144px] md:text-[100px] sm:text-[60px] text-[44px] lg:leading-[158.4px] md:leading-[114.4px] sm:leading-[74.4px] leading-[64.4px] uppercase text-white',
// 14. 文字样式
heroDText: '
  // 中屏幕212px宽
  // 小屏幕80px宽
  // 高度依次减小
  // 边框宽度依次减小
  // 边框圆角50px
  // 边框颜色白色
  // 水平间距依次增加
  md:w-[212px] sm:w-[80px] w-[60px] md:h-[108px] sm:h-[48px] h-[38px] md:border-[18px] border-[9px] rounded-r-[50px] border-white sm:mx-2 mx-[6px]',
```


