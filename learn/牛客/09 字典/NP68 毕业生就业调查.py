#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    : NP68 毕业生就业调查.py
@Author  : ChenLiRui
@Time    : 2024/7/26 下午2:20
@explain : 文件说明
"""

if __name__ == '__main__':
    survey_list = ['Niumei','Niu Ke Le','GURR','LOLO']
    result_dict = {'Niumei': 'Nowcoder','GURR': 'HUAWEI'}
    for survey in survey_list:
        if survey in result_dict.keys():
            print(f'Hi, {survey}! Thank you for participating in our graduation survey!')
        else:
            print(f'Hi, {survey}! Could you take part in our graduation survey?')
    pass
