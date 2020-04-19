from tornado.web import url
from apps.users.handler import SmsHandler, RegisterHandler, LoginHandler

url_pattern = (
    url("/code/", SmsHandler),
    url("/register/", RegisterHandler),
    url("/login/", LoginHandler),
)
