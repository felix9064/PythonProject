#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import Iterable

# 迭代

d = {'a': 1, 'b': 2, 'c': 3}

for key in d:
    print(key)

for key in d.values():
    print(key)

print(isinstance('abc', Iterable))
print(isinstance(123, Iterable))


for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)
