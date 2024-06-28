

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