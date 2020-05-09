#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
r = requests.get('https://www.baidu.com/', params={'q': 'python', 'cat': '1001'})
# 状态码
print(r.status_code)
# 返回页面
print(r.text)
# 查看编码
print(r.encoding)
# 获得bytes对象
print(r.content)

# POST请求
r2 = requests.post('http://182.92.194.36/keith/queryList.php', data={'form_email': 'abc@example.com', 'form_password': '123456'})
print(r2.text)
print(r2.headers)

# r = requests.get(url, timeout=2.5)  # 2.5秒后超时
