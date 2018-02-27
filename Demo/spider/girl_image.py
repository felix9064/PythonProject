#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 爬取妹子图网站（http://www.mzitu.com/all）列表里面的所有图片

import requests
from bs4 import BeautifulSoup
import os
import re


class GirlImage:

    def all_url(self, url):
        """ 根据传入的根url，获取所有待爬取的url """
        html = self.request(url)
        all_a = BeautifulSoup(html.text, 'lxml').find('div', class_='all').find_all('a', href=re.compile('[0-9]+'))
        for a in all_a:
            # <a href="http://www.mzitu.com/122236" target="_blank">妖媚熟女雪千寻惹火福利图</a>
            print('------开始保存：', a.get_text())
            href = a['href']
            # path = 122236
            path = str(href).split('/')[-1]

            # 调用 makedir 函数创建文件夹，这儿path代表的是代号122236
            if self.makedir(path):
                self.html(href)

    @staticmethod
    def request(url):
        """这个函数获取网页的response 然后返回"""
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36',
            'referer': "http://www.mzitu.com/100260/2"
        }
        content = requests.get(url, headers=headers)
        return content

    @staticmethod
    def makedir(path):
        """创建图集文件夹"""
        path = path.strip()
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

    def html(self, href):
        """ 获得图片的页面地址 """
        html = self.request(href)
        # 每个图集包含的图片数量
        max_span = BeautifulSoup(html.text, 'lxml').find('div', class_='pagenavi').find_all('span')[-2].get_text()
        # 根据图集的url获取包含的每张图片所在页面的url
        for page in range(1, int(max_span) + 1):
            # http://www.mzitu.com/122236/1
            page_url = href + '/' + str(page)
            self.img_url(page_url)

    def img_url(self, page_url):
        """ 处理图片所在页面地址获得图片的实际地址 """
        img_html = self.request(page_url)
        img_url = BeautifulSoup(img_html.text, 'lxml').find('div', class_='main-image').find('img')['src']
        self.save_img(img_url)

    def save_img(self, img_url):
        """ 保存图片 """
        # name = 25c01
        name = img_url[-9:-4]
        img = self.request(img_url)
        with open(name + '.jpg', 'ab') as f:
            f.write(img.content)

if __name__ == "__main__":
    girl = GirlImage()
    girl.all_url('http://www.mzitu.com/all')
