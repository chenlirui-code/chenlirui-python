#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    : NP65 名单中出现过的人.py
@Author  : ChenLiRui
@Time    : 2024/7/26 上午11:54
@explain : 文件说明
"""

if __name__ == '__main__':
    arr = 'Tom', 'Tony', 'Allen', 'Cydin', 'Lucy', 'Anna'
    name = input()
    print(arr)
    if name in arr:
        print('Congratulations!')
    else:
        print('What a pity!')
    pass
