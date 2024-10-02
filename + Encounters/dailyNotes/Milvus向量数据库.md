---
aliases: 
theme: 
high_priority: false
tags:
---
你提供的代码片段展示了如何使用 `Milvus` 作为向量数据库，并配置它以连接到 Milvus 服务器。这段代码使用了 `HuggingFaceEmbeddings` 作为嵌入函数，并设置了连接参数，包括 URI、用户名、密码和安全连接标志。

### 代码解释

1. **导入必要的库**：
   确保你已经安装了所需的库，例如 `pymilvus` 和 `sentence_transformers`（用于 `HuggingFaceEmbeddings`）。

   ```bash
   pip install pymilvus sentence-transformers
   ```

2. **定义 `Milvus` 实例**：
   你创建了一个 `Milvus` 实例，并传递了以下参数：

   - `collection_name`: 集合的名称。
   - `embedding_function`: 用于生成向量嵌入的函数。
   - `connection_args`: 连接到 Milvus 服务器的参数。

```python
from pymilvus import connections, FieldSchema, CollectionSchema, DataType, Collection
from sentence_transformers import SentenceTransformer
import os

# 定义 HuggingFace 嵌入函数
class HuggingFaceEmbeddings:
    def __init__(self, model_name):
        self.model = SentenceTransformer(model_name)

    def __call__(self, sentences):
        return self.model.encode(sentences, convert_to_tensor=True).tolist()

# 创建 Milvus 实例
vector_db = Milvus(
    collection_name="OfficeHoursDemoCollection",
    embedding_function=HuggingFaceEmbeddings(model_name="multi-qa-MiniLM-L6-cos-v1"),
    connection_args={
        "uri": os.getenv("MILVUS_URI"),
        "user": os.getenv("MILVUS_USER"),
        "password": os.getenv("MILVUS_PASSWORD"),
        "secure": True,
    },
)
```

### 详细步骤

1. **设置环境变量**：
   确保你在运行脚本之前设置了以下环境变量：

   ```bash
   export MILVUS_URI=https://your-milvus-uri
   export MILVUS_USER=your-milvus-user
   export MILVUS_PASSWORD=your-milvus-password
   ```

2. **定义 HuggingFace 嵌入函数**：
   使用 `SentenceTransformer` 模型来生成句子嵌入。

3. **创建 Milvus 实例**：
   使用 `Milvus` 类创建一个实例，并传入集合名称、嵌入函数和连接参数。

### 示例代码

以下是一个完整的示例代码，展示了如何设置和使用 `Milvus` 向量数据库：

```python
from pymilvus import connections, FieldSchema, CollectionSchema, DataType, Collection
from sentence_transformers import SentenceTransformer
import os

# 定义 HuggingFace 嵌入函数
class HuggingFaceEmbeddings:
    def __init__(self, model_name):
        self.model = SentenceTransformer(model_name)

    def __call__(self, sentences):
        return self.model.encode(sentences, convert_to_tensor=True).tolist()

# 连接到 Milvus 服务器
connections.connect(
    alias="default",
    uri=os.getenv("MILVUS_URI"),
    user=os.getenv("MILVUS_USER"),
    password=os.getenv("MILVUS_PASSWORD"),
    secure=True
)

# 定义集合模式
fields = [
    FieldSchema(name="id", dtype=DataType.INT64, is_primary=True, auto_id=True),
    FieldSchema(name="embedding", dtype=DataType.FLOAT_VECTOR, dim=384)  # 根据模型调整维度
]
schema = CollectionSchema(fields, "Office Hours Demo Collection")

# 创建集合
collection = Collection(name="OfficeHoursDemoCollection", schema=schema)

# 定义嵌入函数
embedding_function = HuggingFaceEmbeddings(model_name="multi-qa-MiniLM-L6-cos-v1")

# 插入数据
sentences = ["This is a test sentence.", "Another test sentence."]
embeddings = embedding_function(sentences)

# 插入向量
data = [embeddings]
collection.insert(data)

# 加载集合
collection.load()

# 查询
search_params = {"metric_type": "L2", "params": {"nprobe": 10}}
results = collection.search(
    data=[embeddings[0]],
    anns_field="embedding",
    param=search_params,
    limit=5
)

for result in results:
    print(result)

# 断开连接
connections.disconnect("default")
```

### 注意事项

1. **模型维度**：
   确保 `dim` 参数与你的嵌入模型输出的向量维度一致。例如，`multi-qa-MiniLM-L6-cos-v1` 模型的输出维度是 384。

2. **安全性**：
   如果你使用的是 HTTPS 连接，请确保 `secure` 参数设置为 `True`。

3. **环境变量**：
   确保在运行脚本之前正确设置了所有需要的环境变量。

通过以上步骤，你应该能够成功地连接到 Milvus 服务器并使用 HuggingFace 的嵌入模型进行向量存储和查询。