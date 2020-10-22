# -*- coding: UTF-8 -*- 
# 作者：hao.ren3
# 时间：2020/1/19 15:28
# IDE：PyCharm

from flask import Blueprint

bp = Blueprint('auth', __name__)

from app.auth import login, register