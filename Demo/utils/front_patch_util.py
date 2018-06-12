#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import re
import shutil


class FrontPatchUtil:
    def __init__(self):
        self.delete_file_set = set()
        self.update_file_set = set()

    def parse(self, front_dir):
        """解析version.changes文件，将要删除的文件和要更新的文件列表放到对应的set集合中"""
        os.chdir(front_dir)
        abs_file = os.path.join(front_dir, r"workspace\jiangyin\trans\convert\patch\version.changes")
        if not os.path.isfile(abs_file):
            print('patch目录下没有version.changes文件')
            return

        current = ""
        with open(abs_file, mode='r', encoding='utf-8') as f:
            for line in f.readlines():
                if line.isspace():
                    continue
                if line.strip().startswith('#'):
                    continue
                if line.strip().startswith("["):
                    regex = re.compile('^\[\w+\]$')
                    m = regex.match(line.strip())
                    if m is not None:
                        current = m.group()
                else:
                    if current == '[DeleteFiles]':
                        self.delete_file_set.add(line.strip())
                    elif current == '[UpdateFiles]':
                        self.update_file_set.add(line.strip())

    def copy_update_file(self, src, destination):
        for update_file in self.update_file_set:
            shutil.copy(os.path.join(src, update_file), os.path.join(destination, update_file))

    def delete_file(self, destination):
        """删除指定目录下的存在于delete_file_set中的文件"""
        if not os.path.isabs(destination):
            print('目标目录%s不是一个绝对路径目录' % destination)
            return None
        if not os.path.exists(destination):
            print('目标目录%s不存在' % destination)
            return None
        if not os.path.isdir(destination):
            print('%s不是一个目录' % destination)
            return None

        for del_file in self.delete_file_set:
            abs_dir = os.path.join(destination, del_file.strip())
            if not os.path.isfile(abs_dir):
                print('%s不是一个文件' % abs_dir)
                continue
            os.unlink(abs_dir)


if __name__ == "__main__":
    front = FrontPatchUtil()
    s_dir = r'E:\Sunline\JRCBank\code\front'
    front.parse(s_dir)
    print(front.delete_file_set)
    d_dir = r'E:\Sunline\JRCBank\code\测试流\front'
    if len(front.delete_file_set) > 0:
        front.delete_file(s_dir)
    if len(front.update_file_set) > 0:
        front.copy_update_file(s_dir, d_dir)
