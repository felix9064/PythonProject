#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 菜鸟Python3教程 编程第一步
# Fibonacci series: 斐波纳契数列
# 两个元素的总和确定了下一个数

# 关键字end可以用于将结果输出到同一行，或者在输出的末尾添加不同的字符


def fib1(index):
    a, b = 0, 1
    while b < index:
        print(b, end=',')
        a, b = b, a + b
    print()


def fib2(index):
    n, a, b = 0, 0, 1
    while n < index:
        print(b, end=" ")
        a, b = b, a + b
        n = n + 1
    print()
    return "done"


def fib3(index):
    lst = [1, 1]
    for i in range(index - 2):
        lst.append(lst[-1] + lst[-2])
    print(list(lst))


def fib4(index):
    a, b, lst = 0, 1, []
    for i in range(index):
        lst.append(a)
        a, b = b, a + b
    return lst

fib1(60)
fib2(10)
fib3(10)
print(list(fib4(10)))
