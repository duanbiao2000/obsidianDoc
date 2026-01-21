import os

# 统计各分类文件夹的文件数
folders = [
    "2.Topics/Coding/语言指南",
    "2.Topics/Coding/系统设计",
    "2.Topics/Coding/AI与大模型",
    "2.Topics/Coding/工程实践",
    "2.Topics/Coding/数据库与存储",
    "2.Topics/认知科学/思维模型",
    "2.Topics/认知科学/学习系统",
    "2.Topics/认知科学/行动协议",
    "2.Topics/个人效能/职业发展",
    "2.Topics/个人效能/生产力系统",
    "2.Topics/个人效能/习惯养成",
    "2.Topics/健康生活/训练协议",
    "2.Topics/健康生活/营养与恢复",
    "2.Topics/写作与英语/写作技巧",
    "2.Topics/写作与英语/英语学习",
    "2.Topics/创业与产品/产品方法论",
    "2.Topics/创业与产品/商业模式",
    "3.Resources/学习资料/学习路径",
    "3.Resources/学习资料/竞赛与准备",
    "3.Resources/日志/趋势预测",
    "3.Resources/日志/周复盘",
    "0.DailyNotes/特殊文件",
]

total = 0
output_lines = []

for folder in folders:
    if os.path.exists(folder):
        count = len([f for f in os.listdir(folder) if f.endswith(".md")])
        output_lines.append(f"{folder}: {count:3d} 个")
        total += count
    else:
        output_lines.append(f"{folder}: 不存在")

output_lines.append("=" * 60)
output_lines.append(f"总计: {total} 个文件")

# 写入文件
with open("file_count.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(output_lines))

print(f"统计完成，共 {total} 个文件，结果已保存到 file_count.txt")
