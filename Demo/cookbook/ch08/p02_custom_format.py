#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
通过 format() 函数和字符串方法使得一个对象能支持自定义的格式化
为了自定义字符串的格式化，我们需要在类上面定义 __format__() 方法
"""


_formats = {
    'ymd': '{d.year}-{d.month}-{d.day}',
    'mdy': '{d.month}/{d.day}/{d.year}',
    'dmy': '{d.day}/{d.month}/{d.year}'
}


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __format__(self, format_spec):
        if format_spec == '':
            format_spec = 'ymd'
        fmt = _formats[format_spec]
        return fmt.format(d=self)


if __name__ == '__main__':
    d = Date(2018, 5, 15)
    print(format(d))
    print(format(d, 'mdy'))

    print('The date is {:ymd}'.format(d))
    print('The date is {:mdy}'.format(d))
