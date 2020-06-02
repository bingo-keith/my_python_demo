#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask
from models.m_xueya_users import User
from routes.r_xueya_users import r_users

app = Flask(__name__)
user = User()

# app给蓝图注册路由
app.register_blueprint(r_users)


if __name__ == '__main__':
    app.run()
