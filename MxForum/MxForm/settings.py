import os

import peewee_async

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
settings = {
    "sms_need": False,
    "api_key": "7ea03fbac6fb21859a166ed661ccda8e",
    "static_path": "C:/projects/tornado_overview/chapter03/static",
    "static_url_prefix": "/static/",
    "template_path": "templates",
    "secret_key":"ZGGA#Mp4yL4w5CDu",
    "jwt_expire":7*24*3600,
    "MEDIA_ROOT": os.path.join(BASE_DIR, "media"),
    "SITE_URL":"http://127.0.0.1:8888",
    "db": {
        "host": "127.0.0.1",
        "user": "root",
        "password": "mtianyanroot",
        "name": "message",
        "port": 3306
    },
    "redis":{
        "host":"127.0.0.1",
        "password": "mtianyanRedisRoot"
    }
}

database = peewee_async.MySQLDatabase(
    'mxforum', host="127.0.0.1", port=3306, user="root", password="mtianyanroot"
)