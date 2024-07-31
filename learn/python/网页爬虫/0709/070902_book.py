import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.51"
}

# response = requests.get("https://movie.douban.com/top250")
response = requests.get("https://books.toscrape.com/", headers=headers)
print(response.status_code)

content = response.text
# print(content)
soup = BeautifulSoup(content, "html.parser")
# print(soup)

all_price = soup.find_all("p", attrs={"class": "price_color"})
# print(all_movies)
for price in all_price:
    print(price.string[2:])

all_title = soup.find_all("h3")
for title in all_title:
    print(title.string)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
