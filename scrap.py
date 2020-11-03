import requests
from bs4 import BeautifulSoup

# page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
page = requests.get("http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html")

code = page.status_code

soup = BeautifulSoup(page.content, 'html.parser')

# print(soup.prettify())
# [type(item) for item in list(soup.children)]
# html = list(soup.children)[2]
# # print(list(html.children))

# body = list(html.children)[3]

# p = list(body.children)[1]
# print(p.get_text())

# p = soup.find_all('p')[0].get_text()
print(soup.prettify())