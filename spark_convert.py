import numpy
from pyspark import SparkContext, SparkConf

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
        # "Forum_containerOf_Post.csv": (["creationdate", "forum_id", "id"], ["forum_id"]),
        # "Post_isLocatedIn_Country.csv": (["creationdate", "id", "place"], ["place"])
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
        "Comment_hasTag_Tag.csv": (["creationdate", "comment_id", "tag_id"], [])
    },
    'Forum_hasMember_Person.csv': {
        "Forum_hasMember_Person.csv": (["creationdate", "forum_id", "person_id"], [])
    },
    'Forum_hasTag_Tag.csv': {
        "Forum_hasTag_Tag.csv": (["creationdate", "forum_id", "tag_id"], [])
    },
    'Person_hasInterest_Tag.csv': {
        "Person_hasInterest_Tag.csv": (["creationdate", "person_id", "tag_id"], [])
    },
    'Person_knows_Person.csv': {
        "Person_knows_Person.csv": (["creationdate", "person1_id", "person2_id"], [])
    },
    'Person_likes_Comment.csv': {
        "Person_likes_Comment.csv": (["creationdate", "person_id", "comment_id"], [])
    },
    'Person_likes_Post.csv': {
        "Person_likes_Post.csv": (["creationdate", "person_id", "post_id"], [])
    },
    'Person_studyAt_University.csv': {
        "Person_studyAt_University.csv": (["creationdate", "person_id", "organisation_id", "classyear"], [])
    },
    'Person_workAt_Company.csv': {
        "Person_workAt_Company.csv": (["creationdate", "person_id", "organisation_id", "workfrom"], [])
    },
    'Post_hasTag_Tag.csv': {
        "Post_hasTag_Tag.csv": (["creationdate", "post_id", "tag_id"], [])
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


arangodb_re_mapping = {
    'Comment.csv': {
        "Comment.csv": ["creationDate", "id", "locationIP", "browserUsed",
                        "content", "length"],
        "Comment_isLocatedIn_Country.csv": ["creationDate", ":START_ID", ":END_ID"],
        "Comment_replyOf_Comment.csv": ["creationDate", ":START_ID", ":END_ID"],
        "Comment_hasCreator_Person.csv": ["creationDate", ":START_ID", ":END_ID"],
        "Comment_replyOf_Post.csv": ["creationDate", ":START_ID", ":END_ID"]
    },
    'Forum.csv': {
        "Forum.csv": ["creationDate", "id", "title"],
        "Forum_hasModerator_Person.csv": ["creationDate", ":START_ID", ":END_ID"]
    },
    'Organisation.csv': {
        "Organisation.csv": ["id", ":LABEL", "name", "url"],
        "Organisation_isLocatedIn_Place.csv": [":START_ID", ":END_ID"]
    },
    'Person.csv': {
        "Person.csv": ["creationDate", "id", "firstName", "lastName", "gender",
                       "birthday:DATE", "locationIP", "browserUsed", "speaks", "email"],
        "Person_isLocatedIn_City.csv": ["creationDate", ":START_ID", ":END_ID"]
    },
    'Place.csv': {
        "Place.csv": ["id", "name", "url", ":LABEL"],
        "Place_isPartOf_Place.csv": [":START_ID", ":END_ID"]
    },
    'Post.csv': {
        "Post.csv": ["creationDate", "id", "imageFile", "locationIP",
                     "browserUsed", "language", "content", "length"],
        "Post_hasCreator_Person.csv": ["creationDate", ":START_ID", ":END_ID"],
        "Forum_containerOf_Post.csv": ["creationDate", ":START_ID", ":END_ID"],
        "Post_isLocatedIn_Country.csv": ["creationDate", ":START_ID", ":END_ID"]
    },
    'TagClass.csv': {
        "TagClass.csv": ["id", "name", "url"],
        "TagClass_isSubclassOf_TagClass.csv": [":START_ID", ":END_ID"]
    },
    'Tag.csv': {
        "Tag.csv": ["id", "name", "url"],
        "Tag_hasType_TagClass.csv": [":START_ID", ":END_ID"]
    },
    'Comment_hasTag_Tag.csv': {
        "Comment_hasTag_Tag.csv": ["creationDate", ":START_ID", ":END_ID"]
    },
    'Forum_hasMember_Person.csv': {
        "Forum_hasMember_Person.csv": ["creationDate", ":START_ID", ":END_ID"]
    },
    'Forum_hasTag_Tag.csv': {
        "Forum_hasTag_Tag.csv": ["creationDate", ":START_ID", ":END_ID"]
    },
    'Person_hasInterest_Tag.csv': {
        "Person_hasInterest_Tag.csv": ["creationDate", ":START_ID", ":END_ID"]
    },
    'Person_knows_Person.csv': {
        "Person_knows_Person.csv": ["creationDate", ":START_ID", ":END_ID"]
    },
    'Person_likes_Comment.csv': {
        "Person_likes_Comment.csv": ["creationDate", ":START_ID", ":END_ID"]
    },
    'Person_likes_Post.csv': {
        "Person_likes_Post.csv": ["creationDate", ":START_ID", ":END_ID"]
    },
    'Person_studyAt_University.csv': {
        "Person_studyAt_University.csv": ["creationDate", ":START_ID", ":END_ID",
                                          "classYear"]
    },
    'Person_workAt_Company.csv': {
        "Person_workAt_Company.csv": ["creationDate", ":START_ID", ":END_ID",
                                      "workFrom"]
    },
    'Post_hasTag_Tag.csv': {
        "Post_hasTag_Tag.csv": ["creationDate", ":START_ID", ":END_ID"]
    }
}

from pyspark.sql import SparkSession

spark = SparkSession.builder.enableHiveSupport().getOrCreate()


def split_data(need_split, mapping, saved_path, re_mapping):
    df = spark.read.options(header='True', delimiter='|').csv(need_split)

    new_columns = [i.replace(".", "_") for i in df.columns]
    df = df.toDF(*new_columns)

    for fname in mapping:
        # print(fname)
        # print(mapping[fname])
        tuple_name_id = mapping[fname]
        # select_column = df[tuple_name_id[0]]
        select_column = df.select(*tuple_name_id[0])

        select_column = select_column.dropna(subset=tuple_name_id[1])

        print(re_mapping[fname])
        print(type(re_mapping[fname]))

        if re_mapping is not None and fname in re_mapping:
            # select_column.columns = re_mapping[fname]
            select_column = select_column.toDF(*re_mapping[fname])
        select_column.coalesce(1).write.option("header", "true").option("nullValue", None).option("sep", "|").csv(
            saved_path + '/' + fname)
        # select_column.toPandas().to_csv(saved_path + '/' + fname, encoding="utf_8", index=False, sep="|")
    print(need_split + " complate......")


all_list = ['Comment.csv', 'Forum.csv', 'Organisation.csv', 'Person.csv', 'Place.csv', 'Post.csv', 'TagClass.csv',
            'Tag.csv', 'Comment_hasTag_Tag.csv', 'Forum_hasMember_Person.csv', 'Forum_hasTag_Tag.csv',
            'Person_hasInterest_Tag.csv', 'Person_knows_Person.csv', 'Person_likes_Comment.csv',
            'Person_likes_Post.csv', 'Person_studyAt_University.csv', 'Person_workAt_Company.csv',
            'Post_hasTag_Tag.csv']

if __name__ == '__main__':
    path = "/data/sf1/format"
    saved_path = "/data/sf1/resolve"
    need_split = ['Comment.csv', 'Forum.csv', 'Organisation.csv', 'Person.csv', 'Place.csv', 'Post.csv', 'TagClass.csv',
                  'Tag.csv', 'Comment_hasTag_Tag.csv', 'Forum_hasMember_Person.csv', 'Forum_hasTag_Tag.csv',
                  'Person_hasInterest_Tag.csv', 'Person_knows_Person.csv', 'Person_likes_Comment.csv',
                  'Person_likes_Post.csv', 'Person_studyAt_University.csv', 'Person_workAt_Company.csv',
                  'Post_hasTag_Tag.csv']

    for name in need_split:
        split_data(path + "/" + name, mapping[name], saved_path, arangodb_re_mapping[name])
        print("start split: " + name)
