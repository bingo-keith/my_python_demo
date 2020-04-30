# -*- coding: utf-8 -*-


print(sorted([36, 5, -12, 9, -21]))

print(sorted([36, 5, -12, 9, -21], key=abs))

print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))

print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))

L = [('Bob', 75), ('Adam', 92), ('Cart', 66), ('Lisa', 88)]


def by_name(user):
    # return user[0].lower()  # 姓名排序
    return -user[1]  # 成绩排序


print(sorted(L, key=by_name))

print(L[1][0])


# sorted()也是一个高阶函数。用sorted()排序的关键在于实现一个映射函数
