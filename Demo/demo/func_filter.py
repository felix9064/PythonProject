#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# python内置的高阶函数：filter()

import math


def is_sqr(x):
    return math.sqrt(x) % 1 == 0

# return math.sqrt(x) == int(math.sqrt(x))

print(list(filter(is_sqr, range(1, 101))))
