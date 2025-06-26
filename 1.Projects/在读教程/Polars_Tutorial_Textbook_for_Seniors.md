# Polars教材：面向大四学生的高性能AI数据处理

## 目标
本教材帮助大四学生掌握**Polars**，替换Pandas处理超大数据集，重点涵盖DataFrame操作、查询优化和AI数据预处理，结合Hugging Face模型构建高效数据管道。教材详尽、实用，适合有Python和Pandas基础的学生，强调性能与内存效率，契合你的AI研究和生产力兴趣。

## 前提条件
- **受众**：顶尖大学大四学生，熟悉Python、Pandas和AI/ML入门。
- **先修知识**：Python、Pandas、NumPy、基本SQL、CSV/Parquet文件处理。
- **工具**：Polars、Python 3.9+、Jupyter Notebook、VS Code、Git、Docker。
- **时长**：6小时（1.5小时理论+4.5小时实践）。

---

## 第1章：Polars简介

### 1.1 为什么选择Polars？
- **优点**：
  - **性能**：Rust实现，多核并行。
  - **内存效率**：Arrow backend，零拷贝。
  - **AI集成**：处理大型数据集，供模型训练/推理。
- **缺点**：
  - 生态较Pandas新。
  - 学习曲线：懒惰计算需适应。
- **适用场景**：AI数据预处理、大规模分析、特征工程。
- **反直觉洞察**：Polars虽复杂，但其SQL-like接口对Pandas用户更易上手。

### 1.2 安装与初始化
- **安装**：
  ```bash
  pip install polars
  ```
- **示例**：
  ```python
  import polars as pl

  df = pl.DataFrame({
      "text": ["I love AI!", "AI is hard"],
      "label": ["POSITIVE", "NEGATIVE"]
  })
  print(df)
  ```
- **实践**：加载示例CSV，打印前5行。

---

## 第2章：数据操作基础

### 2.1 DataFrame操作
- **加载**：
  ```python
  df = pl.read_csv("tweets.csv")
  ```
- **过滤**：
  ```python
  df_filtered = df.filter(pl.col("label") == "POSITIVE")
  ```
- **分组**：
  ```python
  df_grouped = df.group_by("label").agg(count=pl.col("text").count())
  ```

### 2.2 实践
- **任务**：清洗Twitter情感数据集。
- **代码**：
  ```python
  import polars as pl

  df = pl.read_csv("tweets.csv")
  df_cleaned = df.filter(pl.col("text").is_not_null()).select([
      pl.col("text"),
      pl.col("label").cast(pl.Categorical)
  ])
  print(df_cleaned)
  ```
- **测试**：确认数据清洗，统计标签分布。

---

## 第3章：查询优化与懒惰计算

### 3.1 懒惰计算
- **示例**：
  ```python
  lazy_df = pl.scan_csv("tweets.csv").filter(pl.col("label") == "POSITIVE").select([
      pl.col("text"),
      pl.col("label")
  ])
  print(lazy_df.explain())  # 查看查询计划
  df = lazy_df.collect()  # 执行计算
  ```

### 3.2 并行处理
- **示例**：
  ```python
  df = pl.read_parquet("large_tweets.parquet")
  df_grouped = df.group_by("label").agg(count=pl.col("text").count()).collect(streaming=True)
  ```

### 3.3 实践
- **任务**：优化千万级数据集查询。
- **代码**：
  ```python
  lazy_df = pl.scan_parquet("large_tweets.parquet").filter(
      pl.col("text").str.contains("AI")
  ).group_by("label").agg(
      count=pl.col("text").count()
  )
  df = lazy_df.collect(streaming=True)
  print(df)
  ```
- **测试**：比较懒惰计算与Pandas性能。

---

## 第4章：集成AI数据管道

### 4.1 数据预处理
- **示例**：
  ```python
  from transformers import AutoTokenizer

  tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")
  df = pl.read_csv("tweets.csv")
  df_with_tokens = df.with_columns(
      pl.col("text").map_elements(lambda x: len(tokenizer(x)["input_ids"])).alias("token_count")
  )
  ```

### 4.2 工具集成
- **Git**：
  ```bash
  git add .
  git commit -m "Add Polars data pipeline"
  git push origin main
  ```
- **Jira/Obsidian**：跟踪数据处理任务。

### 4.3 实践
- **任务**：为Hugging Face模型预处理数据。
- **测试**：确认数据格式适合模型输入。

---

## 第5章：迷你项目——AI情感分析数据处理

### 5.1 项目目标
构建Polars数据处理管道，包含：
- 加载：Parquet格式情感数据集。
- 处理：清洗、特征提取。
- 部署：Docker+GitHub Actions。

### 5.2 项目结构
```
sentiment-polars/
├── .github/
│   ├── workflows/
│   │   ├── ci.yml
├── data/
│   ├── tweets.parquet
├── src/
│   ├── process.py
├── Dockerfile
├── requirements.txt
```

### 5.3 实现
- **处理脚本**（`src/process.py`）：
  ```python
  import polars as pl
  from transformers import AutoTokenizer

  def process_data(input_file, output_file):
      df = pl.scan_parquet(input_file).filter(
          pl.col("text").is_not_null()
      ).with_columns(
          pl.col("label").cast(pl.Categorical),
          pl.col("text").map_elements(
              lambda x: len(AutoTokenizer.from_pretrained("distilbert-base-uncased")(x)["input_ids"])
          ).alias("token_count")
      ).collect(streaming=True)
      df.write_parquet(output_file)
      return df

  if __name__ == "__main__":
      df = process_data("data/tweets.parquet", "data/processed_tweets.parquet")
      print(df.head())
  ```
- **Dockerfile**：
  ```dockerfile
  FROM python:3.9-slim
  WORKDIR /app
  COPY requirements.txt .
  RUN pip install -r requirements.txt
  COPY . .
  CMD ["python", "src/process.py"]
  ```
- **依赖**（`requirements.txt`）：
  ```
  polars==0.20.0
  transformers==4.35.0
  ```
- **GitHub Actions**（`.github/workflows/ci.yml`）：
  ```yaml
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

### 5.4 测试
- **运行**：
  ```bash
  docker build -t sentiment-polars .
  docker run sentiment-polars
  ```
- **测试**：确认`data/processed_tweets.parquet`生成。

---

## 第6章：优化与进阶

### 6.1 优化
- **分区**：
  ```python
  df.write_partitioned_parquet("data/partitioned_tweets", partition_by="label")
  ```
- **内存管理**：
  ```python
  df = pl.scan_parquet("large_tweets.parquet", low_memory=True)
  ```

### 6.2 进阶
- **Neo4j**：存储关系数据（如你的兴趣）。
- **Spark**：超大规模数据处理。
- **云部署**：GCP BigQuery、AWS S3。

### 6.3 实践
- **任务**：优化数据管道，部署到GCP。
- **测试**：比较优化前后性能。

---

## 资源
- **官方文档**：[Polars](https://pola.rs/docs)、[Hugging Face](https://huggingface.co/docs)
- **教程**：Polars官方教程、Real Python
- **工具**：Jupyter Notebook、VS Code、GitHub、Jira、Obsidian
- **建议**：用`notebooklm.google.com`记录处理流程，结合Obsidian或Jira优化任务管理。