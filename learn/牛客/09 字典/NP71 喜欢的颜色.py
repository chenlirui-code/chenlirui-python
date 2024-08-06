#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    : NP71 喜欢的颜色.py
@Author  : ChenLiRui
@Time    : 2024/7/26 下午2:45
@explain : 文件说明
"""

if __name__ == '__main__':
    result_dict = {
        'Allen': ['red', 'blue', 'yellow'],
        'Tom': ['green', 'white', 'blue'],
        'Andy': ['black', 'pink']
    }

    for name in sorted(result_dict.keys()):
        print(f"{name}'s favorite colors are:")
        for color in result_dict[name]:
            print(color)
    pass
