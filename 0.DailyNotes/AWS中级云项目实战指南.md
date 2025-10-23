# AWS中级云项目实战指南：构建高价值技术作品集（中高级开发者版）

> **核心价值**：超越基础证书，通过5个真实生产级项目展示架构设计能力、问题解决思维与成本优化意识。本指南聚焦**技术深度**与**实战细节**，帮助中高级开发者快速构建可展示的云项目，直击面试官关注点——“如何用云技术解决实际业务问题”。

---

## 一、通用准备：中高级开发者的AWS环境规范

### 1.1 基础环境配置（必须项）
```bash
# 创建专用IAM用户（避免使用root账户）
aws iam create-user --user-name cloud-dev

# 附加最小权限策略（仅限项目所需服务）
aws iam attach-user-policy --user-name cloud-dev --policy-arn arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess
# ...其他服务策略按需添加

# 配置CLI默认区域（建议us-east-1）
aws configure set default.region us-east-1
```

### 1.2 资源管理黄金法则
- **Tagging规范**：所有资源必须添加`Project`、`Owner`、`Environment`标签
  ```bash
  aws s3api create-bucket --bucket my-project-bucket \
    --tagging 'TagSet=[{Key=Project,Value=EventNotifier},{Key=Owner,Value=JohnDoe}]'
  ```
- **自动清理机制**：
  - 使用CloudWatch Events + Lambda定时清理未标记资源
  - 设置AWS Budgets警报（成本>5美元立即通知）
- **生产级安全基线**：
  - 所有Lambda函数启用`VPC`隔离（即使免费层）
  - API Gateway启用`Usage Plans` + `API Key`验证
  - RDS启用`Encryption at Rest`和`Automated Backups`

> 💡 **中高级开发者注意**：  
> - 免费层资源**必须24小时内清理**（如EC2实例、ALB）  
> - 使用`AWS CloudFormation`或`Terraform`管理基础设施（避免手动操作）  
> - 所有敏感数据通过`AWS Secrets Manager`管理（禁止硬编码）

---

## 二、项目实战：从架构设计到生产部署

### 项目一：事件通知系统（Serverless实时警报）  
**核心价值**：展示无服务器架构设计能力，解决“消息可靠性”与“安全边界”问题  

#### 关键实现步骤（技术深度版）
1. **S3静态网站托管优化**  
   ```bash
   # 启用静态网站托管 + 自动HTTPS（通过CloudFront）
   aws s3api put-bucket-website --bucket my-static-site \
     --website-configuration '{
       "IndexDocument": {"Suffix": "index.html"},
       "ErrorDocument": {"Key": "error.html"}
     }'
   ```
   - **安全加固**：  
     - 关闭公共访问权限（通过Bucket Policy）  
     - 使用CloudFront + WAF过滤恶意请求（`AWS::WAFv2::WebACL`模板）
<!--ID: 1761111103077-->


2. **SNS订阅确认的自动化处理**  
   ```javascript
   // Lambda处理SNS订阅确认（关键代码）
   exports.handler = async (event) => {
     const { TopicArn, Token } = JSON.parse(event.Records[0].Sns.Message);
     await sns.confirmSubscription({ TopicArn, Token }).promise();
   };
   ```
   - **陷阱规避**：  
     - 未确认订阅会导致消息丢失（需在Lambda中显式处理`SubscriptionConfirmation`类型）  
     - 为SNS主题设置`DeliveryPolicy`：重试3次+指数退避

3. **API Gateway生产级配置**  
   ```yaml
   # CloudFormation片段（关键安全设置）
   ApiGateway:
     Type: AWS::ApiGateway::RestApi
     Properties:
       EndpointConfiguration: { Types: [REGIONAL] }
       MinimumCompressionSize: 1024 # 启用Gzip压缩
   ```
   - **必须配置项**：  
     - CORS策略（`Access-Control-Allow-Origin: https://your-domain.com`）  
     - 方法级别`Authorization: AWS_IAM`（避免公开端点）  
     - 集成响应映射（过滤敏感头信息）

