### Sonner
- **用途**：Sonner 是一个现代的通知库，用于在Web应用程序中显示通知消息。
- **主要功能**：
  - 提供了多种类型的提示信息，如成功、警告、错误等。
  - 可以自定义样式和行为。
  - 支持自动关闭或手动关闭通知。
  - 易于集成到任何React项目中。

- **使用示例**：
  ```javascript
  import { notify } from 'sonner';

  function SomeComponent() {
    const showNotification = () => {
      notify.success('操作成功！');
    };

    return <button onClick={showNotification}>点击我</button>;
  }
  ```
