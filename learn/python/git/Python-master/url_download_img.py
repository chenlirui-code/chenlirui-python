import requests
import time

from bs4 import BeautifulSoup
from utils.img_util import ImgUtils

if __name__ == "__main__":
    local = time.strftime("%Y.%m.%d")
    url = 'https://pic.netbian.com/4kdongman/index_2.html'
    con = requests.get(url)

    # 原始编码为 ISO-8859-1，先将其解码为字节流
    content_bytes = con.content
    # 再将字节流解码为 utf-8 字符串
    content_utf8_str = content_bytes.decode('ISO-8859-1')

    # 先将获取到的内容解析为 BeautifulSoup 对象
    soup = BeautifulSoup(content_utf8_str, 'html.parser')
    # 提取所有 src 属性值包含.jpg 的 <img> 标签
    img_tags = soup.find_all('img', src=lambda x: '.jpg' in x)
    # 存储 src 值的列表
    src_list = [img['src'] for img in img_tags]
    # print("Total image count:", len(src_list))
    save_path = r"E:\Code\python\base\learn\python\git\Python-master\files\img"
    cnt = 1
    for src in src_list:
        # https://pic.netbian.com/uploads/allimg/240425/163038-1714033838bbaa.jpg
        url = "https://pic.netbian.com/" + src
        ImgUtils.download_image(url, save_path, cnt)
        cnt += 1
