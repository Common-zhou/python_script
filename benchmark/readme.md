这是用来将各种奇奇怪怪的csv文件格式化的

merge_to_one_csv 用于将生成的多个part合并为一个

format_csv是用于将csv的列抽取出来

列关系主要通过开始的mapping_rules映射



## 操作方法（sf1/sf10）。sf100必须使用其他方法
1.首先将所有的文件合并。调用merge_to_one.py

``` shell script
# static 文件可以按以下方法设置
# 父文件夹位置
file_path = r"D:/tiger/data/SF1/composite-merged-fk/static"
# 需要保存的位置
saved_path = r'D:/tiger/data/SF1/composite-merged-fk/merge'
# 文件夹名字
file_list = ['Organisation', 'Place', 'Tag', 'TagClass']


# dynamic
file_path = r"D:/tiger/data/SF1/composite-merged-fk/dynamic"
saved_path = r'D:/tiger/data/SF1/composite-merged-fk/merge'
file_list = ['Comment', 'Comment_hasTag_Tag', 'Forum', 'Forum_hasMember_Person', 'Forum_hasTag_Tag', 'Person',
                                'Person_hasInterest_Tag', 'Person_knows_Person', 'Person_likes_Comment', 'Person_likes_Post',
                                'Person_studyAt_University', 'Person_workAt_Company', 'Post', 'Post_hasTag_Tag']
```

2.选出所有需要挑选的列
```shell script
file_path = r"D:\tiger\data\SF1\composite-merged-fk\merge"
saved_path = r'D:\tiger\data\SF1\composite-merged-fk\format'
file_list = ['Comment.csv', 'Comment_hasTag_Tag.csv', 'Forum.csv', 'Forum_hasMember_Person.csv',
                                'Forum_hasTag_Tag.csv',
                                'Person.csv',
                                'Person_hasInterest_Tag.csv', 'Person_knows_Person.csv', 'Person_likes_Comment.csv',
                                'Person_likes_Post.csv',
                                'Person_studyAt_University.csv', 'Person_workAt_Company.csv', 'Post.csv', 'Post_hasTag_Tag.csv']```
