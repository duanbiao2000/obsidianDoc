## spring boot中的类
 在Java和Spring框架中，配置类（Configuration Class）和工具类（Utility Class）是两种常见的类类型，它们各自有不同的用途和设计目的。

### 配置类（Configuration Class）

配置类通常用于Spring框架中，特别是在使用注解驱动的配置时。这些类使用`@Configuration`注解来标记，表明它们包含了定义Spring应用上下文的bean定义。配置类允许开发者以编程方式定义bean，而不是使用XML文件。配置类可以包含多个带有`@Bean`注解的方法，每个方法都会返回一个bean实例，这些bean会被Spring容器管理。

例如，一个简单的配置类可能看起来像这样：

```java
@Configuration
public class MyConfig {

    @Bean
    public MyService myService() {
        return new MyServiceImpl();
    }
}
```

在这个例子中，`MyConfig`是一个配置类，它定义了一个名为`myService`的bean，当Spring应用启动时，Spring容器会调用`myService`方法并创建`MyServiceImpl`的一个实例。

### 工具类（Utility Class）

工具类是提供一组静态方法的类，这些方法通常用于执行通用任务，如数据验证、字符串处理、数学运算等。工具类的方法通常是无状态的，这意味着它们不依赖于类的实例状态，而是依赖于传递给方法的参数。工具类通常不使用`new`关键字来实例化，而是直接通过类名调用静态方法。

例如，一个简单的工具类可能包含一些字符串处理方法：

```java
public class StringUtils {

    public static String reverseString(String str) {
        return new StringBuilder(str).reverse().toString();
    }
}
```

在这个例子中，`StringUtils`是一个工具类，提供了一个静态方法`reverseString`，用于反转字符串。你可以这样使用它：

```java
String reversed = StringUtils.reverseString("Hello World");
```

### 区别

- **目的**：配置类用于定义Spring应用的bean和配置，而工具类用于提供通用的、可重用的代码片段。
- **实例化**：配置类通常不需要实例化，它们的作用是通过Spring容器来管理bean；工具类则通过类名直接调用静态方法，不需要实例化。
- **注解**：配置类通常使用`@Configuration`注解，而工具类通常不使用特定的注解，除非它们需要特定的行为，如`@UtilityClass`（在Spring Boot中用于自动配置工具类）。

在实际应用中，合理地使用配置类和工具类可以帮助你构建清晰、可维护的代码结构。配置类使得Spring的配置更加灵活和易于管理，而工具类则提高了代码的复用性和可读性。

 在Java和Spring框架中，除了配置类（Configuration Class）和工具类（Utility Class）之外，还有许多其他类型的类，它们在不同的场景下扮演着重要的角色。以下是一些常见的类类型：

1. **实体类（Entity Class）**：
   - 用于表示数据模型，通常与数据库中的表相对应。实体类通常包含属性、getter和setter方法，以及可能的构造器和业务逻辑。

2. **服务类（Service Class）**：
   - 提供业务逻辑的实现，通常与实体类一起工作，处理数据的增删改查（CRUD）操作以及更复杂的业务流程。

3. **控制器类（Controller Class）**：
   - 在Spring MVC框架中，控制器类处理HTTP请求并返回响应。它们通常使用`@Controller`注解，并包含处理特定URL路径的方法。

4. **组件类（Component Class）**：
   - 任何被Spring管理的bean都可以被视为组件。这些类通常使用`@Component`注解，可以是任何类型的类，如服务类、工具类等。

5. **数据访问对象（DAO）类**：
   - 提供对数据库的访问，通常包含执行数据库操作的方法。这些类通常使用`@Repository`注解。

6. **数据传输对象（DTO）类**：
   - 用于在系统的不同层之间传输数据。DTO类通常包含数据属性和相应的getter和setter方法，但不包含业务逻辑。

7. **视图类（View Class）**：
   - 在Spring MVC中，视图类负责渲染用户界面。这可以是JSP、Thymeleaf模板或其他视图技术。

8. **异常处理类（Exception Handler Class）**：
   - 用于处理和定义应用程序中可能发生的异常。这些类通常包含处理特定类型异常的方法，并可能返回错误信息或视图。

