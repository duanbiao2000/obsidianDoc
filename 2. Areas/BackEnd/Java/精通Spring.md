

## 依赖注入

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

##  Spring MVC


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


