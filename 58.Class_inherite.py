#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from my_animal import Animal as A

dog = A('ketty', 5)
dog.run()


# 继承
class Dog(A):
    def __init__(self, name, age, gender):
        super().__init__(name, age)
        self.gender = gender

    def dance(self):
        print('The animal is %s, it is %u years old, it is %s, and it dances!' % (self.name, self.age, self.gender))

# %c	 格式化字符及其ASCII码
# %s	 格式化字符串
# %d	 格式化整数
# %u	 格式化无符号整型
# %o	 格式化无符号八进制数
# %x	 格式化无符号十六进制数
# %X	 格式化无符号十六进制数（大写）
# %f	 格式化浮点数字，可指定小数点后的精度
# %e	 用科学计数法格式化浮点数
# %E	 作用同%e，用科学计数法格式化浮点数
# %g	 %f和%e的简写
# %G	 %F 和 %E 的简写
# %p	 用十六进制数格式化变量的地址


d = Dog('kitty', 3, 'baby')
d.dance()
d.run()
