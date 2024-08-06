#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    : NP96 球的表面积.py
@Author  : ChenLiRui
@Time    : 2024/7/26 下午4:30
@explain : 文件说明
"""
import math


def sphere_area(r):
    π = math.pi
    return round((4 * π * r ** 2),2)


if __name__ == '__main__':
    arr = [1, 2, 4, 9, 10, 13]
    for r in arr:
        print(sphere_area(r))
    pass
