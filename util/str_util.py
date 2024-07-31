#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    : str_util.py
@Author  : ChenLiRui
@Time    : 2024/7/30 上午11:49
@explain : 字符串工具类
"""


class StrUtils:
    @staticmethod
    def is_not_empty(obj):
        """
        判断一个对象的内容是否为空
        """
        if isinstance(obj, str):
            return obj and len(obj.strip()) > 0
        elif isinstance(obj, list):
            return len(obj) > 0
        elif isinstance(obj, dict):
            return len(obj) > 0
        elif hasattr(obj, '__len__'):
            return len(obj) > 0
        else:
            return False

    @staticmethod
    def equals(obj1, obj2):
        """
        比较的obj1和obj2是否相等
        """
        if obj1 is None or obj2 is None:
            return False
        obj1_stripped = obj1.replace(" ", "")
        obj2_stripped = obj2.replace(" ", "")
        if obj1_stripped == obj2_stripped:
            return True
        else:
            return False
