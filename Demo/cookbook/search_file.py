#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 保留最后N个元素
# 问题1.3：在迭代操作或者其他操作的时候，怎样只保留最后有限几个元素的历史记录？
# 使用collections集合包的deque(maxlen=N) 构造函数会新建一个固定大小的队列。
# 当新的元素加入并且这个队列已满的时候，最老的元素会自动被移除掉

from collections import deque

# 生成器函数


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
                print(p_line, end='')
            print("匹配的行  %s" % line1, end='')
            print('-' * 20)
