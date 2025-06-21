# Polars教程辅助测试：面向大四学生的高性能AI数据处理评估

## 目标
评估学生对Polars核心概念（DataFrame操作、懒惰计算、AI预处理）的掌握情况，以及处理超大数据集的能力。测试结合理论和实践，适合有Python和Pandas基础的大四学生，强调性能与内存效率。

## 测试形式
- **类型**：选择题（10分）、简答题（20分）、编程题（70分）
- **时长**：90分钟
- **评分标准**：正确性（50%）、代码结构（30%）、创新性（20%）

---

## 第1部分：选择题（10分，每题2分）

1. Polars的主要优势是：  
   A. UI开发  
   B. 高性能数据处理  
   C. 模型训练  
   D. 数据库管理  
   **答案**：B

2. LazyFrame用于：  
   A. 实时计算  
   B. 懒惰计算  
   C. 数据可视化  
   D. API调用  
   **答案**：B

3. Polars的底层依赖是：  
   A. NumPy  
   B. Apache Arrow  
   C. Pandas  
   D. SQLAlchemy  
   **答案**：B

4. group_by操作用于：  
   A. 数据过滤  
   B. 分组聚合  
   C. 数据排序  
   D. 文件加载  
   **答案**：B

5. GitHub Actions主要用于：  
   A. 代码托管  
   B. CI/CD自动化  
   C. 数据存储  
   D. 模型推理  
   **答案**：B

---

## 第2部分：简答题（20分，每题10分）

1. **问题**：解释Polars懒惰计算的原理，并说明在AI数据处理中的优势。  
   **参考答案**：  
   - **原理**：延迟执行，优化查询计划，减少内存开销。  
   - **AI优势**：加速大型数据集处理，适合特征工程。  
   - **评分点**：清晰描述原理，提及AI场景。

2. **问题**：描述Polars与Pandas的区别，并说明如何避免技术债务。  
   **参考答案**：  
   - **区别**：Polars基于Rust和Arrow，性能更高；Pandas基于NumPy，生态更成熟。  
   - **技术债务**：规范化代码，使用Parquet，自动化测试。  
   - **评分点**：准确对比，提到技术债务管理。

---

## 第3部分：编程题（70分）

### 编程题1：DataFrame操作（30分）
- **任务**：编写Polars脚本：
  - 加载CSV数据集。
  - 过滤非空文本，分组统计标签。
- **要求**：
  - 使用DataFrame API。
  - 验证统计结果。
- **参考代码**：
  ```python
  import polars as pl

  df = pl.read_csv("tweets.csv")
  df_cleaned = df.filter(pl.col("text").is_not_null()).select([
      pl.col("text"),
      pl.col("label").cast(pl.Categorical)
  ])
  stats = df_cleaned.group_by("label").agg(count=pl.col("text").count())
  print(stats)
  ```
- **测试**：
  ```bash
  python script.py
  ```
- **评分标准**：
  - 数据加载（10分）：正确读取CSV。
  - 数据处理（10分）：过滤与分组正确。
  - 代码结构（5分）：清晰、可读。
  - 测试验证（5分）：统计结果正确。

### 编程题2：AI数据管道与Docker（40分）
- **任务**：构建Polars AI数据处理管道：
  - 处理Parquet数据集，添加token_count特征。
  - 容器化管道。
  - 配置GitHub Actions。
- **要求**：
  - 使用懒惰计算。
  - 处理数据加载错误。
- **参考 code**：
  ```python
  # src/process.py
  import polars as pl
  from transformers import AutoTokenizer

  def process_data(input_file, output_file):
      try:
          tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")
          df = pl.scan_parquet(input_file).filter(
              pl.col("text").is_not_null()
          ).with_columns(
              pl.col("label").cast(pl.Categorical),
              pl.col("text").map_elements(
                  lambda x: len(tokenizer(x)["input_ids"])
              ).alias("token_count")
          ).collect(streaming=True)
          df.write_parquet(output_file)
          return df
      except Exception as e:
          print(f"Error: {e}")
          return None

  if __name__ == "__main__":
      df = process_data("data/tweets.parquet", "data/processed_tweets.parquet")
      if df is not None:
          print(df.head())
  ```
  ```dockerfile
  FROM python:3.9-slim
  WORKDIR /app
  COPY requirements.txt .
  RUN pip install -r requirements.txt
  COPY . .
  CMD ["python", "src/process.py"]
  ```
  ```yaml
  # .github/workflows/ci.yml
  name: CI/CD
  on: [push]
  jobs:
    build:
      runs-on: ubuntu-latest
      steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.9'
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Run processing
        run: python src/process.py
      - name: Build Docker image
        run: docker build -t ghcr.io/coleam00/sentiment-polars:latest .
      - name: Push to GitHub Packages
        run: |
          echo ${{ secrets.GITHUB_TOKEN }} | docker login ghcr.io -u ${{ github.actor }} --password-stdin
          docker push ghcr.io/coleam00/sentiment-polars:latest
  ```
  ```text
  # requirements.txt
  polars==0.20.0
  transformers==4.35.0
  ```
- **测试**：
  ```bash
  docker build -t sentiment-polars .
  docker run sentiment-polars
  ```
- **评分标准**：
  - 数据处理（15分）：懒惰计算与特征提取正确。
  - Docker配置（10分）：容器化成功。
  - Actions配置（10分）：CI/CD运行正常。
  - 错误处理（5分）：处理加载错误。

---

## 注意事项
- **提交**：提交项目文件夹（包含`src/`、`Dockerfile`、`requirements.txt`、`.github/workflows/`）。
- **测试环境**：Python 3.9+、Docker，安装`polars`、`transformers`。
- **建议**：用`notebooklm.google.com`记录处理流程，结合Obsidian或Jira跟踪任务。

## 评分总结
- **选择题**：考察基础概念。
- **简答题**：测试理论和设计思维。
- **编程题**：评估高性能数据处理能力，强调AI预处理。
- **反直觉洞察**：Polars虽新，但其性能和SQL-like接口使其成为Pandas的强大替代品。