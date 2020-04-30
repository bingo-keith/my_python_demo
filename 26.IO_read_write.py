#!/usr/bin/env python3
# -*- coding: utf-8 -*-

fpath = 'C:\Windows\system.ini'

with open(fpath, 'r') as f:
    s = f.read()
    print(s)
