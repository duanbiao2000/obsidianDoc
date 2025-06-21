# Spring Boot教程辅助测试：面向大四学生的企业级AI应用开发评估

## 目标
评估学生对Spring Boot核心概念（REST API、AI集成、Docker部署）的掌握情况，以及开发企业级AI应用的能力。测试结合理论和实践，适合有Java基础的大四学生，强调高可维护性与生产部署。

## 测试形式
- **类型**：选择题（10分）、简答题（20分）、编程题（70分）
- **时长**：90分钟
- **评分标准**：正确性（50%）、代码结构（30%）、创新性（20%）

---

## 第1部分：选择题（10分，每题2分）

1. Spring Boot的主要优势是：  
   A. 数据分析  
   B. 自动配置  
   C. UI框架  
   D. 数据库管理  
   **答案**：B

2. @RestController用于：  
   A. 数据库操作  
   B. REST API端点  
   C. 依赖注入  
   D. 模型训练  
   **答案**：B

3. Spring Data JPA用于：  
   A. API路由  
   B. 数据持久化  
   C. 容器化  
   D. 测试框架  
   **答案**：B

4. Dockerfile的ENTRYPOINT指令用于：  
   A. 安装依赖  
   B. 指定启动命令  
   C. 复制文件  
   D. 创建镜像  
   **答案**：B

5. GitHub Actions主要用于：  
   A. 代码托管  
   B. CI/CD自动化  
   C. 数据存储  
   D. 模型推理  
   **答案**：B

---

## 第2部分：简答题（20分，每题10分）

1. **问题**：解释Spring Boot自动配置的原理，并说明在AI应用中的优势。  
   **参考答案**：  
   - **原理**：通过starter依赖和条件注解，自动配置bean和服务器。  
   - **AI优势**：简化REST API开发，快速集成Hugging Face模型。  
   - **评分点**：清晰描述原理，提及AI场景。

2. **问题**：描述Spring Boot与Docker集成的优点，并说明如何避免技术债务。  
   **参考答案**：  
   - **优点**：跨环境一致性，简化部署。  
   - **技术债务**：规范化Dockerfile，定期更新依赖，自动化CI/CD。  
   - **评分点**：准确描述优点，提到技术债务管理。

---

## 第3部分：编程题（70分）

### 编程题1：REST API开发（30分）
- **任务**：编写Spring Boot REST API：
  - 端点：`/api/health`返回健康状态。
  - 使用@Service注入服务层。
- **要求**：
  - 清晰代码结构。
  - 验证API运行。
- **参考代码**：
  ```java
  @RestController
  @RequestMapping("/api")
  public class HealthController {
      private final HealthService service;

      public HealthController(HealthService service) {
          this.service = service;
      }

      @GetMapping("/health")
      public Map<String, String> health() {
          return service.checkHealth();
      }
  }
  ```
  ```java
  @Service
  public class HealthService {
      public Map<String, String> checkHealth() {
          return Map.of("status", "healthy");
      }
  }
  ```
  ```xml
  <!-- pom.xml -->
  <dependency>
      <groupId>org.springframework.boot</groupId>
      <artifactId>spring-boot-starter-web</artifactId>
  </dependency>
  ```
- **测试**：
  ```bash
  mvn spring-boot:run
  curl http://localhost:8080/api/health
  ```
- **评分标准**：
  - 控制器（10分）：正确定义端点。
  - 服务层（10分）：正确注入和实现。
  - 代码结构（5分）：清晰、可读。
  - 测试验证（5分）：API运行正常。

### 编程题2：AI集成与Docker（40分）
- **任务**：构建Spring Boot AI情感分析应用：
  - REST API：`/api/sentiment/predict`调用Python服务。
  - 数据库：H2存储预测结果。
  - Docker：容器化应用。
- **要求**：
  - 处理服务调用错误。
  - 配置GitHub Actions。
