#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    : test_file.py
@Author  : ChenLiRui
@Time    : 2024/8/5 上午10:04
@explain : 文件说明
"""
from utils.file.FileUtils import FileUtils
from utils.log.my_logger import logger

if __name__ == '__main__':
    drives = FileUtils.get_all_drives()
    for drive in drives:
        files = FileUtils.find_file_path(drive, "AliWorkbench.exe")
        logger.info(files)

    pass
