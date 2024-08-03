---
aliases: 
theme: 
original: 
url: 
author: 
date created: "{{date:YYYY-MM-DD HH:mm}}" 
date updated:  "{{date:YYYY-MM-DD HH:mm}}" 
type: 
high_priority: false
tags:
---
 Redis支持的主要命令包括:
### String
- SET - 设置一个key-value对
- GET - 获取指定key的值 
- DEL - 删除一个或多个key
- INCR - 计数器增1操作
- DECR - 计数器减1操作
### List
- LPUSH - 在列表左侧插入元素
- RPUSH - 在列表右侧插入元素
- LPOP - 从列表左侧移除第一个元素
- RPOP - 从列表右侧移除第一个元素
### Set
- SADD - 向集合添加一个或多个成员
- SMEMBERS - 返回集合中的所有成员
- SISMEMBER - 判断一个值是否是集合的成员
### Hash
- HSET - 将哈希表字段值设为指定值
- HGET - 返回哈希表中给定字段的值 
- HDEL - 删除哈希表中一个或多个指定的字段
### Sorted Set
- ZADD - 向有序集合添加一个或多个成员
- ZRANGE - 返回有序集合中指定区间内的成员
此外还有:
- KEYS - 查找所有匹配给定模式的键
- EXISTS - 检查给定键是否存在
- EXPIRE - 设置键的过期时间
等多种命令类型。它们涵盖了Redis的各种数据结构操作。