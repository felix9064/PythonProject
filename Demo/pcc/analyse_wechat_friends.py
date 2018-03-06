#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 获取微信好友信息并分析
from collections import Counter
import itchat
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import pygal


class MyFriends:
    def __init__(self):
        # 扫二维码登录微信网页版
        itchat.auto_login(hotReload=True)
        # 获取微信好友信息列表
        self.friends = itchat.get_friends(update=True)

    def analyse_sex(self):
        """分析好友的性别，并用饼状图展现结果"""

        # 获取所有好友的性别 1-男，2-女，0-未知
        sex_list = list(map(lambda x: x['Sex'], self.friends[1:]))

        # 获取每种性别出现的次数，并按照0，1，2排序
        counts = sorted(list(map(lambda x: x[1], Counter(sex_list).items())), key=lambda x: x[0])
        labels = ['Unknow', 'Male', 'Female']
        colors = ['red', 'green', 'blue']

        plt.figure(figsize=(8, 5), dpi=80)
        plt.axes(aspect=1)
        # 画一个饼图，counts性别统计结果
        plt.pie(counts,
                # 性别展示标签
                labels=labels,
                # 饼图区域配色
                colors=colors,
                # 标签距离圆点距离
                labeldistance=1.1,
                # 饼图区域文本格式
                autopct='%3.1f%%',
                # 饼图是否显示阴影
                shadow=False,
                # 饼图起始角度
                startangle=90,
                # 饼图区域文本距离圆点距离
                pctdistance=0.6)
        plt.legend(loc='upper right',)

        # 解决matplotlib无法显示中文的问题
        font_set = FontProperties(fname=r"C:\windows\fonts\simsun.ttc", size=12)

        plt.title('%s的微信好友性别组成' % self.friends[0]['NickName'], fontproperties=font_set)
        plt.show()

    def analyse_location(self):
        """分析好友所在省份，并生成柱状图展现"""

        # 获取所有好友所在的省份
        provinces_list = list(map(lambda x: x['Province'] if x['Province'] else '未知', self.friends[1:]))

        # 统计各个省份出现的次数，并从大到小排序
        count = sorted(Counter(provinces_list).items(), key=lambda x: x[1], reverse=True)

        # 分别生成对应的x轴和y轴数据列表
        provinces = list(map(lambda x: x[0], count))
        nums = list(map(lambda x: x[1], count))

        # 对结果进行可视化，创建一个柱状图实例
        hist = pygal.Bar()
        hist.title = "%s的微信好友所在省份分布图" % self.friends[0]['NickName']
        hist.x_title = "省份"
        hist.y_title = "好友个数"

        hist.x_labels = provinces
        hist.add("省份", nums)
        hist.render_to_file('friends_location.svg')

if __name__ == '__main__':

    f = MyFriends()
    print(f.friends)
    # f.analyse_sex()
    f.analyse_location()
