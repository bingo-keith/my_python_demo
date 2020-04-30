# -*- coding: utf-8 -*-

from collections.abc import Iterable
from collections.abc import Iterator

print(isinstance([], Iterable))
print(isinstance(100, Iterable))

print(isinstance((x for x in range(10)), Iterator))

print(isinstance([], Iterator))
print(isinstance(iter([]), Iterator)) # iter把Iterable对象转换成Iterator对象
