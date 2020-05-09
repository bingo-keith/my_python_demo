#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# try:
#     f = open('/path/to/file', 'r')
#     f.read()
# finally:
#     if f:
#         f.close()
# 可简化为
# with open('/path/to/file', 'r') as f:
#     f.read()


# 并不是只有open()函数返回的fp对象才能使用with语句。
# 实际上，任何对象，只要正确实现了上下文管理，就可以用于with语句

# 实现上下文管理是通过__enter__和__exit__这两个方法实现的。
# 例如，下面的class实现了这两个方法：
# class Query(object):
#     def __init__(self, name):
#         self.name = name
#
#     def __enter__(self):
#         print('Begin')
#         return self
#
#     def __exit__(self, exc_type, exc_value, traceback):
#         if exc_type:
#             print('Error')
#         else:
#             print('End')
#
#     def query(self):
#         print('Query info about %s...' % self.name)
#
#
# with Query('Bob') as q:
#     q.query()

# 标准库contextlib提供了更简单的写法
# @contextmanager
from contextlib import contextmanager


class Query(object):
    def __init__(self, name):
        self.name = name

    def query(self):
        print('Query info about %s...' % self.name)


@contextmanager
def create_query(name):
    print('Begin')
    q = Query(name)
    yield q
    print('End')


with create_query('Bob') as q:
    q.query()


# 在某段代码执行前后自动执行特定代码
@contextmanager
def tag(name):
    print('<%s>' % name)
    yield
    print('</%s>' % name)


with tag('h1'):
    print('hello')
    print('world')

# 代码的执行顺序是：
# with语句首先执行yield之前的语句，因此打印出<h1>；
# yield调用会执行with语句内部的所有语句，因此打印出hello和world；
# 最后执行yield之后的语句，打印出</h1>。

# 如果一个对象没有实现上下文，就不能用于with语句
# 这个时候可以用closing()来把该对象变为上下文对象
from contextlib import closing
from urllib.request import urlopen

with closing(urlopen('http://www.baidu.com')) as page:
    for line in page:
        print(line)
