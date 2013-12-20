#-*-coding: utf-8 -*-
from flask_wtf import Form
from wtforms import (StringField, BooleanField, PasswordField,
                     SelectField, DateTimeField, TextAreaField)
from wtforms.validators import InputRequired, Email, EqualTo
from wtforms.ext.sqlalchemy.fields import QuerySelectField


class SignInForm(Form):
    email = StringField(
        u'邮箱',
        validators=[InputRequired(message=u'邮箱不能为空')])
    password = PasswordField(
        u'密码',
        validators=[InputRequired(message=u'密码不能为空')])
    loginkeeping = BooleanField(u'记住我')


class SignUpForm(Form):
    email = StringField(
        u'邮箱',
        validators=[InputRequired(message=u'邮箱不能为空')])
    password = PasswordField(
        u'密码',
        validators=[InputRequired(message=u'密码不能为空')])
    confirm =   PasswordField(
        u'确认密码',
        validators=[EqualTo('password', message=u'确认密码不匹配')])
    nickname = StringField(
        u'昵称',
        validators=[InputRequired(message=u'昵称不能为空')])
