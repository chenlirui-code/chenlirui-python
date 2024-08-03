#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    : ai_util.py
@Author  : ChenLiRui
@Time    : 2024/7/30 上午11:44
@explain : ai工具类
"""
import requests
from utils.log.my_logger import logger


class AiUtils:
    @staticmethod
    def get_ai_response(input_text):
        """
        输入文本并返回 AI 机器的回答
        @param input_text:
        @return: AI 机器的回答
        """
        # API endpoint
        url = "https://api.xty.app/v1/chat/completions"

        # 请求头部信息，包括Content-Type和Authorization
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer sk-vqbLassWB9AYYGSD417c7c72565944Cb8fC8EbD9B75a3740"  # 替换为您的实际Authorization token
        }

        # 请求数据，包括模型、用户消息、流式处理、温度参数
        data = {
            "model": "gpt-3.5-turbo",
            "messages": [{"role": "user", "content": input_text}],
            "stream": False,
            "temperature": 0.7
        }

        # 发送POST请求
        response = requests.post(url, json=data, headers=headers)

        # 处理响应
        if response.status_code == 200:
            result = response.json()
            choices = result.get('choices', [])
            if choices:
                msg = choices[0]['message']['content']
            else:
                msg = '出错'
            logger.info(msg)
            return msg
        else:
            logger.error("请求出错: 状态码 %d，错误信息: %s", response.status_code, response.text)
            return "请求出错"
