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