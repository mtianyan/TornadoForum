from datetime import datetime

import jwt
from MxForm.settings import settings
current_time = datetime.utcnow()

data = jwt.encode({
    "name":"bobby",
    "id":1,
    "exp":current_time
}, "abc").decode("utf8")

import time
time.sleep(2)

data = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6Miwibmlja19uYW1lIjpudWxsLCJleHAiOjE1MzcwNjM1MjB9.ugyNxwpimOvc3AZtqvJgR3uitZKMYoAtNeZmtsi_898"
send_data = jwt.decode(data, settings["secret_key"], leeway=1, options={"verify_exp":False})

print(send_data)
