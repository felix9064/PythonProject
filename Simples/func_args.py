#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#函数的参数，有必选参数也叫位置参数，默认参数，可变参数，关键字参数和命名关键字参数
#这5种参数都可以组合使用，但是可变参数无法和命名关键字参数混合使用
#请注意，参数定义的顺序必须是：必选参数，默认参数，可变参数/命名关键字参数 和关键字参数

# 定义一个默认参数的函数
def power(x, n=2):
    s = 1
    while n > 0:
        n = n -1
        s = s * x
    return s

# 默认参数的函数
def enroll(name, gender, age=25, city='beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)

# 默认参数的函数
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

# 定义一个可变参数的函数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

# 定义一个关键字参数的函数，关键字参数必须传入参数名或是组装好的dict
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

# 定义一个命名关键字参数, 命名关键字参数必须传入参数名, 命名关键字参数可以有缺省值
def persion(name, age, *, city, job):
    print(name, age, city, job)


#5中参数可以组合使用
def f1(a, b, c=0, *args, **kw):
    print('a=', a, 'b=', b, 'c=', c, 'args=', args, 'kw=', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a=', a, 'b=', b, 'c=', c, 'd=', d, 'kw=', kw)