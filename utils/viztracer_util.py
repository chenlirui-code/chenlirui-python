#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@File    :viztracer_util.py
@Author  :ChenLiRui
@Date    :2024/7/15 上午10:22 
@explain : VizTracer性能分析
"""
import logging

from pyinstrument import Profiler

logging.basicConfig(level=logging.INFO)


class VizTracerUtils:
    @staticmethod
    def analyze_function(func):
        """
        对给定的函数进行性能分析
        参数：
        func (function)：要分析的函数
        """
        profiler = Profiler()
        profiler.start()
        func()
        profiler.stop()
        logging.info(profiler.output_text())
