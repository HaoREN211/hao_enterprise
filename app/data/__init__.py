# -*- coding: UTF-8 -*- 
# 作者：hao.ren3
# 时间：2020/1/19 16:01
# IDE：PyCharm

from flask import Blueprint

bp = Blueprint('data', __name__)

from app.data import index,description