#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pcc.die import Die
import pygal

# 创建一个D6
die = Die()

# 掷几次次骰子，并将结果存储在一个列表中
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)
# print(results)

# 分析结果，用于存储每一个点数出现的次数
frequencies = []
for value in range(1, die.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)
print(frequencies)


# 对结果进行可视化，创建一个条形图实例
hist = pygal.Bar()

hist.title = "掷一个骰子1000次各个点数出现的次数"
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = "掷骰子出现的点数"
hist.y_title = "各点数出现的次数"

hist.add("D6", frequencies)
hist.render_to_file('die_visual.svg')
