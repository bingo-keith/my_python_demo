#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import itertools
# 无限循环
# naturals = itertools.count(1)
# for n in naturals:
#     print(n)

# 无限循环
# cs = itertools.cycle('ABC')
# for c in cs:
#     print(c)

# 无限循环，第二个参数指定重复次数
# nu = itertools.repeat('A', 3)
# for n in nu:
#     print(n)

# takewhile截取有限序列
# naturals = itertools.count(1)
# ns = itertools.takewhile(lambda x: x <= 10, naturals)
# print(list(ns))

# 把一组迭代对象串联起来
# for c in itertools.chain('ABC', 'XYZ'):
#     print(c)

# 把相邻的重复元素放在一起
for key, group in itertools.groupby('AAABBBCCAAA'):
    print(key, list(group))
# 忽略大小写分组
for key, group in itertools.groupby('AaaBBbcCAAa', lambda c: c.upper()):
    print(key, list(group))

