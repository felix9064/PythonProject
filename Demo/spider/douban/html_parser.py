#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 解析html页面
import re
import urllib.parse as urlparse
from bs4 import BeautifulSoup


class HtmlParser(object):

    def parse(self, page_url, html_content):
        if page_url is None or html_content is None:
            return

        soup = BeautifulSoup(html_content, 'html.parser', from_encoding='utf-8')
        new_urls = self.get_new_urls(page_url, soup)
        new_data = self.get_new_data(page_url, soup)
        return new_urls, new_data

    @staticmethod
    def get_new_data(page_url, soup):
        res_data = {}
        '''
        # <dd class="lemmaWgt-lemmaTitle-title"><h1>Python</h1>
        title_node = soup.find("dd", class_="lemmaWgt-lemmaTitle-title").find("h1")
        res_data["title"] = title_node.get_text()

        # <div class="lemma-summary" label-module="lemmaSummary">
        summary_node = soup.find("div", class_="lemma-summary")
        if summary_node is None:
            summary_node = soup.find("div", class_="lemmaWgt-subLemmaListTitle")
        res_data["summary"] = summary_node.get_text()
        '''

        # <span property="v:itemreviewed">心灵捕手 Good Will Hunting</span>
        name = soup.find("div", id="content").find("h1").find("span")
        res_data["title"] = name.get_text()

        # <strong class="ll rating_num" property="v:average">8.8</strong>
        score = soup.find("div", class_="rating_self").find("strong")
        res_data["score"] = score.get_text()

        res_data["url"] = page_url

        return res_data

    @staticmethod
    def get_new_urls(page_urls, soup):
        new_urls = set()
        # links = soup.find_all('a', href=re.compile(r"/item/\S+"))
        links = soup.find_all('a', href=re.compile(r"https://movie.douban.com/subject/\d+/\?from=subject-page"))
        for link in links:
            #new_url = link['href']
            #new_full_url = urlparse.urljoin(page_urls, new_url)
            new_urls.add(link['href'])
        return new_urls
