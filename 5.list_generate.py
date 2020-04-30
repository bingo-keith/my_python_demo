# -*- coding: utf-8 -*-

print(list(range(1, 11)))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print([x * x for x in range(1, 11)])  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print([x * x for x in range(1, 11) if x % 2 == 0])  # [4, 16, 36, 64, 100]

print([m + n for m in 'ABC' for n in 'XYZ'])  # ['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']

import os
print([d for d in os.listdir('.')])  # ['.ipynb_checkpoints', '1.calc.py', '1_helloWorld.ipynb', '2.function.py', '3.slice.py', '4.iterator.py', '5.list_generate.py']

d = {'x': 'A', 'y': 'B', 'z': 'C'}
print([k + '=' + v for k, v in d.items()])  # ['x=A', 'y=B', 'z=C']

# 在一个列表生成式中，for前面的if ... else是表达式，而for后面的if是过滤条件，不能带else。

print([x for x in range(1, 11) if x % 2 == 0])  # [2, 4, 6, 8, 10]

print([x if x % 2 == 0 else -x for x in range(1, 11)])  # [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10]

# 判断是否是字符串
print(isinstance('abc', str))
print(isinstance(123, str))

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [x.lower() for x in L1 if isinstance(x, str)]
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')
# 测试通过!