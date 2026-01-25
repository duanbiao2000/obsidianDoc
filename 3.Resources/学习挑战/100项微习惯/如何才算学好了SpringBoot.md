---
date: 2025-05-19 13:58
rating: 2.5
tags:
- spring-boot-skills
- microservices-architecture
- Domain/Creativity
- Domain/Mindset
update: 2025-05-22 18:15
---

## 🔗 相关链接

**上级索引**:
- [[3.Resources\学习挑战\100项微习惯\_Index_of_100项微习惯.md|100项微习惯]]
- [[3.Resources\学习挑战\_Index_of_学习挑战.md|学习挑战]]
- [[3.Resources\_Index_of_3.Resources.md|3.Resources]]

**相关主题**:
- [[2.Topics\02.认知系统\学习系统]]

---

### 一、 阶段一：能用 (入门)
- **核心能力**: 快速搭建并运行一个基本的Spring Boot应用。
- **掌握技能**:
  - 使用 `@SpringBootApplication` 启动应用。
  - 编写 `Controller`, `Service`, `Repository` 实现分层架构。
  - 通过 `@Value` 和 `application.yml` 读取配置。
  - 引入 `Starters` (如 `spring-boot-starter-web`) 快速集成功能。
- **评估标准**: 能独立完成一个CRUD Web应用，并打包成可执行Jar运行。

### 二、 阶段二：会调 (掌握)
- **核心能力**: 根据需求定制和优化Spring Boot的默认行为。
- **掌握技能**:
  - 修改内嵌服务器、连接池等默认配置。
  - 理解配置加载**优先级** (命令行 > 环境变量 > `application-{profile}.yml` > `application.yml`)。
  - 理解**条件注解** (`@ConditionalOn...`)，知道自动配置为何生效或失效。
  - 使用 `Actuator` (`/health`, `/metrics`, `/beans`) 监控应用运行时状态。
- **评估标准**: 能分析并解决常见的Bean冲突或自动配置不生效问题；能使用Actuator排查配置和Bean加载问题。

### 三、 阶段三：能拆 (精通)
- **核心能力**: 理解框架内部工作原理，并能开发自定义的可复用组件。
- **掌握技能**:
  - 熟悉 `SpringApplication.run()` 的**启动流程**，理解 `ApplicationContext` 的刷新过程。
  - **能从零开发自定义Starter**: 包含自动配置类 (`@Configuration`)、属性绑定 (`@ConfigurationProperties`) 和条件装配 (`@ConditionalOn...`)。
  - 深入理解 `@EnableAutoConfiguration` 如何通过 `spring.factories` 加载配置类。
  - 了解 `Binder` 如何将配置源绑定到 `@ConfigurationProperties` 对象。
- **评估标准**: 能阅读并解释常用Starter的核心源码；能独立开发一个简单的自定义Starter。

### 四、 阶段四：能控 (架构级)
- **核心能力**: 在大规模分布式系统（微服务、云原生）中有效管理和部署Spring Boot应用。
- **掌握技能**:
  - 结合 `Spring Cloud` 生态，理解并应用服务注册与发现、负载均衡、配置中心、API网关、分布式追踪等。
  - 为 `DevOps/CI/CD` 流程设计Spring Boot的构建和部署策略 (如Docker打包)。
  - 掌握 `Spring Boot` 与 `GraalVM` 结合构建原生镜像以优化启动速度和内存占用。
- **评估标准**: 能设计一个简单的微服务系统原型；能使用Docker打包并描述如何在Kubernetes中部署。

### 五、 阶段五：能变 (创新)
- **核心能力**: 突破框架限制，进行改造、扩展，甚至引领技术发展。
- **掌握技能**:
  - 对整个 `Spring` 生态（Core, AOP, Security, Cloud等）有深刻理解。
  - 能对框架源码进行贡献或提出改进方案。
  - 能主导大型系统的技术栈升级（如从Spring Boot 2到3）。
  - 能针对特定场景（如 `Serverless`）对Spring Boot进行深度裁剪和优化。
- **评估标准**: 能对应用进行深度性能剖析和优化；能在没有Spring Boot的情况下，使用Spring Framework Core构建一个类似的简化框架。