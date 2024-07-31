#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Author  :Chen LiRui
@Date    :2024/7/15 上午10:01 
@explain : 测试函数时间
"""
import time

from util.viztracer_util import analyze_function


def profiler_this():
    time.sleep(0.01)
    time.sleep(0.02)
    time.sleep(0.04)
    time.sleep(0.16)
    time.sleep(0.04)
    time.sleep(0.02)
    time.sleep(0.01)


if __name__ == '__main__':
    analyze_function(profiler_this)
    pass

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
