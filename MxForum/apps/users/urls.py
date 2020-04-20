from tornado.web import url
from apps.users.handler import SmsHandler, RegisterHandler, LoginHandler, ProfileHandler, HeadImageHandler, ChangePasswordHandler

url_pattern = (
    url("/code/", SmsHandler),
    url("/register/", RegisterHandler),
    url("/login/", LoginHandler),
    url("/info/", ProfileHandler),
    url("/headimages/", HeadImageHandler),
    url("/password/", ChangePasswordHandler)
)
