#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>Home</h1>'


@app.route('/login', methods=['GET'])
def login_form():
    return '''<form action="/login" method="post">
                  <p><label>用户名：<input name="username"></label></p>
                  <p><label>密码：<input name="password" type="password"></label></p>
                  <p><button type="submit">登录</button></p>
              </form>'''


@app.route('/login', methods=['POST'])
def login():
    if request.form['username'] == 'admin' and request.form['password'] == 'password':
        return '<h3>Hello, admin</h3>'
    return '<h3>Bad username or password<h3>'


if __name__ == '__main__':
    app.run()
