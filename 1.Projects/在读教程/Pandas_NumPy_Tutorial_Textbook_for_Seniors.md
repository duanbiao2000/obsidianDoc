# Pandas与NumPy教材：面向大四学生的AI数据预处理

## 目标
本教材帮助大四学生掌握**Pandas**和**NumPy**，用于AI数据清洗和预处理，重点涵盖DataFrame操作和向量化计算，结合Hugging Face模型构建高效的数据管道。教材详尽、实用，适合有Python基础的学生，强调与AI框架的衔接，契合你的Python偏好和AI研究兴趣。

## 前提条件
- **受众**：顶尖大学大四学生，熟悉Python和AI/ML入门。
- **先修知识**：Python（列表、字典）、线性代数、统计学。
- **工具**：Python 3.9+、pip、Jupyter Notebook、VS Code、Git。
- **时长**：6小时（1.5小时理论+4.5小时实践）。

---

## 第1章：Pandas与NumPy简介

### 1.1 为什么选择Pandas和NumPy？
- **Pandas优点**：
  - **DataFrame**：表格化数据操作，直观如Excel。
  - **灵活性**：支持多种数据格式（CSV、SQL、JSON）。
  - **AI集成**：与scikit-learn、TensorFlow无缝衔接。
- **NumPy优点**：
  - **向量化**：高效数组计算，优于Python循环。
  - **数学运算**：支持矩阵、统计、线性代数。
- **缺点**：
  - Pandas：大数据性能瓶颈。
  - NumPy：复杂数据结构需结合Pandas。
- **适用场景**：数据清洗、特征工程、嵌入处理。
- **反直觉洞察**：Pandas的简易API隐藏了内存开销，大数据集需优化或用Polars替换。

### 1.2 安装与第一个操作
- **安装**：`pip install pandas numpy`
- **NumPy示例**：
  ```python
  import numpy as np

  arr = np.array([1, 2, 3])
  print(arr * 2)  # 输出: [2 4 6]
  ```
- **Pandas示例**：
  ```python
  import pandas as pd

  df = pd.DataFrame({"text": ["这很好", "不太好"], "label": ["正面", "负面"]})
  print(df)
  ```
- **实践**：加载样例CSV，查看前5行。

---

## 第2章：NumPy向量化计算

### 2.1 数组操作
- **创建**：
  ```python
  import numpy as np

  arr = np.array([[1, 2], [3, 4]])
  zeros = np.zeros((2, 3))
  ```
- **切片**：
  ```python
  print(arr[:, 1])  # 输出: [2 4]
  ```
- **广播**：
  ```python
  print(arr + 10)  # 每个元素加10
  ```

### 2.2 数学运算
- **矩阵运算**：
  ```python
  mat = np.array([[1, 2], [3, 4]])
  print(np.dot(mat, mat))  # 矩阵乘法
  ```
- **统计**：
  ```python
  print(np.mean(arr), np.std(arr))  # 均值、标准差
  ```

### 2.3 AI用例：特征标准化
- **任务**：标准化情感分析特征。
  ```python
  features = np.array([[1, 2], [3, 4], [5, 6]])
  standardized = (features - np.mean(features, axis=0)) / np.std(features, axis=0)
  print(standardized)
  ```
- **实践**：对10x3矩阵进行标准化，验证均值为0、标准差为1。

---

## 第3章：Pandas DataFrame操作

### 3.1 数据加载
- **CSV**：
  ```python
  import pandas as pd

  df = pd.read_csv("sentiment.csv")
  print(df.head())
  ```
- **SQL**：
  ```python
  import sqlite3

  conn = sqlite3.connect("sentiment.db")
  df = pd.read_sql_query("SELECT * FROM predictions", conn)
  ```

### 3.2 数据清洗
- **缺失值**：
  ```python
  df = df.fillna({"score": 0.0})
  df = df.dropna(subset=["text"])
  ```
- **重复值**：
  ```python
  df = df.drop_duplicates(subset=["text"])
  ```

### 3.3 数据转换
- **分组**：
  ```python
  grouped = df.groupby("label")["score"].mean()
  print(grouped)
  ```
- **合并**：
  ```python
  df2 = pd.DataFrame({"text": ["这很好"], "extra": ["info"]})
  merged = df.merge(df2, on="text", how="left")
  ```

### 3.4 AI场景：清洗情感分析数据
- **任务**：清洗CSV数据集。
  ```python
  df = pd.read_csv("sentiment.csv")
  df = df.dropna(subset=["text"])
  df["label"] = df["label"].map({"positive": 1, "negative": 0})
  df["text_length"] = df["text"].str.len()
  print(df.head())
  ```
