#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    : file_util.py
@Author  : ChenLiRui
@Time    : 2024/7/30 上午11:20
@explain : 文件工具类
"""
import os
import logging

logging.basicConfig(level=logging.INFO)


class FileUtils:
    @staticmethod
    def get_all_filename(file_path):
        """ 给一个地址 返回 当前目录的所有文件夹 和文件 """
        folders = []
        files = []
        items = os.listdir(file_path)
        for item in items:
            item_path = os.path.join(file_path, item)
            if os.path.isdir(item_path):
                folders.append(item)
            else:
                files.append(item)
        logging.info(f"在路径 {file_path} 中，获取到的文件夹: {folders}")
        logging.info(f"在路径 {file_path} 中，获取到的文件: {files}")
        return folders, files
