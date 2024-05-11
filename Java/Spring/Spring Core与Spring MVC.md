教案设计：

### 课程标题：深入Spring Core与Spring MVC

#### 课程目标：
- 理解Spring Core的高级特性，包括Bean的生命周期和事件发布机制。
- 掌握Spring MVC的工作原理和主要组件。
- 实践构建RESTful API，并学会处理HTTP请求与响应。

#### 课程大纲：
1. Spring Core高级特性
   - Bean的生命周期和管理
   - 事件发布和监听机制
   - AOP（面向切面编程）的概念和应用
2. Spring MVC基础
   - MVC架构模式介绍
   - Spring MVC的核心组件：控制器、视图解析器、模型和视图
   - 配置和使用Spring MVC
3. RESTful API设计与实现
   - REST架构风格和原则
   - 使用Spring MVC构建RESTful服务
   - 异常处理和数据验证
4. 实践项目：构建一个简单的RESTful应用
   - 设计API和数据库模型
   - 实现API端点
   - 测试和调试

#### 教学方法：
- 理论讲解与实例演示相结合
- 学生小组讨论和实践
- 代码审查和反馈

#### 教学资源：
- Spring官方文档
- 在线教程和视频
- 开源RESTful API示例代码

#### 课程详细步骤：

1. **Spring Core高级特性** (40分钟)
   - 讲解Bean的生命周期，包括各个阶段和如何自定义Bean的创建、初始化和销毁过程。
   - 演示事件发布和监听的实例，解释Spring中不同类型事件的作用。
   - 介绍AOP的概念，以及如何使用Spring AOP进行日志记录、事务管理等。

2. **Spring MVC基础** (40分钟)
   - 介绍MVC架构模式，讲解其优势和适用场景。
   - 详细解释Spring MVC的主要组件和它们的作用。
   - 演示如何配置和使用Spring MVC，包括创建控制器、定义路由和处理请求。

3. **RESTful API设计与实现** (40分钟)
   - 讲解REST架构风格的核心原则和设计方法。
   - 演示如何使用Spring MVC构建RESTful服务，包括资源的URI设计、HTTP方法的使用、状态码的返回等。
   - 讨论异常处理和数据验证在RESTful API中的重要性，并提供实现方法。

4. **实践项目** (60分钟)
   - 分配小组，讨论并设计一个简单的RESTful应用，包括确定API的功能、设计数据库模型。
   - 指导学生实现API端点，并进行基本的测试。
   - 代码审查和反馈，讨论遇到的问题和解决方案。

#### 作业与评估：
- 学生需要提交一个包含至少三个RESTful端点的项目。
- 学生需要编写单元测试来验证API的行为。
- 学生需要提交一份关于项目设计和实现的报告。

笔记：

### Spring Core与Spring MVC笔记

#### Spring Core高级特性
- **Bean生命周期**：包括实例化、属性填充、初始化、使用和销毁等阶段。
- **事件发布**：Spring允许在Bean的生命周期中发布各种事件，如`ContextRefreshedEvent`、`ContextClosedEvent`等。
- **AOP**：通过切面编程可以实现如日志记录、事务管理等横切关注点的模块化。

#### Spring MVC基础
- **MVC架构**：将应用程序分为模型、视图和控制器，以实现关注点分离。
- **核心组件**：
  - **控制器**：处理用户请求并返回响应。
  - **视图解析器**：将逻辑视图名称解析为实际的视图页面。
  - **模型**：存储应用程序数据。
- **配置**：通过`web.xml`或Java配置类来配置DispatcherServlet和相关的监听器。

#### RESTful API设计与实现
- **REST原则**：每个资源都有一个唯一的标识符（URI），使用标准的HTTP方法（GET, POST, PUT, DELETE等）进行操作。
- **构建RESTful服务**：使用`@RestController`注解创建控制器，定义方法来处理不同的HTTP请求。
- **异常处理**：使用`@ControllerAdvice`和`@ExceptionHandler`注解来全局处理异常。
- **数据验证**：使用Spring的`BindingResult`接口或`javax.validation`注解来验证用户输入。

#### 作业
- 设计并实现一个简单的图书馆管理系统的RESTful API，包括书籍的增删改查功能。
- 编写单元测试来测试API的正确性。
- 编写项目报告，包括API设计、实现细节和测试策略。
  为了帮助学生更好地理解和掌握课程内容，以下是一些关键的示例代码和注解，以及它们在Spring Core和Spring MVC中的应用。
