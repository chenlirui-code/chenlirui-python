#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@File    :text_util.py
@Author  :Chen LiRui
@Date    :2024/7/24 下午2:58 
@explain : 文本工具类
"""
import re
import urllib.parse

from utils.logging_util import logger


class TextUtils:
    @staticmethod
    def decode_unicode_to_text(data):
        """
        unicode 转 文字
        @param data: 要转换的 unicode
        @return: 转换后的文字
        """
        if isinstance(data, dict):
            new_data = {}
            for key, value in data.items():
                new_data[key] = TextUtils.decode_unicode_to_text(value)
            # logger.debug("成功将字典中的 Unicode 转换为文字")
            return new_data
        elif isinstance(data, list):
            new_data = []
            for i, item in enumerate(data):
                new_data.append(TextUtils.decode_unicode_to_text(item))
            # logger.debug("成功将列表中的 Unicode 转换为文字")
            return new_data
        elif isinstance(data, str):
            data = re.sub(r'\\u([0-9a-fA-F]{4})', lambda match: chr(int(match.group(1), 16)), data)
            # logger.debug("成功将字符串中的 Unicode 转换为文字")
        return data

    @staticmethod
    def encode_url_to_text(input_string):
        """
        文字 转 url
        @param input_string: 要转换的 url编码
        @return: 转换后的文字
        """
        return urllib.parse.quote(input_string)
