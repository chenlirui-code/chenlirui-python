#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    : NP100 重载运算.py
@Author  : ChenLiRui
@Time    : 2024/7/26 下午4:58
@explain : 文件说明
"""


class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __add__(self, other):
        return Coordinate(self.x + other.x, self.y + other.y)


if __name__ == '__main__':
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())

    c1 = Coordinate(x1, y1)
    c2 = Coordinate(x2, y2)

    result = c1 + c2
    print(result)
    pass
