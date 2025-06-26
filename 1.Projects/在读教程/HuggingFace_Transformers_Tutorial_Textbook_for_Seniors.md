# Hugging Face Transformers教材：面向大四学生的AI应用开发

## 目标
本教材帮助大四学生掌握**Hugging Face Transformers**，开发NLP和多模态AI应用，重点涵盖**Pipeline API**、**模型微调**和**Tokenizers**，结合Hugging Face数据集构建情感分析和图像分类应用。教材详尽、实用，适合有Python基础的学生，强调快速原型开发，契合你的AI研究和生产力兴趣。

## 前提条件
- **受众**：顶尖大学大四学生，熟悉Python和AI/ML入门。
- **先修知识**：Python、NumPy、基本深度学习概念、REST API。
- **工具**：Transformers 4.x、PyTorch/TensorFlow、Datasets、Python 3.9+、Jupyter Notebook、VS Code、Git、Docker.
- **时长**：6小时（1.5小时理论+4.5小时实践）。

---

## 第1章：Hugging Face Transformers简介

### 1.1 为什么选择Transformers？
- **优点**：
  - **预训练模型**：BERT、LLaMA、CLIP等覆盖广泛任务。
  - **简易性**：Pipeline API快速推理，Trainer API简化微调。
  - **社区驱动**：Model Hub提供丰富资源。
- **缺点**：
  - 计算资源需求高。
  - 部署大型模型需优化。
- **适用场景**：NLP（情感分析）、多模态（图像+文本）。
- **反直觉洞察**：Transformers的通用性使其适合快速原型，但生产部署需针对性优化。

### 1.2 安装与初始化
- **安装**：
  ```bash
  pip install transformers==4.35.0 datasets==2.14.0 torch==2.1.0
  ```
- **示例**（Pipeline）：
  ```python
  from transformers import pipeline

  classifier = pipeline("sentiment-analysis")
  result = classifier("I love AI!")
  print(result)  # [{'label': 'POSITIVE', 'score': 0.999}]
  ```
- **实践**：运行Pipeline，测试情感分析。

---

## 第2章：Pipeline API使用

### 2.1 文本分类
- **示例**：
  ```python
  from transformers import pipeline

  classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
  results = classifier(["I love AI!", "AI is hard"])
  print(results)
  ```

### 2.2 图像分类
- **示例**：
  ```python
  from transformers import pipeline

  image_classifier = pipeline("image-classification", model="google/vit-base-patch16-224")
  result = image_classifier("https://example.com/image.jpg")
  print(result)
  ```

### 2.3 实践
- **任务**：用Pipeline实现情感分析和图像分类。
- **测试**：输入文本和图像，检查输出。

---

## 第3章：模型微调

### 3.1 数据准备
- **示例**：
  ```python
  from datasets import load_dataset

  dataset = load_dataset("imdb")
  train_data = dataset["train"].shuffle(seed=42).select(range(1000))
  ```

### 3.2 Trainer API
- **示例**：
  ```python
  from transformers import AutoModelForSequenceClassification, AutoTokenizer, Trainer, TrainingArguments

  model_name = "distilbert-base-uncased"
  tokenizer = AutoTokenizer.from_pretrained(model_name)
  model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=2)

  def tokenize_function(examples):
      return tokenizer(examples["text"], padding="max_length", truncation=True, max_length=128)

  tokenized_datasets = dataset.map(tokenize_function, batched=True)
  training_args = TrainingArguments(
      output_dir="./results",
      num_train_epochs=3,
      per_device_train_batch_size=8,
      evaluation_strategy="epoch",
  )
  trainer = Trainer(
      model=model,
      args=training_args,
      train_dataset=tokenized_datasets["train"],
      eval_dataset=tokenized_datasets["test"],
  )
  trainer.train()
  ```

### 3.3 实践
- **任务**：微调BERT进行情感分析。
- **测试**：评估模型在测试集上的准确率。

---

## 第4章：Tokenizers与数据处理

### 4.1 Tokenizer
- **示例**：
  ```python
  from transformers import AutoTokenizer

  tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")
  encoded = tokenizer("I love AI!", return_tensors="pt", padding=True, truncation=True, max_length=128)
  print(encoded)
  decoded = tokenizer.decode(encoded["input_ids"][0])
  print(decoded)
  ```

