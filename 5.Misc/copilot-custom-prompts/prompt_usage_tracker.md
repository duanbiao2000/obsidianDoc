<%*
/**
 * 提示词使用追踪器
 *
 * 功能：记录 Copilot 提示词的使用情况
 * 使用方法：在调用提示词前使用此模板
 * 创建时间：2026-01-26
 * 相关：知识库优化线路图 P1 - Copilot 提示词库持续优化
 */
-%>

<%*
// 获取当前提示词信息
const currentFile = tp.file.findTFile();
const currentDate = tp.date.now('YYYY-MM-DD');
const currentTime = tp.date.now('HH:mm:ss');

// 提取提示词名称（文件名，去掉扩展名）
const promptName = currentFile.basename;

// 查找或创建使用统计文件
const statsFile = app.vault.getAbstractFileByPath('5.Misc/copilot-custom-prompts/usage_stats.json');

if (!statsFile) {
  // 如果统计文件不存在，创建新的
  const newStats = {
    "version": "1.0",
    "created_at": currentDate + ' ' + currentTime,
    "last_updated": currentDate + ' ' + currentTime,
    "prompts": {}
  };
  newStats.prompts[promptName] = {
    "first_used": currentDate + ' ' + currentTime,
    "last_used": currentDate + ' ' + currentTime,
    "usage_count": 1,
    "notes": [""]
  };

  await app.vault.create('5.Misc/copilot-custom-prompts/usage_stats.json', JSON.stringify(newStats, null, 2));
} else {
  // 读取现有统计
  const content = await app.vault.read(statsFile);
  const stats = JSON.parse(content);

  // 更新当前提示词的使用统计
  if (!stats.prompts[promptName]) {
    stats.prompts[promptName] = {
      "first_used": currentDate + ' ' + currentTime,
      "last_used": currentDate + ' ' + currentTime,
      "usage_count": 1,
      "notes": [""]
    };
  } else {
    stats.prompts[promptName].last_used = currentDate + ' ' + currentTime;
    stats.prompts[promptName].usage_count += 1;
  }

  // 添加使用笔记（可选，需要用户输入）
  const noteContent = await tp.system.prompt('使用此提示词的目的或场景（可选）', '', false);
  if (noteContent && noteContent.trim() !== '') {
    stats.prompts[promptName].notes.push({
      "timestamp": currentDate + ' ' + currentTime,
      "note": noteContent
    });
  }

  stats.last_updated = currentDate + ' ' + currentTime;

  // 保存更新后的统计
  await app.vault.modify(statsFile, JSON.stringify(stats, null, 2));
}

// 输出确认
tR += `✅ 使用记录已更新：${promptName}
  次数：${stats.prompts[promptName]?.usage_count || 1}
  最后使用：${stats.prompts[promptName]?.last_used || currentDate + ' ' + currentTime}`;
-%>

---
## 使用指南

### 手动记录使用
1. 在调用提示词后，在命令面板中输入 `/prompt-usage-tracker`
2. 填写使用目的或场景（可选）
3. 系统会自动更新使用统计

### 自动化集成（推荐）
可以将此脚本集成到常用提示词的 YAML frontmatter 中：

```yaml
---
copilot-usage-tracker: true
---
```

然后在 Templater 设置中配置自动触发。

### 查看使用统计
打开 `5.Misc/copilot-custom-prompts/usage_stats.json` 查看详细统计，或使用 Dataview 查询：

```dataview
TABLE file.link as "提示词", usage_count as "使用次数", last_used as "最后使用"
FROM "5.Misc/copilot-custom-prompts"
WHERE usage_count
SORT usage_count DESC
LIMIT 20
```

---

## 数据结构

```json
{
  "version": "1.0",
  "created_at": "2026-01-26 17:00:00",
  "last_updated": "2026-01-26 17:30:00",
  "prompts": {
    "KM-笔记重构": {
      "first_used": "2026-01-20 10:30:00",
      "last_used": "2026-01-26 15:20:00",
      "usage_count": 15,
      "notes": [
        {
          "timestamp": "2026-01-26 15:20:00",
          "note": "优化项目笔记结构"
        }
      ]
    }
  }
}
```

---

## 相关链接

- [提示词质量评估标准](./提示词质量评估标准.md)
- [Copilot提示词分类索引](./Copilot提示词分类索引.md)
- [5.Misc/_Index_of_5.Misc](../../_Index_of_5.Misc.md)
