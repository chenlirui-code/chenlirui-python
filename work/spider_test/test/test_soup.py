from bs4 import BeautifulSoup

html = """
<html>
<body>
    <a href="https://example.com" target="_blank" class="mnav c-font-normal c-color-t">Example 1</a>
    <a href="https://example2.com" class="mnav c-font-normal c-color-t">Example 2</a>
    <a href="https://example3.com" target="_blank" class="nav c-font-normal c-color-t">Example 3</a>
</body>
</html>
"""

soup = BeautifulSoup(html, 'html.parser')

# 找到所有满足条件的 a 标签
a_tags = soup.find_all('a', attrs={'target': '_blank', 'class': 'mnav c-font-normal c-color-t'})

for a_tag in a_tags:
    print(a_tag)