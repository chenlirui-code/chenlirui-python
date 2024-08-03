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
    def decode(obj, target_encoding):
        """
        将输入的数据按照指定的编码进行解码
        参数:
        obj (list, dict, tuple, set, str 或 bytes): 要解码的数据
        target_encoding (str): 目标编码，如 'ASCII', 'ANSI', 'GBK', 'GB2312', 'UTF-8', 'GB18030', 'UNICODE', 'url'
        返回:
        解码后的结果
        """
        if isinstance(obj, list):
            return [TextUtils.decode(item, target_encoding) for item in obj]
        elif isinstance(obj, dict):
            return {key: TextUtils.decode(value, target_encoding) for key, value in obj.items()}
        elif isinstance(obj, tuple):
            return tuple(TextUtils.decode(item, target_encoding) for item in obj)
        elif isinstance(obj, set):
            return {TextUtils.decode(item, target_encoding) for item in obj}
        elif isinstance(obj, str):
            if target_encoding == 'url':
                obj = urllib.parse.unquote(obj)
            elif target_encoding != 'UNICODE':  # 假设 UNICODE 不是一种直接的编码操作方式
                obj = obj.encode(target_encoding)
        elif isinstance(obj, bytes):
            if target_encoding == 'UTF-8':
                try:
                    return obj.decode('utf-8')
                except UnicodeDecodeError:
                    logger.error("无法使用 UTF-8 解码")
            elif target_encoding == 'GBK':
                try:
                    return obj.decode('gbk')
                except UnicodeDecodeError:
                    logger.error("无法使用 GBK 解码")
            elif target_encoding == 'GB2312':
                try:
                    return obj.decode('gb2312')
                except UnicodeDecodeError:
                    logger.error("无法使用 GB2312 解码")
            elif target_encoding == 'GB18030':
                try:
                    return obj.decode('gb18030')
                except UnicodeDecodeError:
                    logger.error("无法使用 GB18030 解码")
            elif target_encoding == 'ASCII':
                try:
                    return obj.decode('ascii')
                except UnicodeDecodeError:
                    logger.error("无法使用 ASCII 解码")
            elif target_encoding == 'ANSI':  # ANSI 不是一个明确的编码，通常是 Windows 系统下对本地代码页的称呼
                try:
                    return obj.decode('cp1252')  # 常见的 Windows ANSI 编码
                except UnicodeDecodeError:
                    logger.error("无法使用 ANSI 解码")
            else:
                logger.error("不支持的编码类型")

        return obj

    @staticmethod
    def encode(obj, target_encoding):
        """
        对输入对象按照指定编码进行编码
        参数:
        obj (list, dict, tuple, set, str 或 bytes): 要编码的对象
        target_encoding (str): 目标编码类型，如 'ASCII', 'ANSI', 'GBK', 'GB2312', 'UTF-8', 'GB18030', 'UNICODE', 'url'
        返回:
        编码后的结果
        """
        if isinstance(obj, list):
            return [TextUtils.encode(item, target_encoding) for item in obj]
        elif isinstance(obj, dict):
            return {key: TextUtils.encode(value, target_encoding) for key, value in obj.items()}
        elif isinstance(obj, tuple):
            return tuple(TextUtils.encode(item, target_encoding) for item in obj)
        elif isinstance(obj, set):
            return {TextUtils.encode(item, target_encoding) for item in obj}
        elif isinstance(obj, str):
            if target_encoding == 'url':
                return urllib.parse.quote(obj)
            else:
                try:
                    return obj.encode(target_encoding)
                except LookupError:
                    raise ValueError(f"不支持的编码: {target_encoding}")
        elif isinstance(obj, bytes):
            detected_encoding = chardet.detect(obj)['encoding']
            if detected_encoding != target_encoding:
                try:
                    return obj.decode(detected_encoding).encode(target_encoding)
                except UnicodeDecodeError:
                    raise ValueError(f"无法将数据从 {detected_encoding} 解码为 {target_encoding}")
            else:
                return obj
        else:
            raise TypeError("不支持的对象类型进行编码操作")
