from datetime import datetime

from peewee import *
from peewee import Model

db = MySQLDatabase('wt_message', host="127.0.0.1", port=3306, user="root", password="mtianyanroot")


class Message(Model):
    id = AutoField(verbose_name="id")
    name = CharField(max_length=10, verbose_name="姓名")
    email = CharField(max_length=30, verbose_name="邮箱")
    address = CharField(max_length=30, verbose_name="地址")
    message = TextField(verbose_name="留言")

    class Meta:
        database = db
        table_name = "wt_message"


if __name__ == "__main__":
    db.create_tables([Message])
