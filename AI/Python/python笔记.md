
---
aliases:

---
20230828 0948
links:
title:
origin:
tags: #flashcards #todo 


当谈到Python语言中的工厂模式时，一个常见的例子是使用工厂函数来创建不同类型的数据库连接对象。
```python
def create_connection(db_type, host, port, username, password):
    if db_type == "mysql":
        return MySQLConnection(host, port, username, password)
    elif db_type == "postgresql":
        return PostgreSQLConnection(host, port, username, password)
    elif db_type == "mongodb":
        return MongoDBConnection(host, port, username, password)
    else:
        raise ValueError("Unsupported database type")
class MySQLConnection:
    def __init__(self, host, port, username, password):
        # Connect to MySQL database
    def execute_query(self, query):
        # Execute MySQL query
class PostgreSQLConnection:
    def __init__(self, host, port, username, password):
        # Connect to PostgreSQL database
    def execute_query(self, query):
        # Execute PostgreSQL query
class MongoDBConnection:
    def __init__(self, host, port, username, password):
        # Connect to MongoDB database
    def execute_query(self, query):
        # Execute MongoDB query
```
在上面的例子中，`create_connection` 函数充当了工厂函数的角色。它接受数据库类型和连接所需的参数，并根据数据库类型返回相应的连接对象。
根据不同的数据库类型，工厂函数创建不同的连接对象，例如 `MySQLConnection`、`PostgreSQLConnection` 和 `MongoDBConnection`。每个连接对象都有自己的具体实现，包括连接到数据库和执行查询的方法。
通过使用工厂模式，客户端代码可以通过调用 `create_connection` 函数来获取适当的数据库连接对象，而不需要直接与底层的连接类进行交互。这种设计模式提供了一种灵活的方式来创建和管理不同类型的对象，并促进了代码的可扩展性和可维护性。




# 跟老齐学Python:从入门到精通

## 6.3标准库 

```xml
<!--22601.xml-->
<bookstore>
    <book category="COOKING">
        <title lang="en">Everyday Italian</title>
        <author>Giada De Laurentiis</author>
        <year>2005</year>
        <price>30.00</price>
    </book>
    <book category="CHILDREN">
        <title lang="en">Harry Potter</title>
        <author>J K. Rowling</author>
        <year>2005</year>
        <price>29.99</price>
    </book>
        <book category="WEB">
        <title lang="en">Learning XML</title>
        <author>Erik T. Ray</author>
        <year>2003</year>
        <price>39.95</price>
    </book>
</bookstore>
```

```python
import xml.etree.ElementTree as ET

tree = ET.ElementTree(file="22601.xml")
print(tree)

root = tree.getroot()
print(root.tag)

for child in root:
    print(child.tag, child.attrib)

print("=" * 26)
for ele in tree.iter(tag="book"):  # 遍历名称为book的节点
    print(ele.tag, ele.attrib)
print("*" * 26)

for ele in tree.iter(tag="title"):  # 遍历名称为title的节点
    print(ele.tag, ele.attrib, ele.text)
```

```bash
C:\Users\Danny\Documents\Mycodes\bootstap\venv\Scripts\python.exe C:\Users\Danny\Documents\Mycodes\bootstap\最新python的web开发全家桶\gx_day13_demo\test.py 
<xml.etree.ElementTree.ElementTree object at 0x0000017CEF11BFD0>
bookstore
book {'category': 'COOKING'}
book {'category': 'CHILDREN'}
book {'category': 'WEB'}
==========================
book {'category': 'COOKING'}
book {'category': 'CHILDREN'}
book {'category': 'WEB'}
**************************
title {'lang': 'en'} Everyday Italian
title {'lang': 'en'} Harry Potter
title {'lang': 'en'} Learning XML

Process finished with exit code 0
```

