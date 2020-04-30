# -*- coding: utf-8 -*-
import functools
import time


def log(func):
    # （*）会把接收到的参数形成一个元组（数组），而（**）则会把接收到的参数存入一个字典（对象）
    def wrapper(*args, **kw):
        print('class %s():' % func.__name__)
        print(*args, **kw)
        func(*args, **kw)

    return wrapper


@log
def now(arg1, arg2):
    print('2020-04-29')


now('tuple', 'dict')


def log1(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            start_time = time.time()
            # print('%s %s():' % (text, func.__name__))
            print('begin call: %d' % start_time)
            func(*args, **kw)
            end_time = time.time()
            duration = (end_time - start_time) * 1000
            print('end call: %d' % end_time)
            print('duration: %d ms' % duration)

        return wrapper

    return decorator


@log1('execute')
def now1():
    time.sleep(0.2)
    print('2020-04-29')


now1()


# decorator可以增强函数的功能，定义起来虽然有点复杂，但使用起来非常灵活和方便