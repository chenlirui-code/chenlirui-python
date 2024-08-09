#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    : set.py
@Author  : ChenLiRui
@Time    : 2024/8/8 下午3:58
@explain : 文件说明
"""

if __name__ == '__main__':
    if __name__ == '__main__':
        rows = [{'a': 1}, {'b': 2}, {'a': 1}, {'c': 3}]

        unique_rows = set()
        for row in rows:
            unique_rows.add(tuple(row.items()))
        rows2 = [{'a': 12}, {'b': 2}, {'a': 1}, {'c': 32}]
        for row in rows2:
            unique_rows.add(tuple(row.items()))
        print(unique_rows)
    pass
