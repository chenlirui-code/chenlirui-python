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

from util.text_util import convert_unicode_to_text
from work.tianmao.publish.util.database_manager_util import DatabaseManager


class QianNiu:

    @staticmethod
    def search_product_by_brand_and_name(
            conn,
            id,
            brand,
            product_name,
            specifications,
            company,
            resp_json_table_name
    ):
        '''根据品牌和产品名称搜索产品库'''
        # 创建一个会话对象
        request = requests.session()

        # 设置初始的Cookie
        cookies = [
            {'name': 't', 'value': '71b08b05a7289634ac609055eef5f692', 'domain': '.taobao.com', 'path': '/',
                    'secure': True, 'httpOnly': False, 'expirationDate': '2024/10/21 14:24:40'},
                   {'name': 'xlly_s', 'value': '1', 'domain': '.taobao.com', 'path': '/', 'secure': True,
                    'httpOnly': False, 'expirationDate': '2024/7/25 06:06:25'},
                   {'name': '_tb_token_', 'value': 'taUhgdImh5lqfJQC5ZVp', 'domain': '.taobao.com', 'path': '/',
                    'secure': True, 'httpOnly': False, 'expirationDate': None},
                   {'name': '_samesite_flag_', 'value': 'true', 'domain': '.taobao.com', 'path': '/', 'secure': True,
                    'httpOnly': True, 'expirationDate': None},
                   {'name': '3PcFlag', 'value': '1721715873389', 'domain': '.taobao.com', 'path': '/', 'secure': True,
                    'httpOnly': False, 'expirationDate': '2024/8/2 14:24:31'},
                   {'name': 'cookie2', 'value': '1298a3ce5d391fca4b289c0cb7ba1416', 'domain': '.taobao.com',
                    'path': '/', 'secure': True, 'httpOnly': True, 'expirationDate': None}, {'name': 'sgcookie',
                                                                                             'value': 'E100Fb3J06yR%2Bz7QoARIW3OwATfEk0hIm02uc%2BqFUXW%2Bj%2BlhiYbE2Gm7ATuGFPpzmUKrEWkMdVx98Aeon1uMPCfqNt%2Bjda7P%2BN2L%2BWY%2BaJQuX%2B%2F97Gv2%2Bb3iU6oCDPt32R3T',
                                                                                             'domain': '.taobao.com',
                                                                                             'path': '/',
                                                                                             'secure': True,
                                                                                             'httpOnly': True,
                                                                                             'expirationDate': '2025/7/23 14:24:40'},
                   {'name': 'unb', 'value': '2218267619830', 'domain': '.taobao.com', 'path': '/', 'secure': True,
                    'httpOnly': True, 'expirationDate': None}, {'name': 'sn',
                                                                'value': '%E5%A5%BD%E9%9C%80%E8%8D%AF%E5%A4%A7%E8%8D%AF%E6%88%BF%E6%97%97%E8%88%B0%E5%BA%97%3A%E6%B1%9F%E7%AF%B1',
                                                                'domain': '.taobao.com', 'path': '/', 'secure': True,
                                                                'httpOnly': False, 'expirationDate': None},
                   {'name': 'uc1', 'value': 'cookie21=Vq8l%2BKCLiw%3D%3D&cookie14=UoYcAjaH2i7NNw%3D%3D',
                    'domain': '.taobao.com', 'path': '/', 'secure': True, 'httpOnly': False, 'expirationDate': None},
                   {'name': 'csg', 'value': '8453f9ea', 'domain': '.taobao.com', 'path': '/', 'secure': True,
                    'httpOnly': False, 'expirationDate': None},
                   {'name': '_cc_', 'value': 'UIHiLt3xSw%3D%3D', 'domain': '.taobao.com', 'path': '/', 'secure': True,
                    'httpOnly': False, 'expirationDate': '2025/7/23 14:24:40'},
                   {'name': 'cancelledSubSites', 'value': 'empty', 'domain': '.taobao.com', 'path': '/', 'secure': True,
                    'httpOnly': False, 'expirationDate': None},
                   {'name': 'skt', 'value': 'ad43097c774572ae', 'domain': '.taobao.com', 'path': '/', 'secure': True,
                    'httpOnly': True, 'expirationDate': None},
                   {'name': '_mw_us_time_', 'value': '1721715883180', 'domain': 'myseller.taobao.com', 'path': '/',
                    'secure': True, 'httpOnly': True, 'expirationDate': '2024/7/23 07:24:40'},
                   {'name': 'cna', 'value': '+NsTH66fsGcCAduM6fpGjjRt', 'domain': '.taobao.com', 'path': '/',
                    'secure': True, 'httpOnly': False, 'expirationDate': '2025/8/27 06:24:42'},
                   {'name': '_m_h5_tk', 'value': 'e342ed8872b58c984c3e1cc025d7687a_1721723445111',
                    'domain': '.taobao.com', 'path': '/', 'secure': True, 'httpOnly': False,
                    'expirationDate': '2024/7/23 07:54:42'},
                   {'name': '_m_h5_tk_enc', 'value': '27e3677a6cc880203d0c85501e496014', 'domain': '.taobao.com',
                    'path': '/', 'secure': True, 'httpOnly': False, 'expirationDate': '2024/7/23 07:54:42'},
                   {'name': 'tfstk',
                    'value': 'fotr3o2O4MAfgDThgssF_VhuNqsRoGh_rH1CKpvhF_fkFz13YIdDP99hOMReTB55-bIWYIRJMaTWKH6HYsYFR7s5RX7e1ItWOHIWYk5cqwL5O_1FYpdZhfisfLpRvgcs1c_oShoNv6mCxdi_fBIn1fibl-b-NMYIgBdcgZfAL9VlZBf0o9CcE7bHtsbcIONlxMAHnxWFIzf3ra2cn9WwP7Ql-WBGrAc6GYFUP97PsKuTxk-Lfa5MUsrnsnWz91vlgkqFwjYsDpAnTksMWI-FSCiUDg9woiXyuv4cZN8kNtdEbufk0LxlN3cbV_xJnFtBivqhTEYG5FvoGrW2oLtVlhcaYaLDwFQeAjiOVF96vNxo45CfW9RNqEl04CjzZWBm-nKpzW4FrtBV1xkDmo9KBPcQkkULJZAO31MR7yUdrNXV1xk4JyQ84t5seN5..',
                    'domain': '.taobao.com', 'path': '/', 'secure': False, 'httpOnly': False,
                    'expirationDate': '2025/1/19 06:24:42'},
                   {'name': 'isg', 'value': 'BMjIhoXeOnTyblXYOUbkRevFmTDacSx7ZThrd4J5GsM2XWjHKoXcCAAf0TUt7eRT',
                    'domain': '.taobao.com', 'path': '/', 'secure': True, 'httpOnly': False,
                    'expirationDate': '2025/1/19 06:24:42'}
        ]
        # 遍历设置每个Cookie
        for x in cookies:
            request.cookies.set(name=x['name'], value=x['value'])

        headers = {
            '$csrftoken.headername': '$csrfToken.token',
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'bx-v': '2.5.13',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://spu.taobao.com',
            'priority': 'u=1, i',
            'referer': 'https://spu.taobao.com/manager/render.htm?parentTab=spu-all&hasWrapper=1',
            'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Microsoft Edge";v="126"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0',
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
                "title": f"{brand} {product_name}",
                "cat0": {"value": 122966004, "text": "处方药"}
            },
            "pagination": {"current": 1, "pageSize": 100},
            "parentTab": "spu-all", "childTab": ""
        }

        data = {
            'jsonBody': json.dumps(jsonBody),
        }

        try:
            response = request.post(
                'https://spu.taobao.com/manager/ajax/getModels.htm',
                params=params,
                headers=headers,
                data=data
            )
            # print("Response Text:", response.text)
            # raise 1
            resp_json = response.json()
            # 打印 resp_json 的内容，确保它包含了预期的键和值
            # print("resp_json:", resp_json)

            # 检查响应中是否包含成功标志
            if not resp_json['success']:
                raise ValueError('搜索天猫产品库数据错误')
            else:
                # 将 JSON 数据转换为文本
                resp_text = json.dumps(resp_json)
                resp_json = convert_unicode_to_text(resp_text)
                # print(resp_json)
                # 存到数据库中
                data_to_insert = [
                    {
                        'id': id,
                        'brand': brand,
                        'product_name': product_name,
                        'specifications': specifications,
                        'company': company,
                        'resp_json': resp_json,
                    },
                ]
                code = DatabaseManager.batch_write_data(
                    conn, data_to_insert, resp_json_table_name
                )
                if code == 200:
                    print("写入 resp_json成功")
                else:
                    print("写入 resp_json失败")

        except requests.exceptions.RequestException as e:
            print(f"请求发生异常: {e}")
        except json.JSONDecodeError as jde:
            print(f"JSON 解析异常: {jde}")


