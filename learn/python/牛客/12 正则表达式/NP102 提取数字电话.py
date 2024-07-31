#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    : NP102 提取数字电话.py
@Author  : ChenLiRui
@Time    : 2024/7/26 下午5:26
@explain : 文件说明
"""
import re

if __name__ == '__main__':
    string = input()
    phone_number = re.sub(r'\D', '', string)
    print(phone_number)
    pass