#### 成本优化技巧
| 资源类型       | 免费层限制      | 生产级优化方案                     |
|----------------|----------------|-----------------------------------|
| Lambda         | 1M请求/月      | 设置`Reserved Concurrency=1`防止突发流量超支 |
| SNS            | 1M消息/月      | 使用`Message Attributes`过滤无效订阅   |
| CloudFront     | 50GB流量/月    | 启用`Cache-Control: max-age=31536000` |

> ✅ **简历亮点话术**：  
> *“设计高可靠事件通知系统，通过SNS+Lambda实现99.95%消息投递率，采用CloudFront+WAF降低70%恶意请求成本”*

---

### 项目二：CSV数据管道（自动化ETL与可视化）  
**核心价值**：展示数据工程能力，解决“数据质量”与“处理效率”问题  

#### 关键实现步骤（技术深度版）
1. **Glue ETL作业优化（PySpark）**  
   ```python
   # Glue Job脚本核心（处理1GB+ CSV）
   dynamic_frame = glueContext.create_dynamic_frame.from_options(
     connection_type="s3",
     connection_options={"paths": ["s3://raw-bucket/"], "groupFiles": "inPartition"},
     format="csv"
   )
   
   # 使用动态分区避免小文件问题
   transformed_frame = dynamic_frame.apply_mapping([
     ("date", "string", "event_date", "date"),
     ("amount", "double", "total", "double")
   ]).repartition(1) # 重要！避免产生数千小文件
   ```
   - **关键优化点**：  
     - `groupFiles="inPartition"`：合并小文件（减少Glue作业时间）  
     - `repartition(1)`：确保输出为单个Parquet文件（Quicksight优化）  
     - 设置`Glue Job Timeout=30分钟`（防止无限运行）

2. **Quicksight数据集动态刷新**  
   ```bash
   # 通过CLI设置自动刷新（每天凌晨2点）
   aws quicksight create-data-set-refresh-schedule \
     --aws-account-id 123456789012 \
     --data-set-id ABCDEFGH \
     --schedule-id 123 \
     --schedule-frequency '{
       "Interval": "DAILY",
       "Timezone": "UTC",
       "StartAfterDateTime": "2023-01-01T02:00:00Z"
     }'
   ```
   - **数据质量保障**：  
     - 在Glue Job中添加数据验证步骤（如`check_column_nulls`）  
     - 使用CloudWatch告警监控Glue Job失败（`GlueJobFailed`指标）

#### 成本控制策略
- **Glue成本优化**：  
  - 使用`Glue Version 3.0`（比2.0节省30%计算资源）  
  - 设置`Max Capacity=2`（避免过量DPUs）  
- **Quicksight节省技巧**：  
  - 使用`SPICE`数据集时，设置`Refresh Schedule=Daily`（非实时）  
  - 删除未使用的仪表盘（每月节省$10+）

> ✅ **简历亮点话术**：  
> *“构建自动化CSV数据管道，通过Glue ETL处理10GB+数据集，将ETL时间从45分钟降至8分钟，Quicksight仪表盘实现95%数据查询延迟<500ms”*

---

### 项目三：收据处理自动化（AI文档处理）  
**核心价值**：展示AI服务集成能力，解决“非结构化数据处理”问题  

#### 关键实现步骤（技术深度版）
1. **Textract异步处理优化**  
   ```javascript
   // 处理大文件（>5MB）的异步流程
   const startJob = await textract.startDocumentTextDetection({
     DocumentLocation: { S3Object: { Bucket: bucket, Name: key } },
     NotificationChannel: { SNSTopicArn: snsTopicArn, RoleArn: roleArn }
   }).promise();
   
   // 通过SQS队列接收结果（避免Lambda超时）
   const sqs = new SQS();
   const response = await sqs.receiveMessage({
     QueueUrl: process.env.SQS_URL,
     MaxNumberOfMessages: 1
   }).promise();
   ```
   - **必须规避的陷阱**：  
     - Textract同步API仅支持<5MB文件（大文件**必须用异步**）  
     - 未设置`NotificationChannel`会导致结果丢失（需通过SQS/SNS监听）  
     - 为Textract设置`MaxConcurrency=1`（防止API限流）

