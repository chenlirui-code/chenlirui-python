#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    : test_get.py
@Author  : ChenLiRui
@Time    : 2024/8/1 下午3:44
@explain : 文件说明
"""
import json
import requests

request = requests.session()

headers = {
    '$csrftoken.headername': '$csrfToken.token',
    # 'Authority': 'spu.taobao.com',
    # 'method': 'POST',
    # 'path': '/manager/ajax/getModels.htm?ac=table&ac=pagination',
    # 'scheme': 'https',
    'accept': 'application/json, text/plain, */*',
    'accept-encoding': 'gzip, deflate, br, zstd',
    'accept-language': 'zh-CN,zh;q=0.9',
    'bx-v': '2.5.14',
    'cache-control': 'no-cache',
    'content-length': '163',
    'content-type': 'application/x-www-form-urlencoded',

    'cookie': 'cq=ccp%3D1; t=2be392428829996b173668cd2b0d5809; thw=cn; cookie2=1e91714287b3ce70e5992ab606bee804; _tb_token_=58e33b633e371; _samesite_flag_=true; 3PcFlag=1722497330365; xlly_s=1; sgcookie=E1007ZO5BY3sSw2OeZrQtaNYo6mxmRVA3nerq2u4PW3P5tXtrxRDLlDXTnojDlHKEl8KTnEOhcZzQ8MG3EOTex2F9TXouvaN%2FjHAgQ6LXmkqfdiesVq%2BZf7xriXU5t4viLGf; unb=2218267619830; sn=%E5%A5%BD%E9%9C%80%E8%8D%AF%E5%A4%A7%E8%8D%AF%E6%88%BF%E6%97%97%E8%88%B0%E5%BA%97%3A%E6%B1%9F%E7%AF%B1; uc1=cookie14=UoYcAf2iLxXluA%3D%3D&cookie21=WqG3DMC9EA%3D%3D; csg=0365392c; _cc_=UtASsssmfA%3D%3D; cancelledSubSites=empty; skt=88f3ac28e577bfe6; cna=axwuH43OElkCAduM66zdC3ql; _bl_uid=gklvkzURa88ywmgRap9R2z93347p; tfstk=fVTsITYmMR2_6BACnGhFAKNy7wQjadgyXS1vZIUaMNQOHIdPLrlG7mbXh99cQG79_ZtX3LxNgNI4ln9kFsSvut8bse97uPkijIUfuZHrU4uyslbckYkUvCI0Is10DqSA6yKZsu8IU4uy6cCGuBHrip3LGt1Ak1IAD9hCGs2OkPQxO9CfZoe9HZhB99fbB-BOH9Eds1ExTWDCtc691XUd2nCz_pdOdzOHJ1elH4X_kHT1_GTv_9GETe11fTIEz5MyWpRv7Fjnqu7DT39XDp3Q5KO92KBwJYUf33fXM__-r76p5ITCjHyTX__1CgLOv7zWsiKBRN8tnuAeOOI58HonQi76C3XlXDDHhB6wHFsLCvW24B8OALHURKjXXd1dygzYzTNsSoNCqr1CUXGQmo5cmq2BCEPFLGChTUlIORZcX6fBaXGQmtsOt6qxOXZo5; isg=BPn5lhxuu0N-wmfbpbXjf5BoCGXTBu24_Navhxss9yCRoh00YlYRiJg0JKZUGoXw',

    'origin': 'https://spu.taobao.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://spu.taobao.com/manager/render.htm?parentTab=spu-all&hasWrapper=1',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': "Windows",
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}
params = {
    'ac': [
        'table',
        'pagination',
    ],
}
jsonBody = {
    "filter": {
        "status": {"text": "小二确认", "value": 3},
        "title": "开思亭 依巴斯汀片",
        "cat0": {"value": 122966004, "text": "处方药"}
    },
    "pagination": {"current": 1, "pageSize": 100},
    "parentTab": "spu-all", "childTab": ""
}

data = {
    'jsonBody': json.dumps(jsonBody),
}

response = request.post(
    'https://spu.taobao.com/manager/ajax/getModels.htm',
    params=params,
    headers=headers,
    data=data
)
print("Status Code:", response.status_code)
print("Response Text:", response.text)
raise 1
