# PyTorch教程辅助测试：面向大四学生的AI研究与原型开发评估

## 目标
评估学生对PyTorch（张量操作、模型训练、部署）的掌握情况，以及开发AI研究原型的能力。测试结合理论和实践，适合有Python基础的大四学生，强调灵活性和快速迭代。

## 测试形式
- **类型**：选择题（10分）、简答题（20分）、编程题（70分）
- **时长**：90分钟
- **评分标准**：正确性（50%）、代码结构（30%）、创新性（20%）

---

## 第1部分：选择题（10分，每题2分）

1. PyTorch的动态计算图主要优势是：  
   A. 生产部署  
   B. 灵活调试  
   C. 数据存储  
   D. 模型优化  
   **答案**：B

2. 张量操作的核心库是：  
   A. torch.nn  
   B. torch  
   C. torchvision  
   D. torchtext  
   **答案**：B

3. TorchScript用于：  
   A. 数据预处理  
   B. 模型训练  
   C. 静态图导出  
   D. 分布式计算  
   **答案**：C

4. ONNX的主要用途是：  
   A. 模型训练  
   B. 跨框架部署  
   C. 数据可视化  
   D. 超参数调优  
   **答案**：B

5. GitHub Actions主要用于：  
   A. 代码托管  
   B. CI/CD自动化  
   C. 数据存储  
   D. 模型推理  
   **答案**：B

---

## 第2部分：简答题（20分，每题10分）

1. **问题**：解释PyTorch在AI研究中的优势，并说明动态计算图的局限性。  
   **参考答案**：  
   - **优势**：灵活调试，社区活跃，GPU加速。  
   - **局限性**：生产部署需静态化，性能优化复杂。  
   - **评分点**：清晰描述优势与局限，提及研究场景。

2. **问题**：描述TorchScript和ONNX的区别，并说明部署时的注意事项。  
   **参考答案**：  
   - **区别**：TorchScript为PyTorch专用，ONNX跨框架兼容。  
   - **注意事项**：确保输入维度一致，验证模型兼容性。  
   - **评分点**：准确对比，提到部署注意事项。

---

## 第3部分：编程题（70分）

### 编程题1：张量操作与模型定义（30分）
- **任务**：编写Python脚本：
  - 实现张量矩阵乘法。
  - 定义简单神经网络。
- **要求**：
  - 支持GPU加速。
  - 验证模型结构。
- **参考代码**：
  ```python
  import torch
  import torch.nn as nn

  # 张量操作
  x = torch.randn(2, 3)
  y = torch.randn(3, 2)
  if torch.cuda.is_available():
      x, y = x.cuda(), y.cuda()
  z = torch.matmul(x, y)

  # 模型定义
  class SimpleModel(nn.Module):
      def __init__(self):
          super().__init__()
          self.fc = nn.Linear(2, 1)
          self.sigmoid = nn.Sigmoid()

      def forward(self, x):
          return self.sigmoid(self.fc(x))

  model = SimpleModel()
  if torch.cuda.is_available():
      model = model.cuda()

  print(z)
  print(model)
  ```
- **测试**：
  ```bash
  python script.py
  ```
- **评分标准**：
  - 张量操作（10分）：矩阵乘法正确。
  - 模型定义（10分）：结构正确。
  - 代码结构（5分）：清晰、可读。
  - GPU支持（5分）：正确配置。

### 编程题2：模型训练与部署（40分）
- **任务**：开发情感分析模型：
  - 训练PyTorch模型。
  - 导出为TorchScript。
  - 部署FastAPI服务。
  - 配置GitHub Actions CI/CD。
- **要求**：
  - 处理推理错误。
  - 优化训练效率。
- **参考 code**：
  ```python
  # model/train.py
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
  ```python
  # app/app.py
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
  ```dockerfile
  # Dockerfile
  FROM python:3.9-slim
  WORKDIR /app
  COPY app/requirements.txt .
  RUN pip install -r requirements.txt
  COPY app/ .
  COPY sentiment_model.pt .
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
      - name: Train and export
        run: python model/train.py
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
  torch==2.1.0
  transformers==4.35.0
  datasets==2.14.0
  ```
- **测试**：
  ```bash
  docker build -t sentiment-api .
  docker run -p 8000:8000 sentiment-api
  curl "http://localhost:8000/predict?text=I love AI!"
  ```
- **评分标准**：
  - 模型训练（15分）：训练成功。
  - TorchScript导出（10分）：模型导出正确。
  - API部署（10分）：服务正常运行。
  - CI/CD配置（5分）：自动化部署成功。

---

## 注意事项
- **提交**：提交项目文件夹（包含`app/`、`model/`、`Dockerfile`、`.github/workflows/`）。
- **测试环境**：Python 3.9+、Docker、PyTorch 2.1.0。
- **建议**：用`aistudio.google.com`或`notebooklm.google.com`记录实验，结合Obsidian或Jira跟踪任务。

## 评分总结
- **选择题**：考察基础概念。
- **简答题**：测试理论和设计思维。
- **编程题**：评估AI研究与原型能力，强调灵活性。
- **反直觉洞察**：PyTorch的动态计算图加速研究，但部署需静态化优化。