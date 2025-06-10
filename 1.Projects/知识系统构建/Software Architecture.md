---
date: 2025-05-13 15:15
tags: 
source: https://bytebytego.com/guides/top-5-software-architectural-patterns/
---

[ByteByteGo | Software Architecture](https://bytebytego.com/guides/software-architecture/)
![image.png](https://cdn.jsdelivr.net/gh/duanbiao2000/BlogGallery@main/picutre/20250513151748340.png)

您好！您提供了关于软件架构风格和模式的概述，并提到了一张“速查表（cheat sheet）”来帮助理解这些概念。这张图片正是我之前提到的 ByteByteGo 的 **"Software Architecture Styles"**。

这张速查表非常直观地总结了多种软件架构风格和模式。以下是对这张图的详细解读：

图片的核心是一个中心圆圈，上面写着 **"Software Architecture Styles"**，并以不同的颜色和分类区分了各种架构风格。

### 主要分类和架构风格：

1. Concerns (关注点分离)

- CQRS Architecture (命令查询职责分离架构)：

- 目的： 分离数据存储的读写操作，以提高可伸缩性。它将读取模型和写入模型分离，允许它们独立优化。

- 图示： 展示了命令 (commands) 流向写入数据存储，查询 (queries) 从读取数据存储获取。

```
* **Layered (N-tier) Architecture (分层架构 / N层架构)：**
    * **目的：** 将系统分离为逻辑层。常见的层包括表示层 (Presentation Layer)、业务逻辑层 (Business Logic Layer) 和数据访问层 (Database Layer)。
    * **图示：** 清晰地展示了从上到下的分层结构。
```

2. Component Services (组件服务)

- Microkernel Architecture (微内核架构 / 插件架构)：

- 目的： 分离核心系统功能和客户定制部分。一个小的“微内核”提供核心功能，而“插件”则提供扩展和定制功能。

- 图示： 核心 (Core) 部分被插件 (Plugins) 包围。

```
* **Service-Oriented Architecture (SOA - 面向服务架构)：**
    * **目的：** 通过可重用的服务来构建应用，这些服务通过标准接口进行通信。
    * **图示：** 看起来像多个独立的服务相互连接。

* **Microservices Architecture (微服务架构)：**
    * **目的：** 将应用分解为独立部署、小型、模块化的服务集合。
    * **图示：** 展示了 UI (用户界面) 调用多个独立的小服务，每个服务有自己的数据存储。
```

3. Communication (通信方式)

- Event-Driven Architecture (事件驱动架构)：

- 目的： 响应事件的产生、消费和反应。服务通过发布和订阅事件进行异步通信。

- 图示： 展示了发布者 (Publisher) 发布事件到事件总线 (Event Bus)，消费者 (Consumer) 从事件总线订阅事件。

```
* **Publish-Subscribe (发布-订阅模式)：**
    * **目的：** 实现松耦合和异步通信，发布者将消息发送到主题，订阅者接收感兴趣的消息。这是事件驱动架构的一种常见实现模式。
    * **图示：** 生产者 (Producer) 发布，订阅者 (Subscriber) 接收。
```

4. Domain Driven (领域驱动)

- DDD Architecture (领域驱动设计架构)：

- 目的：**“领域驱动设计强调的是‘从技术而非领域逻辑理解技术’的反面!** 我们不是用技术来限制我们的业务，而是用我们对业务的深刻理解，来指导我们的技术选型和实现。技术只是我们实现业务价值的工具，而不是我们思考的起点！”。它强调将业务逻辑建模为领域模型。

- 图示： 展示了领域模型 (Domain Models) 包含聚合 (Aggregates)、实体 (Entities) 和值对象 (Value Objects) 等。

5. Deployment (部署)

- Space-Based Architecture (基于空间的架构)：

- 目的： 解决分布式系统的数据一致性、性能和可伸缩性问题。通过在共享内存空间中复制数据，实现高性能和高可用性。

- 图示： 展示了多个处理单元 (Processing Units) 拥有自己的工作内存 (Working Memory) 和一个复制的中间件 (Virtualized Middleware)。

```
* **Peer-to-Peer (P2P - 点对点模式)：**
    * **目的：** 每个节点既是服务消费者也是服务提供者。
    * **图示：** 展示了多个节点之间直接相互连接。
```

6. Structure (结构)

- Object-Oriented (面向对象)：

- 目的： 使用对象进行封装、继承和多态。

- 图示： 展示了类 (Class) 和接口 (Interface) 的关系。

```
* **Pipeline / Pipe-Filter (管道-过滤器模式)：**
    * **目的：** 将处理任务分解为一系列独立的、可重用的过滤器组件，数据在它们之间通过管道传递。
    * **图示：** 展示了输入数据经过多个过滤器处理后生成输出。

* **Interpreter (解释器模式)：**
    * **目的：** 定义一个语言的文法，并实现一个解释器来解释该语言中的句子。
    * **图示：** 展示了客户端、上下文、抽象表达式和具体表达式的关系。

* **Primary-Secondary (主-从模式)：**
    * **目的：** 协调组件以确保数据一致性和可用性。一个主节点处理所有写入操作，而从节点则复制数据并处理读取请求。
    * **图示：** 展示了主节点 (Primary) 和多个从节点 (Secondary)。

* **Orchestration Architecture (编排架构)：**
    * **目的：** 管理和协调服务之间的工作流程。一个“编排器”负责指挥服务之间的控制流。
    * **图示：** 展示了一个中心编排器 (Orchestrator) 控制多个服务。

* **Choreography (编舞模式)：**
    * **目的：** 服务通过事件进行独立协作，没有中心协调者。
    * **图示：** 展示了服务之间通过事件（Message）相互触发，没有中心节点。

* **Model-View-Presenter (MVP 架构)：**
    * **目的：** 派生自 Model-View-Controller (MVC)，旨在进一步分离视图、模型和表示器，以提高测试性和解耦度。
    * **图示：** 展示了模型 (Model)、视图 (View) 和表示器 (Presenter) 之间的交互。
```

### 总结：

这张速查表是一个非常有价值的参考指南，它将软件架构的多种风格和模式进行了分类和可视化。对于软件开发人员和架构师来说，它提供了一个快速回顾和理解这些关键概念的途径，帮助他们在面对具体项目时，能够根据需求和约束做出明智的架构选择。每种风格和模式都有其特定的优势和劣势，适用于不同的场景和问题域。
