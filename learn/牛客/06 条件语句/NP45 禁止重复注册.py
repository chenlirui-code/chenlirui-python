#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project :python 
@File    :NP45 禁止重复注册.py
@IDE     :PyCharm 
@Author  :Chen LiRui
@Date    :2024/7/15 下午6:48 
@explain : 文件说明
"""

if __name__ == '__main__':
    current_users = ['Niuniu', 'Niumei', 'GURR', 'LOLO']
    new_users = ['GurR', 'Niu Ke Le', 'LoLo', 'Tuo Rui Chi']
    current_users_L = [i.lower() for i in current_users]
    for new_user in new_users:
        if new_user.lower() in current_users_L:
            print(f'The user name {new_user} has already been registered! Please change it and try again!')
        else:
            print(f'Congratulations, the user name {new_user} is available!')

    pass

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
