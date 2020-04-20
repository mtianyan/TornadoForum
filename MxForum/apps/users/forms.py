from wtforms_tornado import Form
from wtforms import StringField
from wtforms.validators import DataRequired, Regexp, AnyOf

MOBILE_REGEX = "^1[3578]\d{9}$|^1[48]7\d{8}$|^176\d{8}$"


class SmsCodeForm(Form):
    mobile = StringField("手机号码",
                         validators=[DataRequired(message="请输入手机号码"), Regexp(MOBILE_REGEX, message="请输入合法的手机号码")])


class LoginForm(Form):
    mobile = StringField("手机号码",
                         validators=[DataRequired(message="请输入手机号码"), Regexp(MOBILE_REGEX, message="请输入合法的手机号码")])
    password = StringField("密码", validators=[DataRequired(message="请输入密码")])


class RegisterForm(Form):
    mobile = StringField("手机号码",
                         validators=[DataRequired(message="请输入手机号码"), Regexp(MOBILE_REGEX, message="请输入合法的手机号码")])
    code = StringField("验证码", validators=[DataRequired(message="请输入验证码")])
    password = StringField("密码", validators=[DataRequired(message="请输入密码")])

class ProfileForm(Form):
    nick_name = StringField("昵称", validators=[DataRequired(message="请填写昵称")])
    gender = StringField("性别", validators=[AnyOf(values=["famale", "male"])])
    address = StringField("地址", validators=[DataRequired(message="请填写地址")])
    desc = StringField("个人简介")


class ChangePasswordForm(Form):
    old_password = StringField("旧密码", validators=[DataRequired(message="请输入旧密码")])
    new_password = StringField("新密码", validators=[DataRequired(message="请输入新密码")])
    confirm_password = StringField("确认密码", validators=[DataRequired(message="请再次输入密码")])