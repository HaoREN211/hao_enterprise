# -*- coding: UTF-8 -*- 
# 作者：hao.ren3
# 时间：2020/1/19 16:01
# IDE：PyCharm

from app.data import bp
from flask import render_template
from flask_login import login_required


@bp.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    return render_template("data/index.html")