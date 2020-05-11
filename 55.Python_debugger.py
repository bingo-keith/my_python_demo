#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pdb


# break 或 b 设置断点	设置断点
# continue 或 c	继续执行程序
# list 或 l	查看当前行的代码段
# step 或 s	进入函数
# return 或 r	执行代码直到从当前函数返回
# exit 或 q	中止并退出
# next 或 n	执行下一行
# pp	打印变量的值
# help	帮助
def test(name):
    d = 'hello, %s' % name
    return d


a = 'aaa'
# pdb.set_trace()  # 设置断点 按输入n回车后执行下一行
b = 'bbb'
c = 'ccc'
final = a + b + c
print(final)
res = test('chilly')
print(res)

