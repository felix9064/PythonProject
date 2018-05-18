#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
定义一个装饰器，它可作用于任何函数上，并打印该函数的执行时间
"""
import functools
import time


def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        ret = fn(*args, **kwargs)
        end_time = time.time()
        print('%s executed in %s ms' % (fn.__name__, (end_time - start_time)))
        return ret

    return wrapper


@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y


@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z


if __name__ == "__main__":
    f = fast(11, 22)
    s = slow(11, 22, 33)
    if f != 33:
        print('测试失败!')
    elif s != 7986:
        print('测试失败!')
    else:
        print('测试成功')
