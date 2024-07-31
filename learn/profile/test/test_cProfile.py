#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import cProfile
import time

"""
@Project :python 
@File    :test_cProfile.py
@IDE     :PyCharm 
@Author  :Chen LiRui
@Date    :2024/7/15 9:13 
@explain : 文件说明
"""


def slow_function():
    time.sleep(2)
    print("Function completed")


def main():
    cProfile.run('slow_function()')


if __name__ == "__main__":
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
