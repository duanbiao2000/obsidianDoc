# 🚀 完整 Markdown 笔记应用（React + Node.js + PostgreSQL）

> **全栈实现**：前端 React 页面 + 后端 REST API + PostgreSQL 数据库  
> 支持：文件上传、语法检查、Markdown 渲染、笔记管理

---

## 📁 项目结构

```
markdown-note-app/
│
├── client/               # React 前端
│   ├── public/
│   └── src/
│       ├── components/
│       ├── services/
│       └── App.js
│
├── server/               # Node.js 后端
│   ├── models/
│   │   └── Note.js
│   ├── routes/
│   │   └── notes.js
│   ├── db.js
│   └── server.js
│
├── docker-compose.yml    # 一键启动 Postgres
└── package.json          # 根目录脚本
```

---

## 🐳 第一步：启动 PostgreSQL（Docker）

```yaml
# docker-compose.yml
version: '3.8'
services:
  postgres:
    image: postgres:15
    restart: always
    environment:
      POSTGRES_USER: noteuser
      POSTGRES_PASSWORD: notepass
      POSTGRES_DB: notedb
    ports:
      - "5432:5432"
    volumes:
      - pgdata:/var/lib/postgresql/data

volumes:
  pgdata:
```

启动数据库：
```bash
docker-compose up -d
```

---

## 🔧 第二步：后端实现（Node.js + Express + PostgreSQL）

### 1. 初始化 server

```bash
cd server
npm init -y
npm install express pg express-fileupload marked compromise cors dotenv
```

### 2. `server/db.js` —— 数据库连接

```js
// server/db.js
const { Pool } = require('pg');

const pool = new Pool({
  connectionString: process.env.DATABASE_URL || 
    'postgres://noteuser:notepass@localhost:5432/notedb'
});

pool.on('connect', () => {
  console.log('✅ PostgreSQL 数据库连接成功');
});

module.exports = {
  query: (text, params) => pool.query(text, params)
};
```

### 3. `server/models/Note.js` —— 数据模型

```js
// server/models/Note.js
const { query } = require('../db');

class Note {
  static async create({ title, content }) {
    const result = await query(
      `INSERT INTO notes (title, content, created_at, updated_at)
       VALUES ($1, $2, NOW(), NOW())
       RETURNING id, title, content, created_at, updated_at`,
      [title, content]
    );
    return result.rows[0];
  }

  static async findAll() {
    const result = await query(
      `SELECT id, title, created_at, updated_at FROM notes ORDER BY created_at DESC`
    );
    return result.rows;
  }

  static async findById(id) {
    const result = await query(
      `SELECT * FROM notes WHERE id = $1`,
      [id]
    );
    return result.rows[0];
  }

  static async update(id, { title, content }) {
    const result = await query(
      `UPDATE notes
       SET title = $1, content = $2, updated_at = NOW()
       WHERE id = $3
       RETURNING id, title, content, created_at, updated_at`,
      [title, content, id]
    );
    return result.rows[0];
  }

  static async delete(id) {
    await query(`DELETE FROM notes WHERE id = $1`, [id]);
  }
}

module.exports = Note;
```

### 4. `server/routes/notes.js` —— 路由

```js
// server/routes/notes.js
const express = require('express');
const Note = require('../models/Note');
const marked = require('marked');
const nlp = require('compromise');
const fileUpload = require('express-fileupload');
const router = express.Router();

// 中间件
router.use(fileUpload({
  useTempFiles: true,
  tempFileDir: '/tmp/',
  limits: { fileSize: 5 * 1024 * 1024 }
}));

// 工具函数
function extractText(md) {
  return md
    .replace(/```[\s\S]*?```/g, '')
    .replace(/`[^`]*`/g, '')
    .replace(/!\[.*?\]\(.*?\)/g, '')
    .replace(/\[.*?\]\(.*?\)/g, '')
    .replace(/[^\w\s]/gi, '')
    .trim();
}

