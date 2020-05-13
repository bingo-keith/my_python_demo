#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 读取模式 （ 'r' ）、 写入模式 （ 'w' ）、 附加模式 （ 'a' ）或让你能够读取和写入文件的模式（ 'r+' ）
with open('dump.txt', 'a') as file_object:
    file_object.write('I love python!!\n' + str(100) + '\n')