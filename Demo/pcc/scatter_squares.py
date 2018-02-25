#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 绘制散点图

import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

# scatter方法绘制一个点
# plt.scatter(x_values, y_values, s=10, c='red')
# plt.scatter(x_values, y_values, s=10, c=(0, 0, 0.95))

# 颜色映射
plt.scatter(x_values, y_values, s=10, c=y_values, cmap=plt.cm.Blues)

# 设置图表的标题及标题的字体大小
plt.title("Square Numbers", fontsize=14)

# 给坐标轴加上标签
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both', labelsize=14)

# 设置每个坐标轴的取值范围
plt.axis([0, 1100, 0, 1100000])

# 打开查看器，并显示绘制的图形
# plt.show()

# 保存图表为图片
plt.savefig('hello.png')
