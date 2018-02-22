#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Python3中字符串相关的一些操作方法

# title()方法使字符串的每个单词首字母大写
name = "felix chang"
print(name.title())

# count()方法用于统计字符串里某个字符出现的次数，可选参数为在字符串搜索的开始与结束位置
print(name.count('x', 1, -1))

# strip()，lstrip()和rstrip()方法分别为去掉字符串两边，左边和右边的空白字符
favorite_language = " java python javascript "
print(favorite_language.rstrip())

# find,index,rfind,rindex等方法用来检测指定字符串是否包含在当前字符串中，可选参数为在字符串搜索的开始与结束位置
# 返回值为第一次查找到的索引值，以r开头的方法则是从当前字符串的右边开始查找
# find和index的区别在于，如果要查找的字符串不在当前字符串中，find返回-1，而index会报一个异常
print(name.find("aaa"))
print(favorite_language.rindex("java"))

# ljust()，rjust()和center()方法分别返回一个原字符串左对齐，右对齐和剧中对齐的新字符串
# 并用指定字符填充至指定的长度，填充字符默认为空格
# 如果指定的长度小于原字符串的长度则返回原字符串
# 类似的方法还有zfill()，在字符串的左边填充0，等价于rjust(len, "0")
# 例1
print(name.center(20, "*"))
print(name.rjust(20, "0"))
print(name.zfill(20))
print("-3.14".rjust(7, "0"))
print("-3.14".zfill(7))

# 例2
for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    print(repr(x*x*x).rjust(4))

# repr() 产生一个解释器易读的表达形式
# str() 函数返回一个用户易读的表达形式
# 例1：
hello = "hello felix\n"
print(hello)
print(repr(hello))

# 例2：
x = 10 * 3.25
y = 200 * 200
print(repr((x, y, ('Google', 'Apple'))))
