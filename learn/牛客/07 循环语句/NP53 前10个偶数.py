#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    : NP53 前10个偶数.py
@Author  : ChenLiRui
@Time    : 2024/7/26 上午9:07
@explain : 文件说明
"""

if __name__ == '__main__':
    min = 0
    max = 19
    my_list = []
    for i in range(min, max + 1):
        if i % 2 == 0:
            my_list.append(i)
    for data in my_list:
        print(data)
    pass
