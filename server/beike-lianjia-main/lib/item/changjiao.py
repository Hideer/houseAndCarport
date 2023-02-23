#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian
# 此代码仅供学习与交流，请勿用于商业用途。
# 二手房信息的数据结构

class ChengJiao(object):
    def __init__(self, district, area, name, price, date, unit_price, desc_url, pic, trade_mark, desc_info, desc_position, desc_tax, desc_dist, desc_cycle, desc_original_price):
        self.district = district
        self.area = area
        self.name = name
        self.price = price
        self.date = date
        self.unit_price = unit_price
        self.desc_url = desc_url
        self.pic = pic
        self.trade_mark = trade_mark
        self.desc_info = desc_info
        self.desc_position = desc_position
        self.desc_tax = desc_tax
        self.desc_dist = desc_dist
        self.desc_cycle = desc_cycle
        self.desc_original_price = desc_original_price

    def text(self):
        return self.district + "," + \
                self.area + "," + \
                self.name + "," + \
                self.price + "," + \
                self.date + "," + \
                self.pic + "," + \
                self.desc_url + "," + \
                self.trade_mark + "," + \
                self.unit_price + "," + \
                self.desc_info + "," + \
                self.desc_position + "," + \
                self.desc_tax + "," + \
                self.desc_dist + "," + \
                self.desc_cycle + "," + \
                self.desc_original_price
