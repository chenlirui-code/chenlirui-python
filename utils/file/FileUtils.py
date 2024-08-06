#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    : file_util.py
@Author  : ChenLiRui
@Time    : 2024/7/30 上午11:20
@explain : 文件工具类
"""
import os


class FileUtils:
    @staticmethod
    def get_all_drives():
        """
        获取系统上所有的盘符
        返回:
        drives (list): 所有盘符的列表
        """
        drives = []
        for drive in range(ord('A'), ord('Z') + 1):
            drive_name = f"{chr(drive)}:\\"
            if os.path.exists(drive_name):
                drives.append(drive_name)
        return drives

    @staticmethod
    def list_files_in_drive(drive):
        """
        列出指定盘符下的所有文件和目录
        参数:
        drive (str): 盘符，例如 'C:\\'
        返回:
        files (list): 盘符下所有文件和目录的列表
        """
        files = []
        try:
            for root, _, filenames in os.walk(drive):
                for filename in filenames:
                    files.append(os.path.join(root, filename))
        except Exception as e:
            print(f"Error listing files in {drive}: {e}")
        return files

    @staticmethod
    def find_file_path(drive, filename):
        """Find the full path of a file given the drive and filename."""
        if not os.path.exists(drive):
            raise ValueError(f"Drive '{drive}' does not exist.")

        for root, _, files in os.walk(drive):
            if filename in files:
                return os.path.join(root, filename)

        return None  # Return None if file is not found

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
        return folders, files
