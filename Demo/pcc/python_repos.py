#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
r = requests.get(url)
print("状态码：", r.status_code)

response_dict = r.json()
print("GitHub上跟Python有关的库的数量：", response_dict['total_count'])

repo_dicts = response_dict['items']
print("当前请求返回的库的数量：", len(repo_dicts))

repo_dict = repo_dicts[0]
print("每个Python库包含的关键字数量：", len(repo_dict))

for repo_dict in repo_dicts:
    print("\nName:", repo_dict['name'])
    print("Owner:", repo_dict['owner']['login'])
    print("Stars:", repo_dict['stargazers_count'])
    print("Repository:", repo_dict['html_url'])
    print("Description:", repo_dict['description'])
