# -*- coding: utf-8 -*-


def is_odd(n):
    return n % 2 == 1


print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))  # [1, 5, 9, 15]


def not_empty(s):
    return s and s.strip()


print(list(filter(not_empty, ['A', '', 'B', None, 'C', ' '])))  # ['A', 'B', 'C']


# 求指定范围的素数
def _odd_iter():
    n = 1
    while True:
        n = n + 1
        yield n


def _not_divisible(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    it = _odd_iter()  # 初始序列
    while True:
        n = next(it)  # 返回序列的第一个
        yield n
        it = filter(_not_divisible(n), it)  # 构造新序列


for n in primes():
    if n < 100:
        print(n)
    else:
        break

# filter()的作用是从一个序列中筛出符合条件的元素。由于filter()使用了惰性计算，所以只有在取filter()结果的时候，才会真正筛选并每次返回下一个筛出的元素。
