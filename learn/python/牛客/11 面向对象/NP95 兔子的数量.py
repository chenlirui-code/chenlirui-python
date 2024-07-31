#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    : NP95 兔子的数量.py
@Author  : ChenLiRui
@Time    : 2024/7/26 下午4:19
@explain : 文件说明
"""


def fibonacci(n):
    if n <= 1:
        return 2
    elif n == 2:
        return 3
    else:
        return fibonacci(n-1) + fibonacci(n-2)


if __name__ == '__main__':
    n = int(input())
    print(fibonacci(n))
    pass
