#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@File    ：test_line_profiler.py
@Author  ：Chen LiRui
@Date    ：2024/7/14 下午3:15 
@explain : 文件说明
"""
import time

from line_profiler_pycharm import profile


@profile
def profiler_this():
    time.sleep(0.01)
    time.sleep(0.02)
    time.sleep(0.04)
    time.sleep(0.16)
    time.sleep(0.04)
    time.sleep(0.02)
    time.sleep(0.01)


if __name__ == '__main__':
    profiler_this()
    pass

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
