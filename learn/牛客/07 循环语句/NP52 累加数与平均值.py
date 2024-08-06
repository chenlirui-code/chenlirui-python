#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    : NP52 累加数与平均值.py
@Author  : ChenLiRui
@Time    : 2024/7/26 上午9:02
@explain : 文件说明
"""

if __name__ == '__main__':
    str = input()
    list = str.split(" ")
    sum = 0
    for e in list:
        sum += int(e)
    pverage = sum / len(list)
    print(sum, " ", pverage)
    pass
