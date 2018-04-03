#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 切片，在Python里，像列表（list）、元组（tuple）和字符串（str）这类序列类型都支持切片操作
# 可以指定起始位置，终止位置，步长
# 切片可以命名

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print(L[0:3])

newList = list(range(100))

print(newList[1:11])
print(newList[-10:-1])

print(newList[90:])
print(newList[-10:])
print(newList[:10])

print(newList[60:80:2])
print(newList[81::2])
print(newList[::10])

# 切片可以命名