### Spring Core高级特性
#### Bean生命周期
在Spring中，一个Bean的生命周期大致可以分为以下几个阶段：
1. 实例化
2. 属性赋值
3. 初始化（调用`init-method`或`@PostConstruct`注解的方法）
4. 使用
5. 销毁（调用`destroy-method`或`@PreDestroy`注解的方法）
示例代码：
```java
@Component
public class MyBean {
    public MyBean() {
        // 构造函数
    }
    @PostConstruct
    public void init() {
        // 初始化方法
    }
    public void doSomething() {
        // Bean的业务逻辑
    }
    @PreDestroy
    public void destroy() {
        // 销毁方法
    }
}
```
#### 事件发布和监听
Spring提供了应用程序事件发布和监听的机制。你可以发布自定义事件，并监听感兴趣的事件。
示例代码：
```java
@Component
public class MyEventListener implements ApplicationListener<MyEvent> {
    @Override
    public void onApplicationEvent(MyEvent event) {
        // 事件处理逻辑
    }
}
public class MyEvent extends ApplicationEvent {
    public MyEvent(Object source) {
        super(source);
    }
    // 自定义事件的方法
}
```
#### AOP
AOP（面向切面编程）允许你将横切关注点（如日志、事务等）与业务逻辑分离。
示例代码：
```java
@Aspect
@Component
public class LoggingAspect {
    @Pointcut("execution(public * com.example.service.*.*(..))")
    public void servicePointcut() {}
    @Before("servicePointcut()")
    public void logBefore(JoinPoint joinPoint) {
        // 日志记录
    }
    @AfterReturning(pointcut = "servicePointcut()", returning = "retVal")
    public void logAfterReturning(JoinPoint joinPoint, Object retVal) {
        // 处理返回值
    }
}
```
### Spring MVC基础
#### MVC架构模式
MVC（Model-View-Controller）模式将应用程序分为三个主要部分：模型（数据）、视图（用户界面）和控制器（业务逻辑）。
#### 核心组件
- **控制器**：处理用户请求并返回响应。
  ```java
  @RestController
  @RequestMapping("/books")
  public class BookController {
      @GetMapping("/{id}")
      public Book getBook(@PathVariable long id) {
          // 获取书籍的业务逻辑
      }
  }
  ```
- **视图解析器**：将逻辑视图名称解析为实际的视图页面。
  ```java
  @Configuration
  public class WebConfig {
      @Bean
      public ViewResolver viewResolver() {
          InternalResourceViewResolver resolver = new InternalResourceViewResolver();
          resolver.setPrefix("/WEB-INF/views/");
          resolver.setSuffix(".jsp");
          return resolver;
      }
  }
  ```
- **模型**：存储应用程序数据。
  ```java
  public class Book {
      private long id;
      private String title;
      // getters and setters
  }
  ```
- **配置**：通过`web.xml`或Java配置类来配置DispatcherServlet和相关的监听器。
  ```java
  @Configuration
  @EnableWebMvc
  public class WebConfig implements WebMvcConfigurer {
      @Bean
      public DispatcherServlet dispatcherServlet() {
          return new DispatcherServlet();
      }
      @Override
      public void configureDefaultServletHandling(DefaultServletHandlerConfigurer configurer) {
          configurer.enable();
      }
  }
  ```
### RESTful API设计与实现
#### REST原则
REST（Representational State Transfer）架构风格强调资源的无状态操作和统一接口。
#### 构建RESTful服务
使用`@RestController`注解创建控制器，定义方法来处理不同的HTTP请求。
```java
@RestController
@RequestMapping("/api/users")
public class UserController {
    @GetMapping("/{id}")
    public User getUser(@PathVariable long id) {
        // 获取用户信息
    }
    @PostMapping
    public User createUser(@RequestBody User user) {
        // 创建新用户
    }
    @PutMapping("/{id}")
    public User updateUser(@PathVariable long id, @RequestBody User user) {
        // 更新用户信息
    }
    @DeleteMapping("/{id}")
    public void deleteUser(@PathVariable long id) {
        // 删除用户
    }
}
```
#### 异常处理
使用`@ControllerAdvice`和`@ExceptionHandler`注解来全局处理异常。
```java
@ControllerAdvice
public class GlobalExceptionHandler {
    @ExceptionHandler(RuntimeException.class)
    @ResponseBody
    public ResponseEntity<String> handleRuntimeException(RuntimeException ex) {
        return new ResponseEntity<>(ex.getMessage(), HttpStatus.INTERNAL_SERVER_ERROR);
    }
}
```
#### 数据验证
使用Spring的`BindingResult`接口或`javax.validation`注解来验证用户输入。
```java
@PostMapping("/users")
public ResponseEntity<?> addUser(@Valid @RequestBody User user, BindingResult result) {
    if (result.hasErrors()) {
        return ResponseEntity.badRequest().body(result.getFieldErrors().stream().map(DefaultFieldError::getDefaultMessage).collect(Collectors.toList()));
    }
    // 处理有效的用户数据
    return ResponseEntity.ok().build();
}
```
通过这些示例代码和注解，学生可以更深入地理解Spring Core和Spring MVC的工作原理，并在实践中应用这些知识来构建功能强大的Web应用程序。