# MongoDB与Redis教材：面向大四学生的AI快速原型开发

## 目标
本教材帮助大四学生掌握**MongoDB**和**Redis**，用于AI快速原型开发，重点涵盖文档操作、缓存策略和实时数据处理，结合Hugging Face模型构建情感分析原型，强调灵活性和高性能。教材详尽、实用，适合有Python基础的学生，契合你的AI研究和生产力兴趣。

## 前提条件
- **受众**：顶尖大学大四学生，熟悉Python和AI/ML入门。
- **先修知识**：Python、JSON、REST API、基本数据库概念。
- **工具**：MongoDB 7.x、Redis 7.x、Python 3.9+、pymongo、redis-py、Jupyter Notebook、VS Code、Git、Docker.
- **时长**：6小时（1.5小时理论+4.5小时实践）。

---

## 第1章：MongoDB与Redis简介

### 1.1 为什么选择MongoDB和Redis？
- **MongoDB优点**：
  - **灵活性**：非结构化数据，动态Schema。
  - **快速原型**：无需预定义表结构。
  - **AI集成**：存储JSON-like情感分析结果。
- **MongoDB缺点**：
  - 查询性能依赖索引。
  - 不适合复杂事务。
- **Redis优点**：
  - **高性能**：内存存储，亚毫秒延迟。
  - **实时处理**：支持Pub/Sub、Streams。
  - **AI集成**：缓存推理结果，实时更新。
- **Redis缺点**：
  - 内存成本高。
  - 数据持久化需配置。
- **适用场景**：AI原型、实时仪表板、推荐系统。
- **反直觉洞察**：MongoDB和Redis组合可实现灵活存储与高性能的平衡，优于单一数据库。

### 1.2 安装与初始化
- **MongoDB安装**：
  - 下载MongoDB Community Server，启动：
    ```bash
    mongod --dbpath ./data/db
    ```
  - Python驱动：
    ```bash
    pip install pymongo
    ```
- **Redis安装**：
  - 使用Docker：
    ```bash
    docker run -d -p 6379:6379 redis
    ```
  - Python驱动：
    ```bash
    pip install redis
    ```
- **MongoDB示例**：
  ```python
  from pymongo import MongoClient

  client = MongoClient("mongodb://localhost:27017/")
  db = client["sentiment_db"]
  collection = db["tweets"]
  collection.insert_one({"text": "I love AI!", "label": "POSITIVE"})
  print(collection.find_one())
  ```
- **Redis示例**：
  ```python
  import redis
<!--ID: 1761111104458-->


  r = redis.Redis(host="localhost", port=6379, decode_responses=True)
  r.set("tweet:1", "POSITIVE")
  print(r.get("tweet:1"))
  ```
- **实践**：连接MongoDB和Redis，插入并查询数据。

---

## 第2章：MongoDB文档操作

### 2.1 CRUD操作
- **插入**：
  ```python
  collection.insert_many([
      {"id": "1", "text": "I love AI!", "label": "POSITIVE"},
      {"id": "2", "text": "AI is hard", "label": "NEGATIVE"}
  ])
  ```
- **查询**：
  ```python
  result = collection.find({"label": "POSITIVE"})
  for doc in result:
      print(doc)
  ```
- **更新**：
  ```python
  collection.update_one({"id": "1"}, {"$set": {"score": 0.9}})
  ```
- **删除**：
  ```python
  collection.delete_one({"id": "2"})
  ```

### 2.2 索引
- **创建索引**：
  ```python
  collection.create_index("id")
  ```

### 2.3 实践
- **任务**：存储情感分析数据。
- **代码**：
  ```python
  from pymongo import MongoClient

  client = MongoClient("mongodb://localhost:27017/")
  db = client["sentiment_db"]
  collection = db["tweets"]
  collection.create_index("id")
  collection.insert_many([
      {"id": "1", "text": "I love AI!", "label": "POSITIVE", "score": 0.9},
      {"id": "2", "text": "AI is hard", "label": "NEGATIVE", "score": 0.7}
  ])
  result = collection.find({"label": "POSITIVE"})
  for doc in result:
      print(doc)
  ```
- **测试**：确认数据插入和查询。
<!--ID: 1761111104464-->


---

## 第3章：Redis缓存与实时处理

### 3.1 缓存
- **设置缓存**：
  ```python
  import redis
  import json

  r = redis.Redis(host="localhost", port=6379, decode_responses=True)
  data = {"id": "1", "label": "POSITIVE", "score": 0.9}
  r.setex("tweet:1", 3600, json.dumps(data))  # 缓存1小时
  print(json.loads(r.get("tweet:1")))
  ```

