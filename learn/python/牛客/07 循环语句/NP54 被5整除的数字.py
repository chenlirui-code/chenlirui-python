#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    : NP54 被5整除的数字.py
@Author  : ChenLiRui
@Time    : 2024/7/26 上午9:10
@explain : 文件说明
"""

if __name__ == '__main__':
    min = 1
    max = 50
    my_list = []
    for num in range(min, max + 1):
        if num % 5 == 0:
            my_list.append(num)
    for my in my_list:
        print(my)
    pass
