#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Topic: collections.deque演示
Desc : deque有一个maxlen参数，当append的时候，如果超过，那么最前面的就被挤出队列。
"""
from collections import deque


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)


if __name__ == "__main__":
    with open("python_file.txt", 'r', encoding="utf-8") as f:
        for line1, prev_lines in search(f, "python", 5):
            for p_line in prev_lines:
                print("列表中的元素 " + p_line)
            print("匹配的行 " + line1)
            print('*' * 30)
