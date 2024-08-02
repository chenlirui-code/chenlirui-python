#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    : test_text.py
@Author  : ChenLiRui
@Time    : 2024/8/2 上午10:06
@explain : 文件说明
"""
from utils.text_util import TextUtils

if __name__ == '__main__':

    s = input()

    data = TextUtils.convert_unicode_to_text(s)

    print(data)
    pass
