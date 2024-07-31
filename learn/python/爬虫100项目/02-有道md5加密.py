#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    : 02-有道md5加密.py
@Author  : ChenLiRui
@Time    : 2024/7/28 下午12:05
@explain : 有道翻译 md5加密
"""

# 导入网络请求
import requests, time, random, math, hashlib


def md5(e):
    msg = e  # 这里假设 e 已经是字符串类型，如果不是，需要先进行适当的转换
    return hashlib.md5(msg.encode('utf-8')).hexdigest()


def S(e):
    return md5(f"client=fanyideskweb&mysticTime={e}&product=webfanyi&key=asdjnjfenknafdfsdfsd")


def translate(key):
    request = requests.session()
    print(math.ceil(time.time() * 1000))
    # 1722221593321     1722221662909
    # 1677916351.720945     1677916351.720945
    # -1811584449@219.140.235.172       -1811584449@219.140.235.172
    # 定义 Cookie
    cookies = {
        "OUTFOX_SEARCH_USER_ID": "1204204223@219.140.235.172",
        "OUTFOX_SEARCH_USER_ID_NCOO": "562866647.8482826",
        "___rl__test__cookies": str(math.ceil(time.time() * 1000)),
    }

    headers = {
        'accept': 'application/json, text/plain, */*',
        'content-type': 'application/x-www-form-urlencoded',
        'referer': 'https://fanyi.youdao.com/',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': 'Windows',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    }
    mysticTime = str(math.ceil(time.time() * 1000) + random.randint(0, 9))[:-1]
    print('MysticTime:', mysticTime)
    # 8a3c8cc308b5e9efd2f597aaf26a8972    8a3c8cc308b5e9efd2f597aaf26a8972
    sign = S(mysticTime)
    print('Sign:', sign)
    # key mysticTime  sign
    data = {
        'i': key,
        'from': 'auto',
        'to': '',
        'useTerm': 'false',
        'domain': 0,
        'dictResult': 'true',
        'keyid': 'webfanyi',
        'sign': sign,
        'client': 'fanyideskweb',
        'product': 'webfanyi',
        'appVersion': '1.0.0',
        'vendor': 'web',
        'pointParam': "client,mysticTime,product",
        'mysticTime': str(mysticTime),
        'keyfrom': 'fanyi.web',
        'mid': 1,
        'screen': 1,
        'model': 1,
        'network': 'wifi',
        'abtest': 0,
        'yduuid': 'abcdefg'
    }
    res = request.post(
        'https://dict.youdao.com/webtranslate',
        headers=headers,
        cookies=cookies,
        data=data
    )
    print('-------------------------')
    print(res.status_code)
    print(res.text)
    if res.status_code == 200:
        print(res.json())

    get_headers = {
        'accept': 'application/json, text/plain, */*',
        'referer': 'https://fanyi.youdao.com/',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': 'Windows',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    }
    get_data = {
        'keyid': 'webfanyi-key-getter',
        'sign': sign,
        'client': 'fanyideskweb',
        'product': 'webfanyi',
        'appVersion': '1.0.0',
        'vendor': 'web',
        'pointParam': "client,mysticTime,product",
        'mysticTime': mysticTime,
        'keyfrom': 'fanyi.web',
        'mid': 1,
        'screen': 1,
        'model': 1,
        'network': 'wifi',
        'abtest': 0,
        'yduuid': 'abcdefg'
    }
    res = request.get(
        'https://dict.youdao.com/webtranslate/key',
        headers=get_headers,
        cookies=cookies,
        data=get_data
    )
    print('-------------------------')
    print(res.status_code)
    print(res.text)
    if res.status_code == 200:
        print(res.json())


pass

if __name__ == '__main__':
    s = input('请输入想输入的单词：')
    translate(s)  # 调用方法
