#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project :python
@File    :qianniu_util.py
@IDE     :PyCharm
@Author  :Chen LiRui
@Date    :2024/7/16 上午11:22
@explain : 天猫上新搜索接口
"""
import json
import requests
import threading

from utils.ai_util import AiUtils
from utils.text_util import TextUtils
from utils.logging_util import logger


def requests_util(request, brand, product_name, headers):
    params = {
        'ac': [
            'table',
            'pagination',
        ],
    }
    jsonBody = {
        "filter": {
            "status": {"text": "小二确认", "value": 3},
            "title": f"{brand} {product_name}",
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
    # logger.info("Response Text:", response.text)
    # raise 1
    resp_json = response.json()
    if not resp_json['success']:
        raise ValueError('搜索天猫产品库数据错误')
    else:
        # logger.info(resp_json)
        temp_data_source = TextUtils.decode_unicode_to_text(process_data_source(resp_json))
        # logger.info(temp_data_source)
        # raise 1
        return temp_data_source


def process_data_source(resp_json):
    """ 删除掉不是 小二确认 的数据 只拿 dataSource 的数据 """
    try:
        if 'data' in resp_json and 'table' in resp_json['data'] and 'dataSource' in resp_json['data']['table']:
            data_source = resp_json['data']['table']['dataSource']
            # logger.info(data_source)
            new_data_source = []
            for data in data_source:
                if data['status'] == '小二确认':
                    new_data = {
                        'spuId': data['spuId'],
                        'keyProps': data['keyProps'],
                        'operation': data['operation']
                    }
                    new_data_source.append(new_data)
            return new_data_source
        else:
            return []
    except KeyError:
        logger.error("数据中缺少必要的属性")
        return []


def write_resp_json(
        id, product_id, price,
        sales,
        brand, product_name,
        specifications, company,
        data_source,
        excelDAO,
        resp_jsonDAO
):
    # 存到数据库中
    data_to_insert = {
        'id': id,
        'product_id': product_id,
        'price': price,
        'sales': sales,
        'brand': brand,
        'product_name': product_name,
        'specifications': specifications,
        'company': company,
        'resp_json': json.dumps(data_source),
    }

    flag = resp_jsonDAO.insert(data_to_insert)
    if flag:
        delete_value = 1
    else:
        delete_value = 3
    # 传入 api接口 过修改 删除为 1
    excelDAO.update_by_id(
        {
            'id': id,
            'is_delete': delete_value
        }
    )


class QianNiu:

    @staticmethod
    def search_product_by_brand_and_name(
            id,
            product,
            product_id,
            price,
            product_name,
            brand,
            sales,
            specifications,
            company,
            excelDAO,
            resp_jsonDAO
    ):
        '''根据品牌和产品名称搜索产品库'''
        # 创建一个会话对象
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

        data_source = []

        allowed_chars = ['Ⅰ', 'Ⅱ', 'Ⅲ', 'Ⅳ', 'Ⅴ', 'Ⅵ', 'Ⅶ', 'Ⅷ', 'Ⅸ', 'Ⅹ']
        if '/' not in brand and any(char in brand for char in allowed_chars):
            brand = ""
            data_source.extend(requests_util(request, brand, product_name, headers))
            # 上面拿到的dataSource数据不为空
            write_resp_json(
                id, product_id, price,
                sales,
                brand, product_name,
                specifications, company,
                data_source,
                excelDAO,
                resp_jsonDAO
            )
        else:
            brand_list = brand.split('/')
            for brand in brand_list:
                if brand not in allowed_chars:
                    # logger.info(brand)
                    data_source.extend(requests_util(request, brand, product_name, headers))
            # 上面拿到的dataSource数据不为空
            write_resp_json(
                id, product_id, price,
                sales,
                brand, product_name,
                specifications, company,
                data_source,
                excelDAO,
                resp_jsonDAO
            )


def resp_json_next(
        id,
        brand,
        product_name,
        resp_json,
        product_id,
        price,
        sales,
        specifications,
        company,
        resp_jsonDAO,
        urlDAO
):
    """ 根据 resp_json 进行之后的处理  dataSource """
    delete_value = 0
    flag = False
    # 如果 dataSource 判断是否有有效数据 安全获取 dataSource
    if resp_json is not None:
        # logger.info("成功获取到 dataSource:", resp_json)
        spec_url_dict = {}
        spuId = None
        for data in resp_json:
            for op in data['operation']:
                if op['text'] == '发布商品':
                    for item in data['keyProps']:
                        if item.startswith('药品规格:'):
                            http_url = op['url']
                            # logger.info(url)
                            spuId = data['spuId']
                            http_specifications = item.split('药品规格:')[1]
                            # logger.info(http_specifications)
                            # 字典存储
                            spec_url_dict[http_specifications] = http_url
                            break
        # 检查字典是否为空
        if spec_url_dict and len(spec_url_dict) > 0:
            # logger.info("字典是存在")
            http_specifications_set = set(spec_url_dict.keys())
            logger.info(specifications)
            bool = False
            http_specifications_temp = None
            for http_specifications in http_specifications_set:
                logger.info(http_specifications)
                # logger.info(type(http_specifications))
                if http_specifications is None:
                    logger.info("http_specifications 为 None")
                    delete_value = 8
                    flag = True
                else:
                    # AI 处理
                    content = (
                            " 旧的规格为 " + http_specifications +
                            ",  新的规格为 " + specifications +
                            ", 如果药品的净重量相同 ？"
                            " 如果相同返回YES"
                            ", 不相同返回NO"
                            ", 只返回YES和NO,不需要解释"
                    )
                    # AI响应时间处理
                    timer = threading.Timer(10, lambda: None)  # 设置 10 秒的定时器
                    timer.start()
                    try:
                        msg = AiUtils.get_ai_response(content)
                        logger.info(msg)
                        if "YES" in msg:
                            http_specifications_temp = http_specifications
                            bool = True
                            break
                        elif http_specifications in specifications:
                            http_specifications_temp = http_specifications
                            bool = True
                            break
                        elif specifications in http_specifications:
                            http_specifications_temp = http_specifications
                            bool = True
                            break
                    except TimeoutError:
                        logger.info("执行AI超时，跳过")
                        delete_value = 9
                        flag = True
                    finally:
                        timer.cancel()  # 取消定时器

            if bool:
                try:
                    url = spec_url_dict[http_specifications_temp]
                    data_to_insert = {
                        'id': id,
                        'spuId': spuId,
                        'url': url,
                        'product_name': product_name,
                        'brand': brand,
                        'product_id': product_id,
                        'price': price,
                        'sales': sales,
                        'specifications': http_specifications_temp,
                        'company': company,
                    }
                    # 写数据
                    code = urlDAO.insert(
                        data_to_insert
                    )
                    # logger.info(code)
                    # 成功 就删除 excel_data  为 1  否则 插入url_table_name数据异常 为 3
                    if code:
                        logger.info(" 写入url_table_name成功 ")
                        delete_value = 1
                        flag = True
                    else:
                        logger.info("  插入url_table_name数据异常 ")
                        delete_value = 3
                        flag = True
                except KeyError as e:
                    logger.info(f"捕获到异常: 键 '{specifications}' 不存在于字典中。异常信息: {e}")
                    delete_value = 4
                    flag = True
            else:
                logger.info(" 规格不符 ")
                delete_value = 5
                flag = True
        else:
            logger.info("字典为空")
            delete_value = 6
            flag = True
    else:
        logger.info("未找到有效的 dataSource 数据")
        delete_value = 7
        flag = True
    if flag:
        # 捕获到异常 删除为 4  为 5 规格不符，为 6 字典为空，为 7 未找到有效的 dataSource 数据
        code = resp_jsonDAO.update_by_id(
            {
                'id': id,
                'is_delete': delete_value
            }
        )
