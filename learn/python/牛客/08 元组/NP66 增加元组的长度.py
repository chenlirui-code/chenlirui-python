#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    : NP66 增加元组的长度.py
@Author  : ChenLiRui
@Time    : 2024/7/26 上午11:58
@explain : 文件说明
"""

if __name__ == '__main__':
    old_arr = 1, 2, 3, 4, 5
    print(old_arr)
    print(len(old_arr))
    new_arr = 6, 7, 8, 9, 10
    arr = old_arr + new_arr
    print(arr)
    print(len(arr))  # 15
    pass
