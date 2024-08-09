#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    : main_rx_drug.py
@Author  : ChenLiRui
@Time    : 2024/8/8 下午2:34
@explain : 处方药
"""
import json

from utils.database.DatabaseUtils import DatabaseUtils
from utils.mybatis.MyBatisPlusUtils import MyBatisPlusUtils
from work.guanyierp.web.web_rx_drug import request_post
from utils.log.my_logger import logger
from datetime import datetime

host = 'localhost'
user = 'root'
password = '1202'
database = 'guanyierp'
# url地址
url = 'https://v2.guanyierp.com/ic/item/data/list'
# cookie
headers = {
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "zh-CN,zh;q=0.9",
    "bx-v": "2.5.11",
    "cache-control": "no-cache",
    "connection": "keep-alive",
    "content-length": "285",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "host": "v2.guanyierp.com",
    "origin": "https://v2.guanyierp.com",
    "pragma": "no-cache",
    "referer": "https://v2.guanyierp.com/ic/item",
    "sec-ch-ua": '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "Windows",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
    "x-requested-with": "XMLHttpRequest",
    "cookie": "loginAppkey=21226717; _ati=7991460485374; userId=762599784623; pin=c326292bd0cc81e03fdf0d76dfc9cb16; gyTenant=13487759595; device_id=H43DMHGEOXDQHSBOO2SBPAQ4T4BV7RRTUVQXS2WUOATTNQU64FAA4GTLZZ4XA4EQSQVLI222XYDG43AUZ64KVZOQXQ; route=c3f21301cc80a84c3f63260a9cf3a701; acw_tc=2760827b17231602889938830eb65bfe6963e348bb0505d38e854b927c4255; shiroCookie=67bc4e8e-8c3d-4ee3-8d0b-49673d12dd12; secToken=iXLU7GMba0rB0nnAJ1zicKVOc%2FJBaBbqhGpDI%2Bw3H8UBQetIpi1WGYnAIsxgpuwfCPx%2BB8sEvuYEh17KRLSOGsf4wGBEYXyDYR0pRp9OJ%2Fp9c%2BeTvgrnxQI1SrKJHQeTFnYFdfJ2m1vIRDNZ5R1brQ%3D%3D; 3AB9D23F7A4B3C9B=H43DMHGEOXDQHSBOO2SBPAQ4T4BV7RRTUVQXS2WUOATTNQU64FAA4GTLZZ4XA4EQSQVLI222XYDG43AUZ64KVZOQXQ; cid=1723160316424_f82afff60a2558377f3396f940eb7b17; tfstk=feOZifAJGfhaj_9cYM1V8Sq9905Og_nS0IsfoEYc5GjGltvU0UtVhP9sWtYcYnI1C1v10H-6rd66gEFVoExxWigtdFLOMsmSV4GWWFIZzjkk_GV3teQzjNcee5B1MsmSA_c7S9fvVJq9mc8n8Z_foSxcoXbhzMV0snjGKkbPysjDms0FxZ_NSl2gsXfhrjGPmgNFzO0ytU1-x-FcBgYGjFT6tXBYBejFoZdd7FIkSKF0iB7NQINH6jh5CKYReCTsgWC6zpfh7ncoj6YkLU6w_0P1DtRebK-sl-Qe3EAR6_zmse5NbTANBrFyqe8DF9RIrbCNsGvf6EarfeRwfFdelr2h_19FUC5owljXdURVuInxT38MEnvV41rA-FJkMdr0nObd8ggE-XcKVzXPFS-bH-B9pwSSWVeYHOjF8ggES-eABZbFV29O."
}
# 跟 rows 500  _dc  1723160418591
params = {
    '_dc': '1723160418591'
}
# 数据总数量
total = 1
# 开始页数 1
page = 1
# 开始的位置  0
start = 0
# 每页的数量 500
rows = 500
# "page": 1,  "start": 0,  "rows": 500
data = {
    "startDate": "",
    "endDate": "",
    "shipperCodes": "",
    "likeCode": "",
    "separatorLikeCode": "",
    "skuCode": "",
    "separatorSkuCode": "",
    "skuName": "",
    "name": "",
    "sName": "",
    "supplierId": "",
    "itemBrandId": "",
    "tagIdsString": "",
    "defaultWarehouseId": "",
    "unique": "",
    "batchManagement": "",
    "disable": False,
    "minusStock": "",
    "packageMaterial": "",
    "categoryId": 58183585003,
    "page": page,
    "start": start,
    "rows": rows
}
# table_name
table_name = datetime.now().strftime('%Y%m%d') + '_rx_drug'


def main_create_table(url, headers, params, data, conn, table_name):
    # 建表 请求 并转换数据 获取一条数据  建表
    table_data = json.loads(request_post(url, headers, params, data).text)['rows'][0]
    DatabaseUtils.create_table_from_dict(conn, table_name, table_data)


def main_batch_insert_data(start, total, page, url, headers, params, data):
    while start < total:
        data['page'] = page
        data['start'] = start
        # 请求 并转换数据
        response = request_post(url, headers, params, data)
        if response:
            response_dict = json.loads(response.text)
            total = int(response_dict['total'])
            # 具体的数据  写数据
            rows_data = response_dict['rows']
            table_dao.batch_insert(rows_data)
        # 每一次都要修改的请求参数
        page = page + 1
        start = start + rows


if __name__ == '__main__':
    # 连接数据库
    conn = DatabaseUtils.create_connection(host, user, password, database)
    # 创建 dao 层的对象
    table_dao = MyBatisPlusUtils(
        connection=conn,
        table_name=table_name
    )
    # 建表 请求 并转换数据 获取一条数据  建表
    main_create_table(url, headers, params, data, conn, table_name)
    # 循环拿数据  写数据
    main_batch_insert_data(start, total, page, url, headers, params, data)
    # 拿数据
    # 处理字段
    # 写数据
    # 搜索网站 存返回
    # 拿返回 写规格对比 ai处理 写正确数据
    # 关闭数据库
    DatabaseUtils.close_connection(conn)
    pass
