---
tags:
  - automation
  - templater
  - kanban
  - priority-management
---

# 优先级动态调整脚本

### `kanban-priority-adjustment.md`

<%*
// 优先级动态调整脚本 - 基于时间紧迫度和依赖关系自动调整优先级
const today = new Date();
const oneWeekFromNow = new Date(today.getTime() + 7 * 24 * 60 * 60 * 1000);

// 优先级矩阵
const priorityMatrix = {
    '★★★★★': { urgency: 7, importance: 10 },
    '★★★★☆': { urgency: 5, importance: 8 },
    '★★★☆☆': { urgency: 3, importance: 6 },
    '★★☆☆☆': { urgency: 2, importance: 4 },
    '★☆☆☆☆': { urgency: 1, importance: 2 }
};

// 计算动态优先级
function calculateDynamicPriority(task) {
    let urgencyScore = 0;
    let importanceScore = task.priorityMatrix?.importance || 5;
    let dependencyScore = 0;

    // 1. 紧急程度评分 (40%)
    if (task.details?.includes("小时 |")) {
        const hours = parseInt(task.details.match(/(\d+)h/)?.[1] || 0);
        if (hours <= 4) urgencyScore = 10;
        else if (hours <= 8) urgencyScore = 8;
        else if (hours <= 16) urgencyScore = 6;
        else urgencyScore = 4;
    }

    // 2. 依赖关系影响 (20%)
    if (task.details?.includes("依赖：")) {
        dependencyScore = 8; // 有依赖关系的任务提升优先级
    }

    // 3. 时间压力 (20%)
    if (task.date) {
        const taskDate = new Date(task.date);
        const daysUntil = Math.ceil((taskDate - today) / (1000 * 60 * 60 * 24));
        if (daysUntil <= 1) urgencyScore = 10;
        else if (daysUntil <= 3) urgencyScore = 8;
        else if (daysUntil <= 7) urgencyScore = 6;
    }

    // 综合计算
    const dynamicPriority =
        urgencyScore * 0.4 +
        importanceScore * 0.3 +
        dependencyScore * 0.2 +
        (task.isBlocking ? 10 : 0) * 0.1;

    return Math.round(dynamicPriority);
}

// 智能优先级调整建议
function generatePrioritySuggestion(task) {
    const currentPriority = task.priority || '★★☆☆☆';
    const newPriority = calculateDynamicPriority(task);

    let suggestion = "";
    if (newPriority > 8) {
        suggestion = "🔴 建议提升到 ★★★★★";
    } else if (newPriority > 6 && currentPriority !== '★★★★☆') {
        suggestion = "🟠 建议提升到 ★★★★☆";
    } else if (newPriority < 3 && currentPriority !== '★☆☆☆☆') {
        suggestion = "🟢 可降级到 ★☆☆☆☆";
    }

    return suggestion;
}

// 输出优先级分析
const tasks = tp.config.target_file_tasks || [];
console.log("=== 优先级分析报告 ===");

tasks.forEach(task => {
    const suggestion = generatePrioritySuggestion(task);
    if (suggestion) {
        console.log(`${task.title}: ${suggestion}`);
    }
});
%>

## 优先级分析结果

<%*
// 在看板中显示优先级建议
const currentDate = tp.date.now("YYYY-MM-DD");
%>

**最后分析时间**：<%= currentDate %>

### 🔴 高优先级任务
- 紧急度高（< 8小时）且未完成的任务
- 依赖任务已完成的阻塞任务

### 🟠 中优先级任务
- 本周内需要完成的任务
- 有依赖关系但依赖未完成的任务

### 🟢 低优先级任务
- 没有明确截止日期的任务
- 可以延后处理的项目

---

## 使用说明

1. **自动触发**：在每次打开看板时自动运行优先级分析
2. **手动触发**：使用 Templater 命令手动运行优先级分析
3. **结果展示**：在看板中显示优先级建议标签

---

## 配置选项

```yaml
priority_analysis:
  auto_trigger: true          # 自动触发优先级分析
  urgency_weight: 0.4         # 紧急程度权重
  importance_weight: 0.3      # 重要程度权重
  dependency_weight: 0.2      # 依赖关系权重
  blocking_weight: 0.1        # 阻塞影响权重
```
