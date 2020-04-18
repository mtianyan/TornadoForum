import json
from urllib.parse import urlencode

from tornado import httpclient
from tornado.httpclient import HTTPRequest

from MxForm.settings import settings


class AsyncYunPian:
    def __init__(self, api_key=None):
        if not api_key:
            self.api_key = settings["api_key"]
        else:
            self.api_key = api_key

    async def send_single_sms(self, code, mobile):
        http_client = httpclient.AsyncHTTPClient()
        url = "https://sms.yunpian.com/v2/sms/single_send.json"
        text = "【袋鼠二手书】您的验证码是{}。如非本人操作，请忽略本短信".format(code)
        post_request = HTTPRequest(url=url, method="POST", body=urlencode({
            "apikey": self.api_key,
            "mobile": mobile,
            "text": text
        }))
        res = await http_client.fetch(post_request)
        return json.loads(res.body.decode("utf8"))


if __name__ == "__main__":
    import tornado

    io_loop = tornado.ioloop.IOLoop.current()

    yun_pian = AsyncYunPian("7ea03fbac6fb21859a166ed661ccda8e")

    # run_sync方法可以在运行完某个协程之后停止事件循环
    from functools import partial

    new_func = partial(yun_pian.send_single_sms, "1234", "18092671458")
    io_loop.run_sync(new_func)
