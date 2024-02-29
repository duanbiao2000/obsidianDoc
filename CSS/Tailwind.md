
```js
const styles = {
  innerWidth: '2xl:max-w-[1280px] w-full',
  interWidth: 'lg:w-[80%] w-[100%]',

  paddings: 'sm:p-16 xs:p-8 px-6 py-12',
  yPaddings: 'sm:py-16 xs:py-8 py-12',
  xPaddings: 'sm:px-16 px-6',
  topPaddings: 'sm:pt-16 xs:pt-8 pt-12',
  bottomPaddings: 'sm:pb-16 xs:pb-8 pb-12',

  flexCenter: 'flex justify-center items-center',
  flexStart: 'flex justify-start items-start',
  flexEnd: 'flex justify-end',
  navPadding: 'pt-[98px]',

  // hero section
  heroHeading:
      'font-bold lg:text-[144px] md:text-[100px] sm:text-[60px] text-[44px] lg:leading-[158.4px] md:leading-[114.4px] sm:leading-[74.4px] leading-[64.4px] uppercase text-white',
  heroDText:
      'md:w-[212px] sm:w-[80px] w-[60px] md:h-[108px] sm:h-[48px] h-[38px] md:border-[18px] border-[9px] rounded-r-[50px] border-white sm:mx-2 mx-[6px]',
};

export default styles;
```
完整注释了每个样式类的含义。

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
完整注释了标题和文字样式的含义。


![(88) Build and Deploy a Modern Next 13 Website With Framer Motion & Tailwind CSS - YouTube](https://www.youtube.com/watch?v=ugCN_gynFYw)
源码地址: [project_metaverse/components/Navbar.jsx at main · adrianhajdin/project_metaverse (github.com)](https://github.com/adrianhajdin/project_metaverse/blob/main/components/Navbar.jsx#L3)
Next.js会自动将public文件夹中的静态资源映射到根路径下。
也就是说,public文件夹中的文件可以直接通过根路径访问,不需要任何前缀。
例如:
- public/image.png 可以通过 /image.png 访问
- public/js/script.js 可以通过 /js/script.js 访问
这是因为Next.js会在构建时将public文件夹中的所有文件copy到输出目录下。
所以在页面中引用public文件夹中的图片/文件时,可以直接使用相对路径:
```jsx
<img src="/image.png"/>
<script src="/js/script.js"></script> 
```
Next.js会自动匹配到public文件夹中的文件。
这一特性带来的好处是:
- 可以很方便地引用静态资源
- 无需关心资源路径
- 部署后也可以直接通过根路径访问
所以我们通常会把一些小图片/icon放在public文件夹中。
