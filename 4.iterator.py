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


def findMinAndMax(L):
    min = L[0]
    max = L[0]
    for value in L:
        if (min > value):
            min = value
        if (max < value):
            max = value
    return min, max


print(findMinAndMax([1, 2, 3, 8, 0, 4, 5, 6]))
