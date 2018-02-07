#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 解析txt文件，并修改指定内容后写入另一个txt文件


def read_file(path):
    with open(path, "r", encoding="GBK") as f:
        lines = f.readlines()
        with open("G:\\Temp\\new_file.txt", "a", encoding="GBK") as w:
            for line in lines:
                w.write(replace_text(line))


def replace_text(line):
    str_array = line.split(",")
    start = str_array[2]
    end = str_array[3]

    str_array[2] = start[0:4] + "." + start[4:6] + "." + start[-2:]
    if end != "长期":
        str_array[3] = end[0:4] + "." + end[4:6] + "." + end[-2:]

    new_line = ""
    for s in str_array:
        new_line += s + ","

    return new_line[0:-1]


if __name__ == "__main__":
    file_path = "G:\\Temp\\sfz20180131.txt"
    read_file(file_path)