def resp_json_next(
        resp_json,
        conn,
        id,
        brand,
        product_name,
        specifications,
        company,
        resp_json_table_name,
        url_table_name
):
    """ 根据 resp_json 进行之后的处理 """
    delete_value = 0
    flag = False
    # 检查 'success' 键是否存在，并且其值为 True
    if 'success' in resp_json and resp_json['success']:
        # 安全获取 dataSource
        dataSource = resp_json.get('data', {}).get('table', {}).get('dataSource', [])
        # print("dataSource:", dataSource)  # 打印 dataSource 的值，用于调试
        # print(len(dataSource))
        # 如果 dataSource 判断是否有有效数据
        if isinstance(dataSource, list) and len(dataSource) == 0:
            delete_value = 7
            flag = True
            # print("未找到有效的 dataSource 数据")
        elif isinstance(dataSource, dict) and len(dataSource) == 0:
            delete_value = 7
            flag = True
            # print("未找到有效的 dataSource 数据")
        elif dataSource is not None:
            # print("成功获取到 dataSource:", dataSource)
            spec_url_dict = {}
            spuId = None
            for data in dataSource:
                status = data.get('status', {})
                if status == '小二确认':
                    target_text = '发布商品'
                    for item in data.get('operation', []):
                        if item.get('text') == target_text:
                            url = item.get('url')
                            keyProps = data.get('keyProps', {})
                            # print(keyProps)
                            old_specifications = None
                            for key in keyProps:
                                if '规格' in key:
                                    colon_index = key.find(':')  # 找到 ':' 的索引位置
                                    if colon_index != -1:  # 如果找到了 ':'
                                        old_specifications = key[colon_index + 1:]  # 获取 ':' 后面的内容
                                        # print(old_specifications)
                            spuId = data.get('spuId', {})
                            # 字典存储
                            spec_url_dict[old_specifications] = url
                else:
                    print("status 屏蔽'")
            if spec_url_dict:  # 检查字典是否为空
                # print("字典是存在")
                old_specifications_key_set = set(spec_url_dict.keys())
                print(specifications)
                bool = False
                old_specifications_temp = None
                for old_specifications in old_specifications_key_set:
                    print(old_specifications)

                    # AI 处理
                    content = (
                            " 旧的规格为 " + old_specifications +
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
                        msg = get_ai_response(content)
                        print(msg)
                        if "YES" in msg:
                            old_specifications_temp = old_specifications
                            bool = True
                            break
                        elif old_specifications in specifications:
                            old_specifications_temp = old_specifications
                            bool = True
                            break
                        elif specifications in old_specifications:
                            old_specifications_temp = old_specifications
                            bool = True
                            break
                    except TimeoutError:
                        print("执行AI超时，跳过")
                        delete_value = 9
                        flag = True
                    finally:
                        timer.cancel()  # 取消定时器

                if bool:
                    try:
                        url = spec_url_dict[old_specifications_temp]
                        data_to_insert = [
                            {
                                'id': id,
                                'spuId': spuId,
                                'url': url,
                                'product_name': product_name,
                                'brand': brand,
                                'specifications': old_specifications_temp,
                                'company': company,
                            },
                        ]
                        # 写数据
                        code = DatabaseManager.batch_write_data(
                            conn, data_to_insert, url_table_name
                        )
                        # print(code)
                        # 成功 就删除 excel_data  为 1  否则 插入url_table_name数据异常 为 3
                        if code == 200:
                            # print(" 写入url_table_name成功 ")
                            delete_value = 1
                            flag = True
                        else:
                            # print("  插入url_table_name数据异常 ")
                            delete_value = 3
                            flag = True
                    except KeyError as e:
                        # print(f"捕获到异常: 键 '{specifications}' 不存在于字典中。异常信息: {e}")
                        delete_value = 4
                        flag = True
                else:
                    # print(" 规格不符 ")
                    delete_value = 5
                    flag = True
            else:
                # print("字典为空")
                delete_value = 6
                flag = True
        else:
            # print("未找到有效的 dataSource 数据")
            delete_value = 7
            flag = True
        if flag:
            # 捕获到异常 删除为 4
            # 为 5 规格不符，为 6 字典为空，为 7 未找到有效的 dataSource 数据
            code = DatabaseManager.update_is_delete_by_id(
                conn,
                resp_json_table_name,
                id,
                delete_value
            )

    else:
        print("请求未成功或没有有效数据")
