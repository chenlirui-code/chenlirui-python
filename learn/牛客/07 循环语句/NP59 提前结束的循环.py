#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    : NP59 提前结束的循环.py
@Author  : ChenLiRui
@Time    : 2024/7/26 上午9:47
@explain : 文件说明
"""

if __name__ == '__main__':
    my_list = [3, 45, 9, 8, 12, 89, 103, 42, 54, 79]
    num = input()
    for i in my_list:
        if i == int(num):
            break
        print(i)
    pass
