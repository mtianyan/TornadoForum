from peewee import MySQLDatabase

from apps.users.models import User
from apps.community.models import CommunityGroup, CommunityGroupMember, Post, PostComment, CommentLike
from apps.question.models import *
from apps.message.models import Message

from MxForm.settings import database

database = MySQLDatabase(
    'mxforum', host="127.0.0.1", port=3306, user="root", password="mtianyanroot"
)


def init():
    # 生成表
    database.create_tables([User])
    database.create_tables([CommunityGroup, CommunityGroupMember])
    database.create_tables([Post, PostComment, CommentLike])
    database.create_tables([Question, Answer])
    database.create_tables([Message])


if __name__ == "__main__":
    init()
