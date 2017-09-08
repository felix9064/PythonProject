#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# python内置的高阶函数：reduce()

from functools import reduce


def prod(x, y):
    return x * y

print(reduce(prod, [2, 4, 5, 7, 12]))
