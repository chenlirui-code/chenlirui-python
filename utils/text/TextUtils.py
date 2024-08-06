#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@File    :TextUtils.py
@Author  :Chen LiRui
@Date    :2024/7/24 下午2:58 
@explain : 文本工具类
"""
import urllib.parse
import chardet

from utils.log.my_logger import logger

class TextUtils:

    @staticmethod
    def normalize_encoding(encoding_type):
        """
        标准化编码类型，将其转换为小写形式
        """
        return encoding_type.lower()

    @staticmethod
    def decode(data, encoding_type):
        """
        将输入的数据按照指定的编码进行解码
        参数:
        data (任何类型): 要解码的数据，可以是字符串、字节数据、列表、字典等
        encoding_type (str): 目标编码类型，如 'ASCII', 'ANSI', 'GBK', 'GB2312', 'UTF-8', 'GB18030', 'url'
        返回:
        解码后的结果，保留原数据类型
        """
        encoding_type = TextUtils.normalize_encoding(encoding_type)  # 标准化编码类型

        if isinstance(data, str):
            if encoding_type == 'url':
                return urllib.parse.unquote(data)  # 对 URL 编码的字符串进行解码
            elif encoding_type in ['utf-8', 'unicode']:
                return data
            else:
                try:
                    # 使用 UTF-8 编码进行中间转换
                    return data.encode('utf-8').decode(encoding_type)
                except (LookupError, UnicodeDecodeError) as e:
                    logger.error(f"无法使用 {encoding_type} 解码: {e}")
                    return data  # 解码失败时返回原始字符串
        elif isinstance(data, bytes):
            detected_encoding = chardet.detect(data)['encoding']
            if detected_encoding:
                try:
                    decoded_data = data.decode(detected_encoding)
                    # 使用 UTF-8 编码进行中间转换
                    return decoded_data.encode('utf-8').decode(encoding_type)
                except (UnicodeDecodeError, UnicodeEncodeError) as e:
                    logger.error(f"无法将数据从 {detected_encoding} 解码为 {encoding_type}: {e}")
                    return data
            else:
                logger.error("无法检测字节数据的编码")
                return data
        elif isinstance(data, dict):
            return {TextUtils.decode(key, encoding_type): TextUtils.decode(value, encoding_type) for key, value in data.items()}
        elif isinstance(data, list):
            return [TextUtils.decode(item, encoding_type) for item in data]
        elif isinstance(data, tuple):
            return tuple(TextUtils.decode(item, encoding_type) for item in data)
        elif isinstance(data, set):
            return {TextUtils.decode(item, encoding_type) for item in data}
        else:
            logger.error("不支持的对象类型进行解码操作")
            return data

    @staticmethod
    def encode(data, encoding_type):
        """
        对输入的数据按照指定编码进行编码
        参数:
        data (任何类型): 要编码的数据，可以是字符串、字节数据、列表、字典等
        encoding_type (str): 目标编码类型，如 'ASCII', 'ANSI', 'GBK', 'GB2312', 'UTF-8', 'GB18030', 'url'
        返回:
        编码后的结果，保留原数据类型
        """
        encoding_type = TextUtils.normalize_encoding(encoding_type)  # 标准化编码类型

        if isinstance(data, str):
            if encoding_type == 'url':
                return urllib.parse.quote(data)  # 对字符串进行 URL 编码
            else:
                try:
                    return data.encode(encoding_type).decode(encoding_type)
                except (LookupError, UnicodeEncodeError) as e:
                    logger.error(f"无法使用 {encoding_type} 编码: {e}")
                    return data  # 编码失败时返回原始字符串
        elif isinstance(data, bytes):
            detected_encoding = chardet.detect(data)['encoding']
            if detected_encoding:
                if detected_encoding.lower() != encoding_type:
                    try:
                        return data.decode(detected_encoding).encode(encoding_type).decode(encoding_type)
                    except (UnicodeDecodeError, UnicodeEncodeError) as e:
                        logger.error(f"无法将数据从 {detected_encoding} 编码为 {encoding_type}: {e}")
                        raise ValueError(f"无法将数据从 {detected_encoding} 编码为 {encoding_type}: {e}")
                else:
                    return data.decode(encoding_type)
            else:
                logger.error("无法检测字节数据的编码")
                return data
        elif isinstance(data, dict):
            return {TextUtils.encode(key, encoding_type): TextUtils.encode(value, encoding_type) for key, value in data.items()}
        elif isinstance(data, list):
            return [TextUtils.encode(item, encoding_type) for item in data]
        elif isinstance(data, tuple):
            return tuple(TextUtils.encode(item, encoding_type) for item in data)
        elif isinstance(data, set):
            return {TextUtils.encode(item, encoding_type) for item in data}
        else:
            logger.error("不支持的对象类型进行编码操作")
            return data
