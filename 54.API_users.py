#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, request
import json

app = Flask(__name__)

users = {
    'code': '1',
    'msg': 'success',
    'list': [
        {
            'id': 0,
            'name': '张飞',
            'age': '33'
        },
        {
            'id': 1,
            'name': '吕布',
            'age': '34'
        },
        {
            'id': 2,
            'name': '刘备',
            'age': '25'
        }
    ]
}


@app.route('/', methods=['GET', 'POST'])
def home():
    print(users)
    # return json.dumps(users, ensure_ascii=False)
    return users


@app.route('/add', methods=['POST'])
def add():
    user = {
        'id': len(users['list']),
        'name': request.form['name'],
        'age': request.form['age']
    }
    # 下面一行有bug，待修复
    if user in users['list']:
        return '不能重复新增'
    if user is not None:
        users['list'].append(user)
    return user


# @app.route('delete', methods=['DELETE'])
# def delete():
#     print(request)
#     return 'delete'
#
#
# @app.route('update', methods=['PUT'])
# def update():
#     print(request)
#     return 'update'


if __name__ == '__main__':
    app.run()
