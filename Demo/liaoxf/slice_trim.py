#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 利用Python的切片功能实现一个类似trim去掉字符串两边空格的方法


def trim1(s):
    if s[:1] != " " and s[-1:] != " ":
        return s
    elif s[:1] == " ":
        return trim1(s[1:])
    elif s[-1:] == " ":
        return trim1(s[:-1])


def trim(s):
    while s[:1] == " ":
        s = s[1:]
    while s[-1:] == " ":
        s = s[:-1]
    return s

# 测试

if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
