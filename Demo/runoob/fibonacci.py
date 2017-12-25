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


def fib2(index):
    n, a, b = 0, 0, 1
    while n < index:
        print(b, end=" ")
        a, b = b, a + b
        n = n + 1
    return "done"

fib2(10)
