#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@File    : excel_util.py
@Author  : Chen LiRui
@Date    : 2024/7/15 下午5:12
@explain : Excel 工具类
"""

import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)  # 配置日志基本设置


class ExcelUtils:
    @staticmethod
    def append_data_to_excel(excel_file, sheet_name, new_data):
        """
        将数据追加到指定 Excel 文件的指定工作表中
        :param excel_file: Excel 文件路径
        :param sheet_name: 工作表名称
        :param new_data: 要追加的新数据，DataFrame 格式
        """
        try:
            # 读取现有的 Excel 文件到 Pandas DataFrame
            try:
                existing_data = pd.read_excel(excel_file, sheet_name=sheet_name, engine='openpyxl')
            except FileNotFoundError:
                existing_data = pd.DataFrame()  # 如果文件不存在，创建一个空的DataFrame

            # 将新数据追加到现有数据的上方
            combined_data = pd.concat([new_data, existing_data], ignore_index=True)

            # 将数据追加到 Excel 文件中的指定工作表，设置 if_sheet_exists 参数为 'eplace' 或 'append'
            with pd.ExcelWriter(excel_file, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
                combined_data.to_excel(writer, sheet_name=sheet_name, index=False)

            logging.info(f"数据已成功追加到 Excel 文件中的 '{sheet_name}' 工作表。")
            return True
        except Exception as e:
            logging.error(f"追加数据到 Excel 文件出现错误：{e}")
            return False

    @staticmethod
    def append_data(excel_file, sheet_name, id, approval_number, expiration_date):
        """
        将数据追加到指定 Excel 文件的指定工作表中
        :param excel_file: Excel 文件路径
        :param sheet_name: 工作表名称
        :param id: ID 列数据
        :param approval_number: 药品批准文号列数据
        :param expiration_date: 药品批准文号有效期列数据
        :return: 成功返回 True，失败返回 False
        """
        try:
            # 创建要追加的新数据 DataFrame
            new_data = pd.DataFrame({
                'ID': [id],
                '药品批准文号': [approval_number],
                '药品批准文号有效期': [expiration_date]
            })

            # 调用静态方法追加数据到 Excel 文件
            return ExcelUtils.append_data_to_excel(excel_file, sheet_name, new_data)
        except Exception as e:
            logging.error(f"追加数据到 Excel 文件出现错误：{e}")
            return False
