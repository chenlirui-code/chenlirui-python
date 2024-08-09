#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    : SpiderUtils.py
@Author  : ChenLiRui
@Time    : 2024/8/7 上午10:00
@explain : 爬虫的工具类
"""


class SpiderUtils:
    @staticmethod
    def header_common(headers_list):
        """
        :param headers_list: headers集合
        :return: 共同的common_headers, 更新后的headers_list
        """
        if not headers_list:
            return {}

        # 初始化为第一个字典的副本
        common_headers = headers_list[0].copy()

        # 遍历剩余的字典，找出共同的键值对
        for headers in headers_list[1:]:
            # 使用集合保存需要删除的键
            keys_to_remove = set()
            for key in list(common_headers.keys()):
                if key in headers and common_headers[key] == headers[key]:
                    continue
                else:
                    keys_to_remove.add(key)

            # 从共同头部中删除不一致的键
            for key in keys_to_remove:
                del common_headers[key]

        # 更新原始 headers_list 中每个字典，仅保留不共同的键值对
        for i, headers in enumerate(headers_list):
            headers_list[i] = {k: v for k, v in headers.items() if
                               k not in common_headers or headers[k] != common_headers[k]}

        return common_headers, headers_list
