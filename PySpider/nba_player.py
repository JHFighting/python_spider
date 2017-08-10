#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2017-08-10 14:01:42
# Project: sport_list

from pyspider.libs.base_handler import *
import xlwt
from xlrd import open_workbook
from xlutils.copy import copy


class Handler(BaseHandler):

    def __init__(self):
        self.row = 0
        workbook = xlwt.Workbook(encoding='utf-8')
        workbook.add_sheet('team')
        workbook.save("nba_player_test.xls")

    crawl_config = {
    }

    @every(minutes=1)
    def on_start(self):
        self.crawl('http://nba.stats.qq.com/team/list.htm', callback=self.index_page, fetch_type='js')

    def index_page(self, response):
        teams_list = response.doc('div[class="teams-list"]').find('a[href^="http://nba.stats.qq.com/team/?id="]')
        for each in teams_list.items():
            self.crawl(each.attr.href, callback=self.player_page, fetch_type='js')

    def player_page(self, response):

        rb = open_workbook('nba_player_test.xls')
        wb = copy(rb)
        ws = wb.get_sheet(0)

        a = []
        team_name = response.doc("h1").text()
        ws.write(0, self.row, team_name)
        player_list = response.doc('table[class="tbl-fixed"]').find('a[href*="type=player"]')
        temp_tag = 1
        for each in player_list.items():
            name = each.text()
            a.append(name)
            ws.write(temp_tag, self.row, name)
            temp_tag += 1

        self.row += 1
        wb.save('nba_player_test.xls')

        return a