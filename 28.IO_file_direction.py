#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

print(os.name)  # 操作系统类型
print(os.environ.get('PUBLIC'))  # 环境变量
# 查看当前目录的绝对路径
print(os.path.abspath('.'))
# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来
print(os.path.join('/数据事业部/districtScore/zwb_py_test', 'testdir'))
# 创建一个目录
# os.mkdir('/数据事业部/districtScore/zwb_py_test/testdir1')
# 删掉一个目录
# os.rmdir('/数据事业部/districtScore/zwb_py_test/testdir1')
# 拆分路径（文件不要求存在）
print(os.path.split('/数据事业部/districtScore/zwb_py_test/1.calc.py'))

print([x for x in os.listdir('.') if os.path.isdir(x)])

print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.ipynb'])

