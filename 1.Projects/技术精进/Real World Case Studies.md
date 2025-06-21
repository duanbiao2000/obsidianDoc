[ByteByteGo | Real World Case Studies](https://bytebytego.com/guides/real-world-case-studies/)
![image.png](https://cdn.jsdelivr.net/gh/duanbiao2000/BlogGallery@main/picutre/20250513110425928.png)

您好！您上传了一张图片，标题是 **"NETFLIX Tech Stack"**。这张图片详细展示了 Netflix 作为全球领先的流媒体平台，其庞大而复杂的技。

以下是图片中提取出的重要概念和关键技术：

### 核心概念：

1. **Tech Stack (技术栈)：**
    
    - **定义：** 指一个软件应用程序或服务所使用的所有技术、编程语言、框架、数据库、工具和平台等的组合。
    - **重要性：** 技术栈的选择对于应用程序的性能、可伸缩性、开发效率、维护成本以及团队能力都有深远影响。Netflix 的技术栈展现了其在构建高可用、大规模分布式系统方面的深厚积累。
2. **Microservices Architecture (微服务架构)：**
    
    - **推断：** 从图中可以看出，Netflix 的后端由大量的“服务 (Services)”组成，并使用了像 Spring Boot, Eureka (服务发现), Zuul (API 网关) 这样的组件，这强烈表明它采用了微服务架构。
    - **特点：** 将大型应用程序拆分为一系列小型、独立的服务，每个服务运行在自己的进程中，并通过轻量级机制（通常是 HTTP API 或消息队列）进行通信。

### 关键技术/组件：

这张图按照不同的功能区域，展示了 Netflix 的技术选择：

1. DevOps (开发运维)

* CI/CD (Continuous Integration/Continuous Delivery)：

* Jira: 项目管理和问题跟踪工具。

* Confluence: 团队协作和文档管理工具。

* Jenkins: 自动化服务器，用于持续集成和交付。

* Spinnaker: 多云持续交付平台，由 Netflix 开源。

* Chaos Engineering (混沌工程)：

* N. Chaos (Netflix Chaos Monkey): 故意在生产环境中注入故障，以测试系统的弹性。

* N. Atlas: Netflix 开源的度量数据收集和可视化平台，用于监控混沌实验和系统运行状态。

* 构建工具：

* Gradle: 强大的构建自动化工具。

* 集群管理/调度：

* Nebula: Netflix 内部使用的集群管理系统。

* 总结： Netflix 在 DevOps 方面投入巨大，通过自动化、持续交付和混沌工程来确保其大规模分布式系统的可靠性和弹性。

2. Mobile (移动端)

* Kotlin: 运行在 Java 虚拟机 (JVM) 上的静态类型编程语言，主要用于 Android 应用开发。

* Swift: 苹果公司开发的编程语言，主要用于 iOS、macOS、watchOS 和 tvOS 应用开发。

* 总结： 针对 Android 和 iOS 这两大主流移动平台，分别采用了其推荐的现代编程语言。

3. Frontend (前端)

* React: Facebook 开源的 JavaScript 库，用于构建用户界面，尤其适用于单页应用。

* JS (JavaScript): Web 前端的核心编程语言。

* 总结： 采用流行的前端框架 React，配合 JavaScript，构建用户界面。

4. Backend (后端)

* GraphQL: 一种用于 API 的查询语言和运行时环境，允许客户端精确请求所需的数据。

* Services (服务): 表示其微服务架构中的各个独立服务。

* Spring Boot: 用于快速构建生产级别 Spring 应用的框架。

* Netflix OSS (Open Source Software - 开源软件):

* Netflix Zuul: 一个 API 网关服务，提供动态路由、监控、弹性负载平衡和安全性等功能。

* Netflix Eureka: 服务发现工具，用于微服务架构中服务的注册与发现。

* 总结： 后端基于 Java 和 Spring Boot，并广泛使用 Netflix 开源的微服务组件，通过 GraphQL 提供灵活的 API 接口。

5. Database (数据库)

* MySQL: 广泛使用的开源关系型数据库管理系统。

* Cassandra: Apache Cassandra，一个高可伸缩、高可用、去中心化的 NoSQL 数据库，特别适合处理海量数据和高写入吞吐量。

* EVcache: Netflix 内部开发的高度分布式的内存缓存系统。

* CockroachDB: 一个分布式 SQL 数据库，提供强一致性、高可用和可伸缩性。

* 总结： 混合使用了关系型数据库 (MySQL) 和多种 NoSQL 数据库 (Cassandra, CockroachDB, EVcache)，以适应不同类型数据和一致性需求。

6. Messaging/Streaming (消息/流处理)

* Kafka (Apache Kafka): 分布式流处理平台，用于构建实时数据管道和流应用程序。

* Apache Flink: 一个开源的流处理框架，用于有状态计算和实时分析。

* 总结： 大量依赖分布式消息队列和流处理框架，处理海量数据流，实现实时分析和系统解耦。

7. Streaming (流媒体)

* AWS S3 (Amazon S3): Amazon Web Services (AWS) 的对象存储服务，用于存储海量数据（如视频内容）。

* AWS Connect/CloudFront: AWS Connect 可能指客服解决方案，而 CloudFront 是 AWS 的内容分发网络 (CDN)，用于加速内容分发，确保视频流的流畅播放。

* AWS Elastic Transcoder: AWS 提供的媒体转码服务，用于将视频文件转换为不同格式和分辨率以适应各种设备。

* 总结： 大量利用 AWS 云服务进行视频内容的存储、分发和转码，确保全球用户高质量的流媒体体验。

8. BIG DATA (大数据)

* Data Storage (数据存储):

* AWS S3: 再次提及，作为大数据存储的首选。

* Redshift: AWS 的云数据仓库服务，用于大规模分析。

* Apache Iceberg: 一个用于大型分析数据集的开放表格式，支持事务语义和 schema 演进。

* Apache Druid: 一个高性能的分布式数据存储和查询系统，用于实时分析。

* Data Processing (数据处理):

* Tableau: 数据可视化和商业智能工具。

* Apache Flink: 再次提及，用于大数据流处理。

* Apache Spark: 快速通用的大数据处理引擎，支持批处理、流处理、SQL、机器学习等。

* 总结： 拥有复杂的大数据处理和存储系统，结合了云数据仓库、实时分析数据库和强大的数据处理框架，以支持其推荐系统、内容生产和业务分析。

### 总体印象：

Netflix 的技术栈是一个**典型的云原生、微服务、大数据驱动**的复杂系统。它大量依赖开源技术，并积极贡献开源社区（如 Spinnaker, Eureka, Zuul），同时充分利用了 AWS 云服务来构建其全球范围内的流媒体基础设施。其技术栈的选择充分体现了对**可伸缩性、弹性、高性能和数据驱动决策**的极致追求。

---
您上传了一张关于 Reddit 核心架构的图片，并提供了相关的文字描述。
![image.png](https://cdn.jsdelivr.net/gh/duanbiao2000/BlogGallery@main/picutre/20250513111950891.png)

以下是图片和文字中提取出的重要概念和关键技术：

### 核心概念：

1. **Scalability (可伸缩性)：** Reddit 架构设计的核心目标之一，能够服务每月超过 10 亿的用户。
2. **Evolutionary Architecture (演进式架构)：** Reddit 的架构并非一成不变，而是持续演进的，从最初的单体应用发展到微服务，并不断优化各层技术。
3. **Microservices (微服务)：** Reddit 从 Python 单体应用开始，逐渐转向使用 Go 构建的微服务架构，实现功能解耦和独立部署。
4. **Hybrid Approach (混合方法)：** Reddit 在许多技术选择上都采用了混合策略，例如数据库的选择（Postgres 和 Cassandra），以及 GraphQL 的使用方式。

### 关键技术/组件：

**1. 用户前端访问层：**

- **User Channels (用户渠道)：** 表示用户通过各种设备和平台（如 Web 浏览器、移动应用）访问 Reddit。
- **Content Delivery Network (CDN) - Fastly CDN：** 作为应用的前端，用于加速内容分发，提高用户访问速度和体验。
- **Web UI Evolution (Web UI 演进)：**
    - **jQuery (早期)：** 早期前端开发中使用的 JavaScript 库。
    - **TypeScript (当前)：** 强类型 JavaScript 超集，用于构建大型前端应用。
    - **Modern Node.js frameworks (当前)：** 使用现代的 Node.js 框架进行前端开发。
- **App Platforms (应用平台)：** 包括 Android 和 iOS 移动应用。

**2. 基础设施与部署：**

- **Hosting Platforms (托管平台)：**
    - **AWS (Amazon Web Services)：** 采用 AWS 作为其应用程序和内部服务的托管平台。
    - **Kubernetes (K8s)：** 容器编排平台，用于管理和部署容器化应用。
- **Load Balancer (负载均衡器) - Envoy：** 位于应用栈的前端，将传入请求路由到适当的服务，确保服务的高可用性和负载均衡。Envoy 是一种流行的开源边缘和服务代理。
- **Deployment & Infra (部署与基础设施)：**
    - **Spinnaker：** 开源的多云持续交付平台。
    - **Drone CI：** 容器原生持续集成平台。
    - **Terraform：** 基础设施即代码 (IaC) 工具，用于自动化基础设施的部署和管理。

**3. API 层与服务间通信：**

- **GraphQL Federation (GraphQL 联邦)：**
    - Reddit 大量使用 GraphQL 作为其 API 层。
    - 已转向 GraphQL Federation，这是一种组合多个小型 GraphQL API (称为 **Domain Graph Services, DGS**) 的方式，以创建统一的 GraphQL API。
    - 在 2022 年，Reddit 的 GraphQL 团队进一步拆分了 GraphQL Monolith (单体)，增加了新的 Go subgraphs (子图) 用于核心 Reddit 实体。
- **Go (编程语言)：** Reddit 从 Python 单体应用转向使用 Go 构建微服务。
- **Messaging Platforms (消息平台)：**
    - **RabbitMQ (async job queue)：** 用于异步作业队列，将昂贵的操作（如用户投票、提交链接）推迟处理，提高响应速度。
    - **Kafka (real-time data transfer)：** 用于实时数据传输，支持内容安全检查和审核规则。
- **Job Workers (作业工作者)：** 处理来自异步作业队列的任务。

**4. 数据存储与一致性：**

- **PostgreSQL (Postgres)：** 作为核心数据模型的主数据库。
- **memcached：** 位于 Postgres 前端的内存缓存系统，用于减轻数据库负载。
- **Cassandra：** 大量用于新功能，因其弹性（Resiliency）和可用性（Availability）特性。
- **Change Data Capture (CDC) with Debezium：** 用于数据复制和维护缓存一致性，通过 Debezium 捕获数据库的变更事件。

### 架构亮点与演进：

- **前端现代化：** 从 jQuery 到 TypeScript 和现代 Node.js 框架。
- **后端微服务化：** 从 Python 单体到 Go 微服务。
- **API 灵活性：** 大力投入 GraphQL，并采用 GraphQL Federation 应对复杂性和扩展性。
- **异构数据存储：** 结合关系型数据库 (Postgres) 和 NoSQL 数据库 (Cassandra)，并通过 Memcached 和 CDC 优化性能和一致性。
- **异步处理和流处理：** 利用 RabbitMQ 和 Kafka 处理高并发和实时数据流。
- **DevOps 自动化：** 使用 Spinnaker, Drone CI, Terraform 等工具实现高效的部署和基础设施管理。
- **云原生：** 充分利用 AWS 和 Kubernetes 作为底层基础设施。

这张图和文字共同描绘了一个大型、复杂、高度优化的分布式系统，展示了 Reddit 如何通过不断的技术演进和采纳前沿技术来应对其庞大的用户基础和高并发挑战。