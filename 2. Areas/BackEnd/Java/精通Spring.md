

## Spring模块


- Spring核心容器提供了Spring Framework的核心功能——依赖注入（DI）、IoC（控制反转）容器和应用程序上下文。
- 横切关注点适用于所有应用程序层——日志记录和安全性等。AOP通常用于实现横切关注点。
- 除了可以全面集成Struts等常用Web框架外，Spring还拥有自己的MVC框架——Spring MVC。
- 业务层主要负责执行应用程序的业务逻辑。使用Spring时，通常在简单Java对象（POJO）中实现业务逻辑。Spring Transactions（spring-tx）为POJO和其他类提供声明式事务管理。
- 数据层通常负责与数据库或外部接口进行交互。

## Spring项目

- Spring Boot 事先提供一组固有设置
- Spring Cloud 实现通用模式
- Spring Data 为不同的数据库提供一致的数据访问方法
- Spring Batch 批处理程序
- Spring Security 声明式身份验证和授权是
- Spring HATEOAS 特别针对通过SpringMVC实现的REST服务。

## 5.0新增功能

- 反应式编程支持； 
- 函数式Web框架；
- Kotlin支持
# 第2章 依赖注入

使用Spring时，一个称为控制反转容器（以下简称IoC容器）的新组件负责创建和装配对象。类定义依赖项，IoC容器创建对象并将依赖项装配在一起。众所周知，这个开创性的概念——由容器负责创建和装配依赖项——称为IoC或依赖注入（DI）。

	依赖注入
	注解
	组件扫描
	bean作用域
	CDI
### Spring IoC容器
Spring IoC容器负责根据应用程序开发人员的配置设置创建bean并将它们装配在一起。
	定义bean和装配(@Component  @Service @Repository)
```java
@Repository
public class DataServiceImpl implements DataService
@Service
public class BussinessServiceImpl implements BuinessService
```
装配: 将DataService类的bean注入BusinessServiceImpl类的bean中 (@Autowired)
```java
public class BusinessServiceImpl{
	@Autowired 
	private DataService dataService;
}
```
硬编码实现DataService
```java
@Repository 
public class DataServiceImpl implements DataService {
	public List<Data> retrieveData (User user) {
		return Arrays.asList(new Data(10), new Data(20));
	}
}
```

### 创建Spring IoC容器
	Bean工厂 (bean声明周期和装配)的基础
	应用程序上下文 (工厂超集)   -建议使用
	应用程序上下文可以采用java配置或XML配置
```java
//Java上下文配置
@Configuration  #定义Spring配置类SpringContext
@ComponentScan (basePackages={"com.mastering.spring"})  #定义组件扫描
class SpringContext{
}
```
### 应用程序上下文的XML配置 (之前介绍Spring Java配置)
	1. 定义XML Spring配置;
	2. 使用XML配置启动应用程序上下文
```XML
//BusinessApplicationContext.xml
<?xml version="1.0" encoding="UTF-8" standalone="no"?> 
<beans>  <!-Namespace definitions removed--> 
  <context:component-scan base-package ="com.mastering.spring"/> 组件扫描
</beans>
```

![[assets/img/精通Spring/IMG-精通Spring-20240714124658391.png]]

	使用@Mock注解为DataService创建模拟对象 
```java
@Mock 
private DataService dataService;

//将他注入接受测试的类BusinessServiceImpl中
@InjectMocks 
private BusinessService service= new BusinessService service = new BusinessServiceImpl();

//采用Mockito BDD方法模拟retrieveData方法:
BDDMockito.given(dataService.retrieveData(
  Matchers.any(Usre.class)))
  .willReturn(Arrays.asList(new Data(10),
  new Data(15), new Data(25)));
//上一段代码定义的内容成为"存根"
```

##  依赖注入类型

	setter注入
	构造函数注入

### setter注入
```java
public class BusinessServiceImpl{
  @Autowired
  private DataService dataService; 
}
```
### 构造函数注入

```java
public class BusinessServiceImpl {
  private DataService dataService;
  @Autowired
  public BusinessServiceImpl (DataService dataService) {
    super();
    this.dataService=dataService;
  }
}
```

# 第3章 Spring MVC
### Model2前端控制器架构

![[assets/img/精通Spring/IMG-精通Spring-20240714124701390.png]]
前端控制器成为 DispatcherServlet

### 创建Spring MVC控制器
```java
@Controller 
public class BasicController {
	@ReuqestMapping(Value = "/welcome")
	@ResponseBody  //构建REST服务
public String welcome() {
  return "welcome to Spring MVC";
}	
}
```

- 设置要测试的控制器
```java
public class BasicControllerTest {
  private MockMvc mockMvc;
  @Before  每次测试前运行以对MockMVC初始化
  public void setup() {
    this.mockMvc = MockMvcBuilders.standaloneSetup(
    new BasicController())
    .build(); 构建MockMvc实例
  }
}
```

- 编写Test方法
![[assets/img/精通Spring/IMG-精通Spring-20240714124701485.png]]

### Spring MVC工作机制
![[assets/img/精通Spring/IMG-精通Spring-20240714124703000.png]]


# 第4章 微服务和云原生应用
	什么事微服务
	云端部署微服务
	微服务相关Spring项目
## Spring开发典型web应用程序架构
![[assets/img/精通Spring/IMG-精通Spring-20240714124703065.png]]
### 数据层
![[assets/img/精通Spring/IMG-精通Spring-20240714124703734.png]]

Spring Framework在应用程序架构中扮演着重要角色。
Spring IoC用于将来自不同层的bean装配在一起。(Spring IoC容器将管理bean的整个生命周期——创建、使用、自动装配和销毁。)
Spring AOP用于将横切关注点织入bean。
Spring还可全面集成不同层中的框架。

## 什么是微服务
	
## 云原生应用程序

## Spring项目

### Spring Boot
### Spring Cloud





# 第5章 Spring Boot构建微服务 (5-7章 通过Boot创建微服务)

	功能
	Spring Initializr
	创建基本RESTful服务

## 快速构建微服务器原型 12步
### 主要目标
- 采用固定配置. 提供配置选项处理偏离默认设置的情况
- 开箱即提供一系列非功能性特性
- 避免大量使用XML配置

## Spring Boot Hello World

1. 在pom.xml中配置spring-boot-starter-parent   (解决框架之间版本兼容性问题)
2. starter (专为不同目的而定制的简化版依赖项描述符)
3. spring-boot-maven-plugin (运行Spring Boot应用程序)
4. Spring Boot启动类
```java
创建Spring Boot启动类

@SpringBootApplication public class ApplicationContext {  
  public static void main(String[] args)
  {
    ApplicationContext ctx = SpringApplication.run(Application.class, args)
  }
}
```
@SpringBootApplication注解是以下3个注解的缩写
- @Conguration   指出Spring应用程序上下文配置文件
- @EnableAutoConfiguration  启用自动配置
- @ComponentScan  在这个类的包和所有子包中扫描Spring bean
### 自动配置

