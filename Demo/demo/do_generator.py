#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 生成器-一边循环一边计算
# 列表元素可以在循环的过程中不断推算出后续的元素
# 这样就不必创建完整的list，从而节省大量的空间

# 第一种方法：将列表生成式最外面的[] 改成()
list_genera1 = (x * x for x in range(10))
for g in list_genera1:
    print(g)


# 用函数循环的方法实现斐波拉契数列
def fibonacci1(num):
    n, a, b = 0, 0, 1
    while n < num:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'

print(fibonacci1(10))


# 第二种方法：如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
# 把上面定义的函数改一下就成了一个生成器
def fibonacci2(num):
    n, a, b = 0, 0, 1
    while n < num:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

for g in fibonacci2(10):
    print(g)


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

for t in triangles(5):
    print(t)
