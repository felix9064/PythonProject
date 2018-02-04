#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# html页面下载器
import urllib.request as urllib


class HtmlDownloader(object):

    def download(self, url):
        if url is None:
            return None
        request = urllib.Request(url)
        request.add_header("user-agent", "Mozilla/5.0")
        response = urllib.urlopen(request)
        if response.getcode() != 200:
            return None
        return response.read()
