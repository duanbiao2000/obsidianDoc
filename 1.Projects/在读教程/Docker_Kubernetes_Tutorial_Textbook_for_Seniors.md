# Docker Compose与Kubernetes教材：面向大四学生的AI应用部署

## 目标
本教材帮助大四学生掌握**Docker Compose**和**Kubernetes（K8s）**，从快速部署AI应用过渡到生产级容器编排，重点涵盖Compose配置、K8s资源管理和CI/CD，结合Hugging Face模型部署情感分析服务。教材详尽、实用，适合有Python基础的学生，强调简易性与可扩展性，契合你的AI研究和生产力兴趣。

## 前提条件
- **受众**：顶尖大学大四学生，熟悉Python和AI/ML入门。
- **先修知识**：Python、Docker基础、REST API、基本Linux命令。
- **工具**：Docker、Docker Compose、Kubernetes（Minikube或GKE）、Python 3.9+、kubectl、VS Code、Git.
- **时长**：6小时（1.5小时理论+4.5小时实践）。

---

## 第1章：Docker Compose与K8s简介

### 1.1 为什么选择Docker Compose和K8s？
- **Docker Compose优点**：
  - **简易性**：单机多容器编排，适合本地开发。
  - **快速部署**：YAML定义服务依赖。
  - **AI集成**：快速运行情感分析服务。
- **Docker Compose缺点**：
  - 不支持自动扩展。
  - 生产环境功能有限。
- **K8s优点**：
  - **可扩展性**：自动扩展、自我修复。
  - **生产级**：负载均衡、滚动更新。
  - **AI集成**：管理大规模推理服务。
- **K8s缺点**：
  - 学习曲线陡峭。
  - 配置复杂。
- **适用场景**：AI服务部署、微服务架构。
- **反直觉洞察**：Docker Compose虽简单，但K8s的复杂性为AI生产部署带来长期收益。

### 1.2 安装与初始化
- **Docker Compose**：
  ```bash
  sudo apt-get install docker-compose
  ```
- **Minikube**：
  ```bash
  curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
  sudo install minikube-linux-amd64 /usr/local/bin/minikube
  minikube start
  ```
- **kubectl**：
  ```bash
  curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
  sudo install kubectl /usr/local/bin/kubectl
  ```
- **示例**（Docker Compose）：
  ```yaml
  # docker-compose.yml
  version: '3.8'
  services:
    app:
      image: python:3.9-slim
      command: python -m http.server 8000
      ports:
        - "8000:8000"
  ```
- **实践**：运行Compose服务，访问`http://localhost:8000`。

---

## 第2章：Docker Compose部署

### 2.1 Compose配置
- **示例**（`docker-compose.yml`）：
  ```yaml
  version: '3.8'
  services:
    backend:
      build: ./backend
      ports:
        - "8000:8000"
      depends_on:
        - redis
    redis:
      image: redis:latest
      ports:
        - "6379:6379"
  ```

### 2.2 Dockerfile
- **示例**（`backend/Dockerfile`）：
  ```dockerfile
  FROM python:3.9-slim
  WORKDIR /app
  COPY requirements.txt .
  RUN pip install -r requirements.txt
  COPY . .
  CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
  ```

### 2.3 实践
- **任务**：部署FastAPI情感分析服务。
- **代码**（`backend/app.py`）：
  ```python
  from fastapi import FastAPI
  from transformers import pipeline

  app = FastAPI()
  classifier = pipeline('sentiment-analysis', model='distilbert-base-uncased-finetuned-sst-2-english')

  @app.get("/predict")
  def predict(text: str):
      result = classifier(text)[0]
      return {"label": result["label"], "score": result["score"]}
  ```
- **依赖**（`backend/requirements.txt`）：
  ```
  fastapi==0.103.0
  uvicorn==0.23.2
  transformers==4.35.0
  torch==2.1.0
  ```
- **运行**：
  ```bash
  docker-compose up
  ```
- **测试**：访问`http://localhost:8000/predict?text=I love AI!`。

---

## 第3章：K8s基础与Pod管理

### 3.1 Pod定义
- **示例**（`pod.yaml`）：
  ```yaml
  apiVersion: v1
  kind: Pod
  metadata:
    name: sentiment-pod
  spec:
    containers:
    - name: backend
      image: sentiment-backend:latest
      ports:
      - containerPort: 8000
  ```

### 3.2 Service暴露
- **示例**（`service.yaml`）：
  ```yaml
  apiVersion: v1
  kind: Service
  metadata:
    name: sentiment-service
  spec:
    selector:
      app: sentiment
    ports:
    - protocol: TCP
      port: 80
      targetPort: 8000
    type: NodePort
  ```

### 3.3 实践
- **任务**：迁移Compose服务到K8s。
- **部署**：
  ```bash
  docker build -t sentiment-backend:latest ./backend
  kubectl apply -f pod.yaml
  kubectl apply -f service.yaml
  minikube service sentiment-service
  ```
- **测试**：访问Minikube提供的URL。

---

## 第4章：K8s高级功能

