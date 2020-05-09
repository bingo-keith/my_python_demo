#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import chardet

print(chardet.detect(b'Hello, world!'))  # {'encoding': 'ascii', 'confidence': 1.0, 'language': ''}

data = '离离原上草，一岁一枯荣'.encode('gbk')
print(chardet.detect(data))  # {'encoding': 'GB2312', 'confidence': 0.7407407407407407, 'language': 'Chinese'}

data = '离离原上草，一岁一枯荣'.encode('utf-8')
print(chardet.detect(data))

data = '最新の主要ニュース'.encode('euc-jp')
print(chardet.detect(data))