#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    : NP82 数学幂运算.py
@Author  : ChenLiRui
@Time    : 2024/7/26 下午3:27
@explain : 文件说明
"""

if __name__ == '__main__':
    x, y = map(int, input().split())

    # 使用两个乘号相连
    result1 = x ** y
    print(result1)

    # 使用 pow 函数
    result2 = pow(y, x)
    print(result2)
    pass
