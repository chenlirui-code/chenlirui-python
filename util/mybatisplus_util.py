#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    : mybatisplus_util.py
@Author  : ChenLiRui
@Time    : 2024/8/1 上午8:25
@explain : MyBatisPlus工具类
"""
import pymysql
import logging

logging.basicConfig(level=logging.INFO)
from typing import List


class MyBatisPlusUtils:

    def __init__(self, database_url: str, database_user: str, database_password: str, database_name: str,
                 table_name: str):
        self.connection = pymysql.connect(
            host=database_url,
            user=database_user,
            password=database_password,
            database=database_name
        )
        self.table_name = table_name

    def find_by_id(self, id: int):
        """
        根据主键 ID 查找数据
        Args:
            id (int): 主键值
        Returns:
            dict: 查找结果
        """
        cursor = self.connection.cursor()
        query = f"SELECT * FROM {self.table_name} WHERE id = %s"
        cursor.execute(query, (id,))
        result = cursor.fetchone()
        if result:
            result_dict = {column[0]: value for column, value in zip(cursor.description, result)}
        cursor.close()
        return result_dict

    def find_all(self):
        """
        获取所有数据
        Returns:
            List[dict]: 所有数据结果
        """
        cursor = self.connection.cursor()
        query = f"SELECT * FROM {self.table_name}"
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        all_results = []
        for result in results:
            result_dict = {column[0]: value for column, value in zip(cursor.description, result)}
            all_results.append(result_dict)
        return all_results

    def find_by_criteria(self, criteria: dict):
        """
        通过自定义条件查找数据
        Args:
            criteria (dict): 包含查询条件的字典，如 {'name': 'John', 'age': 25}
        Returns:
            List[dict]: 符合条件的结果
        """
        conditions = []
        values = []
        for key, value in criteria.items():
            conditions.append(f"{key} = %s")
            values.append(value)
        condition_str = " AND ".join(conditions)
        cursor = self.connection.cursor()
        query = f"SELECT * FROM {self.table_name} WHERE {condition_str}"
        cursor.execute(query, tuple(values))
        results = cursor.fetchall()
        cursor.close()
        return [dict(result) for result in results]

    def insert(self, entity: dict):
        """
        插入一条数据
        Args:
            entity (dict): 要插入的数据，如 {'name': 'John', 'age': 25}
        """
        keys = ', '.join(entity.keys())
        values_placeholders = ', '.join(['%s'] * len(entity))
        cursor = self.connection.cursor()
        query = f"INSERT INTO {self.table_name} ({keys}) VALUES ({values_placeholders})"
        cursor.execute(query, tuple(entity.values()))
        self.connection.commit()
        cursor.close()

    def update(self, entity: dict):
        """
        根据实体对象更新数据
        Args:
            entity (dict): 包含更新字段和值的字典，必须包含主键
        """
        set_statements = []
        values = []
        for key, value in entity.items():
            if key != 'id':  # 假设 'id' 是主键
                set_statements.append(f"{key} = %s")
                values.append(value)
        set_str = ', '.join(set_statements)
        cursor = self.connection.cursor()
        query = f"UPDATE {self.table_name} SET {set_str} WHERE id = %s"
        values.append(entity['id'])
        cursor.execute(query, tuple(values))
        self.connection.commit()
        cursor.close()

    def delete_by_id(self, id: int):
        """
        根据主键 ID 删除数据
        Args:
            id (int): 主键值
        """
        cursor = self.connection.cursor()
        query = f"DELETE FROM {self.table_name} WHERE id = %s"
        cursor.execute(query, (id,))
        self.connection.commit()
        cursor.close()

    def batch_insert(self, entities: List[dict]):
        """
        批量插入数据
        Args:
            entities (List[dict]): 要批量插入的数据列表
        """
        keys = ', '.join(entities[0].keys())
        values_placeholders = ', '.join(['%s'] * len(entities[0]))
        cursor = self.connection.cursor()
        values_list = [tuple(entity.values()) for entity in entities]
        query = f"INSERT INTO {self.table_name} ({keys}) VALUES ({values_placeholders})"
        cursor.executemany(query, values_list)
        self.connection.commit()
        cursor.close()

    def batch_update(self, entities: List[dict]):
        """
        批量更新数据
        Args:
            entities (List[dict]): 要批量更新的数据列表，每个字典必须包含主键
        """
        for entity in entities:
            set_statements = []
            values = []
            for key, value in entity.items():
                if key != 'id':  # 假设 'id' 是主键
                    set_statements.append(f"{key} = %s")
                    values.append(value)
            set_str = ', '.join(set_statements)
            cursor = self.connection.cursor()
            query = f"UPDATE {self.table_name} SET {set_str} WHERE id = %s"
            values.append(entity['id'])
            cursor.execute(query, tuple(values))
        self.connection.commit()
        cursor.close()


# 示例用法
if __name__ == "__main__":
    mybatis_plus = MyBatisPlusUtils(
        database_url="localhost",
        database_user="root",
        database_password="1202",
        database_name="bk_tm_db",
        table_name="test"
    )

    # 查找示例
    # result = mybatis_plus.find_by_id(1)
    # print(result)

    # 查找全部示例
    # all_results = mybatis_plus.find_all()
    # print(all_results)

    # 查找指定查找示例
    # criteria = {'product_name': 'John', 'price': 0}
    # criteria_results = mybatis_plus.find_by_criteria(criteria)
    # print(criteria_results)

    # 插入示例
    # entity_to_insert = {'product': 'SomeValueForPro31duct', 'product_name': 'Alice'}
    # mybatis_plus.insert(entity_to_insert)

    # 更新示例
    # entity_to_update = {'id': 1, 'product': 30}
    # mybatis_plus.update(entity_to_update)

    # 删除示例
    # mybatis_plus.delete_by_id(2)

    # 批量插入示例
    # entities_to_batch_insert = [
    #     {'product': 'Bob', 'product_name': 22},
    #     {'product': 'Charlie', 'product_name': 23}
    # ]
    # mybatis_plus.batch_insert(entities_to_batch_insert)

    # 批量更新示例
    # entities_to_batch_update = [
    #     {'id': 3, 'product': 25},
    #     {'id': 4, 'product': 26}
    # ]
    # mybatis_plus.batch_update(entities_to_batch_update)
