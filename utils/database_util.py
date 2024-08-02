#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    : database_util.py
@Author  : ChenLiRui
@Time    : 2024/8/1 上午10:24
@explain : 数据库工具类
"""
import mysql.connector
import logging

logging.basicConfig(level=logging.DEBUG)
logging.getLogger().setLevel(logging.DEBUG)


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
            logging.debug("数据库连接成功")
            return conn
        except mysql.connector.Error as err:
            print(f"数据库连接失败: {err}")
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
                logging.debug("数据库连接已关闭")
            except mysql.connector.Error as err:
                logging.error(f"关闭数据库连接时出错: {err}")
