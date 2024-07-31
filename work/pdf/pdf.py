#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@File    :pdf.py
@Author  :Chen LiRui
@Date    :2024/7/15 下午5:12 
@explain : 文件说明
"""
import os
import logging

from util.img_clear import clear_images
from util.excel_util import ExcelUtils
from work.pdf.util import pdf_util

logging.getLogger('ppocr').setLevel(logging.WARNING)

if __name__ == '__main__':
    # UNC路径，注意双斜杠或原始字符串
    shared_folder = r'E:\Code\python\base\work\pdf\files\pdf'
    # 图片地址
    cache_path = r"E:\Code\python\base\work\pdf\files\img"
    # 指定文件保存路径
    excel_file = r"E:\Code\python\base\work\pdf\files\e.xlsx"
    sheet_name = 'Sheet1'

    # 获取共享文件夹下的所有文件路径
    file_paths = []
    for root, dirs, files in os.walk(shared_folder):
        for filename in files:
            file_path = os.path.join(root, filename)
            file_paths.append(file_path)

    # 打印所有文件路径
    for pdf_path in file_paths:
        if pdf_path.lower().endswith(".pdf"):
            # 获取文件名（带扩展名）
            file_name_with_extension = os.path.basename(pdf_path)
            # 分离文件名和扩展名
            file_name, file_extension = os.path.splitext(file_name_with_extension)

            result = pdf_util.i_main(pdf_file_path=pdf_path, save_path=cache_path)

            success = False

            if result is None:
                success = ExcelUtils.append_data(excel_file, sheet_name, file_name, "无法识别", "无法识别")
            else:
                success = ExcelUtils.append_data(excel_file, sheet_name, file_name, result[0], result[1])



            if success:
                print(f"数据追加成功！")

                # 根据 pdf_path 删除 PDF 文件
                try:
                    os.remove(pdf_path)
                    print(f"成功删除文件：{pdf_path}")
                except Exception as e:
                    print(f"删除文件时出现错误：{e}")

            else:
                print("数据追加失败。")

            print(
                "================================================================================================================================")

        # 清空图片
        clear_images(cache_path)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
