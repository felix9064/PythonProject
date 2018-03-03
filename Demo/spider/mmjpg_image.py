#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
from bs4 import BeautifulSoup
import time
import requests
import fake_useragent
import os
import random


class GetPic:

    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    def craw(self, root_url):

        self.new_urls.add(root_url)
        count = 1
        while len(self.new_urls) != 0:
            new_url = self.get_new_url()

            dir_str = str(new_url).split('/')
            path = dir_str[-2] + '_' + dir_str[-1]
            if not self.makedir(path):
                continue

            print("开始处理第%d个图集 %s" % (count, new_url))
            self.save_img(new_url)

            if count > 200:
                break

            count += 1

    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url

    def save_img(self, page_url):
        """ 根据图集首页的url来下载整个图集 """
        html = self.request(page_url)

        # 先解析当前页面中的其他图集的超链接，将得到的url放入未解析url集合中
        all_a = BeautifulSoup(html.text, 'lxml').find('div', class_='hot').find_all('a')
        for a in all_a:
            self.new_urls.add(str(a['href']))

        # 计算每个图集包含的图片数量
        max_nums = BeautifulSoup(html.text, 'lxml').find('div', id='page').find_all('a')[-2].get_text()

        # 根据图集的url获取包含的每张图片所在页面的url
        for page in range(1, int(max_nums) + 1):
            img_page = page_url + '/' + str(page)
            img_html = self.request(img_page)
            img_src = BeautifulSoup(img_html.text, 'lxml').find('div', id='content').find('img')['src']
            file_name = str(img_src).split('/')[-1]

            if os.path.exists(file_name):
                time.sleep(1)
                print(file_name + '文件已存在')
                return

            # 保存图片
            img = self.request(img_src)
            with open(file_name, 'wb') as f:
                f.write(img.content)
            time.sleep(random.random() * 3)

    @staticmethod
    def makedir(path):
        """创建图集文件夹，文件夹不能包含\/:*?"<>|这些字符，故需要先去掉这些字符"""
        reg = re.compile('[\\\\/:*?"<>|]')
        path = reg.sub("", str(path.strip()))

        full_path = os.path.join("E:\Image", path)
        if not os.path.exists(full_path):
            print('建了一个名字叫做', path, '的文件夹！')
            os.makedirs(full_path)
            # 切换到新建的目录
            os.chdir(full_path)
            return True
        else:
            print(path, '文件夹已经存在了！')
            return False

    @staticmethod
    def request(url):
        """这个函数获取网页的response"""
        fa = fake_useragent.UserAgent()

        headers = {
            'User-Agent': fa.random,
            'Referer': "http://m.mmjpg.com/"
        }
        content = requests.get(url, headers=headers)
        return content

# 运行程序
if __name__ == '__main__':
    g = GetPic()
    g.craw("http://www.mmjpg.com/mm/6")
