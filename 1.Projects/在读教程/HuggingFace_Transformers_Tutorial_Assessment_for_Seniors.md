# Hugging Face Transformers教程辅助测试：面向大四学生的AI应用开发评估

## 目标
评估学生对Hugging Face Transformers（Pipeline、微调、Tokenizers）的掌握情况，以及开发NLP和多模态AI应用的能力。测试结合理论和实践，适合有Python基础的大四学生，强调快速原型开发。

## 测试形式
- **类型**：选择题（10分）、简答题（20分）、编程题（70分）
- **时长**：90分钟
- **评分标准**：正确性（50%）、代码结构（30%）、创新性（20%）

---

## 第1部分：选择题（10分，每题2分）

1. Hugging Face Pipeline API的主要用途是：  
   A. 模型训练  
   B. 快速推理  
   C. 数据存储  
   D. 模型优化  
   **答案**：B

2. Tokenizer的作用是：  
   A. 模型推理  
   B. 文本分词与编码  
   C. 图像处理  
   D. API部署  
   **答案**：B

3. Trainer API用于：  
   A. 数据预处理  
   B. 模型微调  
   C. 推理加速  
   D. 容器化  
   **答案**：B

4. Datasets库的主要功能是：  
   A. 模型部署  
   B. 数据加载与处理  
   C. 模型量化  
   D. CI/CD配置  
   **答案**：B

5. GitHub Actions主要用于：  
   A. 代码托管  
   B. CI/CD自动化  
   C. 数据存储  
   D. 模型推理  
   **答案**：B

---

## 第2部分：简答题（20分，每题10分）

1. **问题**：解释Hugging Face Transformers在AI开发中的优势，并说明微调的挑战。  
   **参考答案**：  
   - **优势**：预训练模型丰富，Pipeline简化推理，社区支持强。  
   - **挑战**：计算资源需求高，超参数调优复杂。  
   - **评分点**：清晰描述优势与挑战，提及AI场景。

2. **问题**：描述Tokenizer的作用，并说明在多模态任务中的注意事项。  
   **参考答案**：  
   - **作用**：将文本分词并编码为模型输入。  
   - **注意事项**：确保与模型匹配，处理多模态输入格式。  
   - **评分点**：准确描述作用，提到注意事项。

---

## 第3部分：编程题（70分）

### 编程题1：Pipeline与Tokenizer（30分）
- **任务**：编写Python脚本：
  - 用Pipeline实现健康状态分类。
  - 用Tokenizer处理输入文本。
- **要求**：
  - 验证推理结果。
  - 确保Tokenizer正确编码。
- **参考代码**：
  ```python
  from transformers import pipeline, AutoTokenizer

  classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
  tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")

  text = "System is healthy"
  result = classifier(text)
  encoded = tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=128)

  print(result)
  print(encoded)
  ```
- **测试**：
  ```bash
  python script.py
  ```
- **评分标准**：
  - Pipeline推理（10分）：正确分类。
  - Tokenizer处理（10分）：编码正确。
  - 代码结构（5分）：清晰、可读。
  - 测试验证（5分）：输出正常。

### 编程题2：模型微调与部署（40分）
- **任务**：开发情感分析应用：
  - 微调DistilBERT模型。
  - 部署FastAPI服务。
  - 配置GitHub Actions CI/CD。
- **要求**：
  - 处理推理错误。
  - 优化训练效率。
- **参考 code**：
  ```python
  # model/train.py
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
  ```python
  # app/app.py
  from fastapi import FastAPI
  from transformers import pipeline

  app = FastAPI()
  classifier = pipeline("sentiment-analysis", model="./fine_tuned_model")

  @app.get("/predict")
  def predict(text: str):
      try:
          result = classifier(text)[0]
          return {"label": result["label"], "score": result["score"]}
      except Exception as e:
          return {"error": str(e)}
  ```
  ```dockerfile
  # Dockerfile
  FROM python:3.9-slim
  WORKDIR /app
  COPY app/requirements.txt .
  RUN pip install -r requirements.txt
  COPY app/ .
  COPY fine_tuned_model ./fine_tuned_model
  CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
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
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.9'
      - name: Install dependencies
        run: pip install -r app/requirements.txt
      - name: Build Docker image
        run: |
          docker build -t ghcr.io/coleam00/sentiment-api:latest .
          echo ${{ secrets.GITHUB_TOKEN }} | docker login ghcr.io -u ${{ github.actor }} --password-stdin
          docker push ghcr.io/coleam00/sentiment-api:latest
  ```
  ```text
  # app/requirements.txt
  fastapi==0.103.0
  uvicorn==0.23.2
  transformers==4.35.0
  torch==2.1.0
  datasets==2.14.0
  ```
- **测试**：
  ```bash
  docker build -t sentiment-api .
  docker run -p 8000:8000 sentiment-api
  curl "http://localhost:8000/predict?text=I love AI!"
  ```
- **评分标准**：
  - 模型微调（15分）：训练成功。
  - API部署（10分）：服务正常运行。
  - CI/CD配置（10分）：自动化部署成功。
  - 错误处理（5分）：推理错误返回正常。

---

## 注意事项
- **提交**：提交项目文件夹（包含`app/`、`model/`、`Dockerfile`、`.github/workflows/`）。
- **测试环境**：Python 3.9+、Docker、Transformers 4.35.0。
- **建议**：用`notebooklm.google.com`记录开发流程，结合Obsidian或Jira跟踪任务。

## 评分总结
- **选择题**：考察基础概念。
- **简答题**：测试理论和设计思维。
- **编程题**：评估AI应用开发能力，强调快速原型。
- **反直觉洞察**：Transformers通过预训练模型和社区支持加速开发，但优化和部署需谨慎管理。