#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 问题1.8：怎样在数据字典中执行一些计算操作 (比如求最小值、最大值、排序等等)
# 解决方案：可以使用zip和sorted，min，max等函数

prices = {
    'ACME': 45.23,
    'APL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

# 如果你在一个字典上执行普通的数学运算，你会发现它们仅仅作用于键，而不是值
# 返回ACME
print(min(prices))
# 返回IBM
print(max(prices))


# 可以在 min() 和 max() 函数中提供 key 函数参数来获取最小值或最大值对应的键的信息
print(min(prices, key=lambda k: prices[k]))
print(max(prices, key=lambda k: prices[k]))


# 最小股票价格和代码
# 函数zip的参数iterable为可迭代的对象，并且可以有多个参数。
# 该函数返回一个以元组为元素的列表，其中第i个元组包含每个参数序列的第i个元素。
# 返回的列表长度被截断为最短的参数序列的长度。只有一个序列参数时，它返回一个1元组的列表。没有参数时，它返回一个空的列表。
min_price = min(zip(prices.values(), prices.keys()))
print(min_price)


# 最大股票价格和代码
max_price = max(zip(prices.values(), prices.keys()))
print(max_price)


# 排序
prices_sorted = sorted(zip(prices.values(), prices.keys()))
print(prices_sorted)
