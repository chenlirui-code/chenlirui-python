#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    : test_job_details.py
@Author  : ChenLiRui
@Time    : 2024/8/2 上午11:55
@explain : 文件说明
"""
import requests
from bs4 import BeautifulSoup
import json
import xlwt
import time
import random

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
}


# 获取指定城市的编码
def get_city_code(city_name):
    response = requests.get("https://www.zhipin.com/wapi/zpCommon/data/city.json")
    contents = json.loads(response.text)
    cities = contents["zpData"]["hotCityList"]
    city_code = contents["zpData"]["locationCity"]["code"]
    for city in cities:
        if city["name"] == city_name:
            city_code = city["code"]
    return city_code


def get_url(query="", city="", industry="", position="", page=1):
    base_url = "https://www.zhipin.com/wapi/zpgeek/search/joblist.json"
    data = {
        'scene': 1,
        'query': query,
        'city': city,
        'experience': '',
        'payType': '',
        'partTime': '',
        'degree': '',
        'industry': industry,
        'scale': '',
        'stage': '',
        'position': position,
        'jobType': '',
        'salary': '',
        'multiBusinessDistrict': '',
        'multiSubway': '',
        'page': page,
        'pageSize': 30,
    }
    urls = []
    url = base_url.format(query, city, industry, position, page)
    response = requests.get(
        url,
        headers=headers,
        data=data,
    )
    print(response.status_code)
    response_text = response.text
    # print(response_text)
    soup = BeautifulSoup(response_text, "lxml")
    print(soup)
    page_list = soup.find("div", "page").find_all("a")
    urls.append(url)
    print(urls)
    # while page_list[len(page_list) - 1]["href"] != "javascript:;":
    #     page += 1
    #     url = base_url.format(query, city, industry, position, page)
    #     urls.append(url)
    #     response = requests.get(url, headers=headers)
    #     soup = BeautifulSoup(response.text, "lxml")
    #     page_list = soup.find("div", "page").find_all("a")
    return urls


def get_html(url):
    response = requests.get(url, headers=headers)
    return response.text


def job_info(job_name, company, industry, finance, staff_number, salary, site, work_experience, education_bak,
             job_desc):
    return {
        "job_name": job_name,
        "company": company,
        "industry": industry,
        "finance": finance,
        "staff_number": staff_number,
        "salary": salary,
        "site": site,
        "work_experience": work_experience,
        "education_bak": education_bak,
        "job_desc": job_desc
    }


def get_job_desc(jid, lid):
    url = "https://www.zhipin.com/wapi/zpgeek/view/job/card.json?jid={}&lid={}"
    response = requests.get(url.format(jid, lid), headers=headers)
    html = json.loads(response.text)["zpData"]["html"]
    soup = BeautifulSoup(html, "lxml")
    desc = soup.find("div", "detail-bottom-text").get_text()
    return desc


def get_content(html):
    bs = BeautifulSoup(html, 'lxml')
    contents = []
    for info in bs.find_all("div", "job-primary"):
        job_name = info.find("div", "job-title").get_text()
        company = info.find("div", "company-text").a.get_text()
        jid = info.find("div", "info-primary").a["data-jid"]
        lid = info.find("div", "info-primary").a["data-lid"]
        desc = get_job_desc(jid, lid)
        texts = [text for text in info.find("div", "info-primary").p.stripped_strings]
        site = texts[0]
        work_exp = texts[1]
        edu_bak = texts[2]
        salary = info.span.get_text()
        companies = [text for text in info.find("div", "company-text").p.stripped_strings]
        industry = companies[0]
        if len(companies) > 2:
            finance = companies[1]
            staff_num = companies[2]
        else:
            finance = None
            staff_num = companies[1]
        contents.append(
            job_info(job_name, company, industry, finance, staff_num, salary, site, work_exp, edu_bak, desc))
        time.sleep(1)
    return contents


def save_data(content, city, query):
    file = xlwt.Workbook(encoding="utf-8", style_compression=0)
    sheet = file.add_sheet("job_info", cell_overwrite_ok=True)
    sheet.write(0, 0, "职位名称")
    sheet.write(0, 1, "公司名称")
    sheet.write(0, 2, "行业")
    sheet.write(0, 3, "融资情况")
    sheet.write(0, 4, "公司人数")
    sheet.write(0, 5, "薪资")
    sheet.write(0, 6, "工作地点")
    sheet.write(0, 7, "工作经验")
    sheet.write(0, 8, "学历要求")
    sheet.write(0, 9, "职位描述")
    for i in range(len(content)):
        sheet.write(i + 1, 0, content[i]["job_name"])
        sheet.write(i + 1, 1, content[i]["company"])
        sheet.write(i + 1, 2, content[i]["industry"])
        sheet.write(i + 1, 3, content[i]["finance"])
        sheet.write(i + 1, 4, content[i]["staff_number"])
        sheet.write(i + 1, 5, content[i]["salary"])
        sheet.write(i + 1, 6, content[i]["site"])
        sheet.write(i + 1, 7, content[i]["work_experience"])
        sheet.write(i + 1, 8, content[i]["education_bak"])
        sheet.write(i + 1, 9, content[i]["job_desc"])
    file.save(r'c:\projects\{}_{}.xls'.format(city, query))


def main():
    city_name = "深圳"
    city = get_city_code(city_name)
    query = "python"
    urls = get_url(query=query, city=city)
    contents = []
    for url in urls:
        html = get_html(url)
        content = get_content(html)
        contents += content
        time.sleep(5)
    save_data(contents, city_name, query)


if __name__ == '__main__':
    main()
