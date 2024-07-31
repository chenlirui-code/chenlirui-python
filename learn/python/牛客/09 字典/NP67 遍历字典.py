#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    : NP67 遍历字典.py
@Author  : ChenLiRui
@Time    : 2024/7/26 下午2:08
@explain : 文件说明
"""

if __name__ == '__main__':
    dict = {}
    dict['<'] = 'less than'
    dict['=='] = 'equal'
    print('Here is the original dict:')
    for e in dict:
        print(f'Operator {e} means {dict[e]}.')
    sorted(dict)

    dict['>'] = 'greater than'
    print()
    print('The dict was changed to:')
    for e in dict:
        print(f'Operator {e} means {dict[e]}.')
    sorted(dict)
    pass
