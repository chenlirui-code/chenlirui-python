#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    : taobao.py
@Author  : ChenLiRui
@Time    : 2024/8/9 下午3:15
@explain : 文件说明
"""
import re
import time
from pyquery import PyQuery as pq
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from utils.database.DatabaseUtils import DatabaseUtils

# 搜索关键词
KEYWORD = '药品'
# MongoDB 表名
MONGO_TABLE = 'drug'
# 设置 Chrome 的调试地址
chrome_options = Options()
chrome_options.debugger_address = 'localhost:9223'

# 指定 ChromeDriver 的路径
service = Service(executable_path='C:/Program Files/Google/Chrome/Application/chromedriver.exe')  # 替换为实际的路径
browser = webdriver.Chrome(service=service, options=chrome_options)
# 设置 WebDriver 等待时间为 60 秒
wait = WebDriverWait(browser, 60)
# 连接到 MySQL 本地服务器 taobao
conn = DatabaseUtils.create_connection('localhost', 'root', '1202', 'taobao')
cursor = conn.cursor()


def search_page():
    """
    打开淘宝首页，搜索关键词，获取总页数，并抓取第一页的商品信息。
    """
    print('正在搜索')
    try:
        # 打开淘宝首页
        browser.get('https://www.taobao.com')
        # 等待搜索输入框出现
        search_input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#q"))
        )
        # 等待提交按钮可点击
        submit = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#J_TSearchForm > div.search-button > button'))
        )
        # 输入关键词并点击搜索按钮
        search_input.send_keys(KEYWORD)
        submit.click()
        # 等待总页数元素出现
        total = wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, '#sortBarWrap > div > div > div > div > div > span.next-pagination-display'))
        )
        total = int(total.text.split('/')[1].strip())
        # 获取第一页的商品信息
        get_products()
        # 打印总页数
        return total
    except TimeoutException:
        # 处理超时异常，递归调用自身重新尝试
        return search_page()


def next_page(page_number):
    """
    翻到指定的页面并抓取商品信息。
    """
    print('翻页中', page_number)
    try:
        # 等待页码输入框出现
        page_input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#mainsrp-pager > div > div > div > div.form > input"))
        )
        # 等待提交按钮可点击
        submit = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.form > span.btn.J_Submit'))
        )
        # 清空输入框，输入目标页码并提交
        page_input.clear()
        page_input.send_keys(page_number)
        submit.click()
        # 等待当前页码显示正确
        wait.until(EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > ul > li.item.active > span'), str(page_number))
        )
        # 获取当前页的商品信息
        get_products()
    except TimeoutException:
        # 处理超时异常，递归调用自身重新尝试
        next_page(page_number)


def get_products():
    """
    获取当前页面的商品信息并保存到 MongoDB。
    """
    # 等待商品列表出现
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-itemlist .items .item')))
    # 获取当前页面 HTML 内容
    html = browser.page_source
    # 用 PyQuery 解析 HTML
    doc = pq(html)
    # 提取商品信息
    items = doc('#mainsrp-itemlist .items .item').items()
    for item in items:
        # 创建商品字典
        product = {
            'price': item.find('.price').text(),
            'deal': item.find('.deal-cnt').text()[:-3],  # 处理销量字段，去掉最后的“笔”
            'title': item.find('.title').text(),
            'shop': item.find('.shop').text(),
            'location': item.find('.location').text()
        }
        # 打印商品信息
        print(product)
        # 保存商品信息到 MongoDB
        save_to_mongo(product)


def save_to_mongo(result):
    """
    将商品信息存储到 MongoDB 数据库。
    """
    try:
        print(result)
        # 插入数据到 MySQL
        # if db[MONGO_TABLE].insert(result):
        #     print('存储成功', result)
    except Exception:
        # 处理存储失败的情况
        print('存储失败', result)


def main():
    """
    主函数：执行搜索、翻页及数据抓取操作。
    """
    try:
        # 执行搜索，获取总页数
        total = search_page()
        # 提取页数
        total = int(re.compile('(\d+)').search(total).group(1))
        # 遍历每一页，抓取商品信息
        for i in range(2, total + 1):
            # 每次翻页之间等待 3 秒
            time.sleep(3)
            next_page(i)
    except Exception:
        # 处理抓取过程中的错误
        print('爬取错误')
    finally:
        # 关闭浏览器
        browser.close()


if __name__ == '__main__':
    # 执行主函数
    main()
