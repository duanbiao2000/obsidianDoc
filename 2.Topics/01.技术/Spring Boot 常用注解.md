---
date: 2025-05-19 13:58
tags: 
source: https://www.bilibili.com/video/BV1Es4y1q7Bf?spm_id_from=333.788.videopod.episodes&vd_source=7038f96b6bb3b14743531b102b109c43&p=8
---


---
Spring Boot 常用注解涵盖了**依赖注入、配置、Web 开发、事务管理、AOP、数据访问**等多个模块。以下是按功能分类的核心注解汇总：

---

## 🧩 核心类注解（Spring Boot 启动相关）

| 注解                         | 作用                                                                    |
| -------------------------- | --------------------------------------------------------------------- |
| `@SpringBootApplication`   | 核心注解，组合了 `@Configuration`、`@EnableAutoConfiguration`、`@ComponentScan` |
| `@EnableAutoConfiguration` | 自动加载 Spring Boot 配置（已包含在上面）                                           |
| `@ComponentScan`           | 扫描组件所在包（默认是当前类所在包及其子包）                                                |
| `@Configuration`           | 表示配置类，可注册 Bean                                                        |

---

## 🧱 依赖注入相关

| 注解                 | 作用                                       |
| ------------------ | ---------------------------------------- |
| `@Component`       | 标识组件，交由 Spring 容器管理                      |
| `@Service`         | 标识服务类，功能同上，语义更清晰                         |
| `@Repository`      | 标识 DAO 类，同时支持异常转换                        |
| `@Controller`      | 标识控制器（用于 MVC）                            |
| `@RestController`  | `@Controller + @ResponseBody`，返回 JSON 结果 |
| `@Autowired`       | 自动注入 Bean（按类型注入）                         |
| `@Qualifier`       | 和 `@Autowired` 配合使用，按名称注入                |
| `@Value("${xxx}")` | 从配置中读取属性值                                |
| `@Resource`        | JSR-250 注解，按名称注入                         |
| `@Bean`            | 注册第三方或手动创建的 Bean                         |

---

## 🌐 Web 开发相关

| 注解                                                                | 作用                          |
| ----------------------------------------------------------------- | --------------------------- |
| `@RequestMapping`                                                 | 映射 HTTP 请求路径（支持 GET/POST 等） |
| `@GetMapping` / `@PostMapping` / `@DeleteMapping` / `@PutMapping` | 更具体的请求方式映射                  |
| `@RequestParam`                                                   | 获取 URL 参数（如 `/api?id=1`）    |
| `@PathVariable`                                                   | 获取路径参数（如 `/api/1`）          |
| `@RequestBody`                                                    | 将请求体映射为对象                   |
| `@ResponseBody`                                                   | 返回 JSON（非页面）                |
| `@ModelAttribute`                                                 | 绑定请求参数到模型属性                 |
| `@CrossOrigin`                                                    | 解决跨域问题                      |

---

## 💾 数据访问与事务

| 注解                | 作用          |
| ----------------- | ----------- |
| `@Transactional`  | 方法或类开启事务    |
| `@Entity`         | 标识为 JPA 实体类 |
| `@Table`          | 指定对应数据库表名   |
| `@Id`             | 主键          |
| `@GeneratedValue` | 主键生成策略      |
| `@Column`         | 字段映射        |

---

## 🔁 AOP / 拦截器 / 条件控制

| 注解                             | 作用                         |
| ------------------------------ | -------------------------- |
| `@Aspect`                      | AOP 切面类                    |
| `@Before`, `@After`, `@Around` | AOP 通知类型                   |
| `@ConditionalOnProperty`       | 属性匹配时才加载 Bean（常用于 starter） |
| `@Profile`                     | 指定配置在哪个环境启用（如 dev、prod）    |

---

## 🧪 测试相关

| 注解                | 作用                      |
| ----------------- | ----------------------- |
| `@SpringBootTest` | 启动整个 Spring Boot 容器进行测试 |
| `@MockBean`       | 创建 Mock 对象并注入           |
| `@WebMvcTest`     | 仅加载 MVC 相关组件进行测试        |

---

如果你需要，我可以直接生成一个包含这些注解的**Spring Boot 项目模板**（含注解示例、说明注释、测试类）。是否需要 zip 包或 GitHub 项目形式？
