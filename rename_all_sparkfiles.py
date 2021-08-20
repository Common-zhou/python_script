import os

import os, sys, shutil  # 导入模块
import glob


def move_csvfile(need_path):  # 定义函数名称
    all_files = os.listdir(need_path)

    for file_name in all_files:  # 遍历列表下的文件名
        if file_name != sys.argv[0]:  # 代码本身文件路径，防止脚本文件放在path路径下时，被一起重命名
            list = glob.glob(need_path + '/' + file_name + '/part*')
            abs_file = list[0]
            shutil.move(abs_file, need_path + '/' + file_name + ".1")  # 移动文件


if __name__ == '__main__':
    path = r'/data/sf1/resolve'
    move_csvfile(path)

# 运行完之后 只用运行一下脚本就可以
# rm -rf *.csv
# sudo rename 's/\.csv.1$/\.csv/' *.csv.1
