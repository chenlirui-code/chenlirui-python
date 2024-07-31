#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@File    :database_manager_util.py
@Author  :Chen LiRui
@Date    :2024/7/16 下午2:50 
@explain : sql 操作
"""

import mysql.connector


class DatabaseManager:
    @staticmethod
    def connect_to_database(host, user, password, database):
        try:
            conn = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database,
                charset='utf8mb4',
                auth_plugin='mysql_native_password',
                use_pure=False
            )
            print("数据库连接成功")
            return conn
        except mysql.connector.Error as err:
            print(f"数据库连接失败: {err}")
            return None

    @staticmethod
    def batch_write_data(conn, data_list, table_name):  # 修改：将 data_to_insert 改为 data_list，以适应传入的数据是列表
        if conn:
            try:
                cursor = conn.cursor()
                for data in data_list:  # 修改：遍历列表中的每个数据项
                    if 'id' in data:
                        id_value = data['id']
                        # 检查 'id' 是否存在于表中
                        check_query = f"SELECT COUNT(*) FROM {table_name} WHERE id = %s"
                        cursor.execute(check_query, (id_value,))
                        count = cursor.fetchone()[0]

                        if count > 0:
                            # 如果存在，执行更新操作
                            columns = ', '.join([col for col in data.keys() if col != 'id'])
                            update_query = f"UPDATE {table_name} SET {', '.join([f'{col} = %s' for col in columns])} WHERE id = %s"
                            update_values = tuple(data.get(col, None) for col in columns) + (id_value,)
                            cursor.execute(update_query, update_values)
                        else:
                            # 如果不存在，执行插入操作
                            columns = ', '.join(data.keys())
                            placeholders = ', '.join(['%s'] * len(data))
                            insert_query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
                            insert_values = tuple(data[col] for col in data)
                            cursor.execute(insert_query, insert_values)
                    else:
                        # 如果没有提供 'id'，直接执行插入操作
                        columns = ', '.join(data.keys())
                        placeholders = ', '.join(['%s'] * len(data))
                        insert_query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
                        insert_values = tuple(data[col] for col in data)
                        cursor.execute(insert_query, insert_values)

                # 提交事务
                conn.commit()
                print(f"在表 {table_name} 中插入或修改处理成功")
                return 200
            except mysql.connector.Error as err:
                print(f"在表 {table_name} 中插入或修改处理失败: {err}")
                return 404
            finally:
                cursor.close()

    @staticmethod
    def query_data(conn, table_name):
        if conn:
            try:
                cursor = conn.cursor()
                query = f"SELECT * FROM {table_name} WHERE is_delete = 0 AND product_name IS NOT NULL  AND specifications IS NOT NULL AND company IS NOT NULL"
                cursor.execute(query)
                results = cursor.fetchall()
                result_list = []
                for row in results:
                    result_list.append(row)
                return result_list
            except mysql.connector.Error as err:
                print(f"查询失败: {err}")
            finally:
                cursor.close()

    @staticmethod
    def query_data_by_brand(conn, table_name):
        if conn:
            try:
                cursor = conn.cursor()
                query = f"SELECT * FROM {table_name} WHERE brand LIKE '%/%' AND is_delete NOT IN (0, 1)"
                cursor.execute(query)
                results = cursor.fetchall()
                result_list = []
                for row in results:
                    result_list.append(row)
                return result_list
            except mysql.connector.Error as err:
                print(f"查询失败: {err}")
            finally:
                cursor.close()

    import mysql.connector

    @staticmethod
    def query_data_by_id(conn, table_name, id_value):
        if conn:
            try:
                cursor = conn.cursor()
                query = f"SELECT COUNT(*) FROM {table_name} WHERE id = {id_value}"
                cursor.execute(query)
                count = cursor.fetchone()[0]
                if count > 0:
                    return True
                else:
                    return False
            except mysql.connector.Error as err:
                print(f"查询失败: {err}")
            finally:
                cursor.close()

    @staticmethod
    def resp_json_query_data(conn, table_name):
        if conn:
            try:
                cursor = conn.cursor()
                query = f"SELECT * FROM {table_name} WHERE  product_name IS NOT NULL  AND specifications IS NOT NULL AND company IS NOT NULL"
                cursor.execute(query)
                results = cursor.fetchall()
                result_list = []
                for row in results:
                    result_list.append(row)
                return result_list
            except mysql.connector.Error as err:
                print(f"查询失败: {err}")
            finally:
                cursor.close()

    @staticmethod
    def update_is_delete_by_id(conn, table_name, id_value, delete_value):
        if conn:
            try:
                cursor = conn.cursor()
                update_query = f"UPDATE {table_name} SET is_delete = {delete_value} WHERE id = %s"
                cursor.execute(update_query, (id_value,))
                conn.commit()
                if delete_value == 2:
                    print("excel 传入 api 接口")
                elif delete_value == 1:
                    print(f"写入 {table_name} 成功")
                elif delete_value == 3:
                    print(f"插入 {table_name} 数据异常")
                elif delete_value == 4:
                    print("捕获到异常 键不存在于字典中 删除")
                elif delete_value == 5:
                    print("规格不符")
                elif delete_value == 6:
                    print("字典为空")
                elif delete_value == 7:
                    print("未找到有效的 dataSource 数据")
                else:
                    print("未知的 delete_value")
                return 200
            except mysql.connector.Error as err:
                print(f"修改失败: {err}")
                return 404
            finally:
                cursor.close()

    @staticmethod
    def update_resp_json(conn, id, resp_json_table_name, new_resp_json):
        if conn:
            try:
                cursor = conn.cursor()
                update_query = f"UPDATE {resp_json_table_name} SET resp_json = %s WHERE id = %s"
                cursor.execute(update_query, (new_resp_json, id))
                conn.commit()
                return 200
            except mysql.connector.Error as err:
                print(f"修改失败: {err}")
                return 404
            finally:
                cursor.close()


# if __name__ == "__main__":
#
#     # 连接数据库
#     host = 'rm-bp18q46792588r2c2zo.mysql.rds.aliyuncs.com'
#     user = 'bk_tm_clr'
#     password = 'BKclr123&'
#     database = 'bk_tm_db'
#     conn = DatabaseManager.connect_to_database(host, user, password, database)
#
#     # 构造要插入的数据列表
#     data_to_insert = [
#         {'num': '4', 'text': '123'},
#         {'num': '5', 'text': '123'}
#     ]
#     table_name = 'demo'
#
#     DatabaseManager.batch_write_data(
#         conn, data_to_insert, table_name
#     )
#
#     # 关闭数据库连接
#     if conn:
#         conn.close()
#         print("数据库连接已关闭")
