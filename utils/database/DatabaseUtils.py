#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    : DatabaseUtils.py
@Author  : ChenLiRui
@Time    : 2024/8/1 上午10:24
@explain : 数据库工具类
"""
import mysql.connector
import pymysql
import datetime
from utils.log.my_logger import logger
from typing import Any


class DatabaseUtils:
    @staticmethod
    def create_connection(host, user, password, database):
        """
        连接到数据库
        Args:
            host (str): 数据库主机地址
            user (str): 数据库用户名
            password (str): 数据库密码
            database (str): 数据库名称
        Returns:
            mysql.connector.connection.MySQLConnection: 数据库连接对象，如果连接失败返回 None
        """
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
            logger.info("数据库连接成功")
            return conn
        except mysql.connector.Error as err:
            logger.error(f"数据库连接失败: {err}")
            return None

    @staticmethod
    def close_connection(conn):
        """
        关闭数据库连接
        Args:
            conn (mysql.connector.connection.MySQLConnection): 要关闭的数据库连接对象
        """
        if conn:
            try:
                conn.close()
                logger.info("数据库连接已关闭")
            except mysql.connector.Error as err:
                logger.error(f"关闭数据库连接时出错: {err}")

    @staticmethod
    def create_table_from_dict(conn, table_name, data_dict):
        """
        根据给定的字典创建数据库表。
        Args:
            conn (pymysql.connections.Connection): 数据库连接对象
            table_name (str): 要创建的表名
            data_dict (dict): 字典，其中键是字段名，值是字段值
        """
        cursor = conn.cursor()
        # 构建字段和类型
        columns = []
        for key, value in data_dict.items():
            sql_type = get_sql_type(value)
            columns.append(f"`{key}` {sql_type}")
        columns_str = ', '.join(columns)
        create_table_sql = f"CREATE TABLE IF NOT EXISTS `{table_name}` ({columns_str})"
        try:
            cursor.execute(create_table_sql)
            conn.commit()
            print(f"成功创建表 {table_name}")
        except Exception as e:
            print(f"创建表时出错: {e}")
        finally:
            cursor.close()


def get_sql_type(value: Any) -> str:
    """
    根据 Python 值类型获取 SQL 数据类型。
    Args:
        value (Any): Python 数据类型的值
    Returns:
        str: 对应的 SQL 数据类型
    """
    if value is None:
        return 'VARCHAR(100)'  # 默认类型，较小的 VARCHAR
    if isinstance(value, str):
        # 根据字符串长度选择合适的文本类型
        if len(value) > 65535:
            return 'LONGTEXT'
        elif len(value) > 16383:
            return 'MEDIUMTEXT'
        elif len(value) > 255:
            return 'TEXT'
        else:
            return 'VARCHAR(255)'
    elif isinstance(value, int):
        # 根据值的范围选择合适的整数类型
        if -128 <= value <= 127:
            return 'TINYINT'
        elif -32768 <= value <= 32767:
            return 'SMALLINT'
        elif -2147483648 <= value <= 2147483647:
            return 'INT'
        else:
            return 'BIGINT'
    elif isinstance(value, float):
        # 使用 DECIMAL 以避免浮点精度问题
        return 'DECIMAL(15, 6)'  # 更精确的 DECIMAL 类型
    elif isinstance(value, bool):
        return 'BOOLEAN'
    elif isinstance(value, (list, dict)):
        return 'LONGTEXT'  # JSON 类型可以用 LONGTEXT 存储
    elif isinstance(value, (datetime.date, datetime.datetime)):
        # 日期或日期时间
        if isinstance(value, datetime.datetime):
            return 'DATETIME'
        else:
            return 'DATE'
    else:
        # 默认情况
        return 'VARCHAR(255)'  # 使用更合理的 VARCHAR 长度
