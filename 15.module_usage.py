#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 第1行和第2行是标准注释
# 第1行注释可以让这个hello.py文件直接在Unix/Linux/Mac上运行
# 第2行注释表示.py文件本身使用标准UTF-8编码


# 模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释
' a test module '

# 作者姓名，公开源代码后可以查看
__author__ = 'Chilly'

import sys


def test():
    args = sys.argv
    print(args)  # 存储了命令行的所有参数
    if len(args) == 1:
        print('Hello, world!')
    elif len(args) == 2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')


# 当我们在命令行运行hello模块文件时，Python解释器把一个特殊变量__name__置为__main__，
# 而如果在其他地方导入该hello模块时，if判断将失败，因此，这种if测试可以让一个模块通过命
# 令行运行时执行一些额外的代码，最常见的就是运行测试
if __name__ == '__main__':
    test()


def _private_1(name):
    return 'Hello, %s ' % name


def _private_2(name):
    return 'Hi, %s ' % name


def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)

print(greeting('ke'))