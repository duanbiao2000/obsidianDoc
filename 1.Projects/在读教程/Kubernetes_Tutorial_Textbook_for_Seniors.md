# Kubernetes教材：面向大四学生的容器化AI应用管理

## 目标
本教材帮助大四学生掌握**Kubernetes**，用于管理容器化AI应用，重点涵盖Pod、Service和Helm，结合Hugging Face模型构建高可用、可扩展的部署管道。教材详尽、实用，适合有Python和Docker基础的学生，强调生产级AI规模化，契合你的AI研究和生产力兴趣。

## 前提条件
- **受众**：顶尖大学大四学生，熟悉Python、Docker和AI/ML入门。
- **先修知识**：Python、Docker、Linux命令、YAML、REST API。
- **工具**：Kubernetes（Minikube或GKE/EKS）、kubectl、Helm、Docker Desktop、Python 3.9+、VS Code、Git。
- **时长**：8小时（2小时理论+6小时实践）。

---

## 第1章：Kubernetes简介

### 1.1 为什么选择Kubernetes？
- **优点**：
  - **高可用性**：自动故障恢复、负载均衡。
  - **扩展性**：水平Pod自动扩展（HPA）。
  - **AI集成**：管理Hugging Face、FastAPI容器。
- **缺点**：
  - 学习曲线陡峭。
  - 资源开销高于Docker Compose。
- **适用场景**：AI推理服务、微服务、规模化部署。
- **反直觉洞察**：Kubernetes复杂，但通过Helm和自动化大幅简化管理。

