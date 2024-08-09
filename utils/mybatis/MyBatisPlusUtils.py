#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    : MyBatisPlusUtils.py
@Author  : ChenLiRui
@Time    : 2024/8/1 上午8:25
@explain : MyBatisPlus工具类
"""
import pymysql
import decimal
import json
from typing import List, Dict, Any, Union, Optional
from utils.log.my_logger import logger


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

    def find_all(self) -> List[dict]:
        """
        获取所有数据
        Returns:
            List[dict]: 所有数据结果
        """
        try:
            cursor = self.connection.cursor()
            query = f"SELECT * FROM {self.table_name}"
            cursor.execute(query)
            results = cursor.fetchall()
            all_results = [{column[0]: value for column, value in zip(cursor.description, result)} for result in
                           results]
            cursor.close()
            logger.info(f"成功从表 {self.table_name} 获取所有数据")
            return all_results
        except Exception as e:
            logger.error(f"获取所有数据时出错: {e}")
            return []

    def find_by_id(self, id) -> dict:
        """
        根据主键 ID 查找数据
        Args:
            id: 主键值，类型可以是 int、str 等
        Returns:
            dict: 查找结果
        """
        try:
            cursor = self.connection.cursor()
            # 检查 id 类型
            if isinstance(id, int):
                query = f"SELECT * FROM {self.table_name} WHERE id = %s"
                query_params = (id,)
            elif isinstance(id, str):
                query = f"SELECT * FROM {self.table_name} WHERE id = %s"
                query_params = (id,)
            else:
                logger.error(f"不支持的 ID 类型: {type(id)}")
                return {}
            cursor.execute(query, query_params)
            result = cursor.fetchone()
            result_dict = {column[0]: value for column, value in zip(cursor.description, result)} if result else {}
            cursor.close()
            logger.info(f"成功从表 {self.table_name} 根据 ID 查找数据")
            return result_dict
        except Exception as e:
            logger.error(f"查找数据时出错: {e}")
            return {}

    def insert_or_update(self, entity: dict) -> bool:
        """
        插入数据或在插入失败时更新数据（如果主键存在才更新）
        Args:
            entity (dict): 数据，可能包含主键字段'id'
        Returns:
            bool: 操作结果
        """
        if not entity:
            logger.error("提供的实体为空")
            return False

        try:
            cursor = self.connection.cursor()

            # 处理布尔值
            processed_entity = {k: (1 if v is True else 0 if v is False else v) for k, v in entity.items()}

            # 插入操作
            keys = ', '.join(f"`{key}`" for key in processed_entity.keys())
            values_placeholders = ', '.join(['%s'] * len(processed_entity))
            insert_query = f"INSERT INTO `{self.table_name}` ({keys}) VALUES ({values_placeholders})"

            try:
                cursor.execute(insert_query, tuple(processed_entity.values()))
                self.connection.commit()
                logger.info(f"成功向表 `{self.table_name}` 插入数据")
                return True
            except pymysql.err.IntegrityError as e:
                # 插入失败，检查是否为主键冲突
                if e.args[0] == 1062:  # 主键冲突错误代码
                    logger.info("主键冲突，尝试更新")

                    if 'id' not in processed_entity:
                        logger.error("主键冲突，但提供的实体没有主键'id'")
                        return False

                    # 主键冲突，执行更新操作
                    primary_key = 'id'
                    primary_key_value = processed_entity.get(primary_key)
                    set_statements = [f"`{k}` = %s" for k in processed_entity if k != primary_key]
                    set_str = ', '.join(set_statements)
                    update_query = f"UPDATE `{self.table_name}` SET {set_str} WHERE `{primary_key}` = %s"

                    try:
                        cursor.execute(update_query,
                                       tuple(v for k, v in processed_entity.items() if k != primary_key) + (
                                           primary_key_value,))
                        self.connection.commit()
                        logger.info(f"成功更新表 `{self.table_name}` 中的记录")
                        return True
                    except Exception as e:
                        logger.error(f"更新数据时出错: {e}")
                        return False
                else:
                    logger.error(f"插入数据时完整性错误: {e}")
                    return False
        except Exception as e:
            logger.error(f"插入或更新数据时出错: {e}")
            return False
        finally:
            cursor.close()

    def delete_by_id(self, id) -> bool:
        """
        根据 ID 删除数据
        Args:
            id (Union[int, str]): 主键值，可以是整数或字符串
        Returns:
            bool: 操作结果
        """
        try:
            cursor = self.connection.cursor()
            query = f"DELETE FROM {self.table_name} WHERE id = %s"
            cursor.execute(query, (id,))
            self.connection.commit()
            cursor.close()
            logger.info(f"成功删除数据，ID: {id}")
            return True
        except Exception as e:
            logger.error(f"删除数据时出错: {e}")
            return False

    def fake_delete_by_id(self, id) -> bool:
        """
        假删除数据（将 is_delete 字段设为 1）
        Args:
            id (Union[int, str]): 主键值，可以是整数或字符串
        Returns:
            bool: 操作结果
        """
        try:
            cursor = self.connection.cursor()
            query = f"UPDATE {self.table_name} SET is_delete = 1 WHERE id = %s"
            cursor.execute(query, (id,))
            self.connection.commit()
            cursor.close()
            logger.info(f"成功假删除数据，ID: {id}")
            return True
        except Exception as e:
            logger.error(f"假删除数据时出错: {e}")
            return False

    def find_by_equals(self, equal: Dict[str, Any] = None, unequal: Dict[str, Any] = None) -> List[dict]:
        """
        根据自定义条件查找数据
        Args:
            equal (Dict[str, Any], optional): 查询条件，键为字段名，值为条件值
            unequal (Dict[str, Any], optional): 排除条件，键为字段名，值为条件值
        Returns:
            List[dict]: 符合条件的数据
        """
        try:
            conditions = []
            query_params = []

            if equal:
                _process_conditions(conditions, query_params, equal, "=")

            if unequal:
                _process_conditions(conditions, query_params, unequal, "!=")

            final_data = " AND ".join(conditions) if conditions else "1=1"

            cursor = self.connection.cursor()
            query = f"SELECT * FROM `{self.table_name}` WHERE {final_data}"
            cursor.execute(query, query_params)
            results = cursor.fetchall()
            cursor.close()

            logger.info("成功根据条件查找数据")
            return [{column[0]: value for column, value in zip(cursor.description, result)} for result in results]
        except Exception as e:
            logger.error(f"查找数据时出错: {e}")
            return []

    def update_by_equals(self, update_entity: dict = None, equals: dict = None, unequals: dict = None) -> bool:
        """
        根据条件更新数据
        Args:
            update_entity (dict): 更新内容
            equals (dict): 筛选条件
            unequals (dict): 排除条件
        Returns:
            bool: 操作结果
        """
        try:
            set_statements = [f"`{k}` = %s" for k in (update_entity or {}).keys()]
            set_str = ', '.join(set_statements)

            conditions = []
            query_params = []

            if equals:
                _process_conditions(conditions, query_params, equals, "=")
            if unequals:
                _process_conditions(conditions, query_params, unequals, "!=")

            final_data = " AND ".join(conditions) if conditions else "1=1"

            query = f"UPDATE `{self.table_name}` SET {set_str} WHERE {final_data}"
            values = list(update_entity.values()) + query_params

            cursor = self.connection.cursor()
            cursor.execute(query, tuple(values))
            self.connection.commit()
            cursor.close()

            logger.info("成功根据条件更新数据")
            return True
        except Exception as e:
            logger.error(f"更新数据时出错: {e}")
            return False

    def delete_by_equals(self, equals: dict = None, unequals: dict = None) -> bool:
        """
        根据指定条件从表 {self.table_name} 删除数据，并排除某些属性具有特定值的记录
        Args:
            equals (dict, optional): 包含删除条件的字典，如 {'name': 'John', 'age': 25}
            unequals (dict, optional): 包含需要排除的属性值对，如 {'status': 'inactive'}
        Returns:
            bool: 操作成功返回 True，失败返回 False
        """
        try:
            conditions = []
            query_params = []

            if equals:
                _process_conditions(conditions, query_params, equals, "=")

            if unequals:
                _process_conditions(conditions, query_params, unequals, "!=")

            final_data = " AND ".join(conditions) if conditions else "1=1"

            cursor = self.connection.cursor()
            query = f"DELETE FROM `{self.table_name}` WHERE {final_data}"
            cursor.execute(query, query_params)
            self.connection.commit()
            cursor.close()

            logger.info("成功根据条件删除数据")
            return True
        except Exception as e:
            logger.error(f"删除数据时出错: {e}")
            return False

    def fake_delete_by_equals(self, equals: dict = None, unequals: dict = None) -> bool:
        """
        根据指定条件假删除数据（将 is_delete 字段修改为 1），并排除某些属性具有特定值的记录
        Args:
            equals (dict, optional): 包含假删除条件的字典，如 {'name': 'John', 'age': 25}
            unequals (dict, optional): 包含需要排除的属性值对，如 {'status': 'inactive'}
        Returns:
            bool: 操作成功返回 True，失败返回 False
        """
        try:
            conditions = []
            query_params = []

            if equals:
                _process_conditions(conditions, query_params, equals, "=")

            if unequals:
                _process_conditions(conditions, query_params, unequals, "!=")

            final_data = " AND ".join(conditions) if conditions else "1=1"

            cursor = self.connection.cursor()
            query = f"UPDATE `{self.table_name}` SET `is_delete` = 1 WHERE {final_data}"
            cursor.execute(query, query_params)
            self.connection.commit()
            cursor.close()

            logger.info("成功根据条件假删除数据")
            return True
        except Exception as e:
            logger.error(f"假删除数据时出错: {e}")
            return False

    def batch_insert(self, entities: List[dict]) -> bool:
        """
        批量向表 {self.table_name} 插入数据
        Args:
            entities (List[dict]): 要批量插入的数据列表
        Returns:
            bool: 操作成功返回 True，失败返回 False
        """
        if not entities:
            logger.warning("没有提供要插入的数据")
            return False

        try:
            # 数据预处理
            processed_entities = []
            for entity in entities:
                new_entity = {}
                for key, value in entity.items():
                    # 处理空值、布尔值和其他特殊情况
                    if value is None:
                        new_entity[key] = None  # 将 None 转为数据库中的 NULL
                    elif isinstance(value, bool):
                        new_entity[key] = 1 if value else 0  # 布尔值存储为整数
                    elif isinstance(value, (int, float)):
                        new_entity[key] = value
                    elif isinstance(value, str):
                        new_entity[key] = value  # 空字符串保留为 ""，字符串字段不会转换
                    elif isinstance(value, (list, dict)):
                        new_entity[key] = json.dumps(value)  # 将 JSON 对象转换为字符串
                    else:
                        new_entity[key] = str(value)  # 其他类型转为字符串
                processed_entities.append(new_entity)

            if not processed_entities:
                logger.error("处理后的数据为空，无法进行插入操作")
                return False

            # 确定字段名和占位符
            keys = ', '.join(f"`{key}`" for key in processed_entities[0].keys())
            values_placeholders = ', '.join(['%s'] * len(processed_entities[0]))

            # 准备执行批量插入
            cursor = self.connection.cursor()
            values_list = [tuple(entity.values()) for entity in processed_entities]
            query = f"INSERT INTO `{self.table_name}` ({keys}) VALUES ({values_placeholders})"

            cursor.executemany(query, values_list)
            self.connection.commit()
            cursor.close()

            logger.info(f"成功向表 `{self.table_name}` 批量插入数据")
            logger.debug(f"传入参数: {entities}")
            return True

        except pymysql.err.IntegrityError as e:
            logger.error(f"数据完整性错误: {e}")
            return False
        except Exception as e:
            logger.error(f"向表 `{self.table_name}` 批量插入数据时出错: {e}")
            return False

    def batch_update(self, entities: List[Dict[str, Optional[Union[int, str]]]],
                     equals: Optional[Dict[str, Optional[Union[int, str]]]] = None,
                     unequals: Optional[Dict[str, Optional[Union[int, str]]]] = None) -> bool:
        """
        批量更新数据
        Args:
            entities (List[Dict[str, Optional[Union[int, str]]]]): 要批量更新的数据列表，每个字典必须包含主键（如 'id'）
            equals (Optional[Dict[str, Optional[Union[int, str]]]]): 筛选条件
            unequals (Optional[Dict[str, Optional[Union[int, str]]]]): 排除条件
        Returns:
            bool: 操作成功返回 True，失败返回 False
        """
        if not entities:
            logger.warning("更新操作的实体列表为空")
            return False

        try:
            cursor = self.connection.cursor()

            # 准备 SET 语句
            set_statements = [f"`{key}` = %s" for key in entities[0].keys() if key != 'id']
            set_str = ', '.join(set_statements)

            # 准备条件
            conditions = []
            query_params = []

            if equals:
                build_conditions(conditions, query_params, equals, "=")
            if unequals:
                build_conditions(conditions, query_params, unequals, "!=")

            final_conditions = " AND ".join(conditions) if conditions else "1=1"

            # 执行更新操作
            update_query = f"UPDATE `{self.table_name}` SET {set_str} WHERE {final_conditions}"

            for entity in entities:
                values = [entity[key] for key in entity if key != 'id']
                values += query_params
                cursor.execute(update_query, tuple(values))

            self.connection.commit()
            cursor.close()

            logger.info(f"成功从表 {self.table_name} 批量更新数据")
            logger.debug(f"传入参数: {entities}")
            return True
        except Exception as e:
            logger.error(f"从表 {self.table_name} 批量更新数据时出错: {e}")
            logger.error(f"传入参数: {entities}")
            return False

    def batch_delete_by_ids(self, ids: List[Union[int, str]]) -> bool:
        """
        批量根据主键 ID 删除数据
        Args:
            ids (List[Union[int, str]]): 主键值列表，支持 int 和 str 类型
        Returns:
            bool: 操作成功返回 True，失败返回 False
        """
        if not ids:
            logger.warning("删除操作的 ID 列表为空")
            return False

        try:
            cursor = self.connection.cursor()
            # 创建一个 IN 查询的占位符
            placeholders = ', '.join(['%s'] * len(ids))
            query = f"DELETE FROM {self.table_name} WHERE id IN ({placeholders})"
            cursor.execute(query, ids)
            self.connection.commit()
            logger.info(f"成功从表 {self.table_name} 批量根据主键 ID 删除数据")
            logger.debug(f"传入参数: {ids}")
            return True
        except Exception as e:
            logger.error(f"从表 {self.table_name} 批量根据主键 ID 删除数据时出错: {e}")
            logger.error(f"传入参数: {ids}")
            return False
        finally:
            cursor.close()

    def batch_fake_delete_by_ids(self, ids: List[Union[int, str]]) -> bool:
        """
        批量假删除，将 is_delete 字段修改为 1 来表示删除
        Args:
            ids (List[Union[int, str]]): 主键值列表，支持 int 和 str 类型
        Returns:
            bool: 操作成功返回 True，失败返回 False
        """
        if not ids:
            logger.warning("假删除操作的 ID 列表为空")
            return False

        try:
            cursor = self.connection.cursor()
            # 创建一个 IN 查询的占位符
            placeholders = ', '.join(['%s'] * len(ids))
            query = f"UPDATE {self.table_name} SET is_delete = 1 WHERE id IN ({placeholders})"
            cursor.execute(query, ids)
            self.connection.commit()
            logger.info(f"成功从表 {self.table_name} 批量假删除数据")
            logger.debug(f"传入参数: {ids}")
            return True
        except Exception as e:
            logger.error(f"从表 {self.table_name} 批量假删除数据时出错: {e}")
            logger.error(f"传入参数: {ids}")
            return False
        finally:
            cursor.close()


def _process_conditions(conditions: List[str], params: List[Any], condition_dict: Dict[str, Any],
                        operator: str) -> None:
    """
    处理查询条件
    Args:
        conditions (List[str]): 用于存储 SQL 条件的列表
        params (List[Any]): 用于存储查询参数的列表
        condition_dict (Dict[str, Any]): 条件字典，键为字段名，值为条件值
        operator (str): 操作符，"=" 或 "!="
    """
    for k, v in condition_dict.items():
        if v is None:
            if operator == "=":
                conditions.append(f"`{k}` IS NULL")
            else:  # operator == "!="
                conditions.append(f"`{k}` IS NOT NULL")
        elif isinstance(v, bool):
            # 处理布尔类型
            conditions.append(f"`{k}` {operator} %s")
            params.append(1 if v else 0)
        elif isinstance(v, (str, int, float, decimal.Decimal, bytes)):
            conditions.append(f"`{k}` {operator} %s")
            params.append(v)
        else:
            conditions.append(f"`{k}` {operator} %s")
            params.append(v)


def build_conditions(conditions: List[str], query_params: List[Optional[Union[int, str]]],
                     conditions_dict: Dict[str, Optional[Union[int, str]]], operator: str):
    """
    构建 SQL 查询条件
    Args:
        conditions (List[str]): 存储 SQL 条件的列表
        query_params (List[Optional[Union[int, str]]]): 存储条件参数的列表
        conditions_dict (Dict[str, Optional[Union[int, str]]]): 条件字典
        operator (str): 条件操作符，例如 "=" 或 "!="
    """
    for key, value in conditions_dict.items():
        conditions.append(f"`{key}` {operator} %s")
        query_params.append(value)
