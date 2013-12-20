#-*-coding: utf-8 -*-
from flask_wtf import Form
from wtforms import (StringField, BooleanField, PasswordField,
                     SelectField, DateTimeField, TextAreaField)
from wtforms.validators import InputRequired, Email
from wtforms.ext.sqlalchemy.fields import QuerySelectField


class SignInForm(Form):
    username = StringField(
        u'用户名',
        validators=[InputRequired(message=u'用户名不能为空')])
    password = PasswordField(
        u'密码',
        validators=[InputRequired(message=u'密码不能为空')])
    loginkeeping = BooleanField(u'记住我')
