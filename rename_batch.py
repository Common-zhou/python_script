"""
批量重命名，主要用于去除广告
递归重命名
"""
import os

path = r"D:\crashCourse\10分钟速成课：学习技能"
old_str = "1-"
replace_str = ""


def recursive_enter(need_rename_path):
    # 检验给出的路径是否是一个文件：os.path.isfile()

    # 检验给出的路径是否是一个目录：os.path.isdir()
    # 获取路径名：os.path.dirname()
    # 获取文件名：os.path.basename()
    if (not os.path.exists(need_rename_path)):
        # 路径不存在 溜溜球
        print(need_rename_path + " not exist!")
        return
    parent_path = os.path.dirname(need_rename_path)
    file_name = os.path.basename(need_rename_path)

    replace_file_name = file_name.replace(old_str, replace_str)
    new_parent_path = parent_path + "/" + replace_file_name

    os.rename(need_rename_path, new_parent_path)
    if os.path.isdir(need_rename_path):
        lists = os.listdir(new_parent_path)
        # 如果是文件夹 递归进去
        for file in lists:
            new_file = file.replace(old_str, replace_str)
            os.rename(new_parent_path + "/" + file, new_parent_path + "/" + new_file)

            if os.path.isdir(new_parent_path + "/" + new_file):
                recursive_enter(new_parent_path + "/" + new_file)


if __name__ == '__main__':
    recursive_enter(path)
