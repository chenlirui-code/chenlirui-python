#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    : NP75 使用字典计数.py
@Author  : ChenLiRui
@Time    : 2024/7/26 下午3:04
@explain : 文件说明
"""

if __name__ == '__main__':
    word = input()
    count_dict = {}

    for char in word:
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1

    print(count_dict)
    pass