### 4.1 Deployment
- **示例**（`deployment.yaml`）：
  ```yaml
  apiVersion: apps/v1
  kind: Deployment
  metadata:
    name: sentiment-deployment
  spec:
    replicas: 3
    selector:
      matchLabels:
        app: sentiment
    template:
      metadata:
        labels:
          app: sentiment
      spec:
        containers:
        - name: backend
          image: sentiment-backend:latest
          ports:
          - containerPort: 8000
  ```

### 4.2 实践
- **任务**：配置Deployment，暴露Service。
- **部署**：
  ```bash
  kubectl apply -f deployment.yaml
  kubectl apply -f service.yaml
  ```
- **测试**：确认3个Pod运行，访问服务。

---

## 第5章：集成AI部署管道

### 5.1 CI/CD
- **GitHub Actions**（`.github/workflows/ci.yml`）：
  ```yaml
  name: CI/CD
  on: [push]
  jobs:
    deploy:
      runs-on: ubuntu-latest
      steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.9'
      - name: Build Docker image
        run: |
          docker build -t ghcr.io/coleam00/sentiment-backend:latest ./backend
          echo ${{ secrets.GITHUB_TOKEN }} | docker login ghcr.io -u ${{ github.actor }} --password-stdin
          docker push ghcr.io/coleam00/sentiment-backend:latest
      - name: Deploy to Minikube
        run: |
          minikube start
          kubectl apply -f deployment.yaml
          kubectl apply -f service.yaml
  ```

### 5.2 实践
- **任务**：配置CI/CD，部署到Minikube。
- **测试**：确认镜像推送和部署。

---

## 第6章：迷你项目——AI情感分析服务部署

### 6.1 项目目标
从Docker Compose过渡到K8s，部署情感分析服务：
- Compose：本地部署FastAPI+Redis。
- K8s：迁移到Minikube/GKE。
- CI/CD：GitHub Actions自动化。

### 6.2 项目结构
```
sentiment-deployment/
├── .github/
│   ├── workflows/
│   │   ├── ci.yml
├── backend/
│   ├── app.py
│   ├── Dockerfile
│   ├── requirements.txt
├── k8s/
│   ├── deployment.yaml
│   ├── service.yaml
├── docker-compose.yml
```

### 6.3 实现
- **Compose**（`docker-compose.yml`）：
  ```yaml
  version: '3.8'
  services:
    backend:
      build: ./backend
      ports:
        - "8000:8000"
      depends_on:
        - redis
    redis:
      image: redis:latest
      ports:
        - "6379:6379"
  ```
- **K8s Deployment**（`k8s/deployment.yaml`）：
  ```yaml
  apiVersion: apps/v1
  kind: Deployment
  metadata:
    name: sentiment-deployment
  spec:
    replicas: 3
    selector:
      matchLabels:
        app: sentiment
    template:
      metadata:
        labels:
          app: sentiment
      spec:
        containers:
        - name: backend
          image: ghcr.io/coleam00/sentiment-backend:latest
          ports:
          - containerPort: 8000
        - name: redis
          image: redis:latest
          ports:
          - containerPort: 6379
  ```
- **K8s Service**（`k8s/service.yaml`）：
  ```yaml
  apiVersion: v1
  kind: Service
  metadata:
    name: sentiment-service
  spec:
    selector:
      app: sentiment
    ports:
    - protocol: TCP
      port: 80
      targetPort: 8000
    type: NodePort
  ```

### 6.4 测试
- **Compose**：
  ```bash
  docker-compose up
  curl "http://localhost:8000/predict?text=I love AI!"
  ```
- **K8s**：
  ```bash
  minikube start
  kubectl apply -f k8s/deployment.yaml
  kubectl apply -f k8s/service.yaml
  minikube service sentiment-service
  ```

---

## 第7章：优化与进阶

### 7.1 优化
- **HPA**：
  ```yaml
  apiVersion: autoscaling/v2
  kind: HorizontalPodAutoscaler
  metadata:
    name: sentiment-hpa
  spec:
    scaleTargetRef:
      apiVersion: apps/v1
      kind: Deployment
      name: sentiment-deployment
    minReplicas: 2
    maxReplicas: 10
    metrics:
    - type: Resource
      resource:
        name: cpu
        target:
          type: Utilization
          averageUtilization: 70
  ```

### 7.2 进阶
- **Neo4j**：结合知识图谱（如你的兴趣）。
- **Helm**：模板化K8s配置。
- **GKE**：生产级云部署。

### 7.3 实践
- **任务**：配置HPA，优化资源。
- **测试**：模拟高负载，确认Pod扩展。

---

## 资源
- **官方文档**：[Docker Compose](https://docs.docker.com/compose/)、[Kubernetes](https://kubernetes.io/docs/)
- **教程**：Kubernetes Up & Running、Docker Docs
- **工具**：Minikube、kubectl、VS Code、GitHub、Jira、Obsidian
- **建议**：用`notebooklm.google.com`记录部署流程，结合Obsidian或Jira优化任务管理。