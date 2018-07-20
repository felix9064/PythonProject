#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
编程练习：使用二分查找算法求一个任意非负数的平方根（近似值即可）
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

epsilon = 0.0001
num_guesses = 0
low = 0.0
high = max(1.0, x)
ans = (high + low) / 2.0
while abs(ans**2 - x) >= epsilon:
    num_guesses += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low) / 2.0
print("计算的次数：", num_guesses)
print(x, "的近似平方根为：", ans, -ans)
