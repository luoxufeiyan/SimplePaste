#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 20-01-25 下午4:22
# @Author  : LXFY
# @Site    : http://paste.fledding.com
# @File    : ext.py
# @Software: PyCharm
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()
