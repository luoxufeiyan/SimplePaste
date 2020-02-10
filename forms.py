#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 20-01-25 下午4:22
# @Author  : LXFY
# @Site    : http://paste.fledding.com
# @File    : forms.py
# @Software: PyCharm

from __future__ import unicode_literals
from flask_wtf import FlaskForm
from wtforms import TextAreaField, IntegerField, SubmitField, StringField, PasswordField, RadioField
from wtforms.validators import DataRequired, Length


class CodeForm(FlaskForm):
    code = IntegerField('PasteCode', validators=[DataRequired()])
    submit = SubmitField('Go!')


class ContentForm(FlaskForm):
    # code = IntegerField('PasteCode', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()], render_kw={"rows": 30, "cols": 15})
    submit = SubmitField('Submit')

class ModifyForm(FlaskForm):
    # code = IntegerField('PasteCode', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()], render_kw={"rows": 30, "cols": 15})
    status = RadioField('Shown', validators=[DataRequired()], choices=[("1", 'Display'), ("0", 'Hide')], default='1')
    submit = SubmitField('Submit')


class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(), Length(1, 24)])
    password = PasswordField('password', validators=[DataRequired(), Length(1, 24)])
    submit = SubmitField('log in')
