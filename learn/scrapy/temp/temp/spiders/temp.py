#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    : temp.py
@Author  : ChenLiRui
@Time    : 2024/8/7 上午8:38
@explain : 一个用于爬取百度页面信息的Scrapy爬虫示例
"""
import scrapy


class BaiduSpider(scrapy.Spider):
    name = "baidu_spider"  # 爬虫的名称
    allowed_domains = ["baidu.com"]  # 允许爬取的域名
    start_urls = [
        "https://www.baidu.com"
    ]  # 起始的 URL 列表

    def parse(self, response):
        # 提取百度页面的标题
        title = response.css('title::text').get()
        print(f"百度页面的标题: {title}")

    def parse_item(self, response):
        # 假设我们要处理搜索结果页面的逻辑
        # 这里可以提取搜索结果的相关信息
        pass

    def handle_error(self, failure):
        # 处理请求失败的情况
        print(f"请求失败: {failure}")
