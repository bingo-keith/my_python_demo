#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from io import StringIO, BytesIO

# f = StringIO()
# print(f.write('hello'))
# print(f.write(' '))
# print(f.write('world!'))
# print(f.getvalue())  # 获取写入后的str


# f = StringIO('Hello!\nHi!\nGoodbye!')
# while True:
#     s = f.readline()
#     if s == '':
#         break
#     print(s.strip())


f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())

# StringIO和BytesIO是在内存中操作str和bytes的方法，使得和读写文件具有一致的接口
