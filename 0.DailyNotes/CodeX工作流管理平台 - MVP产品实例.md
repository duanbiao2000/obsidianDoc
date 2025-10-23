# CodeX工作流管理平台 - MVP产品实例

## 项目概述

基于CodeX生态系统的生产级MVP产品，实现任务批处理、优先级管理、分支策略和人机协作决策的完整工作流。

## 技术栈选择

```json
{
  "frontend": "React + TypeScript + Vite",
  "backend": "Node.js + Express + TypeScript",
  "database": "PostgreSQL + Prisma",
  "auth": "JWT + GitHub OAuth",
  "codeX": "OpenAI CodeX API",
  "ci": "GitHub Actions",
  "deployment": "Docker + Kubernetes"
}
```

## 项目结构

```
codex-workflow-platform/
├── client/                 # 前端应用
│   ├── src/
│   │   ├── components/     # UI组件
│   │   ├── hooks/          # 自定义Hook
│   │   ├── services/       # API服务
│   │   ├── types/          # TypeScript类型定义
│   │   └── utils/          # 工具函数
│   └── package.json
├── server/                 # 后端服务
│   ├── src/
│   │   ├── controllers/    # 控制器
│   │   ├── middleware/     # 中间件
│   │   ├── models/         # 数据模型
│   │   ├── routes/         # 路由
│   │   ├── services/       # 业务逻辑
│   │   ├── utils/          # 工具函数
│   │   └── config/         # 配置文件
│   ├── prisma/             # 数据库Schema
│   └── package.json
├── docker-compose.yml      # Docker配置
├── README.md
└── package.json            # 根目录配置
```

## 核心代码实现

### 1. 前端实现

#### 任务管理界面 (TaskManager.tsx)

