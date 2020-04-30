# -*- coding: utf-8 -*-

# lambda x: x * x 匿名函数，冒号前面的x表示函数参数
print(list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])))


f = lambda x: x * x
print(f(5))


print(list(filter(lambda x: x % 2 == 1, range(1, 20))))


# Python对匿名函数的支持有限，只有一些简单的情况下可以使用匿名函数