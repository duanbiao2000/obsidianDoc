以下是一个完整的自动化方案，基于 Obsidian + Templater + AnkiConnect 插件，实现从日卡/周卡笔记中：

1. **提取卡片内容**
    
2. **分类归档（上广深）**
    
3. **生成 Anki 卡片模板**
    
4. **一键推送到 Anki**
    
5. **标记已同步状态**
    

---

### 一、前置要求

- Obsidian 已安装：
    
    - [Templater](https://github.com/SilentVoid13/Templater)
        
    - [Dataview](https://github.com/blacksmithgu/obsidian-dataview)
        
- 本地安装并运行 [Anki + AnkiConnect](https://foosoft.net/projects/anki-connect/)（Anki 插件商店搜索安装）
    
- Anki 中已创建名为 `上广深` 的牌组
    
- 可选：使用 Tag 或 frontmatter 标记卡片已同步
    

---

### 二、Obsidian 模板内容（用于 Templater 触发）

**文件名：`生成Anki卡片.md`**

```javascript
<%*
const noteContent = await tp.file.read();
const lines = noteContent.split("\n");

// 筛选出卡片内容行（可使用自定义标记，例如 %%card%%）
const cardLines = lines.filter(l => l.trim().startsWith("%%card%%"));

// 分类上/广/深
const cards = {
  上: [],
  广: [],
  深: []
};

cardLines.forEach(line => {
  const content = line.replace("%%card%%", "").trim();
  const match = content.match(/^(\[上\]|\[广\]|\[深\])(.+)/);
  if (match) {
    const cat = match[1].replace(/\[|\]/g, "");
    const body = match[2].trim();
    cards[cat].push(body);
  }
});

// 推送卡片到 Anki（通过 REST 调用 AnkiConnect）
const fetch = require("node-fetch");
const pushCard = async (front, back) => {
  const res = await fetch("http://localhost:8765", {
    method: "POST",
    body: JSON.stringify({
      action: "addNote",
      version: 6,
      params: {
        note: {
          deckName: "上广深",
          modelName: "Basic",
          fields: { Front: front, Back: back },
          options: { allowDuplicate: false },
          tags: ["上广深"],
        },
      }
    }),
    headers: { "Content-Type": "application/json" }
  });
  return await res.json();
};

// 遍历生成并推送
for (const [cat, list] of Object.entries(cards)) {
  for (const item of list) {
    const [front, back] = item.split("::").map(s => s.trim());
    if (front && back) {
      await pushCard(`[${cat}] ${front}`, back);
    }
  }
}

// 在笔记末尾添加同步标记
await tp.file.append("\n\n✅ 已同步至 Anki: <% tp.date.now("YYYY-MM-DD HH:mm") %>");
-%>
```

---

### 三、如何使用

1. 在你的日卡/周卡中，添加如下格式：
    

```
%%card%% [上] 主动学习的核心理念 :: 是用行动驱动认知
%%card%% [广] 不同学习系统比较 :: 示例：费曼技巧 vs PQ4R
%%card%% [深] 为什么卡片学习法有效 :: 有助于刻意练习与连接构建
```

2. 打开该日卡或周卡，执行 `Templater: Insert template`，选择 `生成Anki卡片`
    
3. 执行后将：
    
    - 自动识别 `[上]`、`[广]`、`[深]` 的卡片
        
    - 推送到 Anki 的 `上广深卡片` 牌组
        
    - 在笔记末尾追加一行 ✅ 标记已同步
        

---

### 四、Anki 卡片样式优化（选配）

可在 Anki 中编辑“Basic”卡片模板的 HTML/CSS，加入层次感与高亮：

```css
.card {
  font-family: "Helvetica Neue", sans-serif;
  font-size: 18px;
  line-height: 1.6;
  color: #333;
  background-color: #f9f9f9;
}

.cloze {
  font-weight: bold;
  border-bottom: 2px dashed #28bea0;
  transition: background-color 0.3s ease;
}

.cloze:hover {
  background-color: #e0f7f1;
}
```

---

如果你想进一步让这个流程支持定时自动同步（如每天早上扫描并推送），可以借助插件如 [Obsidian Tasks](https://github.com/obsidian-tasks-group/obsidian-tasks) 或外部脚本配合 cron。

需要我为你封装这个流程成按钮 / 命令 palette 插件项也可以说一声。是否还希望加一个 Dataview 视图来展示哪些卡片还未同步？