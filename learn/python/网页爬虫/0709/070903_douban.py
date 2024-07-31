import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.51"
}

# response = requests.get("https://movie.douban.com/top250")

for start_num in range(0, 251, 25):
    # print(start_num)
    response = requests.get(f"https://movie.douban.com/top250?start={start_num}", headers=headers)
    # print(" 状态码： " + response.status_code)

    html = response.text
    soup = BeautifulSoup(html, "html.parser")

    all_title = soup.find_all("span", attrs="title")
    # print(all_title)
    for title in all_title:
        if "/" not in title.text:
            print(title.text)




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
