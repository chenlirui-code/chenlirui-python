#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    : NP93 创建集合.py
@Author  : ChenLiRui
@Time    : 2024/7/26 下午4:12
@explain : 文件说明
"""

if __name__ == '__main__':
    names = input().split()
    name_set = set(names)
    sorted_set = sorted(name_set)
    print(sorted_set)
    pass
