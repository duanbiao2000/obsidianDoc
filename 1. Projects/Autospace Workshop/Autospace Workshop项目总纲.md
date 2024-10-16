---
aliases: 
theme: 
high_priority: false
tags:
---
Autospace Workshop 项目是一个使用 [[Nx]] 构建的 monorepo 项目，包含多个应用程序和库，用于构建一个停车场管理系统。

```
 C:\Users\Danny\Documents\Mycodes\Nextjs\autospace-workshop
```


![image.png](https://cdn.jsdelivr.net/gh/duanbiao2000/BlogGallery@main/picture/20240916150351.png)


**项目结构:**

- **apps:**

    - api: 后端 API 应用，使用 NestJS 框架构建，提供 GraphQL 接口。

    - web:  面向用户的 Web 应用，使用 Next.js 框架构建。

    - web-admin: 管理员 Web 应用，使用 Next.js 框架构建。

    - web-manager: 停车场管理员 Web 应用，使用 Next.js 框架构建。

    - web-valet: 代客泊车 Web 应用，使用 Next.js 框架构建。

- **[[libs目录结构]]:**

    - 3d:  3D 模型库，使用 Three.js 和 React Three Fiber 构建。

    - forms: 表单库，包含各种表单组件和逻辑。

    - network: 网络请求库，使用 [[Apollo Client]] 与后端 API 交互。

    - sample-lib: 示例库。

    - ui: UI 组件库，包含各种 UI 组件。

    - util: 工具库，包含各种工具函数和常量。

  

**技术栈:**

  

- **前端:** Next.js, React, Tailwind CSS, Apollo Client, [[Mapbox GL JS]]

- **后端:** [[NestJS]], [[2. Areas/前端开发/NextJS/GraphQL]], Prisma, PostgreSQL [[GraphQL关系梳理]]

- **构建工具:** [[Nx]], Yarn, Docker

  

**主要功能:**

  

- 用户可以通过 Web 应用查找和预订停车位。

- 管理员可以通过 Web 应用管理停车场、停车位和用户。

- 停车场管理员可以通过 Web 应用管理其停车场的停车位和预订。

- 代客泊车员可以通过 Web 应用管理代客泊车服务。

  

**项目特点:**

  

- 使用 monorepo 架构，方便代码共享和管理。

- 使用 TypeScript 编写，提高代码质量和可维护性。

- 使用 GraphQL 构建 API，提供灵活和高效的数据查询。

- [[使用 Docker 容器化数据库]]，方便部署和管理。

  

**开发流程:**

  

1. 克隆代码仓库。

2. 安装依赖项。

3. 配置环境变量。

4. 使用 Docker Compose 启动数据库。

5. 运行 Prisma 迁移。

6. 启动应用程序。

  
  

**总结:**

  

Autospace Workshop 项目是一个功能完善的停车场管理系统，采用现代化的技术栈和架构，具有良好的可扩展性和可维护性。


根据您提供的信息，我会为您创建一个NestJS项目的架构图。这个图将展示主要的模块、服务和它们之间的关系，以及与其他关键组件的交互。



```
graph TD
    A[Client Applications] -->|GraphQL Requests| B(GraphQL API Gateway)
    B -->|Resolvers| C{NestJS Application}
    
    C -->|User Module| D[User Service]
    C -->|Auth Module| E[Auth Service]
    C -->|Parking Module| F[Parking Service]
    C -->|Booking Module| G[Booking Service]
    C -->|Payment Module| H[Payment Service]
    C -->|Admin Module| I[Admin Service]
    C -->|Manager Module| J[Manager Service]
    C -->|Valet Module| K[Valet Service]
    
    D --> L((Database))
    E --> L
    F --> L
    G --> L
    H --> L
    I --> L
    J --> L
    K --> L
    
    M[Prisma ORM] --> L
    
    N[Guards] --> C
    O[Pipes] --> C
    P[Interceptors] --> C
    Q[Exception Filters] --> C
    
    R[Configuration Module] --> C
    S[Logging Module] --> C
    T[Caching Module] --> C
    
    U[External Services] --> C
    
    V[Mapbox Integration] --> F
    W[Payment Gateway] --> H
    
    X[Docker Container] --> L
```

这个架构图展示了基于您提供的信息的NestJS项目结构。以下是对图中各个部分的解释：

1. 客户端应用（Client Applications）：这包括您提到的所有web应用（web, web-admin, web-manager, web-valet）。

2. GraphQL API网关：作为客户端应用和NestJS应用之间的接口。

3. NestJS应用：[[核心后端应用]]，包含多个模块：
   - 用户模块（User Module）
   - 认证模块（Auth Module）
   - 停车模块（Parking Module）
   - 预订模块（Booking Module）
   - 支付模块（Payment Module）
   - 管理员模块（Admin Module）
   - 停车场管理员模块（Manager Module）
   - 代客泊车模块（Valet Module）

4. 数据库：使用PostgreSQL，通过Prisma ORM进行交互。

5. [[NestJS核心功能]]：
   - 守卫（Guards）
   - 管道（Pipes）
   - 拦截器（Interceptors）
   - 异常过滤器（Exception Filters）

6. 辅助模块：
   - 配置模块（Configuration Module）
   - 日志模块（Logging Module）
   - 缓存模块（Caching Module）

7. 外部服务集成：
   - Mapbox集成：用于停车模块的地图功能
   - 支付网关：用于支付模块

8. Docker容器：用于数据库的容器化

这个架构图提供了一个高层次的视图，展示了主要组件及其关系。根据实际需求，您可能需要添加更多细节或调整结构。如果您需要对任何部分进行修改或者想要更详细的解释，请告诉我。