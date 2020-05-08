#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import hashlib

# md5
md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())  # d26a53750bc40b38b65a520292f69306

md55 = hashlib.md5()
md55.update('how to use md5 in '.encode('utf-8'))
md55.update('python hashlib?'.encode('utf-8'))
print(md55.hexdigest())  # d26a53750bc40b38b65a520292f69306

# SHA1
sha1 = hashlib.sha1()
sha1.update('how to use sha1 in '.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())  # 2c76b57293ce30acef38d98f6046927161b46a44

db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}


def login(user, password):
    user_password = hashlib.md5()
    user_password.update(password.encode('utf-8'))
    if user_password.hexdigest() == db[user]:
        return True
    return False


assert login('michael', '123456')
print('michael', login('michael', '123456'))

assert login('bob', 'abc999')
print('bob', login('bob', 'abc999'))

assert login('alice', 'alice2008')
print('alice', login('alice', 'alice2008'))

assert not login('michael', '1234567')
print('michael', login('michael', '1234567'))

assert not login('bob', '123456')
print('bob', login('bob', '123456'))

assert not login('alice', 'Alice2008')
print('alice', login('alice', 'Alice2008'))

print('ok')
