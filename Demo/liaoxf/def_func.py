#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


def quadratic(a, b, c):
    if a == 0:
        print('参数a不能为0')
        return False
    else:
        f_result = (-b + math.sqrt(b*b-4*a*c))/(2*a)
        s_result = (-b - math.sqrt(b*b-4*a*c))/(2*a)
        return f_result, s_result
