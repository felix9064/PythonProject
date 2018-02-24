#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 问题1.6：怎样实现一个键对应多个值的字典 (也叫 multidict )？
# 解决方案：可以很方便的使用 collections 模块中的 defaultdict 来构造这样的字典。

from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)

d1 = defaultdict(set)
d1['a'].add(1)
d1['a'].add(2)
d1['b'].add(4)

pairs = {
    'a': 1,
    'b': 4,
    'c': 6
}

# 自己实现
d = {}
for key in pairs:
    if key not in d:
        d[key] = []
    d[key].append(pairs[key])


# 使用defaultdict实现
d2 = defaultdict(list)
for key in pairs:
    d2[key].append(pairs[key])
print(d2)
