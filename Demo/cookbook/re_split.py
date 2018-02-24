#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 问题2.1 你需要将一个字符串分割为多个字段，但是分隔符 (还有周围的空格) 并不是固定的
# 解决方案：string对象的split()方法只适应于非常简单的字符串分割情形，
# 它并不允许有多个分隔符或者是分隔符周围不确定的空格。
# 当你需要更加灵活的切割字符串的时候，最好使用 re.split() 方法

import re

line = 'asdf fjdk; afed, fjek,asdf, foo'
print(re.split(r'[;,\s]\s*', line))

# 正则表达式中可以包含一个括号捕获分组。如果使用了捕获分组，那么被匹配的文本也将出现在结果列表中
print(re.split(r'(;|,|\s)\s*', line))
