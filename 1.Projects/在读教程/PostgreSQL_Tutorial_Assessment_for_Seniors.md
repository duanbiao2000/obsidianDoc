# PostgreSQL教程辅助测试：面向大四学生的AI元数据管理评估

## 目标
评估学生对PostgreSQL核心概念（SQL、索引优化、向量搜索）的掌握情况，以及管理AI元数据的能力。测试结合理论和实践，适合有Python基础的大四学生，强调高效数据存储和查询。

## 测试形式
- **类型**：选择题（10分）、简答题（20分）、编程题（70分）
- **时长**：90分钟
- **评分标准**：正确性（50%）、代码结构（30%）、创新性（20%）

---

## 第1部分：选择题（10分，每题2分）

1. PostgreSQL的主要优势是：  
   A. 内置向量搜索  
   B. 可靠性与JSONB支持  
   C. 自动AI模型训练  
   D. 轻量级部署  
   **答案**：B

2. 以下哪个命令用于创建B树索引？  
   A. `CREATE INDEX idx ON table USING GIN`  
   B. `CREATE INDEX idx ON table (column)`  
   C. `CREATE VECTOR idx ON table`  
   D. `CREATE TABLE idx ON table`  
   **答案**：B

3. JSONB适合存储：  
   A. 固定结构数据  
   B. 非结构化元数据  
   C. 高并发日志  
   D. 时间序列数据  
   **答案**：B

4. pgvector扩展支持的查询类型是：  
   A. 全文搜索  
   B. 余弦相似度  
   C. 图查询  
   D. 空间查询  
   **答案**：B

5. 生产部署PostgreSQL的推荐平台是：  
   A. Streamlit Cloud  
   B. AWS RDS  
   C. Vercel  
   D. Postman  
   **答案**：B

---

## 第2部分：简答题（20分，每题10分）

1. **问题**：解释JSONB和pgvector在AI元数据管理中的区别，并说明适用场景。  
   **参考答案**：  
   - **区别**：JSONB存储非结构化元数据（如模型配置），pgvector存储嵌入向量，支持相似度查询。  
   - **场景**：JSONB适合存储预测元数据（如score、model），pgvector适合语义搜索（如文本相似度）。  
   - **评分点**：清晰对比两者，提及AI场景。

2. **问题**：描述索引优化的作用，并说明如何避免技术债务。  
   **参考答案**：  
   - **作用**：索引（如B树、GIN）加速查询，减少扫描时间。  
   - **技术债务**：避免过多索引（增加写开销），定期分析`EXPLAIN`，规范化表设计。  
   - **评分点**：准确描述索引，提到技术债务管理。

---

## 第3部分：编程题（70分）

### 编程题1：SQL与JSONB（30分）
- **任务**：编写SQL脚本，包含：
  - 创建`predictions`表，包含`text`、`prediction`和`metadata`（JSONB）。
  - 插入3条记录，包含JSONB元数据。
  - 查询特定模型的预测。
- **要求**：
  - 添加GIN索引。
  - 处理查询性能。
- **参考代码**：
  ```sql
  CREATE TABLE predictions (
      id SERIAL PRIMARY KEY,
      text TEXT NOT NULL,
      prediction VARCHAR(50),
      metadata JSONB
  );

  CREATE INDEX idx_metadata_gin ON predictions USING GIN (metadata);

  INSERT INTO predictions (text, prediction, metadata) VALUES
      ('这很好', '正面', '{"model": "DistilBERT", "score": 0.9}'),
      ('不太好', '负面', '{"model": "BERT", "score": 0.7}'),
      ('我爱AI', '正面', '{"model": "DistilBERT", "score": 0.95}');

  SELECT text, prediction, metadata->>'score' AS score
  FROM predictions
  WHERE metadata->>'model' = 'DistilBERT';
  ```
- **评分标准**：
  - 表设计（10分）：正确定义字段。
  - JSONB操作（10分）：插入和查询正常。
  - 索引（5分）：GIN索引正确。
  - 代码结构（5分）：清晰、可读。

### 编程题2：pgvector与AI集成（40分）
- **任务**：构建Python+PostgreSQL应用，包含：
  - 存储Hugging Face嵌入向量到`embeddings`表。
  - 查询与输入文本最相似的5条记录。
- **要求**：
  - 使用`psycopg2`连接。
  - 处理错误（如无效输入）。
- **参考 code**：
  ```python
  import psycopg2
  import numpy as np
  from transformers import AutoTokenizer, AutoModel

  conn = psycopg2.connect(dbname="ai_metadata", user="postgres", password="password")
  cur = conn.cursor()

  tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")
  model = AutoModel.from_pretrained("distilbert-base-uncased")

  def store_embedding(text):
      try:
          inputs = tokenizer(text, return_tensors="pt")
          embedding = model(**inputs).last_hidden_state.mean(dim=1).detach().numpy()[0]
          cur.execute("INSERT INTO embeddings (text, embedding) VALUES (%s, %s)", (text, embedding.tolist()))
          conn.commit()
      except Exception as e:
          print(f"错误：{e}")

  def find_similar(text):
      try:
          inputs = tokenizer(text, return_tensors="pt")
          embedding = model(**inputs).last_hidden_state.mean(dim=1).detach().numpy()[0]
          cur.execute("SELECT text, embedding <=> %s AS distance FROM embeddings ORDER BY distance LIMIT 5",
                      (embedding.tolist(),))
          return cur.fetchall()
      except Exception as e:
          return [(f"错误：{e}", None)]

  # 测试
  store_embedding("我爱AI")
  similar_texts = find_similar("我爱AI")
  print("相似文本：", similar_texts)
  ```
  ```sql
  CREATE EXTENSION vector;
  CREATE TABLE embeddings (
      id SERIAL PRIMARY KEY,
      text TEXT,
      embedding VECTOR(768)
  );
  ```
- **评分标准**：
  - pgvector操作（15分）：向量存储和查询正常。
  - AI集成（10分）：Hugging Face嵌入正确。
  - 错误处理（10分）：处理无效输入。
  - 代码结构（5分）：清晰、注释完善。

---

## 注意事项
- **提交**：提交项目文件夹（包含`app.py`、`init.sql`、`requirements.txt`）。
- **测试环境**：PostgreSQL 15+，Python 3.9+，安装`psycopg2-binary`、`transformers`。
- **建议**：记录SQL查询过程（如你的`notebooklm.google.com`习惯），便于优化数据库设计。

## 评分总结
- **选择题**：考察基础概念。
- **简答题**：测试理论和设计思维。
- **编程题**：评估开发能力，强调向量搜索和AI集成。
- **反直觉洞察**：PostgreSQL的pgvector让传统关系型数据库胜任现代AI任务，但需平衡性能和复杂性。