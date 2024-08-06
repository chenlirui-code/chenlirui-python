#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    : NP90 修正错误的字母.py
@Author  : ChenLiRui
@Time    : 2024/7/26 下午3:49
@explain : 文件说明
"""

if __name__ == '__main__':
    name = input()
    corrected_name = name.replace('a*', 'ab')
    print(corrected_name)
    pass
