#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    : NP58 找到HR.py
@Author  : ChenLiRui
@Time    : 2024/7/26 上午9:43
@explain : 文件说明
"""

if __name__ == '__main__':
    users_list = [
        'Niuniu', 'Niumei', 'HR',
        'Niu Ke Le', 'GURR', 'LOLO'
    ]
    for users in users_list:
        if 'HR' == users:
            print('Hi, HR! Would you like to hire someone?')
        else:
            print(f'Hi, {users}!Welcome to Nowcoder!')
    print()
    pass
