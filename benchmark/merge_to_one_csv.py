# coding=utf-8
import pandas as pd
import os

"""
这个python文件 主要将文件夹下的csv  都合并到一个里面 
"""


def merge_part(folder_path, save_path, save_name):
    """
        folder_path :主文件夹的名字
        save_path： 存储位置
        save_name： 存储文件名字
    """
    # 将该文件夹下的所有文件名存入一个列表
    file_list = [f for f in os.listdir(folder_path) if not f.startswith('.')]
    # file_list = os.listdir(folder_path)

    # 读取第一个CSV文件并包含表头
    df = pd.read_csv(folder_path + '/' + file_list[0], sep="|", dtype=object)  # 编码默认UTF-8，若乱码自行更改

    # 将读取的第一个CSV文件写入合并后的文件保存
    df.to_csv(save_path + '/' + save_name, encoding="utf_8", index=False, sep="|")

    # 循环遍历列表中各个CSV文件名，并追加到合并后的文件
    for i in range(1, len(file_list)):
        if file_list[i].endswith(".csv"):
            df = pd.read_csv(folder_path + '/' + file_list[i], sep="|", dtype=object)
            df.to_csv(save_path + '/' + save_name, encoding="utf_8", index=False, header=False, mode='a+', sep="|")


def print_list(path):
    print(os.listdir(path))


file_path = "D:/tiger/data/SF1/composite-merged-fk/static"
saved_path = r'D:/tiger/data/SF1/merge'
file_list = ['Organisation', 'Place', 'Tag', 'TagClass']

if __name__ == '__main__':
    # 这是代表是否要进行合并
    # True 代表合并
    # False代表不合并
    dynamic_list = ['Comment', 'Comment_hasTag_Tag', 'Forum', 'Forum_hasMember_Person', 'Forum_hasTag_Tag', 'Person',
                    'Person_hasInterest_Tag', 'Person_knows_Person', 'Person_likes_Comment', 'Person_likes_Post',
                    'Person_studyAt_University', 'Person_workAt_Company', 'Post', 'Post_hasTag_Tag']

    static_list = ['Organisation', 'Place', 'Tag', 'TagClass']

    # 这是父文件夹 在它内部 有不同的文件夹 比如Comment
    dynamic_path = r'D:\social\SF1.tar\composite-merged-fk\dynamic'
    static_path = r'D:\social\SF1.tar\composite-merged-fk\static'

    # print_list(static_path)

    parent_path = file_path

    # 代表从 list中取出这些文件夹  然后合并他们
    # 存入 merge文件夹  必须首先自己创建好merge文件夹
    for file in file_list:
        Folder_Path = parent_path + "/" + file  # 要拼接的文件夹及其完整路径，注意不要包含中文
        SaveFile_Path = saved_path  # 拼接后要保存的文件路径
        SaveFile_Name = file + '.csv'  # 合并后要保存的文件名
        merge_part(Folder_Path, SaveFile_Path, SaveFile_Name)
