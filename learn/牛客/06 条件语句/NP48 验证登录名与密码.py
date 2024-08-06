#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    : NP48 验证登录名与密码.py
@Author  : ChenLiRui
@Time    : 2024/7/26 上午8:42
@explain : 文件说明
"""

if __name__ == '__main__':
    username = input()
    password = input()
    if username == 'admis' and password == 'Nowcoder666':
        print('Welcome!')
    else:
        print('user id or password is not correct!')
