#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    : NP61 牛牛的矩阵相加.py
@Author  : ChenLiRui
@Time    : 2024/7/26 上午10:07
@explain : 文件说明
"""

if __name__ == '__main__':
    arr = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    n = int(input())
    for x in range(len(arr)):
        for y in range(len(arr[x])):
            arr[x][y] *= n
    print(arr)
    pass
