明白了，以下是一个支持 Cloze 填空题型的完整 Templater 脚本，可用于从 Obsidian 笔记中提取内容并通过 AnkiConnect 自动推送为 Cloze 卡片，同时标记为已同步：

### 1. Obsidian 笔记格式（支持 Templater 变量解析）

```markdown
## Card
Question:: {{c1::Obsidian 是什么？}}
Tags:: #anki/上
```

---

### 2. Templater 脚本（`templates/add-cloze-to-anki.js`）

```javascript
<%*
const noteRegex = /Question::\s*(.+)\nTags::\s*(.+)/g;
const fileContent = await tp.file.content();

let match;
let results = [];

while ((match = noteRegex.exec(fileContent)) !== null) {
  const question = match[1].trim();
  const tags = match[2].trim().replace(/#/g, '').split(/[\/\s,]+/).join(' ');

  const payload = {
    "action": "addNote",
    "version": 6,
    "params": {
      "note": {
        "deckName": "上广深卡片",
        "modelName": "Cloze",
        "fields": {
          "Text": question,
          "Extra": ""
        },
        "options": {
          "allowDuplicate": false
        },
        "tags": [tags],
        "audio": [],
        "video": [],
        "picture": []
      }
    }
  };

  const response = await app.plugins.plugins["templater-obsidian"].functions.run_js_code(`
    fetch("http://localhost:8765", {
      method: "POST",
      body: JSON.stringify(${JSON.stringify(payload)})
    }).then(res => res.json())
  `);

  results.push(response);
}

// 添加“已同步”标志
await tp.file.append("\n\n✅ 已同步至 Anki");
-%>
```

---

### 3. 运行方式

- 放在 Templater 模板文件夹中，例如：`templates/add-cloze-to-anki.js`
    
- 在 Obsidian 中运行命令：**Templater: Insert template**
    
- 或绑定快捷键，实现一键同步
    

---

### 注意事项

- **AnkiConnect** 插件需运行且监听端口 `8765`
    
- Cloze 填空需使用 `{{c1::...}}` 的格式
    
- `modelName: "Cloze"` 必须确保你的 Anki 模板支持 Cloze
    

如需进一步扩展（如自动分类 deck 或 cloze 多段处理），我也可以继续优化。是否需要嵌套多个 cloze 自动编号支持？