#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    : 01-xpath解析.py
@Author  : ChenLiRui
@Time    : 2024/7/28 上午9:21
@explain : 数据解析 xpath
"""
# 导入网络请求
import requests
from lxml import etree

# 明确数据
url = 'https://www.douban.com/group/explore'

# 请求发送
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'
}
# 模拟浏览器行为
# res = requests.get(url, headers=headers)
res = requests.request('GET', url=url, headers=headers)
# 数据解析
# print(res.text)
# 使用xpath提取数据 pip install lxml
html = etree.HTML(res.text)
data_list = html.xpath('////*[@id="content"]/div/div[1]/div[1]/div')
# print(data_list)
for data in data_list:
    print(data.xpath('.//a/text()'))
    print("=============================================================================================")