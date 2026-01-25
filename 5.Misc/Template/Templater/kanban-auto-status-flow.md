---
tags:
  - automation
  - templater
  - kanban
  - task-management
  - Type/Template
  - automation
  - templater
  - kanban
  - task-management
  - automation
  - templater
  - kanban
  - task-management
  - Type/Template
  - automation
  - templater
  - kanban
  - task-management
  - automation
  - templater
  - kanban
  - task-management
  - Type/Template
  - automation
  - templater
  - kanban
  - task-management
  - automation
  - templater
  - kanban
  - task-management
  - Type/Template
  - automation
  - templater
  - kanban
  - task-management
  - automation
  - templater
  - kanban
  - task-management
  - Type/Template
  - automation
  - templater
  - kanban
  - task-management
  - automation
  - templater
  - kanban
  - task-management
  - Type/Template
  - automation
  - templater
  - kanban
  - task-management
  - automation
  - templater
  - kanban
  - task-management
  - Type/Template
  - automation
  - templater
  - kanban
  - task-management
  - automation
  - templater
  - kanban
  - task-management
  - Type/Template
  - automation
  - templater
  - kanban
  - task-management
---
# Kanban自动化脚本

## 一、自动状态流转脚本

### `kanban-auto-status-flow.md`

<%*
// 自动状态流转脚本 - 基于依赖关系和时间触发状态更新
const kanbanFile = tp.file.find_tfile("Atlas/kanban");
const taskRegex = /-\s*\[(?<checkbox>[ x])\]\s*(?<title>.+?)\s*(?:\|\s*(?<details>.+?))?\s*(?:✅\s*(?<date>.+?))?$/gm;

// 获取当前看板内容
let content = await app.vault.read(kanbanFile);
let match;
let tasks = [];

// 解析所有任务
while ((match = taskRegex.exec(content)) !== null) {
    tasks.push({
        checkbox: match.groups.checkbox,
        title: match.groups.title,
        details: match.groups.details || "",
        date: match.groups.date || null,
        complete: match.groups.checkbox === 'x'
    });
}

// 状态流转规则
function checkStatusFlow(task) {
    // 规则1: 完成的任务自动移动到Archive
    if (task.complete && task.date) {
        // 检查是否已经在Archive列
        const lineIndex = content.indexOf(task.title);
        const roadMapIndex = content.indexOf("## ARCHIVE");
        return lineIndex < roadMapIndex;
    }

    // 规则2: 依赖任务完成后自动激活后续任务
    if (task.details.includes("依赖：") && !task.complete) {
        const dependencyTask = task.details.match(/依赖：(.*?)】/)?.[1];
        const dependencyComplete = tasks.some(t =>
            t.title.includes(dependencyTask) && t.complete
        );
        return dependencyComplete;
    }

    return false;
}

// 应用状态流转
tasks.forEach(task => {
    if (checkStatusFlow(task)) {
        // 执行状态流转逻辑
        console.log(`需要流转任务: ${task.title}`);
    }
});

// 更新文件（在实际应用中）
// await app.vault.modify(kanbanFile, newContent);
%>
