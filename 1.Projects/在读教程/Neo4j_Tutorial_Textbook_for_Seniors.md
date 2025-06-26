# Neo4j教材：面向大四学生的知识图谱与AI应用

## 目标
本教材帮助大四学生掌握**Neo4j**，用于构建知识图谱并应用于RAG和AI推理场景，重点涵盖Cypher查询、图数据库设计和Python集成，结合Hugging Face模型提升检索与生成能力。教材详尽、实用，适合有Python基础的学生，强调复杂关系查询的优势，契合你的AI研究和生产力兴趣（如`ragas_rag_agent_knowledge_graph.cypher`）。

## 前提条件
- **受众**：顶尖大学大四学生，熟悉Python和AI/ML入门。
- **先修知识**：Python、基本SQL、JSON、REST API、图论基础。
- **工具**：Neo4j Desktop、Python 3.9+、neo4j-driver、Jupyter Notebook、VS Code、Git、Docker。
- **时长**：6小时（1.5小时理论+4.5小时实践）。

---

## 第1章：Neo4j与知识图谱简介

### 1.1 为什么选择Neo4j？
- **优点**：
  - **关系查询**：高效处理复杂关系。
  - **知识图谱**：支持语义推理，增强AI。
  - **RAG集成**：提升检索精度。
- **缺点**：
  - 学习曲线：Cypher需适应。
  - 非结构化数据处理较弱。
- **适用场景**：RAG、推荐系统、语义搜索。
- **反直觉洞察**：图数据库虽复杂，但对关系密集型任务比传统数据库更直观。

### 1.2 安装与初始化
- **安装**：
  - 下载Neo4j Desktop，设置数据库。
  - Python driver：
    ```bash
    pip install neo4j
    ```
- **示例**：
  ```cypher
  CREATE (p:Person {name: "Alice"})-[:KNOWS]->(q:Person {name: "Bob"})
  ```
- **实践**：创建简单图，查询节点。

---

## 第2章：Cypher查询语言

### 2.1 基础查询
- **示例**：
  ```cypher
  MATCH (p:Person)
  WHERE p.name = "Alice"
  RETURN p.name, p.age
  ```

### 2.2 路径查询
- **示例**：
  ```cypher
  MATCH path = (p:Person)-[:KNOWS*1..2]->(q:Person)
  WHERE p.name = "Alice"
  RETURN path
  ```

### 2.3 实践
- **任务**：查询情感分析知识图谱。
- **代码**：
  ```cypher
  MATCH (t:Tweet)-[:HAS_SENTIMENT]->(s:Sentiment)
  WHERE t.text CONTAINS "AI"
  RETURN t.text, s.label
  ```
- **测试**：确认返回相关Tweet和Sentiment。

---

## 第3章：图数据库设计

### 3.1 建模
- **示例**：
  ```cypher
  CREATE (t:Tweet {text: "I love AI!", id: "1"})
  CREATE (s:Sentiment {label: "POSITIVE"})
  CREATE (t)-[:HAS_SENTIMENT]->(s)
  ```

### 3.2 优化
- **索引**：
  ```cypher
  CREATE INDEX ON :Tweet(id)
  ```

### 3.3 实践
- **任务**：设计情感分析知识图谱。
- **代码**：
  ```python
  from neo4j import GraphDatabase

  class KnowledgeGraph:
      def __init__(self, uri, user, password):
          self.driver = GraphDatabase.driver(uri, auth=(user, password))

      def close(self):
          self.driver.close()

      def create_tweet(self, tweet_id, text, sentiment):
          with self.driver.session() as session:
              session.run(
                  "CREATE (t:Tweet {id: $id, text: $text}) "
                  "CREATE (s:Sentiment {label: $sentiment}) "
                  "CREATE (t)-[:HAS_SENTIMENT]->(s)",
                  id=tweet_id, text=text, sentiment=sentiment
              )

  kg = KnowledgeGraph("bolt://localhost:7687", "neo4j", "password")
  kg.create_tweet("1", "I love AI!", "POSITIVE")
  kg.close()
  ```
- **测试**：确认图谱创建。

---

## 第4章：集成RAG与AI管道

### 4.1 RAG架构
- **示例**：
  ```python
  from neo4j import GraphDatabase
  from transformers import pipeline

  class RAGPipeline:
      def __init__(self, uri, user, password, model_name):
          self.driver = GraphDatabase.driver(uri, auth=(user, password))
          self.generator = pipeline("text-generation", model=model_name)

      def query_graph(self, keyword):
          with self.driver.session() as session:
              result = session.run(
                  "MATCH (t:Tweet)-[:HAS_SENTIMENT]->(s:Sentiment) "
                  "WHERE t.text CONTAINS $keyword "
                  "RETURN t.text, s.label",
                  keyword=keyword
              )
              return [(record["t.text"], record["s.label"]) for record in result]

      def generate_answer(self, query, context):
          prompt = f"Query: {query}\nContext: {context}\nAnswer:"
          return self.generator(prompt, max_length=50)[0]["generated_text"]

  rag = RAGPipeline("bolt://localhost:7687", "neo4j", "password", "distilgpt2")
  context = rag.query_graph("AI")
  answer = rag.generate_answer("What is the sentiment about AI?", str(context))
  print(answer)
  ```

