# Docker Compose与Kubernetes教程辅助测试：面向大四学生的AI应用部署评估

## 目标
评估学生对Docker Compose和Kubernetes的掌握情况，以及从快速部署过渡到生产级容器编排的能力。测试结合理论和实践，适合有Python基础的大四学生，强调简易性与可扩展性。

## 测试形式
- **类型**：选择题（10分）、简答题（20分）、编程题（70分）
- **时长**：90分钟
- **评分标准**：正确性（50%）、代码结构（30%）、创新性（20%）

---

## 第1部分：选择题（10分，每题2分）

1. Docker Compose的主要用途是：  
   A. 单机多容器编排  
   B. 生产级自动扩展  
   C. 模型训练  
   D. 数据分析  
   **答案**：A

2. K8s的Pod是：  
   A. 虚拟机  
   B. 最小部署单元  
   C. 数据库  
   D. API网关  
   **答案**：B

3. K8s Service用于：  
   A. 容器构建  
   B. 负载均衡  
   C. 镜像存储  
   D. 代码管理  
   **答案**：B

4. kubectl apply用于：  
   A. 删除资源  
   B. 创建/更新资源  
   C. 编译代码  
   D. 推送镜像  
   **答案**：B

5. GitHub Actions主要用于：  
   A. 代码托管  
   B. CI/CD自动化  
   C. 数据存储  
   D. 模型推理  
   **答案**：B

---

## 第2部分：简答题（20分，每题10分）

1. **问题**：解释Docker Compose在AI部署中的优势，并说明其局限性。  
   **参考答案**：  
   - **优势**：简单配置，快速本地部署，适合开发测试。  
   - **局限性**：不支持自动扩展，生产环境功能不足。  
   - **评分点**：清晰描述优势与局限，提及AI场景。

2. **问题**：描述K8s Deployment的作用，并说明如何避免技术债务。  
   **参考答案**：  
   - **作用**：管理Pod副本，支持滚动更新和自我修复。  
   - **技术债务**：规范化YAML，使用Helm，定期清理旧资源。  
   - **评分点**：准确描述作用，提到债务管理。

---

## 第3部分：编程题（70分）

### 编程题1：Docker Compose部署（30分）
- **任务**：编写Docker Compose配置：
  - 部署健康检查API。
  - 包含Redis服务。
- **要求**：
  - 配置端口映射。
  - 验证服务运行。
- **参考代码**：
  ```yaml
  # docker-compose.yml
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
  ```python
  # backend/app.py
  from fastapi import FastAPI

  app = FastAPI()

  @app.get("/health")
  def health():
      return {"status": "healthy"}
  ```
  ```dockerfile
  # backend/Dockerfile
  FROM python:3.9-slim
  WORKDIR /app
  COPY requirements.txt .
  RUN pip install -r requirements.txt
  COPY . .
  CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
  ```
  ```text
  # backend/requirements.txt
  fastapi==0.103.0
  uvicorn==0.23.2
  ```
- **测试**：
  ```bash
  docker-compose up
  curl http://localhost:8000/health
  ```
- **评分标准**：
  - Compose配置（10分）：正确定义服务。
  - API实现（10分）：返回健康状态。
  - 代码结构（5分）：清晰、可读。
  - 测试验证（5分）：服务运行正常。

### 编程题2：K8s部署与CI/CD（40分）
- **任务**：迁移Compose服务到K8s：
  - 配置Deployment和Service。
  - 集成GitHub Actions CI/CD。
- **要求**：
  - 支持3个Pod副本。
  - 处理部署错误。
- **参考 code**：
  ```yaml
  # k8s/deployment.yaml
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
  ```
  ```yaml
  # k8s/service.yaml
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
  ```yaml
  # .github/workflows/ci.yml
  name: CI/CD
  on: [push]
  jobs:
    deploy:
      runs-on: ubuntu-latest
      steps:
      - uses: actions/checkout@v3
      - name: Build Docker image
        run: |
          docker build -t ghcr.io/coleam00/sentiment-backend:latest ./backend
          echo ${{ secrets.GITHUB_TOKEN }} | docker login ghcr.io -u ${{ github.actor }} --password-stdin
          docker push ghcr.io/coleam00/sentiment-backend:latest
      - name: Deploy to Minikube
        run: |
          minikube start
          kubectl apply -f k8s/deployment.yaml
          kubectl apply -f k8s/service.yaml
  ```
  ```python
  # backend/app.py
  from fastapi import FastAPI
  from transformers import pipeline

  app = FastAPI()
  classifier = pipeline('sentiment-analysis', model='distilbert-base-uncased-finetuned-sst-2-english')

  @app.get("/predict")
  def predict(text: str):
      try:
          result = classifier(text)[0]
          return {"label": result["label"], "score": result["score"]}
      except Exception as e:
          return {"error": str(e)}
  ```
- **测试**：
  ```bash
  minikube start
  kubectl apply -f k8s/deployment.yaml
  kubectl apply -f k8s/service.yaml
  minikube service sentiment-service
  ```
- **评分标准**：
  - Deployment配置（15分）：正确定义3个Pod。
  - Service配置（10分）：服务暴露正常。
  - CI/CD配置（10分）：自动化部署成功。
  - 错误处理（5分）：API错误返回正常。

---

## 注意事项
- **提交**：提交项目文件夹（包含`backend/`、`k8s/`、`docker-compose.yml`、`.github/workflows/`）。
- **测试环境**：Docker、Minikube、Python 3.9+，安装`fastapi`、`transformers`.
- **建议**：用`notebooklm.google.com`记录部署流程，结合Obsidian或Jira跟踪任务。

## 评分总结
- **选择题**：考察基础概念。
- **简答题**：测试理论和设计思维。
- **编程题**：评估AI部署能力，强调从Compose到K8s的过渡。
- **反直觉洞察**：K8s虽复杂，但通过Docker Compose过渡可大幅降低学习门槛。