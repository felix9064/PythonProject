#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# python内置的高阶函数：sorted()


print(list(sorted([36, 5, 12, 9, 21], reverse=False)))

print(list(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)))


L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_name(t):
    return t[0]


def by_score(t):
    return t[1]

L1 = sorted(L, key=by_name)
print(L1)
L2 = sorted(L, key=by_score, reverse=True)
print(L2)
