"""将csv拆分为多个"""
import pandas as pd
# import thread
import os
import time  # 引入time模块


# csv 路径:{output_csv1: {}, output_csv2:{}}
def split_data(need_split, mapping, saved_path, re_mapping):
    df = pd.read_csv(need_split, sep="|", dtype=object)
    start_time = time.clock()

    # for fname in mapping:
    #     # print(fname)
    #     # print(mapping[fname])
    #     tuple_name_id = mapping[fname]
    #     select_column = df[tuple_name_id[0]]
    #     select_column = select_column.dropna(axis=0, subset=tuple_name_id[1])
    #
    #     if re_mapping is not None and fname in re_mapping:
    #         select_column.columns = re_mapping[fname]
    #     select_column.to_csv(saved_path + '/' + fname, encoding="utf_8", index=False, sep="|")
    stop_time = time.clock()
    cost = stop_time - start_time
    print("cost %s second" % (cost))
    print(need_split + " complate......")


mapping = {
    'Comment.csv': {
        # 第一个是列名称  第二个是如果有空值 需要丢弃的行
        "Comment.csv": (["creationdate", "id", "locationip", "browserused", "content", "length"], ["id"]),
        "Comment_isLocatedIn_Country.csv": (["creationdate", "id", "place"], ["place"]),
        "Comment_replyOf_Comment.csv": (["creationdate", "id", "replyofcomment"], ["replyofcomment"]),
        "Comment_hasCreator_Person.csv": (["creationdate", "id", "creator"], ["creator"]),
        "Comment_replyOf_Post.csv": (["creationdate", "id", "replyofpost"], ["replyofpost"])
    },
    'Forum.csv': {
        "Forum.csv": (["creationdate", "id", "title"], ["id"]),
        "Forum_hasModerator_Person.csv": (["creationdate", "id", "moderator"], ["moderator"])
    },
    'Organisation.csv': {
        "Organisation.csv": (["id", "type", "name", "url"], ["id"]),
        "Organisation_isLocatedIn_Place.csv": (["id", "place"], ["place"])
    },
    'Person.csv': {
        "Person.csv": (["creationdate", "id", "firstname", "lastname", "gender", "birthday", "locationip",
                        "browserused",
                        "language", "email"], ["id"]),
        "Person_isLocatedIn_City.csv": (["creationdate", "id", "place"], ["place"])
    },
    'Place.csv': {
        "Place.csv": (["id", "name", "url", "type"], ["id"]),
        "Place_isPartOf_Place.csv": (["id", "ispartof"], ["ispartof"])
    },
    'Post.csv': {
        "Post.csv": (["creationdate", "id", "imagefile", "locationip", "browserused", "language", "content",
                      "length"], ["id"]),
        "Post_hasCreator_Person.csv": (["creationdate", "id", "creator"], ["creator"]),
        "Forum_containerOf_Post.csv": (["creationdate", "forum.id", "id"], ["forum.id"]),
        "Post_isLocatedIn_Country.csv": (["creationdate", "id", "place"], ["place"])
    },
    'TagClass.csv': {
        "TagClass.csv": (["id", "name", "url"], ["id"]),
        "TagClass_isSubclassOf_TagClass.csv": (["id", "issubclassof"], ["issubclassof"])
    },
    'Tag.csv': {
        "Tag.csv": (["id", "name", "url"], ["id"]),
        "Tag_hasType_TagClass.csv": (["id", "hastype"], ["hastype"])
    },
    'Comment_hasTag_Tag.csv': {
        "Comment_hasTag_Tag.csv": (["creationdate", "comment.id", "tag.id"], [])
    },
    'Forum_hasMember_Person.csv': {
        "Forum_hasMember_Person.csv": (["creationdate", "forum.id", "person.id"], [])
    },
    'Forum_hasTag_Tag.csv': {
        "Forum_hasTag_Tag.csv": (["creationdate", "forum.id", "tag.id"], [])
    },
    'Person_hasInterest_Tag.csv': {
        "Person_hasInterest_Tag.csv": (["creationdate", "person.id", "tag.id"], [])
    },
    'Person_knows_Person.csv': {
        "Person_knows_Person.csv": (["creationdate", "person1.id", "person2.id"], [])
    },
    'Person_likes_Comment.csv': {
        "Person_likes_Comment.csv": (["creationdate", "person.id", "comment.id"], [])
    },
    'Person_likes_Post.csv': {
        "Person_likes_Post.csv": (["creationdate", "person.id", "post.id"], [])
    },
    'Person_studyAt_University.csv': {
        "Person_studyAt_University.csv": (["creationdate", "person.id", "organisation.id", "classyear"], [])
    },
    'Person_workAt_Company.csv': {
        "Person_workAt_Company.csv": (["creationdate", "person.id", "organisation.id", "workfrom"], [])
    },
    'Post_hasTag_Tag.csv': {
        "Post_hasTag_Tag.csv": (["creationdate", "post.id", "tag.id"], [])
    }

}

