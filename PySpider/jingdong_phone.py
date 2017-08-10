#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2017-08-10 09:59:24
# Project: jingdong

from pyspider.libs.base_handler import *


class Handler(BaseHandler):
    crawl_config = {
    }

    @every(minutes=24 * 60)
    def on_start(self):
        self.crawl('http://item.jd.com/1312640.html', callback=self.index_page, fetch_type='js')

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        a = []
        for each in response.doc('li[class^="fore"]').items():
            name = each('div[class="p-name"]').text()
            price = each('div[class="p-price"]').text()
            if name and price:
                a.append({"name": name, "price": price})
        return a