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
def new_question():
    files = {
        "image":open("D:/images/python.png", "rb")
    }
    data = {
        "title": "tornado问题",
        "content": "这里是学前教育的交流中心，大家有什么问题可以一起来交流讨论！欢迎大家的加入！",
        "category": "技术问答"
    }
    res = requests.post("{}/questions/".format(web_site_url), headers=headers, data=data, files=files)
    print(res.status_code)
    print(json.loads(res.text))

def get_question():
    res = requests.get("{}/questions/".format(web_site_url), headers=headers)
    print(res.status_code)
    print(json.loads(res.text))

def get_question_detail(question_id):
    res = requests.get("{}/questions/{}/".format(web_site_url, question_id), headers=headers)
    print(res.status_code)
    print(json.loads(res.text))


def add_answer(question_id):
    data = {
        "content": "tornado从入门到实战3"
    }
    res = requests.post("{}/questions/{}/answers/".format(web_site_url, question_id), headers=headers, json=data)
    print(res.status_code)
    print(json.loads(res.text))

def get_answer(question_id):
    res = requests.get("{}/questions/{}/answers/".format(web_site_url, question_id), headers=headers)
    print(res.status_code)
    print(json.loads(res.text))

def add_reply(answer_id):
    data = {
        "replyed_user":1,
        "content": "tornado从入门到实战5"
    }
    res = requests.post("{}/answers/{}/replys/".format(web_site_url, answer_id), headers=headers, json=data)
    print(res.status_code)
    print(json.loads(res.text))

def get_replys(answer_id):
    res = requests.get("{}/answers/{}/replys/".format(web_site_url, answer_id), headers=headers)
    print(res.status_code)
    print(json.loads(res.text))

if __name__ == "__main__":

    #新建问题
    # new_question()
    # get_question()
    # get_question_detail(1)

    # add_answer(1)
    # get_answer(1)
    add_reply(2)
    get_replys(2)
