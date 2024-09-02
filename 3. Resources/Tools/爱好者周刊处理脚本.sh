#!/bin/bash

# 克隆仓库并进入文档目录
#git clone https://github.com/ruanyf/weekly.git
cd weekly/docs

# 合并所有以 issue-2 开头的 md 文件为一个 weekly.md 文件，并放在上上一级目录
#cat issue-2??.md > ../../weekly_$(date +'%Y%m%d_%H%M%S').md
cat issue-*.md > ../../weekly_$(date +'%Y%m%d_%H%M%S').md
# 去除空行和开头空格
sed -i '/^$/d' ../../weekly_*.md
sed -i 's/^[[:space:]]*//' ../../weekly_*.md

# 删除带有图片的行
sed -i '/^!\[\]/d' ../../weekly_*.md

# 删除回顾到完的内容
sed -i '/## 回顾/,/（完）/d' ../../weekly_*.md

# 删除包含 iframe 的内容
sed -i '/<iframe/,/<\/iframe>/d' ../../weekly_*.md

# 删除链接
#sed -i 's/(https[^)]*)//g' ../../weekly_*.md
sed -i 's/(\(https\?\)[^)]*)//g' ../../weekly_*.md
sed -i 's/[][]//g' ../../weekly_*.md

# 提示用户结果已保存
echo "Weekly.md file generated."

# 添加暂停，以便用户查看输出
read -p "Press [Enter] key to exit..."