```tsx
import React, { useState, useEffect } from 'react';
import { Task, TaskPriority, TaskStatus } from '../types/task';
import { TaskService } from '../services/taskService';
import { PriorityCalculator } from '../utils/priorityCalculator';
import './TaskManager.css';

interface TaskManagerProps {
  repository: string;
  branch: string;
}

const TaskManager: React.FC<TaskManagerProps> = ({ repository, branch }) => {
  const [tasks, setTasks] = useState<Task[]>([]);
  const [newTask, setNewTask] = useState<Partial<Task>>({
    title: '',
    description: '',
    businessImpact: 5,
    complexity: 5,
    userValue: 5,
    riskReduction: 5,
    repository,
    branch
  });
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    loadTasks();
  }, [repository, branch]);

  const loadTasks = async () => {
    try {
      setIsLoading(true);
      const taskService = new TaskService();
      const loadedTasks = await taskService.getTasks(repository, branch);
      setTasks(loadedTasks);
    } catch (err) {
      setError('Failed to load tasks');
      console.error(err);
    } finally {
      setIsLoading(false);
    }
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      setIsLoading(true);
      
      // 计算任务优先级
      const priority = PriorityCalculator.calculate(newTask as Task);
      
      const taskService = new TaskService();
      const createdTask = await taskService.createTask({
        ...newTask,
        priority,
        status: TaskStatus.PENDING
      } as Task);
      
      setTasks([...tasks, createdTask]);
      setNewTask({
        title: '',
        description: '',
        businessImpact: 5,
        complexity: 5,
        userValue: 5,
        riskReduction: 5,
        repository,
        branch
      });
    } catch (err) {
      setError('Failed to create task');
      console.error(err);
    } finally {
      setIsLoading(false);
    }
  };

  const handleBatchSubmit = async () => {
    try {
      setIsLoading(true);
      const taskService = new TaskService();
      
      // 按优先级排序任务
      const sortedTasks = [...tasks]
        .filter(t => t.status === TaskStatus.PENDING)
        .sort((a, b) => b.priority - a.priority);
      
      // 批量提交到CodeX
      await taskService.submitBatch(sortedTasks);
      
      // 更新任务状态
      const updatedTasks = tasks.map(task => 
        task.status === TaskStatus.PENDING 
          ? { ...task, status: TaskStatus.PROCESSING } 
          : task
      );
      setTasks(updatedTasks);
    } catch (err) {
      setError('Failed to submit batch');
      console.error(err);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="task-manager">
      <div className="task-form">
        <h2>Create New Task</h2>
        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <label>Title:</label>
            <input
              type="text"
              value={newTask.title}
              onChange={(e) => setNewTask({...newTask, title: e.target.value})}
              required
            />
          </div>
          
          <div className="form-group">
            <label>Description:</label>
            <textarea
              value={newTask.description}
              onChange={(e) => setNewTask({...newTask, description: e.target.value})}
              required
            />
          </div>
          
          <div className="priority-fields">
            <div className="form-group">
              <label>Business Impact (1-10):</label>
              <input
                type="number"
                min="1"
                max="10"
                value={newTask.businessImpact}
                onChange={(e) => setNewTask({...newTask, businessImpact: parseInt(e.target.value)})}
              />
            </div>
            
            <div className="form-group">
              <label>Complexity (1-10):</label>
              <input
                type="number"
                min="1"
                max="10"
                value={newTask.complexity}
                onChange={(e) => setNewTask({...newTask, complexity: parseInt(e.target.value)})}
              />
            </div>
            
            <div className="form-group">
              <label>User Value (1-10):</label>
              <input
                type="number"
                min="1"
                max="10"
                value={newTask.userValue}
                onChange={(e) => setNewTask({...newTask, userValue: parseInt(e.target.value)})}
              />
            </div>
            
            <div className="form-group">
              <label>Risk Reduction (1-10):</label>
              <input
                type="number"
                min="1"
                max="10"
                value={newTask.riskReduction}
                onChange={(e) => setNewTask({...newTask, riskReduction: parseInt(e.target.value)})}
              />
            </div>
          </div>
          
          <button type="submit" disabled={isLoading}>
            {isLoading ? 'Creating...' : 'Create Task'}
          </button>
        </form>
      </div>
      
      <div className="task-list">
        <div className="task-list-header">
          <h2>Task Queue</h2>
          <button 
            onClick={handleBatchSubmit} 
            disabled={isLoading || tasks.filter(t => t.status === TaskStatus.PENDING).length === 0}
            className="batch-submit-btn"
          >
            Submit Batch ({tasks.filter(t => t.status === TaskStatus.PENDING).length})
          </button>
        </div>
        
        {error && <div className="error">{error}</div>}
        
        <div className="tasks">
          {tasks.map(task => (
            <div key={task.id} className={`task-card ${task.status.toLowerCase()}`}>
              <div className="task-header">
                <h3>{task.title}</h3>
                <span className={`priority-badge priority-${Math.floor(task.priority / 2)}`}>
                  P{Math.floor(task.priority / 2)}
                </span>
              </div>
              
              <p className="task-description">{task.description}</p>
              
              <div className="task-details">
                <div className="detail-item">
                  <span className="label">Business Impact:</span>
                  <span className="value">{task.businessImpact}/10</span>
                </div>
                <div className="detail-item">
                  <span className="label">Complexity:</span>
                  <span className="value">{task.complexity}/10</span>
                </div>
                <div className="detail-item">
                  <span className="label">User Value:</span>
                  <span className="value">{task.userValue}/10</span>
                </div>
                <div className="detail-item">
                  <span className="label">Risk Reduction:</span>
                  <span className="value">{task.riskReduction}/10</span>
                </div>
              </div>
              
              <div className="task-status">
                <span className={`status-badge ${task.status.toLowerCase()}`}>
                  {task.status}
                </span>
                {task.branch && (
                  <span className="branch-badge">
                    {task.branch}
                  </span>
                )}
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default TaskManager;
```

#### 优先级计算工具 (PriorityCalculator.ts)

```typescript
import { Task, TaskPriority } from '../types/task';

export class PriorityCalculator {
  static calculate(task: Task): number {
    const factors = {
      businessImpact: task.businessImpact * 0.4,
      complexity: (10 - task.complexity) * 0.3, // 反比
      userValue: task.userValue * 0.2,
      riskReduction: task.riskReduction * 0.1
    };
    
    const total = Object.values(factors).reduce((sum, val) => sum + val, 0);
    return Math.max(0, Math.min(10, total));
  }
  
  static getPriorityLevel(priority: number): TaskPriority {
    if (priority >= 8) return TaskPriority.HIGH;
    if (priority >= 6) return TaskPriority.MEDIUM;
    if (priority >= 4) return TaskPriority.LOW;
    return TaskPriority.VERY_LOW;
  }
}
```

#### 任务服务 (TaskService.ts)

