## Spring注解
![[assets/img/Spring Boot/IMG-Spring Boot-20240714124655322.png]]
 在Spring框架中，`@Service`、`@Repository` 和 `@Controller` 是三个常用的组件注解，它们分别用于标识不同类型的组件，并提供特定的语义和功能。这些注解都继承自 `@Component` 注解，因此它们都具备组件的基本特性，如自动装配（Autowiring）和AOP支持。

1. **@Service**：
   - 用于标识业务逻辑层（Service Layer）的组件。
   - 这些组件通常包含应用程序的核心业务逻辑，如处理数据、执行计算、调用外部服务等。
   - `@Service` 注解的类通常需要与数据访问层（DAO）或持久层（Repository）交互。

   示例：
```java
   @Service
   public class MyService {
       // 业务逻辑方法
   }
   ```

2. **@Repository**：
   - 用于标识数据访问层（Data Access Object）的组件，通常与数据库操作相关。
   - 这些组件负责与数据库进行交互，执行CRUD（创建、读取、更新、删除）操作。
   - `@Repository` 注解的类通常实现 `CrudRepository` 或其他Spring Data JPA提供的接口，以便使用Spring Data JPA的自动实现方法。

   示例：
```java
   @Repository
   public interface MyRepository extends JpaRepository<MyEntity, Long> {
       // 自动实现的方法，如findAll、findById等
   }
   ```

3. **@Controller**：
   - 用于标识Web层的组件，即控制器（Controller）。
   - 控制器负责处理HTTP请求，调用服务层的方法，并返回视图或数据给客户端。
   - `@Controller` 注解的类通常包含处理HTTP请求的方法，这些方法映射到特定的URL路径。

   示例：
```java
   @Controller
   public class MyController {
       @Autowired
       private MyService myService;

       @GetMapping("/my-path")
       public String handleRequest(Model model) {
           // 调用服务层方法
           model.addAttribute("data", myService.getData());
           return "viewName";
       }
   }
   ```

使用这些注解可以帮助你清晰地定义应用程序的结构，并且使得Spring能够自动发现和配置这些组件。这样，你就可以利用Spring的依赖注入和AOP功能来简化组件之间的交互，提高代码的可维护性和可扩展性。

[[Spring Data JPA]]



