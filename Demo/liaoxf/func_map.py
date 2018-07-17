#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# python内置的高阶函数：map()


def format_name(s):
    return s.capitalize()

print(list(map(format_name, ['adam', 'LISA', 'barT'])))