2. **DynamoDB表设计最佳实践**  
   ```json
   {
     "TableName": "Receipts",
     "KeySchema": [
       { "AttributeName": "receipt_id", "KeyType": "HASH" },
       { "AttributeName": "vendor", "KeyType": "RANGE" }
     ],
     "GlobalSecondaryIndexes": [{
       "IndexName": "DateIndex",
       "KeySchema": [{ "AttributeName": "date", "KeyType": "HASH" }],
       "Projection": { "ProjectionType": "ALL" }
     }]
   }
   ```
   - **性能关键点**：  
     - 使用`Global Secondary Index`加速按日期查询（避免全表扫描）  
     - 启用`DAX`加速高频查询（10ms级响应）  
     - 设置`Auto Scaling`（读写容量>1000 RCU/WCU时自动扩容）

#### 成本优化技巧
| 服务          | 免费层限制 | 生产级优化方案                     |
|---------------|-----------|-----------------------------------|
| Textract      | 500页/月  | 对非关键文件使用`DetectDocumentText`（低成本版） |
| DynamoDB      | 25GB存储  | 设置`Time to Live (TTL)`自动清理旧数据 |
| SES           | 62K邮件/月 | 使用`Configuration Sets`监控发送质量 |

> ✅ **简历亮点话术**：  
> *“实现收据AI处理系统，通过Textract+DynamoDB将人工录入效率提升90%，采用SQS异步队列解决大文件处理超时问题，日均处理500+收据”*

---

### 项目四：云词典应用（无服务器API驱动）  
**核心价值**：展示API网关与无服务器架构设计能力，解决“高并发查询”与“数据一致性”问题  

#### 关键实现步骤（技术深度版）
1. **Amplify前端部署优化**  
   ```bash
   # 启用SSR（Next.js）提升SEO
   amplify add hosting
   ? Select the plugin module to execute: Hosting with Amplify Console
   ? Choose a type: Continuous deployment (Git-based deployments)
   ```
   - **关键配置**：  
     - 启用`SSR`（Server-Side Rendering）提升首屏加载速度  
     - 配置`amplify.yml`：`amplify build --cache`（加速CI/CD）

2. **DynamoDB查询优化**  
   ```javascript
   // 使用GSI加速分类查询（避免全表扫描）
   const params = {
     TableName: "CloudTerms",
     IndexName: "CategoryIndex",
     KeyConditionExpression: "category = :cat",
     ExpressionAttributeValues: { ":cat": "AWS" }
   };
   ```
   - **性能陷阱**：  
     - 未使用GSI时，`Scan`操作会随数据量增长呈指数级变慢  
     - 启用`DynamoDB Accelerator (DAX)`使查询延迟<10ms（高并发场景必备）

3. **API Gateway缓存策略**  
   ```yaml
   # CloudFormation片段（关键缓存配置）
   ApiGatewayCache:
     Type: AWS::ApiGateway::Cache
     Properties:
       ClusterSize: "0.5" # 最小缓存节点
       TTL: 300 # 5分钟缓存
   ```
   - **必须配置项**：  
     - 为`GET /terms`端点启用缓存（减少DynamoDB读取）  
     - 设置`CacheKeyParameters`：仅对`term`参数缓存（避免缓存污染）

#### 扩展应用实现技巧
| 拓展方向       | 技术实现要点                                                                 |
|----------------|----------------------------------------------------------------------------|
| **内部知识库** | 为DynamoDB添加`version`字段，实现版本控制；使用Cognito用户池管理权限        |
| **猜词游戏**   | 添加`UserProgress`表记录答题记录；用Lambda定时生成新问题（每小时更新）       |
| **多语言支持** | 使用AWS Translate API自动翻译术语；DynamoDB添加`language`分区键              |

> ✅ **简历亮点话术**：  
> *“设计高并发云词典系统，通过DynamoDB GSI+DAX实现1000+ QPS查询，API Gateway缓存降低60%数据库负载，支持多语言扩展架构”*

---

### 项目五：两层Web应用部署（生产级架构）  
**核心价值**：展示基础设施即代码(IaC)能力，解决“高可用”与“安全隔离”问题  

