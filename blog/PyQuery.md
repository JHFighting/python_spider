<a href="index.md" name="top"><<返回目录</a>

# PyQuery

### 1. 简介

如果说到 `jQuery`，熟悉前端的同学肯定不陌生，它可以简单优雅地对 html 文件进行定位、选择、移动等操作。而本文的主角 `pyquery`，支持以 `jquery` 的方式对 html 进行操作。因此非常适合有前端或 js 基础的同学使用。

### 2. 安装

```sh
pip install pyquery
```

`pyquery`解析依赖`lxml`，因此也需要安装`lxml`。

### 3. 入门

##### 初始化

介绍以下三种初始化方式：

（1）字符串

```python
doc = pyquery.PyQuery("<html></html>")

或

url = 'http://www.jianshu.com/'
req = requests.get(url)
page = req.text
pq = pyquery.PyQuery(page)

```

（2）Pyquery 还可以直接调用内置的网络请求模块，对于简单的网页请求：

```python
url = 'http://www.baidu.com'
pq = pyquery.PyQuery(url=url)
```
（3）传文件

```python
doc = pyquery.PyQuery(filename='hello.html')
```

PyQuery 本身还有网页请求功能，而且会把请求下来的网页代码转为 PyQuery 对象。

```python
from pyquery import PyQuery as pq
print(pq('http://cuiqingcai.com/', headers={'user-agent': 'pyquery'}))
print(pq('http://httpbin.org/post', {'foo': 'bar'}, method='post', verify=True))
```

##### 解析

实例1：

```python
pq = pyquery.PyQuery(url="http://www.jianshu.com")
print(pq.html())	

lis = pq('li')	   # 获取所有 li 标签
li_first = lis.eq(0)	# 获取第一个li标签
for li in lis.items():	# 遍历用到 items 方法返回对象列表
    print(li.text())
    
pq_id = pq('#note-11700031')	# 获取id=note-11700031的标签
pq_class = pq('.have-img')		# 获取class=have-img的标签

```

实例2:    

```python
import pyquery

a = """<p class='a b' xixi='123'>haha</p>
<p class='a'>heihei</p>
<div class='a'><p class='c'><span>span</span>ccc</p>aaa</div>
<div class='a b'>xixi</div>"""

pq = pyquery.PyQuery(a)
print(pq("div.a > span").text())	#	div class=a的span 子标签, 没输出
print(pq("div.a span").text())	# 	输出：span
print(pq('div[class="a b"]').text())	# 输出： xixi

```

##### 属性操作

```python
from pyquery import PyQuery as pq

p = pq('<p id="hello" class="hello"></p>')('p')
print(p.attr("id"))		# 获取属性值

# 修改属性值
print(p.attr("id", "plop"))	
print(p.attr("id", "hello"))
```
输出结果：

```html
hello
<p id="plop" class="hello"/>
<p id="hello" class="hello"/>
```

**常用方法**

```python
from pyquery import PyQuery as pq

#1.html()和text() ——获取相应的HTML块或文本块
d = pq("<head><title>hello</title></head>")
d('head').html()    #返回<title>hello</title>
d('head').text()    #返回hello

#2.根据HTML标签获取元素。注意：当获取到的元素不只一个时，html()、text()方法只返回首个元素的相应内容块
d = pq('<div><p>test 1</p><p>test 2</p></div>')
print(d('p'))           #返回<p>test 1</p><p>test 2</p>
print(d('p').html())    #返回test 1

#3.eq(index) ——根据给定的索引号得到指定元素。接上例，若想得到第二个p标签内的内容，则可以：
print(d('p').eq(1).html()) #返回test 2

#4.filter() ——根据类名、id名得到指定元素，例：
d = pq("<div><p id='1'>test 1</p><p class='2'>test 2</p></div>")
d('p').filter('#1') #返回[<p#1>]
d('p').filter('.2') #返回[<p.2>]

#5.find() ——查找嵌套元素，例：
d = pq("<div><p id='1'>test 1</p><p class='2'>test 2</p></div>")
d('div').find('p')#返回[<p#1>, <p.2>]
d('div').find('p').eq(0)#返回[<p#1>]

#6.直接根据类名、id名获取元素，例：
d = pq("<div><p id='1'>test 1</p><p class='2'>test 2</p></div>")
d('#1').html()#返回test 1
d('.2').html()#返回test 2

#7.获取属性值，例：
d = pq("<p id='my_id'><a href='http://hello.com'>hello</a></p>")
d('a').attr('href')#返回http://hello.com
d('p').attr('id')#返回my_id

#8.修改属性值，例：
d('a').attr('href', 'http://baidu.com')把href属性修改为了baidu


#9.addClass(value) ——为元素添加类，例：
d = pq('<div></div>')
d.addClass('my_class')#返回[<div.my_class>]

#10.hasClass(name) #返回判断元素是否包含给定的类，例：
d = pq("<div class='my_class'></div>")
d.hasClass('my_class')#返回True

#11.children(selector=None) ——获取子元素，例：
d = pq("<span><p id='1'>hello</p><p id='2'>world</p></span>")
d.children()#返回[<p#1>, <p#2>]
d.children('#2')#返回[<p#2>]

#12.parents(selector=None)——获取父元素，例：
d = pq("<span><p id='1'>hello</p><p id='2'>world</p></span>")
d('p').parents()            #返回[<span>]
d('#1').parents('span')     #返回[<span>]
d('#1').parents('p')        #返回[]

#13.clone() ——返回一个节点的拷贝

#14.empty() ——移除节点内容

#15.nextAll(selector=None) ——返回后面全部的元素块，例：
d = pq("<p id='1'>hello</p><p id='2'>world</p><img scr='' />")
d('p:first').nextAll()#返回[<p#2>, <img>]
d('p:last').nextAll()#返回[<img>]

#16.not_(selector) ——返回不匹配选择器的元素，例：
d = pq("<p id='1'>test 1</p><p id='2'>test 2</p>")
d('p').not_('#2')#返回[<p#1>]

```

### 4. 实例

##### [Demo 1](https://github.com/JHFighting/python_spider/blob/master/PyQuery/demo_1.py)

获取简书首页文章标题以及对应的链接地址



 [返回顶部](#top)