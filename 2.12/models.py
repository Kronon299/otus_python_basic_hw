from tortoise import fields
from tortoise.models import Model


class User(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(db_index=True, max_length=255)
    username = fields.CharField(db_index=True, max_length=255, unique=True)
    email = fields.CharField(db_index=True, max_length=255, unique=True)
    posts: fields.ReverseRelation["Post"]

    def __str__(self):
        return f"{self.__class__.__name__} name:{self.name}, id: {self.id}"

    def __repr__(self):
        return self.__str__()


class Post(Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(db_index=True, max_length=255)
    body = fields.TextField()
    user_id: fields.ForeignKeyRelation[User] = fields.ForeignKeyField(
        "models.User", related_name="posts"
    )
    comments: fields.ReverseRelation["Comment"]

    def __str__(self):
        return f"{self.__class__.__name__} title:{self.title}, id: {self.id}"

    def __repr__(self):
        return self.__str__()


class Comment(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(db_index=True, max_length=255)
    email = fields.CharField(db_index=True, max_length=255)
    body = fields.TextField()
    post_id: fields.ForeignKeyRelation[Post] = fields.ForeignKeyField(
        "models.Post", related_name="comments"
    )

    def __str__(self):
        return f"{self.__class__.__name__} name:{self.name}, id: {self.id}"

    def __repr__(self):
        return self.__str__()
