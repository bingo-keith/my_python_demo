# -*- coding: utf-8 -*-

L = [x for x in range(10)]
print(L)

g = (x * x for x in range(10))
for n in g:
    print(n)

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n += 1
    return 'done'
f = fib(5)
for v in f:
    print(v)