#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
@Project ：python 
@File    ：NP34 除法与取模运算.py
@IDE     ：PyCharm 
@Author  ：Chen LiRui
@Date    ：2024/7/14 下午3:27 
@explain : 文件说明
"""

def division(x,y):
    s = x//y
    yu = x%y
    return s,yu

def decimals(x,y):
    return float(x)/y

if __name__ == '__main__':
    x = int(input())
    y = int(input())

    s,yu = division(x,y)
    print("{} {}".format(s, yu))

    xs = decimals(x,y)
    print('%.2f'%xs)
    pass

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
