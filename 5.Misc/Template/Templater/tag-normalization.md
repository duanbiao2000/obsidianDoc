---
description: 标签规范化脚本 - 用于当前文件的标签替换
---
<%*
// ============================================================
// 标签规范化 Templater 脚本
// GitHub Issue #1: https://github.com/duanbiao2000/obsidianDoc/issues/1
//
// 使用方法:
// 1. 在 Obsidian 中打开需要处理的文章
// 2. 运行此 Templater 脚本
// 3. 选择要执行的操作
// ============================================================

// 标签映射表
const tagMappings = {
    // 删除无效标签
    "#Domain/<SubDomain>": null,
    "#Status/<State>": null,
    "#Type/<ContentType>": null,
    "#Domain/": null,
    "#Type/": null,
    "#Status/": null,
    "#6f9": null,
    "#333": null,
    "#SpecDriven": null,

    // Domain 标签映射（高优先级）
    "#AI": "#Domain/AI",
    "#Domain/Cognition": "#Domain/Cognitive",

    // Status 标签映射（高优先级）
    "#todo": "#Status/TODO",
    "#done": "#Status/Done",

    // Type 标签映射（高优先级）
    "#note": "#Type/Note",
    "#Project": "#Type/Project",
    "#MOC": "#Type/MOC",
    "#reference": "#Type/Reference",
    "#permanent-note": "#Type/Note",

    // Domain 标签映射（中优先级）
    "#Domain/CognitiveSystem": "#Domain/Cognitive",
    "#Domain/ContentCreation": "#Domain/Content",
    "#SubDomain/IELTS": "#Domain/Language/IELTS",
    "#ContentCreation": "#Domain/Content",
    "#card": "#Type/Card",

    // Domain 标签映射（低优先级）
    "#Python": "#Domain/Technology/Python",
    "#Architecture": "#Domain/TechStack/SystemDesign",
    "#SystemDesign": "#Domain/TechStack/SystemDesign",
    "#Tech/AI": "#Domain/AI",
    "#OpenSource": "#Domain/Technology/OpenSource",
    "#Domain/Psychology": "#Domain/Cognitive/Psychology",
    "#Domain/MentalModel": "#Domain/Cognitive/MentalModel",
    "#Concurrency": "#Domain/TechStack/Concurrency",
    "#CloudNative": "#Domain/TechStack/CloudNative",
    "#CareerPlanning": "#Domain/Career/Planning",
    "#EngineeringMindset": "#Domain/Career/Engineering",
};

// 统计信息
let stats = {
    deletedTags: 0,
    replacedTags: 0,
    modifications: [],
};

// 获取文件内容
let content = await app.vault.read(this.file);
let originalContent = content;

// 执行标签替换
for (const [oldTag, newTag] of Object.entries(tagMappings)) {
    // 使用正则表达式进行全局替换
    const pattern = new RegExp(`\\b${oldTag.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')}\\b`, 'g');
    const matches = content.match(pattern);

    if (matches && matches.length > 0) {
        if (newTag === null) {
            // 删除标签
            content = content.replace(pattern, '');
            stats.deletedTags += matches.length;
            stats.modifications.push({
                action: 'delete',
                tag: oldTag,
                count: matches.length,
            });
        } else {
            // 替换标签
            content = content.replace(pattern, newTag);
            stats.replacedTags += matches.length;
            stats.modifications.push({
                action: 'replace',
                oldTag: oldTag,
                newTag: newTag,
                count: matches.length,
            });
        }
    }
}

// 清理多余的空行
content = content.replace(/\n\s*\n\s*\n/g, '\n\n');

// 如果有修改，写回文件
if (content !== originalContent) {
    await app.vault.modify(this.file, content);

    // 输出统计信息
    tR += `## ✅ 标签规范化完成\n\n`;
    tR += `**文件**: ${this.file.path}\n\n`;
    tR += `### 📊 统计信息\n`;
    tR += `- 删除标签: ${stats.deletedTags} 次\n`;
    tR += `- 替换标签: ${stats.replacedTags} 次\n`;
    tR += `- 总修改数: ${stats.modifications.length} 项\n\n`;

    if (stats.modifications.length > 0) {
        tR += `### 📝 详细修改\n`;
        for (const mod of stats.modifications) {
            if (mod.action === 'delete') {
                tR += `- ❌ 删除 \`${mod.tag}\` (${mod.count}次)\n`;
            } else {
                tR += `- 🔄 \`${mod.oldTag}\` → \`${mod.newTag}\` (${mod.count}次)\n`;
            }
        }
    }

    tR += `\n---\n`;
    tR += `*执行时间: ${new Date().toLocaleString('zh-CN')}*\n`;
} else {
    tR += `## ℹ️ 无需修改\n\n`;
    tR += `当前文件未发现需要规范化的标签。\n\n`;
    tR += `---\n`;
    tR += `*检查时间: ${new Date().toLocaleString('zh-CN')}*\n`;
}
%>
