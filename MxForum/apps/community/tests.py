import json
from datetime import datetime
import requests
import jwt

current_time = datetime.utcnow()

from MxForm.settings import settings

web_site_url = "http://127.0.0.1:8888"
data = jwt.encode({
    "name":"bobby",
    "id":1,
    "exp":current_time
}, settings["secret_key"]).decode("utf8")

headers={
        "tsessionid":data
    }
def new_group():
    files = {
        "front_image":open("D:/images/python.png", "rb")
    }
    data = {
        "name": "学前教育交流角",
        "desc": "这里是学前教育的交流中心，大家有什么问题可以一起来交流讨论！欢迎大家的加入！",
        "notice": "这里是学前教育的交流中心，大家有什么问题可以一起来交流讨论！欢迎大家的加入！",
        "category": "教育同盟"
    }
    res = requests.post("{}/groups/".format(web_site_url), headers=headers, data=data, files=files)
    print(res.status_code)
    print(json.loads(res.text))

def apply_group(group_id, apply_reason):
    data = {
        "apply_reason": apply_reason,
    }
    res = requests.post("{}/groups/{}/members/".format(web_site_url, group_id), headers=headers, json=data)
    print(res.status_code)
    print(json.loads(res.text))


def get_group(group_id):
    res = requests.get("{}/groups/{}/".format(web_site_url, group_id), headers=headers)
    print(res.status_code)
    print(json.loads(res.text))

def add_post(group_id):
    #发帖
    data = {
        "title":"tornado从入门到实战",
        "content":"tornado从入门到实战"
    }
    res = requests.post("{}/groups/{}/posts/".format(web_site_url, group_id), headers=headers, json=data)
    print(res.status_code)
    print(json.loads(res.text))

def get_post(post_id):
    res = requests.get("{}/posts/{}/".format(web_site_url, post_id), headers=headers)
    print(res.status_code)
    print(json.loads(res.text))

def add_comments(post_id):
    data = {
        "content": "tornado从入门到实战"
    }
    res = requests.post("{}/posts/{}/comments/".format(web_site_url, post_id), headers=headers, json=data)
    print(res.status_code)
    print(json.loads(res.text))

def get_comments(post_id):
    res = requests.get("{}/posts/{}/comments/".format(web_site_url, post_id), headers=headers)
    print(res.status_code)
    print(json.loads(res.text))

def add_reply(comment_id):
    data = {
        "replyed_user":1,
        "content": "tornado从入门到实战2"
    }
    res = requests.post("{}/comments/{}/replys/".format(web_site_url, comment_id), headers=headers, json=data)
    print(res.status_code)
    print(json.loads(res.text))

def get_replys(comment_id):
    res = requests.get("{}/comments/{}/replys/".format(web_site_url, comment_id), headers=headers)
    print(res.status_code)
    print(json.loads(res.text))


def add_like(comment_id):
    res = requests.post("{}/comments/{}/likes/".format(web_site_url, comment_id), headers=headers, json={})
    print(res.status_code)
    print(json.loads(res.text))

if __name__ == "__main__":

    #新建小组
    # new_group()
    # get_group(1)

    # add_post(1)

    # get_post(100)

    add_comments(3)
    get_comments(3)

    add_reply(1)
    get_replys(1)

    add_like(1)
