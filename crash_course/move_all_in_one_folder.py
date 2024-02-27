import os
import shutil

# 源文件夹路径（包含所有子文件夹）
source_folder = r'D:\crashCourse\tmp'

# 目标文件夹路径（所有子文件夹中的文件将被移动到这个文件夹）
destination_folder = r'D:\crashCourse\10分钟速成课：统计学'

# 确保目标文件夹存在，如果不存在则创建它
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# 遍历源文件夹中的所有子文件夹
for root, dirs, files in os.walk(source_folder):
    for file in files:
        # 源文件的完整路径
        source_file_path = os.path.join(root, file)

        # 将文件移动到目标文件夹中
        shutil.move(source_file_path, destination_folder)

print("所有子文件夹中的文件已经成功移动到目标文件夹中！")
