#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 输出结果


class HtmlOutput(object):

    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        if float(data["score"]) > 9.0:
            self.datas.append(data)

    def output_html(self):
        fout = open("movie.txt", "w", encoding="utf8")
        for data in self.datas:
            fout.write("标题：%s\n" % data["title"])
            fout.write("地址：%s\n" % data["url"])
            # fout.write("简介：%s\n" % data["summary"])
            fout.write("分数：%s\n" % data["score"])
            fout.write("\n")

        fout.close()
