#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    : test_insert_bach.py
@Author  : ChenLiRui
@Time    : 2024/8/8 下午7:00
@explain : 文件说明
"""
from datetime import datetime

from utils.database.DatabaseUtils import DatabaseUtils
from utils.mybatis.MyBatisPlusUtils import MyBatisPlusUtils

if __name__ == '__main__':
    # 连接数据库
    host = 'localhost'
    user = 'root'
    password = '1202'
    database = 'guanyierp'
    conn = DatabaseUtils.create_connection(host, user, password, database)
    data = [{
        'id': '667986498409',
        'tenantId': '13487759595',
        'code': '102100405',
        'name': '卡培他滨片（卓仑）---0.15g*10片/盒——齐鲁制药有限公司',
        'simpleName': '',
        'del': False,
        'note': '102100405',
        'categoryId': '247789055525',
        'supplierId': None,
        'unitId': None,
        'weight': '0.0',
        'volume': '0.0',
        'packagePoint': '0.0',
        'salesPoint': '0.0',
        'salesPrice': '0.0',
        'purchasePrice': '0.0',
        'agentPrice': '0.0',
        'costPrice': '18.3',
        'productInsuredAmount': '0.0',
        'stockStatusId': None,
        'stockStatusName': None,
        'combine': False,
        'autoSplit': False,
        'combineSale': None,
        'combineDistribute': None,
        'combineStock': None,
        'skus': [],
        'supplierName': None,
        'itemCategoryName': '处方药 - 肿瘤用药',
        'itemSkuId': None,
        'itemSkuName': None,
        'itemCount': None,
        'skuId': None,
        'itemId': None,
        'itemUnitName': None,
        'itemCombineInfoList': [],
        'picUrl': '',
        'picIp': None,
        'taxNo': '',
        'taxRate': '0.0',
        'originArea': '',
        'supplierOuterId': '',
        'itemAttrList': None,
        'itemAttrInfoValueList': None,
        'itemAttrInfoPropIdList': None,
        'itemAttrRaValueList': None,
        'itemAttrTaValueList': None,
        'itemAttrTaPropIdList': None,
        'itemAttrRaPropIdList': None,
        'itemAttrCkValueList': None,
        'itemAttrCkPropIdList': None,
        'itemCombineRowsList': None,
        'imeiType': 0,
        'imeiTypeName': '无',
        'unique': False,
        'batchManagement': False,
        'itemBrandId': None,
        'shelfLife': '0',
        'warningDays': '0',
        'productionDate': None,
        'minusStock': False,
        'taxCode': None,
        'taxDiscountDesc': None,
        'length': 0.0,
        'width': 0.0,
        'height': 0.0,
        'boxSize': 0.0,
        'itemBrandName': None,
        'createDate': 1699239979000,
        'defaultWarehouseId': 611885326909,
        'defaultWarehouseName': '时空仓',
        'taxDiscount': 0,
        'lowestSalesPrice': '0.0',
        'opicUrl': None,
        'saleUnitId': None,
        'purchaseUnitId': None,
        'saleUnitName': None,
        'purchaseUnitName': None,
        'bestSellingPeriodStart': None,
        'bestSellingPeriodEnd': None,
        'approachingPeriodStart': None,
        'approachingPeriodEnd': None,
        'shipperCode': '0',
        'shipperName': None,
        'vipAntiTheft': False,
        'packageMaterial': False,
        'virtual': False
    }]
    # table_name
    now = datetime.now()
    formatted_now = now.strftime('%Y%m%d')
    table_name = formatted_now + '_rx_drug'
    # 创建 dao 层的对象
    table_dao = MyBatisPlusUtils(
        connection=conn,
        table_name=table_name
    )
    flag = table_dao.batch_insert(
        data
    )
    # 关闭数据库
    DatabaseUtils.close_connection(conn)
    pass