// ✅ 1. 检查语法
router.post('/check-grammar', async (req, res) => {
  let text = '';
  if (req.files?.file) {
    text = req.files.file.data.toString('utf8');
  } else if (req.body.content) {
    text = req.body.content;
  } else {
    return res.status(400).json({ error: '请提供文件或 content' });
  }

  try {
    const cleanText = extractText(text);
    if (!cleanText) {
      return res.json({ suggestions: '无文本可检查' });
    }

    const doc = nlp(cleanText);
    const sentences = doc.sentences().out('array');
    const suggestions = sentences
      .filter((_, i) => doc.sentences().item(i).terms().out('array').length > 30)
      .map(sent => ({
        sentence: sent,
        issue: '句子过长',
        suggestion: '建议拆分为两个短句'
      }));

    res.json({
      original: text,
      suggestions: suggestions.length ? suggestions : '语法良好！',
      sentenceCount: sentences.length
    });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// ✅ 2. 保存笔记
router.post('/save-note', async (req, res) => {
  const { title, content } = req.body;
  if (!title || !content) {
    return res.status(400).json({ error: 'title 和 content 为必填' });
  }

  try {
    const note = await Note.create({ title, content });
    res.status(201).json(note);
  } catch (err) {
    res.status(500).json({ error: '保存失败' });
  }
});

// ✅ 3. 列出笔记
router.get('/list-notes', async (req, res) => {
  try {
    const notes = await Note.findAll();
    res.json(notes);
  } catch (err) {
    res.status(500).json({ error: '获取失败' });
  }
});

// ✅ 4. 渲染 HTML
router.get('/render-html/:id', async (req, res) => {
  try {
    const note = await Note.findById(req.params.id);
    if (!note) return res.status(404).json({ error: '未找到' });

    const html = marked.parse(note.content);
    res.json({ ...note, html });
  } catch (err) {
    res.status(500).json({ error: '渲染失败' });
  }
});

module.exports = router;
```

### 5. `server/server.js` —— 主服务

```js
// server/server.js
require('dotenv').config();
const express = require('express');
const cors = require('cors');
const notesRouter = require('./routes/notes');

const app = express();
const PORT = 5000;

app.use(cors());
app.use(express.json());

// 初始化表（首次运行）
const { query } = require('./db');
const initDB = async () => {
  await query(`
    CREATE TABLE IF NOT EXISTS notes (
      id SERIAL PRIMARY KEY,
      title TEXT NOT NULL,
      content TEXT NOT NULL,
      created_at TIMESTAMP DEFAULT NOW(),
      updated_at TIMESTAMP DEFAULT NOW()
    )
  `);
  console.log('✅ 数据表已准备');
};

app.use('/api', notesRouter);

app.listen(PORT, async () => {
  await initDB();
  console.log(`🚀 后端 API 已启动: http://localhost:${PORT}`);
});
```

---

## 💄 第三步：前端实现（React）

```bash
cd client
npx create-react-app .
npm install axios react-router-dom
```

### 1. `client/src/services/api.js`

```js
// client/src/services/api.js
import axios from 'axios';

export const api = axios.create({
  baseURL: 'http://localhost:5000/api'
});
```

### 2. `client/src/components/UploadGrammarCheck.js`

```jsx
// client/src/components/UploadGrammarCheck.js
import React, { useState } from 'react';
import { api } from '../services/api';

export default function UploadGrammarCheck() {
  const [file, setFile] = useState(null);
  const [text, setText] = useState('');
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleFileChange = (e) => setFile(e.target.files[0]);

  const checkGrammar = async () => {
    setLoading(true);
    const formData = new FormData();
    if (file) formData.append('file', file);
    
    try {
      const res = await api.post('/check-grammar', file ? formData : { content: text }, {
        headers: { 'Content-Type': 'multipart/form-data' }
      });
      setResult(res.data);
    } catch (err) {
      setResult({ error: err.response?.data?.error || '检查失败' });
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <h2>📝 语法检查</h2>
      <input type="file" accept=".md" onChange={handleFileChange} />
      <textarea 
        placeholder="或直接输入 Markdown 文本"
        value={text}
        onChange={e => setText(e.target.value)}
        rows="5"
      />
      <button onClick={checkGrammar} disabled={loading}>
        {loading ? '检查中...' : '检查语法'}
      </button>

      {result && (
        <div>
          <h3>结果：</h3>
          <pre>{JSON.stringify(result, null, 2)}</pre>
        </div>
      )}
    </div>
  );
}
```

### 3. `client/src/components/NoteEditor.js`

```jsx
// client/src/components/NoteEditor.js
import React, { useState } from 'react';
import { api } from '../services/api';

export default function NoteEditor({ onSave }) {
  const [title, setTitle] = useState('');
  const [content, setContent] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const res = await api.post('/save-note', { title, content });
      onSave(res.data);
      alert('保存成功！');
    } catch (err) {
      alert('保存失败');
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        placeholder="标题"
        value={title}
        onChange={e => setTitle(e.target.value)}
        required
      />
      <textarea
        placeholder="输入 Markdown 内容"
        value={content}
        onChange={e => setContent(e.target.value)}
        rows="10"
        required
      />
      <button type="submit">💾 保存笔记</button>
    </form>
  );
}
```

### 4. `client/src/components/NoteList.js`

```jsx
// client/src/components/NoteList.js
import React, { useState, useEffect } from 'react';
import { api } from '../services/api';
import { Link } from 'react-router-dom';

export default function NoteList() {
  const [notes, setNotes] = useState([]);

  useEffect(() => {
    api.get('/list-notes').then(res => setNotes(res.data));
  }, []);

  return (
    <div>
      <h2>📚 笔记列表</h2>
      {notes.map(note => (
        <div key={note.id}>
          <Link to={`/note/${note.id}`}>
            <strong>{note.title}</strong>
          </Link>
          <span> - {new Date(note.created_at).toLocaleString()}</span>
        </div>
      ))}
    </div>
  );
}
```

### 5. `client/src/components/NoteViewer.js`

```jsx
// client/src/components/NoteViewer.js
import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import { api } from '../services/api';

export default function NoteViewer() {
  const { id } = useParams();
  const [note, setNote] = useState(null);

  useEffect(() => {
    api.get(`/render-html/${id}`).then(res => setNote(res.data));
  }, [id]);

  if (!note) return <div>加载中...</div>;

  return (
    <div>
      <h1>{note.title}</h1>
      <div dangerouslySetInnerHTML={{ __html: note.html }} />
    </div>
  );
}
```

### 6. `client/src/App.js`

```jsx
// client/src/App.js
import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import UploadGrammarCheck from './components/UploadGrammarCheck';
import NoteEditor from './components/NoteEditor';
import NoteList from './components/NoteList';
import NoteViewer from './components/NoteViewer';

function App() {
  return (
    <Router>
      <div style={{ padding: 20 }}>
        <nav>
          <Link to="/">语法检查</Link> | 
          <Link to="/new">新建笔记</Link> | 
          <Link to="/notes">笔记列表</Link>
        </nav>

        <Routes>
          <Route path="/" element={<UploadGrammarCheck />} />
          <Route path="/new" element={<NoteEditor onSave={() => {}} />} />
          <Route path="/notes" element={<NoteList />} />
          <Route path="/note/:id" element={<NoteViewer />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
```

---

## ▶️ 第四步：运行全栈应用

```bash
# 1. 启动数据库
docker-compose up -d

# 2. 启动后端
cd server
node server.js

# 3. 启动前端
cd client
npm start
```

访问：`http://localhost:3000`

---

## ✅ 功能验证

| 功能 | 状态 |
|------|------|
| 文件上传语法检查 | ✅ |
| 文本输入语法检查 | ✅ |
| 保存笔记到 PostgreSQL | ✅ |
| 列出所有笔记 | ✅ |
| Markdown 渲染为 HTML | ✅ |
| React 前端页面 | ✅ |
| 路由导航 | ✅ |

---

## 🎯 总结

> 你完成了一个**生产级全栈应用**：
> - **前端**：React + 路由 + 表单
> - **后端**：Express + REST API
> - **数据库**：PostgreSQL（持久化）
> - **功能**：文件上传、语法检查、Markdown 渲染

---

📌 **下一步建议**：
- 添加用户认证（JWT）
- 支持笔记编辑与删除
- 使用 Docker 容器化整个应用
- 部署到 Vercel + Railway

这是你迈向**全栈工程师**的关键一步！

---

## ORM

当然可以！**后端完全可以采用 ORM（Object-Relational Mapping）技术来省略手写 SQL 语句**，这不仅能提升开发效率，还能增强代码可维护性和安全性。

---

## ✅ 为什么应该在你的 Markdown 笔记应用中使用 ORM？

你当前的项目结构是：

- **Node.js + Express + PostgreSQL + React**
- 手动写 SQL 语句（如 `INSERT INTO notes ...`）

👉 使用 ORM 后，你可以把这段代码：
```js
await query(
  `INSERT INTO notes (title, content, created_at, updated_at)
   VALUES ($1, $2, NOW(), NOW()) RETURNING *`,
  [title, content]
);
```

替换成这样简洁的 JavaScript 对象操作：
```js
const note = await Note.create({ title, content });
```

无需再写任何 SQL！

---

## 🛠 推荐 ORM：Sequelize（最适合 Node.js + PostgreSQL）

### 🔧 优点：
| 优势 | 说明 |
|------|------|
| ✅ 零 SQL | 所有增删改查通过 JS 方法完成 |
| ✅ 支持 PostgreSQL/MySQL/SQLite | 完美兼容你的技术栈 |
| ✅ 自动模型同步 | `sequelize.sync()` 自动创建表 |
| ✅ 数据验证 | 内置字段校验（非空、长度、格式等） |
| ✅ 关系管理 | 轻松处理“用户-笔记”等关联 |
| ✅ 防止 SQL 注入 | 参数自动转义 |

---

## 🚀 改造步骤：用 Sequelize 替代原生 SQL

### 1. 安装依赖

```bash
cd server
npm install sequelize sequelize-cli pg pg-hstore
npx sequelize-cli init
```

生成目录结构：
```
server/
├── config/
│   └── config.json     # 数据库配置
├── models/             # 模型文件
├── migrations/         # 迁移脚本
└── seeders/
```

---

### 2. 配置数据库连接 `config/config.json`

```json
{
  "development": {
    "username": "noteuser",
    "password": "notepass",
    "database": "notedb",
    "host": "127.0.0.1",
    "dialect": "postgres"
  }
}
```

---

### 3. 创建模型和迁移

```bash
npx sequelize-cli model:generate --name Note --attributes title:string,content:text
```

自动生成：
- `models/note.js` —— 模型定义
- `migrations/xxxx-create-note.js` —— 建表脚本

---

### 4. 修改模型（添加时间字段自动管理）

```js
// models/note.js
module.exports = (sequelize, DataTypes) => {
  const Note = sequelize.define('Note', {
    title: {
      type: DataTypes.STRING,
      allowNull: false
    },
    content: {
      type: DataTypes.TEXT,
      allowNull: false
    }
  }, {
    timestamps: true,        // 自动生成 createdAt 和 updatedAt
    underscored: false       // 使用 camelCase 字段名
  });

  return Note;
};
```

---

### 5. 执行迁移（创建表）

```bash
npx sequelize-cli db:migrate
```

✅ 自动生成并执行 SQL：
```sql
CREATE TABLE "notes" (
  "id" SERIAL PRIMARY KEY,
  "title" VARCHAR(255) NOT NULL,
  "content" TEXT NOT NULL,
  "createdAt" TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  "updatedAt" TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);
```

---

### 6. 在 `server.js` 中初始化 ORM

```js
// server/server.js
const express = require('express');
const { sequelize } = require('./models'); // 自动加载所有模型
const cors = require('cors');
const notesRouter = require('./routes/notes');

const app = express();
const PORT = 5000;

app.use(cors());
app.use(express.json());

// ORM 同步（开发环境可用，生产环境建议用 migrate）
sequelize.sync({ force: false }) // 不覆盖已有数据
  .then(() => console.log('✅ 数据库同步完成'))
  .catch(err => console.error('❌ 数据库同步失败:', err));

app.use('/api', notesRouter);

app.listen(PORT, () => {
  console.log(`🚀 后端 API 已启动: http://localhost:${PORT}`);
});
```

---

### 7. 改造路由：完全移除 SQL

#### 旧代码（含 SQL）：
```js
const { query } = require('../db');
<!--ID: 1761111102063-->


const result = await query(
  `INSERT INTO notes (title, content, created_at, updated_at)
   VALUES ($1, $2, NOW(), NOW())
   RETURNING *`,
  [title, content]
);
```

#### ✅ 新代码（使用 Sequelize ORM）：

```js
// server/routes/notes.js
const { Note } = require('../models'); // 引入模型

// ✅ 1. 保存笔记（无 SQL）
router.post('/save-note', async (req, res) => {
  const { title, content } = req.body;
  if (!title || !content) {
    return res.status(400).json({ error: '必填字段缺失' });
  }

  try {
    const note = await Note.create({ title, content }); // 自动插入，自动管理时间
    res.status(201).json(note);
  } catch (err) {
    res.status(500).json({ error: '保存失败' });
  }
});

// ✅ 2. 获取所有笔记
router.get('/list-notes', async (req, res) => {
  try {
    const notes = await Note.findAll({
      attributes: ['id', 'title', 'createdAt', 'updatedAt'],
      order: [['createdAt', 'DESC']]
    });
    res.json(notes);
  } catch (err) {
    res.status(500).json({ error: '查询失败' });
  }
});

// ✅ 3. 根据 ID 查找
router.get('/render-html/:id', async (req, res) => {
  try {
    const note = await Note.findByPk(req.params.id); // findByPk = find by primary key
    if (!note) return res.status(404).json({ error: '未找到' });

    const html = marked.parse(note.content);
    res.json({ ...note.toJSON(), html }); // toJSON() 转普通对象
  } catch (err) {
    res.status(500).json({ error: '渲染失败' });
  }
});

// ✅ 4. 更新笔记
router.put('/notes/:id', async (req, res) => {
  const { title, content } = req.body;
  try {
    const note = await Note.findByPk(req.params.id);
    if (!note) return res.status(404).json({ error: '未找到' });

    await note.update({ title, content }); // 自动更新 updated_at
    res.json(note);
  } catch (err) {
    res.status(500).json({ error: '更新失败' });
  }
});

// ✅ 5. 删除笔记
router.delete('/notes/:id', async (req, res) => {
  try {
    const deleted = await Note.destroy({ where: { id: req.params.id } });
    if (!deleted) return res.status(404).json({ error: '未找到' });
    res.status(204).send(); // No Content
  } catch (err) {
    res.status(500).json({ error: '删除失败' });
  }
});
```

---

## 🎯 使用 ORM 的好处总结

| 场景 | 原生 SQL | Sequelize ORM |
|------|----------|----------------|
| 插入数据 | 手写 `INSERT INTO ...` | `Note.create(data)` |
| 查询列表 | 手写 `SELECT ... ORDER BY` | `Note.findAll({ order: [...] })` |
| 查单条 | `SELECT * FROM notes WHERE id=?` | `Note.findByPk(id)` |
| 更新 | `UPDATE ... SET ... WHERE id=?` | `note.update(data)` |
| 删除 | `DELETE FROM ...` | `Note.destroy({ where: { id } })` |
| 表结构变更 | 手动写 migration | `npx sequelize migration:create` |
| 安全性 | 需手动参数化 | 自动防 SQL 注入 |
| 可读性 | SQL 混在 JS 中 | 纯 JavaScript 风格 |

---

## 🚫 什么时候不适合用 ORM？

| 场景 | 建议 |
|------|------|
| 极复杂 SQL（多层嵌套、窗口函数） | 直接用 `sequelize.query('复杂SQL')` |
| 高性能批处理 | 手写优化 SQL 或使用原生批量操作 |
| 学习数据库原理 | 先学 SQL，再用 ORM |

> ✅ 但你的项目完全适合 ORM：CRUD 为主，结构清晰。

---

## 📌 最佳实践建议

1. **开发阶段**：用 `sequelize.sync()` 快速建表
2. **生产环境**：用 `migrations` 控制变更，避免数据丢失
3. **字段验证**：在模型中定义 `allowNull: false`, `validate: { len: [1, 255] }`
4. **关联扩展**：未来加用户系统时，轻松实现 `User.hasMany(Note)`

---

## ✅ 总结

> **是的，你可以而且应该在后端使用 ORM 技术来省略 SQL 语句**。

🔧 **Sequelize + PostgreSQL + Express + React** 是一个非常成熟、高效、易维护的全栈组合。

📌 改造完成后，你的代码将变成：

```js
// 全部 CRUD 操作都不见 SQL！
await Note.create(...)
await Note.findAll(...)
await Note.findByPk(...)
await note.update(...)
await Note.destroy(...)
```

这正是现代后端开发的**标准做法**：**专注业务逻辑，而非数据库语法**。

> 🚀 你现在离专业全栈工程师又近了一步！