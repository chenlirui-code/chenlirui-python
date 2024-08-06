#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    : NP69 姓名与学号.py
@Author  : ChenLiRui
@Time    : 2024/7/26 下午2:25
@explain : 文件说明
"""

if __name__ == '__main__':
    my_dict_1 = {'name': 'Niuniu', 'Student ID': 1}
    my_dict_2 = {'name': 'Niumei', 'Student ID': 2}
    my_dict_3 = {'name': 'Niu Ke Le', 'Student ID': 3}

    dict_list = []
    dict_list.append(my_dict_1)
    dict_list.append(my_dict_2)
    dict_list.append(my_dict_3)

    for item in dict_list:
        name = item['name']
        student_id = item['Student ID']
        print(f"{name}'s student id is {student_id}.")
    pass