- **参考 code**：
  ```java
  @RestController
  @RequestMapping("/api/sentiment")
  public class SentimentController {
      private final SentimentService service;
      private final PredictionRepository repository;

      public SentimentController(SentimentService service, PredictionRepository repository) {
          this.service = service;
          this.repository = repository;
      }

      @GetMapping("/predict")
      public Map<String, Object> predict(@RequestParam String text) {
          try {
              Map<String, String> result = service.predict(text);
              Prediction prediction = new Prediction();
              prediction.setText(text);
              prediction.setPrediction(result.get("prediction"));
              repository.save(prediction);
              return Map.of("text", text, "prediction", result.get("prediction"));
          } catch (Exception e) {
              return Map.of("error", e.getMessage());
          }
      }
  }
  ```
  ```java
  @Service
  public class SentimentService {
      private final RestTemplate restTemplate;

      public SentimentService(RestTemplate restTemplate) {
          this.restTemplate = restTemplate;
      }

      public Map<String, String> predict(String text) {
          String url = "http://localhost:8000/predict?text=" + URLEncoder.encode(text, StandardCharsets.UTF_8);
          ResponseEntity<Map> response = restTemplate.getForEntity(url, Map.class);
          Map<String, String> result = new HashMap<>();
          result.put("prediction", (String) response.getBody().get("label"));
          return result;
      }
  }
  ```
  ```java
  @Entity
  public class Prediction {
      @Id
      @GeneratedValue(strategy = GenerationType.IDENTITY)
      private Long id;
      private String text;
      private String prediction;
      private LocalDateTime createdAt = LocalDateTime.now();
      // Getters and setters
  }
  ```
  ```java
  @Repository
  public interface PredictionRepository extends JpaRepository<Prediction, Long> {
  }
  ```
  ```dockerfile
  FROM openjdk:17-jdk-slim
  WORKDIR /app
  COPY target/sentiment-service-0.0.1-SNAPSHOT.jar app.jar
  ENTRYPOINT ["java", "-jar", "app.jar"]
  ```
  ```yaml
  # .github/workflows/ci.yml
  name: CI/CD
  on: [push]
  jobs:
    build:
      runs-on: ubuntu-latest
      steps:
      - uses: actions/checkout@v3
      - name: Set up JDK 17
        uses: actions/setup-java@v3
        with:
          java-version: '17'
          distribution: 'temurin'
      - name: Build with Maven
        run: mvn package
      - name: Build Docker image
        run: docker build -t ghcr.io/coleam00/sentiment-service:latest .
      - name: Push to GitHub Packages
        run: |
          echo ${{ secrets.GITHUB_TOKEN }} | docker login ghcr.io -u ${{ github.actor }} --password-stdin
          docker push ghcr.io/coleam00/sentiment-service:latest
  ```
- **测试**：
  ```bash
  mvn package
  docker-compose up
  curl http://localhost:8080/api/sentiment/predict?text=I love AI!
  ```
- **评分标准**：
  - API集成（15分）：正确调用Python服务。
  - 数据库存储（10分）：预测结果保存正常。
  - Docker配置（10分）：容器化成功。
  - Actions配置（5分）：CI/CD运行正常。

---

## 注意事项
- **提交**：提交项目文件夹（包含`src/`、`pom.xml`、`Dockerfile`、`.github/workflows/`、`python-service/`）。
- **测试环境**：Java 17、Maven、Docker、Python 3.9+，安装`fastapi`、`transformers`。
- **建议**：用`notebooklm.google.com`记录开发流程，结合Obsidian或Jira跟踪任务。

## 评分总结
- **选择题**：考察基础概念。
- **简答题**：测试理论和设计思维。
- **编程题**：评估企业级AI开发能力，强调集成与部署。
- **反直觉洞察**：Spring Boot虽复杂，但在企业级AI应用中通过自动配置和生态支持大幅提升开发效率。