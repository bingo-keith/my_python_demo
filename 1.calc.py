# -*- coding: utf-8 -*-

print(100 + 200 + 300)
print(10 // 3)
print('显示中文')
print('Hi, %s, you have $%d.' % ('keith', 100000))
print('growth rate. %d %%' % 7)
print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))
print('%.1f' % (72 / 85))
classmates = ['test1', 'test2', 'test3', 'test4']
print(classmates[len(classmates) - 1] == classmates[-1])

L = ['Bart', 'Lisa', 'Adam']
for x in L:
    print('Hello,', x)

n = 1
while n <= 100:
    if n > 3:  # 当n = 11时，条件满足，执行break语句
        break  # break语句会结束当前循环
    print(n)
    n = n + 1
print('END')

n = 0
while n < 5:
    n = n + 1
    if n % 2 == 0:  # 如果n是偶数，执行continue语句
        continue  # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)

s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1 & s2)  # {2, 3}
print(s1 | s2)  # {1, 2, 3, 4}
