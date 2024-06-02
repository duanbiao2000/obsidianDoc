#!/usr/bin/env python3

import os

# 读取热词榜文件
hot_words_file = "热词榜top100.md"

# 定义搜索目录和结果保存目录
search_dir = "docs"
output_dir = "hWordComb"

# 创建结果保存目录
os.makedirs(output_dir, exist_ok=True)

# 提示用户搜索和文件生成开始
print("Generating search results from hot words list...")

# 逐行读取热词榜文件，并生成搜索结果文件
with open(hot_words_file, 'r', encoding='utf-8') as f:
    for line in f:
        # 分割词频和关键字
        parts = line.strip().split('\t')
        if len(parts) != 2:
            print(f"Ignoring line: {line.strip()} - Incorrect format")
            continue
        count, keyword = parts
        # 生成搜索结果文件路径
        output_file = os.path.join(output_dir, f"{keyword}.md")
        # 执行 grep 搜索并保存结果到文件
        os.system(f"grep -nri '{keyword}' {search_dir} > {output_file}")
        # 提示文件生成完毕
        print(f"Generation of {output_file} complete.")

# 提示用户结果已保存
print("Search results saved.")

# 添加暂停，以便用户查看输出
input("Press [Enter] key to exit...")
