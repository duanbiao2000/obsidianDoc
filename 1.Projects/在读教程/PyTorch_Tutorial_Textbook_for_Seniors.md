# PyTorch教材：面向大四学生的AI研究与原型开发

## 目标
本教材帮助大四学生掌握**PyTorch**，进行AI研究和快速原型开发，重点涵盖**张量操作**、**模型训练**和**部署（ONNX/TorchScript）**，结合Hugging Face数据集构建情感分析模型。教材详尽、实用，适合有Python基础的学生，强调灵活性和快速迭代，契合你的AI研究和生产力兴趣。

## 前提条件
- **受众**：顶尖大学大四学生，熟悉Python和AI/ML入门。
- **先修知识**：Python、NumPy、基本深度学习概念、REST API。
- **工具**：PyTorch 2.x、TorchScript、ONNX、Python 3.9+、Jupyter Notebook、VS Code、Git、Docker.
- **时长**：6小时（1.5小时理论+4.5小时实践）。

---

## 第1章：PyTorch简介

### 1.1 为什么选择PyTorch？
- **优点**：
  - **动态计算图**：灵活，适合研究和调试。
  - **社区活跃**：学术和工业支持广泛。
  - **GPU加速**：CUDA优化性能。
- **缺点**：
  - 生产部署需额外工具（如ONNX）。
  - 学习曲线较陡。
- **适用场景**：学术研究、快速原型、NLP。
- **反直觉洞察**：动态计算图加速开发，但静态化部署（如TorchScript）更适合生产。

### 1.2 安装与初始化
- **安装**：
  ```bash
  pip install torch==2.1.0 torchvision==0.16.0
  ```
- **示例**（张量操作）：
  ```python
  import torch

  x = torch.tensor([[1, 2], [3, 4]], dtype=torch.float32)
  y = torch.matmul(x, x)
  print(y)
  ```
- **实践**：运行张量操作，验证GPU加速。

---

## 第2章：张量操作

### 2.1 张量基础
- **示例**：
  ```python
  import torch

  # 创建张量
  x = torch.randn(2, 3)
  # GPU加速
  if torch.cuda.is_available():
      x = x.cuda()
  # 运算
  y = torch.softmax(x, dim=1)
  print(y)
  ```

### 2.2 数据预处理
- **示例**：
  ```python
  from torch.utils.data import DataLoader
  from datasets import load_dataset

  dataset = load_dataset("imdb")["train"].shuffle(seed=42).select(range(1000))
  def preprocess(examples):
      return {"text": examples["text"], "label": examples["label"]}

  dataloader = DataLoader(dataset, batch_size=8)
  ```

### 2.3 实践
- **任务**：实现张量变换，加载IMDB数据集。
- **测试**：验证张量运算和数据加载。

---

## 第3章：模型训练

### 3.1 自定义模型
- **示例**：
  ```python
  import torch
  import torch.nn as nn

  class SentimentModel(nn.Module):
      def __init__(self, vocab_size, embed_dim, hidden_dim):
          super().__init__()
          self.embedding = nn.Embedding(vocab_size, embed_dim)
          self.fc1 = nn.Linear(embed_dim, hidden_dim)
          self.fc2 = nn.Linear(hidden_dim, 1)
          self.sigmoid = nn.Sigmoid()

      def forward(self, x):
          x = self.embedding(x)
          x = x.mean(dim=1)
          x = torch.relu(self.fc1(x))
          x = self.sigmoid(self.fc2(x))
          return x

  model = SentimentModel(vocab_size=1000, embed_dim=16, hidden_dim=16)
  ```

### 3.2 训练循环
- **示例**：
  ```python
  from torch.optim import Adam
  from transformers import AutoTokenizer

  tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")
  criterion = nn.BCELoss()
  optimizer = Adam(model.parameters(), lr=0.001)

  for epoch in range(3):
      for batch in dataloader:
          texts = batch["text"]
          labels = batch["label"].float()
          inputs = tokenizer(texts, return_tensors="pt", padding=True, truncation=True, max_length=128)["input_ids"]
          outputs = model(inputs).squeeze()
          loss = criterion(outputs, labels)
          optimizer.zero_grad()
          loss.backward()
          optimizer.step()
  ```

### 3.3 实践
- **任务**：训练情感分析模型。
- **测试**：评估模型准确率。

---

## 第4章：模型部署（ONNX/TorchScript）

### 4.1 TorchScript
- **示例**：
  ```python
  model.eval()
  example_input = torch.randint(0, 1000, (1, 128))
  scripted_model = torch.jit.trace(model, example_input)
  scripted_model.save("sentiment_model.pt")
  ```

### 4.2 ONNX
- **示例**：
  ```python
  import torch
  import onnx

  torch.onnx.export(
      model,
      example_input,
      "sentiment_model.onnx",
      input_names=["input"],
      output_names=["output"],
      dynamic_axes={"input": {0: "batch_size"}, "output": {0: "batch_size"}}
  )
  ```

### 4.3 实践
- **任务**：导出模型为TorchScript和ONNX。
- **测试**：加载模型，验证推理。

---

## 第5章：集成AI开发管道

### 5.1 FastAPI部署
- **示例**（`app.py`）：
  ```python
  from fastapi import FastAPI
  import torch
  from transformers import AutoTokenizer

  app = FastAPI()
  model = torch.jit.load("sentiment_model.pt")
  tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")

  @app.get("/predict")
  def predict(text: str):
      try:
          inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=128)["input_ids"]
          outputs = model(inputs).squeeze()
          return {"label": "POSITIVE" if outputs.item() > 0.5 else "NEGATIVE", "score": outputs.item()}
      except Exception as e:
          return {"error": str(e)}
  ```

