#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Topic: 让对象支持上下文管理器，即兼容 with 语句
Desc : 为了让一个对象兼容 with 语句，你需要实现 __enter__() 和 __exit__() 方法
下面的例子是自定义一个网络连接
"""
from socket import socket, AF_INET, SOCK_STREAM
from functools import partial


class LazyConnection:
    """
    这个类的关键特点在于它表示了一个网络连接，但是初始化的时候并不会做任何事情
    (比如它并没有建立一个连接)。连接的建立和关闭是使用 with 语句自动完成的
    """
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = family
        self.type = type
        self.sock = None

    def __enter__(self):
        if self.sock is not None:
            raise RuntimeError('Already Connected')
        self.sock = socket(self.family, self.type)
        self.sock.connect(self.address)
        return self.sock

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.sock.close()
        self.sock = None


if __name__ == '__main__':
    conn = LazyConnection(('www.python.org', 80))
    with conn as s:
        # conn.__enter__() 会执行，连接建立
        s.send(b'GET /index.html HTTP/1.1\r\n')
        s.send(b'Host: www.python.org\r\n')
        s.send(b'\r\n')
        resp = b''.join(iter(partial(s.recv, 8192), b''))
        print(resp)
        # conn.__exit__() 会执行，连接关闭
