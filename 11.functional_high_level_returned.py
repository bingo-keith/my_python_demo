# -*- coding: utf-8 -*-


def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax += n
        return ax

    return sum


f1 = lazy_sum(1, 2, 3, 4, 5)
f2 = lazy_sum(1, 2, 3, 4, 5)
print(f1())  # 15
print(f2())  # 15
print(f1 == f2)  # False


def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f)
    return fs


f1, f2, f3 = count()
print(f1(), f2(), f3())  # 9 9 9


def count1():
    def f(j):
        def g():
            return j * j

        return g

    fs = []
    for i in range(1, 4):
        fs.append(f(i))
    return fs


f11, f22, f33 = count1()
print(f11(), f22(), f33())  # 1 4 9


# 闭包、作用域
def create_counter():
    global i
    i = 0

    def counter():
        global i
        i = i + 1
        return i

    return counter


counterA = create_counter()
print(counterA(), counterA(), counterA(), counterA())

# 返回一个函数时，牢记该函数并未执行，返回函数中不要引用任何可能会变化的变量
