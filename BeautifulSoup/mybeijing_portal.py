#coding=utf-8
import re
import urllib.request
from collections import deque
from bs4 import BeautifulSoup

def test():
    queue = deque()
    visited = set()
    baseUrl = "http://219.237.93.162"
    url = baseUrl
    queue.append(url)
    cnt = 0
    resultList = []
    while queue:
        url = queue.popleft()
        visited |= {url}
        print("已经抓取: " + str(cnt) + "   正在抓取: " + url)

        try:
            urlop = urllib.request.urlopen(url, timeout=10)
            if 'html' not in urlop.getheader('Content-Type'):
                continue
            try:
                cnt += 1
                data = urlop.read().decode("utf-8")
            except:
                print("读写失败: " + url)
                continue
            soup = BeautifulSoup(data, "lxml")
            hrefTag = soup.find_all("a", attrs={"href":re.compile('^/.*/')})
            for x in hrefTag:
                nextUrl = x.attrs["href"]
                print("nextUrl = " + nextUrl)
                tempUrl = baseUrl + nextUrl
                print("tempUrl = " + tempUrl)
                if tempUrl not in visited:
                    queue.append(tempUrl)
                    tempDict = {}
                    tempDict["sourceUrl"] = url
                    tempDict["click"] = x.text
                    tempDict["nextUrl"] = tempUrl
                    resultList.append(tempDict)
                    print("加入队列 ---> " + tempUrl)
                print("--------------")
        except:
            print("访问失败: " + url)
            continue
    print("finish")

if __name__ == "__main__":
    test()