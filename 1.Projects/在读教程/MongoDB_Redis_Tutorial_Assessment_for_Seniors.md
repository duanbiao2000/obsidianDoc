# MongoDB与Redis教程辅助测试：面向大四学生的AI快速原型开发评估

## 目标
评估学生对MongoDB（文档操作）和Redis（缓存与实时处理）的掌握情况，以及构建AI快速原型的能力。测试结合理论和实践，适合有Python基础的大四学生，强调灵活性和高性能。

## 测试形式
- **类型**：选择题（10分）、简答题（20分）、编程题（70分）
- **时长**：90分钟
- **评分标准**：正确性（50%）、代码结构（30%）、创新性（20%）

---

## 第1部分：选择题（10分，每题2分）

1. MongoDB的主要数据结构是：  
   A. 表格  
   B. 文档  
   C. 键值对  
   D. 图  
   **答案**：B

2. Redis的Pub/Sub用于：  
   A. 数据存储  
   B. 实时消息传递  
   C. 索引优化  
   D. 数据备份  
   **答案**：B

3. MongoDB的create_index用于：  
   A. 创建集合  
   B. 提升查询性能  
   C. 删除文档  
   D. 更新字段  
   **答案**：B

4. Redis的SETEX命令用于：  
   A. 设置永久键值  
   B. 设置带过期时间的键值  
   C. 发布消息  
   D. 删除键  
   **答案**：B



---

## 第2部分：简答题（20分，每题10分）

1. **问题**：解释MongoDB在AI原型中的优势，并说明其局限性。  
   **参考答案**：  
   - **优势**：灵活的Schema，适合非结构化数据，快速迭代。  
   - **局限性**：查询性能依赖索引，不适合复杂事务。  
   - **评分点**：清晰描述优势与局限，提及AI场景。

2. **问题**：描述Redis缓存的作用，并说明如何避免内存溢出。  
   **参考答案**：  
   - **作用**：减少数据库负载，加速数据访问。  
   - **避免溢出**：设置maxmemory，配置LRU策略，监控使用量。  
   - **评分点**：准确描述作用，提到内存管理。

---

## 第3部分：编程题（70分）

### 编程题1：MongoDB文档操作（30分）
- **任务**：编写Python脚本：
  - 插入健康检查数据到MongoDB。
  - 查询状态为“healthy”的文档。
- **要求**：
  - 创建索引。
  - 验证查询结果。
- **参考代码**：
  ```python
  from pymongo import MongoClient

  client = MongoClient("mongodb://localhost:27017/")
  db = client["health_db"]
  collection = db["checks"]
  collection.create_index("id")
  collection.insert_many([
      {"id": "1", "status": "healthy", "timestamp": "2025-06-22"},
      {"id": "2", "status": "unhealthy", "timestamp": "2025-06-22"}
  ])
  result = collection.find({"status": "healthy"})
  for doc in result:
      print(doc)
  ```
- **测试**：
  ```bash
  python script.py
  ```
- **评分标准**：
  - 数据插入（10分）：正确存储文档。
  - 查询实现（10分）：返回正确结果。
  - 代码结构（5分）：清晰、可读。
  - 索引创建（5分）：正确使用索引。
<!--ID: 1761111104502-->


### 编程题2：AI原型与Redis缓存（40分）
- **任务**：构建AI情感分析API：
  - MongoDB：存储情感分析数据。
  - Redis：缓存推理结果。
  - FastAPI：提供服务。
  - Docker：容器化应用。
- **要求**：
  - 处理缓存未命中。
  - 配置GitHub Actions。
- **参考 code**：
  ```python
  # backend/app.py
  from fastapi import FastAPI
  from pymongo import MongoClient
  import redis
  import json
  from transformers import pipeline

  app = FastAPI()
  client = MongoClient("mongodb://mongo:27017/")
  db = client["sentiment_db"]
  collection = db["tweets"]
  r = redis.Redis(host="redis", port=6379, decode_responses=True)
  classifier = pipeline('sentiment-analysis', model='distilbert-base-uncased-finetuned-sst-2-english')

  @app.get("/predict")
  def predict(text: str):
      cache_key = f"tweet:{text}"
      cached = r.get(cache_key)
      if cached:
          return json.loads(cached)
      try:
          result = classifier(text)[0]
          data = {"text": text, "label": result["label"], "score": result["score"]}
          collection.insert_one(data)
          r.setex(cache_key, 3600, json.dumps(data))
          r.publish("sentiment_channel", json.dumps(data))
          return data
      except Exception as e:
          return {"error": str(e)}
  ```
  ```dockerfile
  FROM python:3.9-slim
  WORKDIR /app
  COPY backend/requirements.txt .
  RUN pip install -r requirements.txt
  COPY backend/ .
  CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
  ```
  ```yaml
  # docker-compose.yml
  version: '3.8'
  services:
    backend:
      build: .
      ports:
        - "8000:8000"
      depends_on:
        - mongo
        - redis
    mongo:
      image: mongo:latest
      ports:
        - "27017:27017"
    redis:
      image: redis:latest
      ports:
        - "6379:6379"
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
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.9'
      - name: Install dependencies
        run: pip install -r backend/requirements.txt
      - name: Build Docker image
        run: docker build -t ghcr.io/coleam00/sentiment-prototype:latest .
      - name: Push to GitHub Packages
        run: |
          echo ${{ secrets.GITHUB_TOKEN }} | docker login ghcr.io -u ${{ github.actor }} --password-stdin
          docker push ghcr.io/coleam00/sentiment-prototype:latest
  ```
  ```text
  # backend/requirements.txt
  fastapi==0.103.0
  uvicorn==0.23.2
  pymongo==4.5.0
  redis==5.0.0
  transformers==4.35.0
  torch==2.1.0
  ```
- **测试**：
  ```bash
  docker-compose up
  curl "http://localhost:8000/predict?text=I love AI!"
  ```
- **评分标准**：
  - MongoDB存储（10分）：数据正确插入。
  - Redis缓存（10分）：缓存命中与未命中处理正常。
  - FastAPI服务（10分）：API运行正常。
  - Docker与CI/CD（10分）：容器化与自动化成功。
<!--ID: 1761111104519-->


---

## 注意事项
- **提交**：提交项目文件夹（包含`backend/`、`Dockerfile`、`docker-compose.yml`、`.github/workflows/`）。
- **测试环境**：Python 3.9+、Docker、MongoDB、Redis，安装`pymongo`、`redis`、`fastapi`、`transformers`.
- **建议**：用`notebooklm.google.com`记录开发流程，结合Obsidian或Jira跟踪任务。

## 评分总结
- **选择题**：考察基础概念。
- **简答题**：测试理论和设计思维。
- **编程题**：评估AI原型开发能力，强调灵活性与性能。
- **反直觉洞察**：MongoDB和Redis组合通过灵活存储与高性能缓存大幅加速AI原型开发。