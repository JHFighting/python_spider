from bs4 import BeautifulSoup
import re

a = """<p class='a b' xixi='123'>haha</p>
<p id="dd" class='a'>heihei</p>
<div class='a'><p class='c'>ccc</p>aaa</div>
<div class='a b'>xixi</div>"""
soup = BeautifulSoup(a, "lxml")

print(" ------ find_all ------")
a = soup.find_all("div")
print(a)

b = soup.find_all("div", "a")
print(b)

c = soup.find_all("div", class_="a b")
print(c)

d = soup.find_all(id="dd")
print(d)

e = soup.find_all(attrs={"xixi":"123"})
print(e)

f = soup.find_all(attrs={"class":re.compile("a")})
print(f)

print(" ------ select ------")
a = soup.select("div")	# 所有div标签
print(a)

b = soup.select("div.a") # 所有div中class有"a"的标签
print(b)

c = soup.select("div .a")	# div标签内class为"a"的子标签
print(c)

d = soup.select("div[class='a b']") # div class='a b'
print(d)