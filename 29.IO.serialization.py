#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pickle
import json


# d = dict(name='Bob', age=20, score=88)
# # 把任意对象序列化成一个bytes
# print(pickle.dumps(d))

# f = open('dump.txt', 'wb')
# pickle.dump(d, f)
# f.close()

# f = open('dump.txt', 'rb')
# d = pickle.load(f)
# f.close()
# print(d)


# d = dict(name='Bob', age=20, score=88)
# print(json.dumps(d))

# json_str = '{"age": 20, "score": 88, "name": "Bob"}'
# print(json.loads(json_str))

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


def student2dict(std):
    return {
        'name:': std.name,
        'age': std.age,
        'score': std.score
    }


print(json.dumps(Student('Bob', 20, 88), default=student2dict))

obj = dict(name='小明', age=20)
print(json.dumps(obj))
print(json.dumps(obj, ensure_ascii=True))
