

**问题1：Spring Boot的核心特性不包括以下哪项？**
??
A. 自动配置
B. 嵌入式服务器
C. 手动依赖管理
D. 快速开发

**问题2：在Spring MVC中，以下哪种方式不常用于Controller和Service层之间传递数据？**
??
A. 命令对象（Command Object）/DTO（Data Transfer Object）
B. POJO（Plain Old Java Object）
C. 直接操作视图文件
D. 使用`@PathVariable`和`@RequestParam`

**问题3：以下哪个组件负责与数据库或其他持久化存储进行交互？**
??
A. Controller
B. Service
C. Repository
D. Model

**问题4：在Spring框架中，以下哪个术语用于描述由Spring容器管理的应用程序组件？**
??
A. Utils
B. Beans
C. Validator
D. Adapters

**问题5：在配置实体管理器工厂时，`packagesToScan`属性的作用是什么？**
??
A. 指定数据源
B. 指定JPA供应商适配器
C. 指定Spring需要扫描的包路径，以便自动检测并注册所有在这些包中的实体类
D. 指定数据库方言

**答案：**
1. C
2. C
3. C
4. B
5. C


## FQA2

**问题1：根据笔记中提到的Spring学习框架，哪个模块主要关注使用Spring Cloud实现服务发现和配置管理？**
?
A. [[Spring Core与Spring MVC]]
B. [[数据访问与持久化]]
C. [[微服务架构]]
D. [[安全性与身份验证]]

---
**问题2：在Spring MVC中，Controller层向Service层传递封装了多个相关数据字段的对象，通常使用以下哪种方式最合适？**
?
A. `@PathVariable`
B. DTO（数据传输对象）
C. `Model`对象
D. `@RequestParam`

---
**问题3：根据笔记描述的典型Spring组件结构，哪个组件主要负责与数据库进行交互，执行数据的持久化和检索？**
?
A. Controller
B. Service
C. Repository
D. Validator

---
**问题4：笔记中提到的`EntityManagerFactory` XML配置示例中，`packagesToScan`属性的作用是什么？**
?
A. 指定数据源的连接信息
B. 指定JPA供应商（如Hibernate）
C. 指定需要扫描以查找实体类的包路径
D. 指定Hibernate使用的数据库方言

---
**问题5：Spring Boot的starter依赖（如 `spring-boot-starter-web`）主要目的是什么？**
?
A. 提供项目的基础目录结构
B. 简化特定功能所需依赖的管理和配置
C. 自动生成所有业务逻辑代码
D. 仅用于项目的测试阶段

---
**问题6：根据笔记内容，Spring Boot中的配置类（Configuration Class）和工具类（Utility Class）的主要区别之一是什么？**
?
A. 配置类使用`@Service`注解，工具类使用`@Component`注解
B. 配置类用于定义Bean和应用配置，工具类提供通用的静态方法
C. 工具类必须由Spring容器管理，配置类不需要
D. 配置类负责处理HTTP请求，工具类负责数据持久化

---
**问题7：笔记中提到，在Spring MVC应用程序中，处理跨层共通关注点（如日志记录、安全性）通常使用哪种技术？**
?
A. 依赖注入 (DI)
B. 控制反转 (IoC)
C. 面向切面编程 (AOP)
D. 模型-视图-控制器 (MVC)

---
**问题8：根据笔记中对Spring Data JPA的描述，当需要执行非常复杂或需要特定数据库函数的查询时，开发者应该使用哪种方式？**
?
A. 仅依赖方法命名约定自动生成查询
B. 在Service层手动编写SQL语句
C. 使用`@Query`注解编写自定义的JPQL或原生SQL查询
D. 使用`@Repository`注解自动完成复杂查询

---
**问题9：在典型的Spring MVC应用中，组件之间的依赖关系通常是怎样的？**
?
A. Service -> Controller -> Repository
B. Controller -> Service -> Repository
C. Repository -> Service -> Controller
D. Controller -> Repository -> Service

---
**问题10：根据笔记内容，以下哪个是Spring Cloud提供的用于服务发现的组件示例？**
?
A. Spring Cloud Config
B. Spring Cloud Gateway
C. Eureka
D. Hystrix

---

**答案：**
1.  C
2.  B
3.  C
4.  C
5.  B
6.  B
7.  C
8.  C
9.  B
10. C

#### Sources:
- [Spring Boot](obsidian://open?vault=obsidianDoc&file=Spring%20Boot)
- [spring boot中的类](obsidian://open?vault=obsidianDoc&file=spring%20boot%E4%B8%AD%E7%9A%84%E7%B1%BB)
- [Spring Boot入门](obsidian://open?vault=obsidianDoc&file=Spring%20Boot%E5%85%A5%E9%97%A8)
- [Spring Core与Spring MVC](obsidian://open?vault=obsidianDoc&file=Spring%20Core%E4%B8%8ESpring%20MVC)
- [Spring注解](obsidian://open?vault=obsidianDoc&file=Spring%E6%B3%A8%E8%A7%A3)
- [Spring 进阶](obsidian://open?vault=obsidianDoc&file=Spring%20%E8%BF%9B%E9%98%B6)
- [企业资源规划系统ERP](obsidian://open?vault=obsidianDoc&file=%E4%BC%81%E4%B8%9A%E8%B5%84%E6%BA%90%E8%A7%84%E5%88%92%E7%B3%BB%E7%BB%9FERP)