#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    : test_log.py
@Author  : ChenLiRui
@Time    : 2024/8/1 下午4:06
@explain : 文件说明
"""

from utils.logging_util import logger


try:
    # 这里模拟一个可能出错的操作
    result = 1 / 0
except Exception as e:
    logger.error('发生错误: %s', e)