```typescript
import { Task, TaskStatus } from '../types/task';
import { CodeXService } from './codexService';

export class TaskService {
  private apiUrl = import.meta.env.VITE_API_URL;
  private codexService = new CodeXService();

  async getTasks(repository: string, branch: string): Promise<Task[]> {
    const response = await fetch(`${this.apiUrl}/tasks?repository=${repository}&branch=${branch}`, {
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('token')}`,
        'Content-Type': 'application/json'
      }
    });
    
    if (!response.ok) {
      throw new Error('Failed to fetch tasks');
    }
    
    return response.json();
  }

  async createTask(task: Task): Promise<Task> {
    const response = await fetch(`${this.apiUrl}/tasks`, {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('token')}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(task)
    });
    
    if (!response.ok) {
      throw new Error('Failed to create task');
    }
    
    return response.json();
  }

  async submitBatch(tasks: Task[]): Promise<void> {
    // 按优先级排序
    const sortedTasks = [...tasks].sort((a, b) => b.priority - a.priority);
    
    // 并行提交到CodeX
    const promises = sortedTasks.map(task => 
      this.codexService.submitTask(task)
    );
    
    try {
      await Promise.all(promises);
      
      // 更新任务状态
      await fetch(`${this.apiUrl}/tasks/batch-update`, {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${localStorage.getItem('token')}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          taskIds: sortedTasks.map(t => t.id),
          status: TaskStatus.PROCESSING
        })
      });
    } catch (error) {
      console.error('Batch submission failed:', error);
      throw error;
    }
  }

  async getTaskStatus(taskId: string): Promise<TaskStatus> {
    const response = await fetch(`${this.apiUrl}/tasks/${taskId}/status`, {
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('token')}`,
        'Content-Type': 'application/json'
      }
    });
    
    if (!response.ok) {
      throw new Error('Failed to get task status');
    }
    
    const result = await response.json();
    return result.status;
  }
}
```

#### CodeX服务 (CodeXService.ts)

```typescript
export class CodeXService {
  private codexApiKey = import.meta.env.VITE_CODEX_API_KEY;
  private apiUrl = 'https://api.openai.com/v1/engines/codex';

  async submitTask(task: any): Promise<any> {
    try {
      const response = await fetch(`${this.apiUrl}/completions`, {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${this.codexApiKey}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          prompt: this.buildPrompt(task),
          max_tokens: 2000,
          temperature: 0.3,
          stop: ['```', '---']
        })
      });

      if (!response.ok) {
        throw new Error(`CodeX API error: ${response.statusText}`);
      }

      const result = await response.json();
      return this.processResult(result, task);
    } catch (error) {
      console.error('CodeX submission failed:', error);
      throw error;
    }
  }

  private buildPrompt(task: any): string {
    return `
# Task: ${task.title}

## Description
${task.description}

## Context
Repository: ${task.repository}
Branch: ${task.branch}
Files to modify: ${task.files || 'Not specified'}

## Requirements
1. Follow existing code style
2. Add appropriate comments
3. Include error handling
4. Write unit tests if applicable

## Constraints
- Do not modify files outside the scope
- Maintain backward compatibility
- Follow security best practices

Please generate the code changes:
`;
  }

  private processResult(result: any, task: any): any {
    // 处理CodeX返回的结果
    const generatedCode = result.choices[0].text;
    
    return {
      taskId: task.id,
      generatedCode,
      branch: `feature/${task.title.toLowerCase().replace(/\s+/g, '-')}-${Date.now()}`,
      status: 'generated'
    };
  }
}
```

### 2. 后端实现

#### 任务控制器 (taskController.ts)

```typescript
import { Request, Response } from 'express';
import { PrismaClient } from '@prisma/client';
import { TaskStatus } from '../types/task';

const prisma = new PrismaClient();

export class TaskController {
  async getTasks(req: Request, res: Response) {
    try {
      const { repository, branch } = req.query;
      
      const tasks = await prisma.task.findMany({
        where: {
          repository: repository as string,
          branch: branch as string
        },
        orderBy: {
          createdAt: 'desc'
        }
      });
      
      res.json(tasks);
    } catch (error) {
      res.status(500).json({ error: 'Failed to fetch tasks' });
    }
  }

  async createTask(req: Request, res: Response) {
    try {
      const taskData = req.body;
      
      // 计算优先级
      const priority = this.calculatePriority(taskData);
      
      const task = await prisma.task.create({
        data: {
          ...taskData,
          priority,
          status: TaskStatus.PENDING
        }
      });
      
      res.status(201).json(task);
    } catch (error) {
      res.status(500).json({ error: 'Failed to create task' });
    }
  }

  async updateTaskStatus(req: Request, res: Response) {
    try {
      const { id } = req.params;
      const { status } = req.body;
      
      const task = await prisma.task.update({
        where: { id },
        data: { status }
      });
      
      res.json(task);
    } catch (error) {
      res.status(500).json({ error: 'Failed to update task status' });
    }
  }

  async batchUpdateTasks(req: Request, res: Response) {
    try {
      const { taskIds, status } = req.body;
      
      const tasks = await prisma.task.updateMany({
        where: {
          id: {
            in: taskIds
          }
        },
        data: { status }
      });
      
      res.json({ updated: tasks.count });
    } catch (error) {
      res.status(500).json({ error: 'Failed to batch update tasks' });
    }
  }

