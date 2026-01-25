---
tags:
  - Type/Code
  - templater-script
description: 项目活跃度监控脚本 - 集成到 Weekly Review
---

# 项目活跃度监控 (Templater Script)

<%*
/**
 * 项目活跃度监控脚本
 * 用途：在 Weekly Review 中自动检查项目活跃度，生成归档提醒
 * 使用：将此脚本添加到 Weekly Review 模板中
 */

// 获取当前日期
const today = moment();
const daysThreshold = 90; // 不活跃阈值（天）
const warningThreshold = Math.floor(daysThreshold * 0.7); // 预警阈值（63天）

// 扫描 1.Projects/ 目录
const projectsFolder = '1.Projects';
const projectFiles = app.vault.getMarkdownFiles()
    .filter(f => f.path.startsWith(projectsFolder))
    .filter(f => !f.path.includes('_Index_'))  // 排除索引文件
    .filter(f => !f.path.includes('CLAUDE.md')); // 排除说明文件

// 分类项目
const inactiveProjects = [];     // 超过 90 天未更新
const warningProjects = [];      // 63-90 天未更新
const activeProjects = [];       // 活跃项目
const noUpdateProjects = [];     // 无 update 字段

// 解析文件元数据
for (const file of projectFiles) {
    const cache = app.metadataCache.getFileCache(file);

    if (!cache || !cache.frontmatter) {
        noUpdateProjects.push({
            path: file.path,
            name: file.basename
        });
        continue;
    }

    const updateDateStr = cache.frontmatter['update'];
    const updateDate = moment(updateDateStr, 'YYYY-MM-DD', true);

    if (!updateDate.isValid()) {
        noUpdateProjects.push({
            path: file.path,
            name: file.basename
        });
        continue;
    }

    const daysInactive = today.diff(updateDate, 'days');
    const project = {
        path: file.path,
        name: file.basename,
        updateDate: updateDate.format('YYYY-MM-DD'),
        daysInactive: daysInactive
    };

    if (daysInactive >= daysThreshold) {
        inactiveProjects.push(project);
    } else if (daysInactive >= warningThreshold) {
        warningProjects.push(project);
    } else {
        activeProjects.push(project);
    }
}

// 生成报告
tR += `\n`;
tR += `## 📊 项目活跃度监控\n`;
tR += `\n`;
tR += `**检查日期**: ${today.format('YYYY-MM-DD')}\n`;
tR += `**不活跃阈值**: ${daysThreshold} 天\n`;
tR += `\n`;
tR += `### 统计摘要\n`;
tR += `\n`;
tR += `- 🟢 **活跃项目**: ${activeProjects.length} 个\n`;
tR += `- 🟡 **预警项目** (${warningThreshold}天未更新): ${warningProjects.length} 个\n`;
tR += `- 🔴 **不活跃项目** (超过${daysThreshold}天): ${inactiveProjects.length} 个\n`;
tR += `- ⚪ **无元数据**: ${noUpdateProjects.length} 个\n`;
tR += `\n`;

// 不活跃项目（需要归档）
if (inactiveProjects.length > 0) {
    tR += `### 🔴 需要归档的项目\n`;
    tR += `\n`;
    tR += `以下项目超过 ${daysThreshold} 天未更新，建议归档到 \`4.Archives/Projects/\`：\n`;
    tR += `\n`;

    // 按不活跃天数排序
    inactiveProjects.sort((a, b) => b.daysInactive - a.daysInactive);

    for (const project of inactiveProjects) {
        // 生成归档任务（使用 Tasks 插件语法）
        tR += `- [ ] [[${project.path}]] - 归档到 Archives (最后更新: ${project.updateDate}, ${project.daysInactive}天前)\n`;
    }
    tR += `\n`;
}

// 预警项目
if (warningProjects.length > 0) {
    tR += `### 🟡 预警项目\n`;
    tR += `\n`;
    tR += `以下项目接近 ${daysThreshold} 天阈值，需要关注：\n`;
    tR += `\n`;

    warningProjects.sort((a, b) => b.daysInactive - a.daysInactive);

    for (const project of warningProjects) {
        tR += `- **[[${project.path}]]** - 更新于 ${project.updateDate} (${project.daysInactive}天前)\n`;
    }
    tR += `\n`;
}

// 活跃项目（可选显示）
if (activeProjects.length > 0 && activeProjects.length <= 10) {
    tR += `### 🟢 活跃项目\n`;
    tR += `\n`;
    tR += `以下项目最近有更新：\n`;
    tR += `\n`;

    activeProjects.sort((a, b) => b.daysInactive - a.daysInactive);

    for (const project of activeProjects) {
        tR += `- **[[${project.path}]]** - 更新于 ${project.updateDate}\n`;
    }
    tR += `\n`;
}

// 无元数据项目
if (noUpdateProjects.length > 0) {
    tR += `### ⚪ 需要补充元数据\n`;
    tR += `\n`;
    tR += `以下项目缺少 \`update\` 字段：\n`;
    tR += `\n`;

    for (const project of noUpdateProjects) {
        tR += `- [[${project.path}]]\n`;
    }
    tR += `\n`;
}

// 下一步行动
tR += `### 📝 下一步行动\n`;
tR += `\n`;

if (inactiveProjects.length > 0) {
    tR += `1. **立即归档**: 将 ${inactiveProjects.length} 个不活跃项目移动到 \`4.Archives/Projects/\`\n`;
    tR += `2. **更新索引**: 修改 \`1.Projects/_Index_of_1.Projects.md\`\n`;
}

if (noUpdateProjects.length > 0) {
    tR += `3. **补充元数据**: 为 ${noUpdateProjects.length} 个项目添加 \`update\` 字段\n`;
}

if (warningProjects.length > 0) {
    tR += `4. **关注预警**: ${warningProjects.length} 个项目即将不活跃，需要确认是否继续\n`;
}

tR += `\n`;
tR += `---\n`;
tR += `\n`;
%>
