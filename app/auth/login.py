# -*- coding: UTF-8 -*- 
# 作者：hao.ren3
# 时间：2020/1/19 15:29
# IDE：PyCharm

from app.auth import bp
from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, current_user
from app.model.user import User
from app.form.user import LoginForm
from werkzeug.urls import url_parse

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('data.index'))
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(username=login_form.username.data).first()
        if user is None or not user.check_password(login_form.password.data):
            flash('用户名或密码不对')
            return redirect(url_for('auth.login'))
        login_user(user, remember=login_form.remember_me.data)

        # 原始URL设置了next查询字符串参数后，应用就可以在登录后使用它来重定向。
        # 装饰器将拦截请求并以重定向到*/login来响应，
        # 但是它会添加一个查询字符串参数来丰富这个URL，如/login?next=/index*。
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('data.index')
        return redirect(next_page)
    return render_template("auth/login.html", login_form=login_form)


