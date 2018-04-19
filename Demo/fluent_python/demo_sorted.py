#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 流畅的Python 第二章示例程序2-16
# sorted排序会返回一个新的列表，原列表不变，而list.sort则是就地排序，其返回值是None

fruits = ['grape', 'raspberry', 'apple', 'banana']
print("使用sorted默认排序", sorted(fruits))
print("排序后原来的列表不会发生变化：", fruits)

print("反向排序：", sorted(fruits, reverse=True))
print("按长度排序：", sorted(fruits, key=len))
print("按长度反向排序：", sorted(fruits, key=len, reverse=True))

fruits.sort()
print("用list.sort函数排序后原来的列表：", fruits)