### 4.2 动态填充
- **示例**：
  ```python
  from transformers import DataCollatorWithPadding

  data_collator = DataCollatorWithPadding(tokenizer=tokenizer)
  ```

### 4.3 实践
- **任务**：处理文本数据，准备微调输入。
- **测试**：确认编码和解码正确。

---

## 第5章：集成AI开发管道

### 5.1 FastAPI部署
- **示例**（`app.py`）：
  ```python
  from fastapi import FastAPI
  from transformers import pipeline

  app = FastAPI()
  classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

  @app.get("/predict")
  def predict(text: str):
      try:
          result = classifier(text)[0]
          return {"label": result["label"], "score": result["score"]}
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
        run: pip install -r requirements.txt
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

## 第6章：迷你项目——情感分析与图像分类应用

### 6.1 项目目标
构建情感分析和图像分类应用：
- Pipeline：快速推理。
- 微调：优化BERT和CLIP。
- 部署：FastAPI+Docker。

### 6.2 项目结构
```
sentiment-image-app/
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
  from transformers import AutoModelForSequenceClassification, AutoTokenizer, Trainer, TrainingArguments
  from datasets import load_dataset

  model_name = "distilbert-base-uncased"
  tokenizer = AutoTokenizer.from_pretrained(model_name)
  model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=2)
  dataset = load_dataset("imdb")

  def tokenize_function(examples):
      return tokenizer(examples["text"], padding="max_length", truncation=True, max_length=128)

  tokenized_datasets = dataset.map(tokenize_function, batched=True)
  training_args = TrainingArguments(
      output_dir="./results",
      num_train_epochs=3,
      per_device_train_batch_size=8,
      evaluation_strategy="epoch",
  )
  trainer = Trainer(
      model=model,
      args=training_args,
      train_dataset=tokenized_datasets["train"].shuffle(seed=42).select(range(1000)),
      eval_dataset=tokenized_datasets["test"].shuffle(seed=42).select(range(200)),
  )
  trainer.train()
  model.save_pretrained("./fine_tuned_model")
  tokenizer.save_pretrained("./fine_tuned_model")
  ```
- **API**（`app/app.py`）：
  ```python
  from fastapi import FastAPI
  from transformers import pipeline

  app = FastAPI()
  text_classifier = pipeline("sentiment-analysis", model="./fine_tuned_model")
  image_classifier = pipeline("image-classification", model="google/vit-base-patch16-224")

  @app.get("/predict/text")
  def predict_text(text: str):
      try:
          result = text_classifier(text)[0]
          return {"label": result["label"], "score": result["score"]}
      except Exception as e:
          return {"error": str(e)}

  @app.get("/predict/image")
  def predict_image(url: str):
      try:
          result = image_classifier(url)[0]
          return {"label": result["label"], "score": result["score"]}
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
  COPY fine_tuned_model ./fine_tuned_model
  CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
  ```
- **依赖**（`app/requirements.txt`）：
  ```
  fastapi==0.103.0
  uvicorn==0.23.2
  transformers==4.35.0
  torch==2.1.0
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
  curl "http://localhost:8000/predict/text?text=I love AI!"
  curl "http://localhost:8000/predict/image?url=https://example.com/image.jpg"
  ```

---

## 第7章：优化与进阶

### 7.1 优化
- **量化**：
  ```python
  from transformers import AutoModelForSequenceClassification
  import torch

  model = AutoModelForSequenceClassification.from_pretrained("./fine_tuned_model")
  model.eval()
  quantized_model = torch.quantization.quantize_dynamic(model, {torch.nn.Linear}, dtype=torch.qint8)
  quantized_model.save_pretrained("./quantized_model")
  ```

### 7.2 进阶
- **Neo4j**：结合知识图谱（如你的兴趣）。
- **多模态扩展**：CLIP+文本生成。
- **GCP Vertex AI**：生产部署。

### 7.3 实践
- **任务**：量化模型，测试推理速度。
- **测试**：比较优化前后延迟。

---

## 资源
- **官方文档**：[Hugging Face Transformers](https://huggingface.co/docs/transformers)、[Datasets](https://huggingface.co/docs/datasets)
- **教程**：Hugging Face Course、Model Hub
- **工具**：Jupyter Notebook、VS Code、GitHub、Jira、Obsidian
- **建议**：用`notebooklm.google.com`记录开发流程，结合Obsidian或Jira优化任务管理。