import sys
import json
from util.database_util import DatabaseUtils
from util.mybatisplus_util import MyBatisPlusUtils
from util.logging_util import logger
from work.tianmao.publish.util.product_util import read_xlsx_excel, split_product, split_pve_brand, \
    split_pve_product_name, split_next
from work.tianmao.publish.util.qianniu_util import QianNiu, resp_json_next

sys.path.append('D:\\work\\python')  # 将 util 文件夹的父目录添加到搜索路径中


def read_excelFile_insert_excel_data(excelDAO, file_excel_path, excel_sheet_name, excel_column_name):
    """读取excel文件中某一页的某一列 ，分解，写入 excel_data"""
    excel_text = read_xlsx_excel(file_excel_path, excel_sheet_name, excel_column_name)
    excel_text.pop(0)
    # 使用 sorted 函数进行排序，并通过 reverse=True 参数实现从大到小排序
    sorted_excel_text = sorted(excel_text, key=lambda x: x['求和项:近30日销量'], reverse=True)

    # 从 excel 写入 数据库
    for excel in sorted_excel_text:
        # 提取变量值
        product_id = excel['商品代码']
        product = excel['商品名称']
        sales = excel['求和项:近30日销量']
        price = excel['price']
        # 排除 price 为 0
        if price != 0:
            product = product.strip().replace(' ', '')
            # pve  前面的两个属性  next 后面的两个属性
            pve, next = split_product(product)
            if pve is not None and next is not None:
                #  print(' 分割成功 ') 执行这里的代码，如果 pve 和 next 都不为 None
                brand_list = split_pve_brand(pve)
                product_name = split_pve_product_name(pve)
                brand = '/'.join(brand_list)
                specifications, company = split_next(next)
                if specifications is None or company is None:
                    # print(' 后面的 next 分割失败 ')
                    data_to_insert = {
                        'product_id': product_id,
                        'price': price,
                        'sales': sales,
                        'product': product
                    }
                else:
                    # 构造要插入的数据列表
                    data_to_insert = {
                        'product_id': product_id,
                        'price': price,
                        'sales': sales,
                        'product_name': product_name,
                        'brand': brand,
                        'specifications': specifications,
                        'company': company,
                        'product': product
                    }

            else:
                #  print(' 分割失败 ') 写到数据库中
                data_to_insert = {
                    'product_id': product_id,
                    'price': price,
                    'sales': sales,
                    'product': product
                }
            #  写入数据 to_insert_to_db(conn, excel_table_name, data_to_)
            excelDAO.insert_or_update(data_to_insert)


def find_excel_data_insert_resp_json_data(excelDAO, resp_jsonDAO):
    """读excel_data的内容，发请求，将请求内容存起来resp_json_data"""
    # 读 没有 删除的内容 is_delete = 0 的 表内容
    # 根据 产品名称 product_name 和 brand  搜索 qianniu
    # 根据 specifications 匹配规格
    excel_data_list = excelDAO.find_by_equals(
        {'is_delete': 0},
        {
            'product_name': None,
            'specifications': None
        }
    )
    for data in excel_data_list:
        # print(data)
        id = data[0]
        product = data[1]
        product_id = data[3]
        price = data[4]
        product_name = data[5]
        brand = data[6]
        sales = data[7]
        specifications = data[8]
        company = data[9]
        # print(data)
        # 内容 找网址 匹配 ，写入 excelDAO  resp_jsonDAO
        QianNiu.search_product_by_brand_and_name(
            id,
            product,
            product_id,
            price,
            product_name,
            brand,
            sales,
            specifications,
            company,
            excelDAO,
            resp_jsonDAO
        )


def find_resp_json_data_insert_url_data(resp_jsonDAO, urlDAO):
    """读resp_json_data调用qianniu_util里面的方法，处理，写入url_data"""
    # 读 没有 删除的内容 is_delete = 0 的 表内容
    resp_json_data_list = resp_jsonDAO.find_by_equals(
        {'is_delete': 0},
        None
    )
    # resp_json_data_list = DatabaseManager.query_data(conn, resp_json_table_name)
    for data in resp_json_data_list:
        id = data[0]
        brand = data[2]
        product_name = data[3]
        resp_json = data[4]
        resp_json = json.loads(resp_json)
        product_id = data[5]
        price = data[6]
        sales = data[7]
        specifications = data[8]
        company = data[9]
        # print(data)
        resp_json_next(
            id,
            brand,
            product_name,
            resp_json,
            product_id,
            price,
            sales,
            specifications,
            company,
            resp_jsonDAO,
            urlDAO
        )


if __name__ == '__main__':
    # 连接数据库
    host = '192.168.110.17'
    user = 'temp'
    password = '123456'
    database = 'bk_tm_db'
    # 创建数据库连接
    connection = DatabaseUtils.create_connection(
        host,
        user,
        password,
        database,
    )
    # 创建表格
    excel_table_name = 'excel'
    resp_json_table_name = "resp_json"
    url_table_name = 'url'

    excelDAO = MyBatisPlusUtils(
        connection=connection,
        table_name=excel_table_name
    )

    resp_jsonDAO = MyBatisPlusUtils(
        connection=connection,
        table_name=resp_json_table_name
    )

    urlDAO = MyBatisPlusUtils(
        connection=connection,
        table_name=url_table_name
    )

    # 示例用法
    file_excel_path = r'C:\Users\admin\Desktop\管易按销量排序处方药&OTC.xlsx'
    excel_sheet_name = '处方药'
    excel_column_name = ['商品代码', '商品名称', '求和项:近30日销量', 'price']

    """读取excel文件中某一页的某一列 ，分解，写入 excel_data"""
    # read_excelFile_insert_excel_data(excelDAO, file_excel_path, excel_sheet_name, excel_column_name)
    """读excel_data的内容，发请求，将请求内容存起来resp_json_data"""
    find_excel_data_insert_resp_json_data(excelDAO, resp_jsonDAO)
    """读resp_json_data调用qianniu_util里面的方法，处理，写入url_data"""
    # find_resp_json_data_insert_url_data(resp_jsonDAO,urlDAO)

    # 关闭数据库连接
    DatabaseUtils.close_connection(connection)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
