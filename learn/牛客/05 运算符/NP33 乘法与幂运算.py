#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
@Project ：python 
@File    ：test_line_profiler.py
@IDE     ：PyCharm 
@Author  ：Chen LiRui
@Date    ：2024/7/14 下午3:15 
@explain : 文件说明
"""


def multiply(x, y):
    """
    乘法函数
    """
    return x * y


def monomial(x, y):
    """
    幂函数
    """
    num = 1
    for i in range(y):
        num *= x
    return num


if __name__ == '__main__':
    x = int(input())
    y = int(input())

    mult_sum = multiply(x, y)
    print(mult_sum)

    mon_sum = monomial(x, y)
    print(mon_sum)

    pass

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
