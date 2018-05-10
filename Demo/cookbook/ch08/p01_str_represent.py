#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
改变对象实例的打印或显示输出，让它们更具可读性
要改变一个实例的字符串表示，可重新定义它的 __str__() 和 __repr__() 方法。
"""


class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Pair({0.x!r}, {0.y!r})'.format(self)

    def __str__(self):
        return '({0.x!s}, {0.y!s})'.format(self)


if __name__ == "__main__":
    p = Pair(3, 4)
    print(p)

    # !r 格式化代码指明输出使用 __repr__() 来代替默认的 __str__()
    print('p is {0!r}'.format(p))
    print('p is {0}'.format(p))
