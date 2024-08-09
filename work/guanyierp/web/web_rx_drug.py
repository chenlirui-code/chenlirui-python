#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    : web_rx_drug.py
@Author  : ChenLiRui
@Time    : 2024/8/8 下午2:40
@explain : 处方药
"""
import requests
from utils.log.my_logger import logger


def request_post(url, headers, params, data):
    # 创建一个会话对象
    request = requests.session()

    # 发送 POST 请求
    response = request.post(
        url=url,
        headers=headers,
        params=params,
        data=data
    )
    if response.status_code == 200:
        return response
    return None
