---
aliases:
date: 2025-12-03 13:14
tags:
source:
update:
rating:
related:
  - "[[高效学习 Python 系统设计]]"
view-count: 5
---
# [[Python 系统设计 6 小时突破方案]]：极简版

## 核心公式
**秒杀 = 削峰 + 异步 + 预减**
**瓶颈 = 库存扣减 (并发写)**
**破局 = Redis (预减) + MQ (解耦) + 限流 (防护)**

---

## 1. 系统设计万能框架 (5步法)

| 步骤 | 核心问题 | 输出 |
|:--- |:--- |:--- |
| **需求澄清** | 做什么？QPS？延迟？一致性？ | 功能 + 性能指标 |
| **能力评估** | 流量/存储/带宽计算 | 瓶颈识别 |
| **架构设计** | 模块划分 + 交互流程 | 架构图 |
| **深度优化** | 瓶颈破局方案 | 技术选型 |
| **扩展讨论** | 故障处理 + 权衡对比 | Trade-off 分析 |

---

## 2. 秒杀系统三大决策

| 决策点 | 问题 | 方案 | 原因 |
|:--- |:--- |:--- |:--- |
| **并发控制** | 10000 QPS 打数据库 | 应用层限流 | DB 只能 1000 QPS |
| **库存扣减** | 并发超卖 | Redis 预减 + 异步确认 | 原子操作 + 秒级响应 |
| **结果通知** | 阻塞用户 | MQ 异步处理 | 解耦 + 削峰 |

---

## 3. 核心架构 (数据流)

```
Client (50000 QPS)
    ↓
[Nginx 限流: 15000 QPS]
    ↓
[Flask × 4] (用户限流 + Redis 预减)
    ↓
[立即返回: "下单成功"] (< 50ms)
    ↓
[RabbitMQ] (异步队列)
    ↓
[订单服务] (消费 MQ + DB 真实扣减)
    ↓
[PostgreSQL] (持久化订单)
```

---

## 4. 关键代码片段

### Redis 预减 (原子操作)
```python
def decr_stock(product_id: int) -> int:
    """返回值 < 0 表示超卖"""
    return redis.decrby(f"stock:{product_id}", 1)

# 使用
remaining = cache.decr_stock(PRODUCT_ID)
if remaining < 0:
    cache.incr_stock(PRODUCT_ID, 1)  # 回滚
    return {"error": "库存不足"}
```

### MQ 发送 (异步解耦)
```python
producer.send_order({
    "order_id": str(uuid.uuid4()),
    "user_id": user_id,
    "product_id": PRODUCT_ID
})
return {"success": True}  # 立即返回
```

### 限流器 (令牌桶)
```python
class TokenBucket:
    def allow_request(self) -> bool:
        now = time.time()
        new_tokens = (now - self.last_refill) * self.refill_rate
        self.tokens = min(self.capacity, self.tokens + new_tokens)
        
        if self.tokens >= 1:
            self.tokens -= 1
            return True
        return False
```

---

## 5. 性能优化路线图

| 方案 | QPS | 延迟 | 复杂度 | 适用场景 |
|:--- |:--- |:--- |:--- |:--- |
| Flask 单机 | 1000 | 300ms | ⭐ | MVP 验证 |
| Flask × 4 + Nginx | 5000 | 150ms | ⭐⭐ | **当前推荐** |
| FastAPI 异步 | 25000 | 50ms | ⭐⭐⭐ | 真实高并发 |
| 本地库存 | 50000 | 20ms | ⭐⭐⭐⭐ | 超大规模 (YAGNI) |

---

## 6. 面试速答模板 (3分钟)

### 开场 (30s)
> "假设 10000 QPS，10秒卖完 100000 件。核心瓶颈是**库存扣减的并发写入**。"

### 方案 (60s)
> "架构分**快速路径**和**异步路径**：
> - 快速路径：Nginx限流 → Flask → Redis预减 → 返回(<50ms)
> - 异步路径：MQ → 订单服务 → DB持久化
> 
> **为什么这样设计？**
> - Redis吞吐量100000+ QPS，DB只有1000 QPS
> - MQ解耦，不阻塞用户
> - 限流防止雪崩"

### 深度 (60s)
> "可能超卖吗？用Redis原子操作理论上不会，但MQ发送失败会丢订单，需要对账补偿。
> 
> 如果QPS升到50000？增加Flask实例或切换FastAPI异步框架。"

### 收尾 (30s)
> "故障处理：Redis主从切换、MQ队列堆积告警、DB读写分离。"

---

## 7. 常见追问破解

### Q1: 为什么不用Kafka？
> "RabbitMQ支持ACK确认，适合实时订单。Kafka是日志系统，吞吐量高但过度设计（YAGNI）。"

### Q2: 同一用户疯狂刷单？
> "多层限流：用户级(10s/5次) → IP级(10s/100次) → 设备指纹 → 验证码（可选）。"

### Q3: Redis挂了？
> "主从切换(< 30s) + 临时降级到本地内存 + 人工对账。"

---

## 8. 实践自检清单

- [ ] 能讲清楚**为什么Redis不是DB**？(吞吐量差异)
- [ ] 能讲清楚**为什么需要MQ**？(异步解耦)
- [ ] 能讲清楚**超卖的3种场景**？(Redis失败/MQ丢失/并发竞争)
- [ ] 能讲清楚**水平扩展的3个方案**？(加实例/异步框架/本地库存)
- [ ] 能画出**数据流架构图**？(限流→预减→MQ→DB)

---

## 黄金法则
**瓶颈定方案，权衡选技术，YAGNI防过度。**

---
**关联笔记：** [[2025-12-07-系统架构分类框架]] | [[2025-12-05-Python学习套件]] | [[2025-12-07-带着答案提问]]