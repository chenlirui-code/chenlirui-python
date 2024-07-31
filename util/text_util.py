#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@File    :text_util.py
@Author  :Chen LiRui
@Date    :2024/7/24 下午2:58 
@explain : 文本工具类
"""
import re
import logging

logging.basicConfig(level=logging.INFO)


class TextUtils:
    @staticmethod
    def convert_unicode_to_text(data):
        """
        unicode 转文字
        @param data: 要转换的 unicode
        @return: 转换后的文字
        """
        if isinstance(data, dict):
            new_data = {}
            for key, value in data.items():
                new_data[key] = TextUtils.convert_unicode_to_text(value)
            logging.info("成功将字典中的 Unicode 转换为文字")
            return new_data
        elif isinstance(data, list):
            new_data = []
            for i, item in enumerate(data):
                new_data.append(TextUtils.convert_unicode_to_text(item))
            logging.info("成功将列表中的 Unicode 转换为文字")
            return new_data
        elif isinstance(data, str):
            data = re.sub(r'\\u([0-9a-fA-F]{4})', lambda match: chr(int(match.group(1), 16)), data)
            logging.info("成功将字符串中的 Unicode 转换为文字")
        return data
