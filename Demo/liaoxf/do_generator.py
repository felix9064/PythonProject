#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 生成器表达式----一边循环一边计算
# 列表元素可以在循环的过程中不断推算出后续的元素
# 这样就不必创建完整的list，从而节省大量的空间

from collections import Iterable
import array

# 第一种方法：将列表生成式最外面的[] 改成()
# 列表生成式
list_comp = [x * x for x in range(10)]
# 生成器表达式
list_gene = (x * x for x in range(10))

# 生成器是可迭代对象
print(isinstance(list_gene, Iterable))

# 如果生成器表达式是一个函数调用过程中的唯一参数，那么不需要额外再用括号把它围起来
symbols = '$¢£¥€¤'
t = tuple(ord(symbol) for symbol in symbols)
print(t)

# 如果生成器表达式不是一个函数的唯一参数，则外面的圆括号是必须的
array.array('I', (ord(s) for s in symbols))

# 生成器表达式是逐个产出元素，从来不会一次性产出一个含有6个T恤样式的列表
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
for t_shirts in ('%s %s' % (c, s) for c in colors for s in sizes):
    print(t_shirts)


# 用函数循环的方法实现斐波拉契数列
def fibonacci1(num):
    n, a, b = 0, 0, 1
    while n < num:
        print(b, end=' ')
        a, b = b, a + b
        n = n + 1
    print('done')
    return 'done'


fibonacci1(20)


# 第二种方法：如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator（生成器函数）
# 把上面定义的函数改一下就成了一个生成器
def fibonacci2(num):
    n, a, b = 0, 0, 1
    while n < num:
        yield b
        a, b = b, a + b
        n = n + 1
    print('done')
    return 'done'


for g in fibonacci2(20):
    print(g, end=' ')


# 练习：输出杨辉三角
def triangles(num):
    n, list1 = 0, [1]
    while n < num:
        yield list1
        i = len(list1) - 1
        while i:
            list1[i] = list1[i] + list1[i-1]
            i -= 1
        list1.append(1)
        n = n + 1


# 输出杨辉三角更简洁的写法
def triangles():
    list2 = [1]
    while True:
        yield list2
        list2 = [x + y for x, y in zip([0] + list2, list2 + [0])]


x = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    x = x + 1
    if x == 10:
        break

if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')