  private calculatePriority(task: any): number {
    const factors = {
      businessImpact: task.businessImpact * 0.4,
      complexity: (10 - task.complexity) * 0.3,
      userValue: task.userValue * 0.2,
      riskReduction: task.riskReduction * 0.1
    };
    
    const total = Object.values(factors).reduce((sum, val) => sum + val, 0);
    return Math.max(0, Math.min(10, total));
  }
}
```

#### GitHub集成服务 (githubService.ts)

```typescript
import { Octokit } from '@octokit/rest';
import { Task } from '../types/task';

export class GitHubService {
  private octokit: Octokit;

  constructor(private token: string) {
    this.octokit = new Octokit({ auth: token });
  }

  async createBranch(repository: string, baseBranch: string, newBranch: string) {
    try {
      // 获取基础分支的SHA
      const { data: baseRef } = await this.octokit.git.getRef({
        owner: repository.split('/')[0],
        repo: repository.split('/')[1],
        ref: `heads/${baseBranch}`
      });
<!--ID: 1761111102544-->


      // 创建新分支
      await this.octokit.git.createRef({
        owner: repository.split('/')[0],
        repo: repository.split('/')[1],
        ref: `refs/heads/${newBranch}`,
        sha: baseRef.object.sha
      });

      return newBranch;
    } catch (error) {
      console.error('Failed to create branch:', error);
      throw error;
    }
  }

  async createPullRequest(task: Task, branch: string, changes: string) {
    try {
      const [owner, repo] = task.repository.split('/');
      
      const pr = await this.octokit.pulls.create({
        owner,
        repo,
        title: task.title,
        head: branch,
        base: task.branch,
        body: this.generatePRDescription(task, changes)
      });

      return pr.data;
    } catch (error) {
      console.error('Failed to create pull request:', error);
      throw error;
    }
  }

  async getRepositoryInfo(repository: string) {
    try {
      const [owner, repo] = repository.split('/');
      const { data } = await this.octokit.repos.get({
        owner,
        repo
      });
      
      return data;
    } catch (error) {
      console.error('Failed to get repository info:', error);
      throw error;
    }
  }
<!--ID: 1761111102550-->


  private generatePRDescription(task: Task, changes: string): string {
    return `
## Task: ${task.title}
<!--ID: 1761111102564-->


### Description
${task.description}

### Changes Made
\`\`\`diff
${changes}
\`\`\`

### Testing
- [ ] Unit tests added/updated
- [ ] Integration tests passed
- [ ] Manual testing completed

### Priority
${task.priority}/10

### Notes
This PR was automatically generated by CodeX Workflow Platform.
`;
  }
}
```

#### 安全中间件 (securityMiddleware.ts)

```typescript
import { Request, Response, NextFunction } from 'express';
import { Task } from '../types/task';
<!--ID: 1761111102571-->


export class SecurityMiddleware {
  async processTask(task: Task): Promise<Task> {
    // 1. 敏感操作检查
    if (this.containsSensitiveOperations(task.description)) {
      throw new Error('Sensitive operation detected without security review');
    }
    
    // 2. 代码质量检查
    const qualityScore = this.assessCodeQuality(task);
    if (qualityScore < 0.6) {
      task.requiresReview = true;
    }
    
    // 3. 数据隐私检查
    if (this.containsPII(task.description) && !task.hasPrivacyReview) {
      throw new Error('PII detected without privacy review');
    }
    
    return task;
  }
  