### 5.2 CI/CD
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
      - name: Install dependencies
        run: pip install -r app/requirements.txt
      - name: Train and export
        run: python model/train.py
      - name: Build Docker image
        run: |
          docker build -t ghcr.io/coleam00/sentiment-api:latest .
          echo ${{ secrets.GITHUB_TOKEN }} | docker login ghcr.io -u ${{ github.actor }} --password-stdin
          docker push ghcr.io/coleam00/sentiment-api:latest
  ```

### 5.3 实践
- **任务**：部署情感分析API。
- **测试**：调用`http://localhost:8000/predict?text=I love AI!`。

---

## 第6章：迷你项目——情感分析模型开发与部署

### 6.1 项目目标
构建情感分析模型开发与部署 pipeline：
- PyTorch：训练模型。
- TorchScript/ONNX：模型导出。
- FastAPI+Docker：API部署。

### 6.2 项目结构
```
sentiment-app/
├── .github/
│   ├── workflows/
│   │   ├── ci.yml
├── app/
│   ├── app.py
│   ├── requirements.txt
├── model/
│   ├── train.py
├── Dockerfile
```

### 6.3 实现
- **训练**（`model/train.py`）：
  ```python
  import torch
  import torch.nn as nn
  from torch.utils.data import DataLoader
  from transformers import AutoTokenizer
  from datasets import load_dataset

  class SentimentModel(nn.Module):
      def __init__(self, vocab_size, embed_dim, hidden_dim):
          super().__init__()
          self.embedding = nn.Embedding(vocab_size, embed_dim)
          self.fc1 = nn.Linear(embed_dim, hidden_dim)
          self.fc2 = nn.Linear(hidden_dim, 1)
          self.sigmoid = nn.Sigmoid()

      def forward(self, x):
          x = self.embedding(x)
          x = x.mean(dim=1)
          x = torch.relu(self.fc1(x))
          x = self.sigmoid(self.fc2(x))
          return x

  model = SentimentModel(vocab_size=1000, embed_dim=16, hidden_dim=16)
  tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")
  dataset = load_dataset("imdb")["train"].shuffle(seed=42).select(range(1000))
  dataloader = DataLoader(dataset, batch_size=8)

  criterion = nn.BCELoss()
  optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

  for epoch in range(3):
      for batch in dataloader:
          texts = batch["text"]
          labels = batch["label"].float()
          inputs = tokenizer(texts, return_tensors="pt", padding=True, truncation=True, max_length=128)["input_ids"]
          outputs = model(inputs).squeeze()
          loss = criterion(outputs, labels)
          optimizer.zero_grad()
          loss.backward()
          optimizer.step()

  torch.jit.save(torch.jit.trace(model, torch.randint(0, 1000, (1, 128))), "sentiment_model.pt")
  ```
- **API**（`app/app.py`）：
  ```python
  from fastapi import FastAPI
  import torch
  from transformers import AutoTokenizer

  app = FastAPI()
  model = torch.jit.load("sentiment_model.pt")
  tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")

  @app.get("/predict")
  def predict(text: str):
      try:
          inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=128)["input_ids"]
          outputs = model(inputs).squeeze()
          return {"label": "POSITIVE" if outputs.item() > 0.5 else "NEGATIVE", "score": outputs.item()}
      except Exception as e:
          return {"error": str(e)}
  ```
- **Dockerfile**：
  ```dockerfile
  FROM python:3.9-slim
  WORKDIR /app
  COPY app/requirements.txt .
  RUN pip install -r requirements.txt
  COPY app/ .
  COPY sentiment_model.pt .
  CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
  ```
- **依赖**（`app/requirements.txt`）：
  ```
  fastapi==0.103.0
  uvicorn==0.23.2
  torch==2.1.0
  transformers==4.35.0
  datasets==2.14.0
  ```

### 6.4 测试
- **运行**：
  ```bash
  docker build -t sentiment-api .
  docker run -p 8000:8000 sentiment-api
  ```
- **测试**：
  ```bash
  curl "http://localhost:8000/predict?text=I love AI!"
  ```

---

## 第7章：优化与进阶

### 7.1 优化
- **混合精度训练**：
  ```python
  from torch.cuda.amp import autocast, GradScaler

  scaler = GradScaler()
  for epoch in range(3):
      for batch in dataloader:
          texts = batch["text"]
          labels = batch["label"].float()
          inputs = tokenizer(texts, return_tensors="pt", padding=True, truncation=True, max_length=128)["input_ids"]
          optimizer.zero_grad()
          with autocast():
              outputs = model(inputs).squeeze()
              loss = criterion(outputs, labels)
          scaler.scale(loss).backward()
          scaler.step(optimizer)
          scaler.update()
  ```

### 7.2 进阶
- **Neo4j**：结合知识图谱（如你的兴趣）。
- **分布式训练**：DataParallel。
- **GCP Vertex AI**：生产部署。

### 7.3 实践
- **任务**：启用混合精度，测试性能。
- **测试**：比较优化前后训练速度。

---

## 资源
- **官方文档**：[PyTorch](https://pytorch.org/docs/stable/index.html)、[ONNX](https://onnx.ai/)
- **教程**：PyTorch Tutorials、GCP AI
- **工具**：Jupyter Notebook、VS Code、GitHub、Jira、Obsidian
- **建议**：用`aistudio.google.com`或`notebooklm.google.com`记录实验，结合Obsidian或Jira优化任务管理。