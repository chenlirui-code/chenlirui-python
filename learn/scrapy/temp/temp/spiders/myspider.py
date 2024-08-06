#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    : myspider.py
@Author  : ChenLiRui
@Time    : 2024/8/6 下午6:07
@explain : 文件说明
"""
import scrapy


class MySpider(scrapy.Spider):
    name = 'myspider'  # Spider的名称

    # 允许的域名，防止Spider爬取到其他域名下的网页
    allowed_domains = ['quotes.toscrape.com']

    # 起始URL列表，Spider从这些URL开始抓取数据
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]

    def parse(self, response):
        # 解析函数，处理每个响应
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('span small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }

        # 获取下一页的URL并继续处理
        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
