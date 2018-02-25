#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pcc.die import Die
import pygal

# 创建两个D6骰子
die_1 = Die()
die_2 = Die()


# 掷几次次骰子，并将结果存储在一个列表中
results = []
for roll_num in range(10000):
    result = die_1.roll() + die_2.roll()
    results.append(result)
# print(results)

# 分析结果，用于存储每一个点数出现的次数
frequencies = []
max_result = die_1.num_sides + die_2.num_sides

for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)
print(frequencies)


# 对结果进行可视化，创建一个条形图实例
hist = pygal.Bar()

hist.title = "掷两个骰子1000次各个点数出现的次数"
hist.x_labels = [x for x in range(2, max_result + 1)]
hist.x_title = "掷骰子出现的点数"
hist.y_title = "各点数出现的次数"

hist.add("D6 + D6", frequencies)
hist.render_to_file('dice_visual.svg')
