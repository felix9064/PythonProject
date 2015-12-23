#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

def quadratic(a,b,c):
#    if not (isinstance(a, (int, float) & isinstance(b, (int, float) & isinstance(c, (int, float)):
#        raise TypeError('bad operand type')
    if a == 0:
        print('参数a不能为0')
        return False
    else:
        fresult = (-b + math.sqrt(b*b-4*a*c))/(2*a)
        sresult = (-b - math.sqrt(b*b-4*a*c))/(2*a)
        return fresult,sresult