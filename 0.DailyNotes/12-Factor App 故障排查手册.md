# 12-Factor App 故障排查手册
> 🚨 **生产环境救火指南** - 快速定位违反12-Factor原则导致的问题
> 
> ⏰ **使用场景**：线上故障、用户投诉、监控告警、系统异常

---

## 🆘 紧急故障分类索引

| 故障类型 | 常见症状 | 可能原因 | 跳转章节 |
|----------|----------|----------|----------|
| **应用无法启动** | 容器启动失败、依赖错误 | 违反要素2/3 | [§1 启动故障](#1-应用启动故障) |
| **用户数据丢失** | 用户登出、购物车清空 | 违反要素6 | [§2 状态故障](#2-状态管理故障) |
| **环境差异故障** | 开发正常生产报错 | 违反要素10/2 | [§3 环境故障](#3-环境一致性故障) |
| **性能突然下降** | 响应慢、超时 | 违反要素8/9 | [§4 性能故障](#4-性能与并发故障) |
| **配置泄露事件** | 密钥暴露、安全漏洞 | 违反要素3 | [§5 安全故障](#5-安全配置故障) |
| **扩容失败** | 水平扩展不生效 | 违反要素6/8 | [§6 扩展故障](#6-扩展性故障) |

---

## 1️⃣ 应用启动故障

### 🔥 故障现象
```bash
# Docker 容器启动失败
docker: Error response from daemon: failed to create shim
Container exited with code 1

# K8s Pod 状态异常
NAME      READY   STATUS             RESTARTS   AGE
myapp-0   0/1     ImagePullBackOff   0          2m
myapp-1   0/1     CrashLoopBackOff   3          5m
```

### 🔍 排查步骤

#### Step 1: 检查依赖问题（要素2）
```bash
# 检查是否违反依赖隔离原则
docker logs <container_id> | grep -E "(ModuleNotFoundError|ImportError|No module)"

# 常见错误信息
ModuleNotFoundError: No module named 'requests'
ImportError: cannot import name 'Flask' from 'flask'
```

**解决方案**：
```bash
# 确保依赖文件完整
[ -f "requirements.txt" ] || echo "❌ 缺少依赖声明文件"

# 构建时安装依赖
RUN pip install --no-cache-dir -r requirements.txt

# 验证依赖安装
RUN pip freeze > installed_packages.txt
```

#### Step 2: 检查配置问题（要素3）
```bash
# 检查环境变量是否缺失
docker logs <container_id> | grep -E "(KeyError|environment|config|setting)"

# 常见错误信息
KeyError: 'DATABASE_URL'
Config Error: Missing required environment variable
```

**解决方案**：
```yaml
# K8s 配置示例
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
data:
  DATABASE_URL: "postgresql://user:pass@db:5432/myapp"
  REDIS_URL: "redis://redis:6379"

# 应用中读取配置
import os
DATABASE_URL = os.environ.get('DATABASE_URL')
if not DATABASE_URL:
    raise Exception("DATABASE_URL environment variable required")
```

#### Step 3: 检查端口绑定问题（要素7）
```bash
# 检查端口冲突
netstat -tulpn | grep :<port>
lsof -i :<port>

# 常见错误信息  
bind: address already in use
Permission denied (port < 1024)
```

**解决方案**：
```python
# 正确的端口绑定方式
import os
port = int(os.environ.get("PORT", 8000))
app.run(host="0.0.0.0", port=port)  # 绑定所有接口
```

### ⚡ 快速修复检查单
- [ ] 检查 `requirements.txt` 是否存在且完整
- [ ] 验证环境变量是否正确注入  
- [ ] 确认端口绑定到 `0.0.0.0` 而非 `127.0.0.1`
- [ ] 检查容器健康检查是否通过

---

## 2️⃣ 状态管理故障

### 🔥 故障现象
```bash
# 用户投诉
"刚才还在购物车的商品突然没了"
"登录状态莫名其妙丢失"
"上传的文件找不到了"

# 监控指标
Session timeout rate: 85%↑
File not found errors: 200%↑  
User re-login frequency: 300%↑
```

### 🔍 排查步骤

#### Step 1: 检查状态存储位置（要素6）
```bash
# 检查应用代码中是否有内存状态存储
grep -r "session\s*=" src/
grep -r "user_data\s*\[\]" src/  
grep -r "upload.*tmp" src/

# 危险代码示例
user_sessions = {}  # ❌ 内存存储
uploaded_files = []  # ❌ 进程内状态
```

**根本原因**：违反要素6（无状态进程），状态存储在进程内存中

**解决方案**：
```python
# ❌ 错误做法 - 内存存储
class SessionManager:
    def __init__(self):
        self.sessions = {}  # 进程重启数据丢失

# ✅ 正确做法 - 外部存储  
import redis
class SessionManager:
    def __init__(self):
        self.redis = redis.Redis(
            host=os.environ.get('REDIS_URL', 'localhost'),
            port=6379
        )
    
    def store_session(self, user_id, data):
        self.redis.setex(f"session:{user_id}", 3600, json.dumps(data))
```

#### Step 2: 检查文件存储位置
```bash
# 检查文件是否存储在本地磁盘
find . -name "uploads" -type d
grep -r "/tmp\|/var" src/

# 检查容器重启后文件丢失
docker exec <container> ls -la /app/uploads/
```

**解决方案**：
```python
# ✅ 使用对象存储
import boto3
s3 = boto3.client('s3')

def upload_file(file_data, filename):
    bucket_name = os.environ.get('S3_BUCKET')
    s3.put_object(
        Bucket=bucket_name,
        Key=filename,
        Body=file_data
    )
    return f"https://{bucket_name}.s3.amazonaws.com/{filename}"
```

### ⚡ 快速修复检查单
- [ ] 会话数据迁移到 Redis/数据库
- [ ] 文件上传迁移到对象存储（S3/MinIO）  
- [ ] 移除所有进程内状态变量
- [ ] 验证多实例运行无数据冲突

---

## 3️⃣ 环境一致性故障

### 🔥 故障现象
```bash
# 开发人员常见抱怨
"在我本地明明是好的！"
"测试环境通过，生产环境报错"
"代码没变，突然就不能用了"

# 具体错误信息
sqlite3.OperationalError: no such table  # 开发用SQLite，生产用PostgreSQL
redis.exceptions.ConnectionError         # 开发无Redis，生产有Redis
SSL certificate verify failed           # 开发HTTP，生产HTTPS
```

### 🔍 排查步骤

#### Step 1: 检查数据库差异（要素10）
```bash
# 检查不同环境使用的数据库
grep -r "sqlite\|mysql\|postgresql" config/
env | grep -i database

# 常见问题
DATABASE_URL_DEV=sqlite:///./dev.db     # ❌ 开发用SQLite
DATABASE_URL_PROD=postgresql://...      # ❌ 生产用PostgreSQL
```

**根本原因**：违反要素10（环境一致性），开发/生产使用不同数据库

**解决方案**：
```yaml
# docker-compose.yml - 开发环境使用相同数据库
version: '3.8'
services:
  database:
    image: postgres:15  # 与生产环境相同版本
    environment:
      POSTGRES_DB: myapp_dev
      POSTGRES_USER: developer
      POSTGRES_PASSWORD: dev_password
  
  app:
    build: .
    environment:
      DATABASE_URL: postgresql://developer:dev_password@database:5432/myapp_dev
```

#### Step 2: 检查依赖版本差异（要素2）
```bash
# 检查版本锁定文件
[ -f "requirements.txt" ] && cat requirements.txt | grep "=="
[ -f "package-lock.json" ] && echo "Node依赖已锁定"

# 检查是否有版本范围
grep -E "\^|\~|\*|>=|<=" requirements.txt
```

**解决方案**：
```bash
# 生成精确版本依赖
pip freeze > requirements.txt

# requirements.txt 示例
Flask==2.3.3        # ✅ 精确版本
SQLAlchemy==2.0.21  # ✅ 精确版本
# 而不是
Flask>=2.0.0        # ❌ 版本范围
```

#### Step 3: 检查环境配置差异（要素3）
```bash
# 对比不同环境的环境变量
env | sort > prod_env.txt  
# 在开发环境运行
env | sort > dev_env.txt
diff dev_env.txt prod_env.txt
```

### ⚡ 快速修复检查单
- [ ] 开发/生产使用相同数据库类型和版本
- [ ] 依赖版本精确锁定（无 `^` `~` `*`）  
- [ ] 使用 Docker 统一运行时环境
- [ ] 环境变量配置文档化和版本控制

---

## 4️⃣ 性能与并发故障

### 🔥 故障现象
```bash
# 性能监控异常
Response time: 2000ms → 15000ms
Error rate: 0.1% → 25%  
CPU usage: 95%+
Memory usage: 90%+

# 用户投诉
"网站突然变得很卡"  
"提交表单转圈很久"
"经常显示服务不可用"
```

### 🔍 排查步骤

#### Step 1: 检查进程模型（要素8）
```bash
# 检查是否正确分离Web和Worker进程
ps aux | grep -E "(gunicorn|celery|worker)"
htop | grep python

# 错误的进程模型
python app.py  # ❌ 单进程处理所有请求
```

**根本原因**：违反要素8（并发），使用单进程处理高并发请求

**解决方案**：
```bash
# ✅ 正确的进程模型
# Web进程 - 处理HTTP请求
gunicorn app:app --workers 4 --bind 0.0.0.0:8000

# Worker进程 - 处理后台任务  
celery -A app.celery worker --loglevel=info

# 队列进程 - 任务调度
celery -A app.celery beat --loglevel=info
```

#### Step 2: 检查水平扩展配置（要素6+8）
```bash
# K8s 检查副本数和资源限制
kubectl get pods -l app=myapp
kubectl describe hpa myapp-hpa

# 检查负载均衡配置
kubectl get svc myapp-service -o yaml
```

**解决方案**：
```yaml
# 水平自动扩展配置
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler  
metadata:
  name: myapp-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: myapp
  minReplicas: 3
  maxReplicas: 20
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70
```

#### Step 3: 检查优雅关闭（要素9）
```bash
# 模拟生产环境重启
kill -TERM <pid>

# 检查是否优雅关闭
tail -f /var/log/app.log | grep -i "shutdown\|sigterm"
```

**解决方案**：
```python
# ✅ 实现优雅关闭
import signal
import sys

def graceful_shutdown(signum, frame):
    print("Received SIGTERM, shutting down gracefully...")
    # 1. 停止接受新请求
    server.stop_accepting_requests()
    # 2. 完成当前请求  
    server.finish_pending_requests()
    # 3. 关闭数据库连接
    db.close()
    print("Shutdown complete")
    sys.exit(0)

signal.signal(signal.SIGTERM, graceful_shutdown)
```

### ⚡ 快速修复检查单
- [ ] 启用水平扩展（HPA）
- [ ] 分离 Web 和 Worker 进程
- [ ] 实现优雅关闭机制
- [ ] 配置健康检查和就绪检查

---

## 5️⃣ 安全配置故障

### 🔥 故障现象
```bash
# 安全扫描告警
"API key exposed in GitHub repository"
"Database credentials found in source code"
"Secret keys committed to version control"

# 实际安全事件
401 Unauthorized → 突然变成 200 OK
数据库被删库跑路
API 被恶意调用产生巨额费用
```

### 🔍 排查步骤

#### Step 1: 检查硬编码配置（要素3）
```bash
# 扫描代码中的敏感信息
grep -r -i "password\|secret\|key\|token" src/
grep -r -E "[0-9a-f]{32}" src/  # API密钥模式
grep -r -E "AKIA[0-9A-Z]{16}" src/  # AWS密钥模式

# 检查是否有配置文件被提交
find . -name "*.env" -not -path "./.env.example"
git log --all --grep="password\|secret"
```

**根本原因**：违反要素3（配置分离），敏感信息硬编码在代码中

**紧急处理**：
```bash
# 1. 立即轮换泄露的密钥
aws iam delete-access-key --access-key-id AKIA...

# 2. 从Git历史中移除敏感信息
git filter-branch --force --index-filter \
  'git rm --cached --ignore-unmatch config/secrets.py' \
  --prune-empty --tag-name-filter cat -- --all

# 3. 强制推送清理后的历史
git push origin --force --all
```

**长期解决方案**：
```python
# ✅ 正确的配置管理
import os
from typing import Optional

class Config:
    DATABASE_URL: str = os.environ.get('DATABASE_URL')
    API_SECRET: Optional[str] = os.environ.get('API_SECRET')
    
    def __post_init__(self):
        if not self.DATABASE_URL:
            raise ValueError("DATABASE_URL environment variable required")
        if not self.API_SECRET:
            raise ValueError("API_SECRET environment variable required")
```

#### Step 2: 检查权限配置
```bash
# 检查容器是否以root用户运行
docker exec <container> whoami
ps -eo pid,user,cmd | grep python

# 检查文件权限
ls -la config/
stat secrets.yaml
```

**解决方案**：
```dockerfile
# ✅ 使用非root用户
FROM python:3.11-slim
RUN useradd --create-home --shell /bin/bash appuser
USER appuser
WORKDIR /home/appuser/app
```

### ⚡ 快速修复检查单
- [ ] 扫描并移除所有硬编码敏感信息
- [ ] 轮换所有可能泄露的密钥
- [ ] 配置密钥管理服务（Vault/AWS Secrets Manager）
- [ ] 容器使用非root用户运行

---

## 6️⃣ 扩展性故障

### 🔥 故障现象
```bash
# 扩容不生效
kubectl scale deployment myapp --replicas=10
# 但负载仍然集中在少数实例上

# 数据不一致
用户A看到的数据 ≠ 用户B看到的数据
缓存数据过期不同步
```

### 🔍 排查步骤

#### Step 1: 检查状态共享（要素6）
```bash
# 检查实例间是否有状态依赖
curl http://instance1/api/user/123
curl http://instance2/api/user/123  
# 返回结果应该一致

# 检查会话亲和性配置
kubectl get svc myapp -o yaml | grep -i "sessionAffinity"
```

**解决方案**：
```yaml
# 移除会话亲和性，实现真正的无状态
apiVersion: v1
kind: Service
spec:
  sessionAffinity: None  # 不要设置为 ClientIP
  ports:
  - port: 80
    targetPort: 8000
```

#### Step 2: 检查负载均衡配置
```bash
# 检查负载均衡算法
kubectl describe ingress myapp-ingress
kubectl get endpoints myapp

# 测试负载分布
for i in {1..10}; do
  curl -s http://myapp.example.com/api/health | grep hostname
done
```

### ⚡ 快速修复检查单
- [ ] 移除所有会话亲和性配置  
- [ ] 验证多实例数据一致性
- [ ] 配置合适的负载均衡算法
- [ ] 实现分布式缓存同步

---

## 🚨 紧急响应流程

### ⚡ 5分钟内必须完成
1. **确认故障范围**：影响多少用户？哪些功能？
2. **检查监控指标**：CPU/内存/网络/错误率
3. **查看最近变更**：最近30分钟有什么部署？
4. **决策回滚**：如果是新部署导致，立即回滚

```bash
# 快速回滚命令
kubectl rollout undo deployment/myapp
docker-compose down && docker-compose up -d --scale app=3
```

### ⏰ 30分钟内修复目标
1. **根因分析**：使用本手册定位具体违反的12-Factor原则
2. **应用热修复**：不重启的情况下修复配置问题
3. **验证修复效果**：确认用户可正常使用
4. **通知相关方**：更新状态页面，通知用户

### 📋 事后复盘必做项
- [ ] 记录故障时间线和修复步骤
- [ ] 分析根因违反了哪些12-Factor原则  
- [ ] 制定预防措施避免同类问题
- [ ] 更新监控和告警规则
- [ ] 团队分享故障经验教训

---

## 📞 紧急联系方式

| 角色 | 姓名 | 电话 | 钉钉/微信 | 主要负责 |
|------|------|------|----------|----------|
| **技术负责人** | _________ | _________ | _________ | 技术决策 |
| **运维负责人** | _________ | _________ | _________ | 基础设施 |  
| **产品负责人** | _________ | _________ | _________ | 业务影响 |
| **客服负责人** | _________ | _________ | _________ | 用户沟通 |

> 💡 **记住**：最好的故障排查就是预防故障发生
> 
> 严格遵循12-Factor原则可以避免80%的生产环境问题