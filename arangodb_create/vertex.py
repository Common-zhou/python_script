from pyArango.collection import Collection, Field, Edges


class Comment(Collection):
    _fields = {
        "name": Field()
    }


class Person(Collection):
    _fields = {
        "lifetime": Field()
    }


class Tag(Collection):
    _fields = {
        "name": Field()
    }


class Organisation(Collection):
    _fields = {
        "name": Field()
    }


class TagClass(Collection):
    _fields = {
        "name": Field()
    }


class Place(Collection):
    _fields = {
        "name": Field()
    }


class Forum(Collection):
    _fields = {
        "name": Field()
    }


class Post(Collection):
    _fields = {
        "name": Field()
    }
