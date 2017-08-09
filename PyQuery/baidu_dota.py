import requests
import pyquery

url = "https://tieba.baidu.com/f?ie=utf-8&kw=dota&fr=search"
r = requests.get(url)
with open("baidu.html", "w", encoding="utf-8") as f:
    f.write(r.text)