# Spring Boot教材：面向大四学生的企业级AI应用开发

## 目标
本教材帮助大四学生掌握**Spring Boot**，用于开发企业级AI应用，重点涵盖REST API开发、AI模型集成和Docker部署，结合Hugging Face模型构建高可维护的推理服务。教材详尽、实用，适合有Java基础的学生，强调Java生态的企业级优势，契合你的AI研究和生产力兴趣。

## 前提条件
- **受众**：顶尖大学大四学生，熟悉Java和AI/ML入门。
- **先修知识**：Java（OOP、Maven）、Linux命令、REST API、JSON。
- **工具**：Spring Boot 3.x、Java 17、Maven、Docker、VS Code、IntelliJ IDEA、Git、Postman。
- **时长**：8小时（2小时理论+6小时实践）。

---

## 第1章：Spring Boot简介

### 1.1 为什么选择Spring Boot？
- **优点**：
  - **自动配置**：简化依赖管理、服务器设置。
  - **企业级**：高可维护性、强类型安全。
  - **AI集成**：支持REST API调用Hugging Face模型。
- **缺点**：
  - 启动时间较长（相比Quarkus）。
  - 学习曲线较陡。
- **适用场景**：企业级AI服务、微服务、数据管道。
- **反直觉洞察**：Spring Boot看似复杂，但通过约定优于配置大幅提升开发效率。

### 1.2 初始化项目
- **使用Spring Initializr**：
  - URL：[start.spring.io](https://start.spring.io)
  - 依赖：Spring Web、Spring Data JPA、H2 Database。
- **运行**：
  ```bash
  mvn spring-boot:run
  ```
- **示例**：
  ```java
  @RestController
  public class HelloController {
      @GetMapping("/hello")
      public String hello() {
          return "Hello, Spring Boot!";
      }
  }
  ```
- **实践**：初始化项目，运行Hello World API。

---

## 第2章：REST API开发

### 2.1 控制器
- **示例**：
  ```java
  @RestController
  @RequestMapping("/api/sentiment")
  public class SentimentController {
      @GetMapping("/predict")
      public Map<String, String> predict(@RequestParam String text) {
          return Map.of("text", text, "prediction", "positive");
      }
  }
  ```

### 2.2 服务层
- **示例**：
  ```java
  @Service
  public class SentimentService {
      public Map<String, String> predict(String text) {
          return Map.of("text", text, "prediction", "positive");
      }
  }
  ```

### 2.3 数据层
- **实体**：
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
- **仓库**：
  ```java
  @Repository
  public interface PredictionRepository extends JpaRepository<Prediction, Long> {
  }
  ```

### 2.4 实践
- **任务**：开发情感分析API，存储预测。
- **代码**：
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
          Map<String, String> result = service.predict(text);
          Prediction prediction = new Prediction();
          prediction.setText(text);
          prediction.setPrediction(result.get("prediction"));
          repository.save(prediction);
          return Map.of("text", text, "prediction", result.get("prediction"));
      }
  }
  ```
- **测试**：用Postman访问`http://localhost:8080/api/sentiment/predict?text=I love AI!`。

---

## 第3章：集成AI模型

### 3.1 调用Hugging Face模型
- **方式**：通过REST API调用Python服务。
- **Python服务**（`python-service/app.py`）：
  ```python
  from fastapi import FastAPI
  from transformers import pipeline

  app = FastAPI()
  classifier = pipeline('sentiment-analysis', model='distilbert-base-uncased-finetuned-sst-2-english')

  @app.get("/predict")
  def predict(text: str):
      result = classifier(text)[0]
      return {"label": result['label'], "score": result['score']}
  ```
- **Spring Boot调用**：
  ```java
  @Service
  public class SentimentService {
      private final RestTemplate restTemplate;

      public SentimentService(RestTemplate restTemplate) {
          this.restTemplate = restTemplate;
      }

      public Map<String, String> predict(String text) {
          String url = "http://python-service:8000/predict?text=" + URLEncoder.encode(text, StandardCharsets.UTF_8);
          ResponseEntity<Map> response = restTemplate.getForEntity(url, Map.class);
          Map<String, String> result = new HashMap<>();
          result.put("prediction", (String) response.getBody().get("label"));
          return result;
      }
  }
  ```

### 3.2 实践
- **任务**：集成Python情感分析服务。
- **配置**：
  ```java
  @Bean
  public RestTemplate restTemplate() {
      return new RestTemplate();
  }
  ```
- **测试**：调用API，确认推理结果。

---

## 第4章：Docker与部署

### 4.1 Dockerfile
- **示例**：
  ```dockerfile
  FROM openjdk:17-jdk-slim
  WORKDIR /app
  COPY target/sentiment-service-0.0.1-SNAPSHOT.jar app.jar
  ENTRYPOINT ["java", "-jar", "app.jar"]
  ```

