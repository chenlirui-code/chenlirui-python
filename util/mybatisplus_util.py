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

from util.database_util import DatabaseUtils

logging.basicConfig(level=logging.INFO)
from typing import List

# !/usr/bin/env python
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
    def __del__(self):
        """
        在对象被销毁时关闭数据库连接
        """
        if hasattr(self, 'connection') and self.connection:
            self.connection.close()

    def __init__(self, connection, table_name: str):
        self.connection = connection
        self.table_name = table_name

    def find_by_id(self, id: int):
        """
        根据主键 ID 从表 {self.table_name} 查找数据
        Args:
            id (int): 主键值
        Returns:
            dict: 查找结果
        """
        try:
            cursor = self.connection.cursor()
            query = f"SELECT * FROM {self.table_name} WHERE id = %s"
            cursor.execute(query, (id,))
            result = cursor.fetchone()
            if result:
                result_dict = {column[0]: value for column, value in zip(cursor.description, result)}
            cursor.close()
            logging.info(f"成功从表 {self.table_name} 根据 ID {id} 查找数据")
            logging.info(f"传入参数: {id}")
            return result_dict
        except Exception as e:
            logging.error(f"从表 {self.table_name} 根据 ID {id} 查找数据时出错: {e}")
            logging.error(f"传入参数: {id}")

    def find_all(self):
        """
        从表 {self.table_name} 获取所有数据
        Returns:
            List[dict]: 所有数据结果
        """
        try:
            cursor = self.connection.cursor()
            query = f"SELECT * FROM {self.table_name}"
            cursor.execute(query)
            results = cursor.fetchall()
            cursor.close()
            all_results = []
            for result in results:
                result_dict = {column[0]: value for column, value in zip(cursor.description, result)}
                all_results.append(result_dict)
            logging.info(f"成功从表 {self.table_name} 获取所有数据")
            return all_results
        except Exception as e:
            logging.error(f"从表 {self.table_name} 获取所有数据时出错: {e}")

    def find_by_conditions(self, criteria: dict, excluded_values: dict):
        """
        通过自定义条件从表 {self.table_name} 查找数据，并排除某些属性具有特定值的记录
        Args:
            criteria (dict): 包含查询条件的字典，如 {'name': 'John', 'age': 25}
            excluded_values (dict): 包含需要排除的属性值对，如 {'status': 'inactive'}
        Returns:
            List[dict]: 符合条件且不包含排除值的结果
        """
        try:
            condition_str = " AND ".join([f"{key} = '{value}'" for key, value in criteria.items()])
            excluded_condition_str = " AND ".join([f"{key}!= '{value}'" for key, value in excluded_values.items()])
            cursor = self.connection.cursor()
            query = f"SELECT * FROM {self.table_name} WHERE {condition_str} AND {excluded_condition_str}"
            cursor.execute(query)
            results = cursor.fetchall()
            cursor.close()
            logging.info(f"成功从表 {self.table_name} 根据条件 {criteria} 且排除 {excluded_values} 查找数据")
            logging.info(f"传入参数: {criteria}, {excluded_values}")
            return results
        except Exception as e:
            logging.error(f"从表 {self.table_name} 根据条件 {criteria} 且排除 {excluded_values} 查找数据时出错: {e}")
            logging.error(f"传入参数: {criteria}, {excluded_values}")

    def insert(self, entity: dict):
        """
        向表 {self.table_name} 插入一条数据
        Args:
            entity (dict): 要插入的数据，如 {'name': 'John', 'age': 25}
        """
        try:
            keys = ', '.join(entity.keys())
            values_placeholders = ', '.join(['%s'] * len(entity))
            cursor = self.connection.cursor()
            query = f"INSERT INTO {self.table_name} ({keys}) VALUES ({values_placeholders})"
            cursor.execute(query, tuple(entity.values()))
            self.connection.commit()
            cursor.close()
            logging.info(f"成功向表 {self.table_name} 插入数据")
            logging.info(f"传入参数: {entity}")
        except Exception as e:
            logging.error(f"向表 {self.table_name} 插入数据时出错: {e}")
            logging.error(f"传入参数: {entity}")

    def update_by_id(self, entity: dict):
        """
        根据实体对象从表 {self.table_name} 更新数据
        Args:
            entity (dict): 包含更新字段和值的字典，必须包含主键
        """
        try:
            set_statements = []
            values = []
            keys = []
            for key, value in entity.items():
                if key != 'id':  # 假设 'id' 是主键
                    set_statements.append(f"{key} = %s")
                    keys.append(key)
                    values.append(value)
            set_str = ', '.join(set_statements)
            cursor = self.connection.cursor()
            query = f"UPDATE {self.table_name} SET {set_str} WHERE id = %s"
            values.append(entity['id'])
            cursor.execute(query, tuple(values))
            self.connection.commit()
            cursor.close()
            logging.info(f"成功从表 {self.table_name} 根据 ID 更新数据")
            logging.info(f"传入参数: {entity}")
        except Exception as e:
            logging.error(f"从表 {self.table_name} 根据 ID 更新数据时出错: {e}")
            logging.error(f"传入参数: {entity}")

    def update_by_conditions(self, update_entity: dict, conditions: dict):
        """
        根据指定的条件从表 {self.table_name} 和更新内容更新数据
        Args:
            update_entity (dict): 包含要更新的字段和值的字典
            conditions (dict): 用于筛选的条件字典
        """
        try:
            set_statements = []
            set_values = []
            condition_statements = []
            condition_values = []

            for key, value in update_entity.items():
                set_statements.append(f"{key} = %s")
                set_values.append(value)

            for key, value in conditions.items():
                condition_statements.append(f"{key} = %s")
                condition_values.append(value)

            set_str = ', '.join(set_statements)
            condition_str = " AND ".join(condition_statements)

            cursor = self.connection.cursor()
            query = f"UPDATE {self.table_name} SET {set_str} WHERE {condition_str}"
            values = set_values + condition_values
            cursor.execute(query, tuple(values))
            self.connection.commit()
            cursor.close()
            logging.info(f"成功从表 {self.table_name} 根据条件和更新内容更新数据")
            logging.info(f"传入参数: update_entity: {update_entity}, conditions: {conditions}")
        except Exception as e:
            logging.error(f"从表 {self.table_name} 根据条件和更新内容更新数据时出错: {e}")
            logging.error(f"传入参数: update_entity: {update_entity}, conditions: {conditions}")

    def insert_or_update(self, entity: dict):
        """
        尝试向表 {self.table_name} 插入数据，如果主键冲突则进行更新
        如果插入失败，输出日志并尝试更新，最后告知操作是成功还是失败，以及是插入还是更新操作
        Args:
            entity (dict): 包含数据的字典
        """
        insert_successful = False
        update_successful = False
        try:
            cursor = self.connection.cursor()
            keys = ', '.join(entity.keys())
            values_placeholders = ', '.join(['%s'] * len(entity))
            insert_query = f"INSERT INTO {self.table_name} ({keys}) VALUES ({values_placeholders})"
            cursor.execute(insert_query, tuple(entity.values()))
            self.connection.commit()
            insert_successful = True
            logging.info(f"成功向表 {self.table_name} 插入数据")
            logging.info(f"传入参数: {entity}")
        except pymysql.err.IntegrityError as e:
            if e.args[0] == 1062:
                logging.info(f"插入数据时因主键冲突，尝试更新")
                set_statements = []
                values = []
                primary_key = 'id' if 'id' in entity else list(entity.keys())[0]
                for key, value in entity.items():
                    if key != primary_key:
                        set_statements.append(f"{key} = %s")
                        values.append(value)
                set_str = ', '.join(set_statements)
                update_query = f"UPDATE {self.table_name} SET {set_str} WHERE {primary_key} = %s"
                values.append(entity[primary_key])
                cursor.execute(update_query, tuple(values))
                self.connection.commit()
                update_successful = True
                logging.info(f"成功从表 {self.table_name} 因主键冲突进行更新数据")
                logging.info(f"传入参数: {entity}")
            else:
                logging.error(f"向表 {self.table_name} 插入数据时出现其他完整性错误: {e}")
                logging.error(f"传入参数: {entity}")
        except Exception as e:
            logging.error(f"向表 {self.table_name} 插入数据时出错: {e}")
            logging.error(f"传入参数: {entity}")
        finally:
            cursor.close()
        if not insert_successful and not update_successful:
            logging.error(f"向表 {self.table_name} 插入和更新数据均失败")
            logging.error(f"传入参数: {entity}")

    def delete_by_id(self, id: int):
        """
        根据主键 ID 从表 {self.table_name} 删除数据
        Args:
            id (int): 主键值
        """
        try:
            cursor = self.connection.cursor()
            query = f"DELETE FROM {self.table_name} WHERE id = %s"
            cursor.execute(query, (id,))
            self.connection.commit()
            cursor.close()
            logging.info(f"成功从表 {self.table_name} 根据 ID {id} 删除数据")
            logging.info(f"传入参数: {id}")
        except Exception as e:
            logging.error(f"从表 {self.table_name} 根据 ID {id} 删除数据时出错: {e}")
            logging.error(f"传入参数: {id}")

    def fake_delete_by_id(self, id: int):
        """
        假删除，将 is_delete 字段修改为 1 来表示从表 {self.table_name} 删除
        Args:
            id (int): 主键值
        """
        try:
            cursor = self.connection.cursor()
            query = f"UPDATE {self.table_name} SET is_delete = 1 WHERE id = %s"
            cursor.execute(query, (id,))
            self.connection.commit()
            cursor.close()
            logging.info(f"成功从表 {self.table_name} 假删除根据 ID {id} 的数据")
            logging.info(f"传入参数: {id}")
        except Exception as e:
            logging.error(f"从表 {self.table_name} 假删除根据 ID {id} 的数据时出错: {e}")
            logging.error(f"传入参数: {id}")

    def delete_by_conditions(self, conditions: dict):
        """
        根据指定条件从表 {self.table_name} 删除数据
        Args:
            conditions (dict): 用于筛选的条件字典
        """
        try:
            conditions_statements = []
            condition_values = []

            for key, value in conditions.items():
                conditions_statements.append(f"{key} = %s")
                condition_values.append(value)

            condition_str = " AND ".join(conditions_statements)

            cursor = self.connection.cursor()
            query = f"DELETE FROM {self.table_name} WHERE {condition_str}"
            cursor.execute(query, tuple(condition_values))
            self.connection.commit()
            logging.info(f"成功从表 {self.table_name} 根据条件删除数据")
            logging.info(f"传入参数: {conditions}")
        except Exception as e:
            logging.error(f"从表 {self.table_name} 根据条件删除数据时出错: {e}")
            logging.error(f"传入参数: {conditions}")
        finally:
            cursor.close()

    def fake_delete_by_conditions(self, conditions: dict):
        """
        根据指定条件假删除数据（将 is_delete 字段修改为 1）
        Args:
            conditions (dict): 用于筛选的条件字典
        """
        try:
            conditions_statements = []
            condition_values = []

            for key, value in conditions.items():
                conditions_statements.append(f"{key} = %s")
                condition_values.append(value)

            condition_str = " AND ".join(conditions_statements)

            cursor = self.connection.cursor()
            query = f"UPDATE {self.table_name} SET is_delete = 1 WHERE {condition_str}"
            cursor.execute(query, tuple(condition_values))
            self.connection.commit()
            logging.info(f"成功从表 {self.table_name} 根据条件假删除数据")
            logging.info(f"传入参数: {conditions}")
        except Exception as e:
            logging.error(f"从表 {self.table_name} 根据条件假删除数据时出错: {e}")
            logging.error(f"传入参数: {conditions}")
        finally:
            cursor.close()

    def batch_insert(self, entities: List[dict]):
        """
        批量向表 {self.table_name} 插入数据
        Args:
            entities (List[dict]): 要批量插入的数据列表
        """
        try:
            keys = ', '.join(entities[0].keys())
            values_placeholders = ', '.join(['%s'] * len(entities[0]))
            cursor = self.connection.cursor()
            values_list = [tuple(entity.values()) for entity in entities]
            query = f"INSERT INTO {self.table_name} ({keys}) VALUES ({values_placeholders})"
            cursor.executemany(query, values_list)
            self.connection.commit()
            cursor.close()
            logging.info(f"成功向表 {self.table_name} 批量插入数据")
            logging.info(f"传入参数: {entities}")
        except Exception as e:
            logging.error(f"向表 {self.table_name} 批量插入数据时出错: {e}")
            logging.error(f"传入参数: {entities}")

    def batch_update(self, entities: List[dict]):
        """
        批量更新数据
        Args:
            entities (List[dict]): 要批量更新的数据列表，每个字典必须包含主键
        """
        try:
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
            logging.info(f"成功从表 {self.table_name} 批量更新数据")
            logging.info(f"传入参数: {entities}")
        except Exception as e:
            logging.error(f"从表 {self.table_name} 批量更新数据时出错: {e}")
            logging.error(f"传入参数: {entities}")
        finally:
            cursor.close()

    def batch_delete_by_ids(self, ids: List[int]):
        """
        批量根据主键 ID 删除数据
        Args:
            ids (List[int]): 主键值列表
        """
        try:
            for id in ids:
                cursor = self.connection.cursor()
                query = f"DELETE FROM {self.table_name} WHERE id = %s"
                cursor.execute(query, (id,))
            self.connection.commit()
            logging.info(f"成功从表 {self.table_name} 批量根据主键 ID 删除数据")
            logging.info(f"传入参数: {ids}")
        except Exception as e:
            logging.error(f"从表 {self.table_name} 批量根据主键 ID 删除数据时出错: {e}")
            logging.error(f"传入参数: {ids}")
        finally:
            cursor.close()

    def batch_fake_delete_by_ids(self, ids: List[int]):
        """
        批量假删除，将 is_delete 字段修改为 1 来表示删除
        Args:
            ids (List[int]): 主键值列表
        """
        try:
            for id in ids:
                cursor = self.connection.cursor()
                query = f"UPDATE {self.table_name} SET is_delete = 1 WHERE id = %s"
                cursor.execute(query, (id,))
            self.connection.commit()
            logging.info(f"成功从表 {self.table_name} 批量假删除数据")
            logging.info(f"传入参数: {ids}")
        except Exception as e:
            logging.error(f"从表 {self.table_name} 批量假删除数据时出错: {e}")
            logging.error(f"传入参数: {ids}")
        finally:
            cursor.close()


# 示例用法
if __name__ == "__main__":
    database_url = "localhost"
    database_user = "root"
    database_password = "1202"
    database_name = "bk_tm_db"
    connection = DatabaseUtils.create_connection(
        database_url,
        database_user,
        database_password,
        database_name,
    )
    mybatis_plus = MyBatisPlusUtils(
        connection=connection,
        table_name="t"
    )

    # 查找示例
    # result = mybatis_plus.find_by_id(1)
    # print(result)

    # 查找全部示例
    # all_results = mybatis_plus.find_all()
    # print(all_results)

    # 查找指定查找示例
    # criteria = {'is_delete': '0'}
    # criteria_results = mybatis_plus.find_by_criteria(criteria)
    # print(criteria_results)

    # 插入示例
    # entity_to_insert = {'product': 'SomeValueForPro31duct', 'product_name': 'Alice'}
    # mybatis_plus.insert(entity_to_insert)

    # 更新示例
    # entity_to_update = {'id': 1, 'product': 30}
    # mybatis_plus.update_by_id(entity_to_update)

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

    # 关闭数据库连接
    DatabaseUtils.close_connection(connection)
