#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import namedtuple, deque, defaultdict, OrderedDict, ChainMap, Counter
import os, argparse

# namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x, p.y)
print(isinstance(p, Point))
print(isinstance(p, tuple))

Circle = namedtuple('Circle', ['x', 'y', 'r'])
c = Circle(1, 2, 3)
print(c.x, c.y, c.r)

# deque
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)

# defaultdict
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print(dd)
print(dd['key1'])  # 返回 abc
print(dd['key2'])  # 不存在，返回默认值

# OrderedDict
d = dict([('a', 1), ('b', 2), ('c', 3)])
print(d)  # dict是无序的
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od)  # OrderedDict是有序的，按插入顺序排序


# OrderedDict 实现栈（FIFO先进先出）的dict
class LastUpdatedOrderedDict(OrderedDict):
    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self.capacity = capacity

    def __setitem__(self, key, value):
        contains_key = 1 if key in self else 0
        if len(self) - contains_key >= self._capacity:
            last = self.popitem(last=False)
            print('remove', last)
        if contains_key:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)


# ChainMap
defaults = {
    'color': 'red',
    'user': 'guest'
}
# 构建命令行参数
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user')
parser.add_argument('-c', '--color')
namespace = parser.parse_args()
command_line_args = {k: v for k, v in vars(namespace).items() if v}

# 组合成ChainMap
combined = ChainMap(command_line_args, os.environ, defaults)

# 打印参数
print('color=%s' % combined['color'])
print('user=%s' % combined['user'])

# python use_chainmap.py -u bob

# Counter
c = Counter()
for ch in 'programing':
    c[ch] += 1
print(c)
c.update('hello')  # 也可以一次性update
print(c)
