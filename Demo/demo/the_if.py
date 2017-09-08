#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
# 低于18.5：过轻
# 18.5-25：正常
# 25-28：过重
# 28-32：肥胖
# 高于32：严重肥胖

height = int(input('请输入你的身高（单位：厘米）：'))
weight = int(input('请输入你的体重（单位：千克）：'))

bmi = weight/(height*height/10000)

if bmi >= 32:
    print('严重肥胖')
elif bmi >= 28:
    print('肥胖')
elif bmi >= 25:
    print('过重')
elif bmi >= 18.5:
    print('正常')
else:
    print('过轻')
