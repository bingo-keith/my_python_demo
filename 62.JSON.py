#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json

users = {
    'code': '1',
    'msg': 'success',
    'list': [
        {
            'id': 0,
            'name': '张飞',
            'classes': ['math', 'chinese']
        },
        {
            'id': 1,
            'name': '吕布',
            'classes': ['chinese', 'music', 'sport']
        },
        {
            'id': 2,
            'name': '刘备'
        }
    ]
}

# 写入文件
with open('users.json', 'w') as file_object:
    # file_object.write(str(users))
    json.dump(users, file_object)

# 读取文件
with open('users.json', 'r') as f:
    file = json.load(f)
    print(file)
