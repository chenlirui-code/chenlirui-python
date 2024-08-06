#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project :python 
@File    :NP47 牛牛的绩点.py
@IDE     :PyCharm 
@Author  :Chen LiRui
@Date    :2024/7/16 上午8:57 
@explain : 文件说明
"""

if __name__ == '__main__':
    dic_1 = {'A': 4.0, 'B': 3.0, 'C': 2.0, 'D': 1.0, 'F': 0}
    # 成绩总和
    sum1 = 0
    # 学分总和
    sum2 = 0
    while True:
        # 绩点
        a = input()
        if a.lower() == 'false':
            break
        # 学分
        b = int(input())
        # 成绩总和 = 绩点*学分，每轮加一次
        sum1 += dic_1[a] * b
        # 每轮加学分总和
        sum2 += b

        # 每门课学分乘上单门课绩点，求和后对学分求均值
    print('%.2f' % (sum1 / sum2))
    pass

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
