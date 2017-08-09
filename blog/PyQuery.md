<a href="../README.md" name="top"><<返回目录</a>

# PyQuery

### 1. 简介

如果说到 `jQuery`，熟悉前端的同学肯定不陌生，它可以简单优雅地对 html 文件进行定位、选择、移动等操作。而本文的主角 pyquery，支持以 jquery 的方式对 html 进行操作。因此非常适合有前端或 js 基础的同学使用。

### 2. 安装

```shell
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

##### 属性操作

```python
from pyquery import PyQuery as pq

p = pq('<p id="hello" class="hello"></p>')('p')
print(p.attr("id"))
print(p.attr("id", "plop"))
print(p.attr("id", "hello"))
```
输出结果：

```html
hello
<p id="plop" class="hello"/>
<p id="hello" class="hello"/>
```

### 4. 实例

##### [Demo 1](https://github.com/JHFighting/python_spider/blob/master/PyQuery/demo_1.py)

获取简书首页文章标题以及对应的链接地址



 [返回顶部](#top)