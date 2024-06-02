import os

# 设置你的Markdown文件所在的目录
directory = "./"
# 设置输出文件的路径
output_file = "Summary.md"

# 创建Markdown文件并写入基础内容
with open(output_file, 'w',  encoding='utf-8') as md_file:
    md_file.write("# Summary\n\n")
    for chapter in os.listdir(directory):
        chapter_path = os.path.join(directory, chapter)
        if os.path.isdir(chapter_path):
            md_file.write(f"## {chapter}\n")
            for file in os.listdir(chapter_path):
                if file.endswith(".md"):
                    file_path = os.path.join(chapter, file)
                    md_file.write(f"- [{file[:-3]}]({file_path})\n")

# 打印完成信息
print(f"{output_file} has been created.")