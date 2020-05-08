#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime, timedelta

now = datetime.now()

# 2020-05-08 15:02:19.276023 小数后面的是毫秒数
print(now)

# <class 'datetime.datetime'>
print(type(now))

# 2020-05-08 20:20:20
print(datetime(2020, 5, 8, 20, 20, 20))

# 获取当前时间戳
print(int(datetime.now().timestamp() * 1000))

# 获取当前本地（北京）时间
print(datetime.fromtimestamp(datetime.now().timestamp()))

# 获取当前伦敦时间
print(datetime.utcfromtimestamp(datetime.now().timestamp()))

# 字符串转换为datetime
print(datetime.strptime('2020-2-3 8:00:00', '%Y-%m-%d %H:%M:%S'))

# 对日期和时间进行加减
print(now + timedelta(hours=2))
print(now + timedelta(days=1))
print(now + timedelta(days=1, hours=2))


