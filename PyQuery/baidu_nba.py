import requests
import pyquery

url = "https://tieba.baidu.com/f?kw=nba&ie=utf-8"
r = requests.get(url)
pq = pyquery.PyQuery(url)
titles = pq("a").filter(".j_th_tit")
for title in titles.items():
    print("title: " + title.text())