#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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

for item in users:
    print(item)  # 获取dict的key

for item in users.items():
    print(item[0])  # 读取tuple的第0项
    print(item[1])  # 读取tuple的第1项
    key, value = item  # 解构
    print(item, key, value)  # 获取dict的key和value，把key和value封装成tuple：(key, value)

for item in users['list']:  # 注意，dict的读取不能用点语法，要用中括号语法
    print(item)  # 数组的每一项
    print(item['name'])

for key, value in users.items():
    print(key, '---', value)  # 遍历items方法的对象可以用解构方式把tuple数据提取出来

arr = [1, 2, 3, 4, 5]
print(arr.pop())  # 返回栈尾元素
print(arr)  # [1, 2, 3, 4]
print(arr.pop(1))  # 返回索引为1的元素
print(arr)  # [1, 3, 4]
print(arr.remove(1))  # 没有返回值
print(arr)  # [3, 4]
print(arr.append(1))  # 没有返回值
print(arr)  # [3, 4, 1]
print('hello world'.title())  # Hello World
print('--------------------')


# 元组
def greeting(*names):
    print(names)


greeting('chilly', 'kitty', 'dad')  # ('chilly', 'kitty', 'dad')


# 关键字参数
def greeting2(**names):
    print(names)  # {'name': 'zs', 'age': 12}


greeting2(name='zs', age=12)
