# Kubernetes教程辅助测试：面向大四学生的容器化AI应用管理评估

## 目标
评估学生对Kubernetes核心概念（Pod、Service、Helm）的掌握情况，以及管理容器化AI应用的能力。测试结合理论和实践，适合有Python和Docker基础的大四学生，强调高可用性和扩展性。

## 测试形式
- **类型**：选择题（10分）、简答题（20分）、编程题（70分）
- **时长**：90分钟
- **评分标准**：正确性（50%）、代码结构（30%）、创新性（20%）

---

## 第1部分：选择题（10分，每题2分）

1. Kubernetes的主要功能是：  
   A. 数据分析  
   B. 容器编排  
   C. 模型训练  
   D. UI框架  
   **答案**：B

2. Pod是Kubernetes的：  
   A. 最小调度单位  
   B. 存储单元  
   C. 网络服务  
   D. 监控工具  
   **答案**：A

3. Service类型LoadBalancer用于：  
   A. 内部通信  
   B. 外部访问  
   C. 数据持久化  
   D. 自动扩展  
   **答案**：B

4. Helm的主要作用是：  
   A. 容器构建  
   B. 应用打包  
   C. 数据库管理  
   D. 代码调试  
   **答案**：B

5. 以下哪个工具用于Kubernetes自动扩展？  
   A. Ingress  
   B. HPA  
   C. ClusterIP  
   D. ConfigMap  
   **答案**：B

---

## 第2部分：简答题（20分，每题10分）

1. **问题**：解释Pod和Service的区别，并说明在AI服务部署中的应用。  
   **参考答案**：  
   - **区别**：Pod是运行容器的最小单位，Service提供网络访问和负载均衡。  
   - **AI应用**：Pod运行AI推理容器，Service暴露API端点。  
   - **评分点**：清晰对比，提及AI场景。

2. **问题**：描述Helm的优点，并说明如何避免技术债务。  
   **参考答案**：  
   - **优点**：简化部署，参数化配置，版本管理。  
   - **技术债务**：规范化Chart结构，定期更新依赖，自动化测试。  
   - **评分点**：准确描述优点，提到技术债务管理。

---

## 第3部分：编程题（70分）

### 编程题1：Pod与Service（30分）
- **任务**：编写Kubernetes YAML文件：
  - 部署FastAPI情感分析Pod（3个副本）。
  - 创建ClusterIP Service暴露API。
- **要求**：
  - 添加资源限制。
  - 验证API访问。
- **参考代码**：
  ```yaml
  # deployment.yaml
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
          resources:
            limits:
              memory: "512Mi"
              cpu: "1"
            requests:
              memory: "256Mi"
              cpu: "0.5"
  ```
  ```yaml
  # service.yaml
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
  ```dockerfile
  # Dockerfile
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

  @app.get("/predict")
  def predict(text: str):
      return {"text": text, "prediction": "positive"}
  ```
  ```text
  # requirements.txt
  fastapi==0.103.0
  uvicorn==0.23.2
  ```
- **测试**：
  ```bash
  docker build -t sentiment-app:latest .
  kubectl apply -f deployment.yaml
  kubectl apply -f service.yaml
  kubectl port-forward svc/sentiment-service 8000:80
  curl http://localhost:8000/predict?text=I love AI!
  ```
- **评分标准**：
  - Deployment（10分）：正确配置副本和容器。
  - Service（10分）：正确暴露API。
  - 资源限制（5分）：正确设置。
  - 代码结构（5分）：清晰、可读。

### 编程题2：Helm与AI部署（40分）
- **任务**：构建Helm Chart，部署AI情感分析应用：
  - FastAPI推理服务。
  - PostgreSQL存储预测。
- **要求**：
  - 参数化replicas和image。
  - 处理数据库连接错误。
- **参考 code**：
  ```yaml
  # sentiment-chart/Chart.yaml
  apiVersion: v2
  name: sentiment
  version: 1.0.0
  ```
  ```yaml
  # sentiment-chart/values.yaml
  replicas: 2
  image: sentiment-app:latest
  servicePort: 80
  postgresql:
    enabled: true
    db: ai_db
    user: user
    password: password
  ```
  ```yaml
  # sentiment-chart/templates/deployment.yaml
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
          env:
          - name: DB_HOST
            value: {{ .Release.Name }}-postgresql
  ```
  ```yaml
  # sentiment-chart/templates/service.yaml
  apiVersion: v1
  kind: Service
  metadata:
    name: {{ .Release.Name }}-service
  spec:
    selector:
      app: {{ .Release.Name }}
    ports:
    - port: {{ .Values.servicePort }}
      targetPort: 8000
    type: ClusterIP
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
          conn = psycopg2.connect("dbname=ai_db user=user password=password host={{DB_HOST}}")
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
  docker build -t sentiment-app:latest .
  helm install sentiment ./sentiment-chart
  kubectl port-forward svc/sentiment-service 8000:80
  curl http://localhost:8000/predict?text=I love AI!
  ```
- **评分标准**：
  - Helm Chart（15分）：正确配置和参数化。
  - AI服务（15分）：推理和存储正常。
  - 错误处理（5分）：处理数据库连接。
  - 代码结构（5分）：清晰、可读。

---

## 注意事項
- **提交**：提交项目文件夹（包含`Dockerfile`、`app.py`、`requirements.txt`、`init.sql`、`sentiment-chart/`）。
- **测试環境**：Minikube、Python 3.9+，安裝`fastapi`、`transformers`、`psycopg2`、Helm。
- **建議**：用`notebooklm.google.com`記錄部署流程，結合Obsidian或Jira優化任務管理。

## 評分總結
- **選擇題**：考察基礎概念。
- **簡答題**：測試理論和設計思維。
- **程式題**：評估容器化能力，強調AI規模化。
- **反直覺洞察**：Kubernetes初期複雜，但通過Helm和自動化大幅提升AI部署效率。