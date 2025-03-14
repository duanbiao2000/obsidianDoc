// 获取所有符合条件的笔记
const notes = dv.pages(
    '-"4. Archives" -"Extras" || #todo' // 筛选条件：排除文件夹或包含标签
).filter(note => note.high_priority === false); // 过滤 high_priority 为 false 的笔记 [[10]]

// 随机打乱笔记顺序
const shuffledNotes = notes.sort(() => Math.random() - 0.5);

// 显示前 10 条笔记
dv.table(
    ["笔记名称", "创作日期"], // 表格列标题
    shuffledNotes.slice(0, 10).map(note => [
        note.file.name, // 笔记名称
        note.file.ctime // 创作日期
    ])
);
