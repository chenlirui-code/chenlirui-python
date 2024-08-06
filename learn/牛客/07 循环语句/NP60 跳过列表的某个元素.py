#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    : NP60 跳过列表的某个元素.py
@Author  : ChenLiRui
@Time    : 2024/7/26 上午10:00
@explain : 文件说明
"""

if __name__ == '__main__':
    for i in range(1, 16):
        if i == 13:
            continue
        print(i, end=" ")
    pass
