# -*- coding: UTF-8 -*- 
# 作者：hao.ren3
# 时间：2020/1/19 16:56
# IDE：PyCharm

from app.form.render_form import RenderForm
from wtforms import HiddenField, TextAreaField, SubmitField

class DescriptionForm(RenderForm):
    id = HiddenField("ID")
    name = TextAreaField("公司简介", render_kw={"class":"form-control",
                                          "style":"height:200px"})
    description_submit = SubmitField("修改", render_kw={"class":"btn btn-xs btn-success"})
