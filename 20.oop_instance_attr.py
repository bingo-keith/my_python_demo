#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Student(object):
    name = 'Student'


s = Student
print(s.name)
print(Student.name)
print(s.name == Student.name)


# 相同名称的实例属性将屏蔽掉类属性，但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性

class Student2(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Student2.count += 1


s1 = Student2('test1')
print(Student2.count)
s2 = Student2('test2')
print(Student2.count)

# 实例属性属于各个实例所有，互不干扰；
# 类属性属于类所有，所有实例共享一个属性；
# 不要对实例属性和类属性使用相同的名字，否则将产生难以发现的错误。
