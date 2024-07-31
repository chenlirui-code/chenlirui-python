#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@File    :img_util.py
@Author  :Chen LiRui
@Date    :2024/7/16 下午4:24 
@explain : img工具类
"""
import os
import time
import requests
import logging
import cv2
import pytesseract
import cv2
import paddlehub as hub

from PIL import Image
from paddleocr import PaddleOCR
from rembg import remove
from manga_ocr import MangaOcr

logging.basicConfig(level=logging.INFO)


class ImgUtils:
    @staticmethod
    def download_image(url, save_path, name):
        """
        给一个网址和一个路径 下载图片到路径中
        @param url: 网址
        @param save_path: 下载图片的地址
        @param char: 后缀名
        """
        try:
            response = requests.get(url)
            if response.status_code == 200:
                today = time.strftime("%Y%m%d")
                new_save_path = os.path.join(save_path, f"{today}_{name}.jpg")
                os.makedirs(os.path.dirname(new_save_path), exist_ok=True)
                with open(new_save_path, 'wb') as f:
                    f.write(response.content)
                logging.info(f"成功下载图片到：{new_save_path}")
                return True
            else:
                logging.error(f"下载图片失败：HTTP 状态码 {response.status_code}")
                return False
        except Exception as e:
            logging.error(f"下载图片时发生异常：{str(e)}")
            return False

    @staticmethod
    def clear_images(folder_path):
        """
        图片删除
        @param folder_path: 有删除图片的文件夹
        """
        try:
            for root, dirs, files in os.walk(folder_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    if file_path.endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp')):
                        os.remove(file_path)
            logging.info(f"图片删除成功，文件夹：{folder_path}")
            return True
        except Exception as e:
            logging.error(f"删除图片时发生异常：{str(e)}")
            return False

    @staticmethod
    def remove_image_background(input_path, output_path):
        """
        从输入路径指定的图片中移除背景，并将处理后的图片保存到输出路径。
        @param input_path: 输入图片文件的路径。
        @param output_path: 处理后图片保存的路径。
        """
        try:
            with open(input_path, 'rb') as i:
                input_data = i.read()
                output_data = remove(input_data)
            with open(output_path, 'wb') as o:
                o.write(output_data)
            logging.info(f"图片处理成功，已保存到 {output_path}")
            return True
        except FileNotFoundError:
            logging.error(f"错误：找不到文件 {input_path}")
            return False
        except Exception as e:
            logging.error(f"处理图片时发生错误：{str(e)}")
            return False

    @staticmethod
    def recognize_captcha(image_path):
        """
        读取图片并使用 PaddleOCR 识别验证码，支持中英文、数字和字母
        @param image_path: 图片地址
        @return: 验证码或提示信息
        """
        ocr = PaddleOCR(use_angle_cls=True, lang='ch')
        result = ocr.ocr(image_path, cls=True)
        if result and result[0]:
            return result[0][0][1][0]
        else:
            return "OCR 识别失败，可能是图片质量问题或其他原因"


if __name__ == '__main__':
    image_path = r"E:\Code\python\base\learn\python\git\Python-master\files\img\img.png"
    # image_path = r"E:\Code\python\base\learn\python\git\Python-master\files\img\img_1.png"
    # image_path = r"E:\Code\python\base\learn\python\git\Python-master\files\img\img_2.png"
    string = ImgUtils.recognize_captcha(image_path)
    print(string)
