#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    : NP55 2的次方数.py
@Author  : ChenLiRui
@Time    : 2024/7/26 上午9:16
@explain : 文件说明
"""

if __name__ == '__main__':
    my_list = []
    min = 1
    max = 10
    for i in range(min, max + 1):
        my_list.append(2 ** i)
    for my in my_list:
        print(my)
    pass
