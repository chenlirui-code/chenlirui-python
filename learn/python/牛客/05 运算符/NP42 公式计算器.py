#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project :python 
@File    :NP42 公式计算器.py
@IDE     :PyCharm 
@Author  :Chen LiRui
@Date    :2024/7/15 下午6:04 
@explain : 文件说明
"""

if __name__ == '__main__':
    arr = list(map(int, input().split()))
    end = arr[0] + arr[1]
    end2 = arr[2] - arr[3]
    print(end * end2)
    pass

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
