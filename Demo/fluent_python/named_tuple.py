#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 流畅的Python 第二章示例程序2-9
# python中collections.namedtuple提供了可命名元组
# 它可以用来构建一个带字段名的元组和一个有名字的类

from collections import namedtuple

# 创建一个具名元组需要两个参数，一个是类名，另一个是类的各个字段的名字。
# 后者可以是由数个字符串组成的可迭代对象，或者是由空格分隔开的字段名组成的字符串
City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))

# tokyo是tuple类型的实例
print(isinstance(tokyo, tuple))

# 可以通过字段名来访问元组中的元素， 也可以通过下标索引来访问
print(tokyo.name, tokyo[1], tokyo.coordinates)

# _fields 属性是一个包含这个类所有字段名称的元组
print(City._fields)

LatLong = namedtuple('LatLong', 'lat long')
delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))

# 用 _make() 通过接受一个可迭代对象来生成这个类的一个实例，它的作用跟City(*delhi_data) 是一样的
delhi1 = City._make(delhi_data)
delhi2 = City(*delhi_data)

Card = namedtuple('Card', ['rank', 'suit'])
