#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
sys.path.append('.')

from flask import Flask
from routes.routes_xueya_users import r_users

app = Flask(__name__)

# app给蓝图注册路由
app.register_blueprint(r_users)


if __name__ == '__main__':
    app.run()
