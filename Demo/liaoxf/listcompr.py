#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 列表生成式

# 例1：使用列表生成式，将列表list1中的元素转小写，并过滤list1中的非字符串元素
# isinstance是Python内置函数，用于判断给定对象是否是给定的类型

list1 = ['Hello', 'World', 18, 'Apple', None]
list2 = [s.lower() for s in list1 if isinstance(s, str)]
print(list2)

if list2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')

# 例2：使用列表生成式，生成一个2n+1的数字列表，n为从3到11的数字
list3 = [2*n + 1 for n in range(3, 12)]
print(list3)

# 例3：过滤出一个指定的数字列表中值大于20的元素
L = [3, 7, 11, 14, 19, 33, 26, 57, 99]
list4 = [x for x in L if x > 20]
print(list4)

# 例4：计算两个集合的全排列，并将结果作为保存至一个新的列表中
L1 = ['香蕉', '苹果', '橙子']
L2 = ['可乐', '牛奶']
list5 = [(x, y) for x in L1 for y in L2]
print(list5)

# 例5：将一个字典转换成由一组元组组成的列表，元组的格式为(key, value)
D = {'Tom': 15, 'Jerry': 18, 'Peter': 13}
list6 = [(k, v) for k, v in D.items()]
print(list6)