- **实践**：加载样例CSV，移除缺失值，添加文本长度列。

---

## 第4章：集成AI数据管道

### 4.1 特征工程
- **文本向量化**：
  ```python
  from transformers import AutoTokenizer

  tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")
  df["tokens"] = df["text"].apply(lambda x: tokenizer.encode(x, truncation=True))
  ```
- **标签编码**：
  ```python
  df["label_encoded"] = df["label"].map({"正面": 1, "负面": 0})
  ```

### 4.2 管道优化
- **内存管理**：
  ```python
  df = df.astype({"score": "float32", "label_encoded": "int8"})
  ```
- **并行化**：
  ```python
  from pandarallel import pandarallel

  pandarallel.initialize()
  df["text_clean"] = df["text"].parallel_apply(lambda x: x.lower())
  ```

### 4.3 实践
- **任务**：为Hugging Face模型准备数据。
  ```python
  import pandas as pd
  import numpy as np
  from transformers import AutoTokenizer

  df = pd.DataFrame({
      "text": ["这很好", "不太好", None],
      "label": ["正面", "负面", "负面"]
  })
  df = df.dropna()
  tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")
  df["tokens"] = df["text"].apply(lambda x: tokenizer.encode(x, truncation=True))
  features = np.array(df["tokens"].tolist())
  labels = np.array(df["label"].map({"正面": 1, "负面": 0}))
  print(features, labels)
  ```

---

## 第5章：迷你项目——AI情感分析数据预处理

### 5.1 项目目标
构建Pandas和NumPy数据处理管道，包含：
- 加载情感分析数据集（CSV）。
- 清洗：去除缺失值、标准化文本。
- 特征提取：向量化文本，生成嵌入。
- 输出：AI模型输入数据。

### 5.2 项目结构
```
sentiment_pipeline/
├── pipeline.ipynb
├── sentiment.csv
└── requirements.txt
```

### 5.3 实现
- **Jupyter Notebook**（`pipeline.ipynb`）：
  ```python
  import pandas as pd
  import numpy as np
  from transformers import AutoTokenizer, AutoModel
  import torch

  # 加载数据
  df = pd.read_csv("sentiment.csv")
  print("原始数据：", df.head())

  # 清洗
  df = df.dropna(subset=["text"])
  df = df.drop_duplicates(subset=["text"])
  df["text"] = df["text"].str.lower()
  df["label"] = df["label"].map({"positive": 1, "negative": 0})
  print("清洗后：", df.head())

  # 特征提取
  tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")
  model = AutoModel.from_pretrained("distilbert-base-uncased")
  def get_embedding(text):
      inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
      with torch.no_grad():
          outputs = model(**inputs)
      return outputs.last_hidden_state.mean(dim=1).numpy()[0]

  df["embedding"] = df["text"].apply(get_embedding)
  features = np.stack(df["embedding"].values)
  labels = df["label"].values
  print("特征形状：", features.shape)
  print("标签形状：", labels.shape)

  # 保存
  np.save("features.npy", features)
  np.save("labels.npy", labels)
  ```
- **样例CSV**（`sentiment.csv`）：
  ```
  text,label
  这很好,positive
  不太好,negative
  我爱AI,positive
  ```
- **依赖**（`requirements.txt`）：
  ```
  pandas==2.1.0
  numpy==1.26.0
  transformers==4.35.0
  torch==2.1.0
  pandarallel==1.6.5
  ```

### 5.4 测试
- 运行：打开`pipeline.ipynb`，执行所有单元格。
- 测试：确认生成`features.npy`和`labels.npy`，验证形状正确。

---

## 第6章：优化与进阶

### 6.1 优化
- **向量化**：
  ```python
  # 低效循环
  for i in range(len(df)):
      df.iloc[i, "score"] = df.iloc[i, "score"] * 2
  # 高效向量化
  df["score"] = df["score"] * 2
  ```
- **内存优化**：
  ```python
  df = df[["text", "label"]].copy()  # 仅保留必要列
  ```

### 6.2 替代方案
- **Polars**：更快的数据框处理。
- **Dask**：分布式大数据处理。

### 6.3 进阶
- **Neo4j**：存储数据关系（如你的兴趣）。
- **Spark**：超大数据集处理。
- **Ray**：并行化特征工程。

---

## 资源
- **官方文档**：[Pandas](https://pandas.pydata.org/docs/)、[NumPy](https://numpy.org/doc/)
- **教程**：Pandas官方教程、Hugging Face指南
- **工具**：Jupyter Notebook、VS Code、GitHub
- **建议**：用`notebooklm.google.com`记录管道设计，尝试XMind规划数据流程。