re_mapping = {
    'Comment.csv': {
        "Comment.csv": ["creationDate:DATETIME", "id:ID(Comment)", "locationIP:STRING", "browserUsed:STRING",
                        "content:STRING", "length:LONG"],
        "Comment_isLocatedIn_Country.csv": ["creationDate:DATETIME", ":START_ID(Comment)", ":END_ID(Place)"],
        "Comment_replyOf_Comment.csv": ["creationDate:DATETIME", ":START_ID(Comment)", ":END_ID(Comment)"],
        "Comment_hasCreator_Person.csv": ["creationDate:DATETIME", ":START_ID(Comment)", ":END_ID(Person)"],
        "Comment_replyOf_Post.csv": ["creationDate:DATETIME", ":START_ID(Comment)", ":END_ID(Post)"]
    },
    'Forum.csv': {
        "Forum.csv": ["creationDate:DATETIME", "id:ID(Forum)", "title:STRING"],
        "Forum_hasModerator_Person.csv": ["creationDate:DATETIME", ":START_ID(Forum)", ":END_ID(Person)"]
    },
    'Organisation.csv': {
        "Organisation.csv": ["id:ID(Organisation)", ":LABEL", "name:STRING", "url:STRING"],
        "Organisation_isLocatedIn_Place.csv": [":START_ID(Organisation)", ":END_ID(Place)"]
    },
    'Person.csv': {
        "Person.csv": ["creationDate:DATETIME", "id:ID(Person)", "firstName:STRING", "lastName:STRING", "gender:STRING",
                       "birthday:DATE", "locationIP:STRING", "browserUsed:STRING", "speaks:STRING[]", "email:STRING[]"],
        "Person_isLocatedIn_City.csv": ["creationDate:DATETIME", ":START_ID(Person)", ":END_ID(Place)"]
    },
    'Place.csv': {
        "Place.csv": ["id:ID(Place)", "name:STRING", "url:STRING", ":LABEL"],
        "Place_isPartOf_Place.csv": [":START_ID(Place)", ":END_ID(Place)"]
    },
    'Post.csv': {
        "Post.csv": ["creationDate:DATETIME", "id:ID(Post)", "imageFile:STRING", "locationIP:STRING",
                     "browserUsed:STRING", "language:STRING", "content:STRING", "length:LONG"],
        "Post_hasCreator_Person.csv": ["creationDate:DATETIME", ":START_ID(Post)", ":END_ID(Person)"],
        "Forum_containerOf_Post.csv": ["creationDate:DATETIME", ":START_ID(Forum)", ":END_ID(Post)"],
        "Post_isLocatedIn_Country.csv": ["creationDate:DATETIME", ":START_ID(Post)", ":END_ID(Place)"]
    },
    'TagClass.csv': {
        "TagClass.csv": ["id:ID(TagClass)", "name:STRING", "url:STRING"],
        "TagClass_isSubclassOf_TagClass.csv": [":START_ID(TagClass)", ":END_ID(TagClass)"]
    },
    'Tag.csv': {
        "Tag.csv": ["id:ID(Tag)", "name:STRING", "url:STRING"],
        "Tag_hasType_TagClass.csv": [":START_ID(Tag)", ":END_ID(TagClass)"]
    },
    'Comment_hasTag_Tag.csv': {
        "Comment_hasTag_Tag.csv": ["creationDate:DATETIME", ":START_ID(Comment)", ":END_ID(Tag)"]
    },
    'Forum_hasMember_Person.csv': {
        "Forum_hasMember_Person.csv": ["creationDate:DATETIME", ":START_ID(Forum)", ":END_ID(Person)"]
    },
    'Forum_hasTag_Tag.csv': {
        "Forum_hasTag_Tag.csv": ["creationDate:DATETIME", ":START_ID(Forum)", ":END_ID(Tag)"]
    },
    'Person_hasInterest_Tag.csv': {
        "Person_hasInterest_Tag.csv": ["creationDate:DATETIME", ":START_ID(Person)", ":END_ID(Tag)"]
    },
    'Person_knows_Person.csv': {
        "Person_knows_Person.csv": ["creationDate:DATETIME", ":START_ID(Person)", ":END_ID(Person)"]
    },
    'Person_likes_Comment.csv': {
        "Person_likes_Comment.csv": ["creationDate:DATETIME", ":START_ID(Person)", ":END_ID(Comment)"]
    },
    'Person_likes_Post.csv': {
        "Person_likes_Post.csv": ["creationDate:DATETIME", ":START_ID(Person)", ":END_ID(Post)"]
    },
    'Person_studyAt_University.csv': {
        "Person_studyAt_University.csv": ["creationDate:DATETIME", ":START_ID(Person)", ":END_ID(Organisation)",
                                          "classYear:LONG"]
    },
    'Person_workAt_Company.csv': {
        "Person_workAt_Company.csv": ["creationDate:DATETIME", ":START_ID(Person)", ":END_ID(Organisation)",
                                      "workFrom:LONG"]
    },
    'Post_hasTag_Tag.csv': {
        "Post_hasTag_Tag.csv": ["creationDate:DATETIME", ":START_ID(Post)", ":END_ID(Tag)"]
    }
}

# list = []
# for i in mapping:
#     list.append(i)
# print(list)

all_list = ['Comment.csv', 'Forum.csv', 'Organisation.csv', 'Person.csv', 'Place.csv', 'Post.csv', 'TagClass.csv',
            'Tag.csv', 'Comment_hasTag_Tag.csv', 'Forum_hasMember_Person.csv', 'Forum_hasTag_Tag.csv',
            'Person_hasInterest_Tag.csv', 'Person_knows_Person.csv', 'Person_likes_Comment.csv',
            'Person_likes_Post.csv', 'Person_studyAt_University.csv', 'Person_workAt_Company.csv',
            'Post_hasTag_Tag.csv']

if __name__ == '__main__':
    path = "/data/sf100/format"
    saved_path = "/data/sf100/resolve"
    need_split = ['Comment.csv']

    for name in need_split:
        split_data(path + "/" + name, mapping[name], saved_path, re_mapping[name])
        print("start split: " + name)
