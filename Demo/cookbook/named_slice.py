#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 问题1.11：你的程序已经出现一大堆已无法直视的硬编码切片下标，然后你想清理下代码。
# 解决方案：对切片进行命名

record = '....................100 .......513.25 ..........'
# 硬编码切片下标
cost = int(record[20:23]) * float(record[31:37])
print(cost)

# 命名切片
SHARES = slice(20, 23)
PRICE = slice(31, 37)
cost1 = int(record[SHARES]) * float(record[PRICE])
print(cost1)
