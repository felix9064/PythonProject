#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Topic: heapq模块 heapq.nlargest 和 heapq.nsmallest 演示
Desc : 从一个集合中获得最大或者最小的 N 个元素列表
"""

import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
# 返回最大的3个数
print(heapq.nlargest(3, nums))
# 返回最小的3个数
print(heapq.nsmallest(3, nums))


# 在函数nlargest和nsmallest的底层实现里面，首先会先将集合数据进行堆排序后放入一个列表中
# 堆数据结构最重要的特征是 heap[0] 永远是最小的元素。并且剩余的元素可以很
# 容易的通过调用 heapq.heappop() 方法得到，该方法会先将第一个元素弹出来，然后
# 用下一个最小的元素来取代被弹出元素
heapq.heapify(nums)
print(nums)


# 两个函数都能接受一个关键字参数，用于更复杂的数据结构中：
portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'APPLE', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YAHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]

# 根据股票的价格来返回3个最大和最小的字典
cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
print(cheap)
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])
print(expensive)
