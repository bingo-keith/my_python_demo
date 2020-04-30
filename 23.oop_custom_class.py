#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pdb


# __str__ 返回用户看到的字符串
class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name: %s)' % self.name


print(Student('chilly'))

for x in range(3):
    # pdb.set_trace()  # 调试代码断点
    print(x)

print('---------------------------------------------------')


# __iter__ 返回一个迭代对象
# __getitem__ 表现得像list那样按照下标取出元素
class Fib(object):
    def __init__(self, n=5):
        self.a, self.b = 0, 1
        self.n = n

    def __iter__(self):
        return self

    def __getitem__(self, item):
        print(item, 'item')  # 这里的item就是f[n]中传入的n
        if isinstance(item, int):  # item是索引
            a, b = 1, 1
            for w in range(item):
                a, b = b, a + b
            return a
        if isinstance(item, slice):  # item是切片
            start = item.start
            stop = item.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for s in range(stop):
                if s >= start:
                    L.append(a)
                a, b = b, a + b
            return L

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > self.n:  # 这里的n就是实例lei传入的参数Fib(10)中的10
            raise StopIteration()
        return self.a


for q in Fib(100):
    print(q)

f = Fib(10)
print(list(f)[2:4])  # 切片
print(f[1:3])


# __delitem__ 删除某个元素
# __getattr__ 动态返回一个属性，解决调用不存在的属性自定义处理时
class Student2(object):
    def __init__(self):
        self.name = 'chilly'

    def __getattr__(self, item):  # 只有在没有找到属性的情况下
        if item == 'score':
            return 99
        # 除了score以外其他的不存在的属性都会返回None


ss = Student2()
print(ss.name)
print(ss.score)


# __call__ 定义一个__call__()方法，就可以直接对实例进行调用
