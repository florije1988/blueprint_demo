# -*- coding: utf-8 -*-
__author__ = 'florije'

from . import db


class Base(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    CreateTime = db.Column(db.DateTime, default=db.func.current_timestamp())
    UpdateTime = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())


class User(Base):
    __tablename__ = 'user_infos'

    Email = db.Column(db.String(50))
    TmpEmail = db.Column(db.String(50))
    UserName = db.Column(db.String(50))
    Password = db.Column(db.String(50))
    Gender = db.Column(db.SmallInteger)
    MsgCount = db.Column(db.Integer, default=0)
    FansCount = db.Column(db.Integer, default=0)
    FollowsCount = db.Column(db.Integer, default=0)

    def __init__(self, email, tmp_email, user_name, password, gender):
        self.Email = email
        self.TmpEmail = tmp_email
        self.UserName = user_name
        self.Password = password
        self.Gender = gender

    def __repr__(self):
        return '<User %r>' % self.name