#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 创建list列表
print('list是一种可变的有序集合，可以随时添加和删除其中的元素。')
classmates = ['Michael', 'Bob', 'Tracy']
print('classmates =', classmates)

# 用len()来获取list长度
print('len(classmates) =', len(classmates))

# 用索引来访问list中每一个位置的元素，记得索引是从0开始的
print('classmates[0] =', classmates[0])
print('classmates[1] =', classmates[1])
print('classmates[2] =', classmates[2])

# 用-1做索引，直接获取最后一个元素
print('classmates[-1] =', classmates[-1])

# 删除末尾元素
classmates.pop()
print('调用pop()之后的classmates =', classmates)

# 往list中追加元素到末尾
classmates.append('Adam')
print('调用append(\'Adam\')之后的classmates =', classmates)

# 可以把元素插入到指定的位置，比如索引号为1的位置
classmates.insert(1, 'Jack')
print('调用insert(1, \'Jack\')之后的classmates =', classmates)

# 删除指定位置的元素
classmates.pop(1)
print('调用pop(1)之后的classmates =', classmates)

# list里面的元素的数据类型也可以不同
List = ['Apple', 123, True]
print("元素各不相同的List = ", List)

s = ['python', 'java', ['asp', 'php'], 'scheme']
print("list元素也可以是另一个list,如：", s)

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

print('L = ', L)
print("打印Apple:", L[0][0])
print("打印Python:", L[1][1])
print("打印Lisa:", L[2][2])
