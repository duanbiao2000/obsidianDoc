# Docker教材：面向大四学生的AI模型容器化部署

## 目标
本教材帮助大四学生掌握**Docker**，用于容器化AI模型和应用，重点涵盖Dockerfile编写、Docker Compose和多阶段构建，结合Hugging Face模型构建跨环境一致的部署管道。教材详尽、实用，适合有Python基础的学生，强调独立开发者管理复杂依赖，契合你的AI研究和生产力兴趣。

## 前提条件
- **受众**：顶尖大学大四学生，熟悉Python和AI/ML入门。
- **先修知识**：Python、Linux命令、JSON、REST API。
- **工具**：Docker Desktop、Python 3.9+、pip、VS Code、Git、Jupyter Notebook。
- **时长**：6小时（1.5小时理论+4.5小时实践）。

---

## 第1章：Docker简介

### 1.1 为什么选择Docker？
- **优点**：
  - **一致性**：跨开发、测试、生产环境一致。
  - **轻量**：相比虚拟机，资源占用低。
  - **AI集成**：简化Hugging Face、TensorFlow依赖。
- **缺点**：
  - 学习曲线：Dockerfile、Compose需实践。
  - 安全：镜像漏洞需扫描。
- **适用场景**：AI模型部署、微服务、数据管道。
- **反直觉洞察**：Docker虽简化部署，但生产环境需Kubernetes管理复杂性。