9. **配置辅助类（Configuration Helper Class）**：
   - 提供配置相关的辅助方法，如属性文件的加载、配置属性的解析等。

10. **拦截器类（Interceptor Class）**：
    - 在Spring MVC中，拦截器类用于在请求处理流程的特定点执行代码，如登录验证、日志记录等。

11. **切面类（Aspect Class）**：
    - 使用Spring AOP（面向切面编程），切面类可以跨越多个类和方法，提供横切关注点的实现，如事务管理、安全性检查等。

12. **事件监听器类（Listener Class）**：
    - 在Spring应用中监听特定事件，如应用启动、bean创建等，并在事件发生时执行相应的操作。



1. **实体类（Entity Class）**:

```java
@Entity
public class User {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String name;
    private String email;

    // Getters and Setters
    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
    public String getEmail() { return email; }
    public void setEmail(String email) { this.email = email; }
}
```

2. **服务类（Service Class）**:

```java
@Service
public class UserService {
    private final UserRepository userRepository;

    public UserService(UserRepository userRepository) {
        this.userRepository = userRepository;
    }

    public User createUser(User user) {
        // Business logic for creating a user
        return userRepository.save(user);
    }
}
```

3. **控制器类（Controller Class）**:

```java
@Controller
public class UserController {
    private final UserService userService;

    public UserController(UserService userService) {
        this.userService = userService;
    }

    @PostMapping("/users")
    public String createUser(@ModelAttribute User user) {
        User createdUser = userService.createUser(user);
        return "redirect:/users/" + createdUser.getId();
    }
}
```

4. **组件类（Component Class）**:

```java
@Component
public class EmailService {
    public void sendEmail(String to, String subject, String body) {
        // Logic to send an email
    }
}
```

5. **数据访问对象（DAO）类**:

```java
@Repository
public interface UserRepository extends JpaRepository<User, Long> {
    // Additional methods if needed
}
```

6. **数据传输对象（DTO）类**:

```java
public class UserDTO {
    private Long id;
    private String name;
    private String email;

    // Getters and Setters
}
```

7. **视图类（View Class）**:

在Spring MVC中，视图通常不是Java类，而是HTML、JSP或Thymeleaf模板。这里提供一个简单的Thymeleaf模板示例：

```html
<!-- user-list.html -->
<table>
    <tr>
        <th>ID</th>
        <th>Name</th>
        <th>Email</th>
    </tr>
    <tr th:each="user : ${users}">
        <td th:text="${user.id}"></td>
        <td th:text="${user.name}"></td>
        <td th:text="${user.email}"></td>
    </tr>
</table>
```

8. **异常处理类（Exception Handler Class）**:

```java
@ControllerAdvice
public class GlobalExceptionHandler {
    @ExceptionHandler(CustomException.class)
    public String handleCustomException(CustomException ex, Model model) {
        model.addAttribute("error", ex.getMessage());
        return "error";
    }
}
```

9. **配置辅助类（Configuration Helper Class）**:

```java
@Configuration
public class AppConfig {
    @Bean
    public PropertySourcesPlaceholderConfigurer propertySourcesPlaceholderConfigurer() {
        PropertySourcesPlaceholderConfigurer configurer = new PropertySourcesPlaceholderConfigurer();
        configurer.setLocation(new ClassPathResource("application.properties"));
        return configurer;
    }
}
```

10. **拦截器类（Interceptor Class）**:

```java
@Component
public class AuthenticationInterceptor implements HandlerInterceptor {
    @Override
    public boolean preHandle(HttpServletRequest request, HttpServletResponse response, Object handler) {
        // Authentication logic
        return true;
    }
}
```

11. **切面类（Aspect Class）**:

```java
@Aspect
@Component
public class LoggingAspect {
    @Before("execution(* com.example.service.*.*(..)) && @annotation(log)")
    public void logBefore(JoinPoint joinPoint, Log annotation) {
        // Logging logic
    }
}
```

12. **事件监听器类（Listener Class）**:

```java
@Component
public class ApplicationListener implements ApplicationListener<ApplicationStartedEvent> {
    @Override
    public void onApplicationEvent(ApplicationStartedEvent event) {
        // Logic to execute when application starts
    }
}
```




[[Spring注解]]