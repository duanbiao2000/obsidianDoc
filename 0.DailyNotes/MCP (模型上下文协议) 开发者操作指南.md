# MCP (模型上下文协议) 开发者操作指南

## 一、MCP 概述

**MCP (Model Context Protocol)** 是由 Anthropic 创建的标准化协议，用于简化大型语言模型(LLM)与外部工具的交互。它解决了传统API集成中的复杂性问题，无需LLM理解API文档或编写代码，而是通过MCP服务器抽象所有复杂性，让LLM只需通过自然语言指令即可与工具交互。

> **核心价值**：MCP就像"AI工具的USB-C接口"，提供统一标准，让LLM能够安全、简单地与各种应用交互。

## 二、环境准备

### 1. 基本要求
- Docker Desktop 安装 (macOS, Windows, Linux)
- 支持MCP的LLM应用 (Claude, LM Studio, Cursor等)
- 需要集成的工具 (Obsidian, Toggle, Kali Linux等)

### 2. Docker MCP 工具包设置
1. 安装Docker Desktop后，启用MCP工具包：
   - 打开Docker Desktop设置 → Beta Features → 启用 "MCP Toolkit"

2. 验证安装：
   ```bash
   docker mcp --version
   ```

## 三、基本使用：Obsidian集成

### 1. 设置Obsidian MCP服务器
1. 在Obsidian中安装 "Local REST API" 社区插件
2. 获取API密钥 (设置 → Local REST API → API Key)
3. 在Docker Desktop中：
   - 点击 "MCP Toolkit" → "Catalog"
   - 搜索 "Obsidian" → 点击 "Add"
   - 粘贴Obsidian API密钥

### 2. 在LLM应用中连接
1. 在Claude/Cursor/LM Studio中：
   - 打开设置 → MCP Integrations
   - 选择 "Docker MCP" 选项
   - 连接成功后，工具列表将自动显示

### 3. 使用示例
```text
"在Obsidian中创建一篇关于如何制作法式压滤咖啡的笔记"
```
LLM将自动调用Obsidian MCP服务器完成操作，无需处理API认证或代码。

## 四、创建自定义MCP服务器：骰子生成器

### 1. 生成代码
使用AI提示工程创建MCP服务器代码：
```text
"创建一个简单的骰子生成器MCP服务器，支持以下功能：
- 掷骰子 (d4, d6, d8, d10, d12, d20)
- 掷多个骰子 (如2d6)
- 硬币翻转
- D&D角色属性生成
- 提供清晰的API文档和错误处理"
```

### 2. 创建项目文件
```bash
mkdir dice-mcp && cd dice-mcp
```

创建以下文件：

**Dockerfile**:
```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY dice_server.py .

EXPOSE 8000

CMD ["python", "dice_server.py"]
```

**requirements.txt**:
```
fastapi
uvicorn
```

**dice_server.py**:
```python
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI()

class DiceRoll(BaseModel):
    dice_type: str
    count: int = 1

@app.post("/roll")
async def roll_dice(roll: DiceRoll):
    dice_types = {
        "d4": 4,
        "d6": 6,
        "d8": 8,
        "d10": 10,
        "d12": 12,
        "d20": 20
    }
    
    if roll.dice_type not in dice_types:
        return {"error": "Invalid dice type"}
    
    sides = dice_types[roll.dice_type]
    results = [random.randint(1, sides) for _ in range(roll.count)]
    
    return {
        "dice_type": roll.dice_type,
        "count": roll.count,
        "results": results,
        "total": sum(results)
    }

@app.post("/flip")
async def flip_coin():
    return {"result": "Heads" if random.choice([True, False]) else "Tails"}

@app.post("/dnd-attributes")
async def generate_dnd_attributes():
    attributes = []
    for _ in range(6):
        rolls = sorted([random.randint(1, 6) for _ in range(4)])
        attributes.append(sum(rolls[1:]))
    return {"strength": attributes[0], "dexterity": attributes[1], "constitution": attributes[2],
            "intelligence": attributes[3], "wisdom": attributes[4], "charisma": attributes[5]}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

### 3. 构建和运行
```bash
# 构建Docker镜像
docker build -t dice-mcp .

