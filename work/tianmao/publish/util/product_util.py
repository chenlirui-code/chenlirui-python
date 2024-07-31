#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@File    : product_util.py
@Author  : Chen LiRui
@Date    : 2024/7/17 下午3:53
@explain : 产品的处理工具类
"""
import openpyxl

from work.tianmao.publish.util.database_manager_util import DatabaseManager


def read_xlsx_excel(url, sheet_name, column_name):
    '''
    读取xlsx格式文件中指定列的数据
    返回值：指定列的数据列表
    '''
    workbook = openpyxl.load_workbook(url)
    sheet = workbook[sheet_name]
    column_data = []
    # 找到指定列的索引
    column_index = None
    for col in sheet.iter_cols():
        if col[0].value == column_name:
            column_index = col[0].column - 1
            break
    if column_index is None:
        raise ValueError(f"未找到名为 {column_name} 的列")
    # 遍历表格中的每一行，获取指定列的数据
    for row in sheet.rows:
        column_data.append(row[column_index].value)
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


if __name__ == '__main__':

    # 连接数据库
    host = 'rm-bp18q46792588r2c2zo.mysql.rds.aliyuncs.com'
    user = 'bk_tm_clr'
    password = 'BKclr123&'
    database = 'bk_tm_db'
    conn = DatabaseManager.connect_to_database(host, user, password, database)

    table_name = 'excel_data'

    # 示例用法
    file_path = r'C:\Users\admin\Desktop\商品库存导出(4).xlsx'
    sheet_name = 'OTC'
    column_name = '商品名称'

    excel_text = read_xlsx_excel(file_path, sheet_name, column_name)
    excel_text.pop(0)

    # 构造要插入的数据列表
    data_to_insert = []

    for product in excel_text:
        product = product.strip().replace(' ', '')
        print(product)
        # pve  前面的两个属性  next 后面的两个属性
        pve, next = split_product(product)
        if pve is not None and next is not None:
            # 执行这里的代码，如果 pve 和 next 都不为 None
            # print(' 分割成功 ')
            print(pve)
            brand_list = split_pve_brand(pve)
            product_name = split_pve_product_name(pve)
            brand = '/'.join(brand_list)
            # print(product_name)
            # print(brand)
            print(next)
            specifications, company = split_next(next)
            # print(specifications)
            # print(company)
            if specifications is None or company is None:
                print(' 后面的 next 分割失败 ')
                data_to_insert = [
                    {
                        'product': product
                    },
                ]
            else:
                # 构造要插入的数据列表
                data_to_insert = [
                    {
                        'product_name': product_name,
                        'brand': brand,
                        'specifications': specifications,
                        'company': company,
                        'product': product
                    },
                ]
        else:
            # print(' 分割失败 ')
            # 写到数据库中
            # print(product)
            data_to_insert = [
                {
                    'product': product
                },
            ]

        DatabaseManager.batch_write_data(
            conn, data_to_insert, table_name
        )

    # 关闭数据库连接
    if conn:
        conn.close()
        print("数据库连接已关闭")

    pass

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
