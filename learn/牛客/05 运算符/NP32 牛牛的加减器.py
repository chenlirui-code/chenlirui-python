# -*- coding: UTF-8 -*-

"""
@Project ：python 
@File    ：NP32 牛牛的加减器.py
@IDE     ：PyCharm 
@Author  ：Chen LiRui
@Date    ：2024/7/14 上午10:19 
@explain : 文件说明
"""


def Add_Sub(x, y):
    sum = x + y
    substract = x - y
    return sum, substract


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    sum, substract = Add_Sub(x, y)
    print(sum, substract, sep='\n')
    pass
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
