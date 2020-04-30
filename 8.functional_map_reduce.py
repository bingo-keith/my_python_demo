# -*- coding: utf-8 -*-
from functools import reduce


def f(x):
    return x * x


r = map(f, [1, 2, 3, 4, 5])  # 返回的是Iterator，是惰性序列，要通过list()遍历出来
print(list(r))


def add(x, y):
    return x + y


print(reduce(add, [1, 2, 3]))  # 相当于add(add(1, 2), 3)


def fn(x, y):
    return x * 10 + y


print(reduce(fn, [1, 3, 5, 7, 9]))  # 13579


def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]


print(reduce(fn, map(char2num, '13579')))


def normalize(name):
    new_name = name.lower()
    new_name = new_name[0].upper() + new_name[1:]
    return new_name


print(normalize('ABC'))


def prod(L):
    def fn(x, y):
        return x * y

    return reduce(fn, L)


print(prod([3, 5, 7, 9]))