### 3.2 发布/订阅
- **发布**：
  ```python
  r.publish("sentiment_channel", json.dumps({"id": "1", "label": "POSITIVE"}))
  ```
- **订阅**：
  ```python
  pubsub = r.pubsub()
  pubsub.subscribe("sentiment_channel")
  for message in pubsub.listen():
      if message["type"] == "message":
          print(json.loads(message["data"]))
  ```

### 3.3 实践
- **任务**：缓存推理结果，订阅实时更新。
- **代码**：
  ```python
  import redis
  import json

  r = redis.Redis(host="localhost", port=6379, decode_responses=True)
  data = {"id": "1", "label": "POSITIVE", "score": 0.9}
  r.setex("tweet:1", 3600, json.dumps(data))
  r.publish("sentiment_channel", json.dumps(data))
  print(json.loads(r.get("tweet:1")))
  ```
- **测试**：确认缓存和订阅正常。
<!--ID: 1761111104479-->


---

## 第4章：集成AI原型管道

### 4.1 FastAPI服务
- **示例**（`backend/app.py`）：
  ```python
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
      result = classifier(text)[0]
      data = {"text": text, "label": result["label"], "score": result["score"]}
      collection.insert_one(data)
      r.setex(cache_key, 3600, json.dumps(data))
      r.publish("sentiment_channel", json.dumps(data))
      return data
  ```

### 4.2 工具集成
- **Git**：
  ```bash
  git add .
  git commit -m "Add MongoDB and Redis AI prototype"
  git push origin main
  ```

### 4.3 实践
- **任务**：开发情感分析API。
- **测试**：调用`http://localhost:8000/predict?text=I love AI!`，确认存储和缓存。

---

## 第5章：迷你项目——AI情感分析原型

### 5.1 项目目标
构建AI情感分析原型，包含：
- MongoDB：存储情感分析数据。
- Redis：缓存推理结果，实时更新。
- API：FastAPI提供服务.

### 5.2 项目结构
```
sentiment-prototype/
├── .github/
│   ├── workflows/
│   │   ├── ci.yml
├── backend/
│   ├── app.py
│   ├── requirements.txt
├── Dockerfile
├── docker-compose.yml
```

### 5.3 实现
- **API**（`backend/app.py`）：
  ```python
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
      result = classifier(text)[0]
      data = {"text": text, "label": result["label"], "score": result["score"]}
      collection.insert_one(data)
      r.setex(cache_key, 3600, json.dumps(data))
      r.publish("sentiment_channel", json.dumps(data))
      return data
  ```
- **Dockerfile**：
  ```dockerfile
  FROM python:3.9-slim
  WORKDIR /app
  COPY backend/requirements.txt .
  RUN pip install -r requirements.txt
  COPY backend/ .
  CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
  ```
- **Docker Compose**（`docker-compose.yml`）：
  ```yaml
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
      volumes:
        - mongo-data:/data/db
    redis:
      image: redis:latest
      ports:
        - "6379:6379"
  volumes:
    mongo-data:
  ```
- **依赖**（`backend/requirements.txt`）：
  ```
  fastapi==0.103.0
  uvicorn==0.23.2
  pymongo==4.5.0
  redis==5.0.0
  transformers==4.35.0
  torch==2.1.0
  ```
- **GitHub Actions**（`.github/workflows/ci.yml`）：
  ```yaml
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
<!--ID: 1761111104487-->


### 5.4 测试
- **运行**：
  ```bash
  docker-compose up
  ```
- **测试**：调用`http://localhost:8000/predict?text=I love AI!`，确认MongoDB存储和Redis缓存。

---

## 第6章：优化与进阶

### 6.1 优化
- **MongoDB**：
  ```python
  collection.create_index([("text", 1)])
  ```
- **Redis**：
  ```python
  r.config_set("maxmemory", "100mb")
  r.config_set("maxmemory-policy", "allkeys-lru")
  ```

### 6.2 进阶
- **MongoDB+Neo4j**：结合知识图谱（如你的兴趣）。
- **Redis Streams**：处理复杂实时数据。
- **云部署**：MongoDB Atlas、GCP Memorystore。

### 6.3 实践
- **任务**：优化查询性能，部署到MongoDB Atlas。
- **测试**：比较优化前后延迟。

---

## 资源
- **官方文档**：[MongoDB](https://www.mongodb.com/docs/)、[Redis](https://redis.io/docs/)
- **教程**：MongoDB University、Redis University
- **工具**：MongoDB Compass、Redis CLI、Jupyter Notebook、VS Code、GitHub、Jira、Obsidian
- **建议**：用`notebooklm.google.com`记录开发流程，结合Obsidian或Jira优化任务管理。