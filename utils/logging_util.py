#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    : logging_util.py
@Author  : ChenLiRui
@Time    : 2024/8/1 下午2:11
@explain : 日志记录器
"""

import logging
import os
import sys

# 获取控制台运行文件的目录（即与运行文件同一级的文件夹）
if getattr(sys, 'frozen', False):
    # 如果是可执行文件（.exe）运行时
    current_dir = os.path.dirname(sys.executable)
else:
    # 脚本运行时
    current_dir = os.path.dirname(os.path.realpath(sys.argv[0]))

# 构建日志文件路径，使用当前脚本的名称加上 debug_log.log
log_file_name = os.path.splitext(os.path.basename(sys.argv[0]))[0] + '_debug_log.log'
file_path = os.path.join(current_dir, log_file_name)

# 创建一个日志记录器
logger = logging.getLogger('my_logger')

# 设置日志级别为 DEBUG
logger.setLevel(logging.DEBUG)

# 创建一个文件处理器，指定保存的文件夹和文件名（仅处理 ERROR 级别及以上的日志）
file_handler = logging.FileHandler(file_path)
file_handler.setLevel(logging.DEBUG)  # 确保此处理器仅处理 DEBUG 级别的日志

# 设置文件处理器的日志格式
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# 将文件处理器添加到日志记录器中
logger.addHandler(file_handler)