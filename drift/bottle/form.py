#-*-coding: utf-8 -*-
from flask_wtf import Form
from wtforms import TextAreaField
from wtforms.validators import InputRequired, Email, EqualTo
from wtforms.ext.sqlalchemy.fields import QuerySelectField


class ThrowForm(Form):
    paper = TextAreaField(
        u'字条', validators=[InputRequired(message=u'字条不能为空')])
