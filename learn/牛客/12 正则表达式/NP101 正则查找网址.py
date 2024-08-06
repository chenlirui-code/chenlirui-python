#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    : NP101 正则查找网址.py
@Author  : ChenLiRui
@Time    : 2024/7/26 下午5:24
@explain : 文件说明
"""
import re

if __name__ == '__main__':
    url = input()
    match = re.match(r'https://www', url)
    if match:
        print(match.span())
    else:
        print("(0, 0)")
    pass
