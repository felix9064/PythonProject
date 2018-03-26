#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 爬取豆瓣上超过指定评分的书籍信息

import requests
import time
from bs4 import BeautifulSoup


class Book:
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    def craw(self, url):
        self.new_urls.add(url)
        count = 1
        while len(self.new_urls) != 0:
            new_url = self.get_new_url()
            print('开始处理第 %d 个页面：%s' % (count, new_url))
            self.save_book(new_url)
            if count > 2000:
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

    def save_book(self, url):
        # 请求url页面，并创建BeautifulSoup解析对象
        html = self.request(url)
        bs = BeautifulSoup(html.text, 'lxml')

        # 先解析当前页面中的其他书籍的超链接，将得到的url放入未解析url集合中
        self.find_more_url(bs)

        # 书名
        book_name = str(bs.find('h1').find('span').get_text()).strip()

        # 评分
        strong = bs.find('strong', class_='rating_num')
        if strong is None:
            print('当前书籍没有评分', book_name)
            return

        book_score = str(strong.get_text()).strip()
        if book_score == '':
            print('当前书籍没有评分', book_name)
            return

        if float(book_score) < 7.0:
            return

        print(book_name, book_score)

        # 解析当前书籍的信息
        dct = dict()
        dct['book_name'] = book_name
        dct['book_score'] = book_score
        dct['book_url'] = url

        self.write_file(dct)

    def find_more_url(self, bs):
        div = bs.find('div', id='db-rec-section').find('div')
        for dl in div.find_all('dl'):
            dt = dl.find('dt')
            if dt is not None:
                href = dt.find('a')['href']
                self.add_new_url(href)

    @staticmethod
    def request(url):
        """这个函数获取网页的response"""
        headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                          "(KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36",
            'Referer': "https://book.douban.com/"
        }
        content = requests.get(url, headers=headers)
        return content

    @staticmethod
    def write_file(dct):
        """ 将一本书籍的相关信息写入txt文件 """
        if not isinstance(dct, dict):
            print('传入的参数不是字典')
            return

        with open(r'E:\\books.txt', 'a', encoding='utf-8') as f:
            f.write('书名：%s\n' % dct['book_name'])
            f.write('评分：%s\n' % dct['book_score'])
            f.write('地址：%s\n' % dct['book_url'])
            f.write('\n')

        time.sleep(2)

if __name__ == "__main__":
    root_url = r"https://book.douban.com/subject/27614904/"
    book = Book()
    book.craw(root_url)
