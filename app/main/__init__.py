# 作者：hao.ren3
# 时间：2019/12/21 8:00
# IDE：PyCharm

from flask import Blueprint

bp = Blueprint('main', __name__)

from app.main.routes import index