# Pandas与NumPy教程辅助测试：面向大四学生的AI数据预处理评估

## 目标
评估学生对Pandas和NumPy核心概念（DataFrame操作、向量化计算）的掌握情况，以及构建AI数据预处理管道的能力。测试结合理论和实践，适合有Python基础的大四学生，强调高效数据处理。

## 测试形式
- **类型**：选择题（10分）、简答题（20分）、编程题（70分）
- **时长**：90分钟
- **评分标准**：正确性（50%）、代码结构（30%）、创新性（20%）

---

## 第1部分：选择题（10分，每题2分）

1. Pandas的主要数据结构是：  
   A. ndarray  
   B. DataFrame  
   C. Tensor  
   D. List  
   **答案**：B

2. NumPy的向量化计算优势在于：  
   A. 简化SQL查询  
   B. 高效数组操作  
   C. 复杂UI渲染  
   D. 数据库连接  
   **答案**：B

3. 以下哪个Pandas方法用于处理缺失值？  
   A. `drop_duplicates`  
   B. `fillna`  
   C. `groupby`  
   D. `merge`  
   **答案**：B

4. NumPy的广播机制适用于：  
   A. 数据清洗  
   B. 不同形状数组运算  
   C. 文本向量化  
   D. 数据库查询  
   **答案**：B

5. 以下哪个工具适合超大数据集处理？  
   A. Pandas  
   B. NumPy  
   C. Dask  
   D. Matplotlib  
   **答案**：C

---

## 第2部分：简答题（20分，每题10分）

1. **问题**：解释Pandas DataFrame和NumPy ndarray的区别，并说明在AI特征工程中的应用。  
   **参考答案**：  
   - **区别**：DataFrame是表格化结构，支持异构数据和标签；ndarray是同构数组，专注高效数值计算。  
   - **AI应用**：DataFrame清洗数据集（如缺失值处理），ndarray计算特征（如标准化）。  
   - **评分点**：清晰对比两者，提及AI场景。

2. **问题**：描述Pandas和NumPy的性能优化方法，并说明如何避免技术债务。  
   **参考答案**：  
   - **优化**：Pandas用向量化操作替代循环，NumPy用广播；减少内存占用（如`astype`）。  
   - **技术债务**：避免链式操作，模块化代码，定期更新依赖。  
   - **评分点**：准确描述优化，提到技术债务管理。

---

## 第3部分：编程题（70分）

### 编程题1：NumPy向量化计算（30分）
- **任务**：编写Python脚本，使用NumPy：
  - 创建10x3随机矩阵。
  - 标准化每列（均值0，标准差1）。
- **要求**：
  - 使用向量化操作。
  - 验证结果。
- **参考代码**：
  ```python
  import numpy as np

  # 创建随机矩阵
  np.random.seed(42)
  matrix = np.random.rand(10, 3)

  # 标准化
  standardized = (matrix - np.mean(matrix, axis=0)) / np.std(matrix, axis=0)

  # 验证
  print("均值：", np.mean(standardized, axis=0))  # 接近0
  print("标准差：", np.std(standardized, axis=0))  # 接近1
  ```
- **评分标准**：
  - 矩阵创建（10分）：正确生成。
  - 标准化（10分）：向量化计算正确。
  - 验证（5分）：均值和标准差正确。
  - 代码结构（5分）：清晰、可读。

### 编程题2：Pandas与AI集成（40分）
- **任务**：编写Python脚本，使用Pandas和Hugging Face：
  - 加载情感分析CSV（包含`text`和`label`列）。
  - 清洗：去除缺失值，标准化文本（小写）。
  - 特征提取：生成Hugging Face token。
- **要求**：
  - 处理错误（如空数据）。
  - 输出特征和标签数组。
- **参考 code**：
  ```python
  import pandas as pd
  import numpy as np
  from transformers import AutoTokenizer

  # 加载数据
  try:
      df = pd.read_csv("sentiment.csv")
  except FileNotFoundError:
      print("文件不存在！")
      df = pd.DataFrame()

  # 清洗
  if not df.empty:
      df = df.dropna(subset=["text"])
      df = df.drop_duplicates(subset=["text"])
      df["text"] = df["text"].str.lower()
      df["label"] = df["label"].map({"positive": 1, "negative": 0})

      # 特征提取
      tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")
      df["tokens"] = df["text"].apply(lambda x: tokenizer.encode(x, truncation=True))
      features = np.array(df["tokens"].tolist())
      labels = df["label"].values

      print("特征形状：", features.shape)
      print("标签形状：", labels.shape)
  else:
      print("数据为空！")
  ```
- **评分标准**：
  - 数据清洗（15分）：正确处理缺失值和文本。
  - 特征提取（15分）：Hugging Face token正确。
  - 错误处理（5分）：处理空数据。
  - 代码结构（5分）：清晰、注释完善。

---

## 注意事项
- **提交**：提交项目文件夹（包含`script.py`或`notebook.ipynb`、`sentiment.csv`、`requirements.txt`）。
- **测试环境**：Python 3.9+，安装`pandas`、`numpy`、`transformers`。
- **建议**：记录数据处理过程（如你的`notebooklm.google.com`习惯），便于优化管道设计。

## 评分总结
- **选择题**：考察基础概念。
- **简答题**：测试理论和设计思维。
- **编程题**：评估开发能力，强调向量化和AI集成。
- **反直觉洞察**：Pandas和NumPy虽强大，但大数据场景需优化或替换为Polars/Dask。