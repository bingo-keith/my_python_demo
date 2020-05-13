#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 注意：windows和linux系统路径中的斜杠不一样，注意一下，windows有时能够正确识别/和\，但linux只识别\
# 绝对路径
# with open('E:/数据事业部/my_python_demo/templates/home.html') as file_object:
# 相对路径
with open('templates\home.html') as file_object:
    # contents = file_object.read()  # 读取所有数据
    lines = file_object.readlines()  # 保存文件内容到lines
    # print(contents.strip())  # 去掉空行，去掉缩进空格
    # for line in file_object:
    #     print(line.rstrip())  # 去掉空行，保留缩进

for line in lines:
    print(line.rstrip()[:15])  # [:n]截取字符串  [:]创建副本
