#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 绘制简单的折线图

import matplotlib.pyplot as plt

input_values = list(range(1, 6))
squares = [x * x for x in input_values]

# 根据传递的参数来绘制出有意义的图形
plt.plot(input_values, squares, linewidth=3)

# 设置图表的标题及标题的字体大小
plt.title("Square Numbers", fontsize=14)

# 给坐标轴加上标签
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both', labelsize=14)

# 打开查看器，并显示绘制的图形
plt.show()
