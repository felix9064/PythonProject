#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 爬取春暖花开论坛的精华帖子中的图片

import os
import fake_useragent
import re
import requests
import time
from bs4 import BeautifulSoup


class Picture:

    def all_url(self, url):
        """一个页面有许多图集，而这样的页面有很多，该方法是根据传入的根url，获取所有的页面url"""
        list_str = url.split('-')
        html = self.request(url)
        last = BeautifulSoup(html.text, 'lxml').find('span', id='fd_page_bottom').find('a', class_='last')['href']
        max_page = str(last).split('-')[-1].split('.')[0]

        for index in range(1, int(max_page) + 1):
            new_url = '%s-%s-%d.html' % (list_str[0], list_str[1], index)
            print('开始处理页面:%s' % new_url)
            self.one_page(new_url)

    def one_page(self, url):
        """处理一个页面中的所有图集"""
        html = self.request(url)
        all_tbody = BeautifulSoup(html.text, 'lxml').find_all('tbody', id=re.compile('(normalthread_)[0-9]+'))
        for tbody in all_tbody:
            href = tbody.find('td', class_='icn').find('a')['href']
            look_time = tbody.find('td', class_='num').em
            name = tbody.find('tr').find('th', class_='new').find('a', class_='s').get_text()

            if int(look_time.get_text()) < 1500:
                continue

            img_url = 'http://%s/%s' % (url.split('/')[2], str(href))
            print('开始处理图集:%s, url:%s' % (name, img_url))
#            path = str(href).split('-')[1]
            self.save_img(img_url, name)
            print('当前图集处理完毕')

    def save_img(self, url, path):
        if self.makedir(path):
            html = self.request(url)
            all_img = BeautifulSoup(html.text, 'lxml').find_all('img', class_='zoom')
            if all_img is None:
                print('当前页面没有图片', url)
                return None

            for img in all_img:
                try:
                    img_url = img['file']
                except KeyError:
                    try:
                        img_url = img['src']
                    except KeyError:
                        print('找不到图片链接', url)
                        continue
                print("开始下载：%s" % img_url)

                try:
                    img = self.request(img_url)
                except requests.exceptions.RequestException as e:
                    print('图片下载失败：', e)
                    continue
                if img.status_code != 200:
                    print('请求失败:%d' % img.status_code)
                    continue

                file_name = str(img_url).split('/')[-1]
                with open(file_name, 'ab') as f:
                    f.write(img.content)

                time.sleep(3)

    @staticmethod
    def makedir(path):
        """创建图集文件夹，文件夹不能包含\/:*?"<>|这些字符，故需要先去掉这些字符"""
        reg = re.compile('[\\\\/:*?"<>|]')
        path = reg.sub("", str(path.strip()))

        full_path = os.path.join("E:\Image\sex", path)
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
        """请求url并返回响应结果"""
        fa = fake_useragent.UserAgent()

        headers = {
            'User-Agent': fa.random,
        }
        content = requests.get(url, headers=headers, timeout=10)
        return content

if __name__ == '__main__':
    p = Picture()
    # p.all_url('http://qqlive8.space/forum-158-1.html')
    p.one_page('http://qqlive8.space/forum-11-4.html')