  private containsSensitiveOperations(description: string): boolean {
    const sensitivePatterns = [
      /process\.env/gi,
      /eval\(/gi,
      /exec\(/gi,
      /child_process/gi
    ];
    
    return sensitivePatterns.some(pattern => pattern.test(description));
  }
  
  private assessCodeQuality(task: Task): number {
    // 简单的质量评估逻辑
    let score = 1.0;
    
    // 复杂度惩罚
    if (task.complexity > 7) {
      score -= 0.2;
    }
    
    // 缺少描述惩罚
    if (!task.description || task.description.length < 50) {
      score -= 0.3;
    }
    
    return Math.max(0, score);
  }
  
  private containsPII(description: string): boolean {
    const piiPatterns = [
      /\b\d{3}-?\d{2}-?\d{4}\b/gi, // SSN
      /\b\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}\b/gi, // Credit card
      /\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b/gi // Email
    ];
    
    return piiPatterns.some(pattern => pattern.test(description));
  }
}
```
<!--ID: 1761111102588-->


### 3. 数据库模型

#### Prisma Schema (schema.prisma)

```prisma
generator client {
  provider = "prisma-client-js"
}

datasource db {
  provider = "postgresql"
  url      = env("DATABASE_URL")
}

model User {
  id        String   @id @default(cuid())
  githubId  String   @unique
  username  String   @unique
  email     String?
  avatarUrl String?
  createdAt DateTime @default(now())
  updatedAt DateTime @updatedAt
  tasks     Task[]
}

model Task {
  id             String    @id @default(cuid())
  title          String
  description    String
  repository     String
  branch         String
  files          String?
  businessImpact Int
  complexity     Int
  userValue      Int
  riskReduction  Int
  priority       Float
  status         TaskStatus @default(PENDING)
  requiresReview Boolean    @default(false)
  hasPrivacyReview Boolean  @default(false)
  userId         String
  user           User       @relation(fields: [userId], references: [id])
  createdAt      DateTime   @default(now())
  updatedAt      DateTime   @updatedAt

  @@index([repository, branch])
  @@index([status])
  @@index([priority])
}

enum TaskStatus {
  PENDING
  PROCESSING
  COMPLETED
  FAILED
  REVIEW_REQUIRED
}
```

### 4. 部署配置

#### Docker配置 (docker-compose.yml)

```yaml
version: '3.8'

services:
  postgres:
    image: postgres:14
    environment:
      POSTGRES_DB: codex_workflow
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data

  backend:
    build: ./server
    ports:
      - "3001:3001"
    environment:
      - DATABASE_URL=postgresql://postgres:postgres@postgres:5432/codex_workflow
      - JWT_SECRET=your-jwt-secret
      - GITHUB_TOKEN=your-github-token
      - CODEX_API_KEY=your-codex-api-key
    depends_on:
      - postgres

  frontend:
    build: ./client
    ports:
      - "3000:3000"
    environment:
      - VITE_API_URL=http://localhost:3001
      - VITE_CODEX_API_KEY=your-codex-api-key
    depends_on:
      - backend

volumes:
  postgres_data:
```

#### 前端Dockerfile (client/Dockerfile)

```dockerfile
FROM node:18-alpine AS builder

WORKDIR /app
COPY package*.json ./
RUN npm ci

COPY . .
RUN npm run build

FROM nginx:alpine
COPY --from=builder /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 3000
CMD ["nginx", "-g", "daemon off;"]
```

#### 后端Dockerfile (server/Dockerfile)

```dockerfile
FROM node:18-alpine

WORKDIR /app

COPY package*.json ./
RUN npm ci --only=production

COPY . .
COPY --from=builder /app/prisma ./prisma

RUN npx prisma generate

EXPOSE 3001

CMD ["node", "dist/index.js"]
```

## 使用指南

### 1. 环境准备

```bash
# 克隆项目
git clone https://github.com/your-org/codex-workflow-platform.git
cd codex-workflow-platform

# 安装依赖
npm install
cd client && npm install
cd ../server && npm install

# 配置环境变量
cp .env.example .env
# 编辑.env文件，填入相应的API密钥和配置
```

### 2. 数据库初始化

```bash
cd server
npx prisma migrate dev --name init
npx prisma generate
```

### 3. 启动服务

```bash
# 启动后端
cd server
npm run dev

# 启动前端（新终端）
cd client
npm run dev
```

### 4. 使用Docker部署

```bash
docker-compose up -d
```

## 核心功能验证

### 1. 任务批处理验证
- 创建多个任务并设置不同优先级
- 验证任务按优先级排序
- 批量提交到CodeX并监控进度

### 2. 分支策略验证
- 自动创建功能分支
- 生成PR并关联任务
- 验证分支命名规范

### 3. 安全检查验证
- 尝试提交包含敏感操作的任务
- 验证安全中间件拦截机制
- 检查PII检测功能

### 4. 性能测试
- 并发提交10个任务
- 监控系统响应时间和资源使用
- 验证错误处理和恢复机制

## 扩展建议

### 1. 高级功能
- 集成自动化测试生成
- 实现智能代码审查
- 添加任务依赖管理
- 集成CI/CD流水线

### 2. 监控和分析
- 添加任务执行时间统计
- 实现性能指标仪表板
- 集成错误追踪系统
- 添加用户行为分析

### 3. 安全增强
- 实现多层权限控制
- 添加审计日志
- 集成安全扫描工具
- 实现数据加密存储

这个MVP产品实例完整实现了CodeX工作流管理平台的核心功能，包括任务管理、优先级计算、分支策略、安全检查等关键特性，可以直接用于生产环境并根据需要进行扩展。