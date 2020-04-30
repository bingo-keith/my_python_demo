#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# try:
#     print('try...')
#     r = 10 / int('a')
#     print('result:', r)
# except ValueError as e:
#     print('ValueError:', e)
# except ZeroDivisionError as e:
#     print('exccept:', e)
# else:
#     print('no error!')
# finally:
#     print('finally...')
import logging
logging.basicConfig(level=logging.INFO)


def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)
        print('Error:', e)
    finally:
        print('finally...')


main()


def foo1(s):
    n = int(s)
    # python -O err.py -O关闭断言，注意是大写字母O，不是0
    assert n != 0, 'n is zero!'
    return 10 / n


def main1():
    foo1('0')


main1()
