#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    : NP70 首都.py
@Author  : ChenLiRui
@Time    : 2024/7/26 下午2:40
@explain : 文件说明
"""

if __name__ == '__main__':
    cities_dict = {
        'Beijing': {'Capital': 'China'},
        'Moscow': {'Capital': 'Russia'},
        'Paris': {'Capital': 'France'}
    }

    for city in sorted(cities_dict.keys()):
        capital = cities_dict[city]['Capital']
        print(f"{city} is the capital of {capital}!")
    pass
