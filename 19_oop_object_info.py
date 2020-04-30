#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import types


def fn():
    pass


# 基本类型都可以用type()判断
print(type(123))
print(type('test'))
print(type(None))
print(type(abs))
print(type(123) == int)
print(type('test') == str)

print(type(fn) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)


# 对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数
# isinstance()就可以告诉我们，一个对象是否是某种类型。先创建3种类型的对象

class Animal(object):
    def run(self):
        print('animal is running...')


a = Animal()
# 能用type()判断的基本类型也可以用isinstance()判断
print(isinstance(a, Animal))

# 还可以判断一个变量是否是某些类型中的一种，比如下面的代码就可以判断是否是list或者tuple
print(isinstance([1, 2, 3], (list, tuple)))

# 总是优先使用isinstance()判断类型，可以将指定类型及其子类“一网打尽”
print(dir('ABC'))


# __xxx__的属性和方法在Python中都是有特殊用途的，比如__len__方法返回长度。
# 在Python中，如果你调用len()函数试图获取一个对象的长度，实际上，在len()函数内部，
# 它自动去调用该对象的__len__()方法

class MyObject(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x


obj = MyObject()

print(hasattr(obj, 'x'))
print(setattr(obj, 'y', 19))
print(getattr(obj, 'y'))
