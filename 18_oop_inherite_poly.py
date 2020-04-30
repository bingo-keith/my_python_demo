#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Animal(object):
    def run(self):
        print('Animal is running...')


class Dog(Animal):
    def run(self):
        print('Dog is running...')


class Cat(Animal):
    def run(self):
        print('Cat is running...')


dog = Dog()
dog.run()
cat = Cat()
cat.run()

# 多态的好处就是，当我们需要传入Dog、Cat、Tortoise……时，
# 我们只需要接收Animal类型就可以了，因为Dog、Cat、Tortoise……都是Animal类型，
# 然后，按照Animal类型进行操作即可。由于Animal类型有run()方法，因此，传入的任意类型，
# 只要是Animal类或者子类，就会自动调用实际类型的run()方法

# 继承可以把父类的所有功能都直接拿过来，这样就不必重零做起，
# 子类只需要新增自己特有的方法，也可以把父类不适合的方法覆盖重写。
# 动态语言的鸭子类型特点决定了继承不像静态语言那样是必须的
