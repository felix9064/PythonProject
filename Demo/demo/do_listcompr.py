#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

# 列表生成式

list_comp1 = [x * x - 1 for x in range(1, 11)]
print(list_comp1)

list_comp2 = [m + n for m in 'ABC' for n in 'XYZ']
print(list_comp2)

list_comp3 = [d for d in os.listdir('.')]
print(list_comp3)

dict1 = {'x': 'A', 'y': 'B', 'z': 'C'}
list_comp4 = [k + '=' + v for k, v in dict1.items()]
print(list_comp4)

list1 = ['Hello', 'World', 'IBM', 'Apple']
list_comp5 = [s.lower() for s in list1]
print(list_comp5)

list2 = ['Hello', 'World', 18, 'Apple', None]
list_comp6 = [s.lower() for s in list2 if isinstance(s, str)]
print(list_comp6)
