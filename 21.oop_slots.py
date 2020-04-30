#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Student(object):
    __slots__ = ('name', 'age')  # 用tuple定义允许绑定的属性名称


s = Student()
s.name = 'chilly'
s.age = 25
# s.score = 99
# 由于score没有被放到__slotes__中，所以不能绑定score属性，试图绑定score将得到AttributeError的错误
# 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，多继承的子类是不起作用的
# 除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__
