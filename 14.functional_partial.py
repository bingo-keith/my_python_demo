# -*- coding: utf-8 -*-
import functools

# functools.partial就是帮助我们创建一个偏函数的，不需要我们自己定义int2()
int2 = functools.partial(int, base=2)
print(int2('1000000'))
print(int2('1000000', base=10))

max2 = functools.partial(max, 10)
print(max2(5, 6, 7))  # 10


# 当函数的参数个数太多，需要简化时，使用functools.partial可以创建一个新的函数，这个新函数可以固定住原函数的部分参数，从而在调用时更简单