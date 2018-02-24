#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 函数的参数，有必选参数也叫位置参数，默认参数，可变参数，关键字参数和命名关键字参数

# 定义一个包含必选参数和默认参数的函数


def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print(power(5, 3))
print(power(5))


# 默认参数的函数


def enroll(name, gender, age=25, city='beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)
enroll('Sarah', 'F')
enroll('Bob', 'M', 7)
enroll('Adam', 'M', city='WuXi')


# 默认参数的函数


def add_end(list1=None):
    if list1 is None:
        list1 = []
    list1.append('END')
    return list1
print(add_end())
print(add_end())
print(add_end([1, 2, 3]))
print(add_end(['x', 'y', 'z']))


# 定义一个可变参数的函数


def calc(*numbers):
    sum1 = 0
    for n in numbers:
        sum1 = sum1 + n * n
    return sum1
print(calc(1, 2, 3))
print(calc(1, 3, 5, 7))

nums = [1, 2, 3]
print(calc(*nums))


# 定义一个含关键字参数的函数，关键字参数允许你传入0个或任意个含参数名的参数，关键字参数必须传入参数名或是组装好的dict


def person(name, age, **kw0):
    print('name:', name, 'age:', age, 'other:', kw0)
person('Felix', 28)
person('Bob', 35, city='Beijing')
person('Adam', 45, gender='M', job='Engineer')

extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra)


# 定义一个含命名关键字参数, 命名关键字参数必须传入参数名, 命名关键字参数可以有缺省值
# 命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数
# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
# 使用命名关键字参数时，要特别注意，如果没有可变参数，就必须加一个*作为特殊分隔符。
# 如果缺少*，Python解释器将无法识别位置参数和命名关键字参数


def person2(name, age, *, city, job):
    print(name, age, city, job)

# 命名关键字参数必须传入参数名，这和位置参数不同。下面注释的函数调用没有传入参数名，调用将报错
# person2('Jack', 24, 'Beijing', 'Engineer')

person2('Jack', 24, city='Beijing', job='Engineer')


# 命名关键字参数可以有缺省值，从而简化调用


def person3(name, age, *, city='Beijing', job):
    print(name, age, city, job)
person3('Jack', 24, job='Engineer')


# 这5种参数都可以组合使用，但是可变参数无法和命名关键字参数混合使用
# 请注意，参数定义的顺序必须是：必选参数，默认参数，可变参数/命名关键字参数 和关键字参数

def f1(a, b, c=0, *args1, **kw1):
    print('a=', a, 'b=', b, 'c=', c, 'args=', args1, 'kw=', kw1)


def f2(a, b, c=0, *, d, **kw2):
    print('a=', a, 'b=', b, 'c=', c, 'd=', d, 'kw=', kw2)

# 在函数调用的时候，Python解释器自动按照参数位置和参数名把对应的参数传进去
f1(1, 2)
f1(1, 2, c=3)
f1(1, 2, 3, 'a', 'b')
f1(1, 2, 3, 'a', 'b', x=99)
f2(1, 2, d=99, ext=None)


# 最神奇的是通过一个tuple和dict，你也可以调用上述函数
# 所以，对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的
args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)

args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
f2(*args, **kw)
