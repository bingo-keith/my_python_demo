#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# try:
#     print(5/0)
# except ZeroDivisionError:
#     print('You cannot divide by zero')

print('Give me two number , and I will divide them.')
print('Enter q to quit.')

while True:
    first = input('\npls input the first number:\n')
    if first == 'q':
        break
    second = input('\npls input the second number:\n')
    try:
        res = int(first) / int(second)
    except ZeroDivisionError:
        print('You cannot divide by zero')
    except FileNotFoundError:
        pass
    except TypeError:
        pass
    else:
        print('The answer is %08.3f' % res)  # 0表示左侧补0，8表示长度，3表示小数点位数
