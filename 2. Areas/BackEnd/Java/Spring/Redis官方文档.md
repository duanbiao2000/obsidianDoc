好的，以下是 Redis 在不同场景下的常用命令及其解释：

**1. 缓存场景**

|   |   |   |   |   |
|---|---|---|---|---|
|**场景**|**命令**|**用途**|**主要参数**|**示例用法**|
|缓存|`SET`|设置指定键的值|key, value, [EX seconds\|PX milliseconds] [NX\|
|缓存|`GET`|获取指定键的值|key|`GET mykey`|
|缓存|`DEL`|删除指定键|key|`DEL mykey`|
|缓存|`EXPIRE`|设置键的过期时间|key, seconds|`EXPIRE mykey 60`|
|缓存|`TTL`|获取键的剩余过期时间|key|`TTL mykey`|
|缓存|`MGET`|获取多个指定键的值|key [key ...]|`MGET key1 key2 key3`|
|缓存|`MSET`|同时设置多个键值对|key value [key value ...]|`MSET key1 "value1" key2 "value2"`|

**2. 消息队列场景**

|   |   |   |   |   |
|---|---|---|---|---|
|**场景**|**命令**|**用途**|**主要参数**|**示例用法**|
|消息队列|`LPUSH`|向列表左侧推入元素|key, value [value ...]|`LPUSH mylist "value1"`|
|消息队列|`RPUSH`|向列表右侧推入元素|key, value [value ...]|`RPUSH mylist "value2"`|
|消息队列|`LPOP`|移除并返回列表左侧的元素|key|`LPOP mylist`|
|消息队列|`RPOP`|移除并返回列表右侧的元素|key|`RPOP mylist`|
|消息队列|`BLPOP`|移除并返回列表左侧的元素（阻塞）|key [key ...], timeout|`BLPOP mylist 10` (阻塞等待 10 秒)|
|消息队列|`BRPOP`|移除并返回列表右侧的元素（阻塞）|key [key ...], timeout|`BRPOP mylist 10`|
|消息队列|`PUBLISH`|将消息发送到指定的频道|channel, message|`PUBLISH mychannel "Hello"`|
|消息队列|`SUBSCRIBE`|订阅一个或多个频道|channel [channel ...]|`SUBSCRIBE mychannel`|
|消息队列|`PSUBSCRIBE`|订阅符合给定模式的频道|pattern [pattern ...]|`PSUBSCRIBE news.*`|

**3. 实时数据分析场景**

|   |   |   |   |   |
|---|---|---|---|---|
|**场景**|**命令**|**用途**|**主要参数**|**示例用法**|
|实时数据分析|`INCR`|将键存储的值加 1|key|`INCR page_views`|
|实时数据分析|`DECR`|将键存储的值减 1|key|`DECR remaining_seats`|
|实时数据分析|`HINCRBY`|将哈希表中指定字段的值增加给定数值|key, field, increment|`HINCRBY user:1001 points 10`|
|实时数据分析|`ZADD`|向有序集合添加成员|key, score, member [score member ...]|`ZADD leaderboard 100 "user1"`|
|实时数据分析|`ZRANGE`|返回有序集合中指定区间内的成员|key, start, stop [WITHSCORES]|`ZRANGE leaderboard 0 9 WITHSCORES`|
|实时数据分析|`ZREVRANGE`|返回有序集合中指定区间内的成员（按分值降序排列）|key, start, stop [WITHSCORES]|`ZREVRANGE leaderboard 0 9 WITHSCORES`|
|实时数据分析|`ZSCORE`|返回有序集合中指定成员的分值|key, member|`ZSCORE leaderboard "user1"`|
|实时数据分析|`SADD`|向集合添加一个或多个成员|key, member [member ...]|`SADD online_users "user1"`|
|实时数据分析|`SMEMBERS`|返回集合中的所有成员|key|`SMEMBERS online_users`|

**4. 分布式锁场景**

|   |   |   |   |   |
|---|---|---|---|---|
|**场景**|**命令**|**用途**|**主要参数**|**示例用法**|
|分布式锁|`SETNX`|当键不存在时，设置键的值|key, value|`SETNX lock:resource "locked"`|
|分布式锁|`SET`|设置键的值，并设置过期时间|key, value, NX, EX seconds|`SET lock:resource "locked" NX EX 10`|
|分布式锁|`DEL`|删除键|key|`DEL lock:resource`|
|分布式锁|`EXPIRE`|设置键的过期时间|key, seconds|`EXPIRE lock:resource 10`|
|分布式锁|`TTL`|获取键的剩余过期时间|key|`TTL lock:resource`|

**总结**

- **缓存场景**：主要使用键值对操作，如 `SET`、`GET`、`DEL` 等，以及设置过期时间的命令 `EXPIRE` 和 `TTL`。
- **消息队列场景**：使用列表操作，如 `LPUSH`、`RPUSH`、`LPOP`、`RPOP`，以及阻塞操作 `BLPOP` 和 `BRPOP`，还有发布订阅模式的命令 `PUBLISH`、`SUBSCRIBE` 和 `PSUBSCRIBE`。
- **实时数据分析场景**：主要使用计数器操作，如 `INCR`、`DECR`、`HINCRBY`，以及有序集合操作，如 `ZADD`、`ZRANGE`、`ZREVRANGE` 和 `ZSCORE`，还有集合操作`SADD`和`SMEMBERS`。
- **分布式锁场景**：使用 `SETNX` 或 `SET` 命令实现互斥，使用 `DEL` 或 `EXPIRE` 命令释放锁。