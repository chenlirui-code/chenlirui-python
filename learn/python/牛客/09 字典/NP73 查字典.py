#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    : NP73 查字典.py
@Author  : ChenLiRui
@Time    : 2024/7/26 下午2:50
@explain : 文件说明
"""

if __name__ == '__main__':
    my_dict = {
        'a': ['apple', 'abandon', 'ant'],
        'b': ['banana', 'bee', 'become'],
        'c': ['cat', 'come'], 'd': 'down'
    }

    letter = input()
    if isinstance(my_dict[letter], list):
        for word in my_dict[letter]:
            print(word, end=" ")
    else:
        print(my_dict[letter])
    pass
