# -*- coding: UTF-8 -*- 
# 作者：hao.ren3
# 时间：2020/1/19 15:36
# IDE：PyCharm

from app import db
from app.auth import bp
from flask import render_template, redirect, url_for
from app.model.user import User
from app.form.user import UserForm
from flask_login import login_user

@bp.route('/register', methods=['GET', 'POST'])
def register():
    user_form = UserForm()
    if user_form.validate_on_submit():
        user = User(username=user_form.username.data)
        user.set_password(user_form.password.data)
        db.session.add(user)

        current_user = User.query.filter_by(username=user_form.username.data).first()
        login_user(current_user, remember=False)
        return redirect(url_for("data.index"))
    return render_template("auth/register.html", user_form=user_form)