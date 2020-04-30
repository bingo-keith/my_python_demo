# -*- coding: utf-8 -*-

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print(calc(1, 2))
print(calc())
nums = [1, 2, 3, 4, 5]
print(calc(*nums))

def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
print(person('Michael', 30, gender=1, hobby='internet'))
extra = {'city': 'Beijing', 'job': 'Engineer'}
print(person('Jack', 24, **extra))

print('------------------------------------------')
def fact(n, res=1):
    if(n == 1):
        return res
    return fact(n - 1, n * res)
print(fact(5))  # 120