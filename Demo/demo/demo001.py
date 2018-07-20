#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
编程练习：用户输入一个整数，然后输出两个整数root和pwr，满足0 <pwr < 6，
并且root**pwr等于用户输入的整数。如果不存在这样一对整数，则输出一条消息进行说明
"""
while True:
    x = input("请输入一个整数：")
    try:
        x = int(x)
        break
    except ValueError:
        print(x, " 不是一个整数")
pwr = 1

while pwr < 6:
    root = 0
    while root**pwr < abs(x):
        root = root + 1
    if root**pwr == abs(x):
        if x < 0:
            root = -root
        elif pwr % 2 == 0:
            print("%d 的 %d 次方等于 %d" % (-root, pwr, x))
        print("%d 的 %d 次方等于 %d" % (root, pwr, x))
    pwr = pwr + 1