### 1.2 安装与第一个容器
- **安装**：参考[Docker Desktop](https://www.docker.com/products/docker-desktop/)。
- **运行**：
  ```bash
  docker run hello-world
  ```
- **实践**：运行`hello-world`，确认Docker正常工作。

---

## 第2章：Dockerfile编写

### 2.1 基本指令
- **示例**：
  ```dockerfile
  FROM python:3.9-slim
  WORKDIR /app
  COPY requirements.txt .
  RUN pip install -r requirements.txt
  COPY . .
  ENTRYPOINT ["python", "app.py"]
  ```
- **AI用例**：容器化Hugging Face模型。
  ```dockerfile
  FROM python:3.9-slim
  WORKDIR /app
  COPY requirements.txt .
  RUN pip install -r requirements.txt
  COPY app.py .
  ENTRYPOINT ["python", "app.py"]
  ```

### 2.2 实践
- **任务**：构建情感分析镜像。
- **代码**（`app.py`）：
  ```python
  from transformers import pipeline

  classifier = pipeline('sentiment-analysis', model='distilbert-base-uncased-finetuned-sst-2-english')
  print(classifier("I love AI!")[0])
  ```
- **依赖**（`requirements.txt`）：
  ```
  transformers==4.35.0
  torch==2.1.0
  ```
- **Dockerfile**：
  ```dockerfile
  FROM python:3.9-slim
  WORKDIR /app
  COPY requirements.txt .
  RUN pip install -r requirements.txt
  COPY app.py .
  CMD ["python", "app.py"]
  ```
- **构建与运行**：
  ```bash
  docker build -t sentiment-app .
  docker run sentiment-app
  ```

---

## 第3章：Docker Compose

### 3.1 Compose结构
- **示例**（`docker-compose.yml`）：
  ```yaml
  version: '3.8'
  services:
    app:
      build: .
      ports:
        - "8000:8000"
    db:
      image: postgres:15
      environment:
        POSTGRES_DB: ai_db
        POSTGRES_USER: user
        POSTGRES_PASSWORD: password
      volumes:
        - db-data:/var/lib/postgresql/data
  volumes:
    db-data:
  ```
- **AI用例**：FastAPI+PostgreSQL情感分析。

### 3.2 实践
- **任务**：编排FastAPI+PostgreSQL。
- **代码**（`app.py`）：
  ```python
  from fastapi import FastAPI
  from transformers import pipeline
  import psycopg2

  app = FastAPI()
  classifier = pipeline('sentiment-analysis', model='distilbert-base-uncased-finetuned-sst-2-english')

  @app.get("/predict")
  def predict(text: str):
      result = classifier(text)[0]
      conn = psycopg2.connect("dbname=ai_db user=user password=password host=db")
      cur = conn.cursor()
      cur.execute("INSERT INTO predictions (text, prediction) VALUES (%s, %s)", (text, result['label']))
      conn.commit()
      cur.close()
      conn.close()
      return {"text": text, "prediction": result['label'], "score": result['score']}
  ```
- **Dockerfile**：
  ```dockerfile
  FROM python:3.9-slim
  WORKDIR /app
  COPY requirements.txt .
  RUN pip install -r requirements.txt
  COPY app.py .
  CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
  ```
- **依赖**（`requirements.txt`）：
  ```
  fastapi==0.103.0
  uvicorn==0.23.2
  transformers==4.35.0
  torch==2.1.0
  psycopg2-binary==2.9.9
  ```
- **运行**：
  ```bash
  docker-compose up
  ```
- **测试**：访问`http://localhost:8000/predict?text=I love AI!`。

---

## 第4章：多阶段构建

### 4.1 多阶段构建
- **示例**：
  ```dockerfile
  # 构建阶段
  FROM python:3.9 AS builder
  WORKDIR /app
  COPY requirements.txt .
  RUN pip install --user -r requirements.txt

  # 生产阶段
  FROM python:3.9-slim
  WORKDIR /app
  COPY --from=builder /root/.local /root/.local
  COPY app.py .
  ENV PATH=/root/.local/bin:$PATH
  CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
  ```

### 4.2 实践
- **任务**：优化情感分析镜像。
- **Dockerfile**：
  ```dockerfile
  FROM python:3.9 AS builder
  WORKDIR /app
  COPY requirements.txt .
  RUN pip install --user -r requirements.txt

  FROM python:3.9-slim
  WORKDIR /app
  COPY --from=builder /root/.local /root/.local
  COPY app.py .
  ENV PATH=/root/.local/bin:$PATH
  CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
  ```
- **测试**：构建镜像，比较体积（`docker images`）。

---

## 第5章：集成AI管道

### 5.1 容器化AI流程
- **代码**：
  ```python
  from fastapi import FastAPI
  from transformers import pipeline
  import psycopg2

  app = FastAPI()
  classifier = pipeline('sentiment-analysis', model='distilbert-base-uncased-finetuned-sst-2-english')

  @app.get("/predict")
  def predict(text: str):
      try:
          result = classifier(text)[0]
          conn = psycopg2.connect("dbname=ai_db user=user password=password host=db")
          cur = conn.cursor()
          cur.execute("INSERT INTO predictions (text, prediction) VALUES (%s, %s)", (text, result['label']))
          conn.commit()
          cur.close()
          conn.close()
          return {"text": text, "prediction": result['label'], "score": result['score']}
      except Exception as e:
          return {"error": str(e)}
  ```

### 5.2 工具集成
- **Git**：版本控制Dockerfile。
- **Jira**：跟踪部署任务（如你的兴趣）。
- **实践**：提交Dockerfile到GitHub，创建Jira任务。

---

## 第6章：迷你项目——AI情感分析容器化部署

### 6.1 项目目标
构建Docker化AI情感分析应用，包含：
- FastAPI推理服务。
- PostgreSQL存储预测。
- 多阶段构建优化镜像。

### 6.2 项目结构
```
sentiment_docker/
├── Dockerfile
├── docker-compose.yml
├── app.py
├── requirements.txt
└── init.sql
```

### 6.3 实现
- **Dockerfile**：
  ```dockerfile
  FROM python:3.9 AS builder
  WORKDIR /app
  COPY requirements.txt .
  RUN pip install --user -r requirements.txt

  FROM python:3.9-slim
  WORKDIR /app
  COPY --from=builder /root/.local /root/.local
  COPY app.py .
  ENV PATH=/root/.local/bin:$PATH
  CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
  ```
- **Compose**（`docker-compose.yml`）：
  ```yaml
  version: '3.8'
  services:
    app:
      build: .
      ports:
        - "8000:8000"
      depends_on:
        - db
    db:
      image: postgres:15
      environment:
        POSTGRES_DB: ai_db
        POSTGRES_USER: user
        POSTGRES_PASSWORD: password
      volumes:
        - ./init.sql:/docker-entrypoint-initdb.d/init.sql
  ```
- **SQL**（`init.sql`）：
  ```sql
  CREATE TABLE predictions (
      id SERIAL PRIMARY KEY,
      text TEXT NOT NULL,
      prediction VARCHAR(50),
      created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
  );
  ```
- **依赖**（`requirements.txt`）：
  ```
  fastapi==0.103.0
  uvicorn==0.23.2
  transformers==4.35.0
  torch==2.1.0
  psycopg2-binary==2.9.9
  ```

### 6.4 测试
- 运行：`docker-compose up`。
- 测试：访问`http://localhost:8000/predict?text=I love AI!`，确认预测和数据库记录。

---

## 第7章：部署与进阶

### 7.1 部署
- **本地**：`docker-compose up`。
- **云部署**：
  - AWS ECS：
    ```bash
    aws ecs register-task-definition --cli-input-json file://task.json
    ```
  - GCP Cloud Run：
    ```bash
    gcloud run deploy sentiment-app \
      --image sentiment-app:latest \
      --region us-central1
    ```

### 7.2 技术债务管理
- **镜像优化**：定期清理未使用镜像（`docker image prune`）。
- **安全**：扫描漏洞（`docker scan`）。
- **模块化**：分离Dockerfile逻辑。

### 7.3 进阶
- **Neo4j**：容器化存储关系（如你的兴趣）。
- **Kubernetes**：生产级编排。
- **CI/CD**：GitHub Actions自动部署。

---

## 资源
- **官方文档**：[Docker](https://docs.docker.com/)、[Hugging Face](https://huggingface.co/docs)
- **教程**：Docker官方教程、Real Python
- **工具**：Docker Desktop、VS Code、GitHub、Jira
- **建议**：用`notebooklm.google.com`记录部署笔记，尝试Obsidian规划Docker工作流。