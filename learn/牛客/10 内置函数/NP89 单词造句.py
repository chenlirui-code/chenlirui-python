#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    : NP89 单词造句.py
@Author  : ChenLiRui
@Time    : 2024/7/26 下午3:48
@explain : 文件说明
"""

if __name__ == '__main__':
    word_list = []
    word = input()
    while word != '0':
        word_list.append(word)
        word = input()
    sentence = " ".join(word_list)
    print(sentence)
    pass
