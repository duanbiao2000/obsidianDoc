---
title: 20241121
createdAt: 2024-11-21 11:45
categories:
  - Mindset
tags:
  - Mindset/Reflection
---

总结

<!--more-->
# Webhook 事件类型
Webhook 事件类型通常用于描述和分类不同的事件，以便接收方能够根据事件类型采取相应的处理措施。以下是一些常见的 webhook 事件类型及其应用场景：

### 1. 用户相关事件
- **user.created**：用户创建
- **user.updated**：用户信息更新
- **user.deleted**：用户删除
- **user.activated**：用户激活
- **user.deactivated**：用户停用

### 2. 订单相关事件
- **order.created**：订单创建
- **order.updated**：订单更新
- **order.completed**：订单完成
- **order.canceled**：订单取消
- **order.refunded**：订单退款

### 3. 付款相关事件
- **payment.created**：支付创建
- **payment.succeeded**：支付成功
- **payment.failed**：支付失败
- **payment.refunded**：支付退款
- **payment.disputed**：支付争议

### 4. 订阅相关事件
- **subscription.created**：订阅创建
- **subscription.updated**：订阅更新
- **subscription.canceled**：订阅取消
- **subscription.renewed**：订阅续订
- **subscription.paused**：订阅暂停

### 5. 产品相关事件
- **product.created**：产品创建
- **product.updated**：产品更新
- **product.deleted**：产品删除
- **product.stock.updated**：库存更新

### 6. 文档相关事件
- **document.created**：文档创建
- **document.updated**：文档更新
- **document.deleted**：文档删除
- **document.published**：文档发布

### 7. 评论相关事件
- **comment.created**：评论创建
- **comment.updated**：评论更新
- **comment.deleted**：评论删除

### 8. 通知相关事件
- **notification.sent**：通知发送
- **notification.read**：通知阅读
- **notification.dismissed**：通知忽略

### 9. 系统相关事件
- **system.maintenance.started**：系统维护开始
- **system.maintenance.ended**：系统维护结束
- **system.error**：系统错误

### 10. 审核相关事件
- **audit.log.created**：审核日志创建
- **audit.log.updated**：审核日志更新
- **audit.log.deleted**：审核日志删除

### 示例：创建和发送订单相关的 webhook

假设你有一个电子商务平台，需要发送订单相关的 webhook 事件。以下是一个示例代码：

#### 创建事件类型

```javascript
const { Svix } = require('@svix/server-sdk');

const svix = new Svix('your-svix-api-key');
const applicationId = 'your-application-id';

async function createOrderEventTypes() {
  try {
    const created = await svix.eventType.create(applicationId, {
      name: 'order.created',
      description: 'An order has been created'
    });

    const updated = await svix.eventType.create(applicationId, {
      name: 'order.updated',
      description: 'An order has been updated'
    });

    const completed = await svix.eventType.create(applicationId, {
      name: 'order.completed',
      description: 'An order has been completed'
    });

    const canceled = await svix.eventType.create(applicationId, {
      name: 'order.canceled',
      description: 'An order has been canceled'
    });

    const refunded = await svix.eventType.create(applicationId, {
      name: 'order.refunded',
      description: 'An order has been refunded'
    });

    console.log('Order event types created:', created, updated, completed, canceled, refunded);
  } catch (error) {
    console.error('Error creating order event types:', error);
  }
}

createOrderEventTypes();
```

#### 发送订单创建的 webhook

```javascript
const payload = {
  orderId: '12345',
  customerName: 'John Doe',
  items: [
    { productId: 'A123', quantity: 2 },
    { productId: 'B456', quantity: 1 }
  ],
  totalAmount: 150.00,
  timestamp: new Date().toISOString()
};

async function sendOrderCreatedWebhook() {
  try {
    const response = await svix.message.create(applicationId, {
      eventType: 'order.created',
      payload: payload
    });
    console.log('Webhook sent successfully:', response);
  } catch (error) {
    console.error('Error sending webhook:', error);
  }
}

sendOrderCreatedWebhook();
```

### 总结

- **用户相关事件**：处理用户生命周期中的各种事件。
- **订单相关事件**：处理订单状态的变化。
- **付款相关事件**：处理支付过程中的各种状态。
- **订阅相关事件**：处理订阅的创建、更新和取消。
- **产品相关事件**：处理产品的创建、更新和删除。
- **文档相关事件**：处理文档的创建、更新和删除。
- **评论相关事件**：处理评论的创建、更新和删除。
- **通知相关事件**：处理通知的发送、阅读和忽略。
- **系统相关事件**：处理系统的维护和错误。
- **审核相关事件**：处理审核日志的创建、更新和删除。

希望这些信息对你有帮助！如果有其他问题，请随时提问。