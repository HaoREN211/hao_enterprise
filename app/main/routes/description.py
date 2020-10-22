# -*- coding: UTF-8 -*- 
# 作者：hao.ren3
# 时间：2020/1/18 14:36
# IDE：PyCharm

from app.main import bp
from flask import render_template
from app.model.description import Description
from app.form.description import DescriptionForm
from config import Config

@bp.route('/description', methods=['GET'])
def description():
    current_description = Description.query.order_by(Description.id.desc()).first()
    form = DescriptionForm()
    form.name.data = current_description.name
    return render_template("description.html",
                           title=Config.ENTERPRISE_NAME,
                           main_page="description",
                           form=form)