### 4.2 工具集成
- **Git**：
  ```bash
  git add .
  git commit -m "Add Neo4j RAG pipeline"
  git push origin main
  ```

### 4.3 实践
- **任务**：为RAG查询知识图谱。
- **测试**：确认生成回答准确。

---

## 第5章：迷你项目——情感分析知识图谱与RAG

### 5.1 项目目标
构建Neo4j知识图谱与RAG应用，包含：
- 图谱：情感分析Tweet与Sentiment。
- 查询：Cypher检索相关实体。
- 集成：Hugging Face生成回答。

### 5.2 项目结构
```
sentiment-neo4j/
├── .github/
│   ├── workflows/
│   │   ├── ci.yml
├── src/
│   ├── rag.py
├── data/
│   ├── tweets.csv
├── Dockerfile
├── requirements.txt
```

### 5.3 实现
- **RAG脚本**（`src/rag.py`）：
  ```python
  from neo4j import GraphDatabase
  from transformers import pipeline
  import polars as pl

  class SentimentGraph:
      def __init__(self, uri, user, password):
          self.driver = GraphDatabase.driver(uri, auth=(user, password))

      def close(self):
          self.driver.close()

      def load_data(self, csv_file):
          df = pl.read_csv(csv_file)
          with self.driver.session() as session:
              for record in df.iter_rows(named=True):
                  session.run(
                      "CREATE (t:Tweet {id: $id, text: $text}) "
                      "CREATE (s:Sentiment {label: $label}) "
                      "CREATE (t)-[:HAS_SENTIMENT]->(s)",
                      id=record["id"], text=record["text"], label=record["label"]
                  )

      def query_graph(self, keyword):
          with self.driver.session() as session:
              result = session.run(
                  "MATCH (t:Tweet)-[:HAS_SENTIMENT]->(s:Sentiment) "
                  "WHERE t.text CONTAINS $keyword "
                  "RETURN t.text, s.label",
                  keyword=keyword
              )
              return [(record["t.text"], record["s.label"]) for record in result]

  class RAGPipeline:
      def __init__(self, graph, model_name):
          self.graph = graph
          self.generator = pipeline("text-generation", model=model_name)

      def run(self, query, keyword):
          context = self.graph.query_graph(keyword)
          prompt = f"Query: {query}\nContext: {context}\nAnswer:"
          return self.generator(prompt, max_length=50)[0]["generated_text"]

  if __name__ == "__main__":
      graph = SentimentGraph("bolt://localhost:7687", "neo4j", "password")
      graph.load_data("data/tweets.csv")
      rag = RAGPipeline(graph, "distilgpt2")
      answer = rag.run("What is the sentiment about AI?", "AI")
      print(answer)
      graph.close()
  ```
- **Dockerfile**：
  ```dockerfile
  FROM python:3.9-slim
  WORKDIR /app
  COPY requirements.txt .
  RUN pip install -r requirements.txt
  COPY . .
  CMD ["python", "src/rag.py"]
  ```
- **依赖**（`requirements.txt`）：
  ```
  neo4j==5.12.0
  transformers==4.35.0
  polars==0.20.0
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
      - name: Run RAG pipeline
        run: python src/rag.py
      - name: Build Docker image
        run: docker build -t ghcr.io/coleam00/sentiment-neo4j:latest .
      - name: Push to GitHub Packages
        run: |
          echo ${{ secrets.GITHUB_TOKEN }} | docker login ghcr.io -u ${{ github.actor }} --password-stdin
          docker push ghcr.io/coleam00/sentiment-neo4j:latest
  ```

### 5.4 测试
- **运行**：
  ```bash
  docker build -t sentiment-neo4j .
  docker run sentiment-neo4j
  ```
- **测试**：确认RAG生成回答。

---

## 第6章：优化与进阶

### 6.1 优化
- **索引**：
  ```cypher
  CREATE INDEX ON :Tweet(text)
  ```
- **查询计划**：
  ```cypher
  EXPLAIN MATCH (t:Tweet)-[:HAS_SENTIMENT]->(s:Sentiment)
  WHERE t.text CONTAINS "AI"
  RETURN t.text, s.label
  ```

### 6.2 进阶
- **LangChain**：集成Neo4j与LLM。
- **GDS**：图算法分析。
- **Neo4j Aura**：云部署。

### 6.3 Practice
- **任务**：优化Cypher查询，部署到Neo4j Aura.
- **测试**：比较优化前后性能。

---

## 资源
- **官方文档**：[Neo4j](https://neo4j.com/docs/)、[Cypher](https://neo4j.com/docs/cypher-manual/)
- **教程**：Neo4j Sandbox、Graph Academy
- **工具**：Neo4j Desktop、Jupyter Notebook、VS Code、GitHub、Jira、Obsidian
- **建议**：用`notebooklm.google.com`记录图谱设计，结合Obsidian或Jira优化任务管理。