### 1.2 安装与第一个集群
- **安装**：
  - Minikube：`minikube start`
  - kubectl：参考[Kubernetes安装](https://kubernetes.io/docs/tasks/tools/).
- **运行**：
  ```bash
  kubectl get nodes
  ```
- **实践**：启动Minikube，确认集群运行。

---

## 第2章：Pod管理

### 2.1 Pod定义
- **YAML示例**：
  ```yaml
  apiVersion: v1
  kind: Pod
  metadata:
    name: sentiment-pod
  spec:
    containers:
    - name: sentiment
      image: sentiment-app:latest
      ports:
      - containerPort: 8000
  ```
- **运行**：
  ```bash
  kubectl apply -f pod.yaml
  kubectl get pods
  ```

### 2.2 控制器
- **Deployment**：
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
        - name: sentiment
          image: sentiment-app:latest
          ports:
          - containerPort: 8000
  ```
- **AI用例**：运行FastAPI情感分析服务。

### 2.3 实践
- **任务**：部署情感分析Pod。
- **Dockerfile**：
  ```dockerfile
  FROM python:3.9-slim
  WORKDIR /app
  COPY requirements.txt .
  RUN pip install -r requirements.txt
  COPY app.py .
  CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
  ```
- **代码**（`app.py`）：
  ```python
  from fastapi import FastAPI
  from transformers import pipeline

  app = FastAPI()
  classifier = pipeline('sentiment-analysis', model='distilbert-base-uncased-finetuned-sst-2-english')

  @app.get("/predict")
  def predict(text: str):
      result = classifier(text)[0]
      return {"text": text, "prediction": result['label'], "score": result['score']}
  ```
- **依赖**（`requirements.txt`）：
  ```
  fastapi==0.103.0
  uvicorn==0.23.2
  transformers==4.35.0
  torch==2.1.0
  ```
- **测试**：
  ```bash
  docker build -t sentiment-app:latest .
  kubectl apply -f deployment.yaml
  kubectl get pods
  ```

---

## 第3章：Service与网络

### 3.1 Service类型
- **ClusterIP**：
  ```yaml
  apiVersion: v1
  kind: Service
  metadata:
    name: sentiment-service
  spec:
    selector:
      app: sentiment
    ports:
    - port: 80
      targetPort: 8000
    type: ClusterIP
  ```
- **LoadBalancer**：
  ```yaml
  apiVersion: v1
  kind: Service
  metadata:
    name: sentiment-service
  spec:
    selector:
      app: sentiment
    ports:
    - port: 80
      targetPort: 8000
    type: LoadBalancer
  ```

### 3.2 Ingress
- **示例**：
  ```yaml
  apiVersion: networking.k8s.io/v1
  kind: Ingress
  metadata:
    name: sentiment-ingress
  spec:
    rules:
    - host: sentiment.local
      http:
        paths:
        - path: /
          pathType: Prefix
          backend:
            service:
              name: sentiment-service
              port:
                number: 80
  ```
- **AI用例**：暴露情感分析API。

### 3.3 实践
- **任务**：创建Service，暴露API。
- **测试**：
  ```bash
  kubectl apply -f service.yaml
  kubectl port-forward svc/sentiment-service 8000:80
  curl http://localhost:8000/predict?text=I love AI!
  ```

---

## 第4章：Helm部署

### 4.1 Helm核心
- **安装**：`helm install`
- **Chart结构**：
  ```
  sentiment-chart/
  ├── Chart.yaml
  ├── values.yaml
  ├── templates/
  │   ├── deployment.yaml
  │   ├── service.yaml
  ```

### 4.2 自定义Chart
- **Chart.yaml**：
  ```yaml
  apiVersion: v2
  name: sentiment
  version: 1.0.0
  ```
- **values.yaml**：
  ```yaml
  replicas: 3
  image: sentiment-app:latest
  servicePort: 80
  ```
- **deployment.yaml**（templates）：
  ```yaml
  apiVersion: apps/v1
  kind: Deployment
  metadata:
    name: {{ .Release.Name }}-deployment
  spec:
    replicas: {{ .Values.replicas }}
    selector:
      matchLabels:
        app: {{ .Release.Name }}
    template:
      metadata:
        labels:
          app: {{ .Release.Name }}
      spec:
        containers:
        - name: sentiment
          image: {{ .Values.image }}
          ports:
          - containerPort: 8000
  ```

### 4.3 实践
- **任务**：创建Helm Chart，部署应用。
  ```bash
  helm create sentiment-app
  helm install sentiment ./sentiment-app
  ```

---

## 第5章：集成AI管道

### 5.1 容器化AI服务
- **Dockerfile**：参考第2章。
- **Kubernetes部署**：
  ```bash
  kubectl apply -f deployment.yaml
  kubectl apply -f service.yaml
  ```

### 5.2 错误处理
- **资源限制**：
  ```yaml
  spec:
    containers:
    - name: sentiment
      image: sentiment-app:latest
      resources:
        limits:
          memory: "512Mi"
          cpu: "1"
        requests:
          memory: "256Mi"
          cpu: "0.5"
  ```
- **健康检查**：
  ```yaml
  livenessProbe:
      httpGet:
        path: /health
        port: 8000
      initialDelaySeconds: 15
      periodSeconds: 10
  ```

### 5.3 实践
- **任务**：部署AI服务，添加资源限制。
- **测试**：模拟高负载，验证Pod稳定性。

---

## 第6章：迷你项目——AI情感分析Kubernetes部署

### 6.1 项目目标
构建Kubernetes AI应用，包含：
- FastAPI推理服务。
- PostgreSQL存储预测。
- Helm部署。

### 6.2 项目结构
```
sentiment_k8s/
├── Dockerfile
├── app.py
├── requirements.txt
├── init.sql
├── sentiment-chart/
│   ├── Chart.yaml
│   ├── values.yaml
│   ├── templates/
│   │   ├── deployment.yaml
│   │   ├── service.yaml
│   │   ├── postgresql.yaml
└── k8s/
    ├── deployment.yaml
    ├── service.yaml
    └── postgresql.yaml
```

### 6.3 实现
- **Dockerfile**：
  ```dockerfile
  FROM python:3.9-slim
  WORKDIR /app
  COPY requirements.txt .
  RUN pip install -r requirements.txt
  COPY app.py .
  CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
  ```
- **应用**（`app.py`）：
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
          conn = psycopg2.connect("dbname=ai_db user=user password=password host=postgresql")
          cur = conn.cursor()
          cur.execute("INSERT INTO predictions (text, prediction) VALUES (%s, %s)", (text, result['label']))
          conn.commit()
          cur.close()
          conn.close()
          return {"text": text, "prediction": result['label'], "score": result['score']}
      except Exception as e:
          return {"error": str(e)}

  @app.get("/health")
  def health():
      return {"status": "healthy"}
  ```
- **Helm Chart**（`values.yaml`）：
  ```yaml
  replicas: 3
  image: sentiment-app:latest
  servicePort: 80
  postgresql:
    enabled: true
    db: ai_db
    user: user
    password: password
  ```
- **依赖**（`requirements.txt`）：
  ```
  fastapi==0.103.0
  uvicorn==0.23.2
  transformers==4.35.0
  torch==2.1.0
  psycopg2-binary==2.9.9
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

### 6.4 测试
- **部署**：
  ```bash
  docker build -t sentiment-app:latest .
  helm install sentiment ./sentiment-chart
  ```
- **测试**：
  ```bash
  kubectl port-forward svc/sentiment-service 8000:80
  curl http://localhost:8000/predict?text=I love AI!
  ```

---

## 第7章：优化与进阶

### 7.1 优化
- **HPA**：
  ```yaml
  apiVersion: autoscaling/v1
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
    targetCPUUtilizationPercentage: 80
  ```
- **监控**：Prometheus+Grafana。

### 7.2 云部署
- **GKE**：
  ```bash
  gcloud container clusters create sentiment-cluster
  helm install sentiment ./sentiment-chart
  ```
- **EKS**：
  ```bash
  eksctl create cluster --name sentiment-cluster
  ```

### 7.3 进阶
- **Neo4j**：容器化存储关系（如你的兴趣）。
- **ArgoCD**：GitOps部署。
- **Istio**：服务网格。

---

## 资源
- **官方文档**：[Kubernetes](https://kubernetes.io/docs/)、[Helm](https://helm.sh/docs/)
- **教程**：Kubernetes官方教程、Hugging Face部署指南
- **工具**：Minikube、kubectl、Helm、VS Code、GitHub
- **建议**：用`notebooklm.google.com`记录部署笔记，结合Obsidian或Jira优化工作流。