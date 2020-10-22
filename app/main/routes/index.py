# -*- coding: UTF-8 -*-
# 作者：hao.ren3
# 时间：2019/12/21 8:00
# IDE：PyCharm

from app.main import bp
from flask import render_template
from config import Config

@bp.route('/', methods=['GET'])
@bp.route('/index', methods=['GET'])
def index():
    return render_template("index.html", title=Config.ENTERPRISE_NAME, main_page="home")

