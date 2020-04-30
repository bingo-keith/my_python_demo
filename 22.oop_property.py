#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 既能检查参数，又可以用类似属性这样简单的方式来访问类的变量呢
class Student(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value


s = Student()
s.score = 60  # 实际转化为s.set_score(60)
print(s.score)  # 实际转化为s.get_score()


# s.score = 9999  # ValueError: score must between 0 ~ 100!


# 还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性
# 下面的birth是可读写属性，而age就是一个只读属性，因为age可以根据birth和当前时间计算出来
class Student2(object):
    @property
    def birth(self):
        return self.birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2020 - self.birth


# @property广泛应用在类的定义中，可以让调用者写出简短的代码，
# 同时保证对参数进行必要的检查，这样，程序运行时就减少了出错的可能性


class Screen(object):
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def resolution(self):
        return self._width * self._height


s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')
