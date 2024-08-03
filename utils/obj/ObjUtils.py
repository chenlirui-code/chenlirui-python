#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    : ObjUtils.py
@Author  : ChenLiRui
@Time    : 2024/8/3 下午3:24
@explain : 文件说明
"""
import numpy as np


class ObjUtils:
    @staticmethod
    def equals(obj1, obj2):
        """
        比较的obj1和obj2是否相等
        """
        if obj1 == obj2:
            return True
        elif obj1 is not None and obj1 == obj2:
            return True
        else:
            return False

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
        elif hasattr(obj, '__bool__'):
            return bool(obj)
        else:
            return obj is not None

    @staticmethod
    def to_string(obj):
        """
        将对象转换为字符串，如果对象为 null ，则返回指定的默认值。
        """
        return str(obj)

    @staticmethod
    def deep_equals(a, b):
        """
        深度比较两个对象是否相等，适用于嵌套对象结构的比较
        """
        if a == b:
            return True
        elif a is None or b is None:
            return False
        else:
            return ObjUtils.deep_equals0(a, b)

    @staticmethod
    def deep_equals0(e1, e2):
        assert e1 is not None
        if isinstance(e1, list) and isinstance(e2, list):
            return ObjUtils.deep_equals(e1, e2)
        elif isinstance(e1, np.ndarray) and isinstance(e2, np.ndarray):
            if e1.dtype == np.byte and e2.dtype == np.byte:
                return np.array_equal(e1, e2)
            elif e1.dtype == np.short and e2.dtype == np.short:
                return np.array_equal(e1, e2)
            elif e1.dtype == np.int_ and e2.dtype == np.int_:
                return np.array_equal(e1, e2)
            elif e1.dtype == np.longlong and e2.dtype == np.longlong:
                return np.array_equal(e1, e2)
            elif e1.dtype == np.char and e2.dtype == np.char:
                return np.array_equal(e1, e2)
            elif e1.dtype == np.float_ and e2.dtype == np.float_:
                return np.array_equal(e1, e2)
            elif e1.dtype == np.double and e2.dtype == np.double:
                return np.array_equal(e1, e2)
            elif e1.dtype == np.bool_ and e2.dtype == np.bool_:
                return np.array_equal(e1, e2)
        else:
            return e1 == e2
