#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import functools


def log(func):
    """
    不带参数的装饰器
    :param func: 被装饰的函数
    :return: 增强（装饰）后的函数

    函数也是对象，它有__name__等属性，但经过decorator装饰之后的函数，它们的__name__已经从原来的'now'变成了'wrapper'
    内置的functools.wraps就是把原始函数的__name__等属性复制到wrapper()函数中
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('begin call %s():' % func.__name__)
        ret = func(*args, **kwargs)
        print('end call %s():' % func.__name__)
        return ret
    return wrapper


def log2(text):
    """
    带参数的装饰器
    :param text: 装饰器参数
    :return: 装饰器函数
    """
    def decorator(func):
        def wrapper(*args, **kw):
            print('begin %s %s():' % (text, func.__name__))
            ret = func(*args, **kw)
            print('end %s %s():' % (text, func.__name__))
            return ret
        return wrapper
    return decorator


@log
def now():
    print('2018-05-16')


@log2('execute')
def hello():
    print('hello, world')


if __name__ == '__main__':
    print(now.__name__)
    print(hello.__name__)
    now()
    hello()