#### 关键实现步骤（技术深度版）
1. **VPC架构设计（Terraform示例）**  
   ```hcl
   # 公有子网（EC2） + 私有子网（RDS）设计
   resource "aws_vpc" "main" {
     cidr_block = "10.0.0.0/16"
   }
   
   resource "aws_subnet" "public" {
     vpc_id            = aws_vpc.main.id
     cidr_block        = "10.0.1.0/24"
     availability_zone = "us-east-1a"
     map_public_ip_on_launch = true # EC2自动分配公网IP
   }
   
   resource "aws_subnet" "private" {
     vpc_id            = aws_vpc.main.id
     cidr_block        = "10.0.2.0/24"
     availability_zone = "us-east-1a"
     map_public_ip_on_launch = false # RDS无公网访问
   }
   ```
   - **安全加固关键点**：  
     - 私有子网的RDS**必须**通过NAT Gateway访问外网（避免直接暴露）  
     - ALB安全组仅允许`0.0.0.0/0:443`，EC2安全组仅允许`ALB安全组:80`  
     - 启用`VPC Flow Logs`监控网络流量

2. **RDS生产级配置**  
   ```bash
   aws rds create-db-instance \
     --db-instance-identifier mydb \
     --db-instance-class db.t4g.micro \
     --engine mysql \
     --allocated-storage 20 \
     --vpc-security-group-ids sg-xxxxxx \
     --publicly-accessible false \ # 关键！禁止公网访问
     --backup-retention-period 7 \
     --enable-performance-insights
   ```
   - **必须配置项**：  
     - `publicly-accessible=false`（防止直接暴露数据库）  
     - `backup-retention-period=7`（满足基础恢复要求）  
     - 启用`Performance Insights`监控SQL瓶颈

3. **ALB健康检查优化**  
   ```bash
   # 设置精准健康检查（避免误判）
   aws elbv2 create-target-group \
     --name my-app-tg \
     --protocol HTTP \
     --port 80 \
     --vpc-id vpc-xxxxx \
     --health-check-path "/health" \ # 自定义健康检查端点
     --health-check-interval-seconds 10 \
     --health-check-timeout-seconds 5
   ```
   - **关键指标**：  
     - 健康检查超时时间 `< 5秒`（避免误杀实例）  
     - 未通过健康检查的实例立即移除（设置`deregistration_delay=30s`）  

#### 成本控制策略
| 资源类型       | 免费层限制      | 生产级优化方案                     |
|----------------|----------------|-----------------------------------|
| ALB            | 750小时/月     | 使用`Application Load Balancer`而非Network（成本更低） |
| EC2            | 750小时/月     | 选择`Graviton`实例（t4g.micro比t3.micro省30%成本） |
| RDS            | 750小时/月     | 启用`Auto Scaling`（仅在高峰时段扩容） |

> ✅ **简历亮点话术**：  
> *“部署高可用两层架构，通过Terraform实现基础设施即代码，ALB+EC2 Auto Scaling支持2000+并发用户，RDS启用多可用区部署确保99.95%可用性”*

---

## 三、中高级开发者专属建议

### 1. 作品集构建策略
| 项目类型       | 展示重点                          | 面试官关注点                     |
|----------------|----------------------------------|--------------------------------|
| Serverless     | 消息可靠性、成本控制、错误处理    | “如何保证消息不丢失？”         |
| 数据管道       | ETL效率、数据质量、可视化优化     | “如何处理10TB数据？”           |
| AI文档处理     | 异步架构设计、AI服务集成          | “大文件处理如何避免超时？”     |
| 无服务器API    | 查询优化、缓存策略、扩展性        | “如何应对突发流量？”           |
| 基础设施部署   | 安全隔离、高可用设计、IaC实现     | “如何设计多区域容灾？”         |

### 2. 避坑指南（中高级开发者必知）
- **⚠️ 免费层陷阱**：  
  - ALB按小时计费（即使未使用），**24小时内必须删除**  
  - Textract免费层仅500页，**大文件处理必须用异步+SQS**  
- **⚠️ 安全红线**：  
  - **永远不要**将RDS设置为`publicly-accessible=true`  
  - **永远不要**在Lambda环境变量中硬编码密钥（改用Secrets Manager）  
- **⚠️ 成本失控场景**：  
  - Glue作业未设置`Max Capacity` → 单次运行$50+  
  - DynamoDB未设置`Auto Scaling` → 突发流量导致$1000+账单  