# 创建Docker MCP目录
mkdir -p ~/.docker/mcp/catalogs

# 创建自定义目录 (custom_catalog.yaml)
cat > ~/.docker/mcp/catalogs/custom_catalog.yaml <<EOF
servers:
  - name: dice
    image: dice-mcp
    tools:
      - name: roll_dice
        description: "Roll dice of specified type and count"
        parameters:
          - name: dice_type
            type: string
            description: "Type of dice (d4, d6, d8, d10, d12, d20)"
          - name: count
            type: integer
            description: "Number of dice to roll"
      - name: flip_coin
        description: "Flip a coin"
      - name: generate_dnd_attributes
        description: "Generate D&D character attributes"
EOF

# 编辑注册表
cat >> ~/.docker/mcp/registry.yaml <<EOF
- name: dice
  ref: custom_catalog.yaml#dice
EOF

# 启动MCP网关
docker mcp gateway run
```

### 4. 测试使用
在LLM应用中：
```text
"掷2个d6骰子"
```
LLM将自动调用骰子生成器并返回结果。

## 五、创建更复杂的MCP服务器：Toggle计时器

### 1. 了解Toggle API
- Toggle API文档: https://toggle.com/api
- 需要获取API密钥

### 2. 创建Toggle MCP服务器
使用AI提示生成代码：
```text
"创建一个Toggle MCP服务器，支持以下功能：
- 开始计时器
- 停止计时器
- 查看当前所有计时器
- 使用Toggle API (https://toggle.com/api)
- 包含错误处理和安全措施
- 从Docker secrets中获取API密钥"
```

### 3. 保存和配置
1. 创建项目文件结构
2. 保存API密钥到Docker secrets：
   ```bash
   docker mcp secret set TOGGLE_API_TOKEN
   ```
3. 创建自定义目录和注册表条目
4. 构建并运行Docker容器

### 4. 测试使用
```text
"查看当前所有正在运行的计时器"
"停止名为'视频拍摄'的计时器"
"开始一个名为'编程'的新计时器"
```

## 六、创建Kali Linux黑客MCP服务器

### 1. 创建Kali MCP服务器
使用AI提示生成代码：
```text
"创建Kali Linux MCP服务器，支持以下工具：
- nmap网络扫描
- WPScan WordPress漏洞扫描
- SQLMap SQL注入测试
- 使用Kali Linux Docker镜像
- 限制执行权限，仅允许安全测试
- 配置白名单IP范围
- 从Docker secrets中获取必要参数"
```

### 2. 安全配置
- **Dockerfile**:
  ```dockerfile
  FROM kalilinux/kali-rolling:latest

  RUN apt-get update && apt-get install -y \
      nmap \
      wpscan \
      sqlmap \
      && apt-get clean \
      && rm -rf /var/lib/apt/lists/*

  COPY kali_server.py /app/kali_server.py
  WORKDIR /app
  CMD ["python", "kali_server.py"]
  ```

- **kali_server.py** (关键部分):
  ```python
  import subprocess
  import json
  from fastapi import FastAPI, HTTPException

  app = FastAPI()

  @app.post("/nmap-scan")
  async def nmap_scan(target: str, options: str = "-sV"):
      try:
          # 限制扫描范围 (示例)
          if not target.startswith("192.168."):
              raise HTTPException(status_code=403, detail="Only internal network scanning allowed")
          
          cmd = f"nmap {options} {target}"
          result = subprocess.run(cmd.split(), capture_output=True, text=True, timeout=30)
          return {"output": result.stdout}
      except Exception as e:
          raise HTTPException(status_code=500, detail=str(e))
  
  # 类似实现WPScan和SQLMap功能
  ```

### 3. 部署和使用
```bash
# 构建镜像
docker build -t kali-mcp .

# 创建Docker secrets (如果需要)
docker mcp secret set KALI_TARGET_WHITELIST "192.168.0.0/24"

# 启动MCP网关
docker mcp gateway run
```

使用示例：
```text
"对192.168.1.5进行nmap扫描，检测开放端口和服务"
```

## 七、远程MCP服务器设置

### 1. 创建远程MCP服务器
1. 在云服务器上部署MCP服务器
2. 使用HTTP/SSE作为传输协议

**Docker运行命令**:
```bash
docker run -p 8811:8811 -e TRANSPORT=sse dice-mcp
```

### 2. 配置客户端连接
在LLM应用的MCP配置中添加：
```yaml
servers:
  - name: remote-kali
    transport: SSE
    url: http://your-server-ip:8811
    tools: [...]  # 工具定义
```

### 3. 与自动化工具集成 (N8N示例)
1. 在N8N中创建新工作流
2. 添加AI节点，选择MCP工具
3. 配置MCP服务器地址 (http://your-server-ip:8811)
4. 创建自动化流程：
   - 检查网络设备状态
   - 扫描漏洞
   - 生成报告并发送通知

## 八、MCP网关高级配置

### 1. 安全管理
- **Docker secrets管理**:
  ```bash
  # 列出所有密钥
  docker mcp secret list
  
  # 设置密钥
  docker mcp secret set API_KEY
  
  # 删除密钥
  docker mcp secret rm API_KEY
  ```

### 2. 网关运行模式
- **本地模式 (标准输入/输出)**:
  ```bash
  docker mcp gateway run
  ```
  
- **远程模式 (SSE)**:
  ```bash
  docker mcp gateway run --transport sse --port 8811
  ```

### 3. 多目录管理
```bash
# 查看当前目录
ls ~/.docker/mcp/catalogs

# 添加多个自定义目录
mkdir -p ~/.docker/mcp/catalogs/custom1
mkdir -p ~/.docker/mcp/catalogs/custom2

# 编辑注册表
cat >> ~/.docker/mcp/registry.yaml <<EOF
- name: server1
  ref: custom1/catalog.yaml#server1
- name: server2
  ref: custom2/catalog.yaml#server2
EOF
```

## 九、最佳实践与安全建议

1. **最小权限原则**:
   - 为每个MCP服务器设置精确的权限
   - 限制网络访问范围 (如仅允许内部IP扫描)
   - 使用Docker secrets管理敏感信息

2. **错误处理**:
   - 为每个工具实现详细的错误处理
   - 提供清晰的错误信息，但不泄露系统细节

3. **监控与日志**:
   - 记录所有MCP工具调用
   - 设置日志轮转和保留策略

4. **测试流程**:
   - 在生产环境前进行充分测试
   - 使用沙盒环境验证功能
   - 实现自动化测试用例

## 十、未来展望

MCP协议正在快速发展，未来可能支持：
- 更多原生工具集成
- 更强大的安全机制
- 跨平台支持
- 企业级认证和授权

> **开发者提示**：MCP代表了AI与工具集成的未来。掌握MCP技术将使您能够构建真正实用的AI助手，将LLM从理论辅助变为实际生产力工具。现在正是学习和掌握这项技术的最佳时机！

## 附录：常用命令参考

| 命令 | 用途 |
|------|------|
| `docker mcp gateway run` | 启动本地MCP网关 |
| `docker mcp gateway run --transport sse --port 8811` | 启动远程MCP网关 |
| `docker mcp secret list` | 列出所有密钥 |
| `docker mcp secret set NAME` | 设置新密钥 |
| `docker mcp catalog ls` | 列出可用目录 |
| `docker build -t my-mcp .` | 构建MCP服务器镜像 |
| `docker ps` | 查看正在运行的容器 |

> **注意**：MCP协议仍在快速发展中，请关注官方文档获取最新信息。


---

# MCP (Model Context Protocol) 开发人员操作指南

## 1. 什么是MCP？

MCP (Model Context Protocol，模型上下文协议) 是由Anthropic创建的一种标准化协议，用于让大型语言模型(LLM)与外部工具和服务进行交互。它解决了LLM与外部工具集成的难题，类似于USB-C解决了我们的线缆问题。

**核心价值**：
- 为LLM提供标准化的工具访问方式
- 抽象化API调用的复杂性
- 使LLM能够通过自然语言指令使用各种工具
- 已成为行业标准，被主流LLM平台广泛支持

## 2. MCP工作原理

MCP通过引入MCP服务器作为中间层来工作：

```
LLM → MCP服务器 → 外部API/工具
```

**关键优势**：
- LLM无需理解API文档、认证机制或编写代码
- MCP服务器处理所有复杂性（API调用、认证等）
- LLM只需用自然语言请求特定工具/任务
- 创建了专为LLM设计的"GUI"（纯文本界面）

## 3. 环境设置

### 前置条件
- Docker Desktop (Mac, Windows, Linux)
- LLM应用（Claude, LM Studio, Cursor等）

### 安装步骤
1. 下载并安装[Docker Desktop](https://www.docker.com/desktop)
   - Windows用户需额外设置WSL2或Hyper-V
2. 启动Docker Desktop并登录（可选但推荐）
3. 启用MCP工具包：
   - 进入Docker Desktop设置 → Beta Features
   - 启用"Docker MCP toolkit"

## 4. 使用现有MCP服务器

### 通过Docker MCP Catalog添加服务器
```bash
# 查看可用MCP服务器
docker mcp catalog ls

# 添加服务器（例如Obsidian）
docker mcp server add obsidian
```

### 管理API密钥
```bash
# 设置API密钥（例如Obsidian）
docker mcp secret set OBSIDIAN_API_KEY your_api_key_here

# 查看已设置的密钥
docker mcp secret ls
```

### 连接LLM客户端
1. 在Docker Desktop中：
   - 转到MCP Toolkit → Clients
   - 选择您的LLM应用（Claude, LM Studio, Cursor等）
   - 点击"Connect"
2. 重启您的LLM应用
3. 在应用设置中选择"MCP Docker"作为MCP服务器

## 5. 构建自定义MCP服务器

### 基本步骤
1. 创建项目目录
2. 编写Dockerfile
3. 创建服务器代码
4. 构建Docker镜像
5. 添加到MCP catalog
6. 更新registry

### 示例：创建骰子滚动MCP服务器

#### 步骤1: 创建项目结构
```bash
mkdir dice-mcp-server && cd dice-mcp-server
touch Dockerfile requirements.txt dice_server.py README.md
```

#### 步骤2: 编写Dockerfile
```dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY dice_server.py .

CMD ["python", "dice_server.py"]
```

#### 步骤3: 创建requirements.txt
```
mcp-server
```

#### 步骤4: 创建dice_server.py
```python
from mcp.server import Server
from mcp.types import ToolResult
import random

server = Server()

@server.tool("roll_dice", "Rolls dice in standard D&D notation (e.g., 2d6)")
def roll_dice(dice_notation: str) -> ToolResult:
    """Rolls dice based on standard D&D notation"""
    try:
        num_dice, sides = map(int, dice_notation.split('d'))
        results = [random.randint(1, sides) for _ in range(num_dice)]
        total = sum(results)
        return ToolResult(
            content=f"Rolled {dice_notation}: {results} = {total}",
            status="success"
        )
    except Exception as e:
        return ToolResult(
            content=f"Error rolling dice: {str(e)}",
            status="error"
        )

@server.tool("flip_coin", "Flips a coin (heads or tails)")
def flip_coin() -> ToolResult:
    """Flips a coin"""
    result = "heads" if random.randint(0, 1) == 0 else "tails"
    return ToolResult(
        content=f"Coin flip result: {result}",
        status="success"
    )

if __name__ == "__main__":
    server.run()
```

#### 步骤5: 构建Docker镜像
```bash
docker build -t dice-mcp-server .
```

#### 步骤6: 添加到MCP catalog
创建`~/.docker/mcp/catalogs/my-custom-catalog.yaml`:
```yaml
servers:
  dice:
    name: "Dice Roller"
    description: "Roll dice for D&D and other games"
    image: "dice-mcp-server"
    tools:
      - name: "roll_dice"
        description: "Rolls dice in standard D&D notation (e.g., 2d6)"
        input_schema:
          type: "object"
          properties:
            dice_notation:
              type: "string"
              description: "Dice notation (e.g., 2d6)"
          required: ["dice_notation"]
      - name: "flip_coin"
        description: "Flips a coin (heads or tails)"
        input_schema: {}
```

#### 步骤7: 更新registry
编辑`~/.docker/mcp/registry.yaml`，添加：
```yaml
dice:
  ref: my-custom-catalog/dice
```

#### 步骤8: 配置LLM客户端
更新您的LLM应用MCP配置，添加自定义catalog：
```yaml
servers:
  - command: docker
    args:
      - mcp
      - gateway
      - run
      - --catalogs
      - docker
      - my-custom-catalog
      - --registry
      - /Users/yourname/.docker/mcp/registry.yaml
    transport: stdio
```

## 6. MCP通信机制

MCP支持两种主要通信方式：

### 本地服务器（推荐）
- **通信方式**：标准输入/输出(STDIO)
- **特点**：
  - 零延迟
  - 无网络开销
  - 仅限本地机器
  - 通过命令行管道交换JSON RPC消息

### 远程服务器
- **通信方式**：HTTP/SSE (Server-Sent Events)
- **特点**：
  - 通过网络访问
  - 需要HTTPS确保安全
  - 适合远程服务
  - 配置更复杂（需要设置Web服务器、认证等）

## 7. Docker MCP Gateway高级用法

### 启动Gateway服务
```bash
# 本地模式（STDIO）
docker mcp gateway run

# 网络模式（SSE）
docker mcp gateway run --transport sse --port 8811
```

### 远程访问配置
```yaml
servers:
  - url: "http://your-ip:8811"
    transport: sse
```

### 多Catalog管理
```bash
docker mcp gateway run \
  --catalogs docker,my-custom-catalog \
  --registry ~/.docker/mcp/registry.yaml
```

## 8. 实用技巧与最佳实践

### 1. 安全管理API密钥
```bash
# 使用Docker MCP Secrets管理敏感信息
docker mcp secret set TOGGL_API_TOKEN your_token_here
```

在服务器代码中通过环境变量访问：
```python
import os
api_token = os.getenv("TOGGL_API_TOKEN")
```

### 2. 调试MCP服务器
```bash
# 查看正在运行的MCP服务器
watch -n 0.5 docker ps

# 手动启动MCP服务器进行调试
docker run -it --rm dice-mcp-server
```

### 3. 构建API集成MCP服务器（以Toggl为例）
1. 详细阅读API文档
2. 在提示中提供清晰的工具描述
3. 包含认证方法和示例请求
4. 实现错误处理和重试逻辑

### 4. 创建Kali Linux MCP服务器
```dockerfile
FROM kalilinux/kali-rolling

RUN apt-get update && apt-get install -y \
    nmap \
    sqlmap \
    wpscan \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY kali_server.py .

CMD ["python3", "kali_server.py"]
```

### 5. 提交到官方Catalog
完成开发后，可将您的MCP服务器提交到Docker官方Catalog：
1. 确保符合所有规范
2. 创建Docker Hub仓库
3. 提交审核请求
4. 等待批准（可能需要时间）

## 结语

MCP是LLM工具集成的革命性协议，它让开发人员能够：
- 快速为LLM添加强大功能
- 创建自定义工具链
- 实现复杂的自动化工作流
- 无需LLM理解底层实现细节

掌握MCP开发技能将使您在AI应用开发领域占据先机。现在正是构建MCP服务器的最佳时机，因为生态系统仍在快速发展，早期采用者将获得巨大优势。

> "这不是未来，这是现在。MCP让LLM真正成为生产力工具，而不仅仅是聊天机器人。" —— 一位兴奋的开发人员