# -*- coding: utf-8 -*-

L = [x for x in range(10)]
print(L)

g = (x * x for x in range(10))
for n in g:
    print(n)


def fib(s_max):
    nn, a, b = 0, 0, 1
    while nn < s_max:
        yield b
        a, b = b, a + b
        nn += 1
    return 'done'


f = fib(5)
for v in f:
    print(v)
