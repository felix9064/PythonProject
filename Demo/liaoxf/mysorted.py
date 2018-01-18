#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 自定义一个排序函数


from functools import partial

my_sort = partial(sorted, key=lambda x: x.lower())

print(my_sort(['bob', 'about', 'Zoo', 'Credit']))
