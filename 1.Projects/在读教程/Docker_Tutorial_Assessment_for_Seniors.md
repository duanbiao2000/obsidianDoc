# Docker教程辅助测试：面向大四学生的AI模型容器化部署评估

## 目标
评估学生对Docker核心概念（Dockerfile、Compose、多阶段构建）的掌握情况，以及容器化AI模型的能力。测试结合理论和实践，适合有Python基础的大四学生，强调跨环境一致性。

## 测试形式
- **类型**：选择题（10分）、简答题（20分）、编程题（70分）
- **时长**：90分钟
- **评分标准**：正确性（50%）、代码结构（30%）、创新性（20%）

---

## 第1部分：选择题（10分，每题2分）

1. Docker的主要优势是：  
   A. 高性能计算  
   B. 跨环境一致性  
   C. 数据库管理  
   D. UI框架  
   **答案**：B

2. Dockerfile的ENTRYPOINT指令用于：  
   A. 安装依赖  
   B. 指定容器启动命令  
   C. 复制文件  
   D. 创建镜像  
   **答案**：B

3. Docker Compose适合：  
   A. 单容器部署  
   B. 多容器编排  
   C. 生产级集群  
   D. 数据分析  
   **答案**：B

4. 多阶段构建的主要目的是：  
   A. 增加镜像体积  
   B. 优化镜像大小  
   C. 加速容器启动  
   D. 简化依赖管理  
   **答案**：B

5. 以下哪个工具用于生产级Docker部署？  
   A. Docker Compose  
   B. Kubernetes  
   C. Jupyter Notebook  
   D. pgAdmin  
   **答案**：B

---

## 第2部分：简答题（20分，每题10分）

1. **问题**：解释Dockerfile和Docker Compose的区别，并说明在AI部署中的应用。  
   **参考答案**：  
   - **区别**：Dockerfile定义单个镜像，Compose编排多容器服务。  
   - **AI应用**：Dockerfile构建AI模型镜像，Compose管理前端+后端+数据库。  
   - **评分点**：清晰对比，提及AI场景。

2. **问题**：描述多阶段构建的优点，并说明如何避免技术债务。  
   **参考答案**：  
   - **优点**：减少镜像体积，提升构建效率，分离开发/生产环境。  
   - **技术债务**：规范化Dockerfile，定期清理镜像，自动化CI/CD。  
   - **评分点**：准确描述优点，提到技术债务管理。

---

## 第3部分：编程题（70分）

### 编程题1：Dockerfile编写（30分）
- **任务**：编写Dockerfile，容器化FastAPI应用：
  - 使用`python:3.9-slim`。
  - 安装`fastapi`和`uvicorn`。
  - 运行简单API。
- **要求**：
  - 处理依赖安装。
  - 验证API运行。
- **参考代码**：
  ```dockerfile
  FROM python:3.9-slim
  WORKDIR /app
  COPY requirements.txt .
  RUN pip install -r requirements.txt
  COPY app.py .
  CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
  ```
  ```python
  # app.py
  from fastapi import FastAPI

  app = FastAPI()

  @app.get("/hello")
  def hello():
      return {"message": "Hello, AI!"}
  ```
  ```text
  # requirements.txt
  fastapi==0.103.0
  uvicorn==0.23.2
  ```
- **测试**：
  ```bash
  docker build -t fastapi-app .
  docker run -p 8000:8000 fastapi-app
  ```
- **评分标准**：
  - Dockerfile（10分）：正确定义。
  - API功能（10分）：运行正常。
  - 依赖管理（5分）：requirements.txt正确。
  - 代码结构（5分）：清晰、可读。

### 编程题2：Compose与多阶段构建（40分）
- **任务**：构建Docker化AI情感分析应用：
  - 多阶段Dockerfile：FastAPI+Transformers。
  - Compose：FastAPI+PostgreSQL。
  - 实现预测API，存储结果。
- **要求**：
  - 优化镜像体积。
  - 处理数据库连接错误。
- **参考 code**：
  ```dockerfile
  # Dockerfile
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
  ```yaml
  # docker-compose.yml
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
  ```python
  # app.py
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
  ```sql
  # init.sql
  CREATE TABLE predictions (
      id SERIAL PRIMARY KEY,
      text TEXT NOT NULL,
      prediction VARCHAR(50),
      created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
  );
  ```
  ```text
  # requirements.txt
  fastapi==0.103.0
  uvicorn==0.23.2
  transformers==4.35.0
  torch==2.1.0
  psycopg2-binary==2.9.9
  ```
- **测试**：
  ```bash
  docker-compose up
  curl "http://localhost:8000/predict?text=I love AI!"
  ```
- **评分标准**：
  - 多阶段构建（15分）：镜像优化正确。
  - Compose编排（10分）：服务运行正常。
  - API与数据库（10分）：预测和存储正确。
  - 错误处理（5分）：处理连接错误。

---

## 注意事项
- **提交**：提交项目文件夹（包含`Dockerfile`、`docker-compose.yml`、`app.py`、`init.sql`、`requirements.txt`）。
- **测试环境**：Docker Desktop、Python 3.9+，安装`fastapi`、`transformers`、`psycopg2`。
- **建议**：用`notebooklm.google.com`记录部署流程，结合Obsidian或Jira跟踪任务。

## 评分总结
- **选择题**：考察基础概念。
- **简答题**：测试理论和设计思维。
- **编程题**：评估容器化能力，强调AI部署。
- **反直觉洞察**：Docker简化开发，但生产环境需Kubernetes或CI/CD优化复杂性。