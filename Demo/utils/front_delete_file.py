# -*- coding: utf-8 -*-
import os


def parse_file(f_home, file_path):
    os.chdir(f_home)
    abs_del_file = os.path.join(f_home, file_path)
    with open(abs_del_file, mode='r', encoding='utf-8') as f:
        for line in f.readlines():
            if line.isspace():
                continue
            if line.startswith('#'):
                continue
            abs_path = os.path.join(f_home, line.strip())
            print('待删除的文件' + abs_path)
            if os.path.isfile(abs_path):
                delete_file(abs_path)


def delete_file(file):
    if os.path.exists(file):
        os.unlink(file)


if __name__ == "__main__":
    front = r'E:\Sunline\JRCBank\code\front'
    f_dir = r'workspace\jiangyin\trans\convert\patch\delete_file'
    parse_file(front, f_dir)
