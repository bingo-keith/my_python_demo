#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
sys.path.append('.')

from flask import Flask
from flask_cors import CORS
from routes.routes_xueya_users import r_users
from routes.routes_xueya_articles import r_articles


app = Flask(__name__)

cors = CORS()
'''
resources：字典、迭代器或字符串	无	全局配置允许跨域的API接口
origins：列表、字符串或正则表达式	Access-Control-Allow-Origin	配置允许跨域访问的源，*表示全部允许
methods：列表、字符串	Access-Control-Allow-Methods	配置跨域支持的请求方式，如：GET、POST
expose_headers：列表、字符串	Access-Control-Expose-Headers	自定义请求响应的Head信息
allow_headers：列表、字符串或正则表达式	Access-Control-Request-Headers	配置允许跨域的请求头
supports_credentials：布尔值	Access-Control-Allow-Credentials	是否允许请求发送cookie，false是不允许
max_age：整数、字符串	Access-Control-Max-Age	预检请求的有效时长
'''
cors.init_app(app=app, resources={r'/api/*': {'origins': '*'}}, supports_credentials=True)


# 请求拦截和预处理
@app.before_request
def authorize():
    pass


# app给蓝图注册路由
app.register_blueprint(r_users)
app.register_blueprint(r_articles)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
