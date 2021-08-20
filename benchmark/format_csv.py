# coding=utf-8
import pandas as pd
import traceback

# 这是你要选出哪些列   顺序就是你写的这个顺序
mapping_rules = {
    "Comment.csv": ["creationdate", "id", "locationip", "browserused", "content", "length",
                    "creator",
                    "place", "replyofpost", "replyofcomment"],
    "Comment_hasTag_Tag.csv": ["creationdate", "comment.id", "tag.id"],
    'Forum.csv': ["creationdate", "id", "title", "moderator"],
    'Forum_hasMember_Person.csv': ["creationdate", "forum.id", "person.id"],
    'Forum_hasTag_Tag.csv': ["creationdate", "forum.id", "tag.id"],
    'Person.csv': ["creationdate", "id", "firstname", "lastname", "gender", "birthday", "locationip", "browserused",
                   "place", "language", "email"],
    'Person_hasInterest_Tag.csv': ["creationdate", "person.id", "tag.id"],
    'Person_knows_Person.csv': ["creationdate", "person1.id", "person2.id"],
    'Person_likes_Comment.csv': ["creationdate", "person.id", "comment.id"],
    'Person_likes_Post.csv': ["creationdate", "person.id", "post.id"],
    'Person_studyAt_University.csv': ["creationdate", "person.id", "organisation.id", "classyear"],
    'Person_workAt_Company.csv': ["creationdate", "person.id", "organisation.id", "workfrom"],
    'Post.csv': ["creationdate", "id", "imagefile", "locationip", "browserused", "language", "content", "length",
                 "creator", "forum.id", "place"],
    'Post_hasTag_Tag.csv': ["creationdate", "post.id", "tag.id"],
    'Organisation.csv': ["id", "type", "name", "url", "place"],
    'Place.csv': ["id", "name", "url", "type", "ispartof"],
    'Tag.csv': ["id", "name", "url", "hastype"],
    'TagClass.csv': ["id", "name", "url", "issubclassof"]
}


def convert_columns_name_tolower(list):
    for i in range(0, len(list)):
        old_column_name = list[i]
        list[i] = old_column_name.replace("_", "").lower()
    return list


def format_csv(absolute_path, saved_path, file):
    print(absolute_path)
    df = pd.read_csv(absolute_path, sep="|", dtype=object)
    rename_columns = convert_columns_name_tolower(df.columns.tolist())
    df.columns = rename_columns

    choosed_columns = mapping_rules[file]
    df = df[choosed_columns]
    print("expect columns: %d, actual get : %d" % (len(choosed_columns), len(df.columns.tolist())))
    df.to_csv(saved_path + '/' + file, encoding="utf_8", index=False, sep="|")


file_path = r"D:\tiger\data\SF1\composite-merged-fk\merge"
saved_path = r'D:\tiger\data\SF1\composite-merged-fk\format'
file_list = ['Organisation.csv', 'Place.csv', 'Tag.csv', 'TagClass.csv']

if __name__ == '__main__':
    # 这些只是示例
    dynamic_list = ['Comment.csv', 'Comment_hasTag_Tag.csv', 'Forum.csv', 'Forum_hasMember_Person.csv',
                    'Forum_hasTag_Tag.csv',
                    'Person.csv',
                    'Person_hasInterest_Tag.csv', 'Person_knows_Person.csv', 'Person_likes_Comment.csv',
                    'Person_likes_Post.csv',
                    'Person_studyAt_University.csv', 'Person_workAt_Company.csv', 'Post.csv', 'Post_hasTag_Tag.csv']

    static_list = ['Organisation.csv', 'Place.csv', 'Tag.csv', 'TagClass.csv']

    dynamic_path = r"D:\tiger\data\SF1\composite-merged-fk\dynamic"
    static_path = r"D:\tiger\data\SF1\composite-merged-fk\merge"

    # 这是文件夹所在的地方
    parent_path = file_path

    for file in file_list:
        absolute_path = parent_path + "/" + file  # 要拼接的文件夹及其完整路径，注意不要包含中文
        try:
            format_csv(absolute_path, saved_path, file)
        except Exception as e:
            traceback.print_exc()
