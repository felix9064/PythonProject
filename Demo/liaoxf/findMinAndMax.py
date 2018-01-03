#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 使用迭代查找一个list中的最大值和最小值，并返回一个tuple


def find_min_and_max(lst):
    max_value = None
    min_value = None
    for v in lst:
        if max_value is None:
            max_value = v
        if min_value is None:
            min_value = v

        if v > max_value:
            max_value = v
        elif v < min_value:
            min_value = v
    return min_value, max_value

# 测试

if find_min_and_max([]) != (None, None):
    print('测试失败!')
elif find_min_and_max([7]) != (7, 7):
    print('测试失败!')
elif find_min_and_max([7, 1]) != (1, 7):
    print('测试失败!')
elif find_min_and_max([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')