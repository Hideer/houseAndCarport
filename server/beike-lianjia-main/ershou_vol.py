#!/usr/bin/env python
# coding=utf-8
# author: Zeng YueTian
# 此代码仅供学习与交流，请勿用于商业用途。
# 获得指定城市的二手房成交数据

from lib.spider.ershou_vol_spider import *

if __name__ == "__main__":
    spider = ErShouVolSpider(SPIDER_NAME)
    spider.start()

