#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# mac 同时上内外网的路由设置，将以下代码保存为py文件，使用sudo跑py文件

import os
import re


def route():
    # 获取路由表的网关IP地址
    data = os.popen("netstat -rn|awk '{print $2}'").readlines()

    # 外网网关IP的正则表达式
    re_ip1 = re.compile(r'172.16.\d{1,3}.\d{1,3}')

    # 内网网关IP的正则表达式
    re_ip2 = re.compile(r'198.98.\d{1,3}.\d{1,3}')

    ip1 = ""
    ip2 = ""

    for x in data:
        print(x)
        if re_ip1.match(x):
            # 捕获外网网关IP
            ip1 = re_ip1.findall(x)[0]

        if re_ip2.match(x):
            # 捕获内网网关IP
            ip2 = re_ip2.findall(x)[0]
    print(ip1, ip2)

    if ip1 is not None and ip2 is not None:
        pass
        # 删除默认外网路由
        os.popen('route delete 0.0.0.0')
        # 添加内网路由
        os.popen('route -n add -net 198.98.0.0 -netmask 255.0.0.0 %s' % ip2)
        # 添加外网路由
        os.popen('route -n add -net 0.0.0.0 -netmask 0.0.0.0 %s' % ip1)


if __name__ == "__main__":
    route()
