#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print('%s is %u years old, it is running!' % (self.name, self.age))