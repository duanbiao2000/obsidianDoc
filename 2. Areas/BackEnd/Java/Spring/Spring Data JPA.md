## FQA


**问题1：Spring Data JPA 的主要目的是什么？**
?
A. 简化基于 Java Persistence API (JPA) 的数据库操作
B. 取代 Hibernate 作为唯一的 [[ORM]] 框架
C. 提供一个全新的数据库查询语言
D. 管理 [[2. Areas/BackEnd/Java/Spring Boot|Spring Boot]] 应用的依赖关系

---
**问题2：在 Spring Data JPA 中，开发者通过继承哪个接口可以轻松获得常用的 CRUD 操作方法？**
?
A. `DataSource`
B. `EntityManager`
C. `JpaRepository` 或 `CrudRepository`
D. `JdbcTemplate`

---
- ? **问题3：Spring Data JPA 支持基于什么来自动生成查询？**
?
A. XML 配置文件
B. 方法命名约定
C. 实体类的注释数量
D. 数据库的存储过程

---
**问题4：当 Spring Data JPA 的方法命名约定无法满足复杂的查询需求时，应该使用哪个注解来编写自定义查询？**
?
A. `@Entity`
B. `@Autowired`
C. `@Transactional`
D. `@Query`

---
**问题5：在 Spring Data JPA 中，`@Transactional` 注解的主要作用是什么？**
?
A. 定义实体类与数据库表的映射关系
B. 自动生成 CRUD 操作
C. 确保数据库操作的原子性（事务管理）
D. 配置数据库连接池

---
**问题6：哪个 Spring Boot 起步依赖可以快速集成 Spring Data JPA？**
?
A. `spring-boot-starter-web`
B. `spring-boot-starter-test`
C. `spring-boot-starter-data-jpa`
D. `spring-boot-starter-security`

---
**问题7：根据笔记内容，以下哪个是 Spring Data JPA 的底层实现之一，并且是一个成熟的 ORM 框架？**
?
A. MyBatis
B. Spring JDBC Template
C. Hibernate
D. Spring Data MongoDB

---
**问题8：如果开发者需要更精确地控制 SQL 语句的执行和性能优化，并且不介意手动编写 SQL，以下哪个技术是 Spring Data JPA 的一个替代选项？**
?
A. Spring Data Redis
B. Hibernate
C. Spring AOP
D. MyBatis

---
**问题9：根据 Spring Boot 笔记中提到的典型分层结构，哪个层负责与数据库进行交互？**
?
A. Controller 层
B. Service 层
C. Repository 层
D. Model 层

---
**问题10：在使用 `@Query` 注解编写自定义 JPQL 查询时，如何将方法参数绑定到查询语句中的命名参数？**
?
A. 使用 `?` 占位符，按顺序绑定
B. 使用 `@Autowired` 注解
C. 使用 `@Param` 注解配合 `:参数名`
D. 直接在查询语句中拼接字符串

---

**答案：**
1.  A
2.  C
3.  B
4.  D
5.  C
6.  C
7.  C
8.  D
9.  C
10. C

#### Sources:
- [Spring Data JPA](obsidian://open?vault=obsidianDoc&file=Spring%20Data%20JPA)
- [Spring注解](obsidian://open?vault=obsidianDoc&file=Spring%E6%B3%A8%E8%A7%A3)
- [Spring Boot](obsidian://open?vault=obsidianDoc&file=Spring%20Boot)