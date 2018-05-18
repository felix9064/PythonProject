#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Topic: 通过在类中实现__call__方法，让该类的实例变成可调用对象，即可以在实例对象后面加()来调用该实例对象
Desc : 流畅的Python 第五章示例程序5-8
"""
import random


class BingoCage:
    """
    BingoCage的实例使用任何可迭代的对象构建，而且会在
    """
    def __init__(self, items):
        """
        在本地构建一个副本，防止列表参数的意外副作用
        :param items: 任何可迭代对象
        """
        self._items = items

        # 打乱列表中元素的顺序
        random.shuffle(self._items)

    def pick(self):
        """
        从列表中取出一个元素，如果列表为空，则抛出异常
        :return: 取出的元素
        """
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')

    def __call__(self, *args, **kwargs):
        """直接调用实例对象实现跟pick一样的功能"""
        return self.pick()


if __name__ == '__main__':
    bingo = BingoCage(list(range(5)))
    print(callable(bingo))
    print('bingo.pack():%d' % bingo.pick())
    print('bingo():%d' % bingo())
