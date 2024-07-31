#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    : NP103 截断电话号码.py
@Author  : ChenLiRui
@Time    : 2024/7/26 下午5:27
@explain : 文件说明
"""
import re

if __name__ == '__main__':
    string = input()
    match = re.match(r'[\d-]+', string)
    if match:
        print(match.group())
    pass
