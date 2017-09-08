#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("tuple和list非常类似，tuple一旦初始化就不能修改")

classmates = ('Michael', 'Bob', 'Tracy')
print('classmates =', classmates)
print('len(classmates) =', len(classmates))
print('classmates[0] =', classmates[0])
print('classmates[1] =', classmates[1])
print('classmates[2] =', classmates[2])
print('classmates[-1] =', classmates[-1])

t = (1,)
print("只有1个元素的tuple定义时必须加一个逗号, t =", t)

# cannot modify tuple:
# classmates[0] = 'Adam'
