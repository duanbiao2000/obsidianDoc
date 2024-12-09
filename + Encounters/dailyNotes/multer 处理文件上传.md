---
aliases: 
<<<<<<< HEAD
theme: 
priority: false
=======
categories: 
high_priority: false
>>>>>>> 93a933e (refactor(dailyNotes): update metadata structure for daily notes)
tags:
---
在MERN（MongoDB, Express, React, Node.js）项目中，`multer` 是一个常用的Node.js中间件，用于处理文件上传。它主要用于解析通过`multipart/form-data`格式提交的表单数据，这是HTML表单上传文件时使用的标准格式。

### `multer` 的主要作用包括：

1. **文件上传**：
   - `multer` 可以将用户上传的文件保存到服务器上的指定目录。
   - 它还可以将文件存储在内存中，适用于小文件或临时文件。

2. **文件过滤**：
   - 你可以配置 `multer` 来限制允许上传的文件类型、大小等。
   - 例如，只允许上传图片文件，并且设置最大文件大小。

3. **重命名文件**：
   - `multer` 允许你自定义文件名，这样可以避免文件名冲突，或者根据需要对文件进行命名。

4. **错误处理**：
   - 如果文件上传过程中出现问题（如文件过大），`multer` 会抛出错误，你可以捕获这些错误并进行相应的处理。

### 基本用法

以下是一个简单的例子，展示了如何在Express应用中使用 `multer` 来处理文件上传：

```javascript
const express = require('express');
const multer = require('multer');

const app = express();

// 设置存储引擎
const storage = multer.diskStorage({
    destination: function (req, file, cb) {
        cb(null, 'uploads/')  // 保存文件的目录
    },
    filename: function (req, file, cb) {
        cb(null, Date.now() + '-' + file.originalname)  // 文件名
    }
});

// 创建multer实例
const upload = multer({ storage: storage });

// 单文件上传路由
app.post('/upload', upload.single('file'), (req, res) => {
    try {
        // req.file 包含上传的文件信息
        res.send('File uploaded successfully.');
    } catch (error) {
        res.status(500).send(error.message);
    }
});

// 多文件上传路由
app.post('/upload-multiple', upload.array('files', 10), (req, res) => {
    try {
        // req.files 包含上传的所有文件信息
        res.send('Files uploaded successfully.');
    } catch (error) {
        res.status(500).send(error.message);
    }
});

app.listen(3000, () => {
    console.log('Server is running on port 3000');
});
```

在这个例子中：

- `multer.diskStorage` 用于配置文件存储的位置和文件名。
- `upload.single('file')` 用于处理单个文件上传，其中 `'file'` 是前端表单字段的名称。
- `upload.array('files', 10)` 用于处理多个文件上传，最多允许上传10个文件。

### 集成到MERN项目

在MERN项目中，通常后端（Node.js + Express）使用 `multer` 来处理文件上传，然后将文件路径或其他相关信息存储在MongoDB数据库中。前端（React）则负责构建文件上传表单，并发送请求到后端API。

这样，`multer` 就成为了连接前后端的关键组件，确保文件能够顺利从客户端上传到服务器，并被正确地处理和存储。