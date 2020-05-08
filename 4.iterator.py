# -*- coding: utf-8 -*-
from collections import Iterable

d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print('key = %s, value = %d' % (key, d[key]))

for value in d.values():
    print(value)

for k, v in d.items():
    print(k, v)

print(isinstance(d, Iterable))


def find_min_and_max(L):
    s_min = L[0]
    s_max = L[0]
    for val in L:
        if s_min > val:
            s_min = val
        if s_max < val:
            s_max = val
    return s_min, s_max


print(find_min_and_max([1, 2, 3, 8, 0, 4, 5, 6]))
