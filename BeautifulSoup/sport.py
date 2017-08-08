#coding=utf-8
from bs4 import BeautifulSoup
import requests

url = "http://sports.qq.com/"
r = requests.get(url)
soup = BeautifulSoup(r.text, "lxml")
newsTag = soup.select("div .scr-newsarea")
imgs = soup.select("img[src^='http://mat1.gtimg.com']")
print("图片url")
for img in imgs:
    print(img.attrs["src"])
print("--------------------")
news = []
for tag in newsTag:
    for temp in tag.select("a[href^='http://sports.qq.com']"):
        new = {}
        new["title"] = temp.get_text()
        new["url"] = temp.attrs["href"]
        news.append(new)

for new in news:
    print(new["title"])
    print(new["url"])
    print("---------------")