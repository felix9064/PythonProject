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
s1 = slice(1, 8)
print(newList[s1])

# 切片可以被赋值
list1 = list(range(10))

list1[2:5] = [20, 30]
print(list1)
del list1[5:7]
list1[3::2] = [11, 22]

# 如果赋值的对象是一个切片，那么赋值语句的右侧必须是个可迭代对象，下面第一个例子会报错
# list1[2:5] = 100
list1[2:5] = [100]
print(list1)
