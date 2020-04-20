from tornado.web import url

from apps.message.handlers import MessageHandler

urlpattern = (
    url("/messages/", MessageHandler),
)
