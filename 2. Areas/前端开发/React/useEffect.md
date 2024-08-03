
```javascript
import React, { useLayoutEffect, useState } from 'react';

function MyComponent() {
  // 声明一个状态变量 'width' 和一个函数 'setWidth' 用于更新它
  const [width, setWidth] = useState(0);

  // useLayoutEffect 钩子在 DOM 变更完成后、浏览器绘制屏幕之前同步执行
  useLayoutEffect(() => {
    // 定义一个函数 'updateWidth' 用于更新 'width' 状态变量
    function updateWidth() {
      // 获取 'myElement' DOM 元素的当前宽度
      const newWidth = document.getElementById('myElement').clientWidth;
      // 使用新宽度更新 'width' 状态变量
      setWidth(newWidth);
    }

    // 添加一个 'resize' 事件监听器，并在事件发生时调用 'updateWidth'
    window.addEventListener('resize', updateWidth);
    // 立即调用 'updateWidth' 来设置初始宽度
    updateWidth();

    // 返回一个清理函数，在组件卸载时移除事件监听器
    return () => {
      window.removeEventListener('resize', updateWidth);
    };
  }, []);

  // 渲染组件
  return (
    <div>
      <div id="myElement">Hello, world!</div>
      <p>Width: {width}px</p>
    </div>
  );
}
```

