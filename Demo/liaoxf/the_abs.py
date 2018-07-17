#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 定义一个求绝对值的函数


def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
