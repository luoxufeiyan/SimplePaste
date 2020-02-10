#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 20-01-25 下午4:22
# @Author  : LXFY
# @Site    : http://paste.fledding.com
# @File    : models.py
# @Software: PyCharm

import time

from ext import db
from flask_login import UserMixin


class PasteText(db.Model):
    __tablename__ = 'text'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=True)
    content = db.Column(db.Text, nullable=False)
    status = db.Column(db.Integer, nullable=False)
    create_time = db.Column(db.Integer, nullable=False)

    def __init__(self, user_id, content, status):
        self.user_id = user_id
        self.content = content
        self.status = status
        self.create_time = time.time()


class User(UserMixin, db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(24), nullable=False)
    password = db.Column(db.String(24), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password
