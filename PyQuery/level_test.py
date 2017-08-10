#coding=utf-8

from pyquery import PyQuery as pq
import requests
import re

def level1():
    baseUrl = "http://www.heibanke.com/lesson/crawler_ex00/"
    r = requests.get(baseUrl)
    h3 = pq(r.text)("h3")
    try:
        number = re.findall(r"(\d+)", h3.text())[0]
        url = baseUrl
        while number:
            url = baseUrl + str(number)
            r = requests.get(url)
            h3 = pq(r.text)("h3")
            print(h3.text())
            numbers = re.findall(r"(\d+)", h3.text())
            if numbers:
                number = numbers[0]
                print("number: " + str(number))
            else:
                break
        print(url)
    except Exception as e:
        print("error: " + str(e))

def level2():
    url = "http://www.heibanke.com/lesson/crawler_ex01/"
    password = 1
    while True:
        data = {"username": "aaa", "password": password}
        r = requests.post(url, data)
        h3 = pq(r.text)("h3").text()
        if "错误" in h3:
            print("password: " + str(password) + " wrong")
            password += 1
        else:
            print(str(password) + " success")
            break