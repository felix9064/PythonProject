#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 打印list:
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

# 打印数字 0 - 9
for x in range(10):
    print(x)

sum1 = 0
for x in range(101):
    sum1 = sum1 + x
print("1+2+3+...+100 = ", sum)

sum2 = 0
n = 99
while n > 0:
    sum2 = sum2 + n
    n = n - 2
print("100以内所有奇数的和为：", sum)	

L = ['Bart', 'Lisa', 'Adam']
for name in L:
    print('Hello,', name)
