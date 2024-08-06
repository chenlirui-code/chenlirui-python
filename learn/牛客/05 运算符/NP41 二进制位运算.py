#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
@Project :python 
@File    :NP41 二进制位运算.py
@IDE     :PyCharm 
@Author  :Chen LiRui
@Date    :2024/7/15 8:42 
@explain : 文件说明
"""

if __name__ == '__main__':
    num_list = input().split()
    num = int(num_list[0])
    num2 = int(num_list[1])
    print(num & num2)
    print(num | num2)
    pass

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