### 3. 高级技术延伸方向
| 当前项目       | 深化方向                          | 技术栈                          |
|----------------|----------------------------------|--------------------------------|
| 事件通知系统   | 多区域消息路由 + 消息重试队列     | SQS死信队列 + CloudFront全球加速 |
| CSV数据管道    | 实时数据流处理（Kinesis + Glue）  | Kinesis Data Streams + Spark Streaming |
| 收据处理       | 多语言OCR + 结构化数据生成        | Amazon Translate + Comprehend   |
| 云词典应用     | 全球分布式缓存（DynamoDB Global Tables） | CloudFront + DAX              |
| 两层Web应用    | 服务网格（Istio） + 多区域部署    | EKS + AWS App Mesh              |

---

## 结语：从项目到职业跃迁

> **核心价值**：  
> - **技术深度 > 证书数量**：面试官更关注“如何解决实际问题”而非“会用什么服务”  
> - **成本意识 = 生产力**：能控制云成本的开发者价值更高（每节省$1成本 = $1000+项目价值）  
> - **架构思维 > 代码能力**：展示从需求到部署的完整设计思考（如：为什么用ALB而非Nginx？）  

> **行动建议**：  
> 1. **立即构建1个项目**：选择与目标岗位最相关的（如数据工程师优先做CSV管道）  
> 2. **用Terraform重做所有项目**：展示基础设施即代码能力（面试必问）  
> 3. **添加成本分析报告**：在GitHub README中说明“如何将月成本控制在$5内”  
> 4. **录制3分钟演示视频**：重点展示“架构决策过程”（如：为何选择DynamoDB而非RDS？）  

> 💡 **终极提示**：  
> **“当你说出‘我用Textract处理大文件时，通过SQS异步队列避免Lambda超时’时，你的技术深度已超过80%的求职者”**  

