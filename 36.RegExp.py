#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

# m = re.match(r'^(\d{3})-(\d{3,8})$', '010-123456')
# print(m.group(0))
# print(m.group(1))
# print(m.group(2))
#
# print(m.groups())
#
#
# def is_valid_email(addr):
#     return re.match(r'^((?:\w+\.*)(?:\w+))@(\w+\.\w{3}(?:\.\w{2})?)$', addr)
#
#
# assert is_valid_email('someone@gmail.com')
# assert is_valid_email('bill.gates@microsoft.com')
# assert not is_valid_email('bob#example.com')
# assert not is_valid_email('mr-bob@example.com')
# print('ok')


def name_of_email(addr):
    return re.match(r'^<?(\w+\s?\w+)>?(?:\s?\w*)@\w+\.\w{3}(?:\.\w{2})?$', addr).groups()[0]


print(name_of_email('tom@voyager.org') == 'tom')
print(name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris')
