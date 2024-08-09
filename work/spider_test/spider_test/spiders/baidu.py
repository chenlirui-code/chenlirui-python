#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    : baidu.py
@Author  : ChenLiRui
@Time    : 2024/8/7 下午2:34
@explain : 百度练习
"""
import scrapy
from bs4 import BeautifulSoup


class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['baidu.com']
    start_urls = ['https://www.baidu.com']

    def start_requests(self):
        headers = {
            "accept": "application/json, text/javascript, */*; q=0.01",
            "accept-encoding": "gzip, deflate, br, zstd",
            "accept-language": "zh-CN,zh;q=0.9",
            "cache-control": "no-cache",
            "connection": "keep-alive",
            "cookie": "BD_UPN=12314753; PSTM=1722133482; BAIDUID=88DD5D6ADC696388ED636F11DC33356B:FG=1; BIDUPSID=7B27933E8AB8F8BEEA4B607368C77385; BAIDUID_BFESS=88DD5D6ADC696388ED636F11DC33356B:FG=1; ZFY=DFcVL4uWn42xEZFsTabf889bJJCvWATHEYpW4It6sZI:C; Hm_lvt_aec699bb6442ba076c8981c6dc490771=1722134011; H_PS_PSSID=60516_60521_60568_60576; BA_HECTOR=8k0k0g20858hah2h2g8lak0h849qss1jb64mp1u; H_PS_645EC=ed4bwjV96qQSyJVx3imj%2BO%2FdhLBVQHuHkd0pqjFHaPVOdAVjbLjVgrrwW84; baikeVisitId=ba6f34c4-6212-4a7b-8b01-99819d9a8b51; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; COOKIE_SESSION=689925_4_4_7_3_2_1_0_4_2_0_0_187604_689976_0_1_1722321889_1723011814_1723011813%7C8%23689976_6_1723011813%7C3; BD_HOME=1",
            "host": "www.baidu.com",
            "pragma": "no-cache",
            "ps-dataurlconfigqid": "0xb81b5bba00040287",
            "referer": "https://www.baidu.com/",
            "sec-ch-ua": '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "Windows",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
        }
        for url in self.start_urls:
            yield scrapy.Request(url, headers=headers, callback=self.parse)

    def parse(self, response):
        # 在此处编写您的处理逻辑，例如提取页面中的某些信息

        soup = BeautifulSoup(response.text, 'html.parser')

        # 找到所有满足条件的 a 标签
        a_tags = soup.find_all('a', attrs={'target': '_blank', 'class': 'mnav c-font-normal c-color-t'})

        with open('E:\\Code\\python\\chenlirui\\work\\spider_test\\txt\\baidu.txt', 'w', encoding='utf-8') as f:
            f.write(str(a_tags))
        pass