> **资源推荐**：  
> - [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/)（所有项目设计依据）  
> - [AWS Cost Optimization Pillar](https://aws.amazon.com/architecture/cost-optimization/)（成本控制终极指南）  
> - [Skill Up by Simply Learn](https://skillup.simplelearn.com)（免费云课程，含AWS认证模拟题）  

> **立即行动**：  
> 在GitHub创建`cloud-projects`仓库，按本指南实现项目，24小时内完成第一个部署。你的简历将因**真实项目细节**与**成本意识**脱颖而出！


---

🎯 AWS 中级云项目实战指南（适合中高级程序员）

本指南基于 Lucy 的视频内容整理，精选 5 个中级 AWS 项目，帮助你从“会用服务”跃升至“能设计架构、解决实际问题”，打造高含金量作品集，增强求职竞争力。每个项目均聚焦真实世界架构模式，强调系统思维、服务集成与自动化能力。

—

📌 通用准备事项（适用于所有项目）

1. ✅ AWS 账户：确保开通 AWS Free Tier，项目完成后务必及时清理资源，避免产生费用。
2. ✅ IAM 权限：为每个项目创建最小权限 IAM 角色/策略，遵循安全最佳实践。
3. ✅ 成本监控：开启 AWS Cost Explorer 和 Budget Alerts。
4. ✅ 项目文档：建议为每个项目撰写 README.md，记录架构图、决策理由、部署步骤、优化思路 —— 这是面试时的核心展示材料。
5. 🎁 优惠提示：配套分步课程见视频描述，使用优惠码 “YouTube 10” 可享 9 折。
6. 🆓 学习平台推荐：Skill Up by Simply Learn（免费证书 + 行业专家课程 + AWS/Google/Microsoft 合作内容）→ 链接见视频描述或置顶评论。

—

🚀 项目一：事件通知系统（无服务器架构实战）

🔧 技术栈：S3 + API Gateway + Lambda + SNS

🎯 目标：构建可扩展的实时通知系统，掌握无服务器事件驱动架构。

✅ 架构步骤：

1. 前端托管：
   - 用 HTML/CSS/events.json 构建前端页面
   - 托管于 S3 并启用 Static Website Hosting

2. 通知引擎：
   - 创建 SNS Topic，配置邮件订阅（支持多邮箱）
   - 编写两个 Lambda 函数：
     - subscribeUser：处理前端订阅请求 → 调用 SNS.subscribe
     - createEvent：接收事件数据 → 调用 SNS.publish

3. API 暴露：
   - 通过 API Gateway 创建两个端点：
     - POST /subscribe → 触发 subscribeUser Lambda
     - POST /events → 触发 createEvent Lambda
   - 启用 CORS，确保前端可调用

4. 前端集成：
   - 调用 API Gateway 端点实现订阅与事件创建

⏱️ 耗时：2–3 小时 | 💰 成本：Free Tier 内（记得删除资源）

💡 应用场景拓展：

- 市场活动通知系统（收集用户邮箱 → 定时推送）
- 内部产品发布警报（员工订阅 → 新版本上线自动通知）
- 团队生日提醒（对接日历 → 自动发送祝福邮件）

📌 面试亮点：能解释为何选择 SNS 而非 SES；如何实现幂等订阅；如何扩展为多通道通知（SMS/Slack）。

—

📊 项目二：自动化 CSV 数据管道（ETL + 可视化）

🔧 技术栈：S3 + Lambda + Glue + QuickSight

🎯 目标：构建端到端无服务器数据流水线，掌握数据清洗、转换、可视化全流程。

✅ 架构步骤：

1. 存储层：
   - 创建 3 个 S3 存储桶：
     - raw-csv-bucket（原始数据）
     - processed-data-bucket（清洗后）
     - transformed-data-bucket（ETL 后）

2. 权限配置：
   - 创建 IAM Role，赋予 Lambda/Glue 访问 S3 的权限

3. 自动触发清洗：
   - 编写 Lambda 函数（Python）：
     - 触发器：S3 PUT 事件（raw-csv-bucket）
     - 功能：读取 CSV → 清洗（去空行、标准化列名等）→ 存入 processed-data-bucket

4. ETL 处理：
   - 使用 AWS Glue：
     - 创建 Glue Crawler → 推断 processed-data-bucket 的 schema
     - 编写 Glue Job（PySpark）→ 转换数据（如聚合、计算衍生字段）→ 输出至 transformed-data-bucket

5. 可视化：
   - 在 QuickSight 中创建数据集 → 连接 transformed-data-bucket
   - 构建仪表盘（柱状图、趋势图等）

⏱️ 耗时：3–4 小时 | 💰 成本：< $1（及时清理 Glue Job 和 QuickSight SPICE）

📌 面试亮点：解释 Lambda vs Glue 的分工；如何处理大文件或并行 ETL；如何添加数据质量校验步骤。

—

🧾 项目三：收据处理自动化系统（AI + 无服务器）

🔧 技术栈：S3 + Textract + Lambda + DynamoDB + SES

🎯 目标：构建智能收据识别与跟踪系统，掌握 AI 服务集成与状态管理。

✅ 架构步骤：

1. 上传入口：
   - 用户上传收据（PDF/JPG/PNG）至 S3 收据存储桶

2. 文本提取：
   - 配置 S3 事件触发 Lambda
   - Lambda 调用 Textract.analyzeDocument → 提取商户、金额、日期等字段

3. 数据持久化：
   - 将结构化数据写入 DynamoDB 表（设计合理主键，如 receiptId + userId）

4. 通知摘要：
   - Lambda 调用 SES 发送邮件摘要（或允许用户通过邮件上传 → SES 接收 → S3 → Textract）

⏱️ 耗时：1–2 小时 | 💰 成本：Free Tier 内（Textract 有免费额度）

📌 面试亮点：如何处理 Textract 识别错误；如何设计 DynamoDB 表结构支持多用户查询；如何扩展为费用报销流程。

—

📖 项目四：云词典应用（全栈无服务器 + 前端托管）

🔧 技术栈：Amplify + API Gateway + Lambda + DynamoDB

🎯 目标：构建 API 驱动的全托管词典应用，掌握前后端分离与无服务器集成。

✅ 架构步骤：

1. 前端部署：
   - 克隆预构建 React 项目（或自己搭建）
   - 使用 AWS Amplify CLI 部署 → 自动 CI/CD + HTTPS + CDN

2. 数据层：
   - 创建 DynamoDB 表（如 CloudTerms，主键 term）
   - 使用 AWS CLI 批量导入术语数据（JSON 格式）

3. 后端逻辑：
   - 编写 Lambda 函数（Node.js/Python）：
     - 输入：API Gateway 传入的 searchTerm
     - 逻辑：DynamoDB getItem → 返回定义

4. API 集成：
   - API Gateway 创建 GET /term/{term} → 集成 Lambda
   - Amplify 前端调用该 API

5. 部署 & 测试：
   - Amplify 自动部署前端，API Gateway 部署后端
   - 测试搜索功能

⏱️ 耗时：2–3 小时 | 💰 成本：Free Tier 内

💡 拓展方向：

- 内部知识库：添加团队术语、缩写解释
- 教学词汇表：教师上传课程术语，学生实时查询
- 互动测验游戏：随机出题 → 用户匹配定义 → 记分排行榜

📌 面试亮点：如何设计 DynamoDB 索引支持模糊搜索；如何添加缓存（API Gateway + CloudFront）；如何实现用户贡献词条功能。

—

🌐 项目五：两层 Web 应用部署（经典三层架构实战）

🔧 技术栈：VPC + EC2 + RDS + ALB

🎯 目标：掌握生产级 Web 应用的网络隔离、高可用部署与负载均衡。

✅ 架构步骤：

1. 网络架构：
   - 创建自定义 VPC（CIDR 如 10.0.0.0/16）
   - 创建 2 个公有子网（跨 AZ）→ 用于 EC2
   - 创建 2 个私有子网（跨 AZ）→ 用于 RDS
   - 配置 Internet Gateway + Route Tables

2. 数据库层：
   - 启动 RDS MySQL 实例（置于私有子网）
   - 配置安全组：仅允许来自 EC2 安全组的 3306 端口
   - 运行 SQL 创建表（如 users, products）

3. 应用层：
   - 启动 2 个 EC2 实例（Ubuntu + Node.js），分别置于不同公有子网
   - 部署简单 Web 应用（连接 RDS，提供 API 或页面）
   - 配置 EC2 安全组：允许 ALB 访问 80/3000 端口

4. 负载均衡：
   - 创建 Application Load Balancer（ALB）
   - Target Group 注册两个 EC2 实例
   - 配置监听器（HTTP 80 → Target Group）
   - 更新 EC2 安全组，允许 ALB IP 访问

5. 测试：
   - 访问 ALB DNS → 应用应正常响应
   - 模拟故障：停用一个 EC2 → 流量自动切到另一台

⏱️ 耗时：2–3 小时 | 💰 成本：大部分 Free Tier，ALB 可能产生少量费用（约 $0.02/小时）

📌 面试亮点：解释为何 RDS 放私有子网；如何实现蓝绿部署；如何添加 Auto Scaling Group；如何配置健康检查与故障转移。

—

✅ 项目完成后，建议：

1. 📁 为每个项目建立 GitHub 仓库，包含：
   - 架构图（用 draw.io 或 Lucidchart）
   - CloudFormation / Terraform 模板（加分项！）
   - 部署脚本（Bash / Python）
   - README（含设计决策、成本估算、优化建议）

2. 🎥 录制 2–3 分钟演示视频，上传 LinkedIn / 个人网站，标题如：
   “Built a Serverless Event Notification System on AWS — End-to-End Architecture Walkthrough”

3. 💬 在面试中使用 STAR 法则描述项目：
   Situation → Task → Action（重点讲架构决策）→ Result（量化成果，如“处理 1000+ 事件/天，成本<$0.5”）

—

🔜 后续计划：

- Lucy 将推出「高级 AWS 项目」系列（如微服务、Kubernetes on EKS、Serverless ML Pipeline 等）
- 🔔 订阅频道 + 开启通知，第一时间获取更新
- 👍 点赞视频 + 评论区留言你最想先做的项目，作者将优先制作详细教程！

—

🧠 总结：这 5 个项目覆盖了无服务器、数据工程、AI 集成、全栈开发、基础设施部署五大方向，是你从“中级”迈向“高级 AWS 工程师”的绝佳跳板。动手做，写清楚，讲明白 —— 你的简历和面试表现将碾压 90% 的竞争者。

立即开始第一个项目吧！🚀