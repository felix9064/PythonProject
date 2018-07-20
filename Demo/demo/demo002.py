#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
编程练习：使用穷举算法求一个任意非负数的平方根（近似值即可）
"""
while True:
    x = input("请输入一个非负数：")
    try:
        x = int(x)
        if x < 0:
            print(x, " 不是一个非负数")
        else:
            break
    except ValueError:
        print(x, " 不符合要求")


epsilon = 0.01
step = epsilon ** 2
num_guesses = 0
ans = 0.0

while abs(ans**2 - x) >= epsilon and ans <= x:
    num_guesses += 1
    ans += step

print("计算的次数：", num_guesses)
if abs(ans**2 - x) >= epsilon:
    print("计算 %s 的平方根失败" % str(x))
else:
    print(x, "的近似平方根为：", ans)
