#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    : NP72 生成字典.py
@Author  : ChenLiRui
@Time    : 2024/7/26 下午2:47
@explain : 文件说明
"""

if __name__ == '__main__':
    names = input().split()
    languages = input().split()

    user_dict = dict(zip(names, languages))
    print(user_dict)
    pass
