#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    : logging_util.py
@Author  : ChenLiRui
@Time    : 2024/8/1 下午2:11
@explain : 日志
"""

# 引入 logging 模块，并设定logger的级别为DEBUG
import logging

# 设置logger的级别为DEBUG
logging.basicConfig(level=logging.DEBUG)
logging.getLogger().setLevel(logging.DEBUG)
