import json

from work.tianmao.publish.util.database_manager_util import DatabaseManager
from work.tianmao.publish.util.product_util import read_xlsx_excel, split_product, split_pve_brand, \
    split_pve_product_name, split_next
from work.tianmao.publish.util.qianniu_util import QianNiu, resp_json_next


def read_excelFile_write_excel_data(conn, table_name, file_excel_path, excel_sheet_name, excel_column_name):
    """读取excel文件中某一页的某一列 ，分解，写入 excel_data"""
    excel_text = read_xlsx_excel(file_excel_path, excel_sheet_name, excel_column_name)
    excel_text.pop(0)

    # 从 excel 写入 数据库
    for product in excel_text:
        product = product.strip().replace(' ', '')
        # print(product)
        # pve  前面的两个属性  next 后面的两个属性
        pve, next = split_product(product)
        if pve is not None and next is not None:
            # 执行这里的代码，如果 pve 和 next 都不为 None
            # print(' 分割成功 ')
            # print(pve)
            brand_list = split_pve_brand(pve)
            product_name = split_pve_product_name(pve)
            brand = '/'.join(brand_list)
            # print(product_name)
            # print(brand)
            # print(next)
            specifications, company = split_next(next)
            # print(specifications)
            # print(company)
            if specifications is None or company is None:
                # print(' 后面的 next 分割失败 ')
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


def read_excel_data_to_qianniu_util_write_resp_json_data(conn, excel_table_name):
    """读excel_data的内容，发请求，将请求内容存起来resp_json_data"""
    # 读 没有 删除的内容 is_delete = 0 的 表内容
    excel_data_list = DatabaseManager.query_data(conn, excel_table_name)
    for data in excel_data_list:
        id = data[0]
        product_name = data[2]
        brand = data[3]
        specifications = data[4]
        company = data[5]
        # print(id)
        # print(product_name)
        # print(brand)
        # print(specifications)
        # print(company)
        # 传入 api接口 过修改 删除为 2
        code = DatabaseManager.update_is_delete_by_id(
            conn,
            excel_table_name,
            id,
            1
        )
        # 内容 找网址 匹配 ，写入
        QianNiu.search_product_by_brand_and_name(
            conn,
            id,
            brand,
            product_name,
            specifications,
            company,
            resp_json_table_name
        )


def read_resp_json_data_to_qianniu_util_write_url_data(conn, resp_json_table_name):
    """读resp_json_data调用qianniu_util里面的方法，处理，写入url_data"""
    # 读 没有 删除的内容 is_delete = 0 的 表内容
    resp_json_data_list = DatabaseManager.query_data(conn, resp_json_table_name)
    for data in resp_json_data_list:
        id = data[0]
        brand = data[1]
        product_name = data[2]
        resp_json = data[3]
        resp_json = json.loads(resp_json)
        is_delete = data[4]
        specifications = data[5]
        company = data[6]
        # print(id)
        # print(brand)
        # print(product_name)
        # print(resp_json)
        # print(is_delete)
        # print(specifications)
        # print(company)
        resp_json_next(
            resp_json,
            conn,
            id,
            brand,
            product_name,
            specifications,
            company,
            resp_json_table_name,
            url_table_name
        )


def solve_much_brand_search_product_by_brand_and_name(conn, resp_json_table_name, url_table_name):
    """读resp_json_data,多品牌处理,写入resp_json_data"""
    # 读 brand 有 / 的 表内容
    resp_json_data_list = DatabaseManager.query_data_by_brand(conn, resp_json_table_name)
    for data in resp_json_data_list:
        id = data[0]
        brand = data[1]
        product_name = data[2]
        specifications = data[5]
        company = data[6]

        brand_list = brand.split('/')
        for brand in brand_list:
            print(id)
            print(brand)
            print(product_name)
            print(specifications)
            print(company)

            # 查询 url_data 里面
            flag = DatabaseManager.query_data_by_id(conn, url_table_name, id)
            if flag:
                # 有url_data数据
                break

            # 内容 找网址 匹配 ，写入
            QianNiu.search_product_by_brand_and_name(
                conn,
                id,
                brand,
                product_name,
                specifications,
                company,
                resp_json_table_name
            )


if __name__ == '__main__':
    # 连接数据库
    host = 'rm-bp18q46792588r2c2zo.mysql.rds.aliyuncs.com'
    user = 'bk_tm_clr'
    password = 'BKclr123&'
    database = 'bk_tm_db'
    conn = DatabaseManager.connect_to_database(host, user, password, database)

    excel_table_name = 'excel_data'
    url_table_name = 'url_data'
    resp_json_table_name = "resp_json_data"

    # 示例用法
    file_excel_path = r'/work/tianmao\files\商品库存导出(4).xlsx'
    excel_sheet_name = '处方药'
    excel_column_name = '商品名称'

    """读取excel文件中某一页的某一列 ，分解，写入 excel_data"""
    read_excelFile_write_excel_data(conn, excel_table_name, file_excel_path, excel_sheet_name, excel_column_name)
    print()
    """读excel_data的内容，发请求，将请求内容存起来resp_json_data"""
    # read_excel_data_to_qianniu_util_write_resp_json_data(conn, excel_table_name)
    print()
    """读resp_json_data调用qianniu_util里面的方法，处理，写入url_data"""
    # read_resp_json_data_to_qianniu_util_write_url_data(conn, resp_json_table_name)
    print()
    """解决多品牌的请求的问题, 读resp_json_data,多品牌处理,写入resp_json_data"""
    # solve_much_brand_search_product_by_brand_and_name(conn, resp_json_table_name, url_table_name)

    # 关闭数据库连接
    if conn:
        conn.close()
        print("数据库连接已关闭")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
