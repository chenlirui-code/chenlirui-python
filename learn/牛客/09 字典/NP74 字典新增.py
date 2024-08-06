#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    : NP74 字典新增.py
@Author  : ChenLiRui
@Time    : 2024/7/26 下午2:54
@explain : 文件说明
"""

if __name__ == '__main__':
    my_dict = {
        'a': ['apple', 'abandon', 'ant'],
        'b': ['banana', 'bee', 'become'],
        'c': ['cat', 'come'],
        'd': 'down'
    }

    letter = input()
    word = input()

    if letter in my_dict:
        my_dict[letter].append(word)
    else:
        my_dict[letter] = [word]

    print(my_dict)
    pass
