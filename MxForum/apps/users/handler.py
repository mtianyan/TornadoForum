import json
from functools import partial
from random import choice
from datetime import datetime

from tornado.web import RequestHandler
import jwt

from apps.users.forms import SmsCodeForm, RegisterForm, LoginForm
from apps.utils.AsyncYunPian import AsyncYunPian
from MxForm.handler import RedisHandler
from apps.users.models import User

class LoginHandler(RedisHandler):
    async def post(self, *args, **kwargs):
        re_data = {}

        param = self.request.body.decode("utf-8")
        param = json.loads(param)
        form = LoginForm.from_json(param)

        if form.validate():
            mobile = form.mobile.data
            password = form.password.data

            try:
                user = await self.application.objects.get(User, mobile=mobile)
                if not user.password.check_password(password):
                    self.set_status(400)
                    re_data["non_fields"] = "用户名或密码错误"
                else:
                    #登录成功
                    #1. 是不是rest api只能使用jwt
                    # session实际上是服务器随机生成的一段字符串， 保存在服务器的
                    # jwt 本质上还是加密技术，userid， user.name

                    #生成json web token
                    payload = {
                        "id":user.id,
                        "nick_name":user.nick_name,
                        "exp":datetime.utcnow()
                    }
                    token = jwt.encode(payload, self.settings["secret_key"], algorithm='HS256')
                    re_data["id"] = user.id
                    if user.nick_name is not None:
                        re_data["nick_name"] = user.nick_name
                    else:
                        re_data["nick_name"] = user.mobile
                    re_data["token"] = token.decode("utf8")

            except User.DoesNotExist as e:
                self.set_status(400)
                re_data["mobile"] = "用户不存在"

            self.finish(re_data)

class RegisterHandler(RedisHandler):
    async def post(self, *args, **kwargs):
        re_data = {}

        param = self.request.body.decode("utf-8")
        param = json.loads(param)
        register_form = RegisterForm.from_json(param)
        if register_form.validate():
            mobile = register_form.mobile.data
            code = register_form.code.data
            password = register_form.password.data

            #验证码是否正确
            redis_key = "{}_{}".format(mobile, code)
            if not self.redis_conn.get(redis_key):
                self.set_status(400)
                re_data["code"] = "验证码错误或者失效"
            else:
                #验证用户是否存在
                try:
                    existed_users = await self.application.objects.get(User, mobile=mobile)
                    self.set_status(400)
                    re_data["mobile"] = "用户已经存在"
                except User.DoesNotExist as e:
                    user = await self.application.objects.create(User, mobile=mobile, password=password)
                    re_data["id"] = user.id
        else:
            self.set_status(400)
            for field in register_form.erros:
                re_data[field] = register_form[field][0]

        self.finish(re_data)


class SmsHandler(RedisHandler):
    def generate_code(self):
        """
        生成随机4位数字的验证码
        :return:
        """
        seeds = "1234567890"
        random_str = []
        for i in range(4):
            random_str.append(choice(seeds))
        return "".join(random_str)

    async def post(self, *args, **kwargs):
        re_data = {}

        param = self.request.body.decode("utf-8")
        param = json.loads(param)
        sms_form = SmsCodeForm.from_json(param)
        if sms_form.validate():
            mobile = sms_form.mobile.data
            code = self.generate_code()
            yun_pian = AsyncYunPian("d6c4ddbf50ab36611d2f52041a0b949e")

            re_json = await yun_pian.send_single_sms(code, mobile)
            if re_json["code"] != 0:
                self.set_status(400)
                re_data["mobile"] = re_json["msg"]
            else:
                #将验证码写入到redis中
                self.redis_conn.set("{}_{}".format(mobile,code), 1, 10*60)
        else:
            self.set_status(400)
            for field in sms_form.errors:
                re_data[field] = sms_form.errors[field][0]

        self.finish(re_data)