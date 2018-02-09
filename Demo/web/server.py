#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 启动一个web服务器，针对请求进行响应
# Python内置了一个WSGI服务器，这个模块叫wsgiref，它是用纯Python编写的WSGI服务器的参考实现
from wsgiref.simple_server import make_server


def application(environ, start_response):
    start_response("200 OK", [("Content-Type", "text/html")])
    body = "<h1>Hello, %s!</h1>" % (environ["PATH_INFO"][1:] or "Felix")
    return [body.encode("utf-8")]

httpd = make_server("", 8000, application)
print("Serving HTTP on port 8000")
httpd.serve_forever()
