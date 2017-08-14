#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2017-08-11 16:47:32
# Project: douban_movie_PhantomJS

from pyspider.libs.base_handler import *


class Handler(BaseHandler):
    crawl_config = {
    }

    def on_start(self):
        self.crawl('http://movie.douban.com/explore#more',
                   fetch_type='js', js_script="""
                   function() {
                       setTimeout("$('.more').click()", 1000);
                   }""", callback=self.index_page)

    @config(age=0)
    def index_page(self, response):
        movie_list = response.doc(".list-wp > .list > a")
        a = []
        for each in movie_list.items():
            name = each("p").text()
            rate = each("strong").text()
            url = each.attr.href
            a.append({
                "name":name,
                "rate":rate,
                "url":url
            })
        return a