#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 爬虫的调度器
from spider.douban import html_outputer, url_manager, html_downloader, html_parser


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.output = html_outputer.HtmlOutput()

    def craw(self, url):
        count = 1
        self.urls.add_new_url(url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print("开始处理第%d个页面 %s" % (count, new_url))
                html_content = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_content)
                self.urls.add_new_urls(new_urls)
                self.output.collect_data(new_data)
                print("第%d个页面处理完成" % count)
            except Exception as e:
                print('爬取失败 count=%d ' % count)
                print(e)

            if count > 200:
                break

            count += 1
        self.output.output_html()

if __name__ == "__main__":
    # root_url = "https://baike.baidu.com/item/Python/407313"
    root_url = "https://movie.douban.com/subject/1292052/?from=subject-page"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
