#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
@Project :python 
@File    :NP38 牛牛的逻辑运算.py
@IDE     :PyCharm 
@Author  :Chen LiRui
@Date    :2024/7/14 下午3:54 
@explain : 文件说明
"""

if __name__ == '__main__':
    x, y = map(int, input().split())
    print(x and y)
    print(x or y)
    print(not x)
    print(not y)
    pass

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
