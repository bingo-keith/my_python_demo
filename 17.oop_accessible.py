#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问
class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def set_score(self, score):
        self.__score = score

    def get_score(self):
        return self.__score


bart = Student('Bart', 59)
bart.set_score(99)
print(bart.get_name())
print(bart.get_score())

# 有些时候，你会看到以一个下划线开头的实例变量名，
# 比如_name，这样的实例变量外部是可以访问的，
# 但是，按照约定俗成的规定，当你看到这样的变量时，
# 意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”
