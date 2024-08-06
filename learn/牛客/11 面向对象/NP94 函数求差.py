#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    : NP94 函数求差.py
@Author  : ChenLiRui
@Time    : 2024/7/26 下午4:16
@explain : 文件说明
"""


def cal(a, b):
    return a - b


if __name__ == '__main__':
    x = int(input())
    y = int(input())

    result1 = cal(x, y)
    result2 = cal(y, x)

    print(result1)
    print(result2)
    pass
