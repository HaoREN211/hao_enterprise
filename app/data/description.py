# -*- coding: UTF-8 -*- 
# 作者：hao.ren3
# 时间：2020/1/19 16:29
# IDE：PyCharm

from flask_login import login_required
from app.model.description import Description
from app.data import bp
from app import db
from app.form.description import DescriptionForm
from flask_login import current_user
from flask import render_template, flash, redirect, url_for
from datetime import datetime


@bp.route('/description', methods=['GET', 'POST'])
@login_required
def description():
    # 第一次进入网页的时候，初始化公司的简介
    if Description.query.count()==0:
        description_to_add = Description(name="", create_user_id=current_user.id, update_user_id=current_user.id)
        db.session.add(description_to_add)

    # 获取最后一次更新的公司简介
    current_description = Description.query.order_by(Description.update_time.desc()).first()
    description_form = DescriptionForm()

    # 当修改表单提交时，如果有修改内容，则更新修改内容。否则则刷新界面。
    if description_form.description_submit.data and description_form.validate_on_submit():
        if description_form.name.data != current_description.name:
            current_description.name = description_form.name.data
            current_description.update_user_id = current_user.id
            current_description.update_time = datetime.now()
            flash("修改成功")
        else:
            flash("毫无任何修改")
        return redirect(url_for("data.index"))

    # 更新修改表单的公司简介内容
    description_form.name.data = current_description.name

    return render_template("data/description.html", form=description_form)