#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    : time.py
@Author  : ChenLiRui
@Time    : 2024/7/28 下午12:35
@explain : 文件说明
"""
import math
import time
import random

if __name__ == '__main__':
    mysticTime = str(math.ceil(time.time() * 1000) + random.randint(0, 9))
    print('MysticTime:', mysticTime)
    pass
