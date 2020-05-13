#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from name_function import get_formatted_name

print('Enter "q" at any time to quit. ')

while True:
    first = input('\nPls give me a first name:')
    if first == 'q':
        break
    last = input('\nPls give me a last name:')
    if last == 'q':
        break
    formatted_name = get_formatted_name(first, last)
    print('\nNeatly formatted name: ' + formatted_name)