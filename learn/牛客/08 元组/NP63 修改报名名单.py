#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    : NP63 修改报名名单.py
@Author  : ChenLiRui
@Time    : 2024/7/26 上午11:40
@explain : 文件说明
"""

if __name__ == '__main__':
    try:
        entry_form = 'Niuniu', 'Niumei'
        print(entry_form)
        entry_form[1] = 'Niukele'
    except Exception:
        print('The entry form cannot be modified!')
    pass
