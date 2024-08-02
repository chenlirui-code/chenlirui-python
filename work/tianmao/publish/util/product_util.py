#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project :python 
@File    :product_util.py
@IDE     :PyCharm 
@Author  :Chen LiRui
@Date    :2024/7/17 下午3:53 
@explain : 文件说明
"""
import openpyxl


def read_xlsx_excel(url, sheet_name, column_name_arr):
    '''
    读取 xlsx 格式文件中指定多列的数据
    返回值：指定多列的数据列表，列表中的每个元素为一个字典，键为列名，值为该列对应的数据
    '''
    workbook = openpyxl.load_workbook(url)
    sheet = workbook[sheet_name]
    column_data = []
    # 找到指定列的索引
    column_indices = {}
    for col in sheet.iter_cols():
        if col[0].value in column_name_arr:
            column_indices[col[0].value] = col[0].column - 1
    # 检查指定列是否都存在
    for column_name in column_name_arr:
        if column_name not in column_indices:
            raise ValueError(f"未找到名为 {column_name} 的列")
    # 遍历表格中的每一行，获取指定列的数据
    for row in sheet.rows:
        row_data = {}
        for column_name, column_index in column_indices.items():
            row_data[column_name] = row[column_index].value
        column_data.append(row_data)
    return column_data


def remove_substring(string, substring):
    """
    删除 子字符串
    @param string:
    @param substring:
    @return:
    """
    start = string.find(substring)
    if start != -1:
        end = start + len(substring)
        return string[:start] + string[end:]
    else:
        return string


def split_product(product):
    """
    截取为前后两段
    @param product:
    @return:
    """
    allowable_chars = ["—", "-", "一"]
    digit_index = None
    for i, char in enumerate(product):
        if char.isdigit():
            for special_char in allowable_chars:
                if i > 0 and product[i - 1] == special_char:
                    digit_index = i - 1
                    break
            if digit_index is not None:
                break

    if digit_index is None:
        return None, None
    else:
        first_part = product[:digit_index]
        second_part = product[digit_index:]
        # 处理 first_part
        for i in range(len(first_part) - 1, -1, -1):
            if first_part[i] not in allowable_chars:
                break
            first_part = first_part[:i]
        # 处理 second_part
        for i in range(len(second_part)):
            if second_part[i] not in allowable_chars:
                break
            second_part = second_part[i + 1:]
        return first_part, second_part


def split_pve_product_name(product):
    start_bracket_arr = ['（', '(', '[', '【']
    end_bracket_arr = ['）', ')', ']', '】']
    for index, i in enumerate(start_bracket_arr):
        product = process_product_name(
            product,
            start_bracket_arr[index],
            end_bracket_arr[index]
        )
    return product


def process_product_name(product, start_bracket, end_bracket):
    start_index = product.find(start_bracket)
    if start_index == -1:
        return product
    while True:
        end_index = product.find(end_bracket, start_index)
        if end_index == -1:
            return product
        temp = product[start_index:end_index + 1]
        product = product.replace(temp, '')
        start_index = product.find(start_bracket)
        if start_index == -1:
            return product


def split_pve_brand(product):
    start_brand = []
    brand = []
    while True:
        temp = start_brand.copy()
        # 查找 '（' 的位置
        start_index1 = product.find('（')
        # 查找 '(' 的位置
        start_index2 = product.find('(')
        # 查找 '[' 的位置
        start_index3 = product.find('[')
        # 查找 '【' 的位置
        start_index4 = product.find('【')

        start_indices = [start_index1, start_index2, start_index3, start_index4]
        valid_start_indices = [i for i in start_indices if i != -1]

        if valid_start_indices:
            start_index = min(valid_start_indices)
        else:
            # 如果没有找到任何起始括号，返回空字符串
            return brand
        # 去除起始位置后的空格
        stripped_part = product[start_index:].lstrip()
        # 查找对应的 '）' 的位置
        end_index1 = stripped_part.find('）')
        # 查找对应的 ')' 的位置
        end_index2 = stripped_part.find(')')
        # 查找对应的 ']' 的位置
        end_index3 = stripped_part.find(']')
        # 查找对应的 '】' 的位置
        end_index4 = stripped_part.find('】')
        end_indices = [end_index1, end_index2, end_index3, end_index4]
        valid_end_indices = [i for i in end_indices if i != -1]
        if valid_end_indices:
            end_index = min(valid_end_indices)
        else:
            # 如果没有找到任何结束括号，返回空字符串
            return brand
        # 提取括号内的品牌
        str = product[start_index:start_index + end_index + 1]
        # print(str)
        if len(str) != 0:
            start_brand.append(str)
            brand.append(product[start_index + 1:start_index + end_index])
            product = remove_substring(product, str)


def split_next(product):
    allowable_chars = ["—", "-", "一"]
    split_index = None
    for i, char in enumerate(allowable_chars):
        if product.find(char) != -1:
            split_index = product.find(char)
            break
    if split_index is not None:
        first_part = product[:split_index]
        second_part = product[split_index:]
        while len(second_part) > 0 and second_part[0] in allowable_chars:
            second_part = second_part[1:]
        return first_part, second_part
    else:
        return None, None
