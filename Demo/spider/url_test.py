#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib.request
import http.cookiejar

url = "http://img.mmjpg.com/2018/1271/1io7.jpg"
"""
print("第一种解析方法")
response1 = urllib.request.urlopen(url)
print(response1.getcode())

print("第二种解析方法")
request = urllib.request.Request(url)
request.add_header("user-agent", "Mozilla/5.0")
response2 = urllib.request.urlopen(request)
print(response2.getcode())
print(len(response2.read()))
"""
cookie = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
urllib.request.install_opener(opener)
response3 = urllib.request.urlopen(url)

for k, v in response3.getheaders():
    data = response3.read()
    print('%s: %s' % (k, v))
    # print('Data:', data.decode('utf-8'))
"""
print(response3.getcode())
print(cookie)
print(response3.read())
"""
