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
    for item in users['list']:
        if item['name'] == user['name']:
            return '不能重复新增'
    users['list'].append(user)
    return user


@app.route('/delete', methods=['DELETE'])
def delete():
    print(request.form['id'])
    user = {}
    for item in users['list']:
        if item['id'] == int(request.form['id']):
            user = item
    if not user:
        return '查无此人'
    else:
        users['list'].remove(user)
    return user


@app.route('/update', methods=['PUT'])
def update():
    print(request.form.to_dict())
    user = request.form.to_dict()
    for item in users['list']:
        if item['id'] == int(user['id']):
            item['name'] = user['name']
            item['age'] = user['age']
    return users


if __name__ == '__main__':
    app.run()