### 4.2 Docker Compose
- **示例**（`docker-compose.yml`）：
  ```yaml
  version: '3.8'
  services:
    spring-boot:
      build: .
      ports:
        - "8080:8080"
      depends_on:
        - python-service
        - db
    python-service:
      build: ./python-service
      ports:
        - "8000:8000"
    db:
      image: h2database/h2
      environment:
        H2_URL: jdbc:h2:mem:ai_db
  ```

### 4.3 实践
- **任务**：容器化Spring Boot应用。
- **构建**：
  ```bash
  mvn package
  docker-compose up
  ```
- **测试**：访问`http://localhost:8080/api/sentiment/predict?text=I love AI!`。

---

## 第5章：集成企业级AI管道

### 5.1 代码管理
- **GitHub**：
  ```bash
  git add .
  git commit -m "Add sentiment analysis API"
  git push origin main
  ```

### 5.2 CI/CD
- **GitHub Actions**（`.github/workflows/ci.yml`）：
  ```yaml
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

### 5.3 实践
- **任务**：配置CI/CD，推送镜像。
- **测试**：确认镜像在`ghcr.io/coleam00/sentiment-service`。

---

## 第6章：迷你项目——企业级AI情感分析服务

### 6.1 项目目标
构建Spring Boot AI应用，包含：
- REST API：情感分析端点。
- 数据库：存储预测结果。
- 部署：Docker+GitHub Actions。

### 6.2 项目结构
```
sentiment-service/
├── .github/
│   ├── workflows/
│   │   ├── ci.yml
├── src/
│   ├── main/
│   │   ├── java/
│   │   │   ├── SentimentController.java
│   │   │   ├── SentimentService.java
│   │   │   ├── Prediction.java
│   │   │   ├── PredictionRepository.java
│   │   ├── resources/
│   │   │   ├── application.yml
├── python-service/
│   ├── app.py
│   ├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── pom.xml
```

### 6.3 实现
- **控制器**：
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
          Map<String, String> result = service.predict(text);
          Prediction prediction = new Prediction();
          prediction.setText(text);
          prediction.setPrediction(result.get("prediction"));
          repository.save(prediction);
          return Map.of("text", text, "prediction", result.get("prediction"));
      }
  }
  ```
- **服务**：
  ```java
  @Service
  public class SentimentService {
      private final RestTemplate restTemplate;

      public SentimentService(RestTemplate restTemplate) {
          this.restTemplate = restTemplate;
      }

      public Map<String, String> predict(String text) {
          String url = "http://python-service:8000/predict?text=" + URLEncoder.encode(text, StandardCharsets.UTF_8);
          ResponseEntity<Map> response = restTemplate.getForEntity(url, Map.class);
          Map<String, String> result = new HashMap<>();
          result.put("prediction", (String) response.getBody().get("label"));
          return result;
      }
  }
  ```
- **POM**（`pom.xml`）：
  ```xml
  <dependencies>
      <dependency>
          <groupId>org.springframework.boot</groupId>
          <artifactId>spring-boot-starter-web</artifactId>
      </dependency>
      <dependency>
          <groupId>org.springframework.boot</groupId>
          <artifactId>spring-boot-starter-data-jpa</artifactId>
      </dependency>
      <dependency>
          <groupId>com.h2database</groupId>
          <artifactId>h2</artifactId>
          <scope>runtime</scope>
      </dependency>
  </dependencies>
  ```
- **Python服务**（`python-service/app.py`）：
  ```python
  from fastapi import FastAPI
  from transformers import pipeline

  app = FastAPI()
  classifier = pipeline('sentiment-analysis', model='distilbert-base-uncased-finetuned-sst-2-english')

  @app.get("/predict")
  def predict(text: str):
      result = classifier(text)[0]
      return {"label": result['label'], "score": result['score']}
  ```
- **依赖**（`python-service/requirements.txt`）：
  ```
  fastapi==0.103.0
  uvicorn==0.23.2
  transformers==4.35.0
  torch==2.1.0
  ```

### 6.4 测试
- **运行**：
  ```bash
  mvn package
  docker-compose up
  ```
- **测试**：访问`http://localhost:8080/api/sentiment/predict?text=I love AI!`，确认数据库记录。

---

## 第7章：优化与进阶

### 7.1 优化
- **缓存**：
  ```java
  @Cacheable("predictions")
  public Map<String, String> predict(String text) {
      // ...
  }
  ```
- **异步**：
  ```java
  @Async
  public CompletableFuture<Map<String, String>> predict(String text) {
      // ...
  }
  ```

### 7.2 进阶
- **Neo4j**：存储关系数据（如你的兴趣）。
- **Kubernetes**：生产级编排。
- **Quarkus**：轻量Java替代。

### 7.3 实践
- **任务**：添加缓存，监控API延迟。
- **测试**：比较优化前后性能。

---

## 资源
- **官方文档**：[Spring Boot](https://spring.io/projects/spring-boot)、[Hugging Face](https://huggingface.co/docs)
- **教程**：Spring Boot官方教程、Baeldung
- **工具**：IntelliJ IDEA、VS Code、GitHub、Jira、Obsidian
- **建议**：用`notebooklm.google.com`记录开发流程，结合Obsidian或Jira优化任务管理。