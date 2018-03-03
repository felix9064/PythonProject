#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# html页面下载器
import urllib.request


class HtmlDownloader(object):

    @staticmethod
    def download(url):
        if url is None:
            return None
        request = urllib.request.Request(url)
        request.add_header("user-agent", "Mozilla/5.0")
        response = urllib.request.urlopen(request)
        if response.getcode() != 200:
            return None
        return response.read()
