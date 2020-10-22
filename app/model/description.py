# -*- coding: UTF-8 -*- 
# 作者：hao.ren3
# 时间：2020/1/19 16:31
# IDE：PyCharm

from app import db
from sqlalchemy.dialects.mysql import BIGINT
from datetime import datetime


# 公司简介表，只有一行数据
class Description(db.Model):
    __table_args__ = {'comment': '公司简介'}
    id = db.Column(BIGINT(unsigned=True), primary_key=True, comment="公司简介")
    name = db.Column(db.Text(16777216), comment="公司简介")
    create_user_id = db.Column(BIGINT(unsigned=True), db.ForeignKey("user.id"), comment="创建者用户ID")
    update_user_id = db.Column(BIGINT(unsigned=True), db.ForeignKey("user.id"), comment="最后一次修改者用户ID")
    create_time = db.Column(db.DateTime, default=datetime.now(), comment="创建时间")
    update_time = db.Column(db.DateTime, default=datetime.now(), comment="最后一次修改时间")