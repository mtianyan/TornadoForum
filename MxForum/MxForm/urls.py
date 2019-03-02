from tornado.web import url
from tornado.web import StaticFileHandler

from apps.users import urls as user_urls
from apps.community import urls as community_urls
from apps.ueditor import urls as ueditor_urls
from apps.question import urls as question_urls
from MxForm.settings import settings
class MyFileHandler(StaticFileHandler):
    def write_error(self, status_code, **kwargs):
        if status_code == 404:
            self.redirect('http://example.com') # Fetching a default resource

urlpattern = [
    (url("/media/(.*)", StaticFileHandler, {'path':settings["MEDIA_ROOT"]}))
]


urlpattern += user_urls.urlpattern
urlpattern += community_urls.urlpattern
urlpattern += ueditor_urls.urlpattern
urlpattern += question_urls.urlpattern

#集成ueditor注意事项
#前端的域名和后端的域名